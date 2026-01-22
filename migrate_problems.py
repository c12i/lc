#!/usr/bin/env python3

"""
Script to migrate new LeetCode problems from /new directory to root directory.
Only migrates problems that don't already exist in the root.
"""

import os
import shutil
from pathlib import Path

def get_problem_directories(base_path):
    """Get all problem directories in a given path."""
    problems = set()
    if not os.path.exists(base_path):
        return problems
    
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item not in ['new', '.git']:
            # Only include directories that look like problem directories
            # (contain numbers or are problem-like names)
            if any(char.isdigit() for char in item) or item.startswith('README'):
                problems.add(item)
    
    return problems

def main():
    # Get the script's directory and workspace root
    script_dir = Path(__file__).parent.absolute()
    workspace_root = script_dir.parent
    new_dir = script_dir
    
    print(f"Workspace root: {workspace_root}")
    print(f"New directory: {new_dir}")
    print()
    
    # Get problem directories in both locations
    root_problems = get_problem_directories(workspace_root)
    new_problems = get_problem_directories(new_dir)
    
    print(f"Problems in root: {len(root_problems)}")
    print(f"Problems in /new: {len(new_problems)}")
    print()
    
    # Find problems that are only in /new
    problems_to_migrate = new_problems - root_problems
    
    if not problems_to_migrate:
        print("No new problems to migrate!")
        return
    
    print(f"Found {len(problems_to_migrate)} new problems to migrate:")
    for problem in sorted(problems_to_migrate):
        print(f"  - {problem}")
    print()
    
    # Migrate the problems
    migrated_count = 0
    failed_count = 0
    
    for problem in sorted(problems_to_migrate):
        src = new_dir / problem
        dst = workspace_root / problem
        
        try:
            print(f"Migrating: {problem}")
            shutil.copytree(src, dst)
            migrated_count += 1
        except Exception as e:
            print(f"  ERROR: Failed to migrate {problem}: {e}")
            failed_count += 1
    
    print()
    print(f"Migration complete!")
    print(f"  Successfully migrated: {migrated_count}")
    print(f"  Failed: {failed_count}")
    print()
    
    # Now delete all problem directories from /new
    print("Cleaning up /new directory...")
    deleted_count = 0
    delete_failed_count = 0
    
    for problem in sorted(new_problems):
        problem_path = new_dir / problem
        try:
            print(f"Deleting: {problem}")
            shutil.rmtree(problem_path)
            deleted_count += 1
        except Exception as e:
            print(f"  ERROR: Failed to delete {problem}: {e}")
            delete_failed_count += 1
    
    print()
    print(f"Cleanup complete!")
    print(f"  Successfully deleted: {deleted_count}")
    print(f"  Failed to delete: {delete_failed_count}")
    print()
    print("Done!")

if __name__ == "__main__":
    main()

