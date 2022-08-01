c=0
a=-1
while a<=0:
  a=input ("Enter Number:", )
  a=eval (a)
f=a
c=a
while c>1:
  c=c-1
  f=f*c
print ("Factorial of",a,":",f)S