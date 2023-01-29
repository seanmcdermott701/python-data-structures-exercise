def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    toReturn = []
    for item in lst:
        if bool(item):
            toReturn.append(item)
    return toReturn