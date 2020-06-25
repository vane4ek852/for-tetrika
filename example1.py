def search_pairs(array, k):
    array_pairs = []
    n = len(array)
    for i in range(0, n, 1):
        for j in range(i+1, n, 1):
            if array[i] + array[j] == k and (array[i], array[j]) not in array_pairs and (array[j], array[i]) not in  array_pairs:
                array_pairs.append((array[i], array[j]))
    return array_pairs
    
print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))