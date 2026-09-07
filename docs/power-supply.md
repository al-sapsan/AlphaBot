# AlphaBot2-Pi — Power Specification and Soldering Guide

**Version:** 1.0  
**Date:** 2026-09-07  
**Project:** Lab4Ros — AlphaBot2-Pi (alpha-01)  
**Status:** Approved

---
## 1. Overview

Separate power supply for the wheeled platform and the compute unit (RPi 5) to ensure reliable operation and extended autonomous runtime.

---

## 2. Power Scheme

```
Source 1: Li-ion 14500 ×2 (7.4V)
    ↓
AlphaBot2-Base (bottom board)
    ↓
LM2596 (onboard regulator)
    ↓
N20 motors ×2, sensors, PCA9685

Source 2: Li-Po 3S 2300mAh 80C (11.1V)
    ↓
ZTW UBEC 8A G2 (11.1V → 5V, 8A)
    ↓
USB-C cable
    ↓
Raspberry Pi 5
```

---

## 3. Component Specifications

### 3.1 Li-Po Battery for RPi 5

| Parameter | Value |
|----------|:--------:|
| Type | Li-Po (lithium-polymer) |
| Configuration | 3S (3 cells in series) |
| Nominal voltage | 11.1V |
| Full voltage | 12.6V |
| Minimum voltage | 9.0V (do not discharge below) |
| Capacity | 2300 mAh |
| Discharge rate | 80C (peak 184A) |
| Connector | **XT60 male** (plug) |
| Weight | 167 g |
| Dimensions | 106 × 34 × 22 mm |
| Energy | 25.5 Wh |

### 3.2 UBEC

| Parameter | Value |
|----------|:--------:|
| Model | ZTW UBEC 8A G2 |
| Input voltage | 7–34V (2–8S) |
| Output voltage | 5.0V (selectable: 5.0/6.0/7.4/8.4V) |
| Output current (continuous) | 8A |
| Output current (peak) | 15A |
| Weight | 14 g |
| Input | Wires (solder XT60 female) |
| Output | Wires (solder USB-C cable) |

### 3.3 Stock Battery for Motors

| Parameter | Value |
|----------|:--------:|
| Type | Li-ion 14500 ×2 |
| Voltage | 7.4V (2S) |
| Location | Stock AlphaBot2-Base compartment |
| Regulation | LM2596 on AlphaBot2-Pi |
| Consumers | N20 motors, sensors, PCA9685 |

---

## 4. Runtime Calculation

### 4.1 RPi 5 (from Li-Po 3S via UBEC)

| Load | Power | Current from Li-Po | Runtime |
|----------|:--------:|:------------:|:------------:|
| Idle | 3W | 0.27A | 8.5 hours |
| ROS 2 active | 6W | 0.54A | 4.2 hours |
| Peak load | 12W | 1.08A | 2.1 hours |

### 4.2 Motors (from 14500 ×2 via LM2596)

| Load | Runtime |
|----------|:------------:|
| Average driving | 30–60 minutes |
| Active maneuvering | 20–30 minutes |

---

## 5. Lab4Ros Connector Standard

| Device | Connector |
|------------|:------:|
| AlphaBot2-Pi (Li-Po 3S) | **XT60** |
| Hawk (Li-Po 4S) | **XT60** |
| Charger | Multi-connector (XT60 available) |
| UBEC input | XT60 female (solder) |
| UBEC output | USB-C (solder) |

---

## 6. Soldering Instructions

### 6.1 Required Materials

| Material | Quantity |
|----------|:------:|
| XT60 female (socket) | 1 pc |
| USB-C cable (to cut) | 1 pc |
| Heat shrink tubing (various diameters) | set |
| AWG 16-18 wire (if extension needed) | 20-30 cm |
| Soldering iron (40-60W) | 1 pc |
| Solder (with flux) | — |
| Multimeter | 1 pc |

### 6.2 Preparation

```
1. Tin the XT60 female contacts
2. Tin the UBEC input wires (red +, black -)
3. Tin the USB-C cable wires (red +5V, black GND)
4. Set UBEC to 5V (selector switch)
```

### 6.3 Soldering XT60 Female to UBEC Input

| XT60 female | UBEC input |
|:-----------:|:---------:|
| **Red** (+) | Red (+) |
| **Black** (-) | Black (-) |

**Process:**

1. Slide heat shrink onto wires before soldering
2. Solder red wire to red XT60 contact
3. Solder black wire to black XT60 contact
4. Slide heat shrink over solder joints
5. Heat shrink (hot air gun or lighter)

**Verification:**

```bash
# Multimeter in continuity mode:
# XT60 red ↔ UBEC red: short circuit (0 Ohm)
# XT60 black ↔ UBEC black: short circuit
# XT60 red ↔ XT60 black: open (infinity)
```

### 6.4 Soldering USB-C Cable to UBEC Output

| USB-C cable | UBEC output |
|:------------:|:----------:|
| **Red** (+5V) | Red (+) |
| **Black** (GND) | Black (-) |
| White/green (data) | **Not used** |

**Process:**

1. Cut the USB-C cable
2. Strip outer insulation (5-7 cm)
3. Find red and black wires (usually AWG 22-24)
4. Insulate data wires (white, green) — do not connect
5. Slide heat shrink on
6. Solder red → red, black → black
7. Insulate with heat shrink

**Verification:**

```bash
# Multimeter in continuity mode:
# USB-C pin 1 (VBUS) ↔ UBEC red: short circuit
# USB-C GND pin ↔ UBEC black: short circuit
# VBUS ↔ GND: open
```

### 6.5 Final Assembly Verification

```bash
1. Connect Li-Po 3S (XT60 male) to XT60 female
2. Multimeter in DC Voltage mode (20V)
3. Measure on USB-C:
   - VBUS (pin 1) and GND: should be 5.0V ±0.2V
4. If > 5.5V — DO NOT CONNECT to RPi 5!
5. If 5.0V ±0.2V — safe to connect
```

---

## 7. Safety Rules

| Rule | Description |
|---------|----------|
| **Always disconnect Li-Po** | When soldering or modifying the circuit |
| **Never short XT60** | Short-circuit currents — tens of amps, fire hazard |
| **Check polarity** | Before applying power |
| **Insulate all connections** | Heat shrink or electrical tape |
| **Do not discharge Li-Po below 9V** | Cell damage |
| **Store in fireproof bag** | Li-Po is fire-hazardous |
| **Charge only with Li-Po charger** | Not any power supply |

---

## 8. Pre-Power-On Checklist

- [ ] XT60 female soldered to UBEC input (correct polarity)
- [ ] USB-C soldered to UBEC output (correct polarity)
- [ ] Heat shrink applied to all connections
- [ ] UBEC selector switch set to 5V
- [ ] Multimeter reads 5.0V ±0.2V on USB-C
- [ ] Li-Po charged (11.1–12.6V)
- [ ] Stock 14500 batteries installed in Alpha-Base compartment
- [ ] RPi 5 connected via USB-C from UBEC
- [ ] Motors connected to Alpha-Base

---

## 9. Final Configuration

| Component | Power Source | Voltage | Current |
|-----------|:----------------:|:----------:|:---:|
| **RPi 5** | Li-Po 3S → UBEC | 5V | up to 5A |
| **N20 motors ×2** | 14500 ×2 → LM2596 | 5V | up to 3A |
| **Sensors** | 14500 ×2 → LM2596 | 5V | < 0.5A |
| **PCA9685** | 14500 ×2 → LM2596 | 5V | < 0.3A |
```
