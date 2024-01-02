def transformation(die_a, die_b):
    x=0
    condA = [1, 2, 3, 4]
    length = 6
    current = []
    combinations = []
    condB = [1, 2, 3, 4, 5, 6, 7, 8]
    start = 0
    DICE_A = dice_a(condA, length, current, combinations)
    current = []
    combinations = []
    DICE_B = dice_b(condB, length, start, current, combinations)
    flag = 0
    sum_ = [0, 1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36]
    for i in DICE_A:
        for j in DICE_B:
            if probabilitysum(i, j) == sum_:
                print("new die_a :",i, end=" ")
                print()
                print("new die_b :",j, end="")
                x = 1
                break
        if x == 1:
            break

def probabilitysum(array1, array2):
    sum_1 = [0]*12
    for i in range(len(array1)):
        for j in range(len(array2)):
            a = array1[i] + array2[j]
            sum_1[a - 1] += 1
    for i in range(len(sum_1)):
        if sum_1[i] != 0:
            sum_1[i] /= 36
    return sum_1


def dice_a(condA, length, current, combinations):
    if len(current) == length:
        combinations.append(current)
        return
    for i in condA:
        dice_a(condA, length, current + [i], combinations)
    
    return combinations
    

def dice_b(condB, length, start, current, combinations):
    if len(current) == length:
        combinations.append(current)
        return
    for i in range(start, len(condB)):
        dice_b(condB, length, i + 1, current + [condB[i]], combinations)
    return combinations


die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]
transformation(die_a, die_b)