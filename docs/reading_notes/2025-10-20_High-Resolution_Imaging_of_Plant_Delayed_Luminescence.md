### Paper: "High-Resolution Imaging of Plant Delayed Luminescence" (Liu et al., 2025)
**Link** [Link text](https://arxiv.org/abs/2501.01173?utm_source=chatgpt.com)


#### Summary
-  A quantitative scientific complementary metal-oxide-semiconductor (qCMOS) camera was used to study delayed luminescence in 3 different species of plants under different treatments.
#### Key Points
- They were able to demonstrate that quantum effects in plants and the structure/architecture or their tissues have a quantitative connection that can potentially be used to evaluate stress (mechanical stim., Ox. stress, light quality) in plants in a manner that bypasses the need and complexity in taking in consideration all molecular components.
- Different species of plants may have divergent methods for managing ROS and different anatomical adaptations that will alter the manner in which the kinetics of delayed luminescence will be expressed in different situatations.

### Notes on Materials and methods
- Plants used:
    - _Hydrocotyle vulgaris_, _Arabidopsis thaliana_, _Ginkgo biloba_
        - Each of these plants has distinct phenotypes that could alter how DL are expressed.
- Plants were either grown from seed (_Arabidopsis_), or seems like already as anestablished plant.
- It will be important to measure light intensity (umol*m**-2*s**-1), establish a photoperiod (12 hours?), and a consistent watering schedule.
- qCMOS camera (Hammamtsu ORCA-Quest)
    - This type of camera requires cooling (-40C)     
    
- "After imaging, all raw data underwent the following standardized processing steps:
(1) Background correction: Pre-acquired dark fields (i.e., 3 × 30s exposures) were used to establish
a noise baseline that was then subtracted from other raw images.
(2) Spatial denoising: A six-frame sequence (i.e., 0–180 s decay, 30 s per exposure) underwent 3 ×
3 pixels median filtering, while retaining the median intensity values within the central pixel
neighborhood.
5
(3) Signal normalization: Leaf region masks extracted valid pixels, with the photon flux calculated
in photons/pixel/30s.
(4) Spatiotemporal analysis: Time-aligned frames were used to generate pixel-wise decay curves and
were then used to quantify DL intensity gradients and decay rates. Time-aligned frames were
processed to extract DL kinetic profiles through the following steps:
a. Leaf region photon flux calculation:
For each exposure frame (30-s interval), the total photon count P(t) within the leaf mask was summed
and normalized by the valid pixel area Apixel and exposure time:
𝐼(𝑡) =
𝑃(𝑡)
𝐴𝑝𝑖𝑥𝑒𝑙×𝑁2 [photons/pixel/30s], where t= 30, 60, 90, 120, 150, and 180 s, respectively.
b. Temporal decay curve generation:
DL intensity values at the six time points {I(0), I(30), ... , I(180)} were plotted as a function of time.
c. Key parameter quantification:
Initial intensity: I(0)=I(t=30), Residual intensity: Ires
=I(180), Normalized residual: Res% =
I(180)
I(0)
× 100."
    - Will need explanation of these and maybe I will be using.
- They used both leaves and whole plant for the initial baseline reading.
- Plant leaves were flattened in **petri dish** lined with moist filter paper and secured along petioles and margins using sterile double-sided tape.
- 3% H2O2 for Ox. stress treatment
    - 2 min. incubate then irradiate 5 min.
    - 30 min post H2O2 time point
- For Light wavelength excitation experiment
    - white, red (660 nm), blue (460 nm) LEDs, 50 umol*m**-2*s**-1)
- Irradiated specimens with different lights after Ox. and mechanical treatments.
- 30, 60, 90, 120, 150, 180 second image captures

#### Thoughts / Applications
- Interesting that UPE detection could be used to evaluate the state of an organism.
- This study is overall similar to the study I will be running.
- Plant choice matters and will be interesting to evaluate different plants.

#### Questions / Follow-ups
- Need to further understand calculations for imaging and if they apply to my study.