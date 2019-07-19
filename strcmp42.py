a,z=map(str,input().split())
co1=0
co2=0
for i in a:
    co1+=1
for i in z:
    co2+=1
if (co1>co2):
    print(a)
else:
    print(z)
