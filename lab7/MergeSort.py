# The complexity of list.pop(0) is O(n), because for it to remove the first element, it also needs to shift all the elements down by an index, which can take a long time depending on the size of the list. The larger the list, the longer it will take to move all the elements, so it's O(n)

# Equivalence classes:
# Both list's size = 1
# B list size is 0 (empty)
# Already sorted lists
# Identical lists

def mergeSort(aList):
    if (len(aList) < 2):
        return(aList)
    else:
        a = aList[0:len(aList)//2]
        b = aList[len(aList)//2: len(aList)]
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)
        return(merge(aButSorted, bButSorted))
        
def merge(listA, listB):
    newList = []
    currIndexA = 0
    currIndexB = 0
    
    while(len(listA) > currIndexA and len(listB) > currIndexB):
        if(listA[currIndexA] < listB[currIndexB]):
            newList.append(listA[currIndexA])
            currIndexA += 1
        else:
            newList.append(listB[currIndexB])
            currIndexB += 1

    # Adds the rest of the list from the current index to the end
    newList.extend(listA[currIndexA:])
    newList.extend(listB[currIndexB:])
    return(newList)