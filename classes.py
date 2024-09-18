# ex 01
def printStars():
    someInt = int(input('Input a number'))
    null = 0
    for x in range(1,someInt+1, 2):
        null = int((someInt-x)/2)
        print(' '*null + '*'*x + ' '*null)
# printStars()

# ex 02
def multiplyElements(list):
    product = 1
    for x in list:
        product = product*x
    print(product)

# multiplyElements([1,2,3,4])

# ex 03
def higherNum(list):
    result = 0
    for x in list:
        if(x>result):
            result = x
    print(result)

# higherNum([34,60,101,200])

def addSubMult():
    flag = 'y'
    while(flag == 'y'):
        a = input('Input a number: ')
        b = input('Input a number: ')
        try:
            a = int(a)
            b = int(b)
        except:
            print('Invalid input. We need a number')
        mySum = a+b
        myProd = a*b
        myDif = a-b
        print("Sum: ", mySum, "Product:", myProd, "Difference:", myDif)
        cont = input('Would you like to continue? ')
        if(cont == 'n'):
            flag = 'n'


# addSubMult()
