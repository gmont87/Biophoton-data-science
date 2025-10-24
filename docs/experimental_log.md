# 🌿 Biophoton Experiment Log
*This file and timeline were generated with guidance from ChatGPT.*
Welcome to your experimental record!  
Use this document to log daily progress, configuration changes, and observations during your biophoton research.  
Each entry includes environmental conditions, setup details, and early data analysis notes.

---

## 🧭 Table of Contents
- [2025-10-23 — Initial Setup Planning](#2025-10-23--initial-setup-planning)
- [2025-10-24 — Materials & Light Isolation Tests](#2025-10-24--materials--light-isolation-tests)
- [2025-10-25 — Sensor Calibration](#2025-10-25--sensor-calibration)
- [2025-10-26 — Dark Box Integration Test](#2025-10-26--dark-box-integration-test)
- [2025-11-01 — First Data Capture Session](#2025-11-01--first-data-capture-session)
- [2025-11-02 — Data Review & Python Analysis](#2025-11-02--data-review--python-analysis)

---

### 2025-10-23 — Initial Setup Planning

**Objective:**  
Define experimental goals, finalize sensor selection, and sketch physical setup.

**Tasks:**  
- [ ] Review materials list (camera, photodiode, LED reference light, etc.)  
- [ ] Design experimental layout sketch  
- [ ] Decide control vs. test sample conditions  
- [ ] Plan Python data pipeline (input → processing → visualization)

**Notes:**  
## The Budget Biophoton Experiment Setup

This setup uses a combination of a used integrated PMT module and a general-purpose, used frequency counter.

---

### 🧩 Components & Estimated Cost

| **Component** | **Description** | **Estimated Cost (Used/Surplus)** | **Source** |
|----------------|-----------------|-----------------------------------|-------------|
| **Photomultiplier Tube (PMT) Module** | Hamamatsu H10721-01 or H6357-11 integrated module (includes PMT, HV supply, and preamp). | $150 – $250 | eBay |
| **Frequency Counter** | A used, standalone frequency counter (e.g., HP 5314A, B&K 1805) to read the pulses. | $50 – $100 | eBay, used test equipment retailers |
| **Power Supply** | A stable, low-voltage DC power supply (e.g., +12V or +15V, 1A) for the PMT module. | $10 – $20 | Amazon, surplus stores |
| **Cables & Connectors** | BNC cable to connect the PMT module output to the frequency counter input. | $10 | Electronics stores |
| **Dark Box / Enclosure** | A light-tight metal or thick plastic box to house the sample and PMT. | $0 – $10 | DIY (e.g., a sealed coffee tin, project box) |

**Total Estimated Cost:** $220 – $390  

---

### 🔍 Explanation of Components

**PMT Module:**  
The integrated Hamamatsu modules (H10721-01 or H6357-11) are key to minimizing setup complexity.  
They provide a ready-to-use output signal (TTL-level pulses) directly from a BNC connector, so you do not have to handle high voltage or design complex preamplifier circuits yourself.

**Frequency Counter:**  
A dedicated, used frequency counter is more reliable and faster than an Arduino for single-photon counting.  
It has a high-speed input (MHz range) capable of accurately counting the rapid pulses produced by the PMT.

**Power Supply:**  
The PMT module needs a standard low-voltage DC supply, which is inexpensive and safe to use.

**Dark Box:**  
Biophoton emission is extremely weak. Any ambient light will completely saturate the PMT.  
The enclosure must be completely sealed from light.

---

### ⚙️ Setup Instructions

**1. Safety First:**  
Although the high voltage is contained within the integrated PMT module, treat all equipment with care.  
Ensure all connections are secure before applying power.

**2. Mount the PMT and Sample in the Dark Box:**  
- Securely mount the PMT module inside the light-tight enclosure.  
- Design a holder for your biophoton sample (e.g., germinating seeds or fruit pulp) so it is close to the PMT’s photocathode window but not touching it.  
- Ensure the box lid creates an absolute light seal. You may need foam weather stripping or black tape.  

**3. Connect the Power:**  
Connect the low-voltage DC power supply to the PMT module’s power input (check the datasheet for correct voltage and polarity, usually +12V or +15V).

**4. Connect the Counter:**  
Use a BNC cable to connect the PMT module’s signal output to the input channel of the frequency counter.

---

### ▶️ Operation

1. Close the dark box completely.  
2. Turn on the PMT power supply.  
3. Turn on the frequency counter and set it to a suitable gate time (e.g., 1 second).  
4. Record the **dark count rate** with no sample inside the sealed box. This is your baseline noise level.  
5. Place your sample inside the sealed box and measure the new count rate.  
6. The difference between the sample count rate and the dark count rate is your **biophoton signal**.  

---



---

### 2025-10-24 — Materials & Light Isolation Tests

**Objective:**  
Ensure dark chamber provides complete light isolation.

**Tasks:**  
- [ ] Assemble cardboard/wood box prototype  
- [ ] Add blackout fabric or foil seams  
- [ ] Test internal darkness using long-exposure photo  
- [ ] Document setup with photo (store image in `/docs/images/`)

**Observations:**  
_(Example: Residual light leak from corner seam; adding foam gasket tomorrow.)_

---

### 2025-10-25 — Sensor Calibration

**Objective:**  
Calibrate sensitivity using a known light source.

**Tasks:**  
- [ ] Use LED at known distance/intensity  
- [ ] Record sensor output for 10s  
- [ ] Create calibration curve in Python  
- [ ] Store code snippet link

**Code Reference:**  
[`code_snippets/2025-10-25_sensor_calibration.py`](../code_snippets/2025-10-25_sensor_calibration.py)

**Results:**  
| LED Intensity | Sensor Value | Notes |
|----------------|---------------|--------|
| Low | 0.02 | minimal detection |
| Medium | 0.15 | steady response |
| High | 0.92 | near saturation |

---

### 2025-11-01 — First Data Capture Session

**Objective:**  
Record spontaneous photon emission from plant tissue in dark chamber.

**Tasks:**  
- [ ] Capture 10-minute dark response  
- [ ] Repeat for control (non-living sample)  
- [ ] Export raw data as `.csv`  
- [ ] Visualize using pandas + matplotlib  

**Code Reference:**  
[`code_snippets/2025-11-01_photon_analysis.py`](../code_snippets/2025-11-01_photon_analysis.py)

---

### 2025-11-02 — Data Review & Python Analysis

**Objective:**  
Compare photon emission time series and create plots.

**Tasks:**  
- [ ] Plot emission intensity vs. time  
- [ ] Perform smoothing using rolling average  
- [ ] Identify emission spikes and correlations  
- [ ] Summarize findings in notes  

**Visualization Example:**  
(Insert matplotlib graph once results are available.)

**Insights:**  
_(Example: Plant sample showed exponential decay curve consistent with delayed luminescence models.)_

---

## 🧩 How to Use This Log

1. Create a new dated section every session (### YYYY-MM-DD — Title).  
2. Link any Python scripts or CSVs.  
3. Keep a clear separation between *objective*, *tasks*, *results*, and *insights*.  
4. Commit to GitHub after each major update — this becomes your experimental record.

---

## 🔗 Related Files
- [Learning Log](./python_learning_log.md)
- [Reading Notes](./reading_notes/)
- [Code Snippets](../code_snippets/)
- [Images Folder](./images/)
