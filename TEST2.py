import random
def generate_random_array():
   
   length = random.randint(1, 10)  

   return [random.randint(1, 100) for _ in range(length)] 
def check_guess(array):
   
   print("Hádej čísla v poli:", array)

   guess = input("Uhádni délku pole: ")

   if int(guess) == len(array):
    
       
       print("Správně!")
       return 1
   else:
       print("Špatně!")
       return 0
def play_game():
   
   rounds = random.randint(1, 15)

   total_points = 0
   print("Vítejte ve hře!")
   print("Budete hrát", rounds, "kol.")
   for _ in range(rounds):
       
       array = generate_random_array()
       total_points += check_guess(array)
   print("Konec hry! Celkový počet bodů:", total_points)
play_game()