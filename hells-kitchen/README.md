# Hell's Kitchen
Welcome to Hell's Kitchen, our third and final event of Hack Kitchen! You will be tasked with solving 3 fast paced puzzles, each in a different programming language. Solve them before  time runs out to earn as many points as possible! 

## Appetizer: C++
Quick! You're given a list (array) of ingredients which you will use to cook up an appetizer, but something seems to be off with the list. Some of the ingredients have random characters in them, but they refer to the same ingredient (ex. "sliders" and "s1l&iD e2rS" refer to the same ingredient)! In order to properly get the ingredients, you need to know how many unique ingredients there are on the list. 

### Your Task
Open the file *getUniqueIngredients.h* and implement the function *_getUniqueIngredients()_*, that, given an array of ingredients and the size of the array as input, will return the number of unique ingredients in the list, ignoring digits, symbols, case, and spaces. 

Feel free to write/use any helper functions!
However, you may only import external functions from the C-standard library.

**Submission:** your edited *getUniqueIngredients.h* file with the function as described along with any necessary helper functions.

**Ex.** [ch.ick.en wi.n.g.s, onion@rings000, chickenwings, oNioNriNgs] → 2

**Ex.** [cheese, cheEse, CHEESE, cheese0, \_cheese\_, c-h-e-e-s-e, c0h0e0e0s0e, c      heese0] → 1

### Running Your Program
After making sure your work is saved, within the hells-kitchen folder, run the following command which will compile the source file:
```shell
g++ -o [PROGRAM-NAME] testGetUniqueIngredients.cpp
```
Make sure to add your own test cases to testGetUniqueIngredients.cpp to test your code!
Then, run the program with the following command, and the number of test cases passed will be printed out!
```shell
./[PROGRAM-NAME]
```
If you have a Windows device, you can either run the code in Microsoft Visual Studio (different from VS Code) or run it in an online C++ compiler ([Online C++ Compiler](https://www.onlinegdb.com/online_c++_compiler)).

## Main Course: Pancake Stack!
### Your Task
For this problem all you need to do is print "pie" to the terminal. Sounds simple enough, right? You'll need to use "Pancake Stack," a stack based, Turing complete, programming language created in 2013 to write your program. 

### Running Your Program
Ensure that you're working within the hells-kitchen folder. Once you have written your Pancake Stack code, open your terminal and run the following command (and replace [FILE NAME] with the name of the file that contains your code):
```shell
python3 pancake_stack.py [FILE NAME]
```

You're not expected to know how to code using Pancake Stack. Part of the fun here is learning how! For reference, check out the [wiki page](https://esolangs.org/wiki/Pancake_Stack#:~:text=Pancake%20Stack%20is%20a%20stack,manipulate%20a%20stack%20of%20pancakes).

Note that Pancake Stack requires Python to be installed, so make sure you get that done before starting!


Example Program: 
```
Put this old pancake on top!
[CAT]
Eat the pancake on top!
How about a hotcake?
Show me a pancake!
If the pancake is tasty, go over to "CAT".
Eat all of the pancakes!
```

The above program will take user input and output whatever they input. 

<details>
    <summary><b>Hint</b></summary>
    <p>If you're stuck, you should definitely check out the wiki page. They have an example showing printing there. 
    In particular, note that the pancake stack program below will output "H": </p>
    <pre>
    Put this heavenly pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put another pancake on top!
    Put syrup on the pancakes!
    Put the top pancakes together!
    Put the top pancakes together!
    Put the top pancakes together!
    Put the top pancakes together!
    Put the top pancakes together!
    Put the top pancakes together!
    Put the top pancakes together!
    Show me a pancake!
    Eat all of the pancakes!
    </pre>
    <p>Understanding what is going on here will be very helpful in trying to print "pie"! </p>
    <p>Additionally, you should consider looking into <a href="https://www.ascii-code.com/">ASCII character codes</a> and the <a href="https://www.geeksforgeeks.org/stack-data-structure/">stack data structure</a>. </p>
    
</details>


## Dessert: Python!
Gordon Ramsay is tasking you with buying ingredients for his dessert service. He's a busy man, so he has no time to actually go shop with you. Therefore, he's given you a list of ingredients and his credit card. Of course, there's a budget.
His ingredient list looks like this:
```
[[ingredient, cost, minimum_required], [ingredient, cost, minimum_required], ... ]
```
However, he doesn't expect you to be able to get all the ingredients in his list. He's given you a minimum count required per ingredient, in hopes of you actually getting him the ingredients he needs. You need to prioritize which ingredients you obtain in this way:
- Purchase as many distinct ingredients as possible
- Then, prioritize ingredients that can have their *minimum_required* requirement met
- In cases where *minimum_required* cannot be met, minimize the amount of money used

Return a list of items *[ingredient, quantity]* that Gordon should purchase in any order. If no ingredients can be purchased, return [ ].

This task is explained again in the *get_gordons_ingredients.py* file with examples.

### Your Task
Open the *get_gordons_ingredients.py* file and implement the method *get_ingredients()* to the best of your ability! Don't worry if you can't meet all 3 of the requirements, Gordon will give you credit for any attempt! He wants you to purchase as many distinct ingredients as possible first before moving on to the other requirements! Good luck!

### Running Your Program
Ensure that you are working within the hells-kitchen folder. Within a terminal, run the following code:
```shell
python3 ./get_gordons_ingredients.py
```

To test your implementation, you can change the *ingredients* and *budget* variables in line 58 and 59 within the file. 
Note that this problem requires python to be installed, so make sure you get that done before starting!

### Python Help
- Download Python: [download](https://www.python.org/downloads/)
- Python Docs: [docs](https://docs.python.org/3/)
- Python Cheatsheet: [geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/)