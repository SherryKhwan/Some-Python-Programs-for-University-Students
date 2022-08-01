p=0
v=-1
a=1
while v<=0:
  v=input ("Enter Voucher Amount:Rs ", )
  v=eval(v)
while (a>0 and a<v and p!=v):
      a=input ("Enter Amount:Rs ")
      a=eval (a)
      if a>0:
        p=p+a
      if p>v:
        p=p-a
        print("Amount exceed Voucher limit, Please try again")
      print ("Purchase:Rs ",p)
b=v-p
print()
print ("1.Voucher Amount:\nRs",v)
print()
print ("2.Total Purchase:\nRs",p)
print()
print ("3.Balance Amount:\nRs",b)    