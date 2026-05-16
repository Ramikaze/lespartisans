import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

for i in [20, 22, 24, 29]:
    print(f"Part {i} ({data[i]['title']}) has {len(data[i]['subparts'])} subparts")

