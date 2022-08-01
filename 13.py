a=-1
b=2
t=0
c=1
m=c+1
while a<0:
  a=input("Enter Number:", )
  a=eval(a)
t=a
while b>0:
  b=input("Enter Number:", )
  b=eval(b)
  t=t+b
  if b>0:
    c=c+1
    m=m+1
A=t/c
print("Average of given",c,"numbers is:",A)  