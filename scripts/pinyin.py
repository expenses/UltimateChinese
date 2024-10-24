from util import gen_pinyin
from anki.collection import Collection
import sys
col = Collection(sys.argv[1])
       
for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if note["Pinyin"].startswith("<") or len(note["Simplified"]) > 1:# or not note["Pinyin"].contains(set("1", "2", "3", "4")):
        continue
    if note["Pinyin"] != gen_pinyin(note["Simplified"]):
        print(f"{note["Simplified"]}, '{note["Pinyin"]}', '{gen_pinyin(note["Simplified"])}', {i}")
        note["Pinyin"] = gen_pinyin(note["Simplified"])
        #col.update_note(note)
        
