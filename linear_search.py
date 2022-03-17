# Exercise 2.1-3
def linear_search(A, v):
    i = 0
    while i < len(A):
        for i in A:
            if A[i] == v:
                return i
            i = i+1
    return "NIL"


def linear_search_tester():
    matrix = [3, 2, 4, 1, 9, 7, 8]
    value = 9
    print(linear_search(matrix, value))


if __name__ == "__main__":
    linear_search_tester()
