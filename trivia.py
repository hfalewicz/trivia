#regular functions
def ask_question(): 
    """Print out a question"""
    print "What is Mickey's pet dogs name?"
    print "What animal shallowed a clock in Peter Pan?"
    print "Who is the first Disney princess?"
    print "What U.S. city is The Princess and The Frog set in?"
    print "In The Lion King, where does Mufasa and his family live?"
    print "In the Little Mermaid, what is the name of Prince Eric's dog?"
    print "In Peter pan, what is the way to Neverland?"
    print "What is the name of Cinderella's mice?"
    print "In Monster's Inc, what is Sulley's full name?"

def multiple_choice(): 
    """Print out multiple choice options"""
    print "a. Donald", "b. Pluto", "c. Goofy", "d. Daisy"
    print "a. Tiger", "b. Parrot", "c. Crocodile", "d. Shark"
    print "a. Snow White", "b. Pocahontas", "c. Tiana", "d. Cinderella"
    print "a. Nashville", "b. New York", "c. Atlanta", "d. New Orleans"
    print "a. Love Rock", "b. Pride Rock", "c. Justice Rock", "d. Peace Rock"
    print "a. Gold", "b. Silver", "c. Bronze", "d. None of the above"
    print "a. Dog", "b. Pluto", "c. Max", "d. Mike"
    print "a. First star to the right and straight on  til morning", "b. Second star to the left and straight on til morning", "c. Third star to the right and straight on til morning","d. Second star to the right and straight on til morning"
    print "a. Jesse and Goose", "b. Jess and Jack-Jack", "c. Gus and Jaq", "d. Wes and Jess"
    print "a. Jim A Sullivan", "b. Sullivan", "c. J P Sullivan", "d. James P Sullivan"

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

def user_answer():
    """Figure out is user's answer is right or wrong"""
    raw_input("What is your answer?") 

def play_game():
    ask_question()
    multiple_choice()
    if user_answer is not "a","b","c","d":
        print "Your choice is not valid."
        user_answer
    if user_answer==answer:
        print "Your answer is correct."
    else:
        print "The correct answer is", correct 

#test functions
def test_ask_question(): 
    print (question)

def test_multiple_choice():    
    print (multiple_choice)

def test_answer(): 
    print (question_and_answer)

def test_user_answer(): 
    print (question_and_)
    answer= raw_input("What is your answer?") 

play_game()
