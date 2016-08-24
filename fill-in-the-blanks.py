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

easy_paragraph = '''All ____1____s follow in a specific format: def ____1_____name(argument1, argument2,...). One ____1____ can pass its results using the ____2____ command, where the format is ____2____ value. As a rule you want a ____1____ to have ____3____ purpose; additional purposes are ideally moved into another ____1____. This helps reduce ____4____ and prevent bugs. It also promotes readability.'''

easy_answers = [["function","functions"],["return"],["one","1"],["repetition","repeated code"]]

medium_paragraph = '''Text variables are refered to as ____1____s. All  ____1____ variables must be surrounded with either a single or double ____2____. New characters can be added to the ____1____ with the ____3____ operator. A ____1____ can be easily searched using the ____1____.____4____(search_value) function. If needed, you can iterate through each character in a ____1____ using its ____5____ value - and for a range.'''

medium_answers = [["string","strings"],["quote","quotes"],["+"],["find"],["index"]]

hard_paragraph = '''A ____1____ is usually created with a declaration that uses the square brackets - []. Within the brackets, each new value is separated with a ____2____. Each value has an integer index value, with ____3____ referring to the first value. A ____1____'s length can be determined using the len(____1_____name). A ____4____ loop works well with ____1____s by using the format: ____4____ variable_name in ____1_____name, which then iterates through each value in the ____1____ - ____5____ at a time.'''

hard_answers = [["list"],["comma","commas"],["0"],["for"],["one","1"]]

extra_paragraph = '''At times, we need the logic to iterate over a set of values, to do this we use ____1____s. There are two kinds of ____1____s: ____2____ and while. When you have a choice, it's best to use a ____2____ ____1____. If you must use a while ____1____, be sure to give it a ____3____ case - something that will always force the code to stop. Otherwise you may create an ____4____ ____1____.'''

extra_answers = [["loop","loops"],["for"],["base"],["infinite"]]

quizes = {}
quizes["easy"] = {}
quizes["easy"]["paragraph"] = easy_paragraph
quizes["easy"]["answers"] = easy_answers
quizes["medium"] = {}
quizes["medium"]["paragraph"] = medium_paragraph
quizes["medium"]["answers"] = medium_answers
quizes["hard"] = {}
quizes["hard"]["paragraph"] = hard_paragraph
quizes["hard"]["answers"] = hard_answers
quizes["extra"] = {}
quizes["extra"]["paragraph"] = extra_paragraph
quizes["extra"]["answers"] = extra_answers

# quizes = {"easy":{"paragraph": easy_paragraph, "answers": easy_answers}}
# quizes = {"medium":{"paragraph": medium_paragraph, "answers": medium_answers}}
# quizes = {"hard":{"paragraph": hard_paragraph, "answers": hard_answers}}
# quizes = {"extra":{"paragraph": extra_paragraph, "answers": extra_answers}}

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
difficulty_levels = ['easy','medium','hard','long','custom']
difficulty_default = difficulty_levels[0]
missed_answer_range = [3, 4, 5, 6]
missed_answer_default = missed_answer_range[0]

def get_quiz():
	max_missed_answers = missed_answer_default
	difficulty = get_difficulty(difficulty_levels)
	if difficulty == "custom":
		max_missed_answers, difficulty = difficulty_custom_values()
	if difficulty == "long":
		run_difficulty_long()
	else:
		run_quiz(quizes[difficulty]["paragraph"],
			quizes[difficulty]["answers"],
			max_missed_answers)

def get_difficulty(levels):
	# Prompts user for desired difficulty
	difficulty = display_prompt("Enter your prefered difficulty",
		levels,
		difficulty_default,
		5,
		"string",
		True )
	return difficulty

def get_max_missed_answers():
	# Prompts user for maximum missed answers - used in custom difficulty games
	max_missed_answers = display_prompt("Maximum number of missed answers",
		missed_answer_range,
		missed_answer_default,
		5,
		"int"
		, True )
	return max_missed_answers

def difficulty_custom_values():
		max_missed_answers = get_max_missed_answers()
		new_level_list = []
		for level in difficulty_levels:
			if level != "custom":
				new_level_list += level
			difficulty = get_difficulty(new_level_list)
			return max_missed_answers, difficulty

def run_difficulty_long():
	for index in range (0,len(quizes)):
		run_quiz(quizes[index]["paragraph"],
		quizes[index]["answers"],
		max_missed_answers)

