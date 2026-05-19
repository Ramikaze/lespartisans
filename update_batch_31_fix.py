import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(pi, ss):
    for s in data[pi].get('subparts', []):
        if ss in s['title']:
            return s
    return None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# FIX: Remove wrongly placed hadiths 2064-2069 from section 683
# ============================================================
P_istikhara = 139
s683 = find_subpart(P_istikhara, "683")

# Remove hadiths numbered 2064 through 2069 (these were wrong estimates)
s683['hadiths'] = [h for h in s683['hadiths'] if int(h['number']) >= 2070]
print(f"Section 683 after cleanup: {len(s683['hadiths'])} hadiths (should be 6: 2070-2075)")

# ============================================================
# Add correct hadiths from page 370 to Chapter 137 (index 138)
# ============================================================
P_bien = 138

# Section 681 - Ce qui est meilleur que le bien
s681 = find_subpart(P_bien, "681"); eh(s681)
s681['hadiths'].extend([
    {"number": "2064", "text": "L'Imām 'Alī (as) a dit : Il n'y a de meilleur que le bien que sa récompense.<sup>2335</sup>"},
    {"number": "2065", "text": "L'Imām al-Ṣādiq (as) a dit : Meilleur que la vérité est celui qui la profère ; meilleur que le bien est celui qui le fait.<sup>2336</sup>"},
    {"number": "2066", "text": "L'Imām al-Hādī (as) a dit : Meilleur que le bien est celui qui le fait ; plus beau que les beaux [mots] est celui qui les dit ; supérieur au savoir est son détenteur.<sup>2337</sup><br><br><span class=\"reference-note\">(Voir également : 214. Le mal, section 1017)</span>"}
])

# Section 682 - Le mérite de celui qui indique le bien
s682 = find_subpart(P_bien, "682"); eh(s682)
s682['hadiths'].extend([
    {"number": "2067", "text": "Le Messager d'Allah (s) a dit : Celui qui indique le bien est comme celui qui le fait.<sup>2338</sup>"},
    {"number": "2068", "text": "Le Messager d'Allah (s) a dit : Celui qui indique le bien a la même rétribution que celui qui le fait.<sup>2339</sup>"}
])

# Insert hadith 2069 at the beginning of section 683
s683['hadiths'].insert(0, {
    "number": "2069",
    "text": "Le Messager d'Allah (s) a dit : Lorsque tu envisages de faire quelque chose, demande le bien et consulte ton Seigneur à son sujet sept fois. Ensuite, observe ce qui vient dans ton cœur en premier lieu : en vérité, le bien se trouve en cela, c'est-à-dire agis en fonction de cela.<sup>2340</sup>"
})

print(f"Section 683 final: {len(s683['hadiths'])} hadiths (should be 7: 2069-2075)")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Page 370 fix applied! Sections 681, 682, 683 corrected.")
