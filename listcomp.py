l = [2,4,8,16]
[i*3 for i in l]
print(l)

cars = ['audi','bmw','benz','mazda','harrier']
cars.append('wish')
cars.insert(2,'premio')
print(cars)
print(cars[4].title())

message = (f"My first car was an "+ cars[0]+ ".")
print(message)

names = ['Drew','Kimani','Brayo','Ann','Faith',]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
del names[4]
print(names)
