import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Delete 517-639
for part in data:
    for subpart in part.get('subparts', []):
        subpart['content'] = [h for h in subpart.get('content', []) if not ('number' in h and 517 <= int(h['number']) <= 639)]

all_updates = []

import ast

for filename in ['add_batch_1.py', 'add_batch_2.py', 'add_batch_3.py']:
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())
        # Find the assignments to 'updates'
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'updates':
                        # Evaluate the list of tuples
                        all_updates.extend(ast.literal_eval(node.value))

# Also we have 586 to 639 in `extract_and_inject.py` as `new_hadiths` which is a dict.
with open('extract_and_inject.py', 'r') as f:
    src = f.read()
    dict_src = src[src.find('new_hadiths = {') : src.find('for k, v in new_hadiths.items():')]
    # We can just extract it manually or use my previous python dict.
