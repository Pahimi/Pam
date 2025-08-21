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
  an = data_test[j]
  printf(an, "-> ", end="")
  results = is_year_leap(an)
  if results == results_test[j]:
    printf("OK")
  else:
    printf("Échoué")
#Factorial

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

for n in range(1, 6):
    print(n,'! = ', factorial_function(n))

