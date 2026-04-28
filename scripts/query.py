#!/usr/bin/env python3
"""
Query helper for db.json — common DSA notes queries.
Usage: python3 scripts/query.py <command> [args]
"""

import json
import sys
from pathlib import Path

def load_db():
    """Load db.json from the repo root."""
    db_path = Path(__file__).parent.parent / "db.json"
    with open(db_path) as f:
        return json.load(f)

def list_unsolved():
    """List all unsolved problems."""
    db = load_db()
    unsolved = [p for p in db["problems"] if p["status"] != "solved"]
    
    if not unsolved:
        print("✅ All problems solved!")
        return
    
    print("Unsolved problems:")
    for p in unsolved:
        patterns = ", ".join(p["patterns"])
        print(f"  [{p['id']}] {p['name']} ({p['difficulty']}) — {patterns}")

def list_by_pattern(pattern_name):
    """List all problems using a specific pattern."""
    db = load_db()
    problems = [p for p in db["problems"] if pattern_name in p["patterns"]]
    
    if not problems:
        print(f"No problems found for pattern: {pattern_name}")
        return
    
    print(f"Problems using '{pattern_name}':")
    for p in problems:
        status = "✅" if p["status"] == "solved" else "🔄"
        print(f"  {status} [{p['id']}] {p['name']} ({p['difficulty']})")

def show_followups(problem_id):
    """Show queued follow-ups for a given problem."""
    db = load_db()
    problem = next((p for p in db["problems"] if p["id"] == problem_id), None)
    
    if not problem:
        print(f"Problem {problem_id} not found")
        return
    
    print(f"Follow-ups for [{problem['id']}] {problem['name']}:")
    if not problem.get("followups"):
        print("  (none)")
        return
    
    for followup_id in problem["followups"]:
        followup = next((p for p in db["problems"] if p["id"] == followup_id), None)
        if followup:
            status = "✅" if followup["status"] == "solved" else "⏳"
            print(f"  {status} [{followup['id']}] {followup['name']}")
        else:
            print(f"  ⏳ [{followup_id}] (not yet in db)")

def list_patterns():
    """List all patterns with problem counts."""
    db = load_db()
    pattern_counts = {}
    
    for problem in db["problems"]:
        for pattern in problem["patterns"]:
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    
    print("Patterns and problem counts:")
    for pattern, count in sorted(pattern_counts.items()):
        print(f"  {pattern}: {count} problem(s)")

def help_text():
    """Show help."""
    print("""
Usage: python3 scripts/query.py <command> [args]

Commands:
  unsolved              List all unsolved problems
  pattern <name>        List problems using a specific pattern
  followups <id>        Show queued follow-ups for a problem
  patterns              List all patterns with problem counts
  help                  Show this message
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_text()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "unsolved":
        list_unsolved()
    elif command == "pattern":
        if len(sys.argv) < 3:
            print("Error: pattern command requires a pattern name")
            sys.exit(1)
        list_by_pattern(sys.argv[2])
    elif command == "followups":
        if len(sys.argv) < 3:
            print("Error: followups command requires a problem ID")
            sys.exit(1)
        show_followups(sys.argv[2])
    elif command == "patterns":
        list_patterns()
    elif command == "help":
        help_text()
    else:
        print(f"Unknown command: {command}")
        help_text()
        sys.exit(1)
