import numpy as np
import matplotlib.pyplot as plt
import unittest


def simulate_multiple_walks_clumsy(n_walks=500, seed=123):
    np.random.seed(seed)
    all_walks = []

    for _ in range(n_walks):
        random_walk = [0]

        for _ in range(100):
            step = random_walk[-1]
            dice = np.random.randint(1, 7)

            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step += 1
            else:
                step += np.random.randint(1, 7)

            if np.random.rand() <= 0.005:
                step = 0

            random_walk.append(step)

        all_walks.append(random_walk)

    return np.array(all_walks)


def plot_end_steps_and_odds():
    all_walks = simulate_multiple_walks_clumsy(n_walks=500, seed=123)
    ends = all_walks[:, -1]

    prob_reach_60 = np.mean(ends >= 60)

    plt.figure()
    plt.hist(ends, bins=10)
    plt.title("Random walks")
    plt.xlabel("End step")
    plt.ylabel("Frequency")
    plt.show()

    # Odds of reaching at least 60 steps are about 60.8%.
    print(f"Odds of reaching at least 60 steps: {prob_reach_60 * 100:.1f}%")

    return prob_reach_60, ends


if __name__ == "__main__":
    prob, ends = plot_end_steps_and_odds()
    unittest.main(argv=["first-arg-is-ignored"], exit=False)