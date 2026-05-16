import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

for i in range(35, 50):
    part = data[i]
    print(f"Index {i}: {part.get('title')} (Subparts: {len(part.get('subparts', []))})")
    if i in [45, 46, 47]:
        for j, sub in enumerate(part.get('subparts', [])):
            print(f"  Subpart {j}: {sub.get('title')} - Hadiths: {len(sub.get('content', []))}")

