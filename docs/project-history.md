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
<img src="https://github.com/al-sapsan/AlphaBot/raw/main/docs/figures/Initial_boards1.jpeg" alt="Initial platform1" style="width: 75%; height: auto;">

<img src="https://github.com/al-sapsan/AlphaBot/blob/main/docs/figures/Initial_boards2.jpeg" alt="Initial platform2" style="width: 75%; height: auto;">

### **Figure 1, 2.** Waveshare's initial platform architecture

---

# Stage 2 - Raspberry Pie Gone Wrong

**Version:** 2.0  
**Date:** September 10, 2026  

According to the Raspberry Pi 5 docs, running it without cooling is a no‑go—so we got a case with two fans (check out Photo 3).

---

<img src="https://github.com/al-sapsan/AlphaBot/blob/main/docs/figures/RasberryPi5.jpeg" alt="Initial platform2" style="width: 55%; height: auto;">

### **Figure 3.** Raspberry Pi 5 in its case.

---

But of course, no good deed goes unpunished 😅. Here’s the catch: the case is just a bit too thick. Because of that, the GPIO pins on the Pi couldn’t line up with the AlphaBot2‑Pi board’s connectors—the case kept bumping into the board’s components and blocking the connection.

---

<img src="https://github.com/al-sapsan/AlphaBot/blob/main/docs/figures/Cannot_connectGPIO.png" alt="Cannot connect GPIO" style="width: 75%; height: auto;">

### **Figure 4.** GPIO alignment problem
> The Raspberry Pi 5 case is too thick to let the pins connect cleanly to the AlphaBot2‑Pi board.
> As you can see, the case frame presses against the nearby components on the AlphaBot board, so the GPIO pins can’t fully seat into their sockets. That’s why we can’t get a proper connection. 🔌❌

---

I fixed the problem with a straightforward solution: a GPIO pin extender. But, of course, the universe decided to test my patience — this little piece of polymer and metal had to travel all the way from China, and I spent 20 days waiting for it to arrive. 😅

---

<img src="https://github.com/al-sapsan/AlphaBot/blob/main/docs/figures/Can_connectGPIO.png" alt="Can connect GPIO" style="width: 75%; height: auto;">

### **Figure 5.** The fix: a GPIO extender solves the alignment problem
>The little piece of polymer and metal did the trick: now the Raspberry Pi 5 connects cleanly to the AlphaBot2‑Pi board, and there’s still enough clearance for proper airflow and cooling. ✅

---





