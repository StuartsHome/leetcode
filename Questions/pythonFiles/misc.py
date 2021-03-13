knights = {'word': 1, 'sentence': 2, 'paragraphs': 3}
for k, v in knights.items():
    print(k, v)

print(list(knights))
print(knights)

# Sorting on len of Dict

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(key=len)
print(cars)