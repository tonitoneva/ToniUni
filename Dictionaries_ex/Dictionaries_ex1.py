counts_dict = {}
word = input()
new_word = []
for c in list(word):
    if c != ' ':
        new_word.append(c)

for c in list(new_word):
    if c not in counts_dict:
        counts_dict[c] = 0
    counts_dict[c] += 1

for key, value in counts_dict.items():
    print(f"{key} -> {value}")


