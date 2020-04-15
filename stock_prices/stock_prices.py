#!/usr/bin/python3

import argparse

def find_max_profit(prices):
  # We have to make sure that the given list has at least 2 prices to continue
  if len(prices) < 2:
    return -1

  # set three variables
  # set the first index of the first item of the list to the minimum price thus far
  # if the number after is greater than it becomes the max price so far; if less, then we move on to the next element and compare

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))