#
# usage: python n51.py {file name}
#


import sys
import re
from n50 import create_sentence_list


def remove_simbol(word):
    pattern = re.compile('[a-zA-Z]')
    for char in word:
        if re.match(pattern, char) is None:
            word = word.replace(char, '')
    return word


def get_word_list(sentence_list):
    word_list = []
    for s in sentence_list:
        tmp_wordlist = s.split()
        for i, word in enumerate(tmp_wordlist):
            tmp_wordlist[i] = remove_simbol(word)
        word_list.append(tmp_wordlist)
    return word_list


if __name__ == '__main__':
    fname = sys.argv[1]
    fdata = open(fname).read()
    fsentence_list = create_sentence_list(fdata)
    fword_list = get_word_list(fsentence_list)

    for sentence_i, fw in enumerate(fword_list):
        print('[{}]'.format(sentence_i+1))
        for w in fw:
            print(w)
        print()
