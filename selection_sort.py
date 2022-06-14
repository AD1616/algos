def selection_sort(A):
    i = 0
    j = 0
    min = 0

    for i in range (0, len(A)):
        # Setting the min index to the current 
        # position in the list
        min = i
        # For each element after the current position,
        # if the element is less than the current position element
        # which is A[min], then update min to be the new element
        # after all elements after the current one have been checked,
        # update the original min to be the new min
        # Now, the outer loop will start at the next element and 
        # the process repeats until the list is sorted
        for j in range (i+1, len(A)):
            if (A[j] < A[min]):
                min = j
        A[i], A[min] = A[min], A[i]
    return A

def selection_sort_tester():
    A = [5,4,1,2,7]
    print(selection_sort(A))

if __name__ == "__main__":
    selection_sort_tester()
