<!--
Mentorship Context: CS Mentor
Skill: cs-mentor
Feedback Log: ../cs-mentor/references/feedback_log.md
-->

# Semester 5: Networks & Systems Programming

## Computer Communications Networks

### Overview
Study of computer networking principles, protocols, and architectures. Covers the OSI and TCP/IP models, data communication, network protocols, and network applications.

### Learning Objectives
- Understand data communication fundamentals: transmission media, encoding, multiplexing
- Understand layered network architectures (OSI, TCP/IP)
- Analyze data link layer protocols: framing, error detection/correction, MAC
- Understand network layer: IP addressing, routing, subnetting
- Analyze transport layer protocols: TCP, UDP, congestion control
- Implement network applications using socket programming

### Detailed Topics
- **Module 1:** Data Communication: analog/digital signals, transmission media (guided, unguided), bandwidth, data rate, Nyquist formula, Shannon capacity
- **Module 2:** Encoding and Modulation: digital-to-digital (NRZ, Manchester), digital-to-analog (ASK, FSK, PSK, QAM), analog-to-digital (PCM, DM)
- **Module 3:** Multiplexing: FDM, TDM, WDM, CDMA, spread spectrum
- **Module 4:** Network Architecture: OSI model, TCP/IP model, encapsulation, peer-to-peer communication
- **Module 5:** Data Link Layer: framing, error detection (parity, CRC, checksum), error correction (Hamming code), flow control (stop-and-wait, sliding window), ARQ (stop-and-wait, go-back-N, selective repeat)
- **Module 6:** Multiple Access: ALOHA, slotted ALOHA, CSMA/CD, CSMA/CA, token passing, Ethernet (802.3), WiFi (802.11)
- **Module 7:** Network Layer: IPv4, IPv6, addressing, subnetting, CIDR, NAT, ICMP, ARP, DHCP
- **Module 8:** Routing: static vs. dynamic, distance vector (RIP), link state (OSPF), path vector (BGP), multicast routing
- **Module 9:** Transport Layer: multiplexing/demultiplexing, UDP, TCP (segment structure, flow control, connection management, congestion control: AIMD, slow start, fast retransmit)
- **Module 10:** Application Layer: HTTP/HTTPS, DNS, SMTP, POP3, IMAP, FTP, DHCP, SNMP

### Books
- **"Data Communications and Networking, 5th Edition"** by Behrouz A. Forouzan (McGraw-Hill, 2012) — Standard text
- **"Computer Networking: A Top-Down Approach, 8th Edition"** by Kurose and Ross (Pearson, 2021)
- **"Computer Networks, 5th Edition"** by Tanenbaum and Wetherall (Pearson, 2010)

### Lab Work
- **Lab 1:** Network cable crimping and testing (straight, crossover)
- **Lab 2:** IP configuration, subnetting exercises, ping, traceroute
- **Lab 3:** Wireshark packet analysis (HTTP, DNS, TCP, ARP)
- **Lab 4:** Socket programming: TCP client-server
- **Lab 5:** Socket programming: UDP client-server
- **Lab 6:** Cisco Packet Tracer: network topology configuration

### YouTube Channels (English)
- **Neso Academy:** Computer networks, data communication
- **Professor Messer:** Network+ certification, networking fundamentals
- **TechTerms:** Networking concepts explained simply
- **PowerCert Animated Videos:** Networking, subnetting, protocols
- **freeCodeCamp.org:** Computer networking full course
- **CertBros:** Networking, CCNA, subnetting
- **NetworkChuck:** Networking, CCNA, cybersecurity

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** Computer networks, data communication — https://youtube.com/ @GateSmashers 
- **KnowledgeGate (Hindi):** Networking, TCP/IP, routing — https://youtube.com/ @KnowledgeGate 
- **Learn Coding (Hindi):** Computer networks, protocols
- **Technical Sagar (Hindi):** Networking, IP addressing, subnetting
- **EduPoint (Hindi):** Computer networks, OSI model
- **Neso Academy (Hindi):** Computer networks in Hindi
- **Easy Engineering (Hindi):** Networking, data communication
- **Urdu IT Academy (Urdu):** Computer networks in Urdu

### Assessment Methods
- Assignments (25%)
- Lab reports (25%)
- Midterm exam (25%)
- Final exam (25%)

---

## Operating Systems

### Overview
Study of operating system concepts: process management, memory management, file systems, and concurrency. Includes hands-on Linux system programming.

