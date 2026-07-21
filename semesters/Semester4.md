<!--
Mentorship Context: CS Mentor
Skill: cs-mentor
Feedback Log: ../cs-mentor/references/feedback_log.md
-->

# Semester 4: Data Structures & Systems

## Numerical Methods

### Overview
Study of numerical techniques for solving mathematical problems that are difficult or impossible to solve analytically. Covers numerical solutions to equations, interpolation, numerical integration/differentiation, solving systems of linear equations, and numerical solutions to ordinary differential equations. Emphasizes implementation in MATLAB/Python.

### Learning Objectives
- Understand error analysis: round-off error, truncation error, numerical stability
- Solve nonlinear equations using iterative methods (bisection, Newton-Raphson, secant)
- Solve systems of linear equations using direct and iterative methods
- Perform interpolation and curve fitting for data approximation
- Apply numerical differentiation and integration techniques
- Solve ordinary differential equations numerically (initial value problems, boundary value problems)
- Implement numerical methods in MATLAB and Python

### Detailed Topics
- **Module 1:** Error Analysis: significant figures, accuracy, precision, round-off error, truncation error, error propagation, stability, conditioning
- **Module 2:** Root Finding: bisection method, false position method, Newton-Raphson method, secant method, fixed-point iteration, convergence criteria, multiple roots
- **Module 3:** Systems of Linear Equations: Gaussian elimination with partial pivoting, LU decomposition, Cholesky decomposition, Thomas algorithm (tridiagonal systems), Jacobi method, Gauss-Seidel method, SOR
- **Module 4:** Matrix Eigenvalue Problems: power method, inverse power method, QR algorithm, eigenvalue applications
- **Module 5:** Interpolation: Lagrange interpolation, Newton's divided differences, Hermite interpolation, cubic spline interpolation, piecewise interpolation
- **Module 6:** Curve Fitting: least squares regression (linear, polynomial, multiple), nonlinear regression, weighted least squares, QR decomposition
- **Module 7:** Numerical Differentiation: finite difference formulas (forward, backward, central), higher-order derivatives, Richardson extrapolation
- **Module 8:** Numerical Integration: Newton-Cotes formulas (trapezoidal rule, Simpson's 1/3 rule, Simpson's 3/8 rule), Romberg integration, Gaussian quadrature, adaptive quadrature
- **Module 9:** Numerical Solutions of ODEs (Initial Value Problems): Euler's method, improved Euler, Runge-Kutta (RK2, RK4), multi-step methods (Adams-Bashforth, Adams-Moulton), predictor-corrector, stability analysis, stiff ODEs
- **Module 10:** Numerical Solutions of ODEs (Boundary Value Problems): shooting method, finite difference method, applications to engineering problems
- **Module 11:** Partial Differential Equations (introductory): finite difference methods for elliptic (Laplace, Poisson), parabolic (heat equation), hyperbolic (wave equation) PDEs

### Books
- **"Numerical Methods for Engineers, 8th Edition"** by Steven C. Chapra and Raymond P. Canale (McGraw-Hill, 2021) — Standard engineering text
- **"Numerical Analysis, 10th Edition"** by Richard L. Burden, J. Douglas Faires, and Annette M. Burden (Cengage, 2015) — Theoretical, rigorous
- **"Applied Numerical Methods with MATLAB for Engineers and Scientists, 4th Edition"** by Steven C. Chapra (McGraw-Hill, 2017) — MATLAB-focused
- **"Numerical Methods using Python"** by John D. Lambert (free online resources)

### Online Resources
- **MIT OCW 18.335:** Numerical Methods (Prof. Steven G. Johnson)
- **MIT OCW 2.993:** Numerical Methods in Engineering
- **3Blue1Brown (YouTube):** Numerical methods visualization
- **Numerical Methods for Engineers (YouTube):** Chapra's lectures

### YouTube Channels (English)
- **3Blue1Brown:** Numerical methods visualization
- **Numerical Methods for Engineers:** Chapra's lectures
- **The Math Guy:** Numerical analysis tutorials
- **MIT OpenCourseWare:** Numerical methods (18.335)
- **Professor Leonard:** Numerical methods, ODEs
- **Numerical Analysis:** Full course lectures

