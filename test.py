def handle(n):
    empty_list = []
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        empty_list.append([a, b])
    return empty_list
