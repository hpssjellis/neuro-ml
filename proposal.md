# Project Proposal: Student-Designed Closed-Loop Neuroplasticity Experiments Using Bidirectional and High-Density Microelectrode Arrays

## Executive Summary

This project proposes a structured collaboration between secondary-school students and a neuroscience research laboratory using a **three-stage electrophysiology architecture**: a **browser-based WetML simulation sandbox** for protocol design, the **Cortical Labs CL1** bidirectional biological computer for rapid closed-loop iteration, and the **MaxWell Biosystems MaxOne** High-Density Microelectrode Array (HD-MEA) for high-resolution mechanistic validation.

The central objective is to enable students to design, implement, and analyze closed-loop reinforcement-learning experiments in cultured human iPSC-derived neural networks, while providing a scientifically rigorous pathway from no-hardware-required protocol design, through rapid educational experimentation, to high-resolution electrophysiological validation.

The project is built around a **translation pipeline**:

0. Students design and rehearse stimulation-zone roles, truth tables, and frequency-based training protocols in a browser-based simulator, with no lab access required.
1. Validated protocol designs are transferred to the CL1, where students develop and optimize reinforcement algorithms and stimulation strategies on living tissue.
2. Successful algorithms are transferred to the MaxOne HD-MEA.
3. High-density recordings reveal the spatial and network mechanisms underlying adaptive behavior.

This staged approach combines a zero-cost, zero-risk design environment with the educational accessibility and rapid iteration of the CL1 and the scientific power and spatial resolution of the MaxOne.

This proposal builds directly on a validated body of published work rather than starting from first principles — specifically Kagan et al., *Neuron* (2022), the original DishBrain study, and the subsequent Cortical Labs research and product line that produced the CL1 (see **References**).

## Why Three Stages?

The simulation sandbox, CL1, and MaxOne each address a different scientific and educational objective, and are designed to hand off directly to one another.

### Stage 0: Browser-Based WetML Simulation Sandbox

Before any student touches live tissue or paid compute time, protocols are designed and pressure-tested in a single-file, browser-based simulator (no installation, no build tools, runs on any classroom Chromebook). The sandbox models the same conceptual architecture used on the MaxOne and CL1:

- **Physical zones vs. functional roles are separate.** A simulated topology (e.g. a 4×4 grid of zones) is deliberately oversized relative to the number of zones actually used for inference — mirroring the fact that only a subset of MaxOne's 26,400 electrodes are used as active stimulation or recording sites in any one protocol.
- **Role assignment**: each zone is manually assigned as Unused, Inference Stimulation, Sensor, Encourage, or Discourage. Encourage/Discourage are training-only modulation roles and are never part of the inference input vector — a direct analog of using a subset of stimulation sites for reinforcement delivery versus task-relevant input/output.
- **Frequency-based plasticity, not on/off stimulation.** Encourage and Discourage zones carry a 0–50 Hz training-frequency parameter rather than a binary flag, so students explore the core DishBrain/CL1 concept — that stimulation *frequency and predictability*, not stimulation presence alone, drives plasticity — before it costs lab time.
- **Editable truth table** mapping inference stimulation patterns to desired sensor outputs, letting students define the "task" a protocol should learn.
- **Influence matrix / heatmap** between stimulation and sensor zones, updated trial-by-trial via a simplified Hebbian-style rule, giving students an intuitive, immediately visible model of how repeated stimulation reshapes a mapping.
- **Save/load of full protocol state** (topology, roles, frequencies, influence weights, truth table) and **Python protocol export**, so a design that performs well in simulation can be handed directly to the Software Engineering Team as a starting point for CL1/MaxOne implementation.

This stage exists specifically to let students iterate on *task design, stimulation geometry, and reinforcement schedule* — the things they actually control — without touching tissue-safety parameters, cloud costs, or lab scheduling. It also gives the program a continuity-friendly artifact: the simulator and any saved protocol JSON files are plain browser-based files that outlive any single school year or piece of hardware.

### CL1: Bidirectional Closed-Loop Learning

The CL1 is Cortical Labs' commercial biological computer, launched in 2025 as a direct successor to the DishBrain research platform. Verified specifications relevant to this proposal:

