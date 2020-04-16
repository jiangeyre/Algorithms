#!/usr/bin/python3

import math

def recipe_batches(recipe, ingredients):
  # initialize batch amount = 0 and get list of keys for ingredients of recipe
  batches = 0
  ing_keys = list(recipe.keys())


  # iterate through recipe and ingredients
  for i in range(len(ing_keys)):
    rec_quantity = recipe.get(ing_keys[i])
    ing_quantity = ingredients.get(ing_keys[i])

    # if no ingredient, set it 0
    if ing_quantity == None:
      ing_quantity = 0

    # Check if there are more of an ingredient than what the recipe requires; if so, divide the ingredient quantity by recipe quantity to find possible amount of batches for given ingredient
    if rec_quantity <= ing_quantity:
      amount = ing_quantity // rec_quantity
      # Set amount of batches for first
      if i == 0:
        batches = amount
      # If the amount is smaller than previous, set possible batches to lowest
      elif amount < batches:
        batches = amount
    else:
      batches = 0

  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))