### YouTube Channels (Hindi/Urdu)
- **Bhagwan Singh (Hindi):** Numerical methods, engineering math — https://youtube.com/@BhagwanSinghVishwakarma
- **Gajendra Purohit (Hindi):** Numerical methods, interpolation — https://youtube.com/@DrGajendraPurohit
- **Manoj Chauhan (Hindi):** Numerical methods, engineering math
- **EduPoint (Hindi):** Numerical methods, root finding
- **Physics Wallah — Math (Hindi):** Numerical methods, ODEs
- **Jaipal Vishwakarma (Hindi):** Numerical methods, numerical integration
- **Engineering Mathematics (Hindi):** Numerical methods in Hindi
- **The Learnyn (Hindi/Urdu):** Numerical methods in bilingual format

### Software Tools
- **MATLAB** (primary tool — matrix operations, numerical computing, visualization)
- **Python:** NumPy, SciPy (optimize, integrate, interpolate, linalg, sparse), Matplotlib
- **GNU Octave** (open-source MATLAB alternative)
- **Wolfram Mathematica** (symbolic and numerical computation)
- **R** (statistical computing)

### Practical Projects
- **Project 1:** Implement root-finding algorithms and compare convergence rates
- **Project 2:** Solve a system of linear equations using LU decomposition and Gauss-Seidel
- **Project 3:** Fit a curve to experimental data using least squares regression
- **Project 4:** Numerical integration: compute the area under a curve using multiple methods
- **Project 5:** Solve a spring-mass-damper ODE system using Runge-Kutta
- **Project 6:** Solve the heat equation (1D parabolic PDE) using finite differences

### Assessment Methods
- Problem sets (25%)
- MATLAB/Python programming assignments (30%)
- Midterm exam (20%)
- Final exam (25%)

---

## Data Structures and Algorithms

### Overview
Comprehensive study of fundamental data structures and algorithms. Covers linear and non-linear data structures, sorting, searching, and algorithm analysis. Emphasizes implementation in C/C++.

### Learning Objectives
- Analyze algorithm efficiency using asymptotic notation (big-O, big-Theta, big-Omega)
- Implement linear data structures: arrays, linked lists, stacks, queues
- Implement non-linear data structures: trees, graphs, hash tables
- Implement sorting and searching algorithms
- Understand algorithm design techniques: divide-and-conquer, greedy, dynamic programming
- Apply data structures to solve real-world problems

### Detailed Topics
- **Module 1:** Algorithm Analysis: time/space complexity, asymptotic notation, recurrence relations, Master theorem
- **Module 2:** Arrays and Strings: static/dynamic arrays, multidimensional arrays, string algorithms, pattern matching (Naive, KMP, Boyer-Moore)
- **Module 3:** Linked Lists: singly, doubly, circular linked lists, operations (insert, delete, search, reverse), applications
- **Module 4:** Stacks: array-based, linked-list-based, applications (expression evaluation, parentheses matching, undo/redo)
- **Module 5:** Queues: FIFO, circular queues, priority queues, dequeues, applications (scheduling, BFS)
- **Module 6:** Trees: binary trees, binary search trees (BST), tree traversal (inorder, preorder, postorder, level-order), BST operations, balanced BST (AVL, Red-Black introduction)
- **Module 7:** Heaps: max-heap, min-heap, heap operations, heap sort, priority queue implementation
- **Module 8:** Graphs: representations (adjacency matrix, adjacency list), BFS, DFS, topological sort, shortest paths (Dijkstra, Bellman-Ford), MST (Kruskal, Prim)
- **Module 9:** Hashing: hash functions, collision resolution (chaining, open addressing), load factor, rehashing, hash table applications
- **Module 10:** Sorting: comparison-based (bubble, selection, insertion, merge, quick, heap) and non-comparison (counting, radix, bucket)
- **Module 11:** Searching: linear search, binary search, interpolation search, searching in trees and graphs
- **Module 12:** Algorithm Design: divide-and-conquer (merge sort, quick sort), greedy (Huffman, activity selection), dynamic programming (Fibonacci, knapsack, LCS)

