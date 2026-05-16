import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

print(f"Total parts: {len(data)}")

for i in range(len(data)-5, len(data)):
    part = data[i]
    print(f"Index {i}: {part.get('title')}")
    for j, sub in enumerate(part.get('subparts', [])):
        print(f"  Subpart {j}: {sub.get('title')} - Hadiths: {len(sub.get('content', []))}")

