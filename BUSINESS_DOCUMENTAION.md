# BUSINESS DOCUMENTAION

## 1) Purpose, scope, and usage principles
This document defines a **complete operational standard** for creating digital businesses in Brazil.  
It was designed for two uses:

1. **Business operations** (strategy, product, growth, finance, compliance).
2. **Conversion into AI skills** (each pillar can become a specialist skill).

### Master rules of the standard
- Every decision must have: **owner + metric + exit criterion**.
- No initiative enters execution without a hypothesis and success criterion.
- No development starts without functional requirements, business rules, and acceptance criteria.
- No growth scales without unit economics within the limits in section 1.1.
- No delivery advances with open critical legal/fiscal risk.

### 1.1 Operational dictionary and default limits (hybrid)
The limits below are **recommended starting values**.  
Each skill must override values when context requires it (segment, ticket size, sales cycle, and maturity).

| Ambiguous term in the text | Mandatory operational definition | Recommended default value |
|---|---|---|
| Healthy unit economics | LTV/CAC >= threshold and CAC Payback <= threshold and Contribution Margin >= threshold | LTV/CAC >= 3; Payback <= 12 months; Margin >= 40% |
| Defined limit | Explicit threshold per KPI in skill input | Never use without a number/percentage |
| Minimum approved | Minimum mandatory artifact set per gate | Required fields completed + approved |
| Validated | Recorded evidence + observed metric | 2 consecutive measurement cycles |
| Prioritized | Formal ranking (RICE/MoSCoW) with owner and deadline | Backlog with ranking + justification |
| Relevant conversion drop | Percentage variation vs recent moving average | Drop > 15% vs 4-week average |
| High churn | Churn above monthly ceiling by segment | B2C > 5%/month; B2B > 3%/month |
| Minimum compliance package approved | Complete legal/fiscal/LGPD kit | Terms + policy + legal basis + fiscal obligations |

**Execution rule for skills:** any gate with "limit", "minimum", "validated", or "prioritized" must point to an objective value.

---

## 2) Universal method: from idea to execution
| Phase | Objective | Mandatory deliverable | Exit gate (do not advance without this) | Primary owner |
|---|---|---|---|---|
| 0. Strategic foundation | Define problem, ICP, and value proposition | Validated business thesis | ICP + prioritized pain + documented unique proposition | Founder/CEO |
| 1. Offer design | Define product/service and commercial package | Main offer + MVP roadmap | MVP scope and quality criteria approved | Product Owner |
| 2. Monetization | Define revenue model and pricing | Revenue strategy | Main model and formal commercial policy | CEO + Finance |
| 3. Go-to-market | Structure acquisition and sales | Channel plan and funnel | CAC target per channel and experimentation plan | Growth Lead |
| 4. Conversion and retention | Improve activation, conversion, and LTV | Activation journey and CRM | Onboarding defined + conversion/retention targets | PO + CRM/CS |
| 5. Operations and governance | Ensure quality delivery | Playbooks, SLAs, and rituals | Owners, handoffs, and active management ritual | Operations |
| 6. Sustainable scale | Grow with financial and legal control | Scale plan | Margin, cash, and compliance within limits | Leadership + CFO + Legal |

---

## 3) Architecture of the 8 pillars (master map)
| Pillar | Core question | Mandatory output |
|---|---|---|
| 1. Strategy and Positioning | What problem do we solve and for whom? | Thesis document + ICP + positioning |
| 2. Offer and Product | What do we deliver and how does it create value? | Offer blueprint + MVP scope + backlog |
| 3. Revenue and Monetization | How do we capture value predictably? | Revenue strategy + pricing + policies |
| 4. Acquisition and Growth | How do we generate demand repeatedly? | Channel plan + funnel + test plan |
| 5. Conversion and Retention | How do we improve activation, recurrence, and LTV? | Customer journey + CRM/CS plan |
| 6. Operations and Management | How do we execute without losing quality? | SOPs + SLAs + execution governance |
| 7. Finance and Unit Economics | Is the business financially sustainable? | Management P&L + scenarios + unit economics |
| 8. Compliance and Governance | Is the business legally protected? | LGPD map + contracts + fiscal trail |

---

