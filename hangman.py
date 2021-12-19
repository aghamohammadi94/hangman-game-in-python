# Hangman Game

import random


import re


class Hangman:
    

    # List of available words
    list_of_words = ['enthusiasm', 'newspaper', 'fantastic', 'eternity', 'hangman', 'passion', 'python', 'galaxy', 'moment', 'smile', 'skype', 'books', 'hello', 'tech', 'name', 'oops', 'car', 'gum', 'gym']


    @classmethod
    def minimum_string_length(cls):    
        # Gets the minimum number of letter letters in the word list
        return min(map(lambda x : len(x), cls.list_of_words))

    @classmethod
    def maximum_string_length(cls):
        # Gets the maximum number of letter letters in the word list
        return max(map(lambda x : len(x), cls.list_of_words))
    
    @classmethod
    def list_of_possible_numbers(cls):
        lst = list(map(lambda x : len(x), cls.list_of_words))
        lst.sort()
        return lst
    
    
       
    def __init__(self,user_selected_number = None):
        
        
        # All the letters that the user guessed are included in this list
        self.total_user_guesses = list()

        
        # The wrong letters that the user is supposed to guess are placed in this list
        self.wrong_letters = list()
        
    
        # To check the type of user input that must be a number and this number must be at least one of the characters in our words
        if type(user_selected_number) == int:
           
            
            selected_words = list()
            
            
            for j in range(len(self.list_of_words)):
                
                
                if user_selected_number == len(self.list_of_words[j]):
                    
                    selected_words.append(self.list_of_words[j])
              
                    
                    
            if len(selected_words) > 1:
                
                # Random selection of available characters
                self.random_word = list(random.choice(selected_words))      
            
            
            elif len(selected_words) == 1:
                self.random_word = list(selected_words[0])
         
          
            # The word is randomly selected by the system itself   
            else:
                self.selected_random_word()
        
        
        # The word is randomly selected by the system itself    
        else:
            self.selected_random_word()       

        
        # Puts a character _ in the random number of letters of the word in list of correct_letters
        self.correct_letters = ['_'] * len(self.random_word)   
        
        
        # Shows the number of user opportunities in a list                 
        print(f'\n👉 {self.correct_letters} 👈')
    
    
        # Here the user remaining opportunities are shown
        print(f'\nYou have {len(self.random_word)} more chances')





    def selected_random_word(self):
        
        
        print('\nYour input was invalid and now the system itself will select a word')
                
                
        # A word is randomly selected from the list of available words by the system and the letters of this word are included in the list
        self.random_word = list(random.choice(self.list_of_words))





    def __repr__(self):
        return f'''The letters in question were the constituents of the word "{''.join(self.random_word)}".'''
        

        
        
        
    # Checks if it is an English letter and if it exists in the word
    def check_letter(self,user_input):
        
        
        if re.match(r'^[a-zA-Z]+\Z', user_input) is not None:
             
            
            # It is checked that one letter must be entered and no more     
            if len(user_input) > 1:
                
                
                print('\nYou only need to enter one English letter')
                
                
            else:
            
                                      
                # Recognizes the duplication of the user's guess
                if user_input in self.total_user_guesses:
                    
                    
                    print(f'\nWhy did you re-enter the letter "{user_input}" ?\n')
                    
                    
                    print(f'Sorry, the repetitive letter "{user_input}" will no longer affect your guess')
                    
                
                # If the user's guess is not repeated, the continuation of the game will be followed here
                else:
                    
                    
                    # The user's non-repetitive guess is added to the list of total_user_guesses
                    self.total_user_guesses.append(user_input)
                    
                    
                    # If the user guesses wrong, that letter will be added to the list of wrong_letters
                    if user_input not in self.random_word:
                        
                        
                        self.wrong_letters.append(user_input)
                        
                        
                        # Here it shows the user's remaining opportunities after right or wrong guesses
                        if len(self.random_word) - len(self.wrong_letters) == 0:
                            
                            print('\n.: 👇 You have used all your chances 👇 :.')
                            
                        else:
                            
                            # Shows the number of user opportunities in a list              
                            print(f'\n👉 {self.correct_letters} 👈')
                            
                            print(f'\nYou have {len(self.random_word) - len(self.wrong_letters)} more chances')
                        
                        
                    # When the user guesses the correct letter  
                    else:
                        
                        
                        # When the user guesses the correct letter, this loop looks for the index of that letter in the random word list
                        for i in range(len(self.random_word)):
                            
                            
                            # If the guessed letter is the same as the random letters of the system
                            if user_input == self.random_word[i]:
                                
                                
                                # Finds the correct letter index, puts that letter in the list of correct_letters
                                self.correct_letters[i] =  user_input
                        
                        
                        # Shows the number of user opportunities in a list              
                        print(f'\n👉 {self.correct_letters} 👈')
                                                        
        else:
            
            print('\nPlease enter only one letter of English letters')  
    
        

    
    
    def get_result(self):
        
        
        # When the user wins the game, display a message to the user
        if self.correct_letters == self.random_word:
            
            
            print('-------- --------')
            print('-------- --------')
            print('You are WIN ! 🙌')
            print('-------- --------')
            print('-------- --------\n')
         
        
        # When the user loses the game, display a message to the user    
        else:
            
            
            print('......... 👾 .........')
            print('......... 👾 .........')
            print('GAME OVER 👾 GAME OVER')
            print('......... 👾 .........')
            print('......... 👾 .........\n')





    # This function returns the False value as long as the game continues and in case of win or loss the True value as output
    def is_finished(self):
        
        
        if len(self.wrong_letters) != len(self.random_word) and self.correct_letters != self.random_word:
            
            
            return False
        
        
        elif len(self.wrong_letters) == len(self.random_word) or self.correct_letters == self.random_word:
            
            
            return True
    
    
    
    
    
    # print function, which shows the latest status of the game
    def print_or_display(self):


        # Description of the user's guesses after the end of the game and display the desired word of the system
        print('\n.: 👇 Description of the game status 👇 :.\n')
        

        # List of all user guesses and their number
        print(f'The total number of your guesses are {len(self.total_user_guesses)} and its list goes like this {self.total_user_guesses}\n')


        # List of user wrong guesses and their number
        print(f'The number of your wrong guesses are {len(self.wrong_letters)} and its list goes like this {self.wrong_letters}\n')
        
        
        # List of user correct guesses and their number
        print(f'This is a list of your correct guesses {self.correct_letters}\n')


        # Display a list of  the desired letters of the system
        print(f'Random system letters : {self.random_word}\n')





