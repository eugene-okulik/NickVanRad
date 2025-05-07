temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def is_hot(x):
    return x > 28


hot_temperatures = list(filter(is_hot, temperatures))
minimum = min(hot_temperatures)
maximum = max(hot_temperatures)
avg = sum(hot_temperatures) / len(hot_temperatures)
print(maximum, minimum, avg)
