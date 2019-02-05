# assignment

Implement steps for BDD/Gherkin feature with data table, which tests solution to following problem.

## problem

A triangle is valid if sum of any of its two sides is greater than the third side. See also https://www.codewars.com/kata/is-this-a-triangle

5, 6, 7 are valid triangle sides, because:

* 5 + 6 > 7
* 6 + 7 > 5
* 5 + 7 > 6

## source

Python function in `src/is_this_a_triangle.py`.

## sample feature with data table

```gherkin
Feature: Testing is_this_a_triangle() function

  Scenario: Is this a triangle?
    Given I have three possible sides of a triangle and its expected validity
        | a | b | c | result |
        | 5 | 6 | 7 | True   |
        | 4 | 8 | 2 | False  |
    When I check whether a triangle can be formed
    Then The result should reflect triangle validity
```

> Note that not every BDD implementation supports data tables. For example, Robot Framework doesn't.
