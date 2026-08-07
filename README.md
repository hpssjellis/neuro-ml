---
canonical: https://hpssjellis.github.io/neuro-ml/
meta-description: neuro machine learning
title: neuro-ml | neuro machine learning
---

# neuro-ml

neuro machine learning

Website of this README.md file: https://hpssjellis.github.io/neuro-ml/

# Project Proposal: Student-Designed Closed-Loop Electrophysiology Experiments Using High-Density Microelectrode Arrays

## Executive Summary

This project proposes a structured collaboration between secondary-school students and a neuroscience research laboratory using the MaxWell Biosystems **MaxOne High-Density Microelectrode Array (HD-MEA)** platform. The objective is to enable students to design, implement, and analyze quantitatively defined closed-loop electrophysiology experiments under laboratory supervision.

Students will develop **spatial stimulation geometries** and **real-time reinforcement algorithms** for cultured human induced pluripotent stem cell (iPSC)-derived neural networks. The scientific objective is to determine how spatiotemporal electrical stimulation influences neural plasticity, functional connectivity, and adaptive network behavior.

A key feature of the program is a **three-year research pipeline** that aligns with the biological time required for neural cultures while providing students with meaningful experimental feedback during every academic year.

This proposal builds directly on a validated body of published work rather than starting from first principles. The MaxOne platform and the closed-loop stimulation/reinforcement paradigm described here are the same class of system used by Cortical Labs (Melbourne, Australia) in their peer-reviewed **DishBrain** research program, beginning with Kagan et al., *Neuron* (2022) and continuing through several follow-up studies (see **References** below). Where possible, this program adopts already-validated electrical stimulation parameters rather than re-deriving safe operating limits, so that student-led innovation is concentrated on stimulation geometry, task/reinforcement design, and real-time software architecture — not on unproven tissue-safety questions.

## Relationship to Published Work (DishBrain / Cortical Labs)

The MaxOne HD-MEA and its underlying closed-loop control approach are not novel to this proposal — they are an established research platform. Cortical Labs' original 2022 study cultured human iPSC-derived and rodent cortical neurons on a Maxwell Biosystems HD-MEA of comparable electrode density and demonstrated that a simulated-game closed-loop feedback system produced measurable behavioral adaptation within minutes. Follow-up studies from the same group extended this into direct sample-efficiency comparisons against modern deep reinforcement learning algorithms (DQN, A2C, PPO), and Cortical Labs has since commercialized a related platform (the CL1) with a cloud-deployable API for closed-loop experiments.

This matters for the proposal in three concrete ways:

1. **Stimulation safety parameters are already characterized.** The original protocol used charge-balanced, positive-first biphasic voltage pulses — the standard low-threshold, tissue-protective waveform for this class of array — with unpredictable "punishment" stimulation delivered around 150 mV at 5 Hz for 4 seconds following a missed response, contrasted against predictable, low-entropy stimulation as the reward signal. Independent characterization of comparable high-density arrays supports safe operating envelopes in the range of roughly ±10 mV to ±1 V per pulse phase, phase durations near 200 μs, well below levels associated with tissue or electrode damage. Students should design *geometry and timing logic* on top of this validated envelope rather than exploring untested voltage/current combinations.
2. **The "reward" mechanism is predictability, not a simulated neurotransmitter.** In the DishBrain paradigm, positive and negative reinforcement are operationalized as *predictable vs. unpredictable* stimulation patterns, following the free-energy principle (Friston et al.) rather than a dopamine-style reward signal. This is an important conceptual clarification for the "positive and negative reinforcement" language in this proposal's Experimental Platform section — it reframes "reward field" design as *entropy/predictability field* design, which is both more scientifically precise and easier to defend to an ethics board.
3. **The stimulation/recording control layer is software, not custom hardware.** MaxWell Biosystems' MaxOne system exposes its acquisition and stimulation control through a Python-based API/SDK running on the instrument's control PC. This means the "Software Engineering Team" role in this proposal — real-time closed-loop control, timing validation, metadata logging — is realistically scoped as a Python integration and pipeline-engineering problem sitting on top of vendor-provided hardware control, not a from-scratch embedded systems build. This is a good match for existing WebSerial/WebBLE/embedded-ML pipeline experience already developed for the `webmcu-ai` curriculum, adapted to a Python/desktop context rather than browser/microcontroller.

## Scientific Objective

Determine whether closed-loop electrical reinforcement modifies the electrophysiological behavior of cultured human neural networks recorded on a **26,400-electrode HD-MEA**.