## 4) Role and responsibility catalog (base for skills)
| Role | Mission | Key decisions | Minimum deliverables |
|---|---|---|---|
| Founder/CEO | Direct strategy and resource allocation | Niche, thesis, macro prioritization, risk | Strategic plan, quarterly goals |
| **Product Owner (PO)** | Translate business goals into executable product work | MVP scope, backlog priority, acceptance criteria | Prioritized backlog, stories, acceptance |
| Product Manager | Manage product discovery and evolution cycle | Impact vs effort trade-offs | Roadmap, product metrics |
| UX/UI Designer | Ensure journey clarity and usability | Flows, information architecture, visual standards | Flows, wireframes, prototypes |
| Tech Lead | Ensure technical feasibility and quality | Technical architecture, NFRs, tech debt | Technical spec, standards |
| Growth Lead | Build a predictable acquisition machine | Channel mix, budget, experiments | Growth plan, channel dashboard |
| CRM/Retention Lead | Improve activation and reduce churn | CRM journeys, segmentation, triggers | Lifecycle flows, playbooks |
| Sales Lead/Closer | Convert opportunities into revenue | Sales process, qualification, scripts | Pipeline, sales playbook |
| Head of Operations | Scale delivery with consistency | Processes, SLAs, automation, handoffs | SOPs, responsibility matrix |
| CFO/Finance | Ensure economic health | Final pricing, reinvestment, cash, risk | P&L, cash flow, financial plan |
| Legal | Cover contractual and regulatory risk | Terms, contracts, legal framing | Contract package and legal opinions |
| DPO/Privacy | Govern personal data and LGPD | Legal basis, retention, incident response | Data inventory and LGPD policy |

> Rule: one person may accumulate roles initially, but **responsibilities** remain mandatory.

---

## 5) Detailed playbook by pillar

## Pillar 1 - Strategy and Positioning
### Objective
Define with precision the problem, priority audience, and competitive differentiation.

### Mandatory inputs
- Initial niche hypothesis.
- Qualitative evidence (interviews, communities, market feedback).
- Direct/indirect competitor analysis.

### Critical decisions
- Primary ICP and secondary ICP.
- Core value promise (in one objective sentence).
- Differentiation thesis (price, speed, specialization, experience, technology).

### Business rules
- **RN-E1:** No offer goes to market without defined ICP.
- **RN-E2:** Every commercial promise must have operational evidence.
- **RN-E3:** Positioning must fit a 30-second message.

### Minimum KPIs
- Interview completion rate per cycle.
- Positive response rate to value proposition.
- Share of recurring objections (for thesis refinement).

### Roles and responsibilities
- Founder/CEO: owner of thesis and prioritization.
- Strategy/PM: consolidates insights and hypotheses.
- Growth: validates messaging in real channels.

### Exit gate
Approved strategy document with ICP, value proposition, differentiators, and validation metrics.

---

## Pillar 2 - Offer and Product
### Objective
Turn the value thesis into a clear offer, executable scope, and consistent experience.

### Mandatory inputs
- Strategic document (pillar 1).
- Team, timeline, and technology constraints.
- Legal/commercial requirements of the offer.

### Critical decisions
- MVP scope and out-of-scope boundary.
- Service level (manual, semi-automated, automated).
- Main purchase and usage journey.

### Business rules
- **RN-P1:** Every backlog item must map to a business objective.
- **RN-P2:** Story without acceptance criteria does not enter development.
- **RN-P3:** Scope change requires reassessment of timeline, cost, and risk.

### Operational checklist
- Define core, optional, and premium offer.
- Structure onboarding, first value delivery, and support.
- Build backlog by epics, stories, and acceptance criteria.
- Define Definition of Ready (DoR) and Definition of Done (DoD).

### Minimum KPIs
- Time to First Value (TTFV).
- Activation rate.
- Main journey completion rate.

### Roles and responsibilities
- **PO:** defines scope, prioritizes backlog, validates acceptance.
- UX/UI: designs flows, removes friction, ensures clarity.
- Tech Lead: validates technical feasibility and NFRs.

### Exit gate
MVP scope approved, prioritized backlog, and acceptance criteria defined for each critical item.

---

## Pillar 3 - Revenue and Monetization
### Objective
Define how the business captures value, sustains cash, and grows with margin.

### Mandatory inputs
- Delivery cost per customer.
- ICP value perception.
- Market benchmark.

### Critical decisions
- Primary revenue model.
- Pricing, discount, upgrade, and cancellation policy.
- Recurring vs transactional revenue capture strategy.

