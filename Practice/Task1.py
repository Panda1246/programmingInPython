def sieveOfErastothanes(n):
    table = list(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            if j in table:
                table.remove(j)
    return table
def leastCommonMultiple(a, b):
    aTable = primeFactorization(a)
    bTable = primeFactorization(b)
    if len(aTable)>len(bTable):
        for i in aTable:
            if i in bTable:
                bTable.remove(i)
    else:
        for i in bTable:
            if i in aTable:
                aTable.remove(i)
    finalTable = aTable + bTable
    result = 1
    for i in finalTable:
        result *= i
    return result

def primeFactorization(n):
    table = sieveOfErastothanes(n)
    factors = []
    for i in table:
        while n % i == 0:
            factors.append(i)
            n = n / i
    return factors

print(sieveOfErastothanes(100))
print(leastCommonMultiple(192,348))