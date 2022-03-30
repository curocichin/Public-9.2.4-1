input("Нажмите Enter:\n")

age0 = int(input("До 18 лет возраст.Введите количество билетов:\n"))
age1 = int(input("С 18 лет до 25 лет возраст.Введите количество билетов:\n"))
age2= int(input("С 25 лет старше возраст.Введите количество билетов:\n"))

prace0 = 0
prace1 = 990
prace2 = 1390

a = age1+age2
print("Ценна")
if a > 3:
   if a >3:
     a = ((age1 * prace1) + (age2 * prace2)) - (((age1 * prace1) + (age2 * prace2))* 0.10)

     print(a)
else:
    a =(age1 * prace1) + (age2 * prace2)
    print(a)
