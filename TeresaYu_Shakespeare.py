#Module 7 Shakespeare Assignment
#Teresa Yu
#This program counts the number of times the word "thou" appears in each of the above files and print the number out to the screen and creates a new file called dave.txt then finds all the instances of the word "Macbeth" and replaces it with the word "Dave"

#defining a function that counts how many instances of 'thou' are in the text, aka the parameter shakespeare.
def manyThou(shakespeare):
  #reading the play and saving the text into a variable.
  text = shakespeare.read()
  #counting how many times thou is in the text, counting the word with an uppercase, lowercase and/or punctuation.
  lowercaseThou = text.count("thou ")
  uppercaseThou = text.count("Thou ")
  puncThou = text.count("thou!") + text.count("thou,") + text.count("thou.") + text.count("Thou!") + text.count("Thou,")
  #adding the instances together to return the number of times 'thou' is correctly found
  count = lowercaseThou+uppercaseThou+puncThou
  return count

#opening (in read mode) and closing each text file and printing the final amount to the console.
with open('Hamlet.txt', 'r') as ham:
  print('The word \'thou\' appears in Hamlet', manyThou(ham), 'times.')
with open('macbeth.txt', 'r') as mac:
  print('The word \'thou\' appears in Macbeth', manyThou(mac), 'times.')
with open('othello.txt', 'r') as oth:
  print('The word \'thou\' appears in Othello', manyThou(oth), 'times.')
with open('romeoandjuliet.txt', 'r') as rAndj:
  print('The word \'thou\' appears in Romeo and Juliet', manyThou(rAndj), 'times.')

#opening and closing the Macbeth file again to read and extract the text. After, we use the .replace() method to find instances of "MACBETH" in all caps or "Macbeth" to replace with "Dave". 
#did not find 'macbeth' with all lowercase since we know it is improper grammar for a pronoun
with open('macbeth.txt', 'r') as data:
  macbethText = data.read()
  daveText = macbethText.replace("Macbeth", "Dave")
  daveText = daveText.replace("MACBETH", "DAVE")

#creating a text file called 'dave.txt' to write our new Dave-Macbeth play
with open("dave.txt", "w") as dave:
  dave.write(daveText)


  

