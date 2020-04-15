#!/usr/bin/python3

import argparse

def find_max_profit(prices):
  # We have to make sure that the given list has at least 2 prices to continue
  if len(prices) < 2:
    return -1

  # set three variables
  # set the first index of the first item of the list to the minimum price thus far
  # if the number after is greater than it becomes the max price so far; if less, then we move on to the next element and compare

  max_price_index = 0
  min_price_now = prices[0]
  max_price_now = 0

  # finding the ma price
  # we will start with the 2nd element
  for i in range(1, len(prices) - 1):
    if prices[i] > max_price_now:
      max_price_now = prices[i]
      max_price_index = i
  
  # find min price that exists before max price in the list
  for i in range(0, max_price_index):
    if prices[i] < min_price_now:
      min_price_now = prices[i]

  # return the profit margin (max - min)
  max_profit = max_price_now - min_price_now
  
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))