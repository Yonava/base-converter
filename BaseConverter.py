supportedChars = ['0','1','2','3','4','5',
'6','7','8','9','a','b','c','d','e',
'f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z']

def errorMsg(issue): return print(f'Error: {issue}')

def bB2Dec(num, base, conv, id):
    # supports up to base 36
    temp = [supportedChars.index(x) for x in num]
    answer = [int(temp[::-1][i])*int(base)**i for i in range(len(temp))]
    if id == 0: return print(f'Answer: {sum(answer)}')
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
        startUp = False
        while not startUp:
            numI, baseI, bConversionI = input('Enter A Number: '), input('Enter The Base: '), input('What Base Do You Want It In: ')
            if baseI.isdigit() and bConversionI.isdigit():
                startUp = True
            elif baseI == 'e' or bConversionI == 'e': return print("Quitting Program...")
            else: errorMsg("Bases must be integers...")
        numI = list(numI)
        for i in numI:
            if i not in supportedChars:
                errorMsg('Number Contains Unsupported Characters.')
                startUp = False
                break
            if supportedChars.index(i) >= int(baseI):
                errorMsg('Nononono, the base is all wrong!')
                startUp = False
                break
        if int(baseI) > len(supportedChars) or int(bConversionI) > len(supportedChars): errorMsg('Bases out of supported range.')
        elif int(bConversionI) == 10 and startUp: bB2Dec(numI, baseI, int(bConversionI), 0)
        elif int(bConversionI) != 10 and startUp: bB2Dec(numI, baseI, int(bConversionI), 1)

if __name__ == "__main__": main()
