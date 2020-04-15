#!/usr/bin/python

import math

# should return 0 since we don't have enough butter!


recipe = {'milk': 100, 'butter': 50, 'flour': 5, "cheese": 10}
ingredients = { 'milk': 138, 'butter': 48, 'flour': 51}
# self.assertEqual(
#     recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {'milk': 1288, 'flour': 9, 'sugar': 95}), 0)
# self.assertEqual(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {'milk': 198, 'butter': 52, 'cheese': 10}),
#                  1)
# self.assertEqual(recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {'milk': 5, 'sugar': 120, 'butter': 500}), 2)
# self.assertEqual(recipe_batches({'milk': 2}, {'milk': 200}), 100)


def recipe_batches(recipe, ingredients):
    times = 9999

    for key in recipe:
        current_value = recipe[key]
        if key in ingredients:
            amount = ingredients[key]
            can_make = amount // recipe[key]
            if can_make < times:
                times = can_make
        else:
            return 0
    return times

# print(ingredients["cheese"])
print(recipe_batches({'milk': 2}, {'milk': 200}))
#
# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
