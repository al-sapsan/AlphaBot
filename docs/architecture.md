# AlphaBot2-Pi Architecture

## Platform

| Component | Value |
|-----------|-------|
| Chassis | AlphaBot2-Pi (Waveshare) |
| Computer | Raspberry Pi 5 2GB |
| OS | Ubuntu 24.04 Server |
| ROS 2 | Jazzy Jalisco |
| DDS | CycloneDDS (Domain 42) |

## Components

| Component | Interface |
|-----------|-----------|
| PCA9685 | I²C (0x40) |
| TLC1543 | SPI |
| ITR20001/T ×5 | GPIO |
| ST188 ×3 | GPIO |
| HC-SR04 | GPIO (TRIG=6, ECHO=27) |
| WS2812B ×2 | GPIO (18) |
| Buzzer | GPIO (12) |
| IR receiver | GPIO (13) |
