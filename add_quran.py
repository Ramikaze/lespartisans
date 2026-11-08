import json
import re

def update_global_search():
    # 1. Read Q from coran-texte.js (texte du Coran sorti de coran-lecture.html)
    with open('coran-texte.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'var Q=(\[.*?\]);\s*var surahNames', content, re.DOTALL)
    if not match:
        match = re.search(r'var Q=(\[.*?\]);', content, re.DOTALL)
        
    if not match:
        print("Could not find var Q=... in coran-texte.js")
        return

    q_json_str = match.group(1)
    
    # We must be careful because Q might have some trailing code if regex fails, but let's assume it's clean.
    try:
        q_data = json.loads(q_json_str)
    except Exception as e:
        print("Failed to parse Q JSON:", e)
        return
        
    print(f"Loaded {len(q_data)} surahs from Coran.")

    # 2. Build the entries
    entries = []
    for surah in q_data:
        surah_num = surah['n']
        surah_fr = surah['fr']
        for verse in surah['v']:
            verse_num = verse[0]
            verse_text = verse[1]
            
            entry = {
                "type": "Coran",
                "title": f"Sourate {surah_num}, Verset {verse_num}",
                "content": verse_text,
                "idx": 8,
                "state": f"{surah_num}-{verse_num}"
            }
            entries.append(entry)
            
    print(f"Created {len(entries)} entries for Coran.")

    # 3. Read global-search-data.js
    with open('global-search-data.js', 'r', encoding='utf-8') as f:
        gs_content = f.read()
        
    # Extract existing array
    gs_match = re.search(r'window\.GLOBAL_SEARCH_INDEX = (\[.*?\]);', gs_content, re.DOTALL)
    if not gs_match:
        print("Could not find GLOBAL_SEARCH_INDEX in global-search-data.js")
        return
        
    try:
        gs_data = json.loads(gs_match.group(1))
    except Exception as e:
        print("Failed to parse GLOBAL_SEARCH_INDEX:", e)
        return
        
    print(f"Loaded {len(gs_data)} existing global search entries.")
    
    # 4. Remove any existing Coran entries to avoid duplicates
    gs_data = [e for e in gs_data if e.get('type') != 'Coran']
    
    # 5. Append new entries
    gs_data.extend(entries)
    print(f"Total entries now: {len(gs_data)}.")
    
    # 6. Write back
    new_gs_content = gs_content[:gs_match.start(1)] + json.dumps(gs_data, ensure_ascii=False) + gs_content[gs_match.end(1):]
    
    with open('global-search-data.js', 'w', encoding='utf-8') as f:
        f.write(new_gs_content)
        
    print("global-search-data.js updated successfully!")

if __name__ == "__main__":
    update_global_search()
