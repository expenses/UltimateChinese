# coding: utf-8
from hsk_3_mappings import gen_mappings
import sys
from anki.collection import Collection

col = Collection(sys.argv[1])

mappings = gen_mappings()
for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if note["Simplified"] in mappings:
        tag = f"UltimateChinese::HSK3.0::{mappings[note["Simplified"]]}"
        print(tag)
        note.add_tag(tag)
    col.update_note(note)
