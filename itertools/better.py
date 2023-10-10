import itertools as it
import ipdb


def better_grouper(inputs, n, fillvallue=None):
    iters = [iter(inputs)] * n
    ipdb.set_trace()
    return it.zip_longest(*iters, fillvalue=('ABCD'))

