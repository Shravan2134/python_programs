quiz_results = {
    "player1": {"score": 12, "time": 30},
    "player2": {"score": 15, "time": 25},
    "player3": {"score": 10, "time": 35}
}

# Arrange the players by their scores in ascending order

sorted_players = {}

players = []

for key in quiz_results:
    players.append(key)

first_score = quiz_results[players[0]]["score"]

for player in players:
    for key, value in quiz_results[player].items():
        if key == "score":
            if value < first_score:
                first_score = value
                first_time = quiz_results[player]["time"]
                sorted_players[player] = {"score": first_score, "time": first_time}
                quiz_results.pop(player)               
print(sorted_players)
    
#     if quiz_results[player]["score"] < first_score:
#         first_score = quiz_results[player]["score"]
#         first_time = quiz_results[player]["time"]
# sorted_players[player] = {"score": first_score, "time": first_time}        
    


print(quiz_results)        
print("Sorted players by score:", sorted_players)



