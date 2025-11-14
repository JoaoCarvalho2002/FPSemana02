gooddic={

}

givenphrase=input()

for i in givenphrase:
    if i in gooddic:
        gooddic[i] = gooddic[i]+1
    else:
        gooddic[i] = 1 
        
print(gooddic)