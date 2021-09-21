def comb_sort(seq):
    gap = len(seq)
    changed = True
    while gap > 1 or changed:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        changed = False
        for i in range(len(seq) - gap):
            j = i+gap
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
                changed = True

if __name__ == "__main__":
    """Sample usage and simple test suite"""

    from random import shuffle

    testset = list(range(1000))
    testcase = testset[:] # make a copy
    shuffle(testcase)
    assert testcase != testset  # we've shuffled it
    comb_sort(testcase)
    assert testcase == testset  # we've unshuffled it back into a copy