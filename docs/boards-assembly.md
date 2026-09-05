## AlphaBot2-Pi Hardware Assembly and Testing

### Initial State (Snapshot v5.2)

| Component | Status |
|-----------|:------:|
| RPi 5 2GB + cooling | ✅ Installed on AlphaBot2-Pi |
| Ubuntu 24.04 Server | ✅ Configured |
| ROS 2 Jazzy | ✅ Installed |
| GPIO extender | ✅ Arrived |
| Alpha-Base + Alpha-Pi boards | ✅ Ready (to be connected) |
| PCA9685 | On Alpha-Pi board |

---

## Stage 1: Preparation

### 1.1 Verify Physical State

```bash
# On alpha-01:
ssh rosdev@192.168.0.50

# Verify RPi 5 is running:
hostname
# alpha-01

# Check temperature:
temp
# Should be < 60°C at idle
```

### 1.2 Install Dependencies for Testing

```bash
# Update packages:
sudo apt update

# Install GPIO and I²C utilities:
sudo apt install -y i2c-tools gpiod python3-smbus python3-rpi.gpio
```

---

## Stage 2: GPIO Extender Installation

### 2.1 Requirements

- 40-pin GPIO extender
- Careful handling — contacts are fragile

### 2.2 Installation

```
1. Power off RPi 5: sudo poweroff
2. Disconnect power
3. Install GPIO extender on the 40-pin RPi 5 header
4. Mount Alpha-Pi board (top board) on the extender
5. Connect Alpha-Pi to Alpha-Base (via 20-pin XH1 connector)
6. Connect power (USB-C or via LM2596)
```

---

## Stage 3: I²C Verification (PCA9685)

```bash
# Power on RPi 5
ssh rosdev@192.168.0.50

# Verify I²C detects PCA9685:
sudo i2cdetect -y 1
```

**Expected result:**

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
```

**`0x40` — PCA9685 detected!**

If empty — check:
- Boards properly connected
- Alpha-Pi power supply
- GPIO extender contact

---

## Stage 4: GPIO Verification

```bash
# Verify all pins are visible:
gpioinfo | head -50
```

**Verify specific pins:**

```bash
# Line sensors (should be input):
gpioinfo | grep -E "GPIO(17|27|22|23|24)"

# Obstacle sensors (input):
gpioinfo | grep -E "GPIO(16|20|21)"

# HC-SR04:
gpioinfo | grep -E "GPIO(6|27)"

# LED, Buzzer, IR (output/input):
gpioinfo | grep -E "GPIO(18|12|13)"
```

---

## Stage 5: PCA9685 Test (Motors)

### 5.1 Verify PCA9685 via Python

```bash
# PWM test:
python3 << 'EOF'
from smbus2 import SMBus
import time

bus = SMBus(1)
addr = 0x40

# Initialize PCA9685
bus.write_byte_data(addr, 0x00, 0x00)
prescale = int(25000000 / (4096 * 50) - 1)  # 50 Hz
bus.write_byte_data(addr, 0x00, 0x10)  # Sleep
bus.write_byte_data(addr, 0xFE, prescale)
bus.write_byte_data(addr, 0x00, 0x80)  # Restart
bus.write_byte_data(addr, 0x00, 0x20)  # Auto-increment

print("PCA9685 initialized at 0x40")

# Test channel 0 (left motor PWM)
for duty in [0, 1024, 2048, 3072, 4095, 2048, 0]:
    bus.write_word_data(addr, 0x06, duty)
    time.sleep(0.5)

print("PCA9685 test complete")
EOF
```

### 5.2 Verify Motors

If motors are connected to Alpha-Base:

```bash
# Apply PWM to motor channels:
python3 << 'EOF'
from smbus2 import SMBus
import time

bus = SMBus(1)
addr = 0x40

# Channels: 0=PWMA, 1=AIN1, 2=AIN2, 3=PWMB, 4=BIN1, 5=BIN2
# (verify according to Alpha-Pi schematic)

# Test left motor forward (50% speed):
bus.write_word_data(addr, 0x06, 2048)  # PWMA
time.sleep(2)
bus.write_word_data(addr, 0x06, 0)     # Stop

print("Motor test complete")
EOF
```

---

## Stage 6: Line Sensors Test (ITR20001/T)

```bash
python3 << 'EOF'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pins = [17, 27, 22, 23, 24]

for pin in pins:
    GPIO.setup(pin, GPIO.IN)

print("Line sensors:")
for pin in pins:
    value = GPIO.input(pin)
    print(f"  GPIO {pin}: {'BLACK (line)' if value else 'WHITE'}")

GPIO.cleanup()
EOF
```

**Verification:** Move a finger/black line over the sensors — values should change.

---

## Stage 7: HC-SR04 Test

```bash
python3 << 'EOF'
import RPi.GPIO as GPIO
import time

TRIG = 6
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.000002)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if time.time() - pulse_start > 0.1:
            return -1
    
    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end - pulse_start > 0.1:
            return -1
    
    distance = (pulse_end - pulse_start) * 34300 / 2
    return distance

print("HC-SR04 test (5 measurements):")
for i in range(5):
    dist = get_distance()
    print(f"  {i+1}: {dist:.1f} cm")
    time.sleep(0.5)

GPIO.cleanup()
EOF
```

**Verification:** Place a hand in front of the sensor — distance should change.

---

## Stage 8: ST188 Obstacle Sensors Test

```bash
python3 << 'EOF'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21]

for pin in pins:
    GPIO.setup(pin, GPIO.IN)

print("Obstacle sensors:")
for pin in pins:
    value = GPIO.input(pin)
    print(f"  GPIO {pin}: {'OBSTACLE' if value else 'CLEAR'}")

GPIO.cleanup()
EOF
```

---

## Stage 9: WS2812B LED Test

```bash
# Install library:
sudo pip3 install rpi-ws281x --break-system-packages

# Test:
python3 << 'EOF'
from rpi_ws281x import PixelStrip, Color
import time

LED_PIN = 18
LED_COUNT = 4  # 4 WS2812B on Alpha-Base

strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

print("LED test (red, green, blue):")
for color in [Color(255,0,0), Color(0,255,0), Color(0,0,255)]:
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(1)

# Turn off
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0,0,0))
strip.show()
print("LED test complete")
EOF
```

---

## Stage 10: Buzzer and IR Test

```bash
python3 << 'EOF'
import RPi.GPIO as GPIO
import time

BUZZER = 12
IR = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(IR, GPIO.IN)

print("Buzzer test (3 beeps):")
for i in range(3):
    GPIO.output(BUZZER, True)
    time.sleep(0.1)
    GPIO.output(BUZZER, False)
    time.sleep(0.1)

print("IR receiver:")
value = GPIO.input(IR)
print(f"  IR: {'SIGNAL' if value else 'NO SIGNAL'}")

GPIO.cleanup()
EOF
```

---

## Hardware Verification Checklist

| Test | Command | Expected Result |
|------|---------|:---------------:|
| PCA9685 | `i2cdetect -y 1` | 0x40 detected |
| GPIO | `gpioinfo` | All pins visible |
| Motors | Python PWM test | Wheels rotate |
| Line sensors | Python test | Values change |
| HC-SR04 | Python test | Distance in cm |
| ST188 | Python test | Obstacle/clear |
| WS2812B | Python test | LEDs light up |
| Buzzer | Python test | Sound |
| IR | Python test | Signal |

---

