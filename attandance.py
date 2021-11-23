## Question
# In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
# You are not allowed to miss classes for four or more consecutive days. 
# Your graduation ceremony is on the last day of the academic year, which is the Nth day.

# Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
# Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

from itertools import product

class attend_checker:
    no_of_ways = 0
    probability_miss = 0

    # find_repeating_permutation
    # custom function to generate all the permutation
    # arguments: str => string Absent and present (0 or 1)
    # pattern => prefix pattern generated in last recursion
    # len_n => lenth of str, n => length of pattern
    # permutation_list => to store pattern

    def find_repeating_permutation(self, str, pattern, len_str, n, permutation_list):
        if n == 0: 
            permutation_list.append(pattern)
            return

        for i in range(len_str):
            temp = pattern + str[i] 
            self.find_repeating_permutation(str, temp, len_str, n-1, permutation_list)

    # main function
    # argument: no_days => user input
    # it calculate all the combination and calculate probability wheter student will able to attend graduation ceremony.
    # To find all the combination product function is used 
    # 0 represent miss classes and 1 represent attended class
    # If student miss class for four or more days he will be not able to attend the ceremony

    def main(self, no_days):
        permutation_list = []
        self.find_repeating_permutation("01", "", 2, no_days, permutation_list )
        for combination in permutation_list:
            temp = ''.join(combination)
            if temp.find('0000') == -1:
                self.no_of_ways +=1
            if temp.find('0000') == -1 and temp[-1]== '0':
                self.probability_miss += 1
    def display(self):
        print(str(self.probability_miss) + "/" + str(self.no_of_ways))

if __name__ == '__main__':
    attend_obj = attend_checker()
    n = input("Enter number of days : ")
    attend_obj.main(int(n))
    attend_obj.display()

# if __name__ == '__main__':
#     attend_obj = attend_checker()
#     attend_obj.main(5)
#     attend_obj.display()

#     attend_obj_new = attend_checker()
#     attend_obj_new.main(10)
#     attend_obj_new.display()
