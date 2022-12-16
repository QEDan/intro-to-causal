from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def plot_colliders(n=1000, plot_dir='plots'):
    plot_dir = Path(plot_dir)
    xs = np.round(100 * stats.norm().rvs(n))
    ys = np.round(100 * stats.norm().rvs(n))
    zs = xs + ys
    plt.scatter(xs, ys)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(plot_dir / 'collider.png')
    plt.close()
    plt.scatter(xs, ys, c=zs)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(plot_dir / 'collider_colors.png')


if __name__ == '__main__':
    plot_colliders()
