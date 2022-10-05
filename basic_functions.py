# for print
name= 'Sonali'
print('My name is:',name)
print('')

# If ou want don't want to end with new line
a='Sonali'
b='ok'
print(a,b,end='_')
print('')


# if you don't want space
print(a,b,sep='*')
print('')


# fromat specifier
value= 50
print('Value is :%d'%(value))

#or
print('So, name is :{}'.format(name))

#or
print('Your name is {name}'.format(name='Sonali'))

#or
c= 20
d=11
print(f'Additon of {c} & {d} is {c+d}')
print('')



# explicit type casting
m= int(input('Enter a number:')) #user input()
sum= m+10
print('So total value is',sum)
print('')

# for address of he variable
print('So address of a is:',id(a))
print('')


# for data type
print('Data type of a is:', type(a))
print('')

# type conversion
print('So, the float value of a is:', float(value))
print(bool(value))
print('')

# creation of list
l=[1,5,7,3,'Sona',[2],True]
print(l)
print('')


# slicing
city='Rourkela'
print(city[0:7])
print(city[::])
print(city[0:7:2])
print(city[::-1])
print('')

# import keyword
import keyword
print(keyword.kwlist)
print('')

#displaying random number between the range
import random
print(random.randint(50,60))







