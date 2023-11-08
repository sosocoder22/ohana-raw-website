import itertools


def pattern_match(pattern, sequence):
    """Count the number of times that pattern occurs in the sequence."""
    pattern = tuple(pattern)
    k = len(pattern)

    # create k iterators for the sequence
    i = itertools.tee(sequence, k)

    # forward the iterators
    for j in range(k):
        for _ in range(j):
            next(i[j])

    count = 0
    for q in zip(*i):
        if pattern == q:
            count += 1

    return count


def main():
    p = [15, 85, 23]
    l = [1582,1982,2823,2838,4681,4863,5200,6241,7333,9583,1606,4832,5622,5641,5719,6781,6907,7270,8527,9801,4585]
    count = pattern_match(p, l)
    print('Found {} instances of {} in the list.'.format(count, p))


if __name__ == '__main__':
    main()