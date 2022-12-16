from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def plot_chains(n=1000, plot_dir='plots'):
    plot_dir = Path(plot_dir)
    xs = stats.norm().rvs(n)
    ys = np.round(0.5 * xs)
    zs = ys + 0.4 * stats.norm().rvs(n)
    plt.scatter(xs, zs)
    plt.savefig(plot_dir / 'chain.png')
    plt.close()
    plt.scatter(xs, zs, c=ys)
    plt.savefig(plot_dir / 'chain_colors.png')
    plt.close()
    plt.scatter(xs, zs, c=np.round(xs - 2 * zs))
    plt.savefig(plot_dir / 'chain_sorted.png')
    plt.close()
    np.random.shuffle(ys)
    plt.scatter(xs, zs, c=ys)
    plt.savefig(plot_dir / 'chain_random.png')
    plt.close()


if __name__ == '__main__':
    plot_chains()
