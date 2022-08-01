a = -1
b = -2
c = 0
while (a<=0) :
  a = input ("Enter 1st Number:", )
  a = eval (a)
while (b<=0) :
  b = input ("Enter 2nd Number:", )
  b = eval (b)  
if (a>b):
  s = a
else:
  s = b 
while c==0:
  m = s % a
  n = s % b
  if n==0:
    if m==0:
      c = c + 1
      print ("LCM:",s)  
  s = s + 1