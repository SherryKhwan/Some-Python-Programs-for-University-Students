c = 0
a = -5
b = -4
while a<=0:
    a = input ("Enter 1st number:", )
    a = eval (a)
while b<=0:
    b = input ("Enter 2nd number:", )
    b = eval (b)
if (a>b):
    e = b
else:
    e = a
while (c==0):
    m = a % e
    n = b % e
    if m==0:
        if n==0:
            print ("HCF/GCD:",e)
            c = c + 1
    e = e - 1
    
