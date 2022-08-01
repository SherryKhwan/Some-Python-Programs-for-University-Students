p=-3
while (p<0 or p>100):
  p=input ("Enter percentage:" )
  p=eval(p)
g="Fail"
if (p>=50):
  g="E"
if (p>=60):
  g="D"
if (p>=70):
  g="B"
if (p>=80):
  g="A"
print("Grade:",g)      
