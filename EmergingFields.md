# Emerging Fields in Computing & Engineering

## Overview
This document covers rapidly evolving fields and technologies that are shaping the future of computing and engineering. Students are encouraged to explore these areas through self-study, projects, and research.

---

## Quantum Computing

### Overview
Quantum computing leverages quantum mechanical phenomena (superposition, entanglement, interference) to perform computations that are infeasible for classical computers.

### Key Concepts
- **Qubits:** Superposition (|0⟩, |1⟩, and both), entanglement, quantum gates
- **Quantum Algorithms:** Shor's algorithm (factoring), Grover's algorithm (search), quantum Fourier transform, quantum phase estimation
- **Quantum Error Correction:** Surface codes, stabilizer codes, fault tolerance
- **Quantum Hardware:** Superconducting qubits (IBM, Google), trapped ions (IonQ), photonic quantum computing, topological qubits

### Learning Resources
- **Books:** "Quantum Computing for Computer Scientists" by Yanofsky and Mannucci, "Quantum Computation and Quantum Information" by Nielsen and Chuang
- **Online Courses:** IBM Qiskit textbook, Microsoft Quantum Learning, MIT Quantum Computing
- **Frameworks:** Qiskit (IBM), Cirq (Google), Q# (Microsoft), PennyLane (quantum ML)
- **Simulators:** IBM Quantum Experience, Amazon Braket, Azure Quantum

### Practical Projects
- Implement quantum teleportation circuit
- Write Grover's search algorithm for a small database
- Simulate quantum error correction codes
- Implement a quantum key distribution (QKD) protocol

---

## Edge Computing

### Overview
Edge computing brings computation and data storage closer to where data is generated, reducing latency, bandwidth usage, and enabling real-time processing.

### Key Concepts
- **Edge Architecture:** Edge devices, edge nodes, edge gateways, fog computing, cloud-edge continuum
- **Edge vs. Cloud:** Latency, bandwidth, privacy, reliability, cost trade-offs
- **Edge ML:** On-device inference, model compression, TinyML, Federated Learning
- **Protocols:** MQTT, CoAP, HTTP/2, gRPC, WebRTC
- **Platforms:** AWS Greengrass, Azure IoT Edge, Google Anthos, EdgeX Foundry

### Learning Resources
- **Books:** "Edge Computing: A Primer" by Cao, "Fog and Edge Computing" by Buyya
- **Online Courses:** Coursera Edge Computing Specialization, Linux Foundation Edge Academy
- **Tools:** KubeEdge, EdgeX Foundry, OpenYurt

### Practical Projects
- Deploy ML inference on a Raspberry Pi
- Build a real-time video analytics pipeline at the edge
- Implement a distributed edge-cloud application
- Set up a Kubernetes cluster at the edge with KubeEdge

---

## Extended Reality (AR/VR/MR)

### Overview
Extended Reality (XR) encompasses Augmented Reality (AR), Virtual Reality (VR), and Mixed Reality (MR), creating immersive digital experiences that blend the physical and virtual worlds.

### Key Concepts
- **AR:** Overlay digital content on the real world (ARKit, ARCore, WebXR)
- **VR:** Fully immersive virtual environments (Unity, Unreal Engine, WebXR)
- **MR:** Interactive virtual objects that respond to the real world (HoloLens, Magic Leap)
- **Spatial Computing:** 3D mapping, SLAM, hand tracking, eye tracking, gesture recognition
- **Rendering:** Real-time 3D rendering, ray tracing, foveated rendering, photogrammetry

### Learning Resources
- **Books:** "Learning Virtual Reality" by Parisi, "Augmented Reality: Principles and Practice" by Schmalstieg
- **Frameworks:** Unity XR Toolkit, Unreal Engine XR, ARKit, ARCore, WebXR, OpenXR
- **Hardware:** Meta Quest, Apple Vision Pro, HoloLens, Magic Leap, PlayStation VR

### Practical Projects
- Build an AR app for furniture placement (ARKit/ARCore)
- Create a VR museum tour experience (Unity)
- Develop a hand-tracking interactive application
- Build a collaborative MR environment

---

## Autonomous Systems

### Overview
Autonomous systems are self-governing systems that can operate without human intervention, including self-driving cars, drones, and autonomous robots.

### Key Concepts
- **Perception:** LiDAR, radar, cameras, sensor fusion, object detection, semantic segmentation
- **Localization and Mapping:** SLAM, visual odometry, GPS/IMU fusion
- **Planning and Control:** Path planning, motion planning, trajectory optimization, Model Predictive Control (MPC)
- **Decision Making:** Behavior planning, prediction, reinforcement learning, imitation learning
- **Safety and Verification:** Functional safety (ISO 26262), formal verification, simulation testing

