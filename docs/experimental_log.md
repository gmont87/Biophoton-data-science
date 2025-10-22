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
_(Example: Decided to use basil and marigold for initial trials due to strong luminescence response in literature.)_

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
