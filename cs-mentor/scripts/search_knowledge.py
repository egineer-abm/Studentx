# Knowledge Search Script
# This script searches for a term across semesters and guides directories.

import os
import sys

def search_knowledge(search_term):
    search_dirs = ['../semesters', '../guides']
    results = []
    
    for dir_path in search_dirs:
        if not os.path.exists(dir_path):
            continue
            
        for filename in os.listdir(dir_path):
            if filename.endswith(".md"):
                file_path = os.path.join(dir_path, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_term.lower() in content.lower():
                        results.append(file_path)
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_knowledge.py <term>")
        sys.exit(1)
        
    term = sys.argv[1]
    matches = search_knowledge(term)
    
    if matches:
        print(f"Found '{term}' in:")
        for match in matches:
            print(f"- {match}")
    else:
        print(f"No results for '{term}'.")
