class TwoSum:
  def __init__(self,list,target):
    self.list = list
    self.target = target
  def solution(self):
    length = len(list)
    for i in range(length-1):
      for j in range(i+1, length):
        if list[i]+list[j] == self.target:
          new = i, j
          return new
    return -1 
list = [2, 11, 7, 15]  
target = 9  
obj = TwoSum(list,target)
print(obj.solution())  