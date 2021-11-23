import itertools as it

def better_grouper(inputs, n, fillvallue=None):
    iters = [iter(inputs)] * n
    import ipdb; ipdb.set_trace()
    return it.zip_longest(*iters, fillvalue=('ABCD'))

