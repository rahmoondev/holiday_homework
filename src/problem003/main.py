#​ 3. List Duplicates Remover
# ​Goal: Write a function that takes a list of numbers or strings and returns a new list with all duplicate items removed.
# Concepts: Lists, loops, or using the set() data structure.



def remove_duplicates(lst:list):
    new_list=[]
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


if __name__=="__main__":
    lst= [1,2,2,3,4,4,5,'a','b','b','c','c']
    result = remove_duplicates(lst)
    print(result)



#another way if order does not matter:

"""
def remove_duplicates():
    remove= list(set(duplicates))
    print(remove)


remove_duplicates()
"""
