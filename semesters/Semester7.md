# Semester 7: Mobile & Cloud Engineering

## Mobile App Development (Intro to .NET MAUI and MVVM)

### Overview
Introduction to mobile application development using .NET MAUI (Multi-platform App UI) and the MVVM (Model-View-ViewModel) architectural pattern. Covers cross-platform development for Android, iOS, Windows, and macOS.

### Learning Objectives
- Understand .NET MAUI framework and cross-platform development
- Implement MVVM architectural pattern with data binding
- Design responsive UIs using XAML
- Handle navigation, data persistence, and platform-specific features
- Access device capabilities (camera, GPS, sensors)
- Deploy and test applications on multiple platforms

### Detailed Topics
- **Module 1:** .NET MAUI Overview: history, architecture, vs. Xamarin.Forms, project structure, dotnet CLI
- **Module 2:** C# Advanced Topics: async/await, LINQ, dependency injection, delegates, events
- **Module 3:** XAML: syntax, elements, properties, layout containers (StackLayout, Grid, FlexLayout, AbsoluteLayout), styles, resources
- **Module 4:** MVVM Architecture: Model, View, ViewModel, data binding, INotifyPropertyChanged, ICommand, RelayCommand, messaging
- **Module 5:** Navigation: Shell navigation, routing, passing parameters, tab bars, flyout menus
- **Module 6:** Controls and UI: Label, Entry, Button, ListView, CollectionView, TableView, CarouselView, RefreshView, SwipeView
- **Module 7:** Data Persistence: Preferences, file system, SQLite database, Entity Framework Core
- **Module 8:** Services and Dependency Injection: HttpClient, REST API consumption, JSON serialization, HttpClientFactory
- **Module 9:** Platform-Specific Features: camera, GPS/location, accelerometer, gyroscope, battery, connectivity, secure storage
- **Module 10:** Testing and Deployment: unit testing, UI testing, app signing, publishing to App Store/Google Play

### Books
- **".NET MAUI in Action"** by Matt Goldman and Alexander Sklar (Manning, 2023)
- **"Enterprise Application Patterns using .NET MAUI"** by Microsoft (free e-book)
- **"XAML Developer Reference"** by Mamta Dalal and Ashish Ghoda (Microsoft Press, 2011)

### Online Resources
- **Microsoft Learn:** .NET MAUI learning path
- **.NET MAUI Documentation:** Official docs
- **David Ortinau (YouTube):** .NET MAUI tutorials
- **James Montemagno (YouTube):** Mobile development, Xamarin/.NET MAUI

### Software Tools
- **Visual Studio 2022** (Community/Professional)
- **.NET 8 SDK** (or latest)
- **Android Emulator** / **Windows Subsystem for Android**
- **Postman** (API testing)

### YouTube Channels (English)
- **James Montemagno:** .NET MAUI, Xamarin, mobile development
- **David Ortinau:** .NET MAUI tutorials, cross-platform dev
- **Gerald Versluis:** https://www.youtube.com/c/GeraldVersluis (.NET MAUI, English)
- **IAmTimCorey:** C#, .NET, MAUI fundamentals
- **Milan Jovanovic:** .NET MAUI, clean architecture
- **Daniel Hindrikes:** .NET MAUI, XAML, mobile UI
- **.NET MAUI Amazing Playlist:** https://www.youtube.com/playlist?list=PL18HZjtdIA4BLwroTGon1LfKkM_RDGdjd

### YouTube Channels (Hindi/Urdu)
- **Technical Sagar (Hindi):** Mobile app development, tech tutorials
- **Learn Coding (Hindi):** C#, .NET, mobile development
- **CodeWithHarry (Hindi):** App development, programming — https://youtube.com/@CodeWithHarry
- **Engineering in Hindi (Hindi):** Mobile app development fundamentals
- **Easy Tech (Hindi/Urdu):** Cross-platform mobile development
- **Urdu IT Academy (Urdu):** Mobile programming in Urdu

### Practical Projects
- **Project 1:** To-do app with MVVM and SQLite
- **Project 2:** Weather app (REST API, location services)
- **Project 3:** Expense tracker (charts, data visualization)
- **Project 4:** Social media feed app (CollectionView, images)
- **Final Project:** Full-stack mobile application (e.g., e-commerce, restaurant finder, fitness tracker)

