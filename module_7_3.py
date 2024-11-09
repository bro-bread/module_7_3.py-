import io
import string
from collections import Counter

class WordsFinder:
    def __init__(self, *file_):
        file = list(file_)
        self.file_names = file

    def get_all_words(self):
        dop_list = {}
        for i in self.file_names:
            with open(i, "r", encoding='utf-8') as file_r:
                clean_text = (file_r.read())
                clean_text1 = clean_text.replace(","," " )
                clean_text2 = clean_text1.replace(".", " ")
                clean_text3 = clean_text2.replace("="," ")
                clean_text4 = clean_text3.replace("!"," ")
                clean_text5 = clean_text4.replace("?", " ")
                clean_text6 = clean_text5.replace(";"," ")
                clean_text7 = clean_text6.replace(":"," ")
                clean_text8 = clean_text7.replace(' - '," ")
                clean_text9 = clean_text8.lower()
                clean_text10 = clean_text9.split()
                dop_list[i] = clean_text10
        return dop_list



    def find(self, word):
        print(" ")
        big = False
        if big == False:
            for u in self.file_names:
                with open(u, "r", encoding='utf-8') as file_r1:

                    clean_text = (file_r1.read())
                    clean_text1 = clean_text.replace(",", " ")
                    clean_text2 = clean_text1.replace(".", " ")
                    clean_text3 = clean_text2.replace("=", " ")
                    clean_text4 = clean_text3.replace("!", " ")
                    clean_text5 = clean_text4.replace("?", " ")
                    clean_text6 = clean_text5.replace(";", " ")
                    clean_text7 = clean_text6.replace(":", " ")
                    clean_text8 = clean_text7.replace(' - ', " ")
                    clean_text9 = clean_text8.upper()
                    clean_text10 = clean_text9.lower()
                    ddd = clean_text10.split()
                    word1 = word.upper()
                    word2 = word1.lower()
                    if word2 in ddd:
                        big = True
                        l_list = [s.lower() for s in ddd]
                        ind = ddd.index(word2) + 1
                        bibl = {word2:ind}
                        return bibl




    def count(self, word):
        for e in self.file_names:
            with open(e, "r", encoding="utf-8") as file_r2:

                clean_text = (file_r2.read())
                clean_text1 = clean_text.replace(",", " ")
                clean_text2 = clean_text1.replace(".", " ")
                clean_text3 = clean_text2.replace("=", " ")
                clean_text4 = clean_text3.replace("!", " ")
                clean_text5 = clean_text4.replace("?", " ")
                clean_text6 = clean_text5.replace(";", " ")
                clean_text7 = clean_text6.replace(":", " ")
                clean_text8 = clean_text7.replace(' - ', " ")
                clean_text9 = clean_text8.upper()
                clean_text10 = clean_text9.lower()
                ddd = clean_text10.split()

                counter = Counter(ddd)
                for key, value in counter.items():
                    if key == word.lower() or key == word.upper():
                        tyt = {e:value}
                        return tyt
                    else:
                        pass



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3-е слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
