'''find out if two words are anagrams of each other'''
word1=input('enter word1')
word2=input('enter word2')
word1=sorted(word1.lower(),key=ord)
word2=sorted(word2.lower(),key=ord)
print(word1==word2)