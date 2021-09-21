def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
    seq MUST BE A MUTABLE SEQUENCE.
    As with list.sort() and random.shuffle this does NOT return 
    """
    changed = True
    GAP = 1
    while changed:
        changed = False
        for item in range(len(seq) - GAP):
            if seq[item] > seq[item+GAP]:
                seq[item], seq[item+GAP] = seq[item+GAP], seq[item]
                changed = True
    return seq

if __name__ == '__main__':
    """Sample usage and simple test suite"""
    from random import shuffle

    testset = list(range(100))
    testcase = testset[:]
    shuffle(testcase)
    assert testcase != testset
    bubble_sort(testcase)
    assert testcase == testset