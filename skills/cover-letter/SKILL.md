---
name: cover-letter
description: Write a tailored, human-sounding cover letter (or motivation answers for an application form) for a specific posting. Use when the user asks for a cover letter, lettre de motivation, or form answers.
---

# Cover letter

Read `profile.md` and the full job description. If the JD can't be accessed,
say so and ask the user to paste it.

Write in the language of the posting, unless it asks for another one.

## Shape (250–330 words, one page)

1. **Opening, two sentences.** What the role is and the one concrete reason
   this user fits it. No "I am writing to apply for".
2. **Proof.** One real story from a job or project that is close to the role's
   daily work: what was built, with what, and what happened. Real numbers only.
3. **Why this team.** One specific thing from the JD or the company's own
   material, connected to something the user has done. Don't repeat the ad's
   phrases back at it.
4. **Honest gap.** If the JD asks for something the user lacks (a tool, a
   language level, a work permit), name it in one sentence and say what the
   user is doing about it. Skip this only if there is no real gap.
5. **Close.** Availability line exactly as in the profile, school agreement if
   relevant, and a plain sign-off.

## Make it sound like a person

- First person, short sentences mixed with longer ones, paragraphs of uneven
  length.
- One small specific detail that only someone who did the work would know
  (what broke, what was learned).
- No: "passionate", "leverage", "cutting-edge", "I am confident that",
  "thrilled", lists of three adjectives, or a summary of the CV.
- No inflated metrics. If a number isn't in the profile, it doesn't exist.

## Application form answers

Same rules, shorter. Answer the question asked, in 2–5 sentences, with one
concrete example. If a form field would force a false answer (e.g. a required
residence the user doesn't have), tell the user and suggest contacting the
recruiter instead of entering something untrue.

## Build

- Use `templates/cover_letter_template.tex`, compile with `pdflatex`, check it
  is one page.
- Also give a plain-text version for pasting into forms.
- Name the file as the profile says (e.g. `Firstname_Lastname_Cover_Letter.pdf`).
