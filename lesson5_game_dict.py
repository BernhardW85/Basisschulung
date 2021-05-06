import random # importiert fertige funktionen/bibliotheken
import json
import datetime

#current_time = datetime.datetime.now()
#print(current_time)

secret = random.randint(1, 30)
# bool_a = True # als Steuervariable, dann while bool_a und bool_a = False als Ausstieg
attempts = 0

with open("lesson5_game_score_dict.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    #score_list.sort()
    #print("Top scores:" + str(score_list[:3]))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " Versuche, Datum: " + score_dict.get("date")  # score_dict["date"]

while True:
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    attempts += 1 # ident mit attempts = attempts + 1

    if guess == secret:
        #score_list.append(attempts) # append hängt das neue Element an die bestehende Liste dazu, sonst würde ich sie überschreiben
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open("lesson5_game_score_dict.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Gewonnen! Die Zahl ist " + str(secret))
        print("Versuche: " + str(attempts))
        break

    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")

    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")