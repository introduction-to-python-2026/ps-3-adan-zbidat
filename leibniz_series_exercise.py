def approximate_pi(n_terms):
    t = 0
    for n in range(n_terms):
     t += (-1) ** n / (2 * n + 1)
     approximate_pi = t * 4
  return approximate_pi

  
