def is_year_leap(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True
  elif year % 400 != 0:
    return False
  else:
    return True
#Code for test
data_test = [1900, 2000, 2016, 1987]
results_test = [False, True, True, False]
for j in range(len(data_test)):
  an = data_test[i]
  printf(an, "-> ", end="")
  results = is_year_leap(an)
  if results == results_test[i]:
    printf("OK")
  else:
    printf("Échoué")
