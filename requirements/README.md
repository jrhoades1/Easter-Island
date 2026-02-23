# Requirements — Easter Island (Rongorongo Decipherment Toolkit)

This directory tracks structured requirements for the project. Each requirement is a
markdown file with YAML frontmatter for machine-readable metadata.

## File Naming

```
REQ-NNN-short-slug.md
```

Examples: `REQ-001-glyph-clustering.md`, `REQ-002-tablet-parser.md`

## Frontmatter Template

```yaml
---
id: REQ-NNN
title: Short human-readable title
status: proposed
priority: high          # critical | high | medium | low
author: claude          # jimmy | claude
requested_by: jimmy     # jimmy | claude | collaborator name
created: YYYY-MM-DD
approved: null
scheduled: null
implemented: null
verified: null
decision: null
tags: [feature, agents, parsing]
---
```

## Statuses

| Status | Description |
|--------|-------------|
| `proposed` | Initial idea — needs review |
| `approved` | Accepted for implementation |
| `rejected` | Not doing this (see decision field) |
| `deferred` | Good idea but not now |
| `scheduled` | Assigned to a sprint or week |
| `in_progress` | Currently being built |
| `implemented` | Code complete, needs verification |
| `verified` | Tested and confirmed working |

## Workflow Rules

- **Claude** can create `proposed` requirements and move `scheduled → in_progress → implemented`
- **Jimmy** approves/rejects proposed items and marks `implemented → verified`
- See `_workflow.yml` for the full transition map

## Cross-Project Report

```bash
python C:\Users\Tracy\Projects\claude-tracking\req_report.py
python C:\Users\Tracy\Projects\claude-tracking\req_report.py --project EASTER-ISLAND
```
