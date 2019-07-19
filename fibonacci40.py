a=int(input())
n1=0
n2=1
while a>0:
  nth=n1+n2
  print(n2,end=' ')
  n1=n2
  n2=nth
  a=a-1
