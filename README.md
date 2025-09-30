# effective-broccoli

## Лабораторная работа 1

### Задание 1
```python
имя = str(input("Имя:"))
возраст = int(input("Возраст:"))
print(f"Привет, {имя}! Через год тебе будет {возраст+1}.")
```

### Задание 2
```python
имя = float(input("a:").replace(",","."))
возраст = float(input("b:").replace(",","."))
print(f"sum={имя+возраст}; avg={round((имя+возраст)/2,2)}")
```
![Картинка 1](./images/lab01/02_sum_avg.png)


### Задание 3
```python
price= int(input("price="))
discount=int(input("discount="))
vat=int(input("vat="))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base} ₽"
      f"\nНДС:               {vat_amount} ₽"
      f"\nИтого к оплате:    {total} ₽")
```
![Картинка 1](./images/lab01/03_discount_vat.png)


### Задание 4
```python
Минуты=int(input("Минуты: "))
print(Минуты//60,":",Минуты%60,sep="")
```
![Картинка 1](./images/lab01/04_minutes_to_hhmm.png)


### Задание 5
```python
f =str(input("ФИО:"))
g = f.split()
h = ""
for i in g:
    h+=i[0]
j = f.split(" ")
k= 0
jj=0
for i in j:
    if len(i)!=0:
        k+=1
        jj+=len(i)
print(f"Инициалы: {h}."
      f"\nДлина (символов): {jj+2}")

```
![Картинка 1](./images/lab01/05_initials_and_len.py.png)


### Задание 6
```python
f = int(input())
q,w=0,0
for i in range(f):
    _,_,_,g = input().split()
    if g == "True":
        q+=1
    else:
        w+=1
print(q,w)
```
![Картинка 1](./images/lab01/06.png)


### Задание 7
```python
i = str(input())
q,w=0,0
for t in range(len(i)):
    if i[t].upper() == i[t]:
        q = t
        break

for t in range(len(i)):
    if i[t] in ['0',"1","2","3","4","5",'6',"7","8","9"]:
        w = t+1
        break
print(i[q:len(i):w-q])
```
![Картинка 1](./images/lab01/07.png)

