def even_odd(A):
    next_eve, next_odd = 0, len(A) - 1
    while next_eve < next_odd:
        if A[next_eve] % 2 == 0:
            next_eve += 1
        else:
            A[next_eve], A[next_odd] = A[next_odd], A[next_eve]
            next_odd -= 1
        print (A[next_eve], A[next_odd])


if __name__ == '__main__':
    next_eve = 0
    next_odd = 0
    A = [1, 2, 3, 4, 5, 6]
    even_odd(A)

