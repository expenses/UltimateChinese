# coding: utf-8
import os


def add_chars(mappings, value, *path):
    for x in (
        open(os.path.join(os.environ["HSK_3_0_DIR"], *path))
        .read()
        .strip("\ufeff")
        .split()
    ):
        mappings[x] = value


def gen_mappings():
    mappings = {}
    add_chars(mappings, "7-9", "HSK List", "HSK 7-9.txt")
    add_chars(mappings, "7-9", "HSK Hanzi", "HSK 7-9.txt")
    add_chars(mappings, 6, "HSK List", "HSK 6.txt")
    add_chars(mappings, 6, "HSK Hanzi", "HSK 6.txt")
    add_chars(mappings, 5, "HSK List", "HSK 5.txt")
    add_chars(mappings, 5, "HSK Hanzi", "HSK 5.txt")
    add_chars(mappings, 4, "HSK List", "HSK 4.txt")
    add_chars(mappings, 4, "HSK Hanzi", "HSK 4.txt")
    add_chars(mappings, 3, "HSK List", "HSK 3.txt")
    add_chars(mappings, 3, "HSK Hanzi", "HSK 3.txt")
    add_chars(mappings, 2, "HSK List", "HSK 2.txt")
    add_chars(mappings, 2, "HSK Hanzi", "HSK 2.txt")
    add_chars(mappings, 1, "HSK List", "HSK 1.txt")
    add_chars(mappings, 1, "HSK Hanzi", "HSK 1.txt")
    return mappings
