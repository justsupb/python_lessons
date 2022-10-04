def create_array(array:list,size:int):
    for i in range (size):
        array.append(i)
def change_indexes(array:list,index1:int,index2:int):
    array[index1],array[index2]=array[index2],array[index1]

array=[]
# succesfull_array=[1,2,3,4]
create_array(array,11)
change_indexes(array,0,10)
print(array)