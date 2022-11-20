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