### Learning Objectives
- Understand OS structures and services
- Manage processes and threads, implement scheduling algorithms
- Synchronize concurrent processes using semaphores, mutexes, monitors
- Analyze memory management: paging, segmentation, virtual memory
- Understand file systems and I/O management
- Write systems-level programs in C (Linux)

### Detailed Topics
- **Module 1:** OS Overview: evolution, types, system calls, OS structure (monolithic, microkernel, hybrid)
- **Module 2:** Process Management: PCB, process states, context switching, fork/exec, process creation in Linux
- **Module 3:** Threads: multithreading models, pthreads, thread synchronization
- **Module 4:** CPU Scheduling: FCFS, SJF, SRTF, Round Robin, priority, MLFQ
- **Module 5:** Process Synchronization: critical section, mutex, semaphore, monitor, classical problems (bounded buffer, readers-writers, dining philosophers)

### YouTube Channels (English)
- **Neso Academy:** Operating systems full course
- **freeCodeCamp.org:** Operating systems full course
- **TechWithTim:** OS concepts, Linux system programming
- **Brian Will:** OS fundamentals
- **Udacity:** Introduction to Operating Systems (Georgia Tech)
- **OSTEP (YouTube):** Operating Systems: Three Easy Pieces video lectures

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** Operating systems, process management — https://youtube.com/ @GateSmashers 
- **KnowledgeGate (Hindi):** OS, memory management — https://youtube.com/ @KnowledgeGate 
- **Neso Academy (Hindi):** Operating systems in Hindi
- **EduPoint (Hindi):** OS concepts, scheduling
- **Technical Gyan (Hindi):** Linux, OS concepts
- **Engineering in Hindi (Hindi):** Operating systems fundamentals
- **Simple Snippets (Hindi):** OS, process synchronization, memory management

### Software Tools
- **Linux (Ubuntu/CentOS)** — Programming environment
- **GCC** — C compiler
- **GDB** — Debugger
- **Valgrind** — Memory debugging
- **VirtualBox / VMware** — Virtual machines

### Assessment Methods
- Programming assignments (Real Linux, pthreads) (30%)
- Quizzes (15%)
- Midterm exam (25%)
- Final exam (30%)

---

## Microprocessors and Assembly Language

### Overview
Study of microprocessor architecture, assembly language programming, and interfacing. Focuses on the 8086/8088 microprocessor family.

### Learning Objectives
- Understand 8086 microprocessor architecture: registers, buses, memory segmentation
- Write assembly language programs for the 8086
- Interface memory and I/O devices with the microprocessor
- Program peripheral chips: 8255 PPI, 8253/8254 timer, 8259 PIC, 8251 USART
- Understand interrupt handling and DMA
- Design microprocessor-based systems

### Detailed Topics
- **Module 1:** 8086 Architecture: execution unit (EU), bus interface unit (BIU), registers, segmentation, physical address generation, pin diagram
- **Module 2:** 8086 Instruction Set: data transfer, arithmetic, logical, shift/rotate, branch, string, processor control instructions
- **Module 3:** 8086 Assembly Programming: addressing modes, assembler directives, procedures, macros, interrupts, software interrupts
- **Module 4:** Memory Interfacing: memory types (SRAM, DRAM, EPROM), address decoding, timing diagrams, memory map
- **Module 5:** I/O Interfacing: I/O ports, I/O instructions, I/O address decoding, programmed I/O, interrupt-driven I/O, DMA
- **Module 6:** 8255 Programmable Peripheral Interface (PPI): modes of operation, interfacing with keyboard, display, ADC, DAC
- **Module 7:** 8253/8254 Programmable Interval Timer: modes, square wave generation, event counting, frequency measurement
- **Module 8:** 8259 Programmable Interrupt Controller (PIC): interrupt handling, cascading, priority modes
- **Module 9:** 8251 USART: serial communication, asynchronous/synchronous modes, baud rate generation
- **Module 10:** Advanced Topics: 8086-based system design, 8087 math coprocessor, introduction to 80386/80486, Pentium

### Books
- **"Microprocessor Architecture, Programming, and Applications with the 8085"** by Ramesh S. Gaonkar (Penram, 2013)
- **"Microprocessors and Interfacing"** by N. Senthil Kumar, M. Saravanan, and S. Jeevananthan (Oxford, 2012)
- **"The 8088 and 8086 Microprocessors: Programming, Interfacing, Software, Hardware, and Applications, 4th Edition"** by Walter A. Triebel and Avtar Singh (Pearson, 2002)

