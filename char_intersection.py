interbase={

}
inter1={

}
inter2={

}
givenphrave1=input()
givenphrave2=input()

for i in givenphrave1.split():
    inter1[i] = inter1.get(i, 0)

for j in givenphrave2.split():
    inter2[j] = inter2.get(j, 0)

set1 = set(inter1.keys())
set2 = set(inter2.keys())

interbase = set1.intersection(set2) 

interbase = sorted(interbase)

for u in interbase[:-1]:
    print(u + " ")
if len(interbase) > 0:
    print(interbase[-1])
