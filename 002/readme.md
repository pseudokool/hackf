[1] Ugly Numbers
posted Jul 16, 2015, 4:15 AM by Carlyle Oliver   [ updated Jul 16, 2015, 4:50 AM ]
A number is called ugly, if it was divisible by any of the one-digit primes (2, 3, 5 or 7). 

Thus, 14 is ugly, but 13 is fine. 39 is ugly, but 121 is not. Note that 0 is ugly. Also note that negative numbers can also be ugly: -14 and -39 are examples of such numbers.



INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will be a single line containing a non-empty string of decimal digits. The string in each test case will be non-empty and will contain only characters '0' through '9'. Each string is no more than 13 characters long. E.g.

1
9
011
12345
OUTPUT SAMPLE:

Print out the number of expressions that evaluate to an ugly number for each test case, each one on a new line. E.g.

0
1
6
64


[2] Reverse And Add
posted Jul 16, 2015, 4:16 AM by Carlyle Oliver   [ updated Jul 16, 2015, 4:51 AM ]
Choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.

For example:

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)
In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10,000. Assume each test case will always have an answer and that it is computable with less than 100 iterations (additions).

OUTPUT SAMPLE:

For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character).

For example:

4 9339


[3] Closest To Zero
posted Jul 16, 2015, 4:49 AM by Carlyle Oliver   [ updated Jul 16, 2015, 11:55 PM ]
Given a random array of integers, both positive and negative, find the pair with sum closest to zero. For instance, in the array [45, -29, -96, -7, -17, 72, -60], the two integers with sum closest to zero are -60 and 72.

Your task is to write a program that finds the two-sum closest to zero. When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or discuss the exercise in the comments below.


[4] Eye-Oh
posted Jul 16, 2015, 5:00 AM by Carlyle Oliver   [ updated Jul 16, 2015, 5:05 AM ]
Part One: Weather Data
In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).



Part Two: Soccer League Table
The file football.dat contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.



Part Three: DRY Fusion
Take the two programs written previously and factor out as much common code as possible, leaving you with two smaller programs and some kind of shared functionality.


