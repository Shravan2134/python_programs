# l = [1,45,35,32,2]
# new = l.sort()
# print(sorted(l))
# # print(new)
# fruits = ["apple","banana","mango"]

# fruits.append("pineapple")
# fruits.insert(2,"grapes")
# print(fruits)

# # print(fruits.index("apple"))
# # print(fruits.index(1)) #--> we cant use index and print its value using index but we can print index using the value in the list


# marks = [90,85,91,85,90,85]
# percentage = [90,100,56]
# marks.extend(percentage)
# new = marks.copy()
# marks.sort()
# print(new)
# print(marks)
# print(marks.count(85))


def index_finder(a):
        value = input("enter the value to find the index :")
        for index, val in enumerate(a):
           if str(value) == str(val):
                 return index
        else:
            return -1   

def Reverse_list(a):
     value = input("enter the list")
     return a[::-1]
        

# print(Reverse_list([90,45,63,84,98]))


def insert_at():
    value = input("enter the values of list :")
    list = value.split(',')
    insert_value = input("enter the value to be inserted :")
    position = int(input("enter the index or position for inserting value :"))
    list.insert(position, insert_value)
    print(list)

def combine_lists(a,b):
     new_list = a+b
     return new_list

def combine_list(a,b):
    new_list = a.extend(b)
    return new_list 
     
# def collection_counter():
#     fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
#     collection = {}
#     count = 0
#     for i in fruits:
#         temp = i
#         if i == temp:
#            count += 1
     

def collection():
     fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
     collection = {}
     for fruit in fruits:
          if fruit in collection:
               collection[fruit] += 1
          else:
               collection[fruit] = 1

     return collection   


def collection_counter():
     fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
     collection = []

     for temp in fruits:
          found = False

          for item in collection:
               if item[0] == temp:
                    found = True
          if not found:
               count = 0
               for fruit in fruits:
                    if fruit == temp:
                         count += 1
               collection.append(temp, count)
     return collection


def add_list(a):
     # a = [1, 2, 3, 4, 5]
     sum = 0
     for i in a:
          sum += i
     return sum

def max_list(a):
	max_value = a[0]
	for i in a:
		if i > max_value:
			max_value = i
	return max_value

def min_list(a):
	min_value = a[0]
	for i in a:
		if i < min_value:
			min_value = i
	return min_value


def sort_list(l):
	sort_list = sorted(l)
	return sort_list


def sort_list_descending(l):
     sort_list = sorted(l, reverse=True)
     return sort_list

def unique_numbers_set(l):
    unique_numbers = list(set(l))
    return list(unique_numbers)


def common_among_lists(a, b):
    common_elements = set(a) & set(b)
    return list(common_elements)





print(common_among_lists([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))


# print(sort_list_descending([1, 2, 3, 4, 5, 6, 7, 8, 9]))








# print(max_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# print(add_list())

# print(collection_counter())

         
# print(collection()) 



# fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# print(insert_at())
