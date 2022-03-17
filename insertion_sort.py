
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence from index 1 to j-1, the term right before A[j]
        i = j-1
        # While loop is checking each term before A[j] to see if it is greater or smaller than A[j]
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


# Exercise 2.1-2
def insertion_sort_2(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] < key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


def insertion_sort_tester():
    matrix = [3, 2, 4, 1, 9, 7, 8]
    print(insertion_sort(matrix))
    print(insertion_sort_2(matrix))


if __name__ == "__main__":
    insertion_sort_tester()

