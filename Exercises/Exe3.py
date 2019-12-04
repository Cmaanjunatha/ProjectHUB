def binary_search(array, key):
    low = 0
    high = len(array)-1
    found = False
    while low <= high and not found:
        mid = low+high//2
        if array[mid] == key:
            found = True
        else:
            if key < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return found





#binary_search([2, 3, 5, 6, 9, 14, 18, 22, 56, 78, 88, 99], 101)


binary_search([2, 3, 5, 6, 9, 14, 18, 22, 56, 78, 88, 99], 18)