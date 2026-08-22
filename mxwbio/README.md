# MaxOne WetML Sandbox (v1)

An open-source, browser-native HD-MEA (High-Density Microelectrode Array) protocol hypothesis generator and experimental design sandbox. Designed for exploring closed-loop neural stimulation, baseline observation, and Hebbian-style training rules without hardware barriers.

👉 **Try this live version:** [https://hpssjellis.github.io/neuro-ml/mxwbio/maxone-sim.html](https://hpssjellis.github.io/neuro-ml/mxwbio/maxone-sim.html)  
📺 **Watch the engineering playlist:** [NeuralML Playlist](https://www.youtube.com/playlist?list=PLEGHz6jvYW9s)

---

## Maxwell Biosystems References
* Maxwell Biosystems: [mxwbio.com](https://www.mxwbio.com/)
* MaxLab Live: [mxwbio.com/products/maxlab-live](https://www.mxwbio.com/products/maxlab-live)
* MaxLab Biocomputing: [mxwbio.com/applications/biocomputing](https://www.mxwbio.com/applications/biocomputing)
* MaxLab API Docs: [api-docs.mxwbio.com](https://api-docs.mxwbio.com/section_api/api.html#doc-section-api)

---

## Testing & Version Index
* **Claude-assisted builds:** [maxone-sim-v##.html](https://hpssjellis.github.io/neuro-ml/mxwbio/maxone-sim-v##.html) *(where number increases as things improve)*
* **Stable Production Build:** [maxone-sim.html](https://hpssjellis.github.io/neuro-ml/mxwbio/maxone-sim.html) *Same as above live demo

---

## Video Series & Architecture Walkthrough

Each video below covers a specific subsystem in this version of the sandbox.

### 1. Baseline Observation & Spontaneous Activity
* **Video:** [Watch Part 1](https://www.youtube.com/playlist?list=PLEGHz6jvYW9s)
* **What it shows:** The raw, chaotic baseline spontaneous firing of a cultured neural network on a MaxOne array before any deliberate stimulation protocol is applied.
* **The Technical Challenge:** Real cultured networks run on their own clock (0.1 to 5 Hz per electrode). Training cannot override this background noise; it has to work *around* or *with* it.

### 2. Time-Multiplexing the 32-Electrode Hardware Limit
* **Video:** [Watch Part 2](https://www.youtube.com/playlist?list=PLEGHz6jvYW9s)
* **What it shows:** How larger stimulus zones are electrode-swapped ("time-multiplexed") across the MaxOne chip's fixed 32-electrode stimulation budget.
* **The Technical Challenge:** Because biological tissue responds on a millisecond timescale, swap dwell times and pulse phase widths dictate whether the tissue registers a coherent signal or just high-frequency noise.

### 3. Closed-Loop Training & Hebbian Weight Updates
* **Video:** [Watch Part 3](https://www.youtube.com/playlist?list=PLEGHz6jvYW9s)
* **What it shows:** Transitioning from Phase 1 (Baseline) to Phase 2 (Protocol Design), applying a basic error-correction rule where stimulation patterns nudge influence weights toward a target truth table.
* **The Open Question:** How do we account for homeostatic scaling in a real biological wet-lab, where the network naturally re-tunes itself to ignore persistent training stimuli over time?

---

## Core Features in Version 1
* **Hardware Mapping:** Modeled after a virtualized subset of a MaxOne chip featuring 32 programmable stimulation sites and a subsampled active view of 1,000 active sensor nodes out of 26,400 physical electrodes.
* **Three.js Volumetric Visualization:** Renders a 3D interface with color-coded nodes (resting, stimulation pulses, inhibition, output sensing events).
* **Clock Scaling & Dynamic Grids:** Supports variable time-scaling between training epochs and fast inference testing, starting from a 2x2 grid up to 4x4 multi-zone topologies.
* **Zero-Install / Vanilla Stack:** Built entirely in a single HTML file using vanilla JavaScript, async/await structures, static function bindings, and inline CSS.

---

## Roadmap for Subsequent Versions
* **Version 2:** Integrate TensorFlow.js backpropagation routines to adapt simulated neuronal network weights dynamically as new training streams arrive, mapping spatial distance rules and precise frequency/amplitude variables.
* **Version 3:** Introduce the dual-layer "sandwich" topology (top stimulation layer and bottom sensing layer with a simulated 3D organoid volume between them) to test directional Z-axis vector fields and zero-latency closed-loop feedback loops.

---

## Peer Review & Questions
If you are working with edge computing, microcontrollers, or neural interfaces, review the logic in `maxone-sim.html` and let me know your take on:
* At 5 Hz background noise, is this kind of localized training pathway physically sustainable, or does the network inevitably re-tune itself to ignore the stim?
