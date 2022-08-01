t=1  # total
b=2  #marks
while (t<b or b<0 or t<=0):
  b=input("Enter Marks Obtained:" ) 
  b=eval(b)
  t=input("Enter Total Marks:")
  t=eval(t)
p=b/t*100
print ("Percentage:",p,"%")      
