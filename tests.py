#calculator basic
def calc():
    print('Calculator')
    x = int(input('First Number: '))
    op = input('Operator: ')
    y = int(input('Second Number: '))
    sum = 0
    error = 'That is no operator I know of'
    if op == '+':
        sum = x + y
        print(x, op, y, '=', sum)
    elif op == '-':
        sum = x - y
        print(x, op, y, '=', sum)
    elif op == '*':
        sum = x * y
        print(x, op, y, '=', sum)
    elif op == '/':
        sum = x / y
        print(x, op, y, '=', sum)
    else:
        print(error)

calc()

#sentence reverse

def reverse():
    print('Reverse')
    base = input('Enter your Sentence: ')
    sent = ''
    for i in base:
        sent = sent + i
    print(sent[::-1])

reverse()


#madlib

def mad():
    print('Madlib')
    a = input('Color: ')
    b = input('An object: ')
    c = input('City: ')
    d = input('Anything Plural: ')
    e = input('Animal: ')
    f = input('Object again: ')
    print('My face went', a, '. I was definetly sick. I used my',b,'to check if I had a fewer.',
          'This sickness ruined my holiday in',c, '. My head was full of',d,'so I didnt notice the charging',
          e,'. Thankfully I had my trusty', f, 'to defend myself.')
mad()


#prime number checker

def prime():
    print('Check if your number is prime')
    prnum = int(input('The number you would like to check: '))
    if prnum > 1:
        for i in range(2,prnum):
            if (prnum % i) == 0:
                print('Your number is not prime, sorry:(')
                break
        else:
            print('Your number is a prime, Nice:)')

prime()