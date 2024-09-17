from helpers import *
# Main program
if welcome_part():
    pls = players()
    if pls[0] == 1:
        player_name = pls[1]
        score = {"right answers": 0, "wrong answers": 0}
        start = time()
        complication(player_name, score)
        end = time()
        seconds = round(end - start)
        print(f"{player_name} finished in {seconds} seconds!")
        score["right answers"] -= score["wrong answers"]
        print(score)
    elif pls[0] == 2:
        player1_name = pls[1]
        player2_name = pls[2]
        scores = [
            {"right answers": 0, "wrong answers": 0},
            {"right answers": 0, "wrong answers": 0}
        ]
        rounds = int(input('How many rounds would you like to play?'))
        for round in range(rounds):
            print(f"\nRound {round + 1}")
            
            print(f"{player1_name}'s turn")
            complication(player1_name, scores[0])
            scores[0]["right answers"] -= scores[0]["wrong answers"]
            print(f"Score for {player1_name}: {scores[0]}")
            
            print(f"\n{player2_name}'s turn")
            complication(player2_name, scores[1])
            scores[1]["right answers"] -= scores[1]["wrong answers"]
            print(f"Score for {player2_name}: {scores[1]}")
        
        print("\nFinal Scores:")
        print(f"{player1_name}: {scores[0]}")
        print(f"{player2_name}: {scores[1]}")
        
        if scores[0]["right answers"] > scores[1]["right answers"]:
            print(f"{player1_name} wins!")
        elif scores[0]["right answers"] < scores[1]["right answers"]:
            print(f"{player2_name} wins!")
        else:
            print("It's a tie!")
else:
    print('Game over')