import re
import time

correctionmade=0
dword = []
def loadwords():
    f=open("dictionarywords.txt",'r')
    for wr in f:
        dword.append(wr.strip())
def typedistance(w1,w2):
    w1=" "+w1
    w2=" "+w2
    l1=len(w1)
    l2=len(w2)
    matrix = [[0 for _ in range(l2)]for _ in range(l1)]
    i=0
    j=0
    while(i<l1):
        matrix[i][0]=i
        i+=1
    while(j<l2):
        matrix[0][j]=j
        j+=1
    i=0
    while(i<l1):
        j=0
        while(j<l2):
            if(not(i==0 or j==0)):
                if(w1[i]!=w2[j]):
                    matrix[i][j]=min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])+1
                else:
                    matrix[i][j] =  matrix[i - 1][j - 1]
            j+=1
        i+=1
    return matrix[l1-1][l2-1]
def checkspell(word,k2):
    global correctionmade
    d=0
    maxd=0
    dictionary=dict()
    for word2 in dword:
        d=typedistance(word.lower(),word2)
        if d==0:
            return 0
        if maxd<d:
            maxd=d
        dictionary[word2]=d
    noOfTerms=0
    k=1
    print(f"suggestion for correct word '{word}' at position no {k2+1} are as follows : ")
    correctionmade+=1
    while k<=maxd:
        for terms in dictionary.keys():
            if noOfTerms<10 and dictionary[terms]==k:
                print(f"{terms}")
                noOfTerms+=1
                if(noOfTerms==10):
                    return 1
        k+=1

print("WELCOME TO SPELL CHECKER APPLICATION")
print("THIS APP IS MADE BY IMON MALLIK")
print("VERSION : 1.0\n\n")
print("ENTER A PARAGRAPH : ")
para = input()
words = re.findall(r'\b\w+\b', para)
# print(words)
loadwords()
k=0
for i in words:
    k+=1
    if i.isdigit()==True:
        continue
    result = checkspell(i,k-1)
if correctionmade==0:
    print("THE FULL PARAGRAPH HAS NO SPELLING ERROR")

if correctionmade==0:
    correctionmade=2
time.sleep(5*correctionmade)