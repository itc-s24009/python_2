for i in range(10):
    if i % 2 == 0:
        print(i * 10)
        continue
    print(i)

print("breakにすると")
for i in range(10):
    if i % 2 == 0:
        print(i + 100)
        break
    print(i)
