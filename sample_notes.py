from anki.collection import Collection
import random
import sys

col_filepath = sys.argv[1]
query = sys.argv[2]
count = int(sys.argv[3])
tag = sys.argv[4] if len(sys.argv) > 4 else None

print(tag)

col = Collection(col_filepath)

selected = col.find_notes(query)
print(len(selected))
sample = random.sample(selected, k=count)
print(len(sample))
notes = [col.get_note(id) for id in sample]
for note in notes:
    if tag:
        note.add_tag(tag)
        col.update_note(note)
    
