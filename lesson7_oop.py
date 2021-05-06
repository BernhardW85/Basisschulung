class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.29
        return pounds

class GolfPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, handicap, tournaments):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.handicap = handicap
        self.tournaments = tournaments

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, red_cards, yellow_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards

markus_golfobj = GolfPlayer(first_name="Markus", last_name="Angermann", height_cm=191, weight_kg=89, points=50, handicap=32, tournaments=2)
petra_golfobj =GolfPlayer(first_name="Petra", last_name="Muster", height_cm=165, weight_kg=65, points=44, handicap=3, tournaments=40)

print(markus_golfobj.points)

golf_players = [markus_golfobj, petra_golfobj]
for player in golf_players:
    print(player.last_name + " " + str(player.handicap))

print(petra_golfobj.weight_to_lbs())

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=178, weight_kg=80, goals=400, red_cards=10, yellow_cards=40)

ronaldo.weight_to_lbs()

golf_players.sort(key=lambda x: x.first_name, reverse=True)
for player in golf_players:
    print("Sortiert: " + player.first_name)


