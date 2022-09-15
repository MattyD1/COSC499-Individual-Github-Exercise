import unittest
import unittest.mock
import mergeSort


def func():
    a = []
    i = 0
    n = 0
    # n = int(input("Add integer, enter a negative to stop adding more numbers"))

    while n >= 0:
        a.append(n)
        n = int(input())
        i += 1
    return a


class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def testMergeSort(self):
        unsortedArray = [4, 5, 2, 1, 7]
        sortedArray = [1, 2, 4, 5, 7]

        self.assertEqual(mergeSort.mergeSort(unsortedArray), sortedArray)

    @unittest.mock.patch('builtins.input', side_effect=[4, 5, 2, 1, 7, -1])
    def testUnitInput(self, mock):
        self.assertEqual(mergeSort.container(), [1, 2, 4, 5, 7])


if __name__ == '__main__':
    unittest.main()
