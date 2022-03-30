def findCeleb(matrix):
    mmm = 0
    for i in range(0, len(matrix)):
        for ID in matrix[i]:
            count = 0
            if ID == 1:
                count += 1
        if count == 0:
            saved = i
            count2 = 0
            for num in range(0, saved-1):
                if matrix[num][saved] == 0:
                    count2 += 1
            for num in range(saved+1, len(matrix)):
                if matrix[num][saved] == 0:
                    count2 += 1
            if count2 == 0:
                mmm += 1
                print("id = " + str(i))
    if mmm == 0:
        print("-1")


def tester():
    matrix1 = [
        [0, 0, 1, 0],
        [0,0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    matrix2 = [
        [0, 0, 0, 1, 0],
        [0,0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    findCeleb(matrix2)


if __name__ == "__main__":
    tester()