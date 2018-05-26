n = int(input("type your number: "))
prev = 1
current = 1

print(prev)
while current < n:
    print(current)
    next = current + prev
    prev = current
    current = next