### Business rules
- **RN-M1:** No offer without formal pricing and refund policy.
- **RN-M2:** Discount outside policy requires approval from finance owner.
- **RN-M3:** Every plan must have a defined minimum margin.

### Minimum KPIs
- MRR/ARR or Monthly Revenue (depending on model).
- Average ticket.
- Contribution margin.
- Upgrade/downgrade rate.

### Roles and responsibilities
- CEO: defines value-capture direction.
- Finance: validates margin and cash impact.
- Growth/Sales: tests elasticity and conversion by price band.

### Exit gate
Validated primary revenue model, published commercial policy, and defined financial targets.

---

## Pillar 4 - Acquisition and Growth
### Objective
Create predictable acquisition with CAC control and lead quality.

### Mandatory inputs
- Validated ICP.
- Formalized offer and pricing.
- Positioning and key messages.

### Critical decisions
- Core channels (organic, paid, partnerships, outbound, community).
- Budget and CAC limit per channel.
- Experiment cadence and cut/scale criteria.

### Business rules
- **RN-G1:** Campaign without hypothesis and target metric does not go live.
- **RN-G2:** Channel with CAC above threshold for 2 cycles enters review.
- **RN-G3:** Every new campaign must have attribution traceability.

### Minimum KPIs
- CAC by channel.
- Conversion rate per funnel stage.
- Cost per qualified lead (CPLQ).
- Acquisition payback.

### Roles and responsibilities
- Growth Lead: owner of channel strategy and experiments.
- Media/Performance: campaign and creative execution.
- Content/SEO: mid/long-term organic acquisition.

### Exit gate
Operational funnel with stage targets and active weekly optimization plan.

---

## Pillar 5 - Conversion and Retention
### Objective
Increase conversion, reduce churn, and raise customer lifetime value.

### Mandatory inputs
- Funnel, onboarding, and usage data.
- Loss/cancellation reasons.
- Base segmentation.

### Critical decisions
- Onboarding strategy by profile.
- CRM journeys (activation, engagement, recovery).
- Customer support/success policy.

### Business rules
- **RN-R1:** Every new customer enters a structured onboarding track.
- **RN-R2:** Retention drop above threshold triggers action plan.
- **RN-R3:** Churn reasons must be classified and reviewed monthly.

### Minimum KPIs
- Activation rate.
- Trial-to-paid conversion (mandatory for trial/freemium models; otherwise use proposal-to-purchase conversion, per section 9.1).
- Revenue churn and customer churn.
- LTV and NPS/CSAT.

### Roles and responsibilities
- CRM/Retention: owner of journeys and segmentation.
- CS: support operations and churn reduction.
- Product: friction adjustments based on real behavior.

### Exit gate
Full lifecycle journey operating, with activation and retention targets.

---

## Pillar 6 - Operations and Management
### Objective
Standardize execution to gain quality, predictability, and scale.

### Mandatory inputs
- Process map of value chain.
- Role and handoff definitions.
- Incident and bottleneck history.

### Critical decisions
- Which processes to standardize first.
- Which SLAs are non-negotiable.
- Which stages require automation.

### Business rules
- **RN-O1:** Critical process requires SOP and owner.
- **RN-O2:** Recurring SLA breach triggers mandatory improvement plan.
- **RN-O3:** Inter-team handoff must have explicit input/output.

### Minimum KPIs
- SLA compliance.
- Operational lead time.
- Rework rate.
- Incident rate.

### Roles and responsibilities
- Operations: owner of SOP, quality, and continuous improvement.
- PMO/Coordination: cadence and execution governance.
- Tech/Automation: efficiency gains through systems.

### Exit gate
Critical processes standardized, SLAs monitored, and governance active.

---

## Pillar 7 - Finance and Unit Economics
### Objective
Ensure financial sustainability and support scale without burning cash.

### Mandatory inputs
- Revenue by business line.
- Fixed, variable, and acquisition costs.
- Default/cancellation history.

### Critical decisions
- Minimum margin per offer.
- Acquisition investment limit.
- Reinvestment policy and cash reserve.

### Business rules
- **RN-F1:** Offer with contribution margin below threshold enters adjustment.
- **RN-F2:** Acquisition above defined maximum payback requires review.
- **RN-F3:** Scaling decision depends on projected cash and controlled risk.

