# Skill Registry

- Project: agenda-equipo-02 (Engram project: `ia isw`)
- Generated: 2026-10-21 by sdd-init
- Cache status: regenerated (no previous registry found)

**Contract**: this file is an INDEX only. The `SKILL.md` at each path is the source of truth — pass the exact path to the delegating agent and let it read the full skill.

## Scan Sources

- Project-level: none found (no `skills/`, `.opencode/skills/`, `.claude/skills/`, `.gemini/skills/`, `.cursor/skills/`, `.github/skills/`, `.codex/skills/`, `.qwen/skills/`, `.kiro/skills/`, `.openclaw/skills/`, `.pi/skills/`, `.agent/skills/`, `.agents/skills/`, `.atl/skills/` in project root).
- User-level: `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/`, `~/.gemini/skills/`, `~/.qwen/skills/`, `~/.kiro/skills/`, `~/.openclaw/skills/`.
- Skipped: `sdd-*` (11 phase skills, loaded by the SDD orchestrator), `_shared`, `skill-registry`.
- Deduplication: first source in scan order wins (`opencode` > `claude` > `agents` > `gemini` > `qwen`/`kiro`/`openclaw`); project-level skills would win over user-level.
- Indexed: 35 skills (21 top-level + 14 session-synced).

## Registry

| Skill | Trigger (from description) | Scope | Path |
| --- | --- | --- | --- |
| branch-pr | creating, opening, or preparing Gentle AI PRs with issue-first checks | user (opencode) | `~/.config/opencode/skills/branch-pr/SKILL.md` |
| chained-pr | PRs over 400 lines, stacked PRs, review slices | user (opencode) | `~/.config/opencode/skills/chained-pr/SKILL.md` |
| cognitive-doc-design | writing guides, READMEs, RFCs, onboarding, architecture, review-facing docs | user (opencode) | `~/.config/opencode/skills/cognitive-doc-design/SKILL.md` |
| comment-writer | PR feedback, issue replies, reviews, Slack/GitHub comments | user (opencode) | `~/.config/opencode/skills/comment-writer/SKILL.md` |
| go-testing | Go tests, coverage, Bubbletea teatest, golden files | user (opencode) | `~/.config/opencode/skills/go-testing/SKILL.md` |
| issue-creation | creating GitHub issues, bug reports, feature requests | user (opencode) | `~/.config/opencode/skills/issue-creation/SKILL.md` |
| judgment-day | judgment day, dual review, adversarial review, juzgar | user (opencode) | `~/.config/opencode/skills/judgment-day/SKILL.md` |
| skill-creator | new skills, agent instructions, documenting AI usage patterns | user (opencode) | `~/.config/opencode/skills/skill-creator/SKILL.md` |
| skill-improver | improve skills, audit skills, refactor skills, skill quality | user (opencode) | `~/.config/opencode/skills/skill-improver/SKILL.md` |
| work-unit-commits | implementation, commit splitting, keeping tests and docs with code | user (opencode) | `~/.config/opencode/skills/work-unit-commits/SKILL.md` |
| humanizer | editing or reviewing prose for AI-sounding text | user (claude) | `~/.claude/skills/humanizer/SKILL.md` |
| research | preliminary research, research outline, academic/benchmark research | user (claude) | `~/.claude/skills/research/SKILL.md` |
| research-add-fields | add field definitions to an existing research outline | user (claude) | `~/.claude/skills/research-add-fields/SKILL.md` |
| research-add-items | add research objects to an existing research outline | user (claude) | `~/.claude/skills/research-add-items/SKILL.md` |
| research-deep | launch independent research agents per outline item | user (claude) | `~/.claude/skills/research-deep/SKILL.md` |
| research-report | summarize deep research results into a markdown report | user (claude) | `~/.claude/skills/research-report/SKILL.md` |
| ugc | /ugc, UGC ads, carousel/video prompt generation (PYNK UGC Studio) | user (claude) | `~/.claude/skills/ugc/SKILL.md` |
| find-skills | "how do I do X", "find a skill for X", discover/install skills | user (agents) | `~/.agents/skills/find-skills/SKILL.md` |
| orca-cli | "$orca-cli", Orca worktrees, terminals, automations, artifacts | user (agents) | `~/.agents/skills/orca-cli/SKILL.md` |
| orchestration | task dispatch, task DAGs, coordinator loops, worker handoff | user (agents) | `~/.agents/skills/orchestration/SKILL.md` |
| deep-research | multi-source research, trend/market analysis, literature review | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/deep-research/SKILL.md` |
| docs | creating/editing shareable documents (reports, proposals, guides), doc export | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/docs/SKILL.md` |
| docx | create/read/edit Microsoft Word `.docx` files | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/docx/SKILL.md` |
| pptx | any `.pptx`/`.potx` file: create, read, edit presentations | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/pptx/SKILL.md` |
| pdf | read, merge, split, fill, encrypt PDFs, OCR | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/pdf/SKILL.md` |
| xlsx | spreadsheet files as primary input/output (`.xlsx`, `.csv`, `.tsv`) | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/xlsx/SKILL.md` |
| google-workspace | creating/changing Google Docs, Sheets, Slides, Drive files | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/google-workspace/SKILL.md` |
| built-in-browser | first step using the built-in browser pane | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/built-in-browser/SKILL.md` |
| chrome-browser | first step with Claude in Chrome (extension browser) | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/chrome-browser/SKILL.md` |
| computer-use | controlling desktop apps on the user's computer, screenshots | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/computer-use/SKILL.md` |
| import-memory | import a memory export from another AI assistant | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/import-memory/SKILL.md` |
| morning | /morning brief as a styled HTML artifact or recurring task | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/morning/SKILL.md` |
| notebooklm | Google NotebookLM API (notebooks, sources, artifacts export) | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/notebooklm/SKILL.md` |
| flumix-carousel | "make a carousel about X", Flumix social media carousels | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/flumix-carousel/SKILL.md` |
| flumix-carousel-image-export | export carousel slides as individual PNGs | user (claude-synced) | `~/.claude/skills/synced/e940d511-168c-4e88-ba30-69769d2043e2_48fb1c8f-24c7-4837-b0b2-ae86b4f25153/flumix-carousel-image-export/SKILL.md` |

## Project Convention Files

| File | Role | Referenced files |
| --- | --- | --- |
| `.github/copilot-instructions.md` | Project agent instructions (Spanish): architecture gate, terminology (Persona / propietario de la agenda), OpenSpec workflow, quality rules | `docs/architecture.md`, `openspec/config.yaml`, `openspec/changes/{change}/` |
| `docs/architecture.md` | Approved architecture: layered (interfaz → API → servicios → repositorios → persistencia), approved tech list, out-of-scope list | — |
| `openspec/config.yaml` | SDD context, per-phase rules, operations guidance | — |

No `AGENTS.md`, `agents.md`, project-level `CLAUDE.md`, `.cursorrules`, or `GEMINI.md` in the project root.
