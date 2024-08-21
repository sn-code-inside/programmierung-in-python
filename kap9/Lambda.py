lbd = lambda x: x + 21
print(lbd(21))
def lambdaAnwenden(x,liste):
    for l in liste:
        print(x(l))
lambdaAnwenden(lbd,[2,3,5,7,11])
lambdaAnwenden(lambda x: x * 2,[2,3,5,7,11])    

