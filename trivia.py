#regular functions
def ask_question(): 
    """Print out a question"""
    print (‘What is Mickey’s pet dogs name?’)
    #write code

def multiple_choice(): 
    """Print out multiple choice options"""
   print(‘a. Donald’, ‘b. Pluto’, ‘c. Goofy’, ‘d. Daisy’)
    #write code

def answer(): 
    """Correct answer for each question"""
    correct_1= b
    #write code

def user_answer():
    """Figure out is user’s answer is right or wrong"""
    #write code

def play_game(): 
   for question,choices,correct in [[‘What is Mickey’s pet dogs’ name?’, [‘a. Donald’, ‘b. Pluto’, ‘c. Goofy’, ‘d. Daisy’], ‘b’], [‘What animal swallowed a clock in Peter Pan?’, [‘a. Tiger’, ‘b. Parrot’, ‘c. Crocodile’, ‘d. Shark’], ‘c’], ['Who is the first Disney princess?', ['a. Snow White','b. Pocahontas', 'c. Tiana', 'd. Cinderella'], 'a'], ['What U.S. city is The Princess and The Frog set in?', ['a. Nashville', 'b. New York', 'c. Altana', 'd. New Orleans'], 'd'], ['In the Lion King, where does Mufasa and his family live?', ['a. Love Rock', 'b. Pride Rock', 'c. Justice Rock', 'd. Peace Rock'], 'b'], ['During the ballroom scene of Beauty & the Beast, what color is her dress?', ['a. Gold', 'b. Silver', 'c. Bronze', 'd. None of the above'], 'a'], ['In the Little Mermaid, what is the name of the dog?', ['a. Dog', 'b. Pluto', 'c. Max', 'd. Mike'], 'c'], ['In Peter Pan, what is the way to Neverland?', [‘a. First star to the right and straight on  til morning', 'b. Second star to the left and straight on til morning', 'c. Third star to the right and straight on til morning','d. Second star to the right and straight on til morning'], 'd'], ['What is the name of the mice in Cinderella?', ['a. Jesse and Goose', 'b. Jess and Jack-Jack', 'c. Gus and Jaq', 'd. Wes and Jess'], 'c'], ['In Monsters Inc., what is the full name for Sulley?', ['a. Jim A Sullivan', 'b. Sullivan', 'c. J P Sullivan', 'd. James P Sullivan'], 'd']]: 
        print(question)
        print(choices)
        user_answer= raw_input(‘What is your answer?’) 
            if user_answer= correct
                print ‘You got the problem correct!’
            if user_answer=!= correct
                print ‘The correct answer was’, correct
    print ‘You have completed all questions. Thank you for playing.’


#test functions
def test_ask_question(): 
    print question

def test_multiple_choice():    
    print multiple_choice

def test_answer(): 
    print question_and_answer

def test_user_answer(): 
    print question_and_
    answer= raw_input(‘What is your answer?’) 
