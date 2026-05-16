import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('[')
end_idx = text.rfind(']') + 1
data = json.loads(text[start_idx:end_idx])

changed = 0
for part in data:
    for sub in part.get('subparts', []):
        if 'content' in sub:
            # Check if there are any hadiths inside 'content'
            if sub['content']:
                if 'hadiths' not in sub:
                    sub['hadiths'] = sub['content']
                else:
                    # Merge if both exist and hadiths is empty
                    if not sub['hadiths']:
                        sub['hadiths'] = sub['content']
                    else:
                        # Append unique
                        for h in sub['content']:
                            if not any(existing_h.get('number') == h.get('number') for existing_h in sub['hadiths']):
                                sub['hadiths'].append(h)
            del sub['content']
            changed += 1

print(f"Changed {changed} subparts")

if changed > 0:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_text = text[:start_idx] + new_json + text[end_idx:]
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
