# Application tracker

One row per posting. Use a Notion database, a spreadsheet, or a plain
`tracker.csv`; the skills only need these columns.

| Column | Type | Notes |
|---|---|---|
| Company | text | |
| Position | text | Exact title, plus reference number if there is one |
| Status | select | To apply · Applied · Interview · Offer · Rejected · Closed · No reply |
| Link | url | Direct link to the posting |
| Source | select | Where you found it (school portal, WTTJ, LinkedIn, company site…) |
| Date applied | date | |
| Score | number | From `fit-score` |
| CV version | text | Which base CV and which projects, so you can compare what works |
| Batch | text | e.g. `2026-11-02 #07` (batch date + number on the list) |
| Notes | text | Contact names, caveats, what went wrong |

## Rules

- **Applied means submitted**, not "documents built".
- **Update Status when a company replies.** Without it, nothing can tell you
  which scores, CV versions or sources lead to interviews.
- **Pick one duplicate rule and write it in your profile.** Strict: "company
  already in the tracker → skip". Loose: "same company + same role → skip".
- If someone else adds rows for you, add a column that marks who added it, so
  their rows aren't mistaken for your applications.

## CSV header

```
Company,Position,Status,Link,Source,Date applied,Score,CV version,Batch,Notes
```
