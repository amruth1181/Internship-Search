---
name: cv-tailor
description: Tailor the user's one-page LaTeX CV to a specific job posting. Use when the user asks for a CV for a posting, "tailor my CV", or as part of an application batch.
---

# CV tailoring

Read `profile.md` and the full job description. If the JD can't be accessed,
say so and ask the user to paste it. Don't tailor to a guessed JD.

## Rules

1. **Truth first.** Every line must come from the profile. Never add a tool,
   number or responsibility that isn't there. If the JD asks for something the
   user lacks, leave it off the CV; the cover letter can address the gap.
2. **Start from the right base CV.** Pick the language with the profile's CV
   language rule, and the base variant closest to the role.
3. **Leave the base CVs untouched.** Write the tailored copy to the batch
   folder (see `application-batch`).
4. **One page.** If it overflows, cut the weakest bullet before shrinking
   fonts or margins.

## What to change per posting

- **Headline:** the role title the posting uses, if it is honestly what the
  user does.
- **Profile paragraph:** 2–3 sentences. Lead with the experience closest to
  the job. No adjectives the user couldn't defend.
- **Skills:** reorder so the JD's tools come first in each row. Don't add
  rows of tools the user lacks.
- **Experience bullets:** keep the facts, reorder so the most relevant bullet
  is first. Use the JD's vocabulary only where it describes the same thing.
- **Projects:** choose 2–3 from the profile's project pool using each
  project's "use when" note. Put the closest match first. Don't repeat what
  the experience section already proves.
- **Availability line:** print it exactly as written in the profile.

## Writing style

- Plain verbs: built, ran, owned, cut. Not "architected", "spearheaded".
- Bold only real numbers and the two or three tools that matter most.
- Vary sentence length. No "Label: sentence" bullets.
- Keep technical terms in English on non-English CVs where that is the local
  convention.

## Build and check

1. Compile with `pdflatex`.
2. Render the PDF to an image and look at it: one page, nothing clipped, no
   orphan lines, links work.
3. If a portal rejects the PDF, rebuild with hyperlinks stripped (text kept).
4. Name the file as the profile says (e.g. `Firstname_Lastname_CV.pdf`).

## Tell the user

One or two lines: which base CV, which projects and why, and any JD
requirement the CV does not cover.

Template: `templates/cv_template.tex`.