### Minimum KPIs and formulas
- Contribution Margin = Revenue - variable costs.
- LTV (estimated) = Average monthly ticket x gross margin x average lifetime (months).
- CAC Payback = CAC / monthly contribution margin per customer.
- Cash runway (months).

### Roles and responsibilities
- CFO/Finance: owner of cash, margin, and scenarios.
- Founder/CEO: decides macro allocation based on scenarios.
- Growth/Sales: adjusts acquisition to financial limits.

### Exit gate
Financial model with scenarios (base, optimistic, critical) and defined risk limits.

---

## Pillar 8 - Compliance and Governance
### Objective
Ensure legal, fiscal, and data compliance to protect the business.

### Mandatory inputs
- Current data flows and contracts.
- Revenue model and fiscal operation.
- Sales channels and customer relationship model.

### Critical decisions
- LGPD legal bases by flow.
- Contract structure by relationship type.
- Tax regime and ancillary obligations.

### Business rules
- **RN-C1:** No personal data without defined purpose and legal basis.
- **RN-C2:** Every relevant commercial relationship requires formal contract.
- **RN-C3:** Launch without fiscal/tax coverage is blocked.

### Minimum KPIs
- Percentage of flows with mapped legal basis.
- Average response time to data subject request.
- Legal/fiscal incidents per period.

### Roles and responsibilities
- Legal: owner of contracts, terms, and legal opinions.
- DPO: owner of LGPD governance.
- Finance/Fiscal: owner of tax compliance.

### Exit gate
Minimum legal/fiscal/LGPD package approved and monitored.

---

## 6) Expanded revenue model library
| Model | How it bills | When to use | Core metric | Critical risk |
|---|---|---|---|---|
| Monthly subscription | Recurring monthly fee | Continuous value and frequent usage | MRR and churn | High churn |
| Annual subscription | Annual payment | Mature and predictable product | ARR and renewal | Large upfront discounting |
| Freemium -> Paid | Free plan + upsell | Broad top of funnel and product with network/use effects | Free-to-paid conversion | Low conversion |
| Trial -> Paid | Trial period | Product with fast perceived value | Trial conversion | Trial without activation |
| One-time purchase | One-off payment | Closed, objective delivery | Average ticket | Unpredictable revenue |
| Per-user license (seat) | Price per active seat | B2B SaaS with teams | ARPA | Seat underutilization |
| Usage-based | Charged by usage volume | APIs, processing, data | Revenue per unit | Usage volatility |
| Tiers (Good/Better/Best) | Plan tiers | Segments with different maturity levels | Plan mix | Cross-tier cannibalization |
| Offer bundle | Product/service package | Cross-sell and ticket expansion | Attach rate | Delivery complexity |
| Setup fee + recurring fee | Setup + recurring | Service-led model with recurring component | Payback and MRR | Service dependency |
| Agency/retainer | Recurring service fee | Ongoing marketing/ops delivery | Contract retention | Operational bottleneck |
| Fixed-fee project | Scope-based fee | Customized deliveries | Margin per project | Scope overrun |
| Marketplace commission | % per transaction | Supply-demand intermediation | GMV and take rate | Fraud and volume dependence |
| Affiliate/reseller | Commission per sale | Partner-led distribution | Revenue per affiliate | Channel quality |
| Advertising/sponsorship | Sell audience inventory | Media/community with traffic | eCPM and fill rate | Audience dependence |
| White-label/OEM | Licensing to third parties | Replicable solution for partners | B2B revenue per contract | Complex support |

### Model selection rule (mandatory order)
1. Check **value nature** (continuous vs one-off).
2. Check **operational capacity** (manual vs automated scale).
3. Validate **unit economics** for each candidate model.
4. Define primary and secondary model (revenue backup).
5. Formalize commercial policy (price, discount, cancellation, refund).

---

## 7) Project/product design strategies
### 7.1 Discovery
- ICP interviews, objection analysis, and jobs-to-be-done mapping.
- Define priority problem in measurable terms.
- Validate desirability risk before building.

### 7.2 Scope definition
- MVP scope: only what proves value and generates business signal.
- Explicit out-of-scope to avoid backlog inflation.
- Prioritization by RICE (Reach, Impact, Confidence, Effort) or MoSCoW.

### 7.3 Experience design
- Map full journey: discovery -> decision -> onboarding -> usage -> renewal.
- Define perceived-value moments.
- Reduce friction in signup, payment, and activation steps.

