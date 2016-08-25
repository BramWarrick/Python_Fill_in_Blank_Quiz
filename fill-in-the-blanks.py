# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a prompt_header containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the prompt_header.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample prompt_header that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own prompt_headers as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_prompt_header = '''All ____1____s follow in a specific format: def ____1_____name(argument1, argument2,...). One ____1____ can pass its results using the ____2____ command, where the format is ____2____ value. As a rule you want a ____1____ to have ____3____ purpose; additional purposes are ideally moved into another ____1____. This helps reduce ____4____ and prevent bugs. It also promotes readability.'''

easy_answers = [["function","functions"],["return"],["one","1"],["repetition","repeated code"]]

medium_prompt_header = '''Text variables are refered to as ____1____s. All ____1____ variables must be surrounded with either a single or double ____2____. New characters can be added to the ____1____ with the ____3____ operator. A ____1____ can be easily searched using the ____1____.____4____(search_value) function. If needed, you can iterate through each character in a ____1____ using its ____5____ value - and for a range.'''

medium_answers = [["string","strings"],["quote","quotes"],["+","plus"],["find"],["index"]]

hard_prompt_header = '''A ____1____ is usually created with a declaration that uses the square brackets - []. Within the brackets, each new value is separated with a ____2____. Each value has an integer index value, with ____3____ referring to the first value. A ____1____'s length can be determined using the len(____1_____name). A ____4____ loop works well with ____1____s by using the format: ____4____ variable_name in ____1_____name, which then iterates through each value in the ____1____ - ____5____ at a time.'''

hard_answers = [["list"],["comma","commas",","],["0"],["for"],["one","1"]]

extra_prompt_header = '''At times, we need the logic to iterate over a set of values, to do this we use ____1____s. There are two kinds of ____1____s: ____2____ and while. When you have a choice, it's best to use a ____2____ ____1____. If you must use a while ____1____, be sure to give it a ____3____ case - something that will always force the code to stop. Otherwise you may create an ____4____ ____1____.'''

extra_answers = [["loop","loops"],["for"],["base"],["infinite"]]

quizes = {}
quizes["easy"] = {}
quizes["easy"]["prompt_header"] = easy_prompt_header
quizes["easy"]["answers"] = easy_answers
quizes["medium"] = {}
quizes["medium"]["prompt_header"] = medium_prompt_header
quizes["medium"]["answers"] = medium_answers
quizes["hard"] = {}
quizes["hard"]["prompt_header"] = hard_prompt_header
quizes["hard"]["answers"] = hard_answers
quizes["extra"] = {}
quizes["extra"]["prompt_header"] = extra_prompt_header
quizes["extra"]["answers"] = extra_answers

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a prompt_header and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

#Global variables
difficulty_levels = ['easy','medium','hard','long','custom']
difficulty_default = difficulty_levels[0]
missed_answer_range = [3, 4, 5, 6]
missed_answer_default = missed_answer_range[0]
max_line_length = 60

def main_sequence():
	# Purpose: Triggered on file open; Guides all subsequent behavior
	# ------------------------------------------------------------------
	print ("\033c")		# Clear screen; no up scroll
	max_missed_answers = missed_answer_default
	difficulty = get_difficulty(difficulty_levels)
	# Get difficulty
	if difficulty == "custom":
		# Get max missed answers and a new difficulty level
		max_missed_answers, difficulty = difficulty_custom_values()
	# A selection of easy, medium, hard, or long is made by this point
	if difficulty == "long":
		# Run all the quizes
		run_difficulty_long(max_missed_answers)
	else:
		# Run the selected difficulty level
		run_quiz(difficulty, max_missed_answers)

