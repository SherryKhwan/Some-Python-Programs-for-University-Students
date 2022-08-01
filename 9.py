r = -5
x = -3
y = -5
z = -7
while r<=0:
  r = input ("Enter Roll Number:" )
  r = eval (r)
while x<0:
  x = input ("Marks obtained in 1st subject:", )
  x = eval (x)
while y<0:
  y = input ("Marks obtained in 2nd subject:", )
  y = eval (y)
while z<0:
  z = input ("Marks obtained in 3rd subject:", )
  z = eval (z)
t = x + y + z
a = t / 3
g = "Fail"
if (a>=50):
  g = "C"    
if (a>=60):
  g = "B"    
if (a>=70):
  g = "A"          
if (a>=80):
  g = "A+"
print ("Roll Number:",r)
print ("Total marks obtained:",t)
print ("Average/Percentage:",a,"%")
print ("Grade:",g)        