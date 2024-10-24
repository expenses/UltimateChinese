from util import gen_pinyin
from anki.collection import Collection
import sys
col = Collection(sys.argv[1])
       
for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "<" in note["Pinyin"] or "(" in note["Pinyin"] or "<" in note["Simplified"] or '"' in note["Simplified"] or note["Simplified"].startswith("A") or len(note["Simplified"]) > 5:
        continue
    fixed_simp = note["Simplified"].replace("\n", "").replace("&lt;br /&gt;B:", "\nB:")
    generated = gen_pinyin(fixed_simp, output_heteronyms=", " in note["Pinyin"])
    if note["Pinyin"] != generated:
        print(f"{note["Simplified"]}, '{note["Pinyin"]}', '{generated}', {i}")
        note["Pinyin"] = generated
        #col.update_note(note)
    if note["Simplified"] != fixed_simp:
        print(f"{note["Simplified"]}, '{fixed_simp}', {i}")
        note["Simplified"] = fixed_simp
        #col.update_note(note)
        
