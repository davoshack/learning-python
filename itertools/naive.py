def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    print(num_groups)
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

for _ in naive_grouper(range(10), 10):
    pass

