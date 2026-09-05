## Decision: GPIO Library Selection for AlphaBot2-Pi

**Date:** 2026-09-05  
**Project:** Lab4Ros — AlphaBot2-Pi (alpha-01)  
**Status:** Approved

---

## 1. Context

| Parameter | Value |
|-----------|-------|
| Platform | Raspberry Pi 5 (2 GB RAM) |
| OS | Ubuntu 24.04 Server (arm64) |
| ROS 2 | Jazzy Jalisco |
| Components | 23 (GPIO, I²C, SPI) |
| Sensor frequency | 10–25 Hz |
| Tasks | Sensor reading, motor control, ROS 2 publishing |

---

## 2. Candidate Comparison

| Criteria | gpiozero | lgpio | RPi.GPIO |
|----------|:--------:|:-----:|:--------:|
| RPi 5 support | ✅ | ✅ | ❌ |
| API simplicity | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| Built-in HC-SR04 | ✅ `DistanceSensor` | ❌ | ❌ |
| Built-in LED/Button | ✅ | ❌ | ❌ |
| Debounce | ✅ | ❌ | ❌ |
| Maintenance status | ✅ Active | ✅ Active | ❌ Deprecated (2019) |
| Development speed | High | Low | Medium |
| For 23 components | ✅ Ideal | ⚠️ Verbose | ❌ Broken |

---

## 3. Decision

**Primary GPIO library: `gpiozero`**

### Rationale

1. **Raspberry Pi 5 support.** RPi.GPIO has not been updated since 2019 and is unstable on BCM2712. gpiozero is actively maintained and works on RPi 5.

2. **Built-in DistanceSensor for HC-SR04.** The `DistanceSensor(echo=27, trigger=6)` class provides one-line setup instead of 20+ lines of manual timing.

3. **Simple API for digital sensors.** `DigitalInputDevice(17).value` reads a line sensor in a single line.

4. **Development speed.** 23 components require rapid prototyping. gpiozero reduces code volume 2–3× compared to lgpio.

5. **Built-in features.** Pull-ups, debounce, and edge detection are included — no manual implementation needed.

---

## 4. Additional Libraries

| Task | Library | Reason |
|------|---------|--------|
| I²C (PCA9685) | `smbus2` | Standard for I²C |
| SPI (TLC1543) | `spidev` | Standard for SPI |
| WS2812B | `rpi_ws281x` | Specialized for NeoPixel |
| Fallback (low-level) | `lgpio` | When fine-grained control is needed |

---

## 5. Installation

```bash
sudo apt install -y \
    python3-gpiozero \
    python3-smbus \
    python3-spidev \
    python3-lgpio

pip3 install rpi-ws281x --break-system-packages
```

---

# Information Sheet: gpiozero

## What is gpiozero

**gpiozero** is a high-level Python library for GPIO control on Raspberry Pi. Created by the Raspberry Pi Foundation. It provides simple classes for common devices: LEDs, buttons, distance sensors, motors, and servo drives.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Digital input/output** | GPIO pin reading and writing |
| **DistanceSensor** | HC-SR04 out of the box |
| **LED / PWMLED** | LEDs, buzzers |
| **Button / DigitalInputDevice** | Buttons, sensors |
| **Servo** | Servo drives |
| **Motor** | DC motors |
| **Debounce** | Contact bounce elimination |
| **Edge detection** | Signal edge handling |

---

## Key Classes for AlphaBot2-Pi

| Class | Purpose | Example |
|-------|---------|---------|
| `DigitalInputDevice` | Line sensors, obstacle sensors, IR | `DigitalInputDevice(17).value` |
| `DistanceSensor` | HC-SR04 | `DistanceSensor(echo=27, trigger=6).distance` |
| `LED` | Buzzer (as LED) | `LED(12).on()` |
| `PWMLED` | PWM control | `PWMLED(18).value = 0.5` |

---

## Usage Example

```python
from gpiozero import DigitalInputDevice, DistanceSensor, LED

# Line sensor
line_sensor = DigitalInputDevice(17)
print(line_sensor.value)  # 1 = black line, 0 = white surface

# HC-SR04
range_sensor = DistanceSensor(echo=27, trigger=6)
print(f"{range_sensor.distance * 100:.1f} cm")

# Buzzer
buzzer = LED(12)
buzzer.on()
```

---

## Limitations

| Limitation | Impact |
|------------|--------|
| Not for real-time | Sufficient for 10–25 Hz |
| Abstraction | Hides low-level details |
| Depends on lgpio | Uses lgpio internally — required as well |

---

## References

- Official documentation: https://gpiozero.readthedocs.io/
- GitHub: https://github.com/gpiozero/gpiozero
- Raspberry Pi documentation: https://www.raspberrypi.com/documentation/computers/os.html

---

