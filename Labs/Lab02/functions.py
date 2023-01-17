#!/usr/bin/env python3
import random
from typing import Iterable, Set


##### Python Reminder

# Fix

def fix_me(numbers: Iterable[int]) -> Iterable[int]:
    # Return all the even numbers in the parameter numbers.
    results = []
    for num in numbers:
        if num % 2 == 0:
            results.append(num)
    return results


#
#
def fix_me_too(numbers: Iterable[int], threshold: int) -> int:
    """
    The function takes an iterable of integers and a threshold.
    The function returns the number of values in numbers that are above the given threshold.
    """
    counter = 0
    for n in numbers:
        if n > threshold:
            counter += 1
    return counter




def get_shared_items(sets: Iterable[Set[int]]) -> Set[int]:
    result = sets[0]
    for i in sets:
        result = result&i
    return result



def get_randoms(divby: int) -> int:
    """
    Return a random number ranged betwee 1 and 1000 that is divisable by divby.
    Generate numbers using np.random.randint until you get such a number.
    """
    x = 0
    while(True):
        x   = random.randint(1,1000)
        if x % divby == 0:
            return x;

        


# def inner_product_r(v1: Iterable[float], v2: Iterable[float]) -> float:
#
#
# def inner_product_c(c1: Iterable[complex], c2: Iterable[complex]) -> complex:


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lstTeam = [{1,2,3},{2,3,4},{3,4,5,2}]
   # print(fix_me(lst))
   # print(fix_me_too(lst, 4))
   #  print(get_shared_items(lstTeam))

