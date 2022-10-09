from typing import List

def merge_sort(data) -> None:
  if len(mylist) > 1:
        mid = len(mylist)/2
        left = mylist[:mid]
        right = mylist[mid:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              mylist[k] = left[i]
              i += 1
            else:
                mylist[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k]=right[j]
            j += 1
            k += 1



# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
