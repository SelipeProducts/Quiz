import random

class option:
  letter = ""
  question_txt = ""

  # getter method for letter
  def get_letter(self): 
      return self.letter
  # setter method for question_txt
  def set_letter(self, x): 
      self.letter = x 
  # getter method for letter
  def get_question_txt(self): 
      return self.question_txt
  # setter method for letter
  def set_question_txt(self, x): 
      self.question_txt = x 

class question:
  my_question = ""
  answer_correct = option()
  answer_wrong1 = option()
  answer_wrong2 = option()
  answer_wrong3 = option()
  answer_wrong4 = option()
  answer_wrong5 = option()
  question_num = 0
  answer_pos = []  #num list with position cordinates
  opt_list = []   #obj list with organized options
  question_score = 0

  # getter method for my_question
  def get_my_question(self): 
      return self.my_question
  # setter method for my_question
  def set_my_question(self, x): 
      self.my_question = x 

  # getter method for answer_correct
  def get_answer_correct(self): 
      return self.answer_correct
  # setter method for answer_correct
  def set_answer_correct(self, x): 
      self.answer_correct = x 

  # getter method for answer_wrong1
  def get_answer_wrong1(self): 
      return self.answer_wrong1
  # setter method for answer_wrong1
  def set_answer_wrong1(self, x): 
      self.answer_wrong1 = x 

  # getter method for answer_wrong2
  def get_answer_wrong2(self): 
      return self.answer_wrong2
  # setter method for answer_wrong2
  def set_answer_wrong2(self, x): 
      self.answer_wrong2 = x 
  
  # getter method for answer_wrong3
  def get_answer_wrong3(self): 
      return self.answer_wrong3
  # setter method for answer_wrong3
  def set_answer_wrong3(self, x): 
      self.answer_wrong3 = x 

  # getter method for answer_wrong4
  def get_answer_wrong4(self): 
      return self.answer_wrong4
  # setter method for answer_wrong4
  def set_answer_wrong4(self, x): 
      self.answer_wrong4 = x 

  # getter method for answer_wrong5
  def get_answer_wrong5(self): 
      return self.answer_wrong5
  # setter method for answer_wrong5
  def set_answer_wrong5(self, x): 
      self.answer_wrong5 = x 

  # getter method for question_num
  def get_question_num(self): 
      return self.question_num
  # setter method for question_num
  def set_question_num(self, x): 
      self.question_num = x 

  # getter method for answer_pos
  def get_answer_pos(self): 
      return self.answer_pos
  # setter method for question_num
  def set_answer_pos(self, x): 
      self.answer_pos = x 
  
  # getter method for opt_list
  def get_opt_list(self): 
      return self.opt_list
  # setter method for opt_list
  def set_opt_list(self, x): 
      self.opt_list = x 

  # getter method for opt_list
  def get_question_score(self): 
      return self.question_score
  # setter method for opt_list
  def set_question_score(self, x): 
      self.question_score = x 
  
  
  def organize_question(self):
    option_a = random.randint(1, 5)
    option_b = random.randint(1, 5)
    while option_b == option_a:
      option_b = random.randint(1, 5)
    option_c = random.randint(1, 5)
    while option_c == option_a or option_c == option_b:
      option_c = random.randint(1, 5)    
    option_d = random.randint(1, 5)
    while option_d == option_a or option_d == option_b or option_d == option_c:
      option_d = random.randint(1, 5)

    option_correct = random.randint(1, 4)
    if option_correct == 1:
      option_a = 0
    elif option_correct == 2:
      option_b = 0
    elif option_correct == 3:
      option_c = 0
    elif option_correct == 4:
      option_d = 0
    #answer will be the option with the value 0
    
    answ_pos_list = [option_a, option_b, option_c, option_d]
    self.set_answer_pos(answ_pos_list)
    #print(option_a, option_b, option_c, option_d)

  def match_compare(self, place, value):
    opt_list = self.get_opt_list()
    opt = option()
    if(len(opt_list) < 4):
      opt_list.append("")
      opt_list.append("")
      opt_list.append("")
      opt_list.append("")
   
    if value == 0:
      opt = self.get_answer_correct()
      opt_list[place] = opt
    elif value == 1:
      opt = self.get_answer_wrong1()
      opt_list[place] = opt
    elif value == 2:
      opt = self.get_answer_wrong2()
      opt_list[place] = opt
    elif value == 3:
      opt = self.get_answer_wrong3()
      opt_list[place] = opt
    elif value == 4:
      opt = self.get_answer_wrong4()
      opt_list[place] = opt
    elif value == 5:
      opt = self.get_answer_wrong5()
      opt_list[place] = opt
    # print(opt_list)
    self.set_opt_list(opt_list)

  def match_answers_with_option(self):
    ans_pos_list = self.get_answer_pos()
    for i in range(0, len(ans_pos_list)):
      self.match_compare(i, ans_pos_list[i])
    
  def print_question(self):
    ques_num = self.get_question_num()
    ques_txt = self.get_my_question()
    print(str(ques_num) + ") " + ques_txt)
    options =  self.get_opt_list()
    op_range = len(options)

    for i in range(0, op_range):
      if i == 0:
        options[i].set_letter("a")
      elif i == 1:
        options[i].set_letter("b")
      elif i == 2:
        options[i].set_letter("c")
      elif i == 3:
        options[i].set_letter("d")
      print(options[i].get_letter(), ")", options[i].get_question_txt())
  
  def compare_answer(self):
    ques_score = self.get_question_score()

    user_in = input("Answer: ")

    answer_c = self.get_answer_correct()
    answer_c_letter = answer_c.get_letter()
    answer_c_quest = answer_c.get_question_txt()

    if(user_in == answer_c_letter or user_in == answer_c_quest):
      ques_score += 10
      self.set_question_score(ques_score)
      print("That's Correct! " + " +10 points")
    else:
      ques_score -= 10
      self.set_question_score(ques_score)
      print("That's Wrong... " + " -10 points")
    #print("\nScore:", self.get_question_score())
    
  
