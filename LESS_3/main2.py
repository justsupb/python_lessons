import random
def add_to_array_random_values(array:list,len:int):
    for i in range(len):
        array.append(random.randint(1,1000))
    return array
array = [12,15,16]
array_full = add_to_array_random_values(array,20)
print(array_full)
import function
function.summator(4,2)