#regular functions
#Ruby and Hannah
def ask_question(question): 
    """Print out a question"""
    print question

#Ruby and Hannah
def multiple_choice(choices): 
    """Print out multiple choice options"""
    print choices
    return raw_input('What is your choice?') 

#Ruby and Hannah
def answer(): 
    """Correct answer for each question"""
    correct_1= "b"
    correct_2= "c"
    correct_3= "a"
    correct_4= "d"
    correct_5= "b"
    correct_6= "a"
    correct_7= "c"
    correct_8= "d"
    correct_9= "c"
    correct_10= "d" 

#Ruby and Hannah
#def user_answer():
    #"""Figure out is user's answer is right or wrong"""
    #raw_input("What is your answer?") 

#Hannah
def play_game(): 
   for question,choices,correct in [
           ["What is Mickey's pet dogs' name?", ["a. Donald", "b. Pluto", "c. Goofy", "d. Daisy"], "b"],
           ["What animal swallowed a clock in Peter Pan?", ["a. Tiger", "b. Parrot", "c. Crocodile", "d.  Shark"], "c"],
           ["What is Mickey's pet dog's name?", ["a. Donald", "b. Pluto", "c. Goofy", "d. Daisy"], "b"],
           ["What animal swallowed a clock in Peter Pan?", ["a. Tiger", "b. Parrot", "c. Crocodile", "d. Shark"], "c"],
           ["Who is the first Disney princess?", ["a. Snow White","b. Pocahontas", "c. Tiana"," d. Cinderella"], "a"],
           ["What U.S. city is The Princess and The Frog set in?", ["a. Nashville", "b. New York", "c. Altana", "d. New Orleans"], "d"],
           ["In the Lion King, where does Mufasa and his family live?", ["a. Love Rock","b. Pride Rock", "c. Justice Rock", "d. Peace Rock"], "b"],
           ["During the ballroom scene of Beauty & the Beast, what color is Belle's  dress?", ["a. Gold", "b. Silver", "c. Bronze", "d. None of the above"], "a"],
           ["In the Little Mermaid, what is Prince Eric's dog's name?", ["a. Dog", "b. Pluto", "c. Max", "d. Mike"], "c"],
           ["In Peter Pan, what is the way to Neverland?", ["a. First star to the right and straight on  til morning", "b. Second star to the left and straight on til morning", "c. Third star to the right and straight on til morning","d. Second star to the right and straight on til morning"], "d"],
           ["What is the name of Cinderella's mice?", ["a. Jesse and Goose", "b. Jess and Jack-Jack", "c. Gus and Jaq", "d. Wes and Jess"], "c"],
           ["In Monsters Inc., what is Sulley's full name?", ["a. Jim A Sullivan", "b. Sullivan", "c. J P Sullivan", "d. James P Sullivan"], "d"]
   ]: 
        ask_question(question)
        user_answer = multiple_choice(choices)
        if user_answer==correct:
            print ("You got the problem correct!")
        else:
            print ("The correct answer was", correct)
        print ("You have completed all questions. Thank you for playing.")

#test functions
def test_ask_question():  # gift from Mr. H
    ask_question('Who are you?')
    ask_question('What is the capital of New York State?')
    ask_question('Would you rather eat a bowl full of spiders or climb up the Empire State Building?')

def test_multiple_choice():     # gift from Mr. H
    multiple_choice(['Eat breakfast','Go back to bed','Take a shower','Skip school'])
    multiple_choice(['Eat breakfast','Go back to bed','Take a shower','Skip school','Go fly a kite'])
    multiple_choice(['Eat breakfast','Go back to bed','Take a shower','Skip school','Wear pants','Put on hat'])
    multiple_choice(['Eat breakfast','Go back to bed'])
    multiple_choice(['You have no choice! Ha!'])

play_game()
