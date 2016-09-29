import random
from random import randint
import json
import urllib
def namescramble(s):
    s=s.lower()
    namearray=list(s)
    newname=[]
    for x in xrange(len(s)):
        cur= randint(0,len(namearray)-1)
        if x==0:
            newname.append(namearray[cur].upper())
            namearray.remove(namearray[cur])
        else:
            newname.append(namearray[cur])
            namearray.remove(namearray[cur])
    return "".join(newname)

def nameGuesser(s):
    htmltext=urllib.urlopen("https://raw.githubusercontent.com/dominictarr/random-name/master/names.json")
    data = json.load(htmltext)
    while(1):
        name=namescramble(s)
        if name in data:
            return name
        else:
            name=namescramble(s)
    return name

name= raw_input("Input Scrambled Name Here: ")
print nameGuesser(str(name))

    
