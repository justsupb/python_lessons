def rec_test(n):
    if n==0:
        return 1
    print(f'результат: {rec_test(n-1)*n}')
    print(n)
    return rec_test(n-1)*n
print(rec_test(3))