### Assessment Methods
- Programming assignments (30%)
- Mobile app projects (30%)
- Midterm exam (20%)
- Final capstone project (20%)

---

## Digital Systems Design

### Overview
Advanced digital systems design using VHDL/Verilog, FPGA implementation, and system-level design. Covers advanced combinational/sequential circuits, finite state machines, and digital system design methodology.

### Learning Objectives
- Design complex digital systems using VHDL/Verilog
- Implement advanced digital circuits (multipliers, dividers, ALUs, memory controllers)
- Design and verify finite state machines
- Implement digital systems on FPGA boards
- Understand timing analysis, design constraints, and optimization
- Apply design-for-test (DFT) techniques

### Detailed Topics
- **Module 1:** Advanced HDL Concepts: VHDL/Verilog data types, operators, concurrent vs. sequential statements, generics, configurations, packages
- **Module 2:** Combinational Logic Design: adders (carry look-ahead, carry save), multipliers (Booth, Wallace tree), comparators, barrel shifters, priority encoders, ALU design
- **Module 3:** Sequential Logic Design: counters, shift registers, sequence generators, dividers, synchronizers, clock domain crossing (CDC)
- **Module 4:** Finite State Machines: Moore, Mealy, state encoding (binary, Gray, one-hot), FSM design examples (traffic light controller, vending machine, UART receiver)
- **Module 5:** Memory Design: RAM, ROM, FIFO, dual-port RAM, register files, memory controllers
- **Module 6:** FPGA Architecture: CLB, slices, LUTs, flip-flops, DSP slices, block RAM, I/O blocks, clock management (PLL, DCM, MMCM)
- **Module 7:** Design Examples: UART, SPI, I2C, VGA controller, keyboard controller, simple processor
- **Module 8:** Timing Analysis: setup/hold, static timing analysis (STA), timing constraints (SDC), clock skew, jitter
- **Module 9:** Design Optimization: area, speed, power optimization, retiming, pipelining, resource sharing
- **Module 10:** Verification and Testing: testbenches, self-checking testbenches, functional coverage, code coverage, DFT (scan chains, BIST)

### Books
- **"Digital Design and Computer Architecture, 2nd Edition"** by Harris and Harris (Morgan Kaufmann, 2012)
- **"FPGA Prototyping by VHDL Examples"** by Pong P. Chu (Wiley, 2008)
- **"Advanced Digital Design with the Verilog HDL, 2nd Edition"** by Michael D. Ciletti (Pearson, 2010)
- **"RTL Hardware Design Using VHDL"** by Pong P. Chu (Wiley, 2006)

### Software Tools
- **Vivado** (Xilinx/AMD) — Synthesis, simulation, implementation
- **Quartus Prime** (Intel/Altera)
- **ModelSim / QuestaSim** (simulation)
- **Icarus Verilog / GHDL** (open-source simulation)
- **GTKWave** (waveform viewer)

### Hardware
- **FPGA Boards:** Basys 3, Nexys A7, Arty A7 (Xilinx Artix-7)
- **DE10-Lite, DE0-Nano** (Intel/Altera)

### YouTube Channels (English)
- **Neso Academy:** Digital electronics, VHDL, Verilog
- **ALL ABOUT ELECTRONICS:** Digital logic, FPGA design
- **EEVblog:** FPGA, digital design, electronics
- **VHDL Guru:** VHDL and FPGA programming tutorials
- **FPGA4FUN:** FPGA design examples and tutorials
- **Digilent:** FPGA tutorials, Vivado, digital design

### YouTube Channels (Hindi/Urdu)
- **Gate Smashers (Hindi):** Digital systems, FPGA — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Digital design, VHDL — https://youtube.com/@KnowledgeGate
- **EduPoint (Hindi):** Digital systems, sequential circuits
- **Technical Gyan (Hindi):** Digital systems, FPGA basics
- **Electronics in Hindi (Hindi):** Digital design, VHDL, Verilog
- **Easy Engineering (Hindi):** Digital systems, FPGA design

