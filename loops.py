#Loops practice
for i in range(11):
    print (i * 1)

for i in range(11):
    print('* +', i)

'''
user_num = int(input('Pick a number for times tables'))

for i in range(13):
    print(user_num, '*', i, '=', user_num*i)
'''
for i in range(1,11):
    print('*', end = ' ')

name = 'Stephen'
counter = 0
for letter in name:
    print(letter, 'comes in ', counter)
    counter +=1


name = 'fiona'

counter = 0

for letter in name:
    print(letter, end = '')
    counter +=2

print(counter)

family = {'daddy':'stephen', 'mammy':'fiona', 'daughter':'saoirse'}
print(family['daddy'])

father = family.get('daddy')

print(father)