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
        i+=1
      else: 
        array[l] = e[j]
        j+=1
      
      l+=1

    while i < len(b):
      array[l] = b[i]
      i+=1
      l+=1

    while j < len(e):
      array[l] = e[j]
      j+=1
      l+=1

if __name__ == '__main__':
  testArray = [1, 4, 2, 6, 10, 12, 44]
  mergeSort(testArray)