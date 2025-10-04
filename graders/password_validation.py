passwords = input().split(',')

results = []
for pw in passwords:
    if 6 <= len(pw) <= 12:
        if (any(ch.islower() for ch in pw) and
            any(ch.isupper() for ch in pw) and
            any(ch.isdigit() for ch in pw) and
            any(not ch.isalnum() and not ch.isspace() for ch in pw)):
            results.append(pw)

print(','.join(results))