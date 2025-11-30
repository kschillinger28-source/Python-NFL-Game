from random import randrange
class Player:
    # Initialize Player attributes
    def __init__(self, name, age, years_experience, jersey_number):
        self.name = name
        self.age = age
        self.years_experience = years_experience
        self.jersey_number = jersey_number
        # get length of firstname
        nameSplit = name.split(" ")
        firstname = nameSplit[0]
        self.letters = len(firstname)
        self.fl = name[0]

    def __repr__(self):
        # return string representation of player
        return self.name + ", Age: " + str(self.age) + ", Years of Experience: " + str(self.years_experience) + ", Jersey Number: " + str(self.jersey_number) + ", Letters in First Name:" + str(self.letters)

class Game:
    def __init__(self):
        #Initialize the players, questions, and game settings
        self.players = []
        self.questions = []
        self.max_guesses = 0
        

    def initialize_players(self):
        #List of players with their attributes
        self.players = [
        
            Player("Aidan O'Connell", 25, 2, 4),
            Player("Aaron Rodgers", 40, 21, 8),
            Player("Anthony Richardson", 22, 2, 5),
            Player("Baker Mayfield", 29, 7, 6),
            Player("Bo Nix", 24, 1, 10),
            Player("Brock Purdy", 24, 3, 13),
            Player("Bryce Young", 23, 2, 9),
            Player("C. J. Stroud", 23, 2, 7),
            Player("Caleb Williams", 23, 1, 18),
            Player("Cooper Rush", 30, 7, 10),
            Player("Derek Carr", 33, 11, 4),
            Player("Drake Maye", 22, 1, 10),
            Player("Drew Lock", 27, 6, 2),
            Player("Geno Smith", 34, 13, 7) ,
            Player("Jalen Hurts", 25, 5, 1),
            Player("Jameis Winston", 30, 10, 2),
            Player("Jared Goff", 29, 9, 16),
            Player("Jayden Daniels", 22, 1, 5),
            Player("Joe Burrow", 27, 5, 9),
            Player("Josh Allen", 28, 7, 17),
            Player("Jordan Love", 25, 5, 10),
            Player("Justin Herbert", 26, 6, 10),
            Player("Kyler Murray", 26, 6, 1),
            Player("Kirk Cousins", 36, 13, 8),
            Player("Lamar Jackson", 27, 7, 8),
            Player("Matthew Stafford", 36, 17, 9),
            Player("Patrick Mahomes", 28, 8, 15),
            Player("Russell Wilson", 35, 14, 3),
            Player("Sam Darnold", 27, 7, 14),
            Player("Trevor Lawrence", 24, 4, 16),
            Player("Tua Tagovailoa", 26, 5, 1),
            Player("Will Levis", 24, 2, 8),
        ]

    def initialize_questions(self):
        #List of questions and conditions
        self.questions = [
            "Question 1 :Does the player have a jersey number less than 5?",
            "Question 2 :Does the player have a jersey number less than 10?",
            "Question 3 :Does the player have a jersey number less than 15?",
            "Question 4 :Is your player over the age of 23?",
            "Question 5 :Is your player over the age of 25",
            "Question 6 :Is your player over the age of 30?",
            "Question 7 :Does the player have more than 3 years of experience?",
            "Question 8 :Does the player have more than 6 years of experience?",
            "Question 9 :Does their first name have over 3 letters?",
            "Question 10 :Does their first name have over 7 letters?",
            "Question 11 :Does their first name start with the Letter A?",
            "Question 12 :Does their first name start with the Letter B?",
            "Question 13 :Does their first name start with the Letter C?",
            "Question 14 :Does their first name start with the Letter D?",
            "Question 15 :Does their first name start with the Letter J?",
            "Question 16 :Does their first name start with the Letter K?",
            "Question 17 :Does the player have more than 8 years of experience?",
        ]

    def show_instructions(self):
        #Print the game instructions
        print("Welcome to the 20 Questions game!")
        print("")
        print("Think of a player from the list, and the program will try to guess who it is.")
    
        print("Answer 'yes' or 'no' to the questions. The program has a limited number of guesses.")
        
        print("If the program guesses the player within the allowed guesses, it wins. Otherwise, you win!")

    def refine_questions(self, remaining_questions, players):
        refined_questions = []
        
        if "Question 1 :Does the player have a jersey number less than 5?" in remaining_questions: 
            for player in players:
                if player.jersey_number < 5:
                    refined_questions.append("Question 1 :Does the player have a jersey number less than 5?")
                    break

        if  "Question 2 :Does the player have a jersey number less than 10?" in remaining_questions: 
            for player in players:
                if player.jersey_number < 10:
                    refined_questions.append( "Question 2 :Does the player have a jersey number less than 10?")
                    break

        if "Question 3 :Does the player have a jersey number less than 15?" in remaining_questions: 
            for player in players:
                if player.jersey_number < 15:
                    refined_questions.append("Question 3 :Does the player have a jersey number less than 15?")
                    break

        if "Question 4 :Is your player over the age of 23?" in remaining_questions: 
            for player in players:
                if player.age > 23:
                    refined_questions.append("Question 4 :Is your player over the age of 23?")
                    break

        if "Question 5 :Is your player over the age of 25" in remaining_questions: 
            for player in players:
                if player.age > 25:
                    refined_questions.append("Question 5 :Is your player over the age of 25")
                    break
        
        if "Question 6 :Is your player over the age of 30" in remaining_questions: 
            for player in players:
                if player.age > 30:
                    refined_questions.append("Question 6 :Is your player over the age of 30")
                    break

        if "Question 7 :Does the player have more than 3 years of experience?" in remaining_questions: 
            for player in players:
                if player.years_experience > 3:
                    refined_questions.append("Question 7 :Does the player have more than 3 years of experience?")
                    break

        if "Question 8 :Does the player have more than 6 years of experience?" in remaining_questions: 
            for player in players:
                if player.years_experience > 6:
                    refined_questions.append("Question 8 :Does the player have more than 6 years of experience?")
                    break

        if "Question 9 :Does their first name have over 3 letters?" in remaining_questions: 
            for player in players:
                if player.letters > 3:
                    refined_questions.append("Question 9 :Does their first name have over 3 letters?")
                    break

        if "Question 10 :Does their first name have over 7 letters?" in remaining_questions: 
            for player in players:
                if player.letters > 7:
                    refined_questions.append("Question 10 :Does their first name have over 7 letters?")
                    break

        if "Question 11 :Does their first name start with the Letter A?" in remaining_questions: 
            for player in players:
                if player.fl == "A":
                    refined_questions.append("Question 11 :Does their first name start with the Letter A?")
                    break
                
        if "Question 12 :Does their first name start with the Letter B?" in remaining_questions: 
            for player in players:
                if player.fl == "B":
                    refined_questions.append("Question 12 :Does their first name start with the Letter B?")
                    break

        if "Question 13 :Does their first name start with the Letter C?" in remaining_questions: 
            for player in players:
                if player.fl == "C":
                    refined_questions.append("Question 13 :Does their first name start with the Letter C?")
                    break

        if "Question 14 :Does their first name start with the Letter D?" in remaining_questions: 
            for player in players:
                if player.fl == "D":
                    refined_questions.append("Question 14 :Does their first name start with the Letter D?")
                    break

        if "Question 15 :Does their first name start with the Letter J?" in remaining_questions: 
            for player in players:
                if player.fl == "J":
                    refined_questions.append("Question 15 :Does their first name start with the Letter J?")
                    break

        if "Question 16 :Does their first name start with the Letter K?" in remaining_questions: 
            for player in players:
                if player.fl == "K":
                    refined_questions.append("Question 16 :Does their first name start with the Letter K?")
                    break

        if "Question 17 :Does the player have more than 8 years of experience?" in remaining_questions: 
            for player in players:
                if player.years_experience > 8:
                    refined_questions.append("Question 17 :Does the player have more than 8 years of experience?")
                    break

                
        return refined_questions

        


        
    def ask_question(self, question):
        #Ask the user the question based on the input of the user
            answer = input(question + " (yes/no): ").strip().lower()
            while answer != "yes" and answer != "no":
                print("Invalid input. Please answer with 'yes' or 'no'.")
                answer = input(question + " (yes/no): ").strip().lower()
            return answer
                
    

    def filter_players(self, question, answer):
        # Filters and eliminates the player based on the user input
        filtered_players = []
        for player in self.players:        
            if "Question 1 " in question:
                if (answer == "yes" and player.jersey_number < 5) or (answer == "no" and player.jersey_number >= 5):
                    filtered_players.append(player)
            elif "Question 2" in question:
                if (answer == "yes" and player.jersey_number < 10) or (answer == "no" and player.jersey_number >= 10):
                    filtered_players.append(player)
            elif "Question 3" in question:
                if (answer == "yes" and player.jersey_number < 15) or (answer == "no" and player.jersey_number >= 15):
                    filtered_players.append(player)
            elif "Question 4" in question:
                if (answer == "yes" and player.age > 23) or (answer == "no" and player.age <= 23):
                    filtered_players.append(player)
            elif "Question 5" in question:
                if (answer == "yes" and player.age > 25) or (answer == "no" and player.age <= 25):
                    filtered_players.append(player)
            elif "Question 6" in question:
                if (answer == "yes" and player.age > 30) or (answer == "no" and player.age <= 30):
                    filtered_players.append(player)
            elif "Question 7" in question:
                if (answer == "yes" and player.years_experience > 3) or (answer == "no" and player.years_experience <= 3):
                    filtered_players.append(player)
            elif "Question 8" in question:
                if (answer == "yes" and player.years_experience > 6) or (answer == "no" and player.years_experience <= 6):
                    filtered_players.append(player)
            elif "Question 9" in question:
                if (answer == "yes" and player.letters > 3) or (answer == "no" and player.letters <= 3):
                    filtered_players.append(player)
            elif "Question 10" in question:
                if (answer == "yes" and player.letters > 7) or (answer == "no" and player.letters <= 7):
                    filtered_players.append(player)
            elif "Question 11" in question:
                if (answer == "yes" and player.fl == "A") or (answer == "no" and player.fl != "A"):
                    filtered_players.append(player)
            elif "Question 12" in question:
                if (answer == "yes" and player.fl == "B") or (answer == "no" and player.fl != "B"):
                    filtered_players.append(player)
            elif "Question 13" in question:
                if (answer == "yes" and player.fl == "C") or (answer == "no" and player.fl != "C"):
                    filtered_players.append(player)
            elif "Question 14" in question:
                if (answer == "yes" and player.fl == "D") or (answer == "no" and player.fl != "D"):
                    filtered_players.append(player)
            elif "Question 15" in question:
                if (answer == "yes" and player.fl == "J") or (answer == "no" and player.fl != "J"):
                    filtered_players.append(player)
            elif "Question 16" in question:
                if (answer == "yes" and player.fl == "K") or (answer == "no" and player.fl != "K"):
                    filtered_players.append(player)
            elif "Question 17" in question:
                if (answer == "yes" and player.years_experience > 8) or (answer == "no" and player.years_experience <= 8):
                    filtered_players.append(player)
            else:
                print("question not valid?")
            

       
        return filtered_players

                

    def game_loop(self):
        # the main function which would narrow down the players
        # until guess is correct or runs out of guesses
        self.players = self.players[:]
        print("\nThe game begins! Think of a player from the list below:")
        for player in self.players:
            print("\n",player)
        #This part of the loop asks the question while
        #eliminating the guesses as well as the
        #not needed players
        remaining_questions = self.questions[:]
        while self.max_guesses > 0 and len(self.players) > 1:
            # filter the questions
            remaining_questions = self.refine_questions(remaining_questions, self.players)

        
             
            if len(remaining_questions) > 0:
                question_index = randrange(len(remaining_questions))
                question = remaining_questions.pop(question_index)
            
            
            answer = self.ask_question(question)
            self.players = self.filter_players(question, answer)
            self.max_guesses -= 1

            print("\nRemaining guesses:", self.max_guesses)
            print("\nPossible players:", [player.name for player in self.players])

        if len(self.players) == 1:
            print("\nThe program guesses: ", self.players, "!")
            print("The program wins!")
        else:
            print("\nThe program couldn't guess your player. You win!")

    def start(self):
        #Start the game, sets the max guesses and allows
        #the user to replay the game
        self.initialize_players()
        self.initialize_questions()
        self.show_instructions()
        self.max_guesses = input("\nEnter the maximum number of guesses! (The more guesses the better the chance the program has!): ")
        while not self.max_guesses.isdigit():
            print("Invalid input. Please enter a number.")

        self.max_guesses = int(self.max_guesses)

        self.game_loop()
        if input("\nWould you like to play again? (yes/no): ").strip().lower() == "yes":
            self.start()


if __name__ == "__main__":
    game = Game()
    game.start()