class quiz:
  questions = []
  quiz_score = 0 

  def __init__(self, questions):   
    self.questions = questions
  # getter method for questions
  def get_questions(self): 
      return self.questions
  # setter method for questions
  def set_questions(self, x): 
      self.questions = x 
  
  # getter method for questions
  def get_quiz_score(self): 
      return self.quiz_score
  # setter method for questions
  def set_quiz_score(self, x): 
      self.quiz_score = x 

  
  def parse_questions(self):
    quiz_score = self.get_quiz_score()
    ques_list = self.get_questions()

    for i in range(0,len(ques_list)):
      ques_list[i].set_question_num(i+1)
      ques_list[i].organize_question()
      ques_list[i].match_answers_with_option()
      
      ques_list[i].print_question()
      ques_list[i].compare_answer()
      question_score = ques_list[i].get_question_score()
      quiz_score += question_score
      self.set_quiz_score(quiz_score)

      print("Score:", self.get_quiz_score(),"\n")



  
  #-----------------------------------------------
def main():
  print("Python Quiz by Cesar F. Lopez")
  print()
  aquest = question()
  aquest.set_my_question("What is 4+4 = ?")

  opt_aquest_c = option()
  opt_aquest_c.set_question_txt("8")
  opt_aquest_w1 = option()
  opt_aquest_w1.set_question_txt("4")
  opt_aquest_w2 = option()
  opt_aquest_w2.set_question_txt("9")
  opt_aquest_w3 = option()
  opt_aquest_w3.set_question_txt("16")
  opt_aquest_w4 = option()
  opt_aquest_w4.set_question_txt("20")
  opt_aquest_w5 = option()
  opt_aquest_w5.set_question_txt("10")
  aquest.set_answer_correct(opt_aquest_c)
  aquest.set_answer_wrong1(opt_aquest_w1)
  aquest.set_answer_wrong2(opt_aquest_w2)
  aquest.set_answer_wrong3(opt_aquest_w3)
  aquest.set_answer_wrong4(opt_aquest_w4)
  aquest.set_answer_wrong5(opt_aquest_w5)

  # ------------------------------------------------

  quest1 = question()
  quest1.set_my_question("What is 10x10 = ?")

  opt_quest1_c = option()
  opt_quest1_c.set_question_txt("100")
  opt_quest1_w1 = option()
  opt_quest1_w1.set_question_txt("10")
  opt_quest1_w2 = option()
  opt_quest1_w2.set_question_txt("1000")
  opt_quest1_w3 = option()
  opt_quest1_w3.set_question_txt("99")
  opt_quest1_w4 = option()
  opt_quest1_w4.set_question_txt("20")
  opt_quest1_w5 = option()
  opt_quest1_w5.set_question_txt("0")
  quest1.set_answer_correct(opt_quest1_c)
  quest1.set_answer_wrong1(opt_quest1_w1)
  quest1.set_answer_wrong2(opt_quest1_w2)
  quest1.set_answer_wrong3(opt_quest1_w3)
  quest1.set_answer_wrong4(opt_quest1_w4)
  quest1.set_answer_wrong5(opt_quest1_w5)
  
  # ----------------------------------------------------
  quest2 = question()
  quest2.set_my_question("What is the number for 1 million?")

  opt_quest2_c = option()
  opt_quest2_c.set_question_txt("1000000")
  opt_quest2_w1 = option()
  opt_quest2_w1.set_question_txt("10")
  opt_quest2_w2 = option()
  opt_quest2_w2.set_question_txt("1000")
  opt_quest2_w3 = option()
  opt_quest2_w3.set_question_txt("1000000000")
  opt_quest2_w4 = option()
  opt_quest2_w4.set_question_txt("1000000000000")
  opt_quest2_w5 = option()
  opt_quest2_w5.set_question_txt("0")
  quest2.set_answer_correct(opt_quest2_c)
  quest2.set_answer_wrong1(opt_quest2_w1)
  quest2.set_answer_wrong2(opt_quest2_w2)
  quest2.set_answer_wrong3(opt_quest2_w3)
  quest2.set_answer_wrong4(opt_quest2_w4)
  quest2.set_answer_wrong5(opt_quest2_w5)
  # ----------------------------------------------------
  quest3 = question()
  quest3.set_my_question("What is the number for 1 million?")

  opt_quest3_c = option()
  opt_quest3_c.set_question_txt("1000000")
  opt_quest3_w1 = option()
  opt_quest3_w1.set_question_txt("10")
  opt_quest3_w2 = option()
  opt_quest3_w2.set_question_txt("1000")
  opt_quest3_w3 = option()
  opt_quest3_w3.set_question_txt("1000000000")
  opt_quest3_w4 = option()
  opt_quest3_w4.set_question_txt("1000000000000")
  opt_quest3_w5 = option()
  opt_quest3_w5.set_question_txt("0")
  quest3.set_answer_correct(opt_quest3_c)
  quest3.set_answer_wrong1(opt_quest3_w1)
  quest3.set_answer_wrong2(opt_quest3_w2)
  quest3.set_answer_wrong3(opt_quest3_w3)
  quest3.set_answer_wrong4(opt_quest3_w4)
  quest3.set_answer_wrong5(opt_quest3_w5)
  # ----------------------------------------------------
  quest4 = question()
  quest4.set_my_question("What is 10 to the power of 9")
  opt_quest4_c = option()
  opt_quest4_c.set_question_txt("1000000000")
  opt_quest4_w1 = option()
  opt_quest4_w1.set_question_txt("90")
  opt_quest4_w2 = option()
  opt_quest4_w2.set_question_txt("100000")
  opt_quest4_w3 = option()
  opt_quest4_w3.set_question_txt("9000000000")
  opt_quest4_w4 = option()
  opt_quest4_w4.set_question_txt("9000000000000")
  opt_quest4_w5 = option()
  opt_quest4_w5.set_question_txt("0")
  quest4.set_answer_correct(opt_quest4_c)
  quest4.set_answer_wrong1(opt_quest4_w1)
  quest4.set_answer_wrong2(opt_quest4_w2)
  quest4.set_answer_wrong3(opt_quest4_w3)
  quest4.set_answer_wrong4(opt_quest4_w4)
  quest4.set_answer_wrong5(opt_quest4_w5)
  # ----------------------------------------------------
  quest5 = question()
  quest5.set_my_question("What is the absolute value of -3")
  opt_quest5_c = option()
  opt_quest5_c.set_question_txt("3")
  opt_quest5_w1 = option()
  opt_quest5_w1.set_question_txt("6")
  opt_quest5_w2 = option()
  opt_quest5_w2.set_question_txt("9")
  opt_quest5_w3 = option()
  opt_quest5_w3.set_question_txt("-3")
  opt_quest5_w4 = option()
  opt_quest5_w4.set_question_txt("30")
  opt_quest5_w5 = option()
  opt_quest5_w5.set_question_txt("9000")
  quest5.set_answer_correct(opt_quest5_c)
  quest5.set_answer_wrong1(opt_quest5_w1)
  quest5.set_answer_wrong2(opt_quest5_w2)
  quest5.set_answer_wrong3(opt_quest5_w3)
  quest5.set_answer_wrong4(opt_quest5_w4)
  quest5.set_answer_wrong5(opt_quest5_w5)
  # ----------------------------------------------------
  # ----------------------------------------------------
  quest_list = [aquest, quest1, quest2, quest4, quest5]
  random.shuffle(quest_list)
  quizgame = quiz(quest_list)
  quizgame.parse_questions()

#test question run code
# aquest.print_question()
# aquest.compare_answer()


main()



#Make sure object have paranthesis when instantiating