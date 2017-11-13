```python

def sum10(number):
	sum = 0
	for i in number:
		sum += i
	return sum

one_to_ten = range(1,11)
result = sum10(one_to_ten)

print(result)

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
