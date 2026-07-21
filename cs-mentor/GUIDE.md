# CS Mentor Skill: User Guide

The `cs-mentor` skill is designed to act as an adaptive, autonomous mentor for your computer science and cybersecurity journey. It leverages the internal knowledge base of this repository (`semesters/` and `guides/`) and continuously improves based on your feedback.

## 1. Getting Started
To activate the mentor skill within your agentic environment, use your interface's command for activating skills:
`activate_skill cs-mentor`

## 2. Interaction Modes (Commands)
The mentor operates using specific commands to steer the mentorship session:

| Command | Purpose |
| :--- | :--- |
| `/mentor-path` | **(Default)** Interactive, one-question-at-a-time guidance through your curriculum. |
| `/deep-dive <topic>` | Explores a specific concept from the roadmaps in depth. |
| `/search-knowledge <term>`| Searches all internal semester/guide files for a term. |
| `/project-audit` | Critique a project idea or get architectural guidance for "Build Your Own X" tasks. |
| `/roadmap-customizer` | Redefine your 12-month study plan based on new constraints. |

## 3. The Self-Improvement Protocol
The CS Mentor is designed to evolve.
- **Feedback Loop:** At the end of every substantive advice block, provide feedback.
- **Memory:** Your feedback is appended to `cs-mentor/references/feedback_log.md`.
- **Self-Correction:** Periodically, the mentor runs `cs-mentor/scripts/analyze_feedback.py` to analyze your feedback and refine its future approach, tone, and pedagogical style.

## 4. Proactive Agentic Capabilities
The mentor doesn't just provide static answers; it can perform tasks to actively assist you:
- **Research:** Use `google_web_search` or `web_fetch` to find the latest documentation when roadmaps need updates.
- **Automation:** Uses `run_shell_command` for interacting with system tools (compilers, git).
- **Knowledge Management:** Dynamically updates your `feedback_log.md` and learning plans using `write_file` and `replace`.

## 5. Best Practices & Philosophy
- **The 70/30 Rule:** Spend 70% of your time building/debugging and 30% studying theory.
- **Deep Understanding:** Never let the mentor skip the "Why." Ask for clarification if a concept feels superficial.
- **Always End with Action:** The mentor is instructed to end responses with a clear next step or a thought-provoking question to keep you moving forward.

---
*For issues or feedback on the mentor itself, use the `/bug` command in your primary interface.*
