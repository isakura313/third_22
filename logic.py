role = input("Введите вашу роль в проекте: ")
age = input("Введите ваш возраст: ")
age = int(age)

if role == "admin" and age > 18:
    print("У вас есть все права")
elif role == "user" and age> 16:
    print("У вас на этом проекте есть некоторые права")
else:
    print(" этот сервис закрыт на карантин")


