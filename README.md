# neuro-ml
neuro machine learning

Website of this README.md file https://hpssjellis.github.io/neuro-ml/



# Project Proposal: Student-Designed Closed-Loop Electrophysiology Experiments Using High-Density Microelectrode Arrays

## Executive Summary

This project proposes a structured collaboration between secondary-school students and a neuroscience research laboratory using the MaxWell Biosystems **MaxOne High-Density Microelectrode Array (HD-MEA)** platform. The objective is not to conduct unsupervised biological research, but to enable students to design and implement quantitatively defined closed-loop electrophysiology experiments under laboratory supervision.

Students will develop spatial stimulation geometries and real-time feedback algorithms for cultured human induced pluripotent stem cell (iPSC)-derived neural networks. The central scientific question is whether spatially structured electrical stimulation combined with automated reinforcement schedules produces measurable changes in network activity, functional connectivity, and stimulus-response performance.

## Scientific Objective

Determine whether closed-loop electrical reinforcement modifies the electrophysiological behavior of cultured human neural networks recorded on a **26,400-electrode HD-MEA**.

The primary hypothesis is that repeated contingent reinforcement following predefined network responses will produce statistically measurable changes in response probability, spike timing, and network connectivity compared with open-loop stimulation controls.

## Experimental System

The MaxOne HD-MEA enables simultaneous recording and stimulation across a high-density electrode array. A subset of electrodes can be dynamically routed for stimulation and recording.

The experiment consists of three components:

1. Spatially patterned electrical stimulation.
2. Real-time detection of network responses.
3. Automated contingent reinforcement based on predefined response criteria.

## Operational Definition of Learning

Learning will be defined operationally as a change in one or more measurable electrophysiological metrics relative to baseline and control conditions.

**Primary outcome measures**

- Evoked response probability.
- Spike latency following stimulation.
- Population burst frequency.
- Functional connectivity inferred from spike-train correlations.
- Information transfer between stimulated and output regions.
- Stability of the response across repeated trials.

## Reinforcement Protocol

Students will implement programmable reinforcement schedules using charge-balanced biphasic stimulation pulses.

**Example experimental paradigm**

- Initial stimulus delivered through a defined spatial electrode pattern.
- Network activity evaluated within a predefined post-stimulus window (for example, **5–20 ms**).
- A response is classified as successful if activity exceeds a threshold in a designated output region.
- Successful responses trigger a reinforcement burst.
- Unsuccessful responses trigger either no reinforcement or an alternative low-frequency stimulation condition.

Importantly, the reinforcement frequencies (for example, **30 Hz versus 2 Hz**) are experimental variables rather than assumed biological learning parameters. Their effects will be compared empirically across experimental groups.

## Student Research Roles

### Experimental Design Team

- Design spatial stimulation geometries.
- Define input and output electrode regions.
- Specify reinforcement contingencies.
- Develop control conditions.

### Computational Analysis Team

- Process spike trains.
- Detect evoked responses.
- Compute connectivity metrics.
- Perform statistical analyses.

### Software Engineering Team

- Implement real-time closed-loop control.
- Integrate recording and stimulation pipelines.
- Validate timing precision.
- Log experimental metadata.

### Laboratory Team (Research Supervision)

- Cell culture and differentiation.
- Sterile handling.
- Electrode preparation.
- Hardware operation.
- Experimental oversight.

## Experimental Controls

A scientifically valid comparison requires parallel control conditions.

### Open-Loop Control

Identical stimulation delivered without contingent reinforcement.

### Random Reinforcement Control

Reinforcement delivered with identical frequency but independent of network output.

### Sham Reinforcement Control

Detection algorithm executed without delivery of reinforcement pulses.

These controls distinguish reinforcement-dependent plasticity from spontaneous network drift and stimulation-induced adaptation.

## Data Analysis

**Primary analysis**

- Within-network comparison before versus after reinforcement.
- Between-group comparison across reinforcement conditions.

**Statistical methods**

- Mixed-effects models for repeated measurements.
- Permutation tests for connectivity changes.
- Survival analysis of response persistence.
- False-discovery-rate correction for multiple comparisons.

## Project Roadmap

### Phase 1 (Months 1–2)

- Literature review.
- Simulation of stimulation geometries.
- Development of response-detection algorithms.
- Validation of timing precision.

### Phase 2 (Months 3–4)

- Baseline recordings.
- Open-loop stimulation experiments.
- Optimization of electrode routing.
- Signal-to-noise characterization.

### Phase 3 (Months 5–6)

- Closed-loop reinforcement experiments.
- Control experiments.
- Quantitative analysis of plasticity metrics.
- Statistical evaluation and reporting.

## Educational Outcomes

Students will gain experience in:

- Experimental design.
- Electrophysiology.
- Signal processing.
- Real-time control systems.
- Quantitative data analysis.
- Scientific reproducibility.

## Expected Deliverables

- A validated closed-loop stimulation software framework.
- A documented stimulation and analysis protocol.
- An anonymized electrophysiology dataset.
- A statistical analysis report comparing reinforcement and control conditions.
- A student co-authored scientific poster or manuscript draft.

This framework allows students to participate meaningfully in advanced neurophysiology research while maintaining rigorous experimental design, quantitative evaluation, and appropriate laboratory supervision.





## maxaOne Time Series Note: there is also a live array view
![media/maxone-time-series.png](media/maxone-time-series.png)


## MaxOne sample data tray
![media/maxone-tray.png](media/maxone-tray.png)


## Old Sensor 12-64x64-neuro-electrodes-front.png
![media/12-64x64-neuro-electrodes-front.png](media/12-64x64-neuro-electrodes-front.png)


## Old Sensor 12-64x64-neuro-electrodes-back.png
![media/****](media/12-64x64-neuro-electrodes-back.png)