### Books
- **"Introduction to Algorithms, 4th Edition"** (CLRS) by Cormen, Leiserson, Rivest, and Stein (MIT Press, 2022)
- **"Data Structures and Algorithm Analysis in C++, 4th Edition"** by Mark Allen Weiss (Pearson, 2013)
- **"Algorithms in C++, Parts 1-5"** by Robert Sedgewick (Addison-Wesley, 2001)
- **"Cracking the Coding Interview, 6th Edition"** by Gayle Laakmann McDowell (CareerCup, 2015) — Interview-focused

### Online Resources
- **MIT OCW 6.006:** Introduction to Algorithms
- **Princeton Algorithms, Part I & II (Coursera):** Robert Sedgewick
- **GeeksforGeeks:** Data Structures
- **Programiz:** DSA tutorials

### YouTube Channels (English)
- **Abdul Bari:** Algorithm design and analysis
- **William Fiset:** Data structures (Java/C++)
- **freeCodeCamp.org:** Data structures full course
- **CS Dojo:** DSA concepts
- **Jenny's Lectures:** DSA, algorithms, data structures
- **mycodeschool:** DSA fundamentals (classic)
- **Back To Back SWE:** Algorithm design, coding interviews
- **Nick White:** LeetCode DSA solutions

### YouTube Channels (Hindi/Urdu)
- **CodeWithHarry (Hindi):** DSA full course in Hindi — https://youtube.com/@CodeWithHarry
- **Apna College (Hindi):** DSA in Hindi, placement preparation — https://youtube.com/@ApnaCollegeOfficial
- **Love Babbar (Hindi):** DSA, competitive programming — https://youtube.com/@LoveBabbar
- **Gate Smashers (Hindi):** DSA, algorithm analysis — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Data structures, algorithms — https://youtube.com/@KnowledgeGate
- **Anuj Bhaiya (Hindi):** DSA for placements, algorithms
- **Saurabh Shukla (MySirG) (Hindi):** DSA concepts
- **Simple Snippets (Hindi):** Data structures, algorithms
- **Urdu IT Academy (Urdu):** DSA in Urdu language

### Practice Platforms
- **LeetCode** (DSA problems)
- **HackerRank** (Data Structures, Algorithms)
- **Codeforces**
- **CSES Problem Set**
- **GeeksforGeeks** (practice problems)

### Assessment Methods
- Programming assignments (30%)
- Quizzes (15%)
- Midterm exam (25%)
- Final exam (30%)

---

## Computer Architecture and Organizations

### Overview
Study of computer organization and architecture, from CPU design to memory hierarchy. Covers instruction set architecture, datapath, control unit, pipelining, and memory systems.

### Learning Objectives
- Understand computer organization basics: CPU, memory, I/O, buses
- Analyze instruction set architecture (ISA) and addressing modes
- Design CPU datapath and control unit (single-cycle, multi-cycle)
- Understand pipelining, hazards, and performance analysis
- Understand memory hierarchy: cache, virtual memory, storage
- Analyze computer performance using CPI, Amdahl's Law

### Detailed Topics
- **Module 1:** Computer Organization Basics: von Neumann architecture, Harvard architecture, system bus, clock, performance metrics
- **Module 2:** Instruction Set Architecture: MIPS/RISC-V, instruction formats (R-type, I-type, J-type), addressing modes, RISC vs. CISC
- **Module 3:** Assembly Language: arithmetic, logic, branching, looping, function calls, stack, recursion
- **Module 4:** CPU Datapath: register file, ALU, program counter, instruction memory, data memory, single-cycle implementation
- **Module 5:** Control Unit: hardwired control, microprogrammed control, control signals, ALU control
- **Module 6:** Pipelining: 5-stage pipeline, pipeline registers, data hazards (forwarding, stalling), control hazards (branch prediction, delayed branching)
- **Module 7:** Memory Hierarchy: SRAM, DRAM, cache organization (direct-mapped, set-associative, fully-associative), cache performance, locality, write policies
- **Module 8:** Virtual Memory: paging, page tables, TLB, address translation, page replacement (FIFO, LRU, Optimal)
- **Module 9:** I/O Systems: memory-mapped I/O, interrupt-driven I/O, DMA, buses, storage (HDD, SSD, RAID)
- **Module 10:** Performance Analysis: CPI, execution time, Amdahl's Law, SPEC benchmarks, superscalar, out-of-order execution