### Learning Resources
- **Books:** "Probabilistic Robotics" by Thrun, Burgard, and Fox, "Autonomous Driving" by Watzenig
- **Simulators:** CARLA, AirSim, Gazebo, Webots, LGSVL
- **Datasets:** KITTI, Waymo Open Dataset, nuScenes, Cityscapes
- **Frameworks:** Autoware, Apollo, ROS 2 Navigation2

### Practical Projects
- Implement lane detection and tracking for a simulated vehicle
- Build a drone autonomous navigation system (PX4/ArduPilot)
- Implement a behavior planning system for autonomous driving
- Deploy a robot with autonomous navigation in a warehouse simulation

---

## Bioinformatics and Computational Biology

### Overview
Bioinformatics applies computational techniques to analyze biological data, including genomics, proteomics, and systems biology.

### Key Concepts
- **Genomics:** DNA sequencing (NGS, long-read), genome assembly, variant calling, GWAS
- **Transcriptomics:** RNA-seq, gene expression analysis, single-cell RNA-seq
- **Proteomics:** Mass spectrometry, protein structure prediction (AlphaFold)
- **Systems Biology:** Metabolic networks, gene regulatory networks, pathway analysis
- **Machine Learning in Biology:** Deep learning for genomics, protein folding, drug discovery

### Learning Resources
- **Books:** "Bioinformatics Algorithms" by Compeau and Pevzner, "Biological Sequence Analysis" by Durbin
- **Tools:** BLAST, Biopython, R/Bioconductor, GATK, Galaxy, Cell Ranger, Seurat
- **Databases:** NCBI, UCSC Genome Browser, UniProt, PDB, Ensembl, GEO
- **Online Courses:** Coursera Bioinformatics Specialization, edX Genomics

### Practical Projects
- Analyze RNA-seq data for differential gene expression
- Build a phylogenetic tree from sequence data
- Implement a variant calling pipeline
- Predict protein structure using AlphaFold

---

## Green Computing and Sustainable Engineering

### Overview
Green computing focuses on designing, manufacturing, and using computing resources in an environmentally sustainable manner, minimizing energy consumption and electronic waste.

### Key Concepts
- **Energy-Efficient Computing:** Low-power processors, energy-aware scheduling, DVFS, green data centers
- **Renewable Energy Integration:** Solar-powered data centers, energy harvesting, battery optimization
- **E-Waste Management:** Recycling, refurbishment, circular economy, RoHS compliance
- **Carbon Footprint:** Carbon-aware computing, carbon offsetting, life cycle assessment
- **Sustainable Software:** Efficient algorithms, cloud optimization, edge computing for sustainability

### Learning Resources
- **Books:** "Green IT" by Velte, "Sustainable Computing" by Tomlinson
- **Standards:** Energy Star, EPEAT, LEED for data centers
- **Tools:** PowerAPI, JouleMeter, Intel RAPL, Cloud Carbon Footprint

### Practical Projects
- Measure and optimize energy consumption of a software application
- Design a solar-powered IoT sensor node
- Implement a carbon-aware task scheduler
- Analyze the carbon footprint of a cloud deployment

---

## Human-Computer Interaction (HCI)

### Overview
HCI studies the design, evaluation, and implementation of interactive computing systems for human use, focusing on usability, accessibility, and user experience.

