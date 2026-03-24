x=input("enter strings: ").split()

sorted_all=[''.join(sorted(i)) for i in x]
sorted_all.sort()

anagrams=[]
inner=[]
for i in sorted_all:
    if not inner:
        inner.append(i)
        print(inner)
    else:
        if inner[0]==i:
            inner.append(i)
        else:
            anagrams.append(inner)
            inner=[i]
anagrams.append(inner)

print(anagrams)