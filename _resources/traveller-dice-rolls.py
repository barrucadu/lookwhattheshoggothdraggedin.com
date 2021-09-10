#! /usr/bin/env nix-shell
#! nix-shell -i python3 --packages "python3.withPackages(ps: [ps.matplotlib])"

import itertools
import matplotlib.pyplot as plt
import math
import sys

def chain_dm(effect):
    if effect <= -6:
        return -3
    if effect <= -2:
        return -2
    if effect <= -1:
        return -1
    if effect <= 0:
        return 0
    if effect <= 5:
        return 1
    return 2


def simulate_chain(mod1, mod2, target=0, combine=None):
    if combine is None:
        combine = lambda abc1, abc2: chain_dm(abc1) + abc2
    successes = 0
    trials = 0
    dice = itertools.product(range(1,7), range(1,7), range(1,7), range(1,7))
    for (dieA1, dieB1, dieA2, dieB2) in dice:
        if combine(dieA1 + dieB1 + mod1, dieA2 + dieB2 + mod2) >= target:
            successes += 1
        trials += 1
    print(mod1, mod2, successes, trials, successes / trials)
    return successes / trials


def simulate(modifiers, target=0, convert=None, eq=False, combine=None):
    if convert is None:
        convert = lambda x: x
    if combine is None:
        combine = lambda abc: abc[:2]
    successes = 0
    trials = 0
    dice = itertools.product(range(1,7), range(1,7), range(1,7))
    for (dieA, dieB) in map(combine, dice):
        if eq:
            if convert(dieA + dieB + modifiers) == target:
                successes += 1
        else:
            if convert(dieA + dieB + modifiers) >= target:
                successes += 1
        trials += 1
    print(modifiers, target, successes, trials, successes / trials)
    return successes / trials


plt.style.use('tableau-colorblind10')
plt.xkcd()

if sys.argv[1] == "basic.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    probabilities = {}
    for mod in range(-10, 11):
        probabilities[mod] = simulate(mod, target=8)
    xs = sorted(probabilities.keys())
    ys = [probabilities[x] for x in xs]
    plt.plot(xs, ys)

    plt.xlabel('Total Modifier')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "difficulties.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    for (name, tn) in [("Simple", 2), ("Easy", 4), ("Routine", 6), ("Average", 8), ("Difficult", 10), ("Very Difficult", 12), ("Formidable", 14), ("Impossible", 16)]:
        label = f"{name} ({tn}+)"
        probabilities = {}
        for mod in range(-10, 11):
            probabilities[mod] = simulate(mod, target=tn)
        xs = sorted(probabilities.keys())
        ys = [probabilities[x] for x in xs]
        plt.plot(xs, ys, label=label)

    plt.legend()
    plt.xlabel('Total Modifier')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "normalised-difficulties.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    probabilities = {}
    for mod in range(-26, 9):
        probabilities[mod] = simulate(mod)
    xs = sorted(probabilities.keys())
    ys = [probabilities[x] for x in xs]
    plt.plot(xs, ys)

    plt.xlabel('Total Modifier minus Difficulty Target')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "normalised-difficulties-trimmed.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    probabilities = {}
    for mod in range(-13, -1):
        probabilities[mod] = simulate(mod)
    xs = sorted(probabilities.keys())
    ys = [probabilities[x] for x in xs]
    plt.plot(xs, ys)

    plt.xlabel('Total Modifier minus Difficulty Target')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "boon-bane.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    for boon in [True, False]:
        for bane in [False, True]:
            if boon and bane:
                continue
            if boon:
                label = "Boon"
                combine = lambda rolls: sorted(rolls)[1:]
            elif bane:
                label = "Bane"
                combine = lambda rolls: sorted(rolls, reverse=True)[1:]
            else:
                label = "Normal"
                combine = lambda rolls: rolls[1:]
            probabilities = {}
            for mod in range(-13, -1):
                probabilities[mod] = simulate(mod, combine=combine)
            xs = sorted(probabilities.keys())
            ys = [probabilities[x] for x in xs]
            plt.plot(xs, ys, label=label)

    plt.legend()
    plt.xlabel('Total Modifier minus Difficulty Target')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "task-chain-dms.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    for tn in [-3, -2, -1, 0, 1, 2]:
        if tn <= 0:
            label = str(tn)
        else:
            label = f"+{tn}"
        probabilities = {}
        for mod in range(-20, 6):
            probabilities[mod] = simulate(mod, target=tn, convert=chain_dm, eq=True)
        xs = sorted(probabilities.keys())
        ys = [probabilities[x] for x in xs]
        plt.plot(xs, ys, label=label)

    plt.legend()
    plt.xlabel('Total Modifier minus Difficulty Target')
    plt.ylabel('Probability')