- **~59 fully bidirectional electrodes** per unit — every active channel can both stimulate and record, a significant expansion from the 8 input channels used in the original 2022 DishBrain experiment.
- **Sub-millisecond closed-loop latency**, down from the roughly 5 ms latency of the original DishBrain setup — a meaningful improvement for real-time reinforcement algorithms.
- **On the order of 200,000 to 800,000 living human-derived neurons** per unit (reported figures vary by source/configuration), grown from stem cells derived from blood or skin samples.
- **Self-contained life-support bioreactor** (temperature, gas exchange, nutrient/waste management) rated to sustain cultures for **up to six months**, with active electrode charge-balancing to preserve neural health over long-term use.
- **Python SDK and browser-based tools** via the "Cortical Cloud" platform, enabling remote, code-deployable experiments without owning physical hardware ("Wetware as a Service"); local control is also available through a touchscreen-based operating system (**biOS**).
- **USB, camera, and actuator peripheral support**, allowing the CL1 to be embedded in broader robotics or sensor-driven experimental setups.
- Listed at roughly **US$35,000 per unit** as of its 2025 commercial launch, with cloud/remote access as a lower-cost alternative for a school-scale program.

This makes the CL1 an ideal platform for:

- reinforcement-learning experiments
- adaptive network control
- real-time feedback
- online optimization
- algorithm development
- student software engineering

Students can directly observe how changes in reinforcement schedules influence network behavior, making the relationship between prediction, stimulation, and learning visually and computationally intuitive — and because remote "Wetware as a Service" access is available, this stage does not necessarily require owning physical hardware.

### MaxOne: High-Density Mechanistic Validation

The MaxOne provides **26,400 electrodes**, enabling:

- spatial propagation mapping
- wavefront analysis
- functional connectivity reconstruction
- regional plasticity measurements
- high-resolution electrophysiological analysis

Only a small subset of MaxOne electrodes (order of tens, not hundreds) are typically routed as active stimulation sites in published protocols, with the bulk of the array used for recording — the same sparse-role principle rehearsed in the Stage 0 sandbox. The MaxOne is therefore the platform for understanding **why** a successful CL1 algorithm works, at a spatial resolution the CL1's 59 channels cannot provide.

The three systems become complementary rather than redundant: the sandbox for protocol design and intuition-building at zero cost, the CL1 for algorithm discovery and rapid iteration on living tissue, and the MaxOne for mechanistic explanation at high spatial resolution.

## Scientific Objective

Determine how programmable bidirectional electrode interactions and spatial stimulation geometries influence adaptive behavior, reinforcement learning, and network plasticity in cultured human neural networks.

The project addresses three complementary questions:

- **Design question (Sandbox):** Which zone-role configurations, truth-table mappings, and frequency-based training schedules produce stable, learnable protocols in simulation?
- **Algorithmic question (CL1):** Which of those reinforcement strategies produce the fastest and most stable adaptive behavior in living tissue?
- **Mechanistic question (MaxOne):** What spatial and network-level electrophysiological changes accompany successful learning?

## Relationship to Published Work (DishBrain / Cortical Labs)

This proposal builds directly on the closed-loop electrophysiology paradigm established by Kagan et al. (*Neuron*, 2022) and subsequent Cortical Labs research. That original study demonstrated that a simulated-game closed-loop feedback system produced measurable behavioral adaptation in cultured neurons within minutes, using a **predictable-versus-unpredictable stimulation** framework grounded in the free-energy principle (Friston et al.) rather than a simulated reward chemical. The CL1 is the direct commercial and technical descendant of that research platform — Cortical Labs' own materials describe its development as evolving from the 2022 DishBrain experiment, with the CL1 later publicly demonstrated running a Doom-based closed-loop task.

The project adopts already-validated stimulation safety parameters and this predictable-versus-unpredictable reinforcement framework, so that students innovate primarily in:

- reinforcement schedule design
- stimulation geometry
- adaptive control algorithms
- network routing
- software architecture

The Stage 0 sandbox is deliberately built around this same predictability/frequency framing — rather than an on/off "reward" model — so students internalize the correct mental model before ever touching a CL1 or MaxOne protocol. The CL1 extends the educational implementation of the DishBrain paradigm, while the MaxOne provides the spatial resolution necessary for detailed electrophysiological analysis. Because the underlying stimulation physics (charge-balanced biphasic pulses, safe voltage/frequency envelopes) has already been characterized and productized across both platforms, students are not exploring untested tissue-safety parameters — they are exploring *task, schedule, and geometry design* on top of validated hardware, starting in simulation and only later moving to tissue.

