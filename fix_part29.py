import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Fix part 29 (which is at index 29)
part29 = data[29]
titles = [
    "La signification du nom du Mahdī",
    "La nécessité de l'Imām",
    "La bonne nouvelle du Mahdī ('aj)",
    "Les deux occultations de l'Imām al-Qā'im ('aj)",
    "La difficulté d'adhérer à la religion durant l'occultation",
    "L'invocation durant l'occultation du Qā'im ('aj)",
    "L'attente active de la délivrance",
    "La réapparition du Qā'im ('aj) après le désespoir des gens",
    "Ceux qui prédisent le moment mentent",
    "La raison de l'occultation",
    "Les personnes bénéficiant de l'Imām durant son occultation",
    "Les partisans du Qā'im",
    "Durant l'apparition",
    "Le monde après la réapparition du Mahdī ('aj)"
]

if len(part29['subparts']) < len(titles):
    part29['subparts'] = [{'title': title, 'content': []} for title in titles]

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:start_idx] + new_json + content[end_idx:]

with open('aune-sagesse-data.js', 'w') as f:
    f.write(new_content)

print("Fixed Part 29 subparts!")
