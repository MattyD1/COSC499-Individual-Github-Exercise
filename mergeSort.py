# Merge Sort Algorithm

def mergeSort(array):
    if len(array) > 1:

        # Integer divide because the array length is odd
        mid = len(array)//2
        # Split the array into 2
        b = array[:mid]
        e = array[mid:]

        # Merge sort is recursive thus we call it again for each half
        mergeSort(b)
        mergeSort(e)

        i = j = l = 0

        while i < len(b) and j < len(e):
            if b[i] < e[j]:
                array[l] = b[i]
                i += 1
            else:
                array[l] = e[j]
                j += 1

            l += 1

        while i < len(b):
            array[l] = b[i]
            i += 1
            l += 1

        while j < len(e):
            array[l] = e[j]
            j += 1
            l += 1

    return array


def UserInput():
    a = []
    i = 0

    n = int(input("Add integer, enter a negative to stop adding more numbers"))

    while n >= 0:
        a.append(n)
        n = int(input("Add integer, enter a negative to stop adding more numbers"))
        i += 1
    return a


def printList(array):
    print("Sorted Array: ")
    for i in range(len(array)):
        print(array[i], end=",")


def container():
    testArray = UserInput()
    mergeSort(testArray)
    return testArray


if __name__ == '__main__':
    printList(container())
