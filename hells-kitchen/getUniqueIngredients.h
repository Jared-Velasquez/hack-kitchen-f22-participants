#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int getUniqueIngredients(string ingredients[], int size) {
    unordered_set <string> myset;
    for (int i = 0; i < size; i++) {
        string clean = "";
        for (int j = 0; j < ingredients[i].size(); j++) {
            char curr = ingredients[i][j];
            if (curr >= 'A' && curr <= 'Z') {
                curr += 32;
            }
            
            // after this point curr is correctly lowercase
            //  and the whole string is correct after this point 
            
            if (curr >= 'a' && curr <= 'z') {
                clean += curr;
            }
        }
        myset.insert(clean);
    }
    return myset.size();
}