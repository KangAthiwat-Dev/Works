def quiz(n, m, dataset):
    dataset.sort()
    sum_max = list(reversed(dataset))
    sum_n_base = 0
    for i in range(n):
        sum_n_base += sum_max[i]
    sum_m_worst = sum(dataset[:m])
    return "{},{}".format(sum_n_base, sum_m_worst)
    
n = int(input())
m = int(input())
dataset = list(map(int, input().split(',')))
result = quiz(n, m, dataset)
print(result)