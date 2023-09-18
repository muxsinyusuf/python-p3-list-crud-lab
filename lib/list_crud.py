def create_an_empty_list():
    
    return  []

def create_a_list():
    fruits = ["apple","bana","orange","grapes"]
    return fruits

def add_element_to_end_of_list(fruits , passion):
    passion = fruits.append("passion")
    return passion

def add_element_to_start_of_list(fruits, cherry):
    cherry = fruits.insert(0,'cherry')
    
    return cherry

def remove_element_from_end_of_list(fruits):
    fruits.pop(6)
    return fruits

def remove_element_from_start_of_list(fruits):
    fruits.remove("apple")
    return fruits

def retrieve_first_element_from_list(lst):
  
    if lst:
        return lst[0]
    else:
        return None


my_list = [1, 2, 3, 4, 5]
first_element = retrieve_first_element_from_list(my_list)
print("First element of the list:", first_element)  


def retrieve_element_from_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None


my_list = [1, 2, 3, 4, 5]
element_at_index_2 = retrieve_element_from_index(my_list, 2)
print("Element at index 2:", element_at_index_2)  

def retrieve_last_element_from_list(lst):
    if lst:
        return lst[-1]
    else:
        return None


my_list = [1, 2, 3, 4, 5]
last_element = retrieve_last_element_from_list(my_list)
print("Last element of the list:", last_element)  

