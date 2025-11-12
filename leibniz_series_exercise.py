def approximate_pi(n_terms):
    total = 0
    for i in range(n_terms):
        term = ((-1) ** i) / (2 * i + 1)  
        total += term
    return 4 * total

