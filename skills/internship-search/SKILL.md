---
name: internship-search
description: Find and shortlist internships that fit the user's profile. Use when the user asks to find internships, stages or intern roles, e.g. "find 20 data engineer internships", "any new roles this week", "search internships in Amsterdam".
---

# Internship search

Read `profile.md` first. If it doesn't exist, ask the user to copy
`profile.example.md` to `profile.md` and fill it in, then stop.

Everything below uses the profile: role tiers, geography, languages, contract
type, job sources, tracker and duplicate rule.

## 1. Build the "already applied" list before searching

- Read the tracker named in the profile (Notion database, spreadsheet or
  `tracker.csv`).
- Apply the user's duplicate rule. If none is given:
  - same company + same role (title or reference) → remove from results, don't
    count it toward the requested number;
  - same company, different role → keep it and say "already applied to
    <other role> here";
  - talent pools and cold pitches don't block new postings at that company.
- Keep searching until the requested number of *new* postings is reached. If
  the market can't supply that many good ones, return fewer and say why.

## 2. Search

Use whichever web search tool is available. Default freshness window: last
week, unless the user names another one.

- Run tier 1 queries first, in every language the user can apply in. Widen
  inside tier 1 (adjacent titles) before dropping to tier 2.
- Run at least one query per target country.
- Search each source in the profile. Useful `site:` patterns:
  - ATS boards: `site:jobs.ashbyhq.com OR site:job-boards.greenhouse.io OR
    site:jobs.lever.co OR site:apply.workable.com intern <role> <city>`
  - Welcome to the Jungle: `site:welcometothejungle.com <role> <city>`
    (search, then open individual job pages; the site's own search needs login)
  - LinkedIn: `site:linkedin.com/jobs/view <role> intern <city>`. Use search
    results only; don't scrape LinkedIn or Indeed pages.
  - Startup boards, national boards (e.g. Hellowork, APEC in France) and
    company early-careers pages for the target countries.
- School career portals (e.g. JobTeaser) usually need a login: remind the user
  to check theirs by hand.

## 3. Verify every posting before recommending it

Open the posting itself and check:

1. **Live and inside the freshness window.** "X hours ago" in search results is
   when the page was indexed, not when the job was posted. Confirm the date on
   the page. For Ashby / Greenhouse / Lever, the public job-board APIs give
   exact dates.
2. **Location** is really in the target geography.
3. **Contract type** matches the profile (internship vs apprenticeship vs
   graduate role). Mislabelled postings are common.
4. **Working language.** "English preferred" doesn't mean English is the
   working language. Flag language risk honestly.
5. **Duration and start date** are compatible.
6. **Eligibility traps:** must be enrolled at a local university, security
   clearance, work permit the user doesn't have.
7. Not on the "already applied" list.

If something can't be confirmed (e.g. a LinkedIn-only listing), say which part
is unconfirmed and ask the user to check on the page.

If a paid search tool with a credit budget is in use, scrape only postings
you're about to recommend and report credits used at the end.

## 4. Score

Score each verified posting with the `fit-score` skill. Only postings scoring
4 or more go in the main shortlist.

## Output

New postings only, grouped by language fit (best first), then role tier, best
score first. Per posting:

- Company, title, city, duration/start, link
- Posting age, and whether it was confirmed on the page or comes from the
  search index
- Language reality
- Score and a one-line reason tied to the user's real experience
- Which base CV to send and which projects to lead with
- Where to apply (portal, email, form)
- "Already applied to <other role> here" where relevant

Then:

- **Maybes:** postings scoring 3–3.5, one line each.
- **Left out:** notable exclusions and why (stale, wrong contract, language,
  eligibility).
- Count of already-applied postings skipped (count only, not the list).

## Style

Short, direct, copy-ready. Never pad the list to hit the number: three honest
matches beat twenty weak ones.
