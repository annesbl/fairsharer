def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: Integer to set the number of iterations
        share: Fraction of the highest value to be shared

    Returns:
        List with adjusted values after iterations.
    """
    from copy import deepcopy
    values_new = deepcopy(values)
    for _ in range(num_iterations):
        max_value = max(values_new)
        max_index = values_new.index(max_value)
        transfer = max_value * share

        values_new[max_index] -= 2 * transfer
        values_new[(max_index - 1) % len(values_new)] += transfer
        values_new[(max_index + 1) % len(values_new)] += transfer
    return values_new

