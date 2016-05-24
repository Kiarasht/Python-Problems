def count_by(x, n):
    my_list = []

    for i in range(x, (n*x)+1, x):
        my_list.append(i)

    return my_list

print(count_by(100, 5))
