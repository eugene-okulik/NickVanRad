def progression():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


targets = {5, 200, 1000, 100000}
results = {}

count = 1
for number in progression():
    if count in targets:
        results[count] = number
        if len(results) == len(targets):
            break
    count += 1

for i in sorted(results):
    print(f"{i}-е число Фибоначчи: {results[i]}")
