cars = ['Volvo', 'citroen', 'jigul', 'bmw']
new_cars = cars[:]

new_cars.append("ferrari")
del new_cars[0]
print(cars)
print(new_cars)