## Dual-Platform Experimental Architecture

### Stage 1: Algorithm Development (CL1)

Students implement programmable closed-loop experiments using the CL1, typically starting from a protocol already prototyped and saved from the Stage 0 sandbox.

Example experiments:

- predictable versus unpredictable reinforcement
- adaptive stimulation policies
- competing input pathways
- transfer learning between electrode groups
- online optimization
- curriculum learning
- state-dependent reinforcement

The emphasis is rapid iteration. A typical experimental cycle:

1. Prototype and refine a reinforcement algorithm in the Stage 0 sandbox.
2. Export the protocol design and implement it on the CL1.
3. Run a 5–10 minute closed-loop experiment.
4. Analyze behavioral metrics.
5. Modify the algorithm (in the sandbox, on the CL1, or both).
6. Repeat.

Multiple experiments can be completed within a school term, and the sub-millisecond latency of the CL1 means the feedback loop is fast enough for students to iterate live during a class period rather than waiting on offline analysis.

### Stage 2: High-Density Validation (MaxOne)

Algorithms that produce significant behavioral adaptation on the CL1 are transferred to the MaxOne.

Students investigate:

- spatial wave propagation
- response latency distributions
- regional plasticity
- functional connectivity
- information transfer
- network recruitment patterns
- long-term stability

This stage converts educational discoveries into mechanistic neuroscience experiments, and benefits from the MaxOne's much longer-running, larger cultures compared to a single CL1 unit's 59-channel footprint.

## Experimental Platform

### Sandbox Investigations (Stage 0)

Students will design and test, entirely in the browser:

- zone role assignments (Inference Stim / Sensor / Encourage / Discourage)
- sparse input/output mappings via editable truth tables
- frequency-based training schedules for Encourage/Discourage zones
- influence-matrix evolution under repeated trials
- exported Python protocol scaffolds for handoff to Stage 1

### CL1 Investigations

Students will design network interaction architectures, including:

- input/output routing
- recurrent feedback loops
- adaptive reinforcement schedules
- distributed sensory encoding
- multi-region competition
- dynamic network control

### MaxOne Investigations

Students will design spatial stimulation geometries, including:

- concentric rings
- radial spokes
- directional gradients
- opposing hemispheres
- rotating stimulation fields
- moving wavefronts
- localized predictability fields (framed as predictable-vs-unpredictable stimulation zones, per the DishBrain free-energy-principle model, rather than a literal "reward" chemical)

## Operational Definition of Learning

Learning will be defined as a measurable change in network behavior relative to baseline and control conditions.

**Design Metrics (Sandbox)**

- convergence of influence-matrix weights toward the target truth table
- sensitivity of convergence to Encourage/Discourage frequency settings
- stability of learned mappings when input patterns are cycled

**Behavioral Metrics (CL1)**

- response probability
- response latency
- adaptive accuracy
- reinforcement efficiency
- retention of learned responses
- transfer between input pathways

**Electrophysiological Metrics (MaxOne)**

- spike timing
- population burst dynamics
- functional connectivity
- spatial propagation velocity
- regional recruitment
- stability of learned network states

## Reinforcement Protocol Notes (carried over from validated published parameters)

- **Pulse shape:** charge-balanced, positive-first biphasic voltage pulses — the lowest-activation-threshold, most tissue-protective waveform, and standard practice on both platforms.
- **Published negative-feedback example (DishBrain, Kagan et al. 2022):** unpredictable stimulation around 150 mV at 5 Hz for approximately 4 seconds following a "miss."
- **Published positive-feedback logic:** predictable, low-entropy stimulation following a "hit" — reward is defined by predictability, not by a distinct reward waveform.
- Both the CL1 and MaxOne handle charge-balancing and safe stimulation envelopes at the hardware/firmware level, so student work should be scoped to schedule and geometry design on top of these built-in safety constraints rather than raw electrical parameter selection.
- The Stage 0 sandbox's 0–50 Hz training-frequency range is a simplified, non-biological placeholder for this predictable/unpredictable and low/high-frequency distinction — useful for building intuition, but explicitly not a substitute for the validated hardware-level parameters used at Stages 1 and 2.

## Three-Year Research Pipeline

