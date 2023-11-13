def myzip(it1 , it2):
    # Ensure both collections are iterable
    iter1 = iter(it1)
    iter2 = iter(it2)
    zipped_data = []
    # Continue until either iterator is exhausted
    while True:
        try:
            element1 = next(iter1)
        except StopIteration:
            break
        try:
            element2 = next(iter2)
        except StopIteration:
            break
        zipped_data.append({'element1': element1, 'element2': element2})

    return zipped_data

# Example usage
# list1 = [1, 2, 3, 4]
# tuple1 = ('a', 'b', 'c')

# result = list(myzip(list1, tuple1))

# myzip(list1,tuple1)