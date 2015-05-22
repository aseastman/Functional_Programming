# This function will count the number of occurances of something in an array
# of lists. Otherwise, we could just call arr.count()
def count_in_array(arr,find_item):
    item_count = reduce(lambda a, x: a + x.count(find_item),arr,0)
    return item_count



#Example    
arr = [[1,2],[1,3]]
print count_in_array(arr,1)

