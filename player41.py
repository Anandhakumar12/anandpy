a,b=map(int,input().split())
key=0
for i in range(1,a):
  da=b**i
  if a==da:
    break
if a==da:
  print("yes")
else:
  print("no")
