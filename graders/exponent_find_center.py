base, power, mid = map(int, input().split())
result = base ** power
print(result)
s = str(result)
n = len(s)
start = (n - mid) // 2
end = start + mid
middle = s[start:end]
print(middle)