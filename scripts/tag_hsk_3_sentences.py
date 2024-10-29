from anki.collection import Collection
from hsk_3_mappings import gen_mappings
import jieba
import sys

mappings = gen_mappings()


def get_level_for_sentence(sentence):
    level = None
    for word in jieba.cut(sentence):
        if word not in mappings:
            continue
        if level == None:
            level = mappings[word]
        elif mappings[word] == "7-9":
            level = mappings[word]
        elif level != "7-9":
            level = max(mappings[word], level)
    return level


col = Collection(sys.argv[1])

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    level = get_level_for_sentence(note["Simplified"])

    if level is None:
        continue
    tag = f"UltimateChinese::HSK3.0::{level}"
    print(tag)
    # note.add_tag(tag)
    # col.update_note(note)
