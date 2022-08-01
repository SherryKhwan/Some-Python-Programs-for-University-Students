x = 0
y = 0
z = 0
i = 0
while (i != 0.3 ):
  if i > 0:
   x = x + 1
  if i < 0:
   y = y + 1
  if i == 0:
   z = z + 1
  i = input ("Enter Any Number: ")
  i = eval (i)
print ("Number of Positive numbers: ",x)
print ("Number of Negative numbers: ",y)
print ("Number of zeros: ",z)