### Software Tools
- **EMU8086** (8086 emulator)
- **MASM/TASM** (assemblers)
- **Proteus** (circuit simulation)
- **Vim/VS Code** (code editor)

### YouTube Channels (English)
- **Neso Academy:** Microprocessors, 8086 architecture
- **ALL ABOUT ELECTRONICS:** Microprocessor fundamentals
- **Sundeep Saradhi Kanthety:** 8086 programming, assembly language
- **Education 4u:** Microprocessor 8086, assembly programming
- **Tutorials Point:** Microprocessor 8086

### YouTube Channels (Hindi/Urdu)
- **Technical Gyan (Hindi):** 8086 microprocessor, assembly programming
- **EduPoint (Hindi):** Microprocessor 8086, interfacing
- **Gate Smashers (Hindi):** Microprocessor, assembly language — https://youtube.com/ @GateSmashers 
- **KnowledgeGate (Hindi):** Microprocessor, 8086 — https://youtube.com/@KnowledgeGate 
- **Engineering in Hindi (Hindi):** Microprocessor architecture
- **Electronics in Hindi (Hindi):** 8086, peripheral interfacing
- **Easy Engineering (Hindi):** Microprocessor, assembly language

### Lab Work
- **Lab 1:** 8086 assembly programming: arithmetic, data transfer
- **Lab 2:** 8086 assembly: loops, procedures, macros
- **Lab 3:** 8086 string operations and interrupt programming
- **Lab 4:** Memory interfacing and address decoding
- **Lab 5:** 8255 PPI: LED and switch interfacing
- **Lab 6:** 8253/8254 timer: frequency generation
- **Lab 7:** 8259 PIC: interrupt handling
- **Lab 8:** ADC/DAC interfacing with 8086

### Assessment Methods
- Assembly programming assignments (25%)
- Lab reports (25%)
- Midterm exam (25%)
- Final exam (25%)

---

## Digital Signal Processing

### Overview
Study of digital signal processing fundamentals: discrete-time signals, DFT/FFT, digital filter design, and real-time processing applications.

### Learning Objectives
- Understand discrete-time signals and systems
- Apply Z-transform and DFT/FFT for signal analysis
- Design FIR and IIR digital filters
- Implement DSP algorithms using MATLAB/Python
- Understand real-time DSP applications

### Detailed Topics
- **Module 1:** Discrete-Time Signals: sampling, quantization, discrete-time sequences, basic operations
- **Module 2:** Discrete-Time Systems: LTI systems, difference equations, impulse response, convolution, stability, causality
- **Module 3:** Z-Transform: ROC, properties, inverse Z-transform, system function, pole-zero analysis
- **Module 4:** Discrete Fourier Transform (DFT): definition, properties, linear/circular convolution, frequency-domain sampling
- **Module 5:** Fast Fourier Transform (FFT): radix-2 DIT-FFT, DIF-FFT, computational complexity, applications
- **Module 6:** FIR Filter Design: window method (rectangular, Hamming, Hanning, Blackman, Kaiser), frequency sampling method, optimal equiripple design (Parks-McClure)
- **Module 7:** IIR Filter Design: analog filter prototypes (Butterworth, Chebyshev, Elliptic), bilinear transformation, impulse invariance, frequency transformations
- **Module 8:** Filter Implementation: direct form I/II, cascade, parallel, finite word-length effects, quantization
- **Module 9:** Multirate DSP: decimation, interpolation, polyphase filters, filter banks
- **Module 10:** Applications: audio processing, speech processing, image processing, radar, communications

### Books
- **"Digital Signal Processing: Principles, Algorithms, and Applications, 4th Edition"** by Proakis and Manolakis (Pearson, 2006)
- **"Digital Signal Processing: A Practical Guide for Engineers and Scientists"** by Steven W. Smith (Newnes, 2002) — Free online (DSPGuide.com)
- **"Understanding Digital Signal Processing, 3rd Edition"** by Richard G. Lyons (Pearson, 2010)
- **"Discrete-Time Signal Processing, 3rd Edition"** by Oppenheim and Schafer (Pearson, 2009)

### Software Tools
- **MATLAB** (Signal Processing Toolbox, DSP System Toolbox)
- **Python:** NumPy, SciPy (signal), Matplotlib
- **GNU Octave**
- **GNU Radio** (SDR processing)

