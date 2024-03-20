#split into 3 conditions becuase;
#the number will just increase as fibonacci sequence
#but when the bunnies hit their last month of their lifesapn, we just need to subtract 1 which is list[0]
#and the rest of the sequence would be to subtract list[i-(death-1)] from fibonacci sequence formula 

def mortal_rabbit(month, death):
  #list = [first month, second month]
  list = [1, 1]
  for i in range(month-2):
    if i < (death-2):
      next = list[i] + list[i+1]
      list.append(next)
    elif i == (death-2):
      next = list[i] + list[i+1] - list[0]
      list.append(next)
    else:
      next = list[i] + list[i+1] - list[i-(death-1)]
      list.append(next)
  return(list)
 

print(mortal_rabbit(92,20))
