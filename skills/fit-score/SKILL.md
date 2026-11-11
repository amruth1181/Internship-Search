---
name: fit-score
description: Score a job or internship posting from 1 to 5 against the user's profile before they spend time applying. Use when the user asks "is this a good fit", "should I apply", "score this posting", or as part of a search batch.
---

# Fit score (1–5, apply at 4+)

Read `profile.md` first. Read the full job description, not the search
excerpt. If the JD can't be accessed, say so and ask the user to paste it.
Never score a guessed JD.

## Step 1: hard gates

Any of these caps the score at 2, whatever else looks good:

- wrong contract type (e.g. apprenticeship when the user needs an internship)
- posting closed, or older than the user's freshness limit with no sign it's
  still open
- a required language the user doesn't have at the stated level
- eligibility the user can't meet (local-university enrolment, citizenship,
  clearance, a work permit they can't get in time)
- seniority clearly above the user (e.g. "2+ years after graduation")

## Step 2: score five things

| Dimension | Weight | 5 looks like | 1 looks like |
|---|---|---|---|
| Role match | 30% | Tier 1 role, day-to-day work is what the user wants | Outside all tiers |
| Stack match | 30% | Most required tools are in the profile's verified skills or shown in a project | Almost none are |
| Evidence | 20% | The user has a job or project that is nearly this role | Nothing concrete to point to |
| Logistics | 10% | Target city, compatible dates and duration | Relocation plus date mismatch |
| Language and eligibility | 10% | No risk | Real risk, even if not a hard gate |

Weighted average, rounded to the nearest 0.5.

Count only skills in the profile. A tool the user has "heard of" is a gap.
Listing a gap is fine; hiding it is not.

## Step 3: decide

- **4–5:** apply. Say which base CV and which projects to lead with.
- **3–3.5:** maybe. Say what would make it worth it (e.g. referral, the user
  really wants this company).
- **Below 3:** skip, with the one reason that matters.

## Output per posting

```
<Company> — <Title>, <City>. Score X/5 → apply / maybe / skip
Why: one line tied to real experience ("Airflow + dbt, matches <job/project>")
Gaps: what the JD asks for that the profile lacks
Risks: language, permit, dates, anything unconfirmed
```

## Learning from results

When the tracker has replies, look at which scores, CV versions and sources
got interviews, and tell the user if the pattern suggests changing the
threshold or the weights. This only works if the user updates statuses.

The scoring idea is adapted from the open-source
[career-ops](https://github.com/santifer/career-ops) project.
