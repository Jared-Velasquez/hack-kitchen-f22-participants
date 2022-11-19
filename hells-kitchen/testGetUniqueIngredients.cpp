#include "getUniqueIngredients.h"
#include <iostream>
using namespace std;

int main() {
    // add your own test cases here!
    string ingredients1[] = {"egg", "tomato", "cheese", "bread", "jam"};
    string ingredients2[] = {"eggs", "egg54s", "s0ou#@p", "\\,89s"};
    string ingredients3[] = {"ch.ick.en wi.n.g.s", "onion@rings000", "chickenwings", "oNioNriNgs"};
    string ingredients4[] = {"cheese", "cheEse", "CHEESE", "cheese0", "\\_cheese\\_", "c-h-e-e-s-e", "c0h0e0e0s0e", "c      heese0"};
    if(getUniqueIngredients(ingredients1, 5) == 5) {
        cout << "Passed test case! 1" << endl;
    } else {
        cout << "Failed test case :(" << endl;
    }
    if(getUniqueIngredients(ingredients2, 4) == 3){
        cout << "Passed test case! 2" << endl;
    } else {
        cout << "Failed test case :(" << endl;
    }
    if(getUniqueIngredients(ingredients3, 4) == 2){
        cout << "Passed test case! 3" << endl;
    } else {
        cout << "Failed test case :(" << endl;
    }
    if(getUniqueIngredients(ingredients4, 8) == 1){
        cout << "Passed test case! 4" << endl;
    } else {
        cout << "Failed test case :(" << endl;
    }
}