### Year 1: Simulation-First Rapid Exploration (Sandbox + CL1)

Students focus on:

- protocol design and rehearsal in the browser-based sandbox (no hardware dependency, usable from day one of the course)
- reinforcement algorithms
- adaptive control
- software development
- behavioral analysis

The objective is high-throughput experimentation — starting entirely in simulation, then moving promising designs to the CL1 — feasible even via remote/cloud access to a CL1 unit if a physical unit is not locally available.

### Year 2: Longitudinal Learning Studies (CL1 + MaxOne)

Selected algorithms are transferred to newly prepared cultures.

Students investigate:

- acquisition
- retention
- transfer
- stability
- long-term plasticity

MaxOne validation begins.

### Year 3: Mechanistic Neuroscience (MaxOne)

Students analyze combined datasets and investigate:

- spatial plasticity mechanisms
- connectivity remodeling
- wave propagation
- adaptive network architecture
- automated optimization of stimulation geometries

The emphasis shifts from parameter exploration to hypothesis-driven neuroscience.

## Continuity Note

This program spans a multi-year biological and educational timeline that may extend past a single teacher's classroom tenure. To remain resilient to staff transitions (including planned retirement from full-time teaching), the program should be structured so that: (1) the software/data pipeline and experimental protocols are documented and version-controlled independently of any one individual, (2) the laboratory partner (family research contact) holds continuity of the biological/instrument side across cohorts, and (3) a designated in-school robotics/computing teacher of record is identified for each academic year, with the original proposer available in an advisory/consulting capacity post-retirement (e.g., via periodic TOC coverage or remote review of student software). The CL1's remote "Wetware as a Service" access model may also reduce continuity risk, since a physical unit does not need to remain sited at one school for the CL1-stage work to continue. The Stage 0 browser-based sandbox further reduces continuity risk: it is a single, dependency-free HTML file that runs offline, requires no institutional account or ongoing subscription, and can be handed to any future teacher of record, TOC, or student cohort with zero setup — protocol files saved from it (JSON) are portable across school years independent of who is running the program.

## Student Research Roles

### Protocol Design Team (Sandbox)

- design zone-role layouts and sparse input/output mappings
- author and iterate on truth tables
- tune Encourage/Discourage frequency schedules and interpret influence-matrix convergence
- export candidate protocols for the Software Engineering Team

### Reinforcement Learning Team

- design adaptive stimulation policies
- optimize reinforcement schedules
- analyze behavioral learning

### Network Architecture Team

- define input/output routing
- design recurrent network structures
- investigate transfer learning

### Computational Analysis Team

- process spike trains
- compute connectivity metrics
- analyze spatial propagation
- perform statistical analyses

### Software Engineering Team

- maintain and extend the Stage 0 simulation sandbox
- implement real-time closed-loop control (Python, on top of the CL1 SDK and the MaxWell control API)
- integrate CL1 and MaxOne APIs
- validate timing precision
- manage experimental databases

### Laboratory Team

- cell culture
- sterile handling
- hardware operation
- experimental oversight

## Experimental Controls

Parallel control conditions will include:

- open-loop stimulation
- random reinforcement
- sham reinforcement
- algorithm-transfer controls
- platform-comparison controls (Sandbox versus CL1 versus MaxOne)

These controls distinguish reinforcement-dependent plasticity from spontaneous network dynamics and platform-specific artifacts, and mirror the control conditions used in the published DishBrain literature (e.g., feedback-without-sensory-input and sensory-input-without-feedback conditions, which showed no learning).

## Ethics and Laboratory Oversight

All cell culture, stem-cell differentiation, and electrophysiology experiments will be conducted under the supervision of the host research laboratory and in accordance with institutional biosafety and ethics approvals. The Stage 0 sandbox involves no biological material whatsoever and is exempt from this oversight; it is included here specifically so students can be assessed on protocol design *before* any request to work with live tissue is made, keeping the ethics-approval scope tightly bounded to Stages 1 and 2.

Students will participate in approved activities including experimental design, software development, stimulation-program development, quantitative data analysis, and scientific interpretation. Biological materials will remain under laboratory control at all times.

