# Stage 1 - Initial architecture

**Version:** 1.0  
**Date:** September 1, 2026  
**Basis:** AlphaBot2-Pi + AlphaBot2-Base datasheets (Waveshare) + hardware testing results

## 1. Platform

| Parameter | Value |
|----------|----------|
| **Chassis** | AlphaBot2-Pi (Waveshare), 2 decks |
| **Compute** | Raspberry Pi 5, 2 GB RAM |
| **Storage** | SanDisk Extreme Pro A2 256 GB MicroSD |
| **OS** | Ubuntu 24.04 Server (64-bit) |
| **ROS 2** | Jazzy (ros-base) |
| **DDS** | CycloneDDS (Domain 42) |
| **I2C** | Enabled (`dtparam=i2c_arm=on`) |
| **GPIO libraries** | gpiozero (primary), smbus2 (I²C), spidev (SPI) |

---

## 2. Boards

| Board | Location | Chips | Functions |
|-------|:------------:|------|---------|
| **AlphaBot2-Base** | Bottom | TB6612FNG, LM393, ST188 ×3, ITR20001/T ×5, WS2812B ×4 | Motors, sensors, LEDs |
| **AlphaBot2-Pi** | Top | PCA9685, TLC1543, CP2102, LM2596 | Servo controller, ADC, UART, regulator, joystick, IR receiver, buzzer |
| **FC-20P cable** | Between boards | — | AlphaBot2-Base ↔ AlphaBot2-Pi connection |

---

# Foto 

---

