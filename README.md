# python-journey
I started learning Python on September 2021. This repository contains everything I've been learning every week since then.
I already had a background in programming, which really helped me understand the core concepts of a new programming language.
Materials I used to learn were the FreeCodeCamp Youtube channel, the book Automating The Boring Stuff with Python (AtBSwP) and, of course, lots and lots of documentation reading.
I'll try to update this repo every day so I could see the exponential progress I make and I hope one day the repo becomes a reference material for those who, as I am now, might start learning Python.

English is not my first language and I'm still in the process of learning it. If this readme has any grammatical errors, feel free to correct me.

Now, I'll briefly explain what each program does :)

### Week 1
First week was all about syntax and understanding of general concepts. 

[Rock, Paper, Scissors](Week%201/RockPaperScissors.py) was my very first project in Python. First of all, the program prompts the user to choose a 'weapon' (rock, paper or scissor).
Later, using the random module, the program chooses a number from 0 to 2 (inclusive) to use it as the index of an array of three items.
Each one of these three items represents one 'weapon'. After that, the program compares the two choices within a set of if statements until it reaches a conclusion and
announces the winner.

[ZigZag](Week%201/ZigZag.py) is a super simple program that I made with the help of the book I mentioned earlier. It basically displays a zig zag on the command line until the user interrrupts the process.

[List Exercise](Week%201/listExercise.py) was one of the exercises AtBSwP presented me after learning about dictionaries. We have an 'initial inventory' (a dictionary that displays
the items we have and the amount of each) and a 'dragon loot' (a list of items, some of them repeated). 
We basically have to insert the items of the loot inside our inventory by counting the amount of items and repeated items we have inside the loot so we can know the total amount
of items we have after the 'looting'. First I created a function that takes a dictionary as an argument and then I iterate over that dictionary to count the amount of items we have inside it.
I also created another function that takes a dictionary and a list as arguments. With the help of the Collections module and with the Counter class I counted the amount of items and repeated items inside the list (the loot)
and then I 'appended' these values to the dictionary with a for loop. Finally the program displays the total amount of items inside our updated inventory.

[Occurrence of Character](Week%201/occurrenceOfChar.py) is a program that counts the amount of times a character appears in a given text. We have a function that takes a string as
an argument. The program iterates over the string with the help of a for loop and appends each charactes and its occurrence inside a dictionary. 
Then the program iterates over said dictionary and, using a set of conditionals, checks which character has the bigger value (the value is a number that shows the occurrence of the character).
If there was only one character that was the most repeated, the program returns a string with the result and if there were two or more characters that appeared the same amount
of times in the text then we append them all to a list.
The program also has a nice error handling feature that consists on checking the data type of the value passed as the argument to the function. The program runs if the value is a string
and if it's not it asks the user to enter one.

[Reverse Data](Week%201/reverseData.py) is a program that started as one that reverses a string and then evolved to one that reverses not only strings but also lists and tuples.
The program has like four versions, each of them is an improvement of the previous one. I'm not gonna explain every version (check it out, the code have comments that explain it all!)
but my general approach was to convert the string passed as an argument to a list, reverse the list using a for loop and .insert(), and then converting the reversed list
back to a string. This was a verbose approach, though. What lead me to the final, and what I think is the most effective version of the code, was learning about slice notation.
In an elegant way, that solved the process previously mentioned.



















