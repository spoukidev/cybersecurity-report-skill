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
├── scripts/
│   └── validate.py          # Package validator (used by CI)
└── references/
    ├── report-templates.md  # Section templates
    ├── style-examples.md    # Language patterns from leading reports
    └── checklists.md        # Quality checklists by report type
```

## How to Use

Clone the repository into your AI tool's skills directory under the skill's name, `cybersecurity-report`. For example:

```bash
# Claude Code (personal skills)
git clone https://github.com/spoukidev/cybersecurity-report-skill.git ~/.claude/skills/cybersecurity-report

# Grok or another tool that reads a skills folder
git clone https://github.com/spoukidev/cybersecurity-report-skill.git .grok/skills/cybersecurity-report
```

The skill triggers on requests such as:
- "Write a professional incident response report..."
- "Create a threat intelligence report in Mandiant/CrowdStrike style..."
- "Write a cybersecurity board report..."
- "Produce an executive summary of this quarter's security posture..."

## Validating changes

Run the stdlib-only validator before committing. CI runs it on every push and pull request:

```bash
python3 scripts/validate.py
```

It checks the `SKILL.md` frontmatter, that every referenced `references/` and `evals/` file exists, and that the eval JSON is well-formed.

## License

MIT License

## Author

Created for professional cybersecurity reporting workflows.
