import itertools as it


def better_grouper(inputs, n, fillvallue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=('ABCD'))