def get_difficulty(levels):
	# Purpose: Prompts user for desired difficulty level. Adaptable input.
	# Inputs:
	#		levels is a list of levels, appropriate to that point in the logic ("custom" creates a logical branch)
	# Output:
	#		difficulty is the user desired difficulty. If they exceeded the max_failed_attempts, they are are given the default
	# ------------------------------------------------------------------
	print ("\033c")		# Clear screen; no up scroll
	difficulty = display_standard_prompt("What is your prefered difficulty",
		levels,
		difficulty_default,
		5,
		"string")
	print "\nYou selected " + difficulty + ".\n\n"
	return difficulty

def difficulty_custom_values():
	# Purpose: Asks user to select difficulty level and maximum missed answers (retries + 1, basically)
	# Output:
	#		max_missed_answers is the total number of tries the user would like to have
	#		difficulty is the desired difficulty for the custom game
	# ------------------------------------------------------------------
	# Build a new list, same as before, but without "custom"
	new_level_list = []
	for level in difficulty_levels:		# Global
		if level != "custom":
			new_level_list.append(level)
	# Get the desired difficulty level, will default if needed
	prompt = "Custom allows you to chose a difficulty and customize how many times you can attempt an answer."
	print reformat_max_line_length(prompt, max_line_length)
	difficulty = get_difficulty(new_level_list)
	# Asks user for prefered number of maximum missed answers
	max_missed_answers = get_max_missed_answers()
	return max_missed_answers, difficulty

def get_max_missed_answers():
	# Purpose: Prompts user for the maximom missed answers - used exclusively in custom games
	# Output:
	#		max_missed_answers is the total number of times the user would like to retry. 
	#			If they don't answer with an appropriate value, the default is assigned
	# ------------------------------------------------------------------
	print ("\033c")		# Clear screen; no up scroll
	max_missed_answers = display_standard_prompt("What is your desired number of maximum missed answers",
		missed_answer_range,			# Global
		missed_answer_default,		# Global
		5,
		"int")
	# Show user their selection, if part of approved list
	print ("\033c")		# Clear screen; no up scroll
	print "\nYou selected " + str(max_missed_answers) + ".\n\n"
	return max_missed_answers

def run_difficulty_long(max_missed_answers):
	# Purpose: Runs all quizes - including the "extra" that's not selectable from normal difficulty prompts
	#		This is not sorted in an easy -> hard format
	# Inputs:
	#		max_missed_answers is the maximum number of times a question will be asked before the correct answer is given
	# ------------------------------------------------------------------
	for difficulty_level in quizes:
		run_quiz(difficulty_level,
		max_missed_answers)

def run_quiz(difficulty, max_missed_answers):
	# Purpose: Brings everything together for the quiz - per difficulty level
	# Inputs:
	# 	prompt_header is the paragraph lead in
	# 	answer_list is the set of approved answers for any prompt - allows for ambiguity with plural, numbers, typed symbol names
	# Output:
	#		Only a print to the screen showing the final, complete paragrach. No variables returned.
	# ------------------------------------------------------------------
	prompt_header = quizes[difficulty]["prompt_header"]
	answer_list = quizes[difficulty]["answers"]
	prompt_feedback = ""
	# Loops through all prompts; calling another procedure to display and handle results
	for answer_index in range (0, len(answer_list)):
		prompt_question = "What word or symbol should replace "
		replace_string, replacement_new, prompt_feedback = display_quiz_prompt(prompt_header,
			prompt_feedback,
			prompt_question,
			answer_list[answer_index],
			answer_list[answer_index][0],
			max_missed_answers,
			answer_index)
		prompt_header = prompt_header.replace(replace_string, replacement_new)
	print "\n\n" + reformat_max_line_length(prompt_header, max_line_length)