### Books
- **"Computer Organization and Design: The Hardware/Software Interface, RISC-V Edition"** by Patterson and Hennessy (Morgan Kaufmann, 2021)
- **"Computer Architecture: A Quantitative Approach, 7th Edition"** by Hennessy and Patterson (Morgan Kaufmann, 2023)
- **"Digital Design and Computer Architecture, 2nd Edition"** by Harris and Harris (Morgan Kaufmann, 2012)
- **"Computer Systems: A Programmer's Perspective, 3rd Edition"** by Bryant and O'Hallaron (Pearson, 2016)

### Online Resources
- **MIT OCW 6.004:** Computation Structures
- **UC Berkeley CS61C:** Great Ideas in Computer Architecture
- **Onur Mutlu (YouTube):** Digital Design & Computer Architecture lectures

### YouTube Channels (English)
- **Onur Mutlu:** Digital Design & Computer Architecture (ETH Zurich)
- **David Black-Schaffer:** Computer Architecture tutorials
- **MIT 6.004 (YouTube):** Computation Structures
- **UC Berkeley CS61C:** Great Ideas in Computer Architecture
- **Easy Engineering:** Computer architecture, organization
- **Neso Academy:** Computer organization and architecture

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** Computer architecture, organization — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Computer architecture, COA — https://youtube.com/@KnowledgeGate
- **Neso Academy (Hindi):** Computer organization, architecture
- **EduPoint (Hindi):** Computer architecture, CPU design
- **Technical Gyan (Hindi):** Computer hardware, architecture
- **Engineering in Hindi (Hindi):** COA, computer organization
- **Easy Engineering (Hindi):** Computer architecture, pipelining
- **Urdu IT Academy (Urdu):** Computer architecture in Urdu

### Software Tools
- **RARS/RISC-V Simulator** (assembly programming)
- **MARS MIPS Simulator**
- **Logisim Evolution** (CPU component design)
- **gem5** (architecture simulator)

### Lab Work
- **Lab 1:** RISC-V assembly programming
- **Lab 2:** ALU design in Logisim
- **Lab 3:** Single-cycle CPU datapath design
- **Lab 4:** Pipeline simulation and hazard detection
- **Lab 5:** Cache simulation and performance analysis

### Assessment Methods
- Assignments (25%)
- Labs (25%)
- Midterm exam (25%)
- Final exam (25%)

---

## Signals and Systems

### Overview
Study of continuous-time and discrete-time signals and systems. Covers time-domain and frequency-domain analysis, Fourier transforms, Laplace transforms, and Z-transforms.

### Learning Objectives
- Classify signals and systems (continuous/discrete, LTI, causal, stable)
- Analyze LTI systems using convolution and impulse response
- Apply Fourier series and Fourier transforms for signal analysis
- Apply Laplace transforms and Z-transforms for system analysis
- Understand sampling theorem and its implications
- Analyze system stability and causality

### Detailed Topics
- **Module 1:** Introduction to Signals: continuous vs. discrete, periodic vs. aperiodic, even/odd, energy/power signals
- **Module 2:** Systems: classification, LTI systems, impulse response, step response, causality, stability
- **Module 3:** Convolution: continuous-time convolution, discrete-time convolution, properties, graphical interpretation
- **Module 4:** Fourier Series: trigonometric and exponential forms, convergence, Gibbs phenomenon, frequency spectrum
- **Module 5:** Fourier Transform: definition, properties, Fourier transform pairs, Parseval's theorem
- **Module 6:** Laplace Transform: ROC, properties, inverse Laplace, system analysis (transfer function, poles, zeros, stability)
- **Module 7:** Z-Transform: ROC, properties, inverse Z-transform, system analysis for discrete systems
- **Module 8:** Sampling Theorem: Nyquist rate, aliasing, reconstruction, quantization
- **Module 9:** Discrete-Time Fourier Transform (DTFT) and DFT: properties, FFT algorithm

