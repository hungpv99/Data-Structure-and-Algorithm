import operator

def is_upper(word):
    return (word[0] >= 'A' and word[0] <= 'Z')

def get_words(path_file):
    f = open(path_file)
    content = f.read()
    f.close()
    content.replace(',', '')
    words = content.split(' ')
    return words

def get_frequencies(words):
    start_sentence = True
    long_word = []
    dic = {}

    #get ignore word
    f = open('Task 12/ignore.txt')
    ignore_word = f.read()
    f.close()

    for word in words:

        #if is not starting sentence
        if not start_sentence and word.lower() not in ignore_word:

            word = word.strip()

            #check finish sentence
            if word.endswith('.'):
                start_sentence = True
                word = word[:-1]
            else:
                start_sentence = False

            #check is uppercase
            if is_upper(word):
                long_word.append(word)
            else:
                if len(long_word) > 1:
                    tmp = ' '.join(long_word)
                    long_word = []
                    if tmp in dic:
                        dic[tmp] += 1
                    else:
                        dic[tmp] = 1

            #compute frequence of word
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        else:
            start_sentence = False
            long_word = []
        
        #sort by frequencies word
        dic_sorted = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    return dic_sorted

if __name__ == '__main__':
    print(get_frequencies(get_words('Task 12/test.txt')))