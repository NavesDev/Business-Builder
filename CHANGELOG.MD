# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Added comprehensive business framework documentation for digital business creation, monetization, operations, compliance, and development handoff.
- Added bilingual documentation assets (`BUSINESS_DOCUMENTAION.md` and `docs/pt-br/BUSINESS_DOCUMENTAION_PT-BR.md`) covering the full playbook structure.
- Added deterministic-skill guidance including required input/output contract, status rules, and traceability IDs.
- Added professional bilingual README documentation (`README.md` canonical EN and `docs/pt-br/README_PT-BR.md` translation).
- Added developer-oriented README elements: badges, table of contents, setup/validation commands, and contribution workflow.
- Added role-based Product Owner skill at `skills/product-owner/SKILL.md` with deterministic output contract, handoff quality gates, and RED/GREEN validation artifacts.
- Added a documented skill testing protocol (pressure scenarios + test log workflow) in EN/PT-BR READMEs and the skill template.
- Added `init` skill at `skills/init/SKILL.md` with deterministic intake for `novo|existente|em_construcao`, `.business-builder/` workspace bootstrap, `idea.md`/`users.md` create-or-update behavior, and `product-owner` validation routing.
- Added init validation assets at `skills/init/validation/pressure-scenarios.md` and `skills/init/validation/test-log.md`.
- Added init workspace templates under `skills/init/templates/.business-builder/` for root artifacts, context, product-management, and product-output scaffolding.

### Changed
- Expanded monetization coverage with a broader revenue model library and explicit model-selection sequence.
- Strengthened execution quality with operational dictionary defaults, KPI applicability matrix, and objective gate/risk thresholds.
- Established English as the canonical documentation direction, with PT-BR maintained under `docs/`.
- Replaced the minimal root README with a full project positioning and documentation navigation guide.
- Refined cross-functional execution with explicit function-interface contracts, handoff packet structure, SLA rules, and escalation levels.
- Updated AI skill blueprint to enforce role-based skill naming and file layout (`skills/<role-based-skill-name>/SKILL.md`), with `product-manager` as the recommended first implementation.
- Clarified EN and PT-BR READMEs to explicitly position Business Builder as an AI plugin.
