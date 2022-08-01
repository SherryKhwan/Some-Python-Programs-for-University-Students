m=-1
t=-2
f=-1
n=input("Enter Name:", )
while m>t:
  while m<0:
    m=input ("Marks Obtained:", )
    m=eval(m)
  while t<=0:
    t=input("Total Marks:", )
    t=eval(t)
while f<0:
  f=input ("Enter Full Fees:", )
  f=eval (f)
p=m/t*100
r=70/100*f
s=60/100*f
if p<=50:
  g="No Scholarship"
if p>60:
  g="You have 30% Scholarship"
if p>70:
    g="You have 40% Scholarship"
    print ("You have to pay Rs:",s)
if (p>60 and p<70):
  print ("You have to pay Rs:",r)
print (g)
