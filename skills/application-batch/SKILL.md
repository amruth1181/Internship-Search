---
name: application-batch
description: Run a full application batch end to end - search, score, tailor a CV and cover letter per posting, zip the PDFs, and log everything in the tracker. Use when the user asks for "a batch", "20 applications", or "find roles and prepare everything".
---

# Application batch

Read `profile.md` first.

## Steps

1. **Search** with `internship-search` for the number the user asked for
   (default 20).
2. **Score** with `fit-score`. Show the list and scores. Wait for the user to
   confirm or drop postings before building documents, unless they said to go
   straight through.
3. **Number the final list once: 01, 02, 03…** This order is fixed from here
   on. The chat list, the folders and the tracker rows all use it.
4. **Tailor** a CV (`cv-tailor`) and cover letter (`cover-letter`) per posting
   into:

   ```
   batches/<YYYY-MM-DD>/
     01_<Company>/cv.tex, cover_letter.tex
     02_<Company>/...
     batch.md      <- the numbered list with links, scores and apply channel
   ```

5. **Build the zip:**

   ```
   python scripts/make_batch.py batches/<YYYY-MM-DD> --name "Firstname_Lastname"
   ```

   It compiles every folder, checks each PDF is one page, and writes a zip
   with **PDFs only**, in the same numbered folders.
6. **Check before sending.** Open the zip listing and confirm folder N holds
   the documents for posting N on the list, and that each letter names the
   right company. A numbering mismatch sends the wrong letter to the wrong
   company, so this check is not optional.
7. **Give the user** the zip and the numbered list with direct apply links.
8. **Log** each posting in the tracker after the user says it was submitted
   (see `templates/tracker_schema.md`): company, role, link, date, source,
   score, CV version, status "Applied". Don't mark something applied because
   documents were built.

## During applying

- Posting turned out closed, or the apply button is missing: mark it "Closed"
  or "To apply" in the tracker with a note. Don't silently drop it.
- A portal says the user already applied: stop and tell them; don't work
  around it.

## After the batch

Short summary: how many built, submitted, closed, still to apply. Remind the
user to update statuses when companies reply, because scoring and CV A/B
comparisons depend on it.