def run_quiz(paragraph, answer_list, max_missed_answers):
	for answer_index in range (0, len(answer_list)):
		replacement_new = display_prompt(paragraph,
		 answer_list[answer_index],
		 answer_list[answer_index][0],
		 max_missed_answers,
		 "string",
		 False,
		 answer_index)
		paragraph = paragraph.replace(replacement_target, replacement_new)

def run_question(question_big, prompt, possible_answers, answer_index):
	failed_attempts = 0
	while is_not_answered(result, possible_answers) and is_within_max_attempts(failed_attempts, max_failed_attempts):
		question_big = build_question_full(
			paragraph,
			prompt_preamble,
			answer_index)
		answer = display_question()
		replace = replace()
	return

def is_not_answered(result, possible_answers):
	result = result not in possible_answers
	return result

def is_within_max_attempts():
	result = failed_attempts < max_failed_attempts
	return result

def return_answer():
	result = raw_input(prompt)
	result = result_norm(result, var_type)
	return

def display_prompt(paragraph_formatted, possible_answers, default_answer,max_failed_attempts, var_type, is_quiz_prompt, answer_number):
	failed_attempts = 0
	result = ""
	prompt_preamble = ""
	replacement_target = "_" * 4 + str(answer_number + 1) + "_"*4
	prompt = "What should be substituted for " + replacement_target + "? "
	while result not in possible_answers and failed_attempts < max_failed_attempts:
		prompt = build_question_full(paragraph_formatted, prompt_preamble, prompt)
		prompt += build_prompt_question(user_question,
		 possible_answers,
		 var_type,
		 is_quiz_prompt)
		result = raw_input(prompt)
		result = result_norm(result, var_type)
		failed_attempts += 1
		prompt_preamble = prompt_response_after_wrong(failed_attempts,max_failed_attempts)
	if failed_attempts >= max_failed_attempts:
		return default_answer
	if is_quiz_prompt:
		prompt_preamble = prompt_response_good(result, default_answer)
	return default_answer

def build_question_full(paragraph, prompt_preamble, answer_index):
	question_full = "\n\n" + paragraph + "\n\n"
	question_full += prompt_preamble
	question_full += prompt
	return question_full

def build_replacement_value 

def prompt_response_good(result, default_answer):
	if result == default_answer:
		print "\n\nCorrect!"
	else:
		new_prompt = "\n\n\While this is an approved answer, a more accurate answer would be '" + default_answer + ".'"
		new_prompt = add_text_color(new_prompt, new_prompt, "red")
		return new_prompt

def prompt_preamble_after_wrong(failed_attempts, max_failed_attempts):
	prompt = "\n\nPlease try again.\n"
	prompt = add_text_color(prompt, prompt, "red")
	prompt += "You have " + str(max_failed_attempts - failed_attempts) + " attempts left."
	return prompt

def build_prompt_question(user_prompt, possible_answers, var_type, is_quiz_prompt):
	prompt = "\n" + user_prompt
	if not is_quiz_prompt:
		choices = build_choices(possible_answers, var_type)
		prompt += " (" + choices + ")"
	prompt += ": "
	return question

def build_choices(possible_answers, var_type):
	if var_type == "string":
		choices = ", ".join(possible_answers)
	elif var_type == "int":
		choices = str(min(possible_answers)) + " - " + str(max(possible_answers))
	return choices

def result_norm(result, var_type):
	# Cleans user inputs for use in validations
	# result is the value to be cleaned based on its /intended/ type
	# type is the /intended/ type; rules follow based on necessary validations and substitutions
	if var_type == "string":
		result = result.lower()
	elif var_type == "int":
		if result.isdigit():
			result = int(result)
	return result

def add_text_color(replacement_target, wrap_string, color_value):
	color_number = 37
	if color_value == "red":
		color_number = "31"
	color_wrapped_text = "033[0;" + color_number + wrap_string + "\033[0m"
	colorized_text = replacement_target.replace(wrap_string, color_wrapped_text)
	return colorized_text

#print get_difficulty()
#print range(1,10)
#print get_max_missed_answers()
#print build_choices(missed_answer_range,"int")
#print build_choices(difficulty_levels,"string")
print run_quiz(quizes["medium"]["paragraph"],quizes["medium"]["answers"],5)
#print quizes["easy"]["answers"]