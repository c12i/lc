#!/usr/bin/env python3

"""
Script to migrate new LeetCode problems from /new directory to root directory.
Only migrates problems that don't already exist in the root.
Also generates README files for any problems missing them.
"""

import argparse
import os
import re
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

def extract_problem_info(dirname):
    """Extract problem number and name from directory name."""
    # Pattern: {number}-{problem-name}
    match = re.match(r'^(\d+)-(.+)$', dirname)
    if match:
        number = match.group(1)
        name_slug = match.group(2)
        # Convert slug to title case
        name = name_slug.replace('-', ' ').title()
        return number, name, name_slug
    return None, None, None

def create_readme(problem_dir, number, title, slug):
    """Create a README.md file for a problem if it doesn't exist."""
    readme_path = problem_dir / 'README.md'

    # Don't overwrite existing READMEs
    if readme_path.exists():
        return False

    content = f"# {number}. {title}\n\nhttps://leetcode.com/problems/{slug}/\n"

    with open(readme_path, 'w') as f:
        f.write(content)

    return True

def generate_missing_readmes(workspace_root):
    """Generate README files for all problems that are missing them."""
    print("\nChecking for missing README files...")
    created_count = 0

    for item in sorted(os.listdir(workspace_root)):
        item_path = workspace_root / item

        # Skip if not a directory or special directories
        if not item_path.is_dir() or item in ['new', '.git', '__pycache__']:
            continue

        # Extract problem info
        number, title, slug = extract_problem_info(item)

        if number and title and slug:
            if create_readme(item_path, number, title, slug):
                print(f"  ✓ Created README for: {number}. {title}")
                created_count += 1

    if created_count > 0:
        print(f"\nGenerated {created_count} missing README files")
    else:
        print("  All problems already have README files")

    return created_count

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Migrate new LeetCode problems from /new to root directory'
    )
    parser.add_argument(
        '--no-cleanup',
        action='store_true',
        help='Skip deleting problem directories from /new after migration'
    )
    args = parser.parse_args()

    # Get the script's directory (workspace root) and new directory
    workspace_root = Path(__file__).parent.absolute()
    new_dir = workspace_root / 'new'

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

    # Optionally delete all problem directories from /new
    if args.no_cleanup:
        print("Skipping cleanup of /new directory (--no-cleanup flag set)")
    else:
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

    # Generate README files for any problems missing them
    generate_missing_readmes(workspace_root)

    print()
    print("Done!")

if __name__ == "__main__":
    main()