### 7.4 Experimentation architecture
- Every experiment requires hypothesis, variable, audience, timeframe, and metric.
- Decision standard: scale, iterate, or kill experiment.
- Single learning repository to avoid repeating mistakes.

---

## 8) Requirements and business rules standard for development
This is the mandatory final stage for the product/engineering team.

### 8.1 Minimum structure of technical handoff package
- Business capability map by pillar.
- Functional requirements (RF) by flow.
- Non-functional requirements (RNF) by technical domain.
- Formalized business rules (BR).
- Acceptance criteria (CA) by story.
- Dependencies, risks, and assumptions.

### 8.2 Functional requirement template (RF)
```text
ID: RF-###
Title:
Business objective:
Primary actor:
Main flow:
Alternative flows/exceptions:
Mandatory inputs:
Expected outputs:
Audit events:
Related business rules: BR-###
```

### 8.3 Business rule template (BR)
```text
ID: BR-###
Description: If [condition], then [action], except when [exception].
Origin: Pillar X
Business rationale:
Impact on revenue/cost/risk:
```

### 8.4 Acceptance criteria template (CA)
```text
ID: CA-###
Scenario (Given):
Action (When):
Result (Then):
Observable metric:
```

### 8.5 Mandatory non-functional requirements (RNF)
- Security (auth, authorization, audit trail).
- Performance (maximum time per critical operation).
- Availability (technical SLA per module).
- Observability (logs, metrics, alerts).
- Reliability (failure handling and idempotency).
- Privacy (data minimization and retention).

### 8.6 Definition of Ready (DoR) and Definition of Done (DoD)
**Minimum DoR:** story with context, linked BR, defined acceptance, and mapped dependencies.  
**Minimum DoD:** implemented, validated against acceptance criteria, monitorable, and documented.

---

## 9) Brazil compliance (mandatory block)
### LGPD
- Personal data inventory (collection, use, storage, disposal).
- Legal basis by purpose.
- Process for data subject rights (access, correction, deletion, portability).
- Retention policy and incident response.

### Contracts and consumer
- Terms of use, privacy policy, and commercial policy.
- Contracts with suppliers, partners, and affiliates.
- Compliance with CDC for offers, cancellation, and advertising.

### Tax/fiscal
- Tax framework by business model (with accounting guidance).
- Tax invoice issuance by operation type.
- Financial and fiscal reconciliation routine.

### Intellectual property
- Ownership of brand, software, content, and knowledge base.
- Mandatory assignment/licensing contracts when software, content, or brand is created by third parties.

---

## 9.1 KPI applicability matrix (mandatory for skills)
To eliminate "when applicable", each skill must tag KPI as **mandatory** or **mandatory substitute**.

| Primary KPI | Mandatory when | Mandatory substitute when not applicable |
|---|---|---|
| MRR/ARR | Recurring model (subscription, retainer, recurring license) | Total monthly revenue + contribution margin |
| Trial->paid conversion | Trial or freemium model | Proposal->purchase conversion |
| Revenue/customer churn | Recurring revenue | Repeat purchase rate or contract renewal rate |
| NPS | Base with minimum valid response volume in the cycle | Standardized CSAT per interaction |
| CAC Payback | Paid channels or significant commercial investment | Acquisition cost by channel + sales cycle length |

**Rule:** no skill may return KPI as "N/A". If primary KPI does not apply, substitute KPI becomes mandatory.

---

## 10) Risk and controls matrix with action triggers
| Risk | Objective trigger | Immediate action | Owner |
|---|---|---|---|
| CAC out of control | CAC > `CAC_MAXIMO` for 2 consecutive cycles | Freeze channel scale and review offer/creative | Growth |
| Low conversion | Conversion drop > `QUEDA_CONVERSAO_MAXIMA` | Review journey and value propositions per stage | PO + Growth |
| High churn | Monthly churn > `CHURN_MAXIMO_SEGMENTO` | Trigger retention plan and cancellation interviews | CRM/CS |
| Margin compression | Contribution margin < `MARGEM_MINIMA` | Review pricing, cost, and offer mix | Finance |
| LGPD risk | Incident or data request not answered on time | Trigger DPO protocol and legal communication | DPO/Legal |
| Operational bottleneck | Recurring SLA breach | Review process, capacity, and automation | Operations |

---