def display_quiz_prompt(prompt_header, prompt_feedback, prompt_question, possible_answers, default_answer, max_failed_attempts, answer_index):
	# Purpose Runs one question until answered correctly or max failed attempts is reached.
	# Inputs: (none are formatted for line length at the point of input)
	#		prompt_header is the paragraph
	#		prompt_feedback is the feedback from the previous answer
	#		promt_question is the call to action (without the ____x____ and ensuinig punctuation)
	#		possible_answers is a list of all approved answers
	#		default_answers is the one, best answer
	#		max_failed_attempts is the number of times a question will be presented to the user before the default answer is given
	#		answer_index is the place in the overall paragraph - used for creating the prompt and replace_string
	# Outputs:
	#		replace_string (e.g. "____1____"); used externally for replacement in prompt_header with correct answer
	#		default_value used as replacement for replace string in external function
	#		prompt_feedback is necessary to provide user feedback outside of this function
	# ------------------------------------------------------------------
	print ("\033c")		# Clear screen; no up scroll
	failed_attempts = 0
	answer = ""
	# Loop through user answers until answered or max exceeded
	while is_not_answered(answer, possible_answers) and is_within_max_attempts(failed_attempts, max_failed_attempts):
		# Get full_question and the replace_sting (e.g "____1____")
		full_question, replace_string = build_quiz_question(prompt_header, prompt_feedback, prompt_question, answer_index)
		# Add color to the prompted area (replace_string), for improved readability
		full_question = add_text_color(full_question, replace_string, "green")
		# Get user answer
		answer = return_answer(full_question, "string")
		if is_not_answered(answer, possible_answers):
			# Answer was wrong; increment failed_attempts and create feedback
			failed_attempts += 1
			prompt_feedback = prompt_feedback_after_wrong(failed_attempts, max_failed_attempts)
			print ("\033c")		# Clear screen; no up scroll
	if not is_within_max_attempts(failed_attempts, max_failed_attempts):
		# max_failed_attempts has been exceeded; provide feedback & the correct answer
		prompt_feedback = prompt_feedback_after_max_attempts_quiz(max_failed_attempts, default_answer)
		print "\n\n" + prompt_feedback
		return replace_string, default_answer, prompt_feedback
	# Answer was correct; provide feedback, return result
	print ("\033c")		# Clear screen; no up scroll
	prompt_feedback = prompt_response_good(answer, default_answer)
	return replace_string, default_answer, prompt_feedback

def reformat_max_line_length(text_string, max_line_length):
	# Purpose: Takes the text_sting and breaks it on line breaks, then feeds it through a line resizer
	# Assumption: It's okay if strings, if lacking a space, exceed the max_line_length
	# Inputs:
	#		text_string is the raw string to be reformatted with new lines (\n) added
	#		max_line_length is maximum length of any displayed line within a human readable
	# Output:
	#		result is the text string, unchanged except for the addition of new lines, where appropriate
	# ------------------------------------------------------------------
	new_string = ""
	text_line_list = text_string.split("\n")
	for line in text_line_list:
		new_string += reformat_line_max_line_length(line, max_line_length)
	return new_string

def reformat_line_max_line_length(text_string, max_line_length):
	# Purpose: Takes the text_sting and reformats it to a maximum length
	# Assumption: It's okay if strings, if lacking a space, exceed the max_line_length
	# Inputs:
	#		text_string is the raw string (line) to be reformatted with new lines (\n) added
	#		max_line_length is maximum length of any displayed line within a human readable
	# Output:
	#		result is the text string, unchanged except for the addition of new lines, where appropriate
	# ------------------------------------------------------------------
	temp_string = text_string[0:max_line_length]
	cut_value = temp_string.rfind(" ")
	# If text_string has no spaces or is already of appropriate length, return text_string
	if cut_value == -1 or len(text_string) <= max_line_length:
		return text_string + "\n"
	else:
		# Recursively iterate through text_string, building a human readable (the +1 is to move past the " ")
		result = text_string[0:cut_value] + "\n" + reformat_max_line_length(text_string[cut_value + 1:],max_line_length)
	return result

