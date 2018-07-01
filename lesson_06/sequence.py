sequence = [0]

reversed_sequence = []
matches = 0
n = int(input("type the number of iterations: "))

for i in range(n):
    matches = 0
    for j in range(len(sequence)):
        if sequence[j] == sequence[len(sequence)-1 - j]:
            matches += 1
    sequence.append(matches)

for item in sequence:
    print(item)