### Lab Work
- **Lab 1:** HDL design of combinational circuits (adder, multiplier, ALU)
- **Lab 2:** HDL design of sequential circuits (counters, shift registers, sequence detector)
- **Lab 3:** FSM design: traffic light controller
- **Lab 4:** UART transmitter/receiver design
- **Lab 5:** VGA controller design
- **Lab 6:** FPGA synthesis, implementation, and board programming
- **Final Project:** Simple processor design (RISC-V or custom ISA)

### Assessment Methods
- HDL assignments (25%)
- Lab reports (25%)
- Midterm exam (20%)
- Final project (30%)

---

## Engineering Entrepreneurship

### Overview
Study of entrepreneurship principles for engineering and technology ventures. Covers opportunity identification, business model development, startup finance, and technology commercialization.

### Learning Objectives
- Identify and evaluate technology-based business opportunities
- Develop business models using Lean Startup and Business Model Canvas
- Understand startup finance: funding, valuation, revenue models
- Create a business plan and pitch deck
- Understand intellectual property (patents, trademarks, copyrights)
- Navigate the startup ecosystem (incubators, accelerators, venture capital)

### Detailed Topics
- **Module 1:** Entrepreneurial Mindset: characteristics of entrepreneurs, creativity, innovation, risk-taking
- **Module 2:** Opportunity Identification: problem-solution fit, market research, customer discovery, MVP
- **Module 3:** Business Model Canvas: value proposition, customer segments, channels, revenue streams, cost structure, key partners
- **Module 4:** Lean Startup Methodology: build-measure-learn, validated learning, pivot vs. persevere
- **Module 5:** Intellectual Property: patents, trademarks, copyrights, trade secrets, licensing, IP strategy
- **Module 6:** Startup Finance: bootstrapping, angel investors, venture capital, crowdfunding, revenue models (SaaS, freemium, subscription)
- **Module 7:** Financial Projections: revenue forecasting, cost estimation, break-even analysis, valuation methods (DCF, comparables)
- **Module 8:** Pitching and Fundraising: pitch deck creation, elevator pitch, investor meetings, term sheets
- **Module 9:** Technology Commercialization: university tech transfer, spin-offs, technology licensing
- **Module 10:** Legal and Regulatory: company formation, incorporation, contracts, employment law, compliance

### Books
- **"The Lean Startup"** by Eric Ries (Crown Business, 2011)
- **"Business Model Generation"** by Osterwalder and Pigneur (Wiley, 2010)
- **"The Startup Owner's Manual"** by Blank and Dorf (K&S Ranch, 2012)
- **"Zero to One"** by Peter Thiel (Crown Business, 2014)

### YouTube Channels (English)
- **Y Combinator:** Startup school, fundraising, growth
- **Stanford eCorner:** Entrepreneurship lectures, innovation
- **Harvard Innovation Labs:** Startup resources, pitching
- **How to Start a Startup (Stanford):** Lectures by Sam Altman, Paul Graham
- **The Lean Startup (Eric Ries):** Lean methodology talks
- **Startup Grind:** Founder interviews, entrepreneurship

### YouTube Channels (Hindi/Urdu)
- **EduPoint (Hindi):** Entrepreneurship, business concepts
- **Management in Hindi (Hindi):** Entrepreneurship, business planning
- **Technical Sagar (Hindi):** Startup ecosystem, tech entrepreneurship
- **Finance Hindi (Hindi):** Startup finance, funding
- **Professional Development (Hindi/Urdu):** Entrepreneurship, career development
- **Urdu Tutorials (Urdu):** Entrepreneurship in Urdu

### Assessment Methods
- Business model canvas (20%)
- Market research report (20%)
- Pitch deck and presentation (30%)
- Business plan (30%)

---

## Cloud and Distributed Computing

### Overview
Study of cloud computing and distributed systems. Covers cloud service models, virtualization, containerization, distributed storage, and large-scale system design.

### Learning Objectives
- Understand cloud computing models (IaaS, PaaS, SaaS)
- Work with major cloud providers (AWS, Azure, GCP)
- Design and deploy applications using containers and orchestration (Docker, Kubernetes)
- Understand distributed systems: consistency, replication, fault tolerance
- Design scalable and resilient cloud architectures
- Implement Cloud-native applications

