stones = int(input("сколько камней: "))

while stones > 0:
    turn = int(input("сколько возьмете: "))
    if 1 <= turn <= 3 and turn < stones:
        stones = stones - turn

    print(stones)
