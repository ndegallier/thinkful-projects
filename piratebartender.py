# Pirate Bartender Project

import random

# create yes/no question function
def yes_no(question):
	reply = str(raw_input(question + ' (y/n): '))
	if reply[0] == 'y': 
		return True
	elif reply[0] == 'n':
		return False
	elif reply[0] != 'y' or reply[0] != 'n':
		return yes_no("Ye must enter 'y' or 'n', ye foolish pirate")


# create dictionary of questions and ingredients
questions = {
	"angry": "Want it angry?",
	"forgiving": "Do ye like yer drink to forgive ye?",
	"easy": "Do ye like yer drink to go down easy?",
	"sugary": "Should yer drink be sugary?",
}

ingredients = {
	"angry": ["Blackbeard's rum", "pint of gin", "quart of whisky"],
	"forgiving": ["mermaid's ale", "hard lemonade", "hard cider"],
	"easy": ["water", "ice cold", "straight"],
	"sugary": ["sprite", "apple juice", "no fun"],
}

# start the program by inquiring for the user's name
name = raw_input("Argh matey, what be yer name? ")
print "Great {}, I'' be making yer drink this evenin'.".format(name)

# create empty dictionary for answers
answers = {}

# function for questions 
def inquiry(dictionary):
	for key in dictionary:
		if yes_no(dictionary[key]) == True:
			answers.update({key: True})
		
# function to list size and ingredients
def blender(dictionary):
	contents = []
	for key in dictionary:
		if dictionary[key] == True:
			contents.append(random.choice(ingredients[key]))
	print contents
			

if __name__ == '__main__':
	inquiry(questions)
	blender(answers)