def display_standard_prompt(prompt_question, possible_answers, default_answer, max_failed_attempts, var_type):
	# Prompts user for answer (non-quiz) and allows a number of retries if answers provided are not in list
	#Inputs:
	# 	prompt_question is the question to be posed
	# 	possible_answers is a list of possible answers, can be numbers or text. User is prompted with values.
	# 	default_answer is assigned after max_failed_attempts is exceeded
	# 	var_type is used to format prompt intuitively as well as for answer clean up (string -> int)
	# Output:
	#		user answer, or if exceeded max_failed_attempts, I set them to default
	# ------------------------------------------------------------------
	failed_attempts = 0
	answer = ""
	prompt_feedback = ""
	# While no possible answers are selected and max_failed_attempts is not excceeded
	while is_not_answered(answer, possible_answers) and is_within_max_attempts(failed_attempts, max_failed_attempts):
		# Builds the full question, with header, feedback and specific call to action - in that order
		full_question = build_standard_question(prompt_feedback, prompt_question, possible_answers, var_type)
		answer = return_answer(full_question, var_type)
		if is_not_answered(answer, possible_answers):
			# Answer was not in approved list; provide user feedback
			failed_attempts += 1
			prompt_feedback = prompt_feedback_after_wrong(failed_attempts, max_failed_attempts)
	if not is_within_max_attempts(failed_attempts, max_failed_attempts):
		# Max attempts exceeded; provide feedback and correct answer
		prompt_feedback = prompt_feedback_after_max_attempts_standard(max_failed_attempts, default_answer)
		print "\n\n" + prompt_feedback
		return default_answer
	return answer

def return_answer(full_question, var_type):
	# Purpose: solicits user input and conforms it to type
	# Inputs:
	#		full_question is the prompt provided to the user
	#		var_type allows the result to be conformed to expectation (e.g. "3" -> 3)
	# Output:
	#		User input, regardless of quality
	# ------------------------------------------------------------------
	result = raw_input(full_question)
	# clean up the answr so comparisons work well
	result = result_norm(result, var_type)
	return result

def result_norm(result, var_type):
	# Purpose: cleans user inputs for use in validations
	# Inputs:
	#		result is the user answer from an external function
	#		var_type is the intended final type for the answer
	# Output:
	#		result is the sanitized version of the answer (lower case or str -> int)
	# ------------------------------------------------------------------
	if var_type == "string":
		# Make lowercase for easier comparisons
		result = result.lower()
	elif var_type == "int":
		if result.isdigit():
			# Is numberic, so convert this over to int
			result = int(result)
	return result

def build_standard_question(prompt_feedback, prompt_question,  possible_answers, var_type):
	# Purpose: creates the user question; non-quiz (e.g. difficulty_level)
	# Inputs:
	#		prompt_feedback is feedback on previous answer (e.g. "Correct!")
	#		prompt_question is the call to action part of the string
	# 	possible_answers is used to provide a list of choices within the question line
	#		var_type is used to make the choices intuitive to a user; text values: listed, numeric: range
	# Output:
	#		prompt is a human readable, line formatted string
	# ------------------------------------------------------------------
	prompt = "\n"
	if len(prompt_feedback) > 0:
		# Feedback exists, append line break, and feedback - feedback is cleaned for max_line_length
		prompt += "\n" + reformat_max_line_length(prompt_feedback, max_line_length)
	# Gets choice string, which is adaptively built based on var_type
	choice_string = build_choice_string(possible_answers, var_type)
	# Create prompt_question; this is kept separate since it needs a SEPARATE cleaning for max_line_length
	prompt_question += " " + choice_string + "?:  "
	prompt_question = "\n" + reformat_max_line_length(prompt_question, max_line_length)
	prompt += prompt_question
	return prompt

def build_choice_string(possible_answers, var_type):
	# Purpose: Takes a list and formats it into a human readable, parenthetical
	# Inputs:
	#		possible_answers is list of all possible answers; for reformatting into string
	#		var_type is a string that tells the function how to respond. String is a full list; int is a numeric range.
	# Output:
	#		choice is the formatted listing of choices, based on desired format
	# ------------------------------------------------------------------
	if var_type == "string":
		# Desired format is string, so make a full list of values
		choices = ", ".join(possible_answers)
	elif var_type == "int":
		# Desired format is int, so create a number range
		choices = str(min(possible_answers)) + " - " + str(max(possible_answers))
	if len(choices) > 0:
		choices = "(" + choices + ")"
	return choices