Cortical Labs' own Chief Scientific Officer has publicly and directly addressed the ethical implications of this class of research, stating that despite their biological origins, these cultured neuron networks are not considered conscious. Given that the original DishBrain publication explicitly raised and debated the term "sentience" in relation to cultured neural networks, this proposal should present its framing (predictability/entropy-based reinforcement, not anthropomorphized "reward," and the "not conscious" position taken by the platform's own developers) clearly and early to any school board, ethics board, or parent-facing materials, to avoid unnecessary controversy grounded in a misunderstanding of the underlying mechanism.

## Expected Deliverables

- A browser-based, dependency-free WetML protocol design sandbox (Stage 0), including save/load and Python export
- A validated closed-loop reinforcement-learning software framework
- A library of adaptive stimulation algorithms
- A library of spatial stimulation geometries
- A cross-platform translation pipeline (Sandbox → CL1 → MaxOne)
- An anonymized electrophysiology dataset
- Mechanistic analyses of adaptive network behavior
- Student-authored scientific posters, reports, and manuscript contributions

## Significance

This project creates a sustainable educational-to-research pipeline in which secondary-school students participate in authentic neuroscience while contributing directly to the development of next-generation bio-hybrid learning experiments — starting from a zero-cost, zero-risk simulation environment and progressing, for validated designs, to living tissue.


<br><br>
<hr>

## References

**Primary published research (DishBrain / Cortical Labs)**

