def royxatni_2_qismga_boling(royxat):
    return royxat[:len(roxat)//2], royxat[len(roxat)//2:]

# Misol royxat
roxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ro'yxatni 2 qismga bo'lish
qism1, qism2 = royxatni_2_qismga_boling(roxat)

print("Qism 1:", qism1)
print("Qism 2:", qism2)
```

```python
def royxatni_2_qismga_boling(royxat):
    n = len(roxat)
    return royxat[:n//2], royxat[n//2:]

# Misol royxat
roxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ro'yxatni 2 qismga bo'lish
qism1, qism2 = royxatni_2_qismga_boling(roxat)

print("Qism 1:", qism1)
print("Qism 2:", qism2)