def build_quiz_question(prompt_header, prompt_feedback, prompt_question, answer_index):
	# Purpose: Takes the various elements for a quiz question and turns it into two strings:
	#		full_question and the substring to be highlighted.
	#		All sections are reformatted to reflect max_line_length (global variable)
	# Inputs:
	#		prompt_header is, in this context, the leading paragraph for a quiz question
	#		prompt_feedback is the feedback from the previous user entry
	#		prompt_question is the specific call to action
	#		answer_index guides the function in creating the replace_string - the area of concern for this quiz.
	#			The value created with this is also needed externally for substitutions.
	# Outputs:
	#		prompt is the full string to be displayed to the user in raw form
	#		replace_target is the string, found within prompt, that will need further action (highlighting, substitution)
	# ------------------------------------------------------------------
	prompt = ""
	if len(prompt_header) > 0:
		# prompt_header extists, so format it correctly for line length and vertical space
		prompt += "\n" + reformat_max_line_length(prompt_header, max_line_length) + "\n"
	if len(prompt_feedback) > 0:
		# prompt_feedback extists, so format it correctly for line length and vertical space
		prompt += "\n" + reformat_max_line_length(prompt_feedback, max_line_length)
	# build replace_string, then use it in the final parts of the prompt
	replace_string = "_" * 4 + str(answer_index+1) + "_" * 4
	prompt += "\n" + prompt_question + " " + replace_string + "?  "
	return prompt, replace_string

def prompt_response_good(result, default_answer):
	# Purpose: creates a string for user feedback. Used when answers are correct.
	#	Inputs:
	# 	result is their answer, which we know is in the approved list, but may not be the default (best) answer.
	# 	default_answer is the best answer to the question. Response to the user will change if they gave the best answer.
	# Output:
	# response is a string to be used as feedback to the user, based on their answer.
	# ------------------------------------------------------------------
	if result == default_answer:
		# Best answer was given
		response = "Correct!"
		response = add_text_color(response, response, "green")
	else:
		# Approved, but not best answer was provided
		response = "While this is an approved answer, a more accurate answer would be '" + str(default_answer) + ".'"
		response = add_text_color(response, response, "green")
	return response

def prompt_feedback_after_wrong(failed_attempts, max_failed_attempts):
	# Purpose: creates a string for user feedback. Used when the answer is incorrect.
	# Inputs:
	#		failed_attempts is the count of failed attempts on this answer
	#		max_failed_attempts is the global or user defined maximum number of retries per question
	#	Ouput:
	#		response is a string with feedback to the user based on their input. Grammar is correct.
	# ------------------------------------------------------------------
	response = "Please try again.\n"
	response = add_text_color(response, response, "red")
	response += "You have " + str(max_failed_attempts - failed_attempts) 
	# GRAMMAR NAZI saw this coming
	if max_failed_attempts - failed_attempts == 1:
		response += " attempt left."
	else:
		response += " attempts left."
	return response

def prompt_feedback_after_max_attempts_standard(max_failed_attempts, default_answer):
	# Purpose: creates a string for user feedback. Used when maximum failed attempts is exceeded.
	#		NON-QUIZ (final area of response is different)
	# Inputs:
	#		max_failed_attempts is the maximum number of times a question will be presented
	#		default answer is used when max attempts is exceeded - this is communicated to the user
	# Output:
	#		response is the feedback to be displayed to the user		
	# ------------------------------------------------------------------
	response = "You've reached the maximum number of attempts (" + str(max_failed_attempts) + ")."
	response = add_text_color(response, response, "red") 
	response += "\nYou have been defaulted to '" + str(default_answer) + ".'"	
	return response