- Kagan, B.J. et al. (2022). *[In vitro neurons learn and exhibit sentience when embodied in a simulated game-world](https://www.cell.com/neuron/fulltext/S0896-6273(22)00806-6).* Neuron. Open access, CC BY 4.0.
- Khajehnejad, M., Habibollahi, F., Loeffler, A., Paul, A., Razi, A., Kagan, B.J. (2024). *[Biological Neurons Compete with Deep Reinforcement Learning in Sample Efficiency in a Simulated Gameworld](https://arxiv.org/pdf/2405.16946).* arXiv:2405.16946.
- Khajehnejad, M. et al. (2025). *[Dynamic Network Plasticity and Sample Efficiency in Biological Neural Cultures: A Comparative Study with Deep Reinforcement Learning](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12320521/).* Cyborg and Bionic Systems.
- [Cortical Labs Research page](https://corticallabs.com/research) — full list of published papers, including the CL API real-time closed-loop paper.

**CL1 platform (specifications and launch coverage)**

- [Cortical Labs — CL1 product page](https://corticallabs.com/cl1) — official specs, Python SDK, Cortical Cloud / Wetware-as-a-Service access.
- [IEEE Spectrum: "Biological Computer for Sale"](https://spectrum.ieee.org/biological-computer-for-sale) — independent technical coverage confirming the expansion from 8 inputs (DishBrain) to 59 bidirectional electrodes (CL1), and the drop from ~5 ms to sub-millisecond latency.
- [Cortical Labs CL1 — Good Design Awards project page](https://good-design.org/projects/cortical-labs-cl1/) — design/engineering details, active charge-balancing, biOS touchscreen, peripheral support.
- [CL1 Biological Computer — Premier's Design Awards entry](https://premiersdesignawards.vic.gov.au/entries/2025/product-design/cortical-labs-cl1-biological-computer) — life-support system, six-month culture viability, Cortical Cloud details.
- ["Exclusive Look at CL1: One-on-One with Cortical Labs' Chief Scientist"](https://deniseholt.us/exclusive-inside-look-one-on-one-with-cortical-labs-chief-scientist-from-dishbrain-to-cl1/) — Brett Kagan on the Python API and the ethics/consciousness question.
- ["Researchers teach a biological computer called CL1 ... to play Doom"](https://cerebrodigital.net/en/researchers-teach-a-biological-computer-called-cl1-made-with-human-brain-cells-to-play-doom/) — CL1 Doom demonstration and clarification of what "deploying code" to neurons actually means.
- [Reply and University of Milan — CL1 research collaboration announcement](https://secure.businesswire.com/news/home/20260128715625/en/Reply-and-the-University-of-Milan-Launch-Experimental-Research-on-Biological-Computing-Based-on-Cortical-Labs-CL1-Platform) — example of an academic partnership built on the CL1 platform, useful as a precedent for a school-lab partnership pitch.

**Coverage and context (original DishBrain result)**

- [UCL News: "Human brain cells in a dish learn to play Pong"](https://www.ucl.ac.uk/news/2022/oct/human-brain-cells-dish-learn-play-pong)
- [Monash University: "Brain cells in a dish learn to play Pong"](https://www.monash.edu/medicine/news/latest/2022-articles/brain-cells-in-a-dish-learn-to-play-pong)
- [Nature News & Views: "Neurons in a dish learn to play Pong — what's next?"](https://www.nature.com/articles/d41586-022-03229-y)
- [ScienceDaily: "Human brain cells in a dish learn to play Pong in real time"](https://www.sciencedaily.com/releases/2022/10/221012132528.htm)

**Video**

- [Cortical Labs official YouTube channel](https://www.youtube.com/channel/UCq4mqLeGRdq47sHumYMIDJw) — DishBrain demos, CL1 launch, neurons playing Doom with source on GitHub.
- ["Brain in a Dish Plays Pong: Cortical Labs' CL1 Biocomputer"](https://www.youtube.com/watch?v=W-NGW_VHYOw) — lab walkthrough, Melbourne.
- ["Cortical Labs' CL1 Just Made Traditional Computers Obsolete"](https://www.youtube.com/watch?v=6wUrgu0pvI4) — CL1 launch coverage.

**Hardware / platform**

###  Multi-Electrode Array Platforms for Neural Network Research

- **[MaxWell Biosystems](https://www.mxwbio.com/products/maxone)** — Manufacturer of the MaxOne (single-well) and MaxTwo (multi-well) HD-MEA platforms, widely cited for high-resolution, long-term neuronal network monitoring.
- **[Cortical Labs](https://corticallabs.com/cl1)** — Developer of the CL1 biological computer, which utilizes a closed-loop stimulation paradigm directly integrated with neurons on a silicon chip.
- **[3Brain](https://www.3brain.com/products/multiwell/coreplate-tm-multiwell-96w)** — Provider of the CorePlate™ 96W, a high-throughput HD-MEA system capable of simultaneous recording across all wells.
- **[Multi Channel Systems](https://www.multichannelsystems.com/products/mesh-mea)** — Manufacturer of the Mesh MEA, specifically designed for 3D organoid electrophysiology, allowing recordings from within the structure.
- **[Axion BioSystems](https://axionbiosystems.com/products/mea/maestro-pro)** — Maker of the *Maestro Pro* and *Maestro Edge* platforms; standard equipment for automated, high-throughput closed-loop stimulation and neuronal recording assays.
- **[Blackrock Neurotech](https://blackrockneurotech.com/products/neuroport-electrode/)** — Manufacturer of the Utah Array and high-density penetrating probes, primarily utilized for in-vivo neural interfacing.
- **[Neuronexus](https://neuronexus.com/products/)** — Provides a wide range of silicon-based neural probes (planar and 3D) optimized for diverse in-vitro and in-vivo network recording applications.
- **[Cambridge NeuroTech](https://cambridgeneurotech.com)** — Specializes in ultra-dense silicon probes and specialized microelectrode arrays, highly regarded for signal-to-noise ratio in network-level recordings.
- **[Alpha MED Scientific](https://www.med64.com)** — Originators of the MED64 system, offering established platforms for high-sensitivity recordings from stem-cell-derived models and brain slices.
- **[TissueLabs](https://tissuelabs.com)** — Focused on organoid-compatible platforms and biofabrication, relevant for researchers integrating electrophysiology into custom organ-on-chip neural models.
- **[Harvard Bioscience](https://www.harvardbioscience.com/products/organoid-electrophysiology)** — Distributor of the Mesh MEA technology (see Multi Channel Systems) for organoid-specific electrophysiology.
- **[BMSeed](https://www.bmseed.com/overview)** — In Vitro Research Tools with True In Vivo Relevance. 
- **[]()** —
- **[]()** —
- **[]()** —
- **[]()** —
- **[]()** —
- **[]()** —



## HDF5 File Viewers


- **[https://myhdf5.hdfgroup.org/view](https://myhdf5.hdfgroup.org/view)** -Seems to be the best online hdf5 viewer
- **[https://myhdf5.hdfgroup.org/help#remote](https://myhdf5.hdfgroup.org/help#remote)** —Possible links 
- **[https://hdfviewer.com/](https://hdfviewer.com/)** — Online hdf5 viewer
- **[https://perchance.org/hdf5-file-viewer](https://perchance.org/hdf5-file-viewer)** — another hdf5 viewer
- 







