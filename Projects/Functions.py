def m1():
    print('Hello World')
m1()

def m2(name='no name'):
    print('Hello {}'.format(name))
m2()

def m3(x):
    if x == True:
        return 'correct'
    elif x == False:
        return 'incorrect'
print(m3(1))

def m4(x,y,z):
    if z:
        # print(x)
        return x
    else:
        # print(y)
        return y

def m5(x,y):
    return x+y