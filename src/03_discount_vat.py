price= int(input("price="))
discount=int(input("discount="))
vat=int(input("vat="))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base} ₽"
      f"\nНДС:               {vat_amount} ₽"
      f"\nИтого к оплате:    {total} ₽")