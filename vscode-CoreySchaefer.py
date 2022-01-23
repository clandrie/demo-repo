message = 'Hello World'

print(message.count('Hello'))
print(message.count('l'))

print(message.find('e'))

new_message = message.replace('World','Universe')

print(message)

greeting = 'Hello'
name = 'Michael'

message2 = greeting + ', ' + name
print(message2)

message3 = greeting + ',' + name + '.Welcome!'
print(message3)

message4 = '{}, {}.Welcome to message 4!'.format(greeting,name)
print(message4)

#Advanced String Formatting
#String Concatenation is not ideal, complicated
person = {'name': 'Jenn','age': 23}
sentence = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence)

tag = 'h1'
text = 'This is a headline'
sentence2 = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence2)

#From Dictionary Can use key with placeholder
sentence3 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence3)

#can also access lists
list = ['Jenn', 23]
sentence4 = 'My name is {0[0]} and I am {0[1]} years old.'.format(list)
print(sentence4)

#can also access classes with placeholder
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack','33')
print(p1.name)
print(p1.age)

sentence5 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence5)

#Can also pass in keyword arguments to formate
sentence6 = 'My name is {name} and I am {age} years old.'.format(name='Jenn',age='30')
print(sentence6)

#keyword with dictionary; the two asterisks mean to UNPACK dictionary
#I need to learn unpacking still
personB = {'name': 'Bob', 'age': 40}
sentence7 = 'My name is {name} and I am {age} years old.'.format(**personB)
print(sentence7)

#7:01; loop through and form and print numbers
for i in range (1,11):
    sentence8 = 'The value is {:02}'.format(i)
    print(sentence8)

pi = 3.14159265
sentence9 = 'Pi is equal to {:02}'.format(pi)
print(sentence9)