


text = ("To be or not to be")
text = text.lower()
text = text.split(" ")
memo = {}
counter = 0


for i in text:
    if i in memo:
        memo[i].append(counter)
    else:
        memo[i] = [counter]
        counter += 1

print(memo)