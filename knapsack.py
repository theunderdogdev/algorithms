weights = [int(wt) for wt in input("Enter weights separated by spaces: ").split(" ")]
profits = [int(pft) for pft in input("Enter profits separated by spaces: ").split(" ")]
capacity = int(input("Enter knapsack capacity: "))
table = None


def prepare_memory():
    global table
    global weights
    global profits
    table = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    for item in range(len(weights) + 1):
        for kpc in range(capacity + 1):
            if item != 0 and kpc != 0:
                if kpc < weights[item - 1]:
                    table[item][kpc] = table[item - 1][kpc]
                else:
                    table[item][kpc] = max(table[item - 1][kpc],
                                           table[item - 1][kpc - weights[item - 1]] + profits[item - 1])


def take_decisions():
    prepare_memory()
    weights_included = [0] * len(weights)
    global table
    i = len(table) - 1
    j = len(table[0]) - 1
    max_val = table[i][j]
    while i != 0 and j != 0:
        print(i, j)
        if max_val not in table[i - 1]:
            weights_included[i - 1] = 1
            j -= weights[i - 1]
            i -= 1
            max_val = table[i][j]
        else:
            i -= 1
    return weights_included


print(take_decisions())
print(*table, sep="\n")

# Enter weights separated by spaces: 2 4 6 9
# Enter profits separated by spaces: 40 42 25 12
# Enter knapsack capacity: 10