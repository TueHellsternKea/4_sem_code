import math, statistics, random, time, sys, locale
import ray
import numpy as np

def estimate_pi(num_samples, return_points=False):
    xs = np.random.uniform(low=-1.0, high=1.0, size=num_samples)
    ys = np.random.uniform(low=-1.0, high=1.0, size=num_samples)
    xys = np.stack((xs, ys), axis=-1)
    inside = xs*xs + ys*ys <= 1.0
    in_circle = xys[inside].shape[0]
    approx_pi = 4.0*in_circle/num_samples
    if return_points == False:
        return approx_pi, in_circle  # just return the estimate
    else:
        xys_in=xys[inside]
        xys_out=xys[~inside]
        return approx_pi, in_circle, xys_in, xys_out

class MonteCarloPi():
    def __init__(self):
        self.in_circle_count = 0
        self.total_count = 0

    def sample(self, num_samples):
        # Ignore the returned Pi, because we want to calculate it using accumulated values.
        _, in_circle, xys_in, xys_out = estimate_pi(num_samples, return_points=True)
        self.in_circle_count += in_circle
        self.total_count += num_samples
        return self.pi(), self.in_circle_count, self.total_count, xys_in, xys_out

    def pi(self):
        return 4.0*self.in_circle_count/self.total_count

# locale.setlocale(locale.LC_ALL, locale.getlocale())
def str_large_n(n, padding=None):
    if padding == None:
        padding=len(str(n))
    return locale.format_string(f'%{padding}d', n, grouping=True)

def compute_pi_for(Ns, compute_pi_loop):
    result_fmt = '~pi = {:8.6f} (stddev = {:7.6f}, error = {:7.6f}%), duration = {:9.5f} seconds'
    ns = []
    means = []
    stddevs = []
    errors = []
    durations = []
    for N in Ns:
        ns.append(N)
        print(f'# samples = {str_large_n(N)}: ', end='', flush=True)
        start = time.time()

        pis = compute_pi_loop(N)
        durations.append(time.time() - start)
        means.append(statistics.mean(pis))
        stddevs.append(statistics.stdev(pis))
        errors.append(abs(means[-1] - math.pi)*100.0/math.pi)
        print(result_fmt.format(means[-1], stddevs[-1], errors[-1], durations[-1]))
    return ns, means, stddevs, errors, durations


repeat=10  # We'll do this many calculations for a given N and average the results.

def compute_pi_loop(N):
    values = [MonteCarloPi().sample(N) for i in range(repeat)]
    return [approx_pi for approx_pi, inside_count, total_count, xys_in, xys_out in values]

@ray.remote
class RayMonteCarloPi(MonteCarloPi):
    @ray.method(num_returns=5)  
    def sample(self, num_samples):
        return super().sample(num_samples)


# No @ray.remote needed here, at least for our first optimizations.
def ray_compute_pi_loop(N):
    actors = [RayMonteCarloPi.remote() for _ in range(repeat)]
    pi_ids = [actor.sample.remote(N)[0] for actor in actors]  # only return the id for Pi values
    # ray.get blocks until all the tasks for the ids are finished.
    return ray.get(pi_ids)

def main():
    global repeat

    Ns = [500, 1000, 5000, 10000, 50000, 100000]

    import argparse
    parser = argparse.ArgumentParser(description="Monte Carlo Pi Calculator")
    parser.add_argument('Ns', metavar='N', type=int, default=Ns, nargs='*',
        help='Runs with the specified number of samples')
    parser.add_argument('-r', '--repeat', metavar='M', type=int, default=repeat, nargs='?',
        help='Repeat for each N, then compute average, stdev, etc.')
    parser.add_argument('-l', '--local', help="Run Ray locally. Default is to join a cluster",
        action='store_true')

    args = parser.parse_args()
    print(f"""
        {parser.description}
        Ns:           {args.Ns}
        Repeat per N: {args.repeat}
        Run locally?  {args.local}
        """)
    repeat = args.repeat

    print("\nResults without Ray:")
    ns, means, stddevs, errors, durations = compute_pi_for(args.Ns, compute_pi_loop)

    print("\nResults with Ray:")
    if args.local:
        ray.init(num_cpus=repeat)
    else:
        ray.init(address='auto')
    ray_ns, ray_means, ray_stddevs, ray_errors, ray_durations = compute_pi_for(args.Ns, ray_compute_pi_loop)

if __name__ == '__main__':
    main()