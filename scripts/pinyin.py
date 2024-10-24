from util import gen_pinyin
from anki.collection import Collection
import sys
col = Collection(sys.argv[1])
       
for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "<" in note["Pinyin"] or "(" in note["Pinyin"] or note["Pinyin"] != "" or "<" in note["Simplified"] or len(note["Simplified"]) != 1:
        continue
    if note["Pinyin"] != gen_pinyin(note["Simplified"]):
        print(f"{note["Simplified"]}, '{note["Pinyin"]}', '{gen_pinyin(note["Simplified"])}', {i}")
        note["Pinyin"] = gen_pinyin(note["Simplified"])
        #col.update_note(note)
        
