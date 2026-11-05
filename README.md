# Cybersecurity Report Skill

Professional cybersecurity report writing skill for AI models (Claude, Grok, and others).

Inspired by the structure, tone, and rigor of leading industry publications:
- Mandiant M-Trends
- CrowdStrike Global Threat Report
- IBM X-Force Threat Intelligence Index
- Verizon DBIR

## What It Does

Helps AI models produce high-quality, professional cybersecurity reports including:
- Incident Response reports
- Cyber Threat Intelligence (CTI) reports
- Threat landscape / annual reports
- Executive and board summaries

## Key Principles

- **Executive-first**: Write so leadership can act from the summary alone
- **Evidence-based**: Ground claims in data; state confidence levels
- **Business impact**: Translate technical findings into operational, financial, and regulatory impact
- **Actionable**: End with prioritized, specific recommendations
- **Precise language**: Measured, objective tone matching industry standards

## Structure

```
cybersecurity-report-skill/
├── SKILL.md                 # Main skill instructions
├── CHANGELOG.md             # Version history
├── evals/
│   ├── evals.json           # Test cases
│   └── triggers.json        # Trigger phrases
└── references/
    ├── report-templates.md  # Section templates
    ├── style-examples.md    # Language patterns from leading reports
    └── checklists.md        # Quality checklists by report type
```

## How to Use

Place the skill in your AI model's skills directory (e.g., `.grok/skills/cybersecurity-report/` or equivalent for Claude/other systems).

The skill triggers on requests such as:
- "Write a professional incident response report..."
- "Create a threat intelligence report in Mandiant/CrowdStrike style..."
- "Write a cybersecurity board report..."
- "Produce an executive summary of this quarter's security posture..."

## License

MIT License

## Author

Created for professional cybersecurity reporting workflows.
