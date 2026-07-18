# Semester 8: Web & Intelligent Systems

## Web Engineering

### Overview
Study of modern web development: frontend, backend, databases, APIs, and deployment. Covers full-stack web application development using contemporary frameworks and tools.

### Learning Objectives
- Build responsive frontends using React/Angular/Vue
- Develop backend APIs using Node.js/.NET/Django
- Design and interact with databases (SQL and NoSQL)
- Implement authentication, authorization, and security
- Deploy web applications to cloud platforms

### Detailed Topics
- **Module 1:** Web Fundamentals: HTTP/HTTPS, REST, JSON, cookies, sessions, CORS, web security basics (XSS, CSRF, SQL injection)
- **Module 2:** HTML5 and CSS3: semantic HTML, CSS Grid, Flexbox, responsive design, CSS frameworks (Bootstrap, Tailwind)
- **Module 3:** JavaScript: ES6+, DOM manipulation, async/await, fetch API, modules, bundlers (Webpack, Vite)
- **Module 4:** Frontend Frameworks: React (components, hooks, state management, routing), or Angular (components, services, RxJS), or Vue (Vue 3, Composition API, Pinia)
- **Module 5:** Backend Development: Node.js (Express, Next.js, NestJS), or ASP.NET Core (Web API, MVC), or Django (DRF, Django Channels)
- **Module 6:** Database Integration: ORMs (Entity Framework, Prisma, Django ORM, Mongoose), SQL, NoSQL, migrations
- **Module 7:** Authentication and Authorization: JWT, OAuth 2.0, session-based auth, role-based access control
- **Module 8:** API Design: RESTful API design principles, versioning, error handling, rate limiting, GraphQL
- **Module 9:** Testing: unit, integration, end-to-end (Jest, Cypress, Playwright, Selenium)
- **Module 10:** Deployment: cloud platforms (Vercel, Netlify, AWS, Azure, Heroku), CI/CD, Docker, SSL/TLS, domain management

