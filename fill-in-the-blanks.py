# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
difficulty_levels = ['easy','medium','hard','custom','random']
difficulty_default = difficulty_levels[0]
missed_answer_range = [3, 4, 5, 6]
missed_answer_default = missed_answer_range[0]

def display_prompt(user_prompt, possible_answers, default_answer,max_failed_attempts, var_type, show_possible_answers):
	#	Standardized prompt; after maximum allowed attempts, assign default/correct value
	# user_prompt is a string alerting the user to the desired input
	# possible_answers is always a list of values of any length; used to determine if answer is appropriate or correct
	# default_answer is a string used after the maximum failed attempts are exceeded
	# max_failed_attempts is an integer; once exceeded a default or correct answer will be used
	# var_type is a string; allows user inputs to be sanitized to avoid errors
	# show_possible_answers is a boolean, allowing choices to be displayed where needed
	failed_attempts = 0
	result = ""
	while result not in possible_answers and failed_attempts <= max_failed_attempts:
		prompt = build_prompt(user_prompt, choice_list, var_type, show_possible_answers)
		result = raw_input(prompt)
		result = result_norm(result, var_type)
		failed_attempts += 1
	if failed_attempts >= max_failed_attempts:
		return default_answer
	return result

def build_choices(choice_list, var_type):
	if var_type == "string":
		choices = ", ".join(choice_list)
	elif var_type == "int":
		choices = str(min(choice_list)) + " - " + str(max(choice_list))
	return choices

def build_prompt(user_prompt, choice_list, var_type, show_possible_answers):
	prompt = user_prompt
	if show_possible_answers:
		choices = build_choices(possible_answers, var_type)
		prompt += "(" + choices + ")"
	prompt += ": "

def get_difficulty():
	# Prompts user for desired difficulty
	difficulty = display_prompt("Enter your prefered difficulty",
		difficulty_levels,
		difficulty_default,
		5,
		"string" )

def get_max_missed_answers():
	# Prompts user for maximum missed answers - used in custom difficulty games
	difficulty = display_prompt("Maximum number of missed answers",
		missed_answer_range,
		missed_answer_default,
		5,
		"int" )

def result_norm(result, var_type):
	# Cleans user inputs for use in validations
	# result is the value to be cleaned based on its /intended/ type
	# type is the /intended/ type; rules follow based on necessary validations and substitutions
	if var_type == "string":
		result = result.lower()
	elif var_type == "int":
		if type(result) != 'int':
			result = -99
	return result

def display_paragraph(quiz):
	user_input = raw_input("\033[0;34mType in a value\033[0m")
	print user_input

#print get_difficulty()
print range(1,10)
#print get_max_missed_answers()
print build_choices(missed_answer_range,"int")
print build_choices(difficulty_levels,"string")