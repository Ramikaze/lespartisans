import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

highest = 0
for part in data:
    for sub in part.get('subparts', []):
        for h in sub.get('content', []):
            if 'number' in h:
                try:
                    num = int(h['number'])
                    if num > highest:
                        highest = num
                except ValueError:
                    pass

print(f"Highest hadith number found: {highest}")
