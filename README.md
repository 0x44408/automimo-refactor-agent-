# automimo-refactor-agent-

# AutoMimo Refactor Agent 🤖🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**AutoMimo Refactor Agent** is an autonomous, AI-driven codebase maintenance tool built on top of **OpenClaw**. It is designed to automatically scan software repositories for technical debt, refactor legacy code according to modern architectural standards, and run localized unit tests to ensure safe, closed-loop verification before autonomously generating Pull Requests (PRs).

This project was built as a core demonstration of production-grade AI Agent capabilities for the **Xiaomi MiMo 100T** grant program.

---

## 💡 Core Problem & Logic Flow

### The Problem
As engineering teams scale, legacy codebases accumulate technical debt, outdated design patterns, and deprecated API usages. Manual code refactoring and structural reviews consume significant developer hours, slowing down features delivery.

### The Agent Workflow (Long-Chain Reasoning)
The repository implements a structured, multi-agent execution loop:

1. **Static Code Analysis:** The agent scans the target codebase to detect complex methods, code duplication, or anti-patterns.
2. **Contextual Planning:** It ingests the surrounding modules and architecture guidelines into its context window, generating a step-by-step refactoring plan using chain-of-thought reasoning.
3. **Refactoring Execution:** Powered by LLMs (Claude/MiMo), the agent rewrites the code snippet to be cleaner, modular, and optimized.
4. **Closed-Loop Verification:** The agent automatically runs `pytest` in an isolated environment. If a test fails, the error logs are fed back into the agent to self-correct the code.
5. **Git Automation:** Upon achieving a 100% test success rate, the agent creates a new Git branch, commits the changes, and submits a structured Pull Request.

---

## 🛠️ Tech Stack

* **AI Agent Framework:** OpenClaw / Claude Code
* **Primary LLMs:** MiMo Series / Claude 3.5 Sonnet
* **Language:** Python 3.10+
* **Testing:** PyTest
* **Automation:** GitHub Actions (CI/CD integration)
│   └── test_agent.py          # Functional testing for agent reliability
└── README.md                  # Project documentation
