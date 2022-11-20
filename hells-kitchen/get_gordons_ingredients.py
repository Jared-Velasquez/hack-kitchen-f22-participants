""" 
Given a list of ingredients with [ingredient, cost, minimum_required] and budget
Gordon needs this program to maximize the number of distinct ingredients that he can 
    purchase before purchasing more of a single ingredient, prioritizing ingredients that
    can have their minimum_required met (or closest to meeting) within the budget.
    - In cases where minimum_required cannot be met, minimize the amount of money used.
 
Return a shopping list of ingredients with the quantity that Gordon can buy. It should be in
    the form of [[ingredient, quantity], [ingredient, quantity], ...]. 
    - The list can be returned in any order.
    - If no ingredients can be purchased, return [] (an empty list)
Constraints: 
    - All prices are non-negative. 
    - Ingredient list will contain at least 1 ingredient.
    - This is only for a dessert service, so the ingredient list will be limited to 50 distinct ingredients.
    - Gordon is rich, so the budget is limited to a generous 500000
###############################################################################
Example 1
Ingredients:    [["flour", 3.59, 2],
                ["egg", 0.99, 6],
                ["baking soda", 3.49, 1]]
Budget: 13
Return: [["flour", 2], ["egg", 2], ["baking soda", 1]]
Explanation: 
    Prioritize one of each item first. Add 1 bag of flour, 1 egg, and 1 box of baking soda. 
    This totals 8.07. 
    Next, prioritize the other bag of flour since the minimum_requirement can be reached.
    This totals 8.07 + 3.59 = 11.66
    Finally, only the eggs are left to purchase. Purchase as many eggs as possible. In this case, only 1 
    more egg can be purchased to stay under budget.
    This totals 11.66 + 0.99 = 12.65 < 13
###############################################################################
Example 2
Ingredients:    [["flour", 3.59, 2],
                ["egg", 0.99, 6],
                ["baking soda", 3.49, 1]]
Budget: 7
Return: [["baking soda", 1], ["egg", 3]]
Explanation:
    Prioritize one of each item. Add 1 egg and 1 box of baking soda. 
    This totals 4.48
    Flour cannot be added to the shopping list because it would go over budget. (4.48 + 3.59 > 7)
    Since there is 7 - 4.48 = 2.52 left, purchase 2 more eggs. 
    This totals 6.46 < 7
"""

# Dessert service starts in 30 minutes, so complete the function asap and don't disappoint Gordon!
def get_ingredients(ingredients, budget):
    # sort
    sorted_price_ingredients = sorted(ingredients, key=lambda x: x[1])
    # Write your code here
    copyBudget = budget
    clean = {}
                
    #- Purchase as many distinct ingredients as possible
    #- Then, prioritize ingredients that can have their *minimum_required* requirement met
    #- In cases where *minimum_required* cannot be met, minimize the amount of money used
    
    # pass 1. buy one of as much as you can afford
    for idx, i in enumerate(sorted_price_ingredients):
        if i[1] <= budget:
            clean[i[0]] = 1
            budget -= i[1]
            sorted_price_ingredients[idx][2] -= 1
        else:
            break
        if budget <= 0:
            break
    # pass 2. buy minimum_required for cheapest items first 
    sorted_pass2_ingredients = sorted(sorted_price_ingredients, key=lambda x: x[1]*x[2])
    for idx, i in enumerate(sorted_pass2_ingredients): 
        # buy the entire minimum
        if i[1]*i[2] <= budget:
            budget -= i[1]*i[2]
            clean[i[0]] += i[2]
            sorted_pass2_ingredients[idx][2] = 0
        else: 
            break
    # pass 3. use any remaining money to b=uy the cheapest items
    while sorted_price_ingredients[0][1] <= budget:
        clean[sorted_price_ingredients[0][0]] += 1
        budget -= i[1]

    keysQuantity = []
    for i in clean:
        quantity = clean.get(i)
        keysQuantity.append([i, quantity])
    return keysQuantity

if __name__ == '__main__':
    # Edit ingredients and budget to test your program
    ingredients = [["water", 2.99, 1]]
    ingredients1 = [["a", 3.2, 3], ["b", 6.3, 2]]
    ingredient2 = [["flour", 3.59, 2],
                ["egg", 0.99, 6],
                ["baking soda", 3.49, 1]]
    budget = 7
    print(get_ingredients(ingredient2, budget))