The primary hypothesis is that contingent reinforcement following predefined network responses will produce measurable changes in response probability, spike timing, network connectivity, and stimulus-response performance compared with open-loop stimulation controls.

This hypothesis has already been supported at a foundational level by the original DishBrain result; the novel contribution of this program is not "whether closed-loop reinforcement works" but rather how spatial stimulation geometry, reinforcement schedule design, and multi-region routing affect the *rate, stability, and generalizability* of that learning — territory the published literature has only begun to explore.

## Experimental Platform

The MaxOne HD-MEA enables simultaneous recording and stimulation across a high-density electrode array. A subset of electrodes can be dynamically routed for stimulation and recording, allowing students to design complex **spatial stimulation fields**. Only a small subset of electrodes (order of tens, not hundreds) are typically routed as active stimulation sites in published protocols, with the bulk of the array used for recording — a useful design constraint for students to work within.

Students will investigate stimulation geometries such as:

- Concentric rings
- Radial spokes
- Directional gradients
- Opposing hemispheres
- Rotating stimulation fields
- Moving wavefronts
- Localized predictability/reward fields

The educational objective is to give students ownership of experimental design, while the laboratory objective is to develop a high-throughput platform for systematic exploration of spatiotemporal reinforcement strategies in living neural networks.

## Operational Definition of Learning

Learning will be defined operationally as a change in measurable electrophysiological metrics relative to baseline and control conditions.

**Primary outcome measures**

- Evoked response probability
- Spike latency following stimulation
- Population burst frequency
- Functional connectivity inferred from spike-train correlations
- Information transfer between stimulated and output regions
- Stability of responses across repeated trials

## Reinforcement Protocol

Students will implement programmable reinforcement schedules using charge-balanced biphasic stimulation pulses, adopting parameters already validated in published closed-loop MEA work as a safe starting envelope rather than an open design variable:

- **Pulse shape:** charge-balanced, positive-first biphasic voltage pulses (lowest activation threshold, most tissue-protective, standard practice on this class of array).
- **Typical phase duration:** on the order of 200 μs.
- **Typical amplitude range:** roughly ±10 mV to ±1 V per phase, depending on target region and desired activation probability — well inside ranges independently characterized as safe on comparable high-density arrays.
- **Published negative-feedback example (DishBrain, Kagan et al. 2022):** unpredictable stimulation around 150 mV at 5 Hz for approximately 4 seconds following a "miss."
- **Published positive-feedback logic:** predictable, low-entropy stimulation following a "hit" — reward is defined by predictability, not by a distinct reward waveform.

**Example experimental paradigm**

1. Deliver a spatially defined stimulation pattern.
2. Evaluate network activity within a predefined post-stimulus window (for example, **5–20 ms**).
3. Classify responses using predefined electrophysiological criteria.
4. Deliver contingent reinforcement following successful responses (predictable pattern) or unsuccessful responses (unpredictable pattern), following the validated DishBrain logic above.
5. Compare reinforcement schedules across experimental conditions.

Reinforcement frequencies (for example, **30 Hz versus 2 Hz**) are treated as **experimental variables** rather than assumed biological learning mechanisms and will be evaluated empirically, building on — rather than replacing — the published baseline protocol.

## Three-Year Research Pipeline

### Year 1: Rapid Stimulation Mapping

Students focus on **high-throughput experimental design and rapid iteration** using existing laboratory cultures that have completed their primary research purpose but remain electrophysiologically active.

The experimental cycle is intentionally short:

1. Design a stimulation pattern.
2. Apply a **5–10 minute closed-loop protocol**.
3. Record electrophysiological responses.
4. Analyze the data.
5. Modify the stimulation program.

Because experiments can be completed quickly, students can test multiple variables within a single school term, including spatial geometry, pulse timing, reinforcement contingency, and response thresholds.

The laboratory can schedule **monthly experimental rounds**, allowing students to receive rapid feedback and refine their algorithms throughout the year.

### Year 2: Longitudinal Plasticity Experiments

Students begin experiments on cultures prepared specifically for the educational research program.

Because cultures are available from the beginning of the academic year, students can initiate stimulation immediately and follow the same network over weeks and months.

Research questions include:

- Predictable versus unpredictable reinforcement schedules
- Acquisition of stimulus-response behavior
- Retention of learned responses
- Changes in functional connectivity
- Long-term stability of trained networks

This phase generates the first **longitudinal plasticity datasets**.

### Year 3: Next-Generation Experimental Design

Students analyze the combined dataset from previous cohorts and design more sophisticated experiments.

Research directions may include:

