from decimal import Decimal
# dve raznovidnosti na decimal pri koito poluchavame razlichen rezultat

a = 0.1
b = 0.1
c = 0.1
print(a + b + c)

a = Decimal(0.1)
b = Decimal(0.1)
c = Decimal(0.1)
print(a + b + c)

a = Decimal("0.1")
b = Decimal("0.1")
c = Decimal("0.1")
print(a + b + c)