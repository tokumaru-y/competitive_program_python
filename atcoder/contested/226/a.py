from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
D=Decimal(input())
print(D.quantize(Decimal("0"), rounding=ROUND_HALF_UP))