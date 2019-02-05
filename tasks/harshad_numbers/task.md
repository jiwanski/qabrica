# assignment

Write parameterized tests for all three methods in Harshad class.

## problem

Harshad numbers can be divided by the sum of their digits. Original task is described on https://www.codewars.com/kata/harshad-or-niven-numbers. See also https://en.wikipedia.org/wiki/Harshad_number

Example:

**36** is a Harshad number, because it is divisible by 3 + 6.
Next Harshad number is **40**.
A series of 5 Harshad numbers greater than 10 is **12, 18, 20, 21, 24**.

The above results are calculated with following methods:

- is_valid(n), checks if n is a Harshad number
- get_next(n), returns the next Harshad number > n
- get_series(n, start), returns a series of n Harshad numbers, optional start value not included

## source

Python class in `src/harshad_numbers.py`.

## sample test data

| actual | expected |
| --- | --- |
| is_valid(20) | True |
| is_valid(21) | True |
| is_valid(22) | False |
| get_next(0) | 1 |
| get_next(1) | 2 |
| get_next(17) | 18 |
| get_series(10) | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| get_series(20) | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42] |
| get_series(10, 10) | [12, 18, 20, 21, 24, 27, 30, 36, 40, 42] |
| get_series(10, 1000) | [1002, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1020] |

>  Note that get_series() has a default parameter, which I found tricky to implement in pytest, hence two separate tests for this method.
