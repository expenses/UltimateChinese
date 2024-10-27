# coding: utf-8
from anki.collection import Collection

col = Collection("/home/ashley/.local/share/Anki2/UltimateChinese/collection.anki2")
for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    print(note["SentenceSimplified"])

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note:
        print(note["SentenceSimplified"], note["SentencePinyin"])

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note:
        print(note["SentenceSimplified"], note["SentencePinyin"])

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note and note["SentencePinyin"] == "":
        print(note)

from scripts.fix_pinyin import gen_pinyin
from scripts.util import gen_pinyin

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note and note["SentencePinyin"] == "":
        print(gen_pinyin(scripts["SentenceSimplified"]))

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note and note["SentencePinyin"] == "":
        print(gen_pinyin(note["SentenceSimplified"]))

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note and note["SentencePinyin"] == "":
        note["SentencePinyin"] = gen_pinyin(note["SentenceSimplified"])

for i, note in enumerate(col.get_note(id) for id in col.find_notes("")):
    if "SentenceSimplified" in note and note["SentencePinyin"] == "":
        note["SentencePinyin"] = gen_pinyin(note["SentenceSimplified"])
        col.update_note(note)
