Testing at

https://hpssjellis.github.io/neuro-ml/maxone/maxone-sim-v0#.html  where # increases as things improve

Typically https://hpssjellis.github.io/neuro-ml/maxone/maxone-sim.html  is the best stable version.




Build a complete, single-file HTML webpage using vanilla JavaScript, inline CSS, and a Three.js WebGL visualization to serve as a pedagogical sandbox and simulation testbed for High-Density Microelectrode Array (HD-MEA) biocomputing workflows.

### Core Simulation Specifications for Version 1:
1. **Hardware Mapping & Limitations:**
   - Model a virtualized subset of a MaxOne chip architecture featuring 32 programmable stimulation sites and a subsampled active view of 1,000 active sensor nodes out of the total 26,400 physical electrodes.
   - Implement spatial zone management supporting configurable zones for stimulation (stim), inhibition (inhib), excitation (excite), and output sensing (sense).
2. **Visual Layout (Three.js):**
   - Render a 3D volumetric space representing a single-layer microelectrode array interface, with a clear toggle path prepared for a future bi-layer (top/bottom sandwich) expansion.
   - Use color-coded nodes to distinguish active states: green for resting, red/pink for excitation/stimulation pulses, blue for inhibition, and yellow/orange for output sensing events.
3. **Behavioral Logic & Clock Scaling:**
   - Implement variable time-scaling via JavaScript loops: a slow training epoch mode (allowing weight adjustments and spatial distance rule evaluations) and a fast inference testing mode.
   - Start the layout with a minimal 2x2 grid configuration placed at maximal physical separation across the bounds, with UI controls to dynamically scale outward to 3x3 and higher multi-zone topologies.
4. **Code and Architecture Conventions:**
   - Strictly use camelCase for all JavaScript variables and function names, ensuring every local variable and function name explicitly starts with the prefix "my" (e.g., myCanvasContainer, myRunSimulationLoop).
   - Keep the code completely self-contained within a single HTML file with minimal, clean inline CSS. Use async/await structures rather than .then promise formatting. Use static links to function names instead of addEventListener bindings.

### Roadmap for Subsequent Versions:
- **Version 2:** Integrate TensorFlow.js backpropagation routines to adapt the simulated neuronal network weights dynamically as new training streams arrive, mapping spatial distance rules and precise frequency/amplitude variables for stim, inhibit, and excite signals.
- **Version 3:** Introduce the dual-layer "sandwich" topology (top stimulation layer and bottom sensing layer with a simulated 3D organoid volume between them) to test directional Z-axis vector fields and zero-latency closed-loop feedback loops before physical C++ API deployment.





