def get_words():
    file = open("wordlist.txt", "r")
    words = file.readlines()
    file.close()
    return words

def get_anagrams(words):
    dic = {}
    for w in words:
        w = w.replace("\n","") #CAT | ATC
        word = ''.join(sorted(w)) #ACT | ACT
        if word not in dic:
            dic[word] = w #"ACT":"CAT"
        else:
            dic[word] += ','+w #ACT": "CAT","ATC"
    return dic

def delete_when_one(dic):
    og_dic = dict(dic)
    for k,word in dic.items():
        if "," not in word:
            og_dic.pop(k)
    return og_dic

words = get_words()
anagrams = get_anagrams(words)
final_list = delete_when_one(anagrams)
print(len(final_list))
