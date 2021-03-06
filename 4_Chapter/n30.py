def sentence_mapping(target):
    result = []
    for s in target:
        tmpL = []
        x = s[:-1].split('\n')
        for l in x:
            surface, tail = l.split('\t')
            sp = tail.split(',')
            tmpL.append({'surface': surface, 'base': sp[6], 'pos': sp[0], 'pos1': sp[1]})
        result.append(tmpL)
    return result


if __name__ == '__main__':
    with open("./neko.txt.mecab") as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        result = sentence_mapping(sentenceL)
        print(result)
