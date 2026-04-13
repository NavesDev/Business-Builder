# 🏗️ Business Builder

> An AI-powered plugin for **Business Logic Development** — turn a raw business idea into a fully architected, revenue-ready blueprint in minutes.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

---

## 📖 Description

**Business Builder** is an AI plugin that bridges the gap between a business idea and its technical and commercial execution. You provide a concept; the AI delivers:

- **Backend Logic Structure** — Entities, services, APIs, and data flows mapped out automatically.
- **Revenue & Billing Models** — SaaS, Freemium, Marketplace, Pay-per-use, and more — with a recommended fit for your idea.
- **Viability Analysis** — Market positioning, competitive risks, and key assumptions surfaced early.
- **Infrastructure Blueprint** — Cloud architecture, third-party integrations, and scaling considerations.

Whether you are a solo founder, a startup team, or an enterprise architect, Business Builder gives you a structured, actionable starting point so you can move from concept to code with confidence.

---

## 🤖 AI Skills

Business Builder is composed of specialised AI skills that each handle a distinct domain:

| Skill | Description |
|---|---|
| **Business Architect** | Decomposes the business idea into logical domains, entities, and service boundaries. |
| **Revenue Model Designer** | Evaluates and recommends billing strategies (SaaS, Freemium, Marketplace, etc.). |
| **Viability Analyst** | Assesses market fit, identifies risks, and surfaces critical assumptions. |
| **Infrastructure Planner** | Designs the cloud/infrastructure topology required to support the business at scale. |
| **API Blueprint Generator** | Generates a high-level REST/GraphQL API contract aligned with the business logic. |
| **Data Model Architect** | Produces entity-relationship diagrams and database schema suggestions. |
| **Prompt Engineer** | Manages and optimises the prompts used by every other skill for consistent, high-quality output. |

---

## 📁 Project Structure

```
Business-Builder/
├── src/                  # Core plugin source code
│   ├── engine.py         # Orchestration engine — routes requests to skills
│   ├── models.py         # Shared data models and schema definitions
│   └── utils.py          # Shared utility functions
├── skills/               # Individual AI skill modules
│   ├── business_architect.py
│   ├── revenue_model_designer.py
│   ├── viability_analyst.py
│   ├── infrastructure_planner.py
│   ├── api_blueprint_generator.py
│   └── data_model_architect.py
├── prompts/              # Prompt templates used by each skill
│   ├── business_architect.md
│   ├── revenue_model_designer.md
│   ├── viability_analyst.md
│   ├── infrastructure_planner.md
│   ├── api_blueprint_generator.md
│   └── data_model_architect.md
├── docs/                 # Documentation and examples
│   ├── architecture.md
│   ├── skills.md
│   └── examples/
├── tests/                # Unit and integration tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### Prerequisites

- Python **3.10** or higher
- An OpenAI API key (or a compatible LLM provider key)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/NavesDev/Business-Builder.git
   cd Business-Builder
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Linux / macOS
   .venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy the example env file and fill in your credentials:

   ```bash
   cp .env.example .env
   ```

   Open `.env` and set:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   MODEL_NAME=gpt-4o          # or any supported model
   ```

---

## 🚀 How to Use

### Basic Usage

Run Business Builder from the command line by providing your business idea as a prompt:

```bash
python -m src.engine "I want to build a subscription-based platform that connects freelance chefs with home diners."
```

The plugin will sequentially invoke each AI skill and output a structured report to the terminal and to `output/report.md`.

### Example Output

```
📌 Business Concept: Freelance chef marketplace
───────────────────────────────────────────────
🏗️  Business Architecture     ✅  Generated
💰  Revenue Model             ✅  Recommended: Marketplace (commission) + SaaS tiers
📊  Viability Analysis        ✅  Score: 74/100 — Medium-High feasibility
☁️   Infrastructure Blueprint  ✅  Generated
🔌  API Blueprint             ✅  Generated (12 endpoints)
🗄️   Data Model               ✅  Generated (8 entities)

Full report saved to: output/report.md
```

### Selecting Specific Skills

You can run individual skills by passing the `--skill` flag:

```bash
python -m src.engine "SaaS analytics tool for e-commerce" --skill revenue_model_designer
```

### Python API

```python
from src.engine import BusinessBuilder

bb = BusinessBuilder()
report = bb.run("A B2B SaaS tool that automates payroll compliance for SMEs.")
print(report.revenue_model)
print(report.infrastructure)
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you would like to change, then submit a pull request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-new-skill`
3. Commit your changes: `git commit -m 'feat: add new skill'`
4. Push to the branch: `git push origin feature/my-new-skill`
5. Open a pull request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