- Competing stimulation pathways
- Spatial reward-field optimization
- Adaptive reinforcement algorithms
- Multi-region input/output routing
- Transfer of learned responses between network regions
- Automated optimization of stimulation geometries

The emphasis shifts from parameter exploration to **hypothesis-driven experimental design**.

## Continuity Note

This program spans a multi-year biological and educational timeline that may extend past a single teacher's classroom tenure. To remain resilient to staff transitions (including planned retirement from full-time teaching), the program should be structured so that: (1) the software/data pipeline and experimental protocols are documented and version-controlled independently of any one individual, (2) the laboratory partner (family research contact) holds continuity of the biological/instrument side across cohorts, and (3) a designated in-school robotics/computing teacher of record is identified for each academic year, with the original proposer available in an advisory/consulting capacity post-retirement (e.g., via periodic TOC coverage or remote review of student software).

## Student Research Roles

### Experimental Design Team

- Design spatial stimulation geometries
- Define input and output regions
- Specify reinforcement contingencies
- Develop experimental controls

### Computational Analysis Team

- Process spike trains
- Detect evoked responses
- Compute connectivity metrics
- Perform statistical analyses

### Software Engineering Team

- Implement real-time closed-loop control (likely a Python layer on top of the MaxWell Biosystems control API/SDK)
- Integrate recording and stimulation pipelines
- Validate timing precision
- Log experimental metadata

### Laboratory Team (Research Supervision)

- Cell culture and differentiation
- Sterile handling
- Electrode preparation
- Hardware operation
- Experimental oversight

## Experimental Controls

A scientifically valid comparison requires parallel control conditions.

### Open-Loop Control

Identical stimulation delivered without contingent reinforcement.

### Random Reinforcement Control

Reinforcement delivered with identical frequency but independent of network output.

### Sham Reinforcement Control

Detection algorithms executed without delivery of reinforcement pulses.

These controls distinguish reinforcement-dependent plasticity from spontaneous network drift and stimulation-induced adaptation, and mirror control conditions used in the published DishBrain literature (e.g., feedback-without-sensory-input and sensory-input-without-feedback conditions, which showed no learning).

## Data Analysis

**Primary analysis**

- Within-network comparison before versus after reinforcement
- Between-group comparison across reinforcement conditions

**Statistical methods**

- Mixed-effects models for repeated measurements
- Permutation tests for connectivity changes
- Survival analysis of response persistence
- False-discovery-rate correction for multiple comparisons

## Ethics and Laboratory Oversight

All cell culture, stem-cell differentiation, and electrophysiology experiments will be conducted under the supervision of the host research laboratory and in accordance with institutional biosafety and ethics approvals.

Students will participate in approved activities including experimental design, software development, stimulation-program development, quantitative data analysis, and scientific interpretation. Biological materials will remain under laboratory control at all times. Given that the original DishBrain publication explicitly raised and debated the term "sentience" in relation to cultured neural networks, this proposal should present its framing (predictability/entropy-based reinforcement, not anthropomorphized "reward") clearly and early to any school board, ethics board, or parent-facing materials, to avoid unnecessary controversy grounded in a misunderstanding of the underlying mechanism.

## Expected Deliverables

- A validated closed-loop stimulation software framework (Python, built on the MaxWell control API)
- A library of spatial stimulation geometries
- Standardized reinforcement protocols, grounded in published safe parameter ranges
- An anonymized electrophysiology dataset
- A statistical comparison of reinforcement and control conditions
- Student-authored scientific posters, reports, and manuscript contributions

This program creates a sustainable research pipeline in which each student cohort contributes to the next generation of bio-hybrid electrophysiology experiments, while maintaining rigorous experimental design, quantitative analysis, ethical oversight, and continuity across multiple years of investigation.

## maxOne Time Series
![media/maxone-time-series.png](media/maxone-time-series.png)

## maxOne live array view
![media/sensor-array.png](media/sensor-array.png)

## MaxOne sample data tray
![media/maxone-tray.png](media/maxone-tray.png)

## Old Sensor 12-64x64-neuro-electrodes-front.png
![media/12-64x64-neuro-electrodes-front.png](media/12-64x64-neuro-electrodes-front.png)