elif sys.argv[1] == "task-chain-heat.png":
    plt.figure(figsize=(10,10))

    modrange = list(range(-20, 6))
    data = [
        [ simulate_chain(mod1, mod2) for mod1 in modrange
        ] for mod2 in modrange
    ]
    data.reverse()

    plt.imshow(data, cmap='hot')
    plt.xticks([i for i in range(len(modrange))], modrange)
    plt.yticks([i for i in range(len(modrange))], reversed(modrange))
    plt.xlabel('First Check (Total Modifier minus Difficulty Target)')
    plt.ylabel('Second Check (Total Modifier minus Difficulty Target)')

elif sys.argv[1] == "task-chain-heat-unbound.png":
    plt.figure(figsize=(10,10))

    modrange = list(range(-20, 6))
    data = [
        [ simulate_chain(mod1, mod2, combine=lambda roll1, roll2: roll1 + roll2) for mod1 in modrange
        ] for mod2 in modrange
    ]
    data.reverse()

    plt.imshow(data, cmap='hot')
    plt.xticks([i for i in range(len(modrange))], modrange)
    plt.yticks([i for i in range(len(modrange))], reversed(modrange))
    plt.xlabel('First Check (Total Modifier minus Difficulty Target)')
    plt.ylabel('Second Check (Total Modifier minus Difficulty Target)')

elif sys.argv[1] == "try-again.png":
    plt.figure(figsize=(9,7)).gca().xaxis.get_major_locator().set_params(integer=True)

    for label in ["Normal", "Pushed", "Chained"]:
        probabilities = {}
        for mod in range(-13, -1):
            straight = simulate(mod)
            if label == "Normal":
                probabilities[mod] = straight
            elif label == "Pushed":
                probabilities[mod] = straight + (1 - straight) * straight
            elif label == "Chained":
                successes = 0
                trials = 0
                dice = itertools.product(range(1,7), range(1,7), range(1,7), range(1,7))
                for (dieA1, dieB1, dieA2, dieB2) in dice:
                    if dieA1 + dieB1 + mod >= 0:
                        successes += 1
                    elif chain_dm(dieA1 + dieB1 + mod) + dieA2 + dieB2 + mod >= 0:
                        successes += 1
                    trials += 1
                print(mod, successes, trials, successes / trials)
                probabilities[mod] = successes / trials
        xs = sorted(probabilities.keys())
        ys = [probabilities[x] for x in xs]
        plt.plot(xs, ys, label=label)

    plt.legend()
    plt.xlabel('Total Modifier minus Difficulty Target')
    plt.ylabel('Probability of Success')

elif sys.argv[1] == "opposed-heat.png":
    plt.figure(figsize=(10,10))

    modrange = list(range(-20, 6))
    data = [
        [ simulate_chain(mod1, mod2, combine=lambda abc1, abc2: abc1 - abc2) for mod1 in modrange
        ] for mod2 in modrange
    ]
    data.reverse()

    plt.imshow(data, cmap='hot')
    plt.xticks([i for i in range(len(modrange))], modrange)
    plt.yticks([i for i in range(len(modrange))], reversed(modrange))
    plt.xlabel('First Check (Total Modifier minus Difficulty Target)')
    plt.ylabel('Second Check (Total Modifier minus Difficulty Target)')

elif sys.argv[1] == "opposed-heat-chain-dm.png":
    plt.figure(figsize=(10,10))

    modrange = list(range(-20, 6))
    data = [
        [ simulate_chain(mod1, mod2, combine=lambda abc1, abc2: chain_dm(abc1) - chain_dm(abc2)) for mod1 in modrange
        ] for mod2 in modrange
    ]
    data.reverse()

    plt.imshow(data, cmap='hot')
    plt.xticks([i for i in range(len(modrange))], modrange)
    plt.yticks([i for i in range(len(modrange))], reversed(modrange))
    plt.xlabel('First Check (Total Modifier minus Difficulty Target)')
    plt.ylabel('Second Check (Total Modifier minus Difficulty Target)')

else:
    raise Exception("what?")

plt.savefig(sys.argv[1], bbox_inches='tight')
