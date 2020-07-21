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

pows = ['dod','groc','taŭs']


def d3toText(number):
    print("converting",number)
    #create text string for 3 digit number
    if not len(number) == 3:
        return "!!!error!!!"
    grocoj = number[0]
    dodoj = number[1] 
    unuoj = number [2]
    name = ''
    if not (grocoj == '0'):
        if not (grocoj == '1'):
            name += names[grocoj]
        name += pows[1] + ' '
    if not (dodoj == '0'):
        if not (dodoj == '1'):
            name += names[dodoj]
        name += pows[0] + ' '
    if not (unuoj == '0'):
        name += names[unuoj]
    return name

def addZero(number):
    #add zeroes at begining to complete digits in order of 3
    mod = len(number)%3
    if mod == 0:
        return number
    out = '0' * (3 - mod)
    out += number
    return out

def splitIn3(number):
    n = 3
    lst = list(addZero(number))
    lst = [lst[i:i + n] for i in range(0, len(lst), n)]
    out = []
    for i in lst:
        out.append("".join(i))
    return out

def toText(number):
    digits =len(number)
    #check if the number is nul
    if number == '0' * digits:
        return 'nul'
    parts = splitIn3(number)
    pw = len(parts) - 1 #pow
    text = ''
    for part in parts:
        text += d3toText(part)
        if pw > 0:
            text += " " + pows[2]
            if pw > 1:
                text += '-je-' + names[str(pw)]
            text += " "
        pw -= 1
    return text

def add(a,b):
    if not (len(a) == 1 and len(b) == 1):
        return '!!!error!!!'
    index_a = numbers.index(a)
    index_b = numbers.index(b)
    index_c = index_a + index_b
    out = ''
    if index_c >= len(numbers):
        out += '1' #carry
        index_c = index_c - len(numbers)
    out += numbers[index_c]
    return out


def getRandom():
    #random num generation
    max_digits = 12
    digits = randrange(max_digits) + 1
    # choose a first digit different from 0
    dig = choice(numbers[-11:])
    result = dig
    # the rest of digits
    for p in range(digits - 1):
        dig = choice(numbers)
        result += dig
    return result


for i in range(5):
    num = getRandom()
    name = toText(num) 
    print ("number: ", num)
    print ("text: ", name)


