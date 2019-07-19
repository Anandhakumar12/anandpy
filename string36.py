a=str(input())
cott=0
for i in a:
    if i.isnumeric() or i.isalpha():
        pass
    else:
        cott+=1
print(cott)
