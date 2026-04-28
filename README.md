# DSA Notes

A structured, pattern-driven system for tracking Data Structures & Algorithms problems, solutions, and progress.

## Structure

```
dsa-notes/
├── problems/          ← individual problem notes (markdown files)
├── patterns/          ← curated pattern indices and insights
├── sessions/          ← daily logs of what you worked on
├── db.json            ← lightweight metadata index
└── README.md          ← this file
```

## Quick Start

### 1. **Add a New Problem**

Create a file `problems/XXXX-problem-name.md` using the template in [problems/0217-contains-duplicate.md](problems/0217-contains-duplicate.md).

### 2. **Update the Index**

Add an entry to `db.json`:
```json
{
  "id": "0002",
  "name": "Add Two Numbers",
  "patterns": ["linked-lists"],
  "difficulty": "medium",
  "status": "unsolved",
  "followups": [],
  "file": "problems/0002-add-two-numbers.md",
  "last_seen": "2025-01-21"
}
```

### 3. **Log Your Session**

Create or update `sessions/YYYY-MM-DD.md` with what you solved and what's queued next.

## The Three Entities

- **Problems:** Individual LeetCode-style challenges with solutions and follow-ups
- **Patterns:** Curated indices grouping problems by technique (hashing, DP, sliding window, etc.)
- **Sessions:** Daily logs for tracking progress and follow-ups you haven't solved yet

## Querying with `jq`

List all unsolved problems:
```bash
jq '.problems[] | select(.status == "unsolved") | {id, name, patterns}' db.json
```

Find all problems using a specific pattern:
```bash
jq '.problems[] | select(.patterns[] == "hashing")' db.json
```

### Querying with Python

Use the included query script for easier access:

```bash
# List all unsolved problems
python3 scripts/query.py unsolved

# Find all problems using a pattern
python3 scripts/query.py pattern hashing

# Show queued follow-ups for a problem
python3 scripts/query.py followups 0217

# List all patterns
python3 scripts/query.py patterns
```

## Integration with GitHub

### GitHub Issues Workflow

Every queued follow-up gets its own GitHub Issue for tracking:

1. **Create an issue** when you queue a follow-up (e.g., from a session or parent problem)
   - Use the [followup issue template](.github/ISSUE_TEMPLATE/followup.md)
   - Title: `[FOLLOWUP] 00XX - Problem Name`
   - Labels: `followup` and `hashing`
   - Link to the parent problem in the issue body

2. **Link the issue** to the queued problem in your session log:
   ```markdown
   - [ ] [0015 - 3Sum](../problems/0015-three-sum.md) (#42 — queued 2025-01-20)
   ```

3. **Close the issue** when you solve the problem
   - Update `db.json` and the pattern index
   - Add a commit reference to the issue before closing

### GitHub Projects (Optional)

Create a Kanban board with columns:
- **To Do** — newly queued follow-ups
- **In Progress** — problem you're currently working on
- **Done** — solved problems

Automate: link issues to the project and let automation move cards based on issue state.

## Example Workflow

1. **Morning:** Open today's session file (`sessions/2025-01-21.md`)
2. **Solve a problem:** Add the note to `problems/`
3. **Link it:** Update the corresponding pattern index (e.g., `patterns/hashing.md`)
4. **Queue follow-ups:** Add unchecked items to the problem's follow-ups list
5. **End of day:** Update `db.json` and close the session log

---

**Why this approach?**

- **Portable:** Everything is markdown + JSON, works everywhere, version-controlled
- **Scalable:** `db.json` stays lightweight; query with simple tools (`jq`, Python, etc.)
- **Linked:** Problems reference patterns, patterns reference problems, sessions log context
- **Minimal overhead:** No database setup, no special tooling required