import ray
import numpy as np


@ray.remote
def map(data, npartitions):
    outputs = [list() for _ in range(npartitions)]
    for row in data:
        outputs[int(row * npartitions)].append(row)
    return tuple(sorted(output) for output in outputs)

@ray.remote
def reduce(*partitions):
    # Flatten and sort the partitions.
    return sorted(row for partition in partitions for row in partition)

ray.init()
npartitions = 4
dataset = [np.random.rand(100) for _ in range(npartitions)]  # Random floats from the range [0, 1).
map_outputs = [
        map.options(num_returns=npartitions).remote(partition, npartitions)
        for partition in dataset]
outputs = []
for i in range(npartitions):
    # Gather one output from each map task.
    outputs.append(reduce.remote(*[partition[i] for partition in map_outputs]))
print(ray.get(outputs))

print('hello')