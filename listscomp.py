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

for index,name in enumerate(names):
    print(index,name)

motocycles = ['honda','suzuki','yamaha','tvs']
popped_bike = motocycles.pop()
print(popped_bike)
print(motocycles)
print(f"The last bike i owned was"+" "+popped_bike.title())
first_owned = motocycles.pop(0)
print(f"The first owned bike was"+" "+first_owned)


courses = ['history','physics','maths','computer']
courses2 = ['french','biology']
nums = [1,4,7,9,3]

print(courses[-1])
print(courses[0:2])    #slicing
#list methods
courses.append('Art') #adds item at the end of the list
print(courses)

courses.insert(1, 'agriculture') #adds item at specific position
print(courses)

courses.extend(courses2)  #used when we have multiple values we wanna add to our list
print(courses)

courses.remove('physics')
print(courses)

courses.pop()
print(courses)#removes last item and returns value that was removed

courses.reverse()
courses.sort()

print(courses.index('maths'))

for index,course in enumerate(courses):
    print(index,course)

course_str = ', '.join(courses)
print(course_str)

#list comprehensions
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)

under_10 = [ x for x in range(10)]
print('under_10:'+ str(under_10))

squares = [x**2 for x in under_10]
print('square:'+ str(squares))

ten_x = [x*10 for x in range(10)]
print('ten_x:'+ str(ten_x))

odds = [x for x in range(10) if x%2==1]
print('odds:'+str(odds))

s = 'I love 2 g0 to the store 7 times a we3k'
num = [x for x in s if x.isnumeric()]
print('num:'+ ''.join(num))
