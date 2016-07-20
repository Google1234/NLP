'''
import sys
usrargv = sys.argv
print usrargv
print usrargv[0]
print usrargv[1]
'''
import spell_check
import sys
if __name__ == "__main__":
    usrargv=sys.argv
    if len(usrargv)==1:
        trie = spell_check.make_trie_from_txtFile("english_words.txt") # The default file
    else:
        trie = spell_check.make_trie_from_txtFile(usrargv[1])
    check = spell_check.spell_check(trie)
    while 1:
        word=raw_input("word:")
        #max_distance=int(raw_input("max distance:"))
        #TopK=int(raw_input("return numbers:"))
        #check.spell_check(word, max_distance, TopK)
        check.spell_check(word)