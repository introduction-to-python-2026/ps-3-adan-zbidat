def approximate_pi(n_terms):
    list_of_alternating_signs=[]
    list_of_numbers=[]
    for i in range(n_terms):
      list_of_numbers.append(i)
      if i%2==0 :
         list_of_alternating_signs.append(1)
      else:
         list_of_alternating_signs.append(-1)
    leibniz_series=[]
    for i in range(n_terms):
      leibniz_series.append(list_of_alternating_signs[i]*(1/(2*list_of_numbers[i]+1)))
    return ((sum(leibniz_series))*4)
    
