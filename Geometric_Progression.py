# Write a function that determines if a list of integers follows a geometric progression
# Test your function with the following lists:
# list1 = [2, 4, 6, 8, 10]
# list2 = [3, 6, 12, 24, 48]

def check_gp(alist):
  if len(alist) <= 1:
    return True
  elif alist[0] == 0:
    return False
  else:
    r = alist[1]/alist[0]
    for i in range(1,len(alist)):
      if alist[i]/alist[i-1] != r:
        return False
    return True

# *Bonus* Write a function that makes use of the previous function and returns the sum to infinity of a geometric progression if it exists
# Test your function with the following lists:
# list3 = [625, 125, 25, 5, 1]

def sum(blist):
  if check_gp(blist):
    if len(blist) < 1:
      return 0
    elif len(blist) == 1:
      return blist[0] # assume r = 0
    elif blist[1]/blist[0] >= 1:
      return "sum to infty does not exist"
    else:
      return blist[0]/(1-(blist[1]/blist[0]))
    
