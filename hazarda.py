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

def getPows(digits):
    pows = ['','dod ', 'groc ', 'taŭs ', 'dod ', 'groc '][:digits]
    pows.reverse()
    return pows


def toText(number):
    parts = list(number)
    digits =len(parts)
    pows = getPows(digits)
    name = ''
    #process first digit
    dig = parts.pop(0)
    if not (dig == '1' and digits > 1):
        name += names[dig]
    if digits > 1:
        name += pows.pop(0)
    for dig in parts:
        p = pows.pop(0)
        #if is 0 or 1 skip it
        if not (dig == '0' or dig == '1'):
            name += names[dig]+p
        elif p == 'taŭs ' or (dig == '1' and not p == ''):
            name += p
            
    return name

def getRandom():
    #random num generation
    max_digits = 6
    digits = randrange(max_digits) + 1
    # choose a first digit different from 0
    dig = choice(numbers[-11:])
    result = dig
    # the rest of digits
    for p in range(digits - 1):
        dig = choice(numbers)
        result += dig
    return result

num = getRandom()
name = toText(num) 
print ("number: ", num)
print ("text: ", name)
