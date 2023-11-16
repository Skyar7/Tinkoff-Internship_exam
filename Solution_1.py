A, B, C, D = map(int,input().split(' '))

if D > B:
    # Не уложился в тариф.
    print(A + C * (D - B))
else:
    # Уложился в тариф.
    print(A)