import jieba
from pypinyin import pinyin

def gen_pinyin(hanzi_string):
    if len(hanzi_string) == 1:
        heteronyms = pinyin(hanzi_string, heteronym=True)
        
        return ' '.join(', '.join(''.join(heteronym) for heteronym in inner) for inner in heteronyms)
    segmented = jieba.cut(hanzi_string)
    return ' '.join(''.join((''.join(char) for char in pinyin(word))) for word in segmented)
