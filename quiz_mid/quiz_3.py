def quiz(datasets):
    dataset = datasets.split(';')
    result = []
    for data in dataset:
        chars = data.split(',')
        section = " ".join(chars)
        result.append(section)
        section = ""
    result.sort()
    result_reversed = reversed(result)
    return result_reversed

results = quiz(input())
for result in results:
    print(result)