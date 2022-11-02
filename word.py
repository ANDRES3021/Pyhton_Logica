#!/usr/bin/python3

def count_word(texto):
    words=texto.split()
    i = 0
    while i < len(words):
        word=words[i]
        if word == words[-1]:
            i+=1
            break
        i+=1
    return(i)

print("please write a phrase or a word")
res = count_word(input())
print("the number of words is ",res)