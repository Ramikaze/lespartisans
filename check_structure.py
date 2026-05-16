import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

for i, part in enumerate(data):
    if i >= 16 and i <= 21:
        print(f"Part {i}: {part['title']}")
        for j, sub in enumerate(part['subparts']):
            if j < 3 or j > len(part['subparts']) - 3:
                print(f"  Subpart {j}: {sub['title']}")
            elif j == 3:
                print(f"  ...")
