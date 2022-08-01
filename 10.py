n=-1
while n<=0:
    n=input("Enter Number:", )
    n=eval(n)
a=0
d=n
while d>1:
    d=d-1
    r=n%d
    if(r==0):
        a=a+1
if a>1:
    print (n, "is not a Prime Number.")
else:
    print (n, "is a Prime Number.")
    
#qpy:console


