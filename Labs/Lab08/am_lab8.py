#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
matplotlib.use('TkAgg')


def load_table(data: Path):
    f = data.open()
    results = {}
    f.readline()
    for line in f:
        lineParts = line.split()
        results[lineParts[0]] = np.array(list(map(lambda n: float(n), lineParts[1:])))
    f.close()
    return results


def lp3(x, y):
    return lp(x, y, 3)


def lp(x, y, p):
    return np.sum((np.abs(x - y) ** p) ** (1 / p))


def cosine(x, y):
    return 1 - ((x.reshape((1, -1)) @ y.reshape((-1, 1))) /
                ((x.reshape((1, -1)) @ x.reshape((-1, 1))) ** 0.5) * ((y.reshape((1, -1)) @ y.reshape((-1, 1))) ** 0.5))


def weighted_jaccard_similarity(x, y):
    return np.sum(np.min([x, y], axis=0)) / np.sum(np.max([x, y], axis=0))


def weighted_jaccard_distance(x, y):
    return 1 - weighted_jaccard_similarity(x, y)


def samples2distances_table(samples):
    results = {}
    funcs = (('Cosine', cosine), ('lp3', lp3), ('WJD', weighted_jaccard_distance))

    for (f_name, f_ptr) in funcs:
        mat = np.zeros((len(samples.values()), len(samples.values())))
        for x in samples.values():
            i = j = 0
            for y in samples.values():
                mat[i][j] = f_ptr(x, y)
                j += 1
            i += 1
        results[f_name] = mat
    return results


def plot_distances(results, labels, figure):
    fig, ax = plt.subplots(1, len(results))
    funcs = ('Cosine', 'lp3', 'WJD')

    for i in range(3):
        ax[i].set_xticks(range(len(labels)), labels)
        ax[i].set_yticks(range(len(labels)))
        ax[i].imshow(results[funcs[i]], cmap='gray')
        ax[i].set_title(funcs[i])

    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


def run(data: Path, figure):
    data_table = load_table(data)
    print(data_table)
    distances = samples2distances_table(data_table)
    print(distances)
    plot_distances(distances, list(data_table.keys()), figure)


if __name__ == '__main__':
    run(Path('data.tsv'),
        None)