## 11) Management cadence (mandatory rituals)
- **Daily (operations):** critical queue, incidents, bottlenecks.
- **Weekly (performance):** funnel, revenue, churn, top experiments.
- **Biweekly (product):** backlog review, scope, and learnings.
- **Monthly (executive):** management P&L, cash, risks, and allocation decisions.
- **Quarterly (strategic):** repositioning, new bets, and line shutdowns.

---

## 12) Maturity roadmap and gates
| Level | State | Mandatory evidence |
|---|---|---|
| Level 0 - Hypothesis | Problem and audience under validation | ICP and thesis under test |
| Level 1 - Foundation | Functional offer and first sales | MVP delivering value and initial funnel |
| Level 2 - Traction | Predictable acquisition and operations | Channels with controlled CAC and active retention |
| Level 3 - Scale | Growth with margin and governance | Unit economics within section 1.1 limits + robust compliance |
| Level 4 - Optimization | Disciplined expansion | Revenue portfolio and mature processes |

---

## 13) Blueprint to convert this standard into AI skills
### 13.1 Recommended skills (minimum)
| Skill | Objective | Mandatory input | Standard output |
|---|---|---|---|
| skill-estrategia-posicionamento | Define ICP and value thesis | Niche, pains, market signals | Validated thesis + prioritized ICP |
| skill-oferta-produto | Build offer and MVP backlog | Strategic thesis + constraints | MVP scope + backlog + acceptance |
| skill-receita-monetizacao | Define revenue model and pricing | Cost, perceived value, benchmark | Primary model + commercial policy |
| skill-aquisicao-growth | Structure channels and funnel | ICP + offer + budget | Channel plan + CAC targets |
| skill-conversao-retencao | Improve activation and LTV | Funnel and churn data | CRM/CS plan + retention targets |
| skill-operacao-gestao | Standardize execution | Current processes and SLAs | SOPs + handoffs + governance |
| skill-financas-unit-economics | Ensure sustainability | Revenue, costs, cash | Financial model + limits |
| skill-compliance-governanca | Cover legal/fiscal/LGPD | Data flows and contracts | Minimum compliance package |
| skill-handoff-dev | Translate business to engineering | Outputs from 8 pillars | Prioritized RF/RNF/BR/CA |

### 13.2 Deterministic contract per skill (mandatory)
Each skill must follow the same Markdown contract to keep consistency.

#### Block A - Mandatory skill input
| Field | Mandatory | Example |
|---|---|---|
| skill_id | Yes | `skill-aquisicao-growth` |
| segment | Yes | `B2B`, `B2C`, or `Hybrid` |
| revenue_model | Yes | `Monthly subscription` |
| maturity_stage | Yes | `Level 1`, `Level 2` |
| thresholds | Yes | `CAC_MAXIMO`, `MARGEM_MINIMA`, `CHURN_MAXIMO_SEGMENTO` |

#### Block B - Mandatory skill output
| Section | Mandatory minimum content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, or `gate_failed` |
| Summary diagnosis | 3 to 5 lines with context and primary conclusion |
| Decisions made | List with IDs (`DEC-001`, `DEC-002`), decision, and rationale |
| Executed checklist | List with IDs (`CHK-*`) and status (`ok`, `pending`, `blocked`) |
| KPIs and limits | KPI, current value, target, limit, and unit |
| Risks | IDs (`RSK-*`), level, mitigation, and owner |
| Gates | IDs (`GATE-*`) with result (`pass` or `fail`) and corrective action |
| Next action package | Action, owner, and due date |

#### Block C - Deterministic status rules
1. If any gate has `fail`, final status = `gate_failed`.
2. If no gate fails and checklist has `pending`/`blocked`, status = `mandatory_adjustments`.
3. If all gates pass and checklist has no pending items, status = `approved`.
4. Every skill must keep stable IDs (`DEC-*`, `CHK-*`, `RSK-*`, `GATE-*`) for traceability.

---

## 14) Final development readiness checklist
Before engaging technical team, confirm:
- [ ] MVP scope approved by PO and leadership.
- [ ] RF, RNF, BR, and CA complete and unambiguous.
- [ ] External dependencies identified.
- [ ] Critical risks with mitigation plan.
- [ ] Compliance requirements embedded in backlog.
- [ ] Business KPI linked to each priority delivery.

> If any item above is pending, the project **does not enter development**.