### Detailed Topics
- **Module 1:** Cloud Computing Fundamentals: NIST definition, cloud models (public, private, hybrid, community), service models (IaaS, PaaS, SaaS, FaaS)
- **Module 2:** Virtualization: hypervisors (Type 1/2), virtual machines, resource management, VM migration
- **Module 3:** Containers: Docker, container images, Dockerfile, Docker Compose, container registries
- **Module 4:** Container Orchestration: Kubernetes architecture, pods, services, deployments, ConfigMaps, Secrets, Helm
- **Module 5:** AWS/Azure/GCP: compute (EC2, Lambda, Azure Functions), storage (S3, Blob, Cloud Storage), databases (RDS, DynamoDB, Cosmos DB)
- **Module 6:** Distributed Systems: CAP theorem, consistency models (strong, eventual, causal), replication, partitioning
- **Module 7:** Distributed Storage: HDFS, Cassandra, Ceph, distributed file systems, object storage
- **Module 8:** Cloud Architecture: microservices, serverless, event-driven, load balancing, auto-scaling, CDN
- **Module 9:** DevOps and CI/CD: CI/CD pipelines, Infrastructure as Code (Terraform, CloudFormation), monitoring (Prometheus, Grafana)
- **Module 10:** Cloud Security: IAM, encryption, VPC, security groups, compliance, shared responsibility model

### Books
- **"Cloud Computing: Concepts, Technology & Architecture"** by Erl, Puttini, and Mahmood (Prentice Hall, 2013)
- **"Designing Data-Intensive Applications"** by Martin Kleppmann (O'Reilly, 2017) — The definitive distributed systems book
- **"The Kubernetes Book"** by Nigel Poulton (free e-book)
- **"Site Reliability Engineering"** by Beyer et al. (O'Reilly, 2016) — Google SRE

### Online Resources
- **AWS Academy / AWS Educate**
- **Microsoft Learn:** Azure fundamentals
- **Google Cloud Skills Boost**
- **CNCF (Cloud Native Computing Foundation):** Landscape, training

### Software Tools
- **Docker Desktop** (local containerization)
- **Minikube / Kind** (local Kubernetes)
- **AWS CLI / Azure CLI / gcloud CLI**
- **Terraform** (Infrastructure as Code)
- **Ansible** (configuration management)

### YouTube Channels (English)
- **TechWorld with Nana:** Docker, Kubernetes, DevOps, cloud
- **freeCodeCamp.org:** Cloud computing, AWS, Azure full courses
- **NetworkChuck:** Cloud, networking, cybersecurity
- **AWS Online Tech Talks:** Official AWS tutorials and talks
- **Microsoft Azure:** Official Azure tutorials and demos
- **Google Cloud Tech:** Official GCP tutorials
- **Kunal Kushwaha:** DevOps, cloud-native, Kubernetes

### YouTube Channels (Hindi/Urdu)
- **CodeWithHarry (Hindi):** Cloud computing, Docker, DevOps — https://youtube.com/@CodeWithHarry
- **Technical Sagar (Hindi):** Cloud, AWS, Azure tutorials
- **Gate Smashers (Hindi):** Distributed systems, cloud — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Distributed systems, cloud computing — https://youtube.com/@KnowledgeGate
- **Learn Coding (Hindi):** Cloud computing, AWS, Azure
- **Engineering in Hindi (Hindi):** Cloud, distributed computing
- **Urdu IT Academy (Urdu):** Cloud computing in Urdu

### Practical Projects
- **Project 1:** Dockerize a web application (Dockerfile, Docker Compose)
- **Project 2:** Deploy a containerized app on Kubernetes (Minikube)
- **Project 3:** Serverless application (AWS Lambda, API Gateway, DynamoDB)
- **Project 4:** Multi-tier cloud architecture (load balancer, web tier, database tier)
- **Project 5:** Cloud monitoring and auto-scaling implementation

### Certifications (Optional)
- **AWS Certified Cloud Practitioner / Solutions Architect Associate**
- **Microsoft Azure Fundamentals (AZ-900)**
- **Google Cloud Digital Leader**

### Assessment Methods
- Cloud assignments (30%)
- Lab exercises (20%)
- Midterm exam (20%)
- Final cloud architecture project (30%)
