# Business Builder

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Canonical Language: EN](https://img.shields.io/badge/Canonical-EN-blue)
![PT--BR Translation](https://img.shields.io/badge/Translation-PT--BR-orange)

Business Builder is a documentation-first framework for creating digital businesses with clear operational standards across strategy, product, monetization, growth, governance, and development handoff.

## Table of Contents
- [Why this project exists](#why-this-project-exists)
- [What is included](#what-is-included)
- [Documentation map](#documentation-map)
- [Recommended usage flow](#recommended-usage-flow)
- [Setup and validation commands](#setup-and-validation-commands)
- [Canonical language policy](#canonical-language-policy)
- [Contributing](#contributing)
- [Governance and legal](#governance-and-legal)

## Why this project exists
Most digital business projects fail because strategy decisions and implementation artifacts are disconnected.  
Business Builder provides a structured operating model that links business goals to actionable outputs (requirements, business rules, acceptance criteria, metrics, and risk controls).

## What is included
- End-to-end business framework (8 pillars)
- Expanded revenue model library with selection criteria
- Deterministic skill contract guidance
- Development handoff standard (RF/RNF/BR/CA)
- Compliance baseline for Brazil (LGPD, contracts, tax/fiscal, IP)

## Documentation map
- Main framework: [`BUSINESS_DOCUMENTAION.md`](BUSINESS_DOCUMENTAION.md)
- Alternate-language framework: [`docs/pt-br/BUSINESS_DOCUMENTAION_PT-BR.md`](docs/pt-br/BUSINESS_DOCUMENTAION_PT-BR.md)
- PT-BR README translation: [`docs/pt-br/README_PT-BR.md`](docs/pt-br/README_PT-BR.md)
- Superpowers workspace: [`docs/superpowers/`](docs/superpowers/)
- Skills: [`skills/`](skills/)

## Recommended usage flow
1. Read the business framework document.
2. Pick the target pillar (strategy, product, monetization, growth, etc.).
3. Extract decisions, KPIs, gates, and risks.
4. Produce implementation handoff artifacts (RF/RNF/BR/CA).
5. Execute and monitor metrics/risk triggers continuously.

## Setup and validation commands
```bash
git clone <your-repository-url>
cd BusinessBuilder

# Check key documentation files
ls -la README.md BUSINESS_DOCUMENTAION.md docs/pt-br/README_PT-BR.md docs/pt-br/BUSINESS_DOCUMENTAION_PT-BR.md

# Check README structure
grep -nE "^## " README.md docs/pt-br/README_PT-BR.md

# Check canonical/translation policy sections
grep -nE "Canonical language policy|Politica de idioma canonico" README.md docs/pt-br/README_PT-BR.md
```

## Canonical language policy
- `README.md` is the canonical README (English).
- `docs/pt-br/README_PT-BR.md` is the Portuguese translation.
- Update workflow: edit EN first, then synchronize PT-BR in the same change cycle.

## Contributing
1. Create a branch: `git checkout -b docs/<short-topic>`.
2. Keep changes focused and scoped.
3. Preserve EN/PT-BR parity when updating README content.
4. Open a PR describing what changed and what was synchronized.

## Governance and legal
- Changelog: [`CHANGELOG.MD`](CHANGELOG.MD)
- Code of Conduct: [`CODE_OF_CONDUCT.MD`](CODE_OF_CONDUCT.MD)
- License: [`LICENSE`](LICENSE)
