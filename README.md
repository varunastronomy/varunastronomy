<div align="center">
  <img src="assets/varun-cosmic-command-center.png" width="100%" alt="Cosmic research command centre representing scientific software and mission-data analysis">

  # M. Varun | Space Data → Research Software → Discovery

  **Computational Astrophysicist · Scientific Python Developer · PhD Research Scholar**  
  **CHRIST (Deemed to be University), Bengaluru, India**

  [![Software](https://img.shields.io/badge/Research_Software-19_Public_Projects-37C7FF?style=for-the-badge)](#-research-software-command-deck)
  [![Research](https://img.shields.io/badge/Peer--Reviewed_Research-4_Papers-AF7CFF?style=for-the-badge)](#-peer-reviewed-science)
  [![GitHub](https://img.shields.io/badge/GitHub-varunastronomy-111827?style=for-the-badge&logo=github)](https://github.com/varunastronomy)
</div>

## Mission profile

I build reproducible software that carries X-ray observations from mission products to defensible scientific measurements. My work spans neutron-star binaries, thermonuclear bursts, burst oscillations, QPO searches, spectral modelling, variability, polarimetry, archive automation, and publication-ready analysis.

```text
MISSION DATA → CALIBRATION → TIMING + SPECTRA → INFERENCE → PEER-REVIEWED SCIENCE
     🛰️             ⚙️              📈               🧠                🌌
```

<div align="center">
  <img src="assets/research-workflow.gif" width="100%" alt="Synthetic workflow from space data through analysis and interpretation">
  <br><sub><b>Synthetic portfolio visualisation:</b> conceptual workflow, not observational data.</sub>
</div>

## Technical flight deck

<p align="center">
  <img src="https://img.shields.io/badge/Python-Scientific_Computing-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Linux-Research_Automation-FCC624?style=flat-square&logo=linux&logoColor=black">
  <img src="https://img.shields.io/badge/HEASoft-Mission_Analysis-143D59?style=flat-square">
  <img src="https://img.shields.io/badge/XSPEC-Spectral_Inference-702963?style=flat-square">
  <img src="https://img.shields.io/badge/Stingray-X--ray_Timing-00A6A6?style=flat-square">
  <img src="https://img.shields.io/badge/Astropy-FITS_%26_Time-FF7A00?style=flat-square&logo=astropy&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub_Actions-Validation-2088FF?style=flat-square&logo=githubactions&logoColor=white">
</p>

**Mission experience:** NICER · NuSTAR · AstroSat · RXTE · Insight-HXMT · XPoSat · IXPE<br>
**Methods:** event processing · GTIs · HIDs · power spectra · FFT/\(Z^2\) searches · PyXspec · MCMC · uncertainty propagation

## Research-software command deck

### Mission processing and products

| Project | Capability |
|---|---|
| [Varun's Custom NICER Pipeline](https://github.com/varunastronomy/varun-custom-nicer-pipeline) | Fault-isolated observation reduction and product orchestration |
| [Spectral Product Generation](https://github.com/varunastronomy/spectral-product-generation) | Concurrent spectra, backgrounds, responses, and grouping |
| [PhotonForge](https://github.com/varunastronomy/photonforge-xray-light-curves) | GTI-aware source, background, and net light curves |
| [NuSTAR Archive Downloader](https://github.com/varunastronomy/nustar-public-archive-downloader) | Public-catalogue queries and concurrent AWS acquisition |
| [HXMT Processing Orchestrator](https://github.com/varunastronomy/custom-hxmt-processing-orchestrator) | Transparent research-stage HE/ME/LE orchestration template |

### Timing and transient signals

| Project | Capability |
|---|---|
| [BurstScope](https://github.com/varunastronomy/burstscope-xray-characterisation) | Burst morphology, timing landmarks, and GTIs |
| [Burst Oscillation Search](https://github.com/varunastronomy/burst-oscillation-search) | Trial-aware FFT and \(Z^2_1\) candidate search |
| [mHz QPO Search](https://github.com/varunastronomy/mhz-qpo-search) | Energy-resolved Lomb–Scargle exploration |
| [kHz QPO Search](https://github.com/varunastronomy/khz-qpo-search) | Multi-observation high-frequency search |
| [RMS Spectrum Analyzer](https://github.com/varunastronomy/rms-spectrum-analyzer) | GTI-aware PDS and energy-resolved fractional RMS |
| [X-ray Dip Classifier](https://github.com/varunastronomy/xray-dip-classifier) | Interactive dipping-event annotation |

### Spectroscopy and inference

| Project | Capability |
|---|---|
| [XSpecFit](https://github.com/varunastronomy/xspecfit-spectral-fitting) | PyXspec fitting, confidence reporting, and review |
| [FluxTrace](https://github.com/varunastronomy/fluxtrace-xray-flux-analysis) | Total, intrinsic, bolometric, and component fluxes |
| [PyXspec MCMC Explorer](https://github.com/varunastronomy/pyxspec-mcmc-explorer) | Goodman–Weare chains and posterior visualisation |
| [Accretion Rate Calculator](https://github.com/varunastronomy/accretion-rate-calculator) | Uncertainty-aware accretion diagnostics |
| [Spectral Radius Calculator](https://github.com/varunastronomy/spectral-radius-calculator) | Model-dependent disk and blackbody radii |

### State evolution and visualisation

| Project | Capability |
|---|---|
| [Hardness Intensity Generator](https://github.com/varunastronomy/hardness-intensity-generator) | Background-subtracted HIDs and FITS tables |
| [HID Parameter Animator](https://github.com/varunastronomy/hid-parameter-animator) | Time-ordered HID and parameter animations |
| [Parameter Trend Explorer](https://github.com/varunastronomy/xray-parameter-trend-explorer) | Interactive all-pairs trend screening |

> Each project documents assumptions, dependencies, permission terms, and validation boundaries. Syntax success is not presented as scientific validation.

## Live repository index

Automatically refreshed daily and available on demand.

<!-- REPOSITORY_INDEX_START -->
- [accretion-rate-calculator](https://github.com/varunastronomy/accretion-rate-calculator) — Independent X-ray astronomy research software by M. Varun.
- [burst-oscillation-search](https://github.com/varunastronomy/burst-oscillation-search) — Search X-ray burst event data for trial-corrected FFT and Z-squared oscillation candidates.
- [burstscope-xray-characterisation](https://github.com/varunastronomy/burstscope-xray-characterisation) — Interactive Python workflow for measuring timing landmarks and generating GTIs from thermonuclear X-ray burst light curves.
- [custom-hxmt-processing-orchestrator](https://github.com/varunastronomy/custom-hxmt-processing-orchestrator) — Independent X-ray astronomy research software by M. Varun.
- [fluxtrace-xray-flux-analysis](https://github.com/varunastronomy/fluxtrace-xray-flux-analysis) — Measure model-dependent X-ray fluxes and uncertainties across observation sets with PyXspec.
- [hardness-intensity-generator](https://github.com/varunastronomy/hardness-intensity-generator) — Generate background-subtracted X-ray hardness-intensity diagrams and reusable FITS products.
- [hid-parameter-animator](https://github.com/varunastronomy/hid-parameter-animator) — Independent X-ray astronomy research software by M. Varun.
- [khz-qpo-search](https://github.com/varunastronomy/khz-qpo-search) — Independent X-ray astronomy research software by M. Varun.
- [mhz-qpo-search](https://github.com/varunastronomy/mhz-qpo-search) — Independent X-ray astronomy research software by M. Varun.
- [nustar-public-archive-downloader](https://github.com/varunastronomy/nustar-public-archive-downloader) — Independent X-ray astronomy research software by M. Varun.
- [photonforge-xray-light-curves](https://github.com/varunastronomy/photonforge-xray-light-curves) — PhotonForge: concurrent, GTI-aware X-ray light-curve generation and background subtraction
- [pyxspec-mcmc-explorer](https://github.com/varunastronomy/pyxspec-mcmc-explorer) — Independent X-ray astronomy research software by M. Varun.
- [rms-spectrum-analyzer](https://github.com/varunastronomy/rms-spectrum-analyzer) — Measure GTI-aware, energy-resolved X-ray fractional RMS with Stingray.
- [spectral-product-generation](https://github.com/varunastronomy/spectral-product-generation) — Concurrent, GTI-aware generation and organization of X-ray spectra, responses, backgrounds, and analysis products.
- [spectral-radius-calculator](https://github.com/varunastronomy/spectral-radius-calculator) — Independent X-ray astronomy research software by M. Varun.
- [varun-custom-nicer-pipeline](https://github.com/varunastronomy/varun-custom-nicer-pipeline) — M. Varun's independent, fault-tolerant Python pipeline for NICER data reduction and Level-3 product orchestration.
- [xray-dip-classifier](https://github.com/varunastronomy/xray-dip-classifier) — Independent X-ray astronomy research software by M. Varun.
- [xray-parameter-trend-explorer](https://github.com/varunastronomy/xray-parameter-trend-explorer) — Independent X-ray astronomy research software by M. Varun.
- [xspecfit-spectral-fitting](https://github.com/varunastronomy/xspecfit-spectral-fitting) — Automate multi-observation X-ray spectral fitting, uncertainty reporting, and review with PyXspec.
<!-- REPOSITORY_INDEX_END -->

## Peer-reviewed science

### First-author research

- **Discovery of a 459 Hz Burst Oscillation in XTE J1810−189 with NICER** — *The Astrophysical Journal* 995, 153 (2025). [DOI](https://doi.org/10.3847/1538-4357/ae21d3)
- **Spectral and Type I X-ray Burst Studies of M15 X-2 Using NICER Observations** — *Journal of High Energy Astrophysics* 49, 100461 (2026). [DOI](https://doi.org/10.1016/j.jheap.2025.100461)
- **Spectral and Type I X-ray Burst Studies of 4U 1702−429 Using AstroSat Observations** — *MNRAS* 529, 2234–2241 (2024). [DOI](https://doi.org/10.1093/mnras/stae636)

### Co-authored research

- **First Polarimetric View of GX 349+2 with IXPE** — *The Astrophysical Journal* 985, 229 (2025). [DOI](https://doi.org/10.3847/1538-4357/add330)

## What I bring to a mission team

- End-to-end ownership from event products to traceable scientific outputs
- Research-grade Python and Linux automation across mission archives
- Signal processing, spectral inference, uncertainty propagation, and statistical caution
- Failure-aware pipelines, checkpoints, structured reports, and reproducible figures
- Peer-reviewed experience turning complex observations into defensible results

## Professional direction

Open to research-software engineering, scientific data science, mission-data operations, space-sector R&D, and Python development roles where careful computation supports real discovery.

<div align="center">

### `observe → question → build → validate → discover`

[![Explore repositories](https://img.shields.io/badge/Explore-varunastronomy-37C7FF?style=for-the-badge&logo=github&logoColor=white)](https://github.com/varunastronomy?tab=repositories)

<sub>Only professional identity, institutional affiliation, publications, and public GitHub work are presented. No personal contact information is published.</sub>
</div>