### Books
- **"Signals and Systems, 2nd Edition"** by Oppenheim, Willsky, and Nawab (Pearson, 1996)
- **"Signals and Systems: A MATLAB Integrated Approach"** by Oktay Alkin (CRC Press, 2014)
- **"Digital Signal Processing, 4th Edition"** by Proakis and Manolakis (Pearson, 2006)

### Online Resources
- **MIT OCW 6.003:** Signals and Systems (Prof. Oppenheim)
- **3Blue1Brown:** Fourier Transform series
- **Michael van Biezen (YouTube):** Signals and systems

### YouTube Channels (English)
- **Michael van Biezen:** Signals and systems, Fourier, Laplace
- **MIT 6.003 (YouTube):** Signals and Systems (Prof. Oppenheim)
- **3Blue1Brown:** Fourier Transform visualized
- **Neso Academy:** Signals and systems
- **Tutorials Point:** Signals and systems lectures
- **The Organic Chemistry Tutor:** Laplace, Fourier transforms
- **Professor Leonard:** Laplace transforms, differential equations

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** Signals and systems, transforms — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Signals, systems, Fourier — https://youtube.com/@KnowledgeGate
- **EduPoint (Hindi):** Signals and systems, Laplace, Fourier
- **Bhagwan Singh (Hindi):** Signals, systems, transforms
- **Gajendra Purohit (Hindi):** Signals, systems, Fourier series
- **Engineering in Hindi (Hindi):** Signals and systems
- **Simple Engineering (Hindi/Urdu):** Signals and systems in bilingual

### Software Tools
- **MATLAB** (Signal Processing Toolbox)
- **Python:** NumPy, SciPy (signal), Matplotlib
- **GNU Octave**

### Assessment Methods
- Problem sets (25%)
- MATLAB/Python assignments (25%)
- Midterm exam (25%)
- Final exam (25%)

---

## Complex Variables and Transforms

### Overview
Study of complex analysis and integral transforms. Covers complex numbers, analytic functions, contour integration, and advanced transform methods.

### Learning Objectives
- Perform operations with complex numbers and understand complex functions
- Understand analytic functions, Cauchy-Riemann equations, and harmonic functions
- Evaluate complex integrals using Cauchy's theorem and residue theorem
- Apply Fourier and Laplace transforms to engineering problems
- Understand conformal mapping and its applications

### Detailed Topics
- **Module 1:** Complex Numbers: arithmetic, polar form, De Moivre's theorem, roots, complex exponential
- **Module 2:** Complex Functions: limits, continuity, differentiation, analytic functions, Cauchy-Riemann equations
- **Module 3:** Elementary Functions: exponential, trigonometric, hyperbolic, logarithmic, power functions
- **Module 4:** Complex Integration: contour integrals, Cauchy's theorem, Cauchy's integral formula, derivatives
- **Module 5:** Series: Taylor series, Laurent series, radius of convergence, singularities
- **Module 6:** Residue Theorem: residues, evaluation of real integrals, improper integrals, trigonometric integrals
- **Module 7:** Conformal Mapping: mapping properties, Möbius transformations, applications to boundary value problems
- **Module 8:** Fourier and Laplace Transforms (Advanced): applications to differential equations, signal processing

### Books
- **"Complex Variables and Applications, 9th Edition"** by Brown and Churchill (McGraw-Hill, 2013) — Standard text
- **"Complex Analysis: A First Course with Applications, 3rd Edition"** by Dennis G. Zill (Jones & Bartlett, 2014)
- **"Advanced Engineering Mathematics, 10th Edition"** by Erwin Kreyszig (Wiley, 2011)

### Online Resources
- **MIT OCW 18.04:** Complex Variables with Applications
- **3Blue1Brown:** Complex analysis visualization
- **Wolfram MathWorld:** Complex analysis

### YouTube Channels (English)
- **3Blue1Brown:** Complex analysis visualization
- **MIT OCW 18.04:** Complex Variables with Applications
- **Mathispower4u:** Complex analysis tutorials
- **Faculty of Khan:** Complex analysis, residues, contour integration
- **The Math Sorcerer:** Complex variables, complex analysis

