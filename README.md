# Project AlphaBot2-Pi (alpha-01)

**Version:** 2.1  
**Date:** September 3, 2026  
**Basis:** AlphaBot2-Pi + AlphaBot2-Base (Waveshare)  


**⚖️ License:** MIT | ⚙️ **ROS2:** Jazzy | 🍓 **Platform:** Raspberry Pi 5

---
> 👉 <span style="color:deepskyblue; font-size: 20px">Links:</span>
> The history of changes and improvements in the project see [here](https://www.waveshare.com/wiki/AlphaBot2-Pi#AlphaBot2-Base)

## 1. Platform

| Parameter | Value |
|-----------|-------|
| **Chassis** | AlphaBot2-Pi (Waveshare), 2-tier |
| **Computing Unit** | Raspberry Pi 5, 2 GB RAM |
| **Storage** | SanDisk Extreme Pro A2 256 GB MicroSD |
| **OS** | Ubuntu 24.04 Server (64-bit) |
| **ROS 2** | Jazzy (ros-base) |
| **DDS** | CycloneDDS (Domain 42) |
| **I2C** | Enabled (`dtparam=i2c_arm=on`) |

### 🚀 Features

- Motor control via PCA9685 → TB6612FNG
- Reading 5 line sensors (following the line)
- Read 3 obstacle sensors
- HC-SR04 Ultrasonic range finder
- RGB LEDs WS2812B
- Buzzer, IR receiver, joystick
- Publishing data in ROS 2 topics

---

## 2. Boards

| Board | Location | Chips | Functions |
|-------|:--------:|:-----:|-----------|
| **AlphaBot2-Base** | Lower tier | TB6612FNG, LM393, ST188 ×3, ITR20001/T ×5, WS2812B ×2 | Motors, sensors, LEDs, battery compartment |
| **AlphaBot2-Pi** | Upper tier | PCA9685, TLC1543, CP2102, LM2596 | PWM controller, ADC, UART, voltage regulator, servo connector, joystick, IR receiver, buzzer |
| **FC-20P cable** | Between boards | — | Connection AlphaBot2-Base ↔ AlphaBot2-Pi |

> 👉 <span style="color:deepskyblue; font-size: 20px">Links:</span>

> Details for **AlphaBot2-Base** see [here](https://www.waveshare.com/wiki/AlphaBot2-Pi#AlphaBot2-Base)
> 
> Details for **AlphaBot2-Pi** see [here](https://www.waveshare.com/wiki/AlphaBot2-Pi#AlphaBot2-Pi)
>
> Details for **Hardware Assembly and Testing** see [here](https://github.com/al-sapsan/AlphaBot/blob/main/docs/boards-assembly.md)

---

## 3. Microcontrollers and Sensors

### Main (on boards)

| Component | Purpose | Interface | Board |
|-----------|---------|-----------|:-----:|
| **PCA9685** | 16-channel PWM controller — motors and servos | I2C (0x40) | AlphaBot2-Pi |
| **TLC1543** | 10-bit ADC for analog sensors | SPI | AlphaBot2-Pi |
| **TB6612FNG** | Dual N20 motor driver | PCA9685 → TB6612 | AlphaBot2-Base |
| **LM393** | Dual comparator — digitizing IR sensor signals | Analog → GPIO | AlphaBot2-Base |

### Sensors

| Component | Purpose | Interface | Board |
|-----------|---------|-----------|:-----:|
| **ITR20001/T** ×5 | IR line-tracking sensors (surface reflection) | GPIO (via LM393) | AlphaBot2-Base (bottom) |
| **ST188** ×3 | IR obstacle sensors | GPIO (via LM393) | AlphaBot2-Base |
| **HC-SR04** | Ultrasonic distance sensor (2–400 cm) | GPIO (Trig + Echo) | Connector on AlphaBot2-Base |
| **Potentiometer** | Adjusting sensitivity threshold for obstacle sensors | Hardware | AlphaBot2-Base |

### External (separate boards, planned)

| Component | Purpose | Interface |
|-----------|---------|-----------|
| **STM32F401CCU6** | Encoders, micro-ROS | Serial USB |
| **Raspberry Pi Pico W** | Additional sensors | Serial USB |

---

## 4. Actuators

| Device | Model | Specifications | Control | Board |
|--------|-------|----------------|---------|:-----:|
| N20 Motors ×2 | N20 Micro Gear Motor | 6V, 600 RPM, 1:30 gear ratio | PCA9685 → TB6612FNG | AlphaBot2-Base |
| Servo | MG90 | Positional, 180° rotation | PCA9685 | Connector on AlphaBot2-Pi |
| Servo Interface | Servo connector | Pan-Tilt + extra servo | PCA9685 | AlphaBot2-Pi |
| Wheels | Rubber | Diameter 42 mm, width 19 mm | Mechanical | AlphaBot2-Base |
| Omni-wheel | Caster wheel | Front, swivel | Mechanical | AlphaBot2-Base |

---

## 5. Input and Control

| Device | Purpose | Interface | Board |
|--------|---------|-----------|:-----:|
| **Joystick** | Manual robot control | GPIO / ADC (TLC1543) | AlphaBot2-Pi |
| **IR Receiver** | Receiving commands from IR remote | GPIO | AlphaBot2-Pi |
| **CP2102** | USB-UART bridge for debugging | USB | AlphaBot2-Pi |
| USB TO UART | Controlling Pi via UART | UART | AlphaBot2-Pi |

---

## 6. Indication

| Component | Purpose | Control | Board |
|-----------|---------|---------|:-----:|
| **WS2812B** ×2 | Addressable RGB LEDs | GPIO (bit-bang) | AlphaBot2-Base |
| **Buzzer** | Passive buzzer — audio alerts | GPIO | AlphaBot2-Pi |
| Obstacle Avoiding Indicators | Light up when an obstacle is detected | Hardware (LM393) | AlphaBot2-Base |
| Power Indicator | Power status LED | Hardware | AlphaBot2-Base |

---

## 7. Power Supply

| Component | Power Source | Voltage | Current |
|-----------|:----------------:|:----------:|:---:|
| **RPi 5** | Li-Po 3S → UBEC | 5V | up to 5A |
| **N20 motors ×2** | 14500 ×2 → LM2596 | 5V | up to 3A |
| **Sensors** | 14500 ×2 → LM2596 | 5V | < 0.5A |
| **PCA9685** | 14500 ×2 → LM2596 | 5V | < 0.3A |

> 📌 <span style="color:red; font-size: 20px">Note:</span>
> [see here in details](https://github.com/al-sapsan/AlphaBot/blob/main/docs/power-supply.md)

---

## 8. Communication Interfaces

| Interface | Devices | Protocol |
|-----------|---------|----------|
| **I2C** | PCA9685 (0x40) | I2C |
| **SPI** | TLC1543 | SPI |
| **GPIO** | ITR20001/T ×5, ST188 ×3, HC-SR04, WS2812B ×2, Joystick, IR Receiver, Buzzer | GPIO |
| **USB-UART** | CP2102 | UART |
| **FC-20P Cable** | Connection AlphaBot2-Base ↔ AlphaBot2-Pi | GPIO |
| **40-pin GPIO** | RPi 5 ↔ AlphaBot2-Pi | — |
| **Serial USB** | STM32F401, Pico W (planned) | USB |

---

## 9. ROS 2: Planned Nodes and Topics

| Node | Publishing | Subscribing | Message Type |
|------|:----------:|:-----------:|--------------|
| `motor_driver` | `/alpha_bot/odometry` | `/cmd_vel` | `geometry_msgs/Twist` |
| `line_sensors` | `/alpha_bot/line_sensors` | — | `std_msgs/Int32MultiArray` |
| `range_sensor` | `/alpha_bot/range` | — | `sensor_msgs/Range` |
| `obstacle_sensors` | `/alpha_bot/obstacles` | — | `std_msgs/Int32MultiArray` |
| `led_controller` | — | `/alpha_bot/leds` | `std_msgs/ColorRGBA` |
| `buzzer` | — | `/alpha_bot/buzzer` | `std_msgs/Bool` |
| `joystick` | `/alpha_bot/joystick` | — | `sensor_msgs/Joy` |
| `ir_receiver` | `/alpha_bot/ir_command` | — | `std_msgs/Int32` |

---

## 10. Full List of Components

| # | Component | Type | Interface | Board | Status |
|:--:|:-----------|:------:|:---------:|:-----:|:------:|
| 1 | PCA9685 | PWM Controller | I2C (0x40) | Pi | ⬚ |
| 2 | TLC1543 | ADC | SPI | Pi | ⬚ |
| 3 | TB6612FNG | Motor Driver | PCA9685 | Base | ⬚ |
| 4 | LM393 | Comparator | Analog | Base | ⬚ |
| 5 | ITR20001/T ×5 | Line Sensors | GPIO | Base | ⬚ |
| 6 | ST188 ×3 | Obstacle Sensors | GPIO | Base | ⬚ |
| 7 | HC-SR04 | Ultrasonic Rangefinder | GPIO | Base | ⬚ |
| 8 | WS2812B ×2 | RGB LEDs | GPIO | Base | ⬚ |
| 9 | Potentiometer | Obstacle Threshold | Hardware | Base | ⬚ |
| 10 | N20 ×2 | Motors | TB6612FNG | Base | ⬚ |
| 11 | Omni-wheel | Wheel | Mechanical | Base | ✅ |
| 12 | Servo Interface | Servo Connector | PCA9685 | Pi | ⬚ |
| 13 | Joystick | Manual Control | GPIO/ADC | Pi | ⬚ |
| 14 | IR Receiver | IR Receiver | GPIO | Pi | ⬚ |
| 15 | Buzzer | Buzzer | GPIO | Pi | ⬚ |
| 16 | CP2102 | USB-UART | USB | Pi | ⬚ |
| 17 | LM2596 | 5V Regulator | Power | Pi | ✅ |
| 18 | Power Switch | Power Switch | — | Base | ✅ |
| 19 | Battery Holder 14500 ×2 | Battery Compartment | — | Base | ✅ |
| 20 | STM32F401CCU6 | Encoders, micro-ROS | Serial USB | External | ⬚ |
| 21 | Pico W | Sensors | Serial USB | External | ⬚ |
| 22 | Obstacle Indicators | Obstacle LEDs | Hardware | Base | ✅ |
| 23 | Power Indicator | Power LED | Hardware | Base | ✅ |
