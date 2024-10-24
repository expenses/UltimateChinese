import jieba
from pypinyin import pinyin

def gen_pinyin(hanzi_string):
    output = ""
    if len(hanzi_string) == 1:
        heteronyms = pinyin(hanzi_string, heteronym=True)
        
        output = ' '.join(', '.join(''.join(heteronym) for heteronym in inner) for inner in heteronyms)
    else:
        segmented = jieba.cut(hanzi_string)
        output = ' '.join(''.join((''.join(char) for char in pinyin(word))) for word in segmented)
    return output.replace("！", "!").replace(" !", "!").replace("。", ".").replace(" .", ".").replace(" ？", "?").replace("，", ",").replace(" ,", ",").replace("、", "-")
