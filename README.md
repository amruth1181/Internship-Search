# Internship workflow

A set of Claude skills for running an internship search as a repeatable
process: find postings, score them, tailor a one-page CV and cover letter for
each, package the batch, and track what happens.

I built this while searching for a data internship in France as a
master's student. It is written for that situation (stages, conventions,
French and English postings) but everything personal lives in one profile
file, so it works for other fields and countries.

## What's inside

| Skill | What it does |
|---|---|
| `internship-search` | Finds fresh postings, verifies each on the page (date, contract type, language, eligibility) and skips ones you already applied to |
| `fit-score` | Scores a posting 1–5 against your real profile. Apply at 4+ |
| `cv-tailor` | Tailors a one-page LaTeX CV to the job description, using only true facts from your profile |
| `cover-letter` | Writes a short, human-sounding letter or form answers, with honest handling of gaps |
| `application-batch` | Runs all of the above for a batch (e.g. 20 postings), zips the PDFs in numbered folders and logs to your tracker |

Plus:

- `profile.example.md` — the one file you fill in
- `templates/cv_template.tex`, `templates/cover_letter_template.tex` — blank one-page templates
- `templates/tracker_schema.md` — columns for a Notion database, spreadsheet or CSV
- `scripts/make_batch.py` — compiles a batch, checks every PDF is one page, zips PDFs only

## Setup

1. Clone the repo.
2. Copy `profile.example.md` to `profile.md` and fill it in. It is
   git-ignored, so your details stay local.
3. Put your own content in a copy of `templates/cv_template.tex`. One base CV
   per role type and language is enough.
4. Create your tracker from `templates/tracker_schema.md`.
5. Add the skills to Claude:
   - **Claude Code:** copy the folders in `skills/` to `.claude/skills/` in
     your project (or `~/.claude/skills/`).
   - **Claude app:** zip each skill folder, upload it as a custom skill, and
     add `profile.md` to a Project.
6. Install a LaTeX distribution with `pdflatex` if you want to build PDFs
   locally.

A web search tool is needed for searching. A Notion connector is optional.

## Use

```
find 20 data engineer internships in Paris from the last week
score this posting: <link or pasted JD>
tailor my CV and write a cover letter for #3
run a batch of 20 and zip everything
```

Build a batch by hand:

```
python scripts/make_batch.py batches/2026-11-02 --name "Firstname_Lastname"
```

## Principles

- **Nothing invented.** If a skill or number isn't in your profile, it doesn't
  go on a CV or in a letter.
- **Read the real job description.** No tailoring to a guess.
- **Score before you apply.** Fewer, better applications.
- **Numbering is sacred.** The list, the folders and the tracker share one
  order, so the right letter reaches the right company.
- **Track replies.** It is the only way to learn what works.

## Credits

The 1–5 scoring idea is adapted from
[career-ops](https://github.com/santifer/career-ops).

## Licence

MIT