## Old Sensor 12-64x64-neuro-electrodes-back.png
![media/****](media/12-64x64-neuro-electrodes-back.png)

<br><br><br><br><br>
<hr>

# Gemini Generated images of the possible view from the MaxOne live array interface

1. Blue stimulating electrode not active (For the present running program and for this screen shot)
2. Green stimulating electrode that are active (possibly with a repeating frequency of stimulation)
3. Grid shows grouped areas of neurons for planned positive- and negative-reinforcement studies (see note above: "positive/negative" here means predictable vs. unpredictable stimulation, per the DishBrain free-energy-principle framing, not a literal reward chemical)
4. Red dots active sensed neuron firing at that time

Note: All time frames are recorded for student analysis after the fact.

## possibly-view01.jpg
![/media/possibly-view01.jpg](/media/possibly-view01.jpg)

Generated using Gemini, possibly reproducible using this prompt and the maxOne live array [media/sensor-array.png](media/sensor-array.png) as an input.

Prompt: and insert above image [media/sensor-array.png](media/sensor-array.png) as attached input.

A detailed photograph of a large, modern computer monitor displaying the "MaxLab Live" high-content electrophysiology software interface, based on the layout seen in image_0.png. The screen shows the central sensor grid canvas with the original background of scattered, natural magenta neural activity clusters. Overlaid centrally on the grid is a precise, large circular arrangement of exactly 32 crisp blue stimulation points. Within this circle, four specific, non-adjacent blue points are distinctly colored vibrant green, indicating active stimulation. A prominent 4x3 grid of thin, solid black lines is overlaid across the entire sensor area, creating 12 distinct rectangular analysis zones. The fourth quadrant (bottom-right) of this grid is intensely highlighted, containing a significantly denser cluster of bright red neural activity dots, signifying a specific region of trained, heightened activation in response to the stimulation. All original surrounding software UI elements, toolbars, the Ubuntu launcher on the left, and the text "Flow for high-throughput, high-content electrophysiology" in the upper-left corner are preserved and sharp. The monitor is positioned in a modern lab setting, with blurred out-of-focus lab equipment in the background. The perspective is a three-quarter view of the screen.

That generated the following image:

## possibly-view02.jpg
![/media/possibly-view02.jpg](/media/possibly-view02.jpg)

<br><br>
<hr>

## References

**Primary published research (DishBrain / Cortical Labs)**

- Kagan, B.J. et al. (2022). *In vitro neurons learn and exhibit sentience when embodied in a simulated game-world.* Neuron. Open access, CC BY 4.0. https://www.cell.com/neuron/fulltext/S0896-6273(22)00806-6
- Khajehnejad, M., Habibollahi, F., Loeffler, A., Paul, A., Razi, A., Kagan, B.J. (2024). *Biological Neurons Compete with Deep Reinforcement Learning in Sample Efficiency in a Simulated Gameworld.* arXiv:2405.16946. https://arxiv.org/pdf/2405.16946
- Khajehnejad, M. et al. (2025). *Dynamic Network Plasticity and Sample Efficiency in Biological Neural Cultures: A Comparative Study with Deep Reinforcement Learning.* Cyborg and Bionic Systems. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12320521/
- Cortical Labs Research page (full list of published papers, including the CL API real-time closed-loop paper): https://corticallabs.com/research

**Coverage and context**

- UCL News: "Human brain cells in a dish learn to play Pong" — https://www.ucl.ac.uk/news/2022/oct/human-brain-cells-dish-learn-play-pong
- Monash University: "Brain cells in a dish learn to play Pong" — https://www.monash.edu/medicine/news/latest/2022-articles/brain-cells-in-a-dish-learn-to-play-pong
- Nature News & Views: "Neurons in a dish learn to play Pong — what's next?" — https://www.nature.com/articles/d41586-022-03229-y
- ScienceDaily: "Human brain cells in a dish learn to play Pong in real time" — https://www.sciencedaily.com/releases/2022/10/221012132528.htm

**Video**

- Cortical Labs official YouTube channel (DishBrain demos, CL1 launch, neurons playing Doom with source on GitHub): https://www.youtube.com/channel/UCq4mqLeGRdq47sHumYMIDJw
- "Brain in a Dish Plays Pong: Cortical Labs' CL1 Biocomputer" (lab walkthrough, Melbourne): https://www.youtube.com/watch?v=W-NGW_VHYOw
- "Cortical Labs' CL1 Just Made Traditional Computers Obsolete" (CL1 launch coverage): https://www.youtube.com/watch?v=6wUrgu0pvI4

**Hardware / platform**

- MaxWell Biosystems (manufacturer of the MaxOne HD-MEA used in this proposal and in DishBrain): https://www.mxwbio.com
- Cortical Labs CL1 / Cortical Cloud (commercial platform built on the same closed-loop stimulation paradigm, Python-deployable): https://corticallabs.com/cl1

*This site is open source. [Improve this page](https://github.com/hpssjellis/neuro-ml/edit/main/README.md).*
