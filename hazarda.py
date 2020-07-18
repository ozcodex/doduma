from random import random, randrange, choice

numbers = ['0','1','2','3','4','5','6','7','8','9','X','E']

names = {
        '0':'nul',
        '1':'unu',
        '2':'du',
        '3':'tri',
        '4':'kvar',
        '5':'kvin',
        '6':'ses',
        '7':'sep',
        '8':'ok',
        '9':'naŭ',
        'X':'dek',
        'E':'elv'
        }

#random num generation

max_digits = 6
digits = randrange(max_digits) + 1

pows = ['','dod ', 'groc ', 'taŭs ', 'dod ', 'groc '][:digits]
pows.reverse()

# choose a first digit different from 0
dig = choice(numbers[-11:])
result = dig
name = ''
if not (dig == '1' and digits > 1):
    name += names[dig]
if digits > 1:
    name += pows.pop(0)

    # the rest of digits
    for p in pows:
        dig = choice(numbers)
        result += dig
        #if is 0 skip it
        if not dig == '0':
            name += names[dig]+p
        elif p == 'taŭs ':
            name += p

print ("digits: ", digits)
print ("number: ", result)
print ("text: ", name)
