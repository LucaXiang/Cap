#!/usr/bin/env python3
"""
Script to find all Rust files with let chains syntax and report them.
This helps identify files that need manual fixing for Rust 2021 compatibility.
"""

import os
import re
from pathlib import Path

def find_let_chains(directory):
    """Find all .rs files containing '&& let' pattern."""
    pattern = re.compile(r'&&\s*let\s+')
    results = []
    
    for root, dirs, files in os.walk(directory):
        # Skip target and node_modules directories
        dirs[:] = [d for d in dirs if d not in ['target', 'node_modules', '.git']]
        
        for file in files:
            if file.endswith('.rs'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = list(pattern.finditer(content))
                        if matches:
                            # Get line numbers
                            lines = content[:matches[0].start()].count('\n') + 1
                            results.append({
                                'file': filepath,
                                'count': len(matches),
                                'first_line': lines
                            })
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return results

if __name__ == '__main__':
    # Search in crates and apps directories
    all_results = []
    
    for search_dir in ['crates', 'apps']:
        if os.path.exists(search_dir):
            results = find_let_chains(search_dir)
            all_results.extend(results)
    
    if all_results:
        print(f"\nFound {len(all_results)} files with let chains syntax:\n")
        for r in sorted(all_results, key=lambda x: x['file']):
            print(f"  {r['file']}: {r['count']} occurrences (first at line {r['first_line']})")
        print(f"\nTotal: {sum(r['count'] for r in all_results)} occurrences in {len(all_results)} files")
    else:
        print("No let chains found!")