### Books
- **"Web Development with Node.js and Express, 2nd Edition"** by Ethan Brown (O'Reilly, 2019)
- **"Learning React, 2nd Edition"** by Alex Banks and Eve Porcello (O'Reilly, 2020)
- **"Full-Stack Web Development with ASP.NET Core 8"** by Sunil Kumar S. (Apress, 2024)
- **"Designing Web APIs"** by Jin, Sahni, and Shevat (O'Reilly, 2018)

### Software Tools
- **VS Code / WebStorm** (IDE)
- **Git / GitHub** (version control)
- **Postman / Insomnia** (API testing)
- **Browser DevTools** (debugging)
- **Docker** (containerization)

### YouTube Channels (English)
- **Traversy Media:** Full-stack web development, React, Node.js, CSS
- **freeCodeCamp.org:** Web development full courses
- **The Net Ninja:** React, Vue, Node.js, CSS, Git tutorials
- **Web Dev Simplified:** HTML, CSS, JavaScript, React
- **Fireship:** Web development, frameworks, cloud
- **Academind:** React, Angular, Node.js, Python
- **Kevin Powell:** CSS mastery, responsive design
- **Chai aur Code:** https://www.youtube.com/@chaiaurcode
- **Hitesh Code Lab:** https://www.youtube.com/@HiteshCodeLab

### YouTube Channels (Hindi/Urdu)
- **CodeWithHarry (Hindi):** Web development, React, Node.js — https://youtube.com/@CodeWithHarry
- **Apna College (Hindi):** Web development full course — https://youtube.com/@ApnaCollegeOfficial
- **Thapa Technical (Hindi):** React, JavaScript, web development
- **Technical Sagar (Hindi):** Web development, frameworks
- **Learn Coding (Hindi):** HTML, CSS, JavaScript, PHP
- **Easy Tutorials (Hindi):** Web design, HTML, CSS, JavaScript
- **Urdu IT Academy (Urdu):** Web development in Urdu

### Practical Projects
- **Project 1:** Personal portfolio website (responsive, CSS Grid/Flexbox)
- **Project 2:** Blog platform (React frontend, Node.js/Express backend, MongoDB)
- **Project 3:** E-commerce web app (product catalog, cart, checkout, payment integration)
- **Project 4:** Real-time chat application (WebSockets, Socket.io)
- **Final Project:** Full-stack web application with authentication, database, and deployment

### Assessment Methods
- Coding assignments (25%)
- Web development projects (30%)
- Midterm exam (20%)
---

## System Design Architecture (Additional Course)

### Overview
Study of scalable, reliable, and maintainable software system design. This course covers the fundamental building blocks, architectural patterns, and trade-offs required to design and scale large systems.

### Learning Objectives
- Design scalable web applications for millions of users.
- Understand database partitioning (sharding), caching strategies, and load balancing.
- Compare monolithic vs. microservices architectures.
- Design efficient APIs (REST, GraphQL, gRPC) for high-performance communication.
- Understand security, observability, and reliability in distributed environments.

### Detailed Topics
- **Module 1: Foundations of Scalability:** Latency, throughput, availability (the "nines"), horizontal vs. vertical scaling, CAP theorem, PACELC theorem.
- **Module 2: Load Balancing and Caching:** Layer 4 vs. Layer 7 load balancing algorithms (round-robin, least-connections, consistent hashing), CDN strategies, multi-level caching (browser, CDN, server-side, database).
- **Module 3: Database Design:** ACID vs. BASE models, SQL (relational) vs. NoSQL (key-value, document, wide-column, graph), database sharding (partitioning strategies), replication (master-slave, master-master), query optimization.
- **Module 4: Messaging and Asynchrony:** Producer-consumer pattern, message queues (Kafka, RabbitMQ, SQS), pub/sub models, event-driven architecture, handling eventual consistency.
- **Module 5: Architectural Patterns & Security:** Microservices, serverless, SOA, API Gateway, rate limiting, authentication/authorization (JWT, OAuth 2.0), observability (logging, metrics, tracing).

### Recommended Books
- **"Designing Data-Intensive Applications"** by Martin Kleppmann (O'Reilly).
- **"System Design Interview – An Insider's Guide"** by Alex Xu.

### Practical Projects
- **Project 1:** Design a URL shortening service (like Bitly) focusing on database sharding and high-frequency read/write performance.
- **Project 2:** Design a real-time messaging application (like WhatsApp/Discord) covering WebSockets, message persistence, and presence service.
- **Project 3:** Design a news feed system (like Twitter/Instagram) covering data partitioning, fan-out-on-write vs. fan-out-on-read, and caching strategies.


---

## Deep Learning

### Overview
Study of deep neural networks: architectures, training techniques, and applications. Covers CNNs, RNNs, transformers, GANs, and deep learning frameworks.

### Learning Objectives
- Understand neural network fundamentals: backpropagation, activation functions, regularization
- Design and train CNNs for image processing
- Implement RNNs/LSTMs for sequence data
- Apply transfer learning and fine-tuning
- Understand transformers and attention mechanisms
- Implement generative models (GANs, VAEs, diffusion models)

### Detailed Topics
- **Module 1:** Neural Network Foundations: perceptron, MLP, backpropagation, gradient descent, loss functions, learning rate, regularization, dropout, batch normalization
- **Module 2:** Convolutional Neural Networks (CNNs): convolution, pooling, stride, padding, filter banks, LeNet, AlexNet, VGG, ResNet, Inception, EfficientNet
- **Module 3:** Recurrent Neural Networks (RNNs): vanishing/exploding gradients, LSTM, GRU, bidirectional RNNs, sequence-to-sequence models, attention
- **Module 4:** Transfer Learning: pre-trained models, feature extraction, fine-tuning, domain adaptation
- **Module 5:** Transformers: self-attention, multi-head attention, positional encoding, BERT, GPT, ViT, vision transformers
- **Module 6:** Generative Models: autoencoders, variational autoencoders (VAEs), GANs (DCGAN, StyleGAN, CycleGAN), diffusion models
- **Module 7:** Advanced Topics: reinforcement learning with deep Q-networks, neural style transfer, object detection (YOLO, Faster R-CNN), semantic segmentation
- **Module 8:** Deep Learning Frameworks: TensorFlow, Keras, PyTorch, JAX, Lightning, Hugging Face

### Books
- **"Deep Learning"** by Goodfellow, Bengio, and Courville (MIT Press, 2016) — Free online
- **"Deep Learning with Python, 2nd Edition"** by François Chollet (Manning, 2021)
- **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 3rd Edition"** by Géron (O'Reilly, 2022)
- **"Programming PyTorch for Deep Learning"** by Ian Pointer (O'Reilly, 2019)

### Software Tools
- **PyTorch, TensorFlow, Keras** (deep learning frameworks)
- **Jupyter Notebook / Google Colab**
- **Weights & Biases** (experiment tracking)
- **Hugging Face** (transformers, pre-trained models)

### YouTube Channels (English)
- **Andrej Karpathy:** Neural networks, GPT, AI fundamentals
- **3Blue1Brown:** Neural networks, backpropagation visualized
- **Aladdin Persson:** PyTorch, CNN, GAN, deep learning tutorials
- **sentdex:** Python deep learning, TensorFlow, PyTorch
- **Nicholas Renotte:** Deep learning projects, computer vision
- **DeepLearningAI:** Andrew Ng's deep learning specialization courses
- **Yannic Kilcher:** Deep learning research, transformers, GPT

### YouTube Channels (Hindi/Urdu)
- **CodeWithHarry (Hindi):** Deep learning, TensorFlow, PyTorch — https://youtube.com/@CodeWithHarry
- **Gate Smashers (Hindi):** Deep learning, neural networks — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Deep learning, CNNs, RNNs — https://youtube.com/@KnowledgeGate
- **Technical Sagar (Hindi):** AI, deep learning, neural networks
- **Engineering in Hindi (Hindi):** Deep learning fundamentals
- **Learn Coding (Hindi):** Python deep learning, AI
- **Simple Snippets (Hindi):** Neural networks, deep learning

### Practical Projects
- **Project 1:** Image classifier (CNN, CIFAR-10/100)
- **Project 2:** Text generation with RNN/LSTM
- **Project 3:** Neural style transfer (VGG-based)
- **Project 4:** Sentiment analysis with BERT (fine-tuning Hugging Face)
- **Project 5:** Image generation with GANs or diffusion models
- **Final Project:** Deep learning application (e.g., medical image diagnosis, speech recognition, chatbot)

### Assessment Methods
- Programming assignments (25%)
- Model implementation projects (25%)
- Midterm exam (20%)
- Final deep learning project (30%)

---

## Robotics

### Overview
Study of robotics fundamentals: kinematics, dynamics, control, perception, and programming. Covers robot manipulators, mobile robots, and autonomous systems.

### Learning Objectives
- Understand robot kinematics and dynamics
- Implement forward and inverse kinematics for manipulators
- Apply control algorithms for robot motion
- Implement perception algorithms (sensors, computer vision)
- Program robots using ROS (Robot Operating System)
- Design and simulate robot systems

### Detailed Topics
- **Module 1:** Introduction to Robotics: robot types, applications, coordinate systems, degrees of freedom, workspace
- **Module 2:** Spatial Transformations: homogeneous transformations, rotation matrices, quaternions, Euler angles
- **Module 3:** Forward Kinematics: Denavit-Hartenberg (DH) parameters, transformation matrices, kinematic chains
- **Module 4:** Inverse Kinematics: analytical vs. numerical methods, Jacobian, singularities, redundancy
- **Module 5:** Robot Dynamics: Newton-Euler formulation, Lagrangian mechanics, inertia matrix, Coriolis forces
- **Module 6:** Trajectory Planning: joint-space vs. task-space, cubic splines, quintic splines, trapezoidal velocity profiles
- **Module 7:** Robot Control: PID control, computed torque control, impedance control, force control
- **Module 8:** Sensors and Perception: encoders, IMUs, ultrasonic, LiDAR, cameras, RGB-D (Kinect, RealSense), sensor fusion (Kalman filter, EKF)
- **Module 9:** Mobile Robotics: differential drive, omnidirectional, localization (Monte Carlo, particle filter), mapping (SLAM), path planning (A*, Dijkstra, RRT, DWA)
- **Module 10:** Robot Operating System (ROS): ROS architecture, nodes, topics, services, actions, ROS 2, simulation (Gazebo), visualization (RViz)

### Books
- **"Introduction to Robotics: Mechanics and Control, 4th Edition"** by John J. Craig (Pearson, 2017)
- **"Robotics: Modelling, Planning and Control, 2nd Edition"** by Siciliano, Sciavicco, Villani, and Oriolo (Springer, 2010)
- **"Programming Robots with ROS"** by Quigley, Gerkey, and Smart (O'Reilly, 2015)
- **"Springer Handbook of Robotics, 2nd Edition"** by Siciliano and Khatib (Springer, 2016)

### Software Tools
- **ROS 2** (Robot Operating System)
- **Gazebo** (simulation)
- **RViz** (visualization)
- **MoveIt** (motion planning)
- **MATLAB** (Robotics Toolbox)
- **Python:** NumPy, OpenCV, PyBullet

### Hardware (Optional)
- **Arduino / Raspberry Pi** (microcontroller)
- **Robot kits:** TurtleBot, PhantomX, RoboMaster
- **Sensors:** ultrasonic, IR, IMU, LiDAR, camera
- **Actuators:** servo motors, DC motors, stepper motors

### YouTube Channels (English)
- **Robotics with ROS:** ROS tutorials, robot programming
- **The Construct:** ROS, robotics simulation, Gazebo
- **Articulated Robotics:** Robotics fundamentals, ROS, kinematics
- **MIT OCW:** Introduction to Robotics (Prof. Harry Asada)
- **Stanford CS223A:** Robotics (Prof. Oussama Khatib)
- **Robotnik:** Robotics, ROS, autonomous systems
- **Vincent A. (YouTube):** Robotics, computer vision, SLAM

### YouTube Channels (Hindi/Urdu)
- **Technical Sagar (Hindi):** Robotics, AI, automation
- **Gate Smashers (Hindi):** Robotics, AI concepts — https://youtube.com/@GateSmashers
- **KnowledgeGate (Hindi):** Robotics, control systems — https://youtube.com/@KnowledgeGate
- **EduPoint (Hindi):** Robotics fundamentals, kinematics
- **Engineering in Hindi (Hindi):** Robotics, automation basics
- **Easy Engineering (Hindi):** Robotics, control, sensors
- **Urdu IT Academy (Urdu):** Robotics in Urdu

### Lab Work
- **Lab 1:** ROS basics: nodes, topics, services, launch files
- **Lab 2:** Forward kinematics computation (Python/MATLAB)
- **Lab 3:** Inverse kinematics and trajectory planning
- **Lab 4:** PID control of a robotic arm
- **Lab 5:** Mobile robot localization and navigation
- **Lab 6:** SLAM implementation (gmapping, cartographer)
- **Lab 7:** Robot simulation in Gazebo

### Assessment Methods
- Assignments (20%)
- ROS programming labs (30%)
- Midterm exam (20%)
- Final robotics project (30%)

---

## Final Year Project

### Overview
Capstone project demonstrating the culmination of engineering knowledge. Students work in teams to design, implement, and present a comprehensive engineering project.

### Learning Objectives
- Apply engineering knowledge to solve a real-world problem
- Plan and manage a project from conception to completion
- Work effectively in a team environment
- Design and implement a complete system
- Document and present the project professionally
- Demonstrate project management, technical writing, and presentation skills

### Project Phases
- **Phase 1: Project Proposal (Week 1-3)**
  - Problem identification and analysis
  - Literature review and market research
  - Project scope, objectives, and deliverables
  - Technical feasibility and resource requirements
  - Project proposal submission and approval

- **Phase 2: Requirements and Design (Week 4-7)**
  - Functional and non-functional requirements
  - System architecture and design
  - Component/module specification
  - Technology stack selection
  - Design review and approval

- **Phase 3: Implementation (Week 8-14)**
  - Agile development sprints
  - Component implementation and integration
  - Version control (Git)
  - Regular progress reviews with supervisor

- **Phase 4: Testing and Validation (Week 15-17)**
  - Unit testing, integration testing, system testing
  - Performance testing and optimization
  - User acceptance testing
  - Bug fixing and refinement

- **Phase 5: Documentation (Week 17-18)**
  - Final project report (IEEE/ACM format)
  - User manual
  - Technical documentation
  - System architecture diagrams

- **Phase 6: Presentation and Demonstration (Week 19)**
  - Project poster
  - Live demonstration
  - Oral presentation
  - Q&A session

- **Phase 7: Final Submission (Week 20)**
  - Complete source code
  - Final report
  - Project deliverables
  - Lessons learned

### Project Categories
- **Hardware:** Embedded systems, IoT, robotics, digital systems
- **Software:** Web applications, mobile apps, AI/ML, blockchain
- **Mixed:** Cyber-physical systems, automation, smart devices
- **Research:** Novel algorithms, theoretical contributions, surveys

### Documentation
- **Project Proposal:** Problem statement, motivation, objectives, methodology, timeline, resources
- **Design Document:** System architecture, component design, data flow, interface specifications
- **Progress Reports:** Bi-weekly updates, milestones achieved, challenges, revisions
- **Final Report:** Abstract, introduction, literature review, methodology, implementation, results, discussion, conclusion, references
- **Poster:** Visual summary of the project

### YouTube Channels (English)
- **freeCodeCamp.org:** Full project tutorials, portfolio building
- **The Coding Train:** Creative coding, project-based learning
- **sentdex:** Python projects, practical applications
- **Nicholas Renotte:** AI/ML project tutorials
- **Traversy Media:** Full-stack project tutorials

### YouTube Channels (Hindi/Urdu)
- **CodeWithHarry (Hindi):** Project tutorials, coding — https://youtube.com/@CodeWithHarry
- **Apna College (Hindi):** Project-based learning — https://youtube.com/@ApnaCollegeOfficial
- **Technical Sagar (Hindi):** Tech projects, career guidance
- **Learn Coding (Hindi):** Project tutorials, web development
- **Engineering in Hindi (Hindi):** Engineering project guidance

### Assessment Methods
- Project proposal (10%)
- Design and implementation (40%)
- Testing and validation (15%)
- Final report (20%)
- Presentation and demonstration (15%)

### Recommended Tools
- **Version Control:** Git, GitHub/GitLab
- **Project Management:** Jira, Trello, Asana
- **Documentation:** LaTeX, Overleaf, Notion
- **Design:** Figma, Lucidchart, Draw.io
- **CI/CD:** GitHub Actions, GitLab CI
- **Collaboration:** Slack, Discord, Microsoft Teams
