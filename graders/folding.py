num_str, size = input().split()
size = int(size)

chunks = [num_str[i:i+size] for i in range(0, len(num_str), size)]
print(" ".join(chunks))

total = sum(int(chunk) for chunk in chunks)
print(total)