### YouTube Channels (English)
- **Mike X Cohen:** DSP, signal processing tutorials
- **Neso Academy:** Digital signal processing
- **MATLAB (Official):** DSP tutorials using MATLAB
- **freeCodeCamp.org:** Digital signal processing course
- **Brian Douglas:** Control systems, DSP fundamentals
- **David Dorran:** DSP tutorials, filter design

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** DSP, DFT, FFT — https://youtube.com/ @GateSmashers 
- **KnowledgeGate (Hindi):** Digital signal processing — https://youtube.com/ @KnowledgeGate 
- **EduPoint (Hindi):** DSP, filter design, Z-transform
- **Neso Academy (Hindi):** DSP in Hindi
- **Engineering in Hindi (Hindi):** Signal processing, FFT
- **Simple Engineering (Hindi/Urdu):** DSP fundamentals in bilingual
- **Electronics in Hindi (Hindi):** DSP, digital filters

### Lab Work
- **Lab 1:** Discrete-time signal generation and visualization
- **Lab 2:** Convolution and correlation
- **Lab 3:** DFT and FFT computation
- **Lab 4:** FIR filter design (window method)
- **Lab 5:** IIR filter design (Butterworth, Chebyshev)
- **Lab 6:** Audio processing: filtering, equalization, effects

### Assessment Methods
- Problem sets (20%)
- MATLAB/Python assignments (30%)
- Midterm exam (25%)
- Final exam (25%)

---

## Engineering Economics

### Overview
Study of economic principles for engineering decision-making. Covers cost analysis, time value of money, project evaluation, and financial management.

### Learning Objectives
- Understand time value of money and interest formulas
- Evaluate engineering projects using NPV, IRR, payback period, benefit-cost ratio
- Perform cost estimation and break-even analysis
- Understand depreciation, taxes, and inflation
- Apply decision-making under uncertainty

### Detailed Topics
- **Module 1:** Engineering Economics Fundamentals: role of economics in engineering, types of costs (fixed, variable, direct, indirect, sunk, opportunity)
- **Module 2:** Time Value of Money: simple interest, compound interest, effective interest rate, present/future worth, uniform series, gradient series, geometric series
- **Module 3:** Project Evaluation: net present value (NPV), internal rate of return (IRR), payback period, benefit-cost ratio, profitability index
- **Module 4:** Comparison of Alternatives: present worth analysis, annual worth analysis, rate of return analysis, incremental analysis
- **Module 5:** Depreciation: straight-line, declining balance, sum-of-years digits, MACRS
- **Module 6:** Taxes: corporate tax, capital gains, after-tax analysis
- **Module 7:** Inflation: consumer price index, constant dollars, inflation-adjusted analysis
- **Module 8:** Cost Estimation: learning curves, cost indices, parametric estimation, engineering estimates
- **Module 9:** Break-Even Analysis: break-even point, profit-volume analysis, sensitivity analysis
- **Module 10:** Decision-Making Under Uncertainty: expected value, decision trees, risk analysis, Monte Carlo simulation

### Books
- **"Engineering Economy, 17th Edition"** by William G. Sullivan, Elin M. Wicks, and C. Patrick Koelling (Pearson, 2018)
- **"Engineering Economics: Financial Decision Making for Engineers, 6th Edition"** by Niall M. Fraser, Elizabeth M. Jewkes, and Mehrdad Pirnia (Pearson, 2012)
- **"Principles of Engineering Economic Analysis, 6th Edition"** by White, Case, and Pratt (Wiley, 2012)

### Software Tools
- **Microsoft Excel** (financial functions: NPV, IRR, PMT, FV)
- **MATLAB** (financial toolbox)
- **Python** (NumPy financial functions)

### YouTube Channels (English)
- **Engineering Economics Guy:** Engineering economy, NPV, IRR
- **IIT Madras (NPTEL):** Engineering Economics
- **Neso Academy:** Engineering economics
- **Corporate Finance Institute:** Project evaluation, financial analysis
- **Edspira:** Accounting, finance, economics
- **The Engineering Mindset:** Engineering economics basics

### YouTube Channels (Hindi/Urdu)
- **EduPoint (Hindi):** Engineering economics, cost analysis
- **Guru99 (Hindi):** Engineering economy, NPV, IRR
- **Management in Hindi (Hindi):** Engineering economics, project evaluation
- **Economics in Hindi (Hindi):** Engineering economics fundamentals
- **Finance Hindi (Hindi):** Time value of money, cost analysis
- **Professional Development (Hindi/Urdu):** Engineering economics, decision making
- **Urdu Tutorials (Urdu):** Engineering economics in Urdu

### Assessment Methods
- Problem sets (30%)
- Case study analysis (20%)
- Midterm exam (25%)
- Final exam (25%)
