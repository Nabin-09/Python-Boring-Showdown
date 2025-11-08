import random
from decimal import Decimal

l1 = ['Argentina' , 'India' , 'Nepal' , 'Bangladesh']
print(random.choice(l1))
random.shuffle(l1)
print(l1) 

 
 #Bangladesh
 # ['Nepal', 'Argentina', 'India', 'Bangladesh']

print((0.1 +0.1 +0.1) - 0.3) #5.551115123125783e-17 therefore use the decimal package for apt calculations

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1') - Decimal('0.2')) #0.1
