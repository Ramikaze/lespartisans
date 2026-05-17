import os
import re

def check_files():
    html_files = []
    js_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.gemini' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
            elif f.endswith('.js'):
                js_files.append(os.path.join(root, f))

    print("--- Checking Links ---")
    files_to_check = html_files + js_files
    for filepath in files_to_check:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Extract href="something" or src="something"
            links = re.findall(r'(?:href|src)=["\']([^"\'#]+)["\']', content)
            for link in links:
                if link.startswith('http') or link.startswith('mailto:') or link.startswith('data:'):
                    continue
                # Local link
                target_path = os.path.join(os.path.dirname(filepath), link)
                if '?' in target_path:
                    target_path = target_path.split('?')[0]
                if not os.path.exists(target_path):
                    print(f"[Broken Link] in {filepath} -> {link}")

    print("--- Done ---")

check_files()
