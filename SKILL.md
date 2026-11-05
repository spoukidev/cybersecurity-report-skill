---
name: cybersecurity-report
description: "Produce professional cybersecurity reports in the style of Mandiant M-Trends, CrowdStrike Global Threat Report, IBM X-Force, and Verizon DBIR. Use when writing incident response reports, threat intelligence reports, executive summaries, or annual threat landscape reports."
type: workflow
lifecycle: active
---

# Cybersecurity Report — Professional Writing Skill

Write cybersecurity reports that match the professional standards of leading industry publications. Prioritize clarity for executives while retaining technical rigor for practitioners.

## Core Principles

1. **Executive-first**: Write the executive summary so a board member can understand the situation, impact, and required decisions after reading only that section.
2. **Evidence-based**: Ground every claim in observed data, telemetry, or investigation findings. State confidence levels.
3. **Business impact**: Translate technical findings into operational, financial, regulatory, and reputational impact.
4. **Actionable**: End with prioritized, specific recommendations. Avoid generic advice.
5. **Audience-aware**: Use layered content — high-level narrative in the body, technical depth in appendices or dedicated sections.
6. **Precise language**: Objective, measured tone. Avoid hype, marketing language, or absolute statements without evidence.

## Report Types and When to Use Them

| Report Type | Primary Audience | Key Focus | Typical Length |
|-------------|------------------|-----------|----------------|
| **Incident Response** | Leadership + IR team | What happened, impact, response, lessons | 8–25 pages |
| **Threat Intelligence / CTI** | SOC, CTI analysts, leadership | Actor, TTPs, IOCs, defensive implications | 6–20 pages |
| **Threat Landscape / Annual** | Broad (exec + technical) | Trends, metrics, sector/region breakdowns | 20–100+ pages |
| **Executive / Board Summary** | Board, C-suite | Risk posture, key metrics, decisions needed | 2–6 pages |

## Universal Structure (Adapt as Needed)

### 1. Cover / Header
- Report title, classification (TLP:RED/AMBER/GREEN/CLEAR), date, version, authors
- Optional: short thematic title (e.g., "Year of the Evasive Adversary")

### 2. Executive Summary (Critical)
- 1–2 paragraphs stating the central finding and confidence
- Key findings (3–6 bullets or short paragraphs)
- Business impact summary
- Top 3–5 recommendations
- Optional: "By the Numbers" callout box with 4–6 critical metrics

### 3. Methodology / Scope (when relevant)
- Data sources and time period
- Limitations and gaps
- Analytic techniques used

### 4. Findings / Narrative Sections
- Timeline of events (for IR)
- Technical analysis
- Actor profile / Attribution (with confidence)
- MITRE ATT&CK mapping
- Impact assessment

### 5. Recommendations
- Prioritized by residual risk and effort
- Specific, measurable where possible
- Assigned owners or functions when known

### 6. Appendices
- Indicators of Compromise (with context)
- Full timeline
- MITRE ATT&CK Navigator layer or detailed technique table
- Glossary
- Data tables

## Writing Style Guidelines

**Do**:
- Lead with the conclusion, then support with evidence
- Use specific numbers ("median dwell time of 11 days" not "dwell time decreased")
- Separate confidence from likelihood (ICD-203 style)
- Use active voice for recommendations
- Define acronyms on first use
- Use consistent terminology (prefer industry standards: MITRE ATT&CK, VERIS, etc.)

**Don't**:
- Bury the lead in technical detail
- Use unsubstantiated superlatives ("unprecedented", "catastrophic") without data
- Mix marketing language with analysis
- Present raw logs or IOCs without context
- Attribute without stating confidence and supporting signals

## Key Sections by Report Type

### Incident Response Report
1. Executive Summary
2. Incident Overview (type, severity, systems affected, detection source)
3. Timeline of Key Events
4. Technical Findings (initial access, lateral movement, actions on objectives)
5. Impact Assessment (data, operations, financial, regulatory)
6. Response Actions Taken (containment, eradication, recovery)
7. Root Cause Analysis
8. Lessons Learned and Recommendations
9. Appendices (IOCs, full timeline, evidence list)

### Cyber Threat Intelligence Report
1. Executive Summary + Key Findings table (decision question | finding | confidence | likelihood)
2. Actor Snapshot (aliases, motivation, sectors, tradecraft)
3. Activity Overview
4. Representative Techniques (MITRE ATT&CK)
5. Indicators of Compromise (with context and Pyramid of Pain tier)
6. Defensive Implications and Detection Guidance
7. Attribution Analysis (signals table)
8. Anticipated Activity

### Threat Landscape / Annual Report Style
1. Foreword / Introduction with theme
2. Executive Summary + By the Numbers
3. Key Trends (initial access vectors, motivations, sectors, regions)
4. Deep dives (ransomware, cloud, specific actor types, emerging techniques)
5. Regional or Industry breakouts
6. Recommendations
7. Appendices (MITRE coverage, methodology, glossary)

## Confidence and Likelihood

Use the following consistently:

**Confidence** (evidence strength): High / Moderate / Low

**Likelihood** (forward-looking only): Almost certain / Very likely / Likely / Roughly even chance / Unlikely / Very unlikely / Almost no chance

State confidence on every analytic judgment. Apply likelihood only to predictive statements.

## Quality Checklist Before Delivery

- [ ] Executive summary can stand alone
- [ ] Every major claim has supporting evidence or is labeled as assessment
- [ ] Business impact is quantified or clearly described
- [ ] Recommendations are specific and prioritized
- [ ] IOCs have context (role in activity)
- [ ] Attribution (if present) includes confidence and supporting signals
- [ ] Acronyms defined
- [ ] Tone is professional and measured
- [ ] Structure matches audience needs

## References

- See `references/report-templates.md` for detailed section templates
- See `references/style-examples.md` for language patterns from leading reports
- See `references/checklists.md` for type-specific quality checklists
