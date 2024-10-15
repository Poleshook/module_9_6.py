def all_variants(text):
    n = len(text)
    for j in range(n):
        for k in range(j + 1, n + 1):
            yield text[j:k]


a = all_variants("abc")
for i in a:
    print(i)