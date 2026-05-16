import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# The parts and subparts we know exist in update_data_batch.py
required = {
    20: 4,
    22: 3,
    24: 3
}

for part_idx, count in required.items():
    part = data[part_idx]
    while len(part['subparts']) < count:
        part['subparts'].append({"title": f"Subpart {len(part['subparts'])}", "content": []})

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:start_idx] + new_json + content[end_idx:]

with open('aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Fixed subparts!")
