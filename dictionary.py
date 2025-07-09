# fruit_colors = {
#     "apple": "red",
#     "banana": "yellow",
#     "grape": "purple",
#     "orange": "orange"
# }
# vegetable_colors = {
#     "carrot": "orange",
#     "broccoli": "green",
#     "spinach": "green",
#     "potato": "brown"
# }   

# print(fruit_colors.keys())
# print(vegetable_colors.values())

# for key,value in fruit_colors.items():
#     print(f"{key} is {value}")

# for key,value in vegetable_colors.items():
#     print(f"{key} is {value}")


# # fruit_colors.update(vegetable_colors)
# # fruit_colors.clear()
# fruit_colors.popitem()
# # fruit_colors.pop('banana')
# print(fruit_colors)
# # print(fruit_colors.get("yellow","Enter the valid Key value"))

# fruits = {"apple": 5, "banana": 8, "orange": 6}

# Add new fruit grape with quantity 10

# fruits["grape"] = 10
# fruits["banana"] = 12

# # check whether mango is in the dictionary

# for key in fruits.keys():
#     if "Mango" in key:
#         print(f"Found {key} in the dictionary")
#         break
# else:
#     print("Mango not found in the dictionary")
		

# first_index = list(fruits.keys())[0]
# first_value = fruits[first_index]

# print(first_value)

# print(fruits.get("Mango", "Does not exists"))
# print(fruits)

# grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# first_index = list(grades.keys())[0]
# first_value = grades[first_index]
# result = 0



# for key,value in grades.items():
# 	if value > first_value and first_value == value:
# 		first_value = value

# for keys, values in grades.items():
# 	 if first_value == values:
# 		 print(f"{keys} has the highest grade: {values}")

# # # print(f"The highest grade is: {result}")


quiz_results = {
    "player1": {"score": 12, "time": 30},
    "player2": {"score": 15, "time": 25},
    "player3": {"score": 10, "time": 35}
}

# Find the player with the highest score
highest_score = 0

for player,stats in quiz_results.items():
    if stats["score"] > highest_score:
        highest_score = stats["score"]
        top_player = player

print(f"The player with the highest score is {top_player} with a score of {highest_score}.")

zero_index = list(quiz_results.keys())[0]
zero_value = quiz_results[zero_index]

first_timing = zero_value["time"]


for player, stats in quiz_results.items():
    if stats["time"] < first_timing:
        first_timing = stats["time"]
        fastest_player = player
print(f"The fastest player is {fastest_player} with a time of {first_timing} seconds.")

quiz_results["player4"] = {"score": 14, "time": 28}       


print("Updated quiz results:", quiz_results)


# quiz_results.pop("player2", None)  # Remove player2 if exists\


# sort based on the score
# sorted_dict = sorted(quiz_results.items(), key=lambda item:item[1]["score"], reverse=True)


zero_index 


sorted_quiz = {}

unproccesed_keys = []

for key in quiz_results:
    unproccesed_keys.append(key)
print("Unprocessed keys:", unproccesed_keys)    

 























# print("Updated quiz results:", quiz_results)






