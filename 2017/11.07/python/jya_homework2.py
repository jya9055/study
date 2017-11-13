```python

i = -1
sum = 0

one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while i < 10:
	i += 1
	sum += one_to_ten[i]

print(sum)

```

**Make function!**
`like:`
```python
def sum(number):
    # .. TODO
    return 0
```

`I want to reuse this function, like:`
```python
one_to_ten = sum(range(1,11))
one_to_five = sum(range(1,6))
five_to_ten = sum(range(5,11))
```