def prompt_feedback_after_max_attempts_quiz(max_failed_attempts, default_answer):
	# Purpose: creates a string for user feedback. Used when maximum failed attempts is exceeded.
	#		QUIZ (final area of response is different)
	# Inputs:
	#		max_failed_attempts is the maximum number of times a question will be presented
	#		default answer is used when max attempts is exceeded - this is communicated to the user
	# Output:
	#		response is the feedback to be displayed to the user	
	# ------------------------------------------------------------------
	response = "You've reached the maximum number of attempts."
	response = add_text_color(response, response, "red")
	response += "\nThe desired answer was '" + default_answer + ".'\n"
	return response

def add_text_color(replacement_target, wrap_string, color_value):
	# Purpose: adds color to a section of text
	# Inputs:
	#		replacement_target is the full text, within which color will be added
	#		wrap string is the string to be wrapped in the intended color
	#		color_value is a string with the color name; only two are allowed: red & green
	# Output:
	#		colorized_text is the text with color added, assuming wrap string was in replacement string
	# ------------------------------------------------------------------
	color_number = "37m"			# White
	if color_value == "red":
		color_number = "31m"
	elif color_value == "green":
		color_number = "32m"
	# Create new variable - wrapped string with color tags
	color_wrapped_text = "\033[0;" + color_number + wrap_string + "\033[0m"
	# Replace text with colorized version
	colorized_text = replacement_target.replace(wrap_string, color_wrapped_text)
	return colorized_text

def is_not_answered(result, possible_answers):
	# Purpose: created to make logic more human readable in calling function
	#		If result is found in possible_answers it returns False; otherwise it's True
	# Inputs:
	#		result is the user answer
	#		possible_answers is a list of possible answers.
	# Output:
	#		result is the True/False of whether an appropriate answer was entered
	# ------------------------------------------------------------------
	result = result not in possible_answers
	return result

def is_within_max_attempts(failed_attempts, max_failed_attempts):
	# Purpose: created to make logic more human readable in calling function
	#		If max failed attempts has NOT been exceeded, this returns True, else False
	# Inputs:
	#		failed_attempts is the running total of user attemps at an appropriate answer
	#		max_failed_attempts is the maximum, once exceeded this function returns False
	# Output:
	#		result is the True/False of whether the attempts is still within allowed number range
	# ------------------------------------------------------------------
	result = failed_attempts < max_failed_attempts
	return result

# print prompt_feedback_after_wrong(3, 5)
# print display_standard_prompt("Yes?", ["yes","no"], "yes", 5, "string")
# print is_within_max_attempts(4, 3)
# print build_choice_string(['3','4','5'], "string")
# print build_quiz_question("empty feedback", "", "Look okay", 3)
# print display_quiz_prompt("this is a paragraph. No really, it is.", "number", ['3','4','5'], '5', 5,3)
main_sequence()
# print get_difficulty(difficulty_levels)
# print reformat_max_line_length(quizes["easy"]["prompt_header"], 60)

# test =  "You've reached the maximum number of attempts.\n"
# test += "The desired answer was 'function.'"
# print build_quiz_question(quizes["easy"]["prompt_header"], test, "words are here, they're a question?", 1)
# print reformat_max_line_length(test, 60)
# print reformat_max_line_length(quizes["easy"]["prompt_header"], 60)
# print "\n\nAll ____1____s follow in a specific format: def\n____1_____name(argument1, argument2,...). One ____1____ can\npass its results using the ____2____ command, where the\nformat is ____2____ value. As a rule you want a ____1____\nto have ____3____ purpose; additional purposes are ideally\nmoved into another ____1____. This helps reduce ____4____\nand prevent bugs. It also promotes readability.\n\n\nYou've reached the maximum number of attempts.\nThe desired answer was 'function.'\n\nwords are here, they're a question? ____2____?  "