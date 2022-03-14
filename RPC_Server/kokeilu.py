import database
import game



uusi = database.Database("testi.db")

print("PASKA")

print(uusi.get_ID())
print(uusi.get_ID())
print(uusi.get_ID())


uusi.insert_new_user("Aapo", "Salasana")
p1 = "Aapo"
p2 = "Bella"

peli = game.Game(p1, p2)

peli.p1_move("R")

peli.p2_move("S")

outcome = peli.solve_game()


uusi.insert_game_history(0 , p1, p2, outcome)

print(uusi.get_game_information())
print(uusi.get_user_information())


print(uusi.check_credentials("Aapo", "Salasana"))

print(uusi.get_game_info_wins_user("Aapo"))