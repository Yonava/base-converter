supportedChars = ['0','1','2','3','4','5',
'6','7','8','9','a','b','c','d','e',
'f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v']

def errorMsg(issue): return print(f'Error: {issue}')

def bB2Dec(num, base, conv, id):
    # supports up to base 32
    temp = []
    answer = []
    for x in num: temp.append(supportedChars.index(x))
    for i in range(len(temp)):
        answer.append(int(temp[::-1][i])*int(base)**i)
    if id == 0: return print(f'A: {sum(answer)}')
    dec2bB(sum(answer), conv)
    
def dec2bB(num, conv): 
    answer = []
    while True:
        answer.append(supportedChars[num % conv])
        num //= conv
        if num < 1: break
    return print('A: ', *answer[::-1], sep='')

def main():
    while True:
        numI, baseI, bConversionI = input('Enter A Number: '), input('Enter The Base: '), input('What Base Do You Want It In: ')
        if bConversionI == 'e': exit()
        else:
            if int(bConversionI) == 10: 
                numI = list(numI)
                bB2Dec(numI, baseI, int(bConversionI), 0)
            elif int(baseI) == 10: dec2bB(int(numI), int(bConversionI))
            else:
                numI = list(numI)
                bB2Dec(numI, baseI, int(bConversionI), 1)

if __name__ == "__main__": main()