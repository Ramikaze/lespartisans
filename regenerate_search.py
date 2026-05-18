import json
import re

def clean_html(text):
    if not text:
        return ""
    # Strip HTML tags like <sup>, <em>, <strong>, <br>, <span>, etc.
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    # Collapse spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def regenerate_search_index():
    # 1. Load aune-sagesse-data.js
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        db_content = f.read()
    
    start_idx = db_content.find('[')
    end_idx = db_content.rfind(']') + 1
    db_data = json.loads(db_content[start_idx:end_idx])
    
    print(f"Loaded {len(db_data)} chapters from aune-sagesse-data.js")

    # 2. Load global-search-data.js
    with open('global-search-data.js', 'r', encoding='utf-8') as f:
        gs_content = f.read()
        
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
    
    # 3. Filter out old Aune de la Sagesse entries
    non_aune_entries = [e for e in gs_data if e.get('type') != 'Aune de la Sagesse']
    print(f"Kept {len(non_aune_entries)} non-Aune entries.")
    
    # 4. Generate new Aune de la Sagesse entries
    new_aune_entries = []
    for p_idx, part in enumerate(db_data):
        part_title = part.get('title', '')
        for s_idx, subpart in enumerate(part.get('subparts', [])):
            subpart_title = subpart.get('title', '')
            title = f"{part_title} — {subpart_title}"
            
            # Combine intro and hadiths
            intro = subpart.get('introduction', '')
            hadiths = [h.get('text', '') for h in subpart.get('hadiths', [])]
            full_text = " ".join([intro] + hadiths)
            
            cleaned_content = clean_html(full_text)
            # Truncate at 600 characters
            content_truncated = cleaned_content[:600]
            
            entry = {
                "type": "Aune de la Sagesse",
                "title": title,
                "content": content_truncated,
                "idx": 17,
                "state": f"{p_idx},{s_idx}"
            }
            new_aune_entries.append(entry)
            
    print(f"Generated {len(new_aune_entries)} new Aune entries.")
    
    # 5. Combine and sort or write back
    # To preserve the original sorting (Aune entries first, then others or vice-versa),
    # let's just append new Aune entries to the start or end of the list.
    # In the original file, they were mixed or in specific order. Let's see:
    # We can just put Aune entries first, then others, or maintain the exact insertion order.
    # Let's put new_aune_entries first, then non_aune_entries.
    final_gs_data = new_aune_entries + non_aune_entries
    print(f"Total entries in new index: {len(final_gs_data)}.")
    
    # 6. Write back
    new_gs_content = gs_content[:gs_match.start(1)] + json.dumps(final_gs_data, ensure_ascii=False) + gs_content[gs_match.end(1):]
    with open('global-search-data.js', 'w', encoding='utf-8') as f:
        f.write(new_gs_content)
        
    print("global-search-data.js updated and synchronized successfully!")

if __name__ == "__main__":
    regenerate_search_index()
