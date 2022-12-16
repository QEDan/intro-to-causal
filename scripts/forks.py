from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def plot_forks(n=1000, plot_dir='plots'):
    plot_dir = Path(plot_dir)
    xs = np.round(0.5 * stats.norm().rvs(n))
    ys = xs + 0.2 * stats.norm().rvs(n)
    zs = xs + 0.2 * stats.norm().rvs(n)
    plt.scatter(ys, zs)
    plt.savefig(plot_dir / 'fork.png')
    plt.close()
    plt.scatter(ys, zs, c=xs)
    plt.xlabel('Y')
    plt.ylabel('Z')
    plt.savefig(plot_dir / 'forks_colors.png')


if __name__ == '__main__':
    plot_forks()