### YouTube Channels (Hindi/Urdu)
- **Bhagwan Singh (Hindi):** Complex variables, transforms — https://youtube.com/@BhagwanSinghVishwakarma
- **Gajendra Purohit (Hindi):** Complex analysis, residues — https://youtube.com/@DrGajendraPurohit
- **Manoj Chauhan (Hindi):** Complex variables, engineering math
- **EduPoint (Hindi):** Complex analysis, contour integration
- **Physics Wallah — Math (Hindi):** Complex variables
- **Jaipal Vishwakarma (Hindi):** Complex analysis, transforms
- **The Learnyn (Hindi/Urdu):** Complex variables in bilingual format

### Assessment Methods
- Problem sets (30%)
- Midterm exam (30%)
- Final exam (40%)

---

## Engineering Project Management

### Overview
Introduction to project management principles and practices for engineering projects. Covers project lifecycle, planning, scheduling, resource management, risk management, and project documentation.

### Learning Objectives
- Understand project management frameworks (PMBOK, PRINCE2, Agile)
- Develop project plans, schedules, and budgets
- Apply project scheduling techniques (Gantt charts, CPM, PERT)
- Manage project resources, teams, and stakeholders
- Identify and manage project risks
- Use project management software tools

### Detailed Topics
- **Module 1:** Project Management Fundamentals: definition, project lifecycle, constraints (scope, time, cost, quality)
- **Module 2:** Project Initiation: project charter, stakeholder identification, feasibility study, project selection
- **Module 3:** Project Planning: work breakdown structure (WBS), activity definition, resource estimation, cost estimation
- **Module 4:** Project Scheduling: Gantt charts, network diagrams, critical path method (CPM), PERT, float/slack, critical chain
- **Module 5:** Resource Management: resource allocation, leveling, team building, responsibility assignment matrix (RAM)
- **Module 6:** Risk Management: risk identification, qualitative/quantitative analysis, risk response planning, risk monitoring
- **Module 7:** Project Execution and Monitoring: earned value management (EVM), performance metrics, change control, quality management
- **Module 8:** Agile Project Management: Scrum, Kanban, sprint planning, daily stand-ups, retrospectives
- **Module 9:** Project Closure: project handover, lessons learned, post-project evaluation, documentation
- **Module 10:** Project Management Software: Microsoft Project, Jira, Trello, Asana, Primavera

### Books
- **"A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7th Edition"** (PMI, 2021)
- **"Project Management: A Systems Approach to Planning, Scheduling, and Controlling, 12th Edition"** by Harold Kerzner (Wiley, 2017)
- **"Project Management for Engineering and Construction, 3rd Edition"** by Garold D. Oberlender (McGraw-Hill, 2014)
- **"Scrum: The Art of Doing Twice the Work in Half the Time"** by Jeff Sutherland (Crown Business, 2014)

### YouTube Channels (English)
- **Project Management Institute (PMI):** PMP, project management
- **The Agile Coach:** Scrum, Agile, Kanban
- **It's PM:** Project management tutorials
- **PMC Lounge:** PMP exam prep, project management
- **KnowledgeHut:** Agile, Scrum, project management
- **Simplilearn:** Project management, PMP, Agile

### YouTube Channels (Hindi/Urdu)
- **Guru99 (Hindi):** Project management, PMP in Hindi
- **IT Skills (Hindi):** Project management, Scrum in Hindi
- **Learn with Sam (Hindi):** PMP, project management
- **Management in Hindi (Hindi):** Project planning, scheduling
- **Agile Hindi (Hindi):** Scrum, Agile methodologies in Hindi
- **Professional Development (Hindi/Urdu):** Project management, leadership
- **Urdu Tutorials (Urdu):** Project management in Urdu

### Software Tools
- **Microsoft Project** (professional scheduling)
- **Jira** (Agile/Scrum project management)
- **Trello / Asana** (task management)
- **Primavera P6** (enterprise project management)
- **GanttProject** (free, open-source)

### Assessment Methods
- Project planning assignments (30%)
- Group project (project plan + presentation) (30%)
- Midterm exam (20%)
- Final exam (20%)
