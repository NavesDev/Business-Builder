# Architecture Overview

## High-Level Design

Business Builder follows a **pipeline architecture** where each AI skill is an independent module that can be run in isolation or as part of the full orchestration flow.

```
User Input (idea)
       │
       ▼
 ┌─────────────┐
 │   Engine    │  ← src/engine.py
 └──────┬──────┘
        │
        ├──► Business Architect      → skills/business_architect.py
        ├──► Revenue Model Designer  → skills/revenue_model_designer.py
        ├──► Viability Analyst       → skills/viability_analyst.py
        ├──► Infrastructure Planner  → skills/infrastructure_planner.py
        ├──► API Blueprint Generator → skills/api_blueprint_generator.py
        └──► Data Model Architect    → skills/data_model_architect.py
                                              │
                                              ▼
                                       BusinessReport
                                       (src/models.py)
                                              │
                                              ▼
                                      output/report.md
```

## Key Design Decisions

- **Stateless skills** — each skill receives the raw idea (and optional context from previous skills) and returns a string.
- **Prompt-driven** — all AI behaviour is controlled via Markdown prompt templates in `/prompts`, keeping the Python code clean and the prompts easy to iterate.
- **LLM-agnostic** — the engine is designed to plug in any LLM provider (OpenAI, Anthropic, local models) via an adapter pattern.
