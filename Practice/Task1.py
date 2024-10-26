def sieve_of_erastothanes(n):
    table = list(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * 2, n + 1, i):
            if j in table:
                table.remove(j)
    return table


def least_common_multiple(a, b):
    a_table = prime_factorization(a)
    b_table = prime_factorization(b)
    if len(a_table) > len(b_table):
        for i in a_table:
            if i in b_table:
                b_table.remove(i)
    else:
        for i in b_table:
            if i in a_table:
                a_table.remove(i)
    final_table = a_table + b_table
    result = 1
    for i in final_table:
        result *= i
    return result


def prime_factorization(n):
    table = sieve_of_erastothanes(n)
    factors = []
    for i in table:
        while n % i == 0:
            factors.append(i)
            n = n / i
    return factors


print(sieve_of_erastothanes(100))
print(least_common_multiple(192, 348))
