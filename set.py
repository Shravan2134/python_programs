# # set1 = {5, 12, 18, 7, 3, 12, 9, 21}
# # set2 = {"apple", "banana", "cherry", "apple", "date", "fig", "grape", "banana"}

# # print(set1.union(set2))
# # set1.add(15)

# # print(set1.difference(set2))
# # set1.pop()
# # print(set1)
# # set1.remove(7)
# # print(set1)
# # set1.discard(12)
# # print(set1)
# # set1.discard(12)
# # print(set1)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# set2 = {2, 4, 6, 9, 10, 11, 12, 13, 14, 15}
# set1 = set(list)
# print(set1)

# set1.remove(4)
# print(set1)

# if 4 in set1:
#     print("4 is present in the set")
# else:
#     print("4 is not present in the set")

# print(len(set1))

# set3 = set1.intersection(set2)
# print(set3.issubset(set2))
# print(set2.issuperset(set3))
# # print(set3)
# # print(len(set3))


def Check_unique(n):
    n = int(input("Enter a number: "))
    list = []
    while n > 0:
        digit = input("enter the value:")
        list.append(digit)
        n -= 1
    unique_set = set(list)
    # print("The unique values are:", len(unique_set))
    return "the unique values are:", len(unique_set)


print(Check_unique(5))
