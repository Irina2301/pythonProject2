quantity = int(input("Введите количество билетов: "))
age = [int(input("Введите возраст: "))for i in range(0, quantity)]
count = []
for i in range(len(age)):
    age[i] = int(age[i])
    if age[i] < 18:
        price = 0
        count.append(price)
        print(("Цена билета: "), price, ("руб"))
    elif 18 <= age[i] <= 25:
        price = 990
        count.append(price)
        print(("Цена билета: "), price, ("руб"))
    else:
        price = 1390
        count.append(price)
        print(("Цена билета: "), price, ("руб"))
e = int(sum(count))
if quantity > 3:
    e = e*0.9
    print("Полная стоимость билетов с учетом 10% скидки составит: ", e,("руб"))
else:
    print("Полная стоимость билетов составит: ", e, ("руб"))
