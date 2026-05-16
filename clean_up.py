import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

removed_count = 0
for part in data:
    for subpart in part.get('subparts', []):
        original_len = len(subpart.get('content', []))
        subpart['content'] = [h for h in subpart.get('content', []) if not ('number' in h and 421 <= int(h['number']) <= 612)]
        removed_count += original_len - len(subpart['content'])

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:start_idx] + new_json + content[end_idx:]

with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Removed {removed_count} hadiths!")
