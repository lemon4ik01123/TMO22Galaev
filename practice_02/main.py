def pages_per_day(pages, days):
    if days == 0:
        return 'На ноль делить нельзя'
    return pages / days
assert pages_per_day(84, 7) == 12
assert pages_per_day(10, 0) == 'На ноль делить нельзя'
assert pages_per_day(50, 5) == 10

words = ['том', 'книга', 'энциклопедия']
result = sorted(words, key=lambda word: len (word))
print(result)