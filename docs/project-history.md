# Stage 1 - Initial architecture

**Version:** 1.0  
**Date:** September 1, 2026  

## 1. Platform

| Parameter | Value |
|----------|----------|
| **Chassis** | AlphaBot2-Pi (Waveshare), 2 decks |
| **Compute** | Raspberry Pi 5, 2 GB RAM 📌|
| **Storage** | SanDisk Extreme Pro A2 256 GB MicroSD |
| **OS** | Ubuntu 24.04 Server (64-bit) |
| **ROS 2** | Jazzy (ros-base) |
| **DDS** | CycloneDDS (Domain 42) |
| **I2C** | Enabled (`dtparam=i2c_arm=on`) |
| **GPIO libraries** | gpiozero (primary), smbus2 (I²C), spidev (SPI) |

> 📌 **Note:**
> according to the technical specifications, the AlphaBot2‑Pi can originally be equipped with Raspberry Pi 3B/3B+/4B single‑board computers [see here](https://www.waveshare.com/product/raspberry-pi/robots/mobile-robots/alphabot2-pi-acce-pack.htm). However, in 2026, with the Raspberry Pi 5 already in production, purchasing an older model is not very practical. Therefore, the decision was made to use the Raspberry Pi 5 with 2 GB of RAM, and the consequences of this choice will be described further below.

---

## 2. Boards

| Board | Location | Chips | Functions |
|-------|:------------:|------|---------|
| **AlphaBot2-Base** 👇| Bottom | TB6612FNG, LM393, ST188 ×3, ITR20001/T ×5, WS2812B ×4 | Motors, sensors, LEDs |
| **AlphaBot2-Pi** 👇| Top | PCA9685, TLC1543, CP2102, LM2596 | Servo controller, ADC, UART, regulator, joystick, IR receiver, buzzer |
| **FC-20P cable** | Between boards | — | AlphaBot2-Base ↔ AlphaBot2-Pi connection |

> 👉 **Links:** 
> details for **Waveshare's AlphaBot2-Base** and **Waveshare's AlphaBot2-Pi** see [here](https://www.waveshare.com/wiki/AlphaBot2-Pi#AlphaBot2-Base) and
 [here](https://www.waveshare.com/wiki/AlphaBot2-Pi#AlphaBot2-Pi)

---
<img src="https://github.com/al-sapsan/AlphaBot/raw/main/docs/figures/2026-09-10%2020-31-00.jpeg" alt="Initial platform1" style="width: 75%; height: auto;">

<img src="https://github.com/al-sapsan/AlphaBot/raw/main/docs/figures/2026-09-10%2020-31-42.jpeg" alt="Initial platform2" style="width: 75%; height: auto;">

### **Figure 1, 2.** Waveshare's initial platform architecture

---

# Stage 2 - Raspberry Pie Gone Wrong

**Version:** 2.0  
**Date:** September 10, 2026  