### Key Concepts
- **Usability:** Learnability, efficiency, memorability, errors, satisfaction (Nielsen's heuristics)
- **User-Centered Design:** User research, personas, scenarios, prototyping, iterative design
- **Interaction Design:** Command-line, GUI, touch, gesture, voice, multimodal interaction
- **Accessibility:** WCAG, universal design, assistive technologies, screen readers
- **Evaluation:** Usability testing, A/B testing, eye tracking, cognitive walkthroughs

### Learning Resources
- **Books:** "The Design of Everyday Things" by Norman, "Interaction Design" by Sharp, Preece, and Rogers
- **Tools:** Figma, Sketch, Adobe XD, Balsamiq, Axure
- **Online Courses:** Coursera HCI Specialization, Interaction Design Foundation

### Practical Projects
- Conduct a usability evaluation of a website
- Design and prototype a mobile app (Figma)
- Implement an accessible web interface (WCAG compliance)
- Build a voice-controlled application

---

## Agentic AI Development

### Overview
Agentic AI focuses on building autonomous agents that can plan, reason, and execute tasks using LLMs. This field integrates AI-assisted coding, tool use, and agentic workflows to build intelligent software systems.

### Key Concepts & Modules
- **Module 1: Agentic Workflows:** Planning (chain-of-thought, tree-of-thought), reflection, tool use (using search, code execution, web browsing), and multi-agent orchestration.
- **Module 2: AI-Assisted Coding (Intro):** Leveraging AI models to generate, debug, test, and document code efficiently. Techniques for prompt engineering in coding assistants (GitHub Copilot, Cursor), context management, and utilizing agentic CLIs for automated development.
- **Module 3: LLM Integration:** Prompt engineering, Retrieval-Augmented Generation (RAG) for agent knowledge, fine-tuning for specific agent tasks, and managing agent context window limitations.
- **Module 4: Agent Frameworks:** Hands-on experience with LangChain, AutoGen (multi-agent), CrewAI, and understanding the AgentProtocol standard.

### Learning Resources
- **Online Courses:** DeepLearning.AI Agentic Workflows, LangChain Academy, Coursera LLM specializations.
- **Tools:** Cursor IDE, GitHub Copilot, LangSmith (for tracing), CrewAI Studio.

### Practical Projects
- **Project 1:** Build a research assistant agent that uses search, reads multiple sources, and summarizes papers into a structured report.
- **Project 2:** Create an agentic coding assistant that automates code review, generates documentation, and writes missing unit tests for a repository.
- **Project 3:** Develop a multi-agent system to automate a simple workflow (e.g., data analysis pipeline, content generation, or market research) where agents negotiate and exchange data.

### YouTube Channels (English)
- **AI Engineer:** https://www.youtube.com/@aiDotEngineer
- **Dave Ebbelaar:** https://www.youtube.com/@daveebbelaar

---

## Neuromorphic Computing

### Overview
Neuromorphic computing designs computing systems inspired by the structure and function of the human brain. It uses artificial neurons, synapses, and spike-based communication to perform computation in a highly parallel, event-driven, and energy-efficient manner, enabling real-time sensory processing and cognitive tasks.

### Key Concepts
- **Spiking Neural Networks (SNNs):** Event-driven computation, spike-timing-dependent plasticity (STDP), Leaky Integrate-and-Fire (LIF) neurons, temporal coding, surrogate gradient learning
- **Neuromorphic Hardware:** Memristors, neuromorphic chips (Intel Loihi 2, IBM TrueNorth/NorthPole, BrainChip Akida), analog/digital hybrid circuits, NeuroGrid
- **Brain-Inspired Architectures:** Neural cores, synaptic crossbar arrays, asynchronous circuits, event-driven processing, address-event representation (AER)
- **Learning Mechanisms:** On-chip local learning, Hebbian learning, STDP, three-factor learning rules, equilibrium propagation
- **Event-Based Sensing:** Dynamic vision sensors (DVS), event-based audio sensors, neuromorphic tactile sensors, closed-loop neuromorphic systems

### Learning Resources
- **Books:** "Neuromorphic Engineering" by Liu et al., "Spiking Neuron Models" by Gerstner and Kistler, "Memristive Networks" by Adamatzky, "Neuromorphic Computing and Engineering" by Indiveri
- **Online Courses:** Intel Neuromorphic Computing Academy, UZH/ETH Neuromorphic Engineering (Coursera), Nengo deep learning tutorials, Telluride Neuromorphic Workshop
- **Frameworks:** Lava (Intel), Nengo, NEST, Brian2, SNN Torch, Norse, SpikingJelly, Rockpool
- **Hardware:** Intel Loihi 2, IBM NorthPole, BrainChip Akida, SynSense Speck, Innatera T1

### Practical Projects
- Implement a spiking neural network for MNIST digit recognition using SNN Torch or Norse
- Build an event-based vision pipeline using DVS camera data and a neuromorphic processor
- Simulate a keyword spotting system using a neuromorphic audio processing pipeline
- Implement STDP-based unsupervised learning on a pattern recognition task
- Deploy a neuromorphic model on Intel Loihi 2 using the Lava framework

### YouTube Channels (English)
- **Intel Neuromorphic Community:** https://www.youtube.com/@IntelNeuromorphic
- **Neuromorphic Engineer:** https://www.youtube.com/@neuromorphic_engineer
- **Nengo AI:** https://www.youtube.com/@NengoBrainSimulator

---

1. **Pick one field** that aligns with your interests and career goals
2. **Start with fundamentals** — read the recommended books and take online courses
3. **Hands-on practice** — work through tutorials and build small projects
4. **Join communities** — participate in forums, Discord servers, subreddits, and local meetups
5. **Contribute to open source** — find projects on GitHub related to these fields
6. **Attend conferences** — follow key conferences (NeurIPS, ICRA, CVPR, CHI, ISSCC)
7. **Build a portfolio** — document your projects and share them on GitHub, LinkedIn, or a personal website