class FruitsHangman(Hangman):
         
    # List of available words
    list_of_words = ['strawberry', 'watermelon', 'nectarine', 'blueberry', 'mulberry', 'avocado', 'apricot', 'orange', 'cherry', 'banana', 'apple', 'grape', 'lemon', 'mango', 'melon', 'pear', 'kiwi', 'fig']





class ColorHangman(Hangman):  
        
    # List of available words
    list_of_words = ['aquamarine', 'sandybrown', 'chocolate', 'amethyst', 'lavender', 'seagreen', 'mustard', 'magenta', 'purple', 'violet', 'golden', 'silver', 'yellow', 'orange', 'wheat', 'black', 'white', 'olive', 'beige', 'cream', 'amber', 'cyan', 'gray', 'bone', 'teal', 'pink', 'red']





# Asks the user if he wants to choose the number of letters in a random word
question_from_the_user = input('''\nWould you like to help us choose a random word ?
                               
Please pay attention : No letters other than "y" and "n" are accepted !!! ''').lower()



game_class = FruitsHangman



if question_from_the_user == 'y':         
      
            
    print('\nPlease enter a number to select the number of characters in the word')
    print(f'\nPlease pay attention : The number entered must be between {game_class.minimum_string_length()} and {game_class.maximum_string_length()} ! Otherwise the system will choose')
    print(f'\nPlease select the number you enter from the numbers in this list : {game_class.list_of_possible_numbers()}')
    
    user_selected_number = input('\nSo please enter an acceptable number : ')
    
    
    try:
        
        game = game_class(int(user_selected_number))
        
    except:
        
        game = game_class()
        
else:
    
    game = game_class()





while not game.is_finished():
    
         
    new_input = input('\nPlease enter an English letter : ').lower()


    game.check_letter(new_input)


game.print_or_display()


game.get_result()


print(game)

