import numpy as np

def simulate_once(seed=123):
    np.random.seed(seed)

    rand_float = np.random.rand()

    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)

    step = 50
    print(f"Before throw step = {step}")

    dice = np.random.randint(1, 7)

    if dice in (1, 2):
        step -= 1
    elif dice in (3, 4, 5):
        step += 1
    else:
        extra = np.random.randint(1, 7)
        step += extra

    print(f"After throw dice = {dice}")
    print(f"After throw step = {step}")

    return rand_float, dice1, dice2, dice, step


if __name__ == "__main__":
    rand_float, d1, d2, dice, step = simulate_once(seed=123)
    print(f"Random float: {rand_float}")
    print(f"Random integer 1: {d1}")
    print(f"Random integer 2: {d2}")
