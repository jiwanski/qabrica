# assignment

Implement steps for BDD/Gherkin feature with scenario outline, which tests solution to the following problem.

## problem

Function multiples_of_3_or_5() returns sum of multiples of 3 or 5 below a certain number. See also https://projecteuler.net/problem=1.

Example:
multiples_of_3_or_5(10) returns 23 because below 10 there are:
* multiples of 3:  3, 6, 9
* multiple of 5: 5

Sum of (3 + 6 + 9) + 5 is 23.

## source

Python function in `src/multiples_of_3_or_5.py`.

## sample feature with scenario outline

```gherkin
Feature: Testing multiples_of_3_or_5() function

  Scenario Outline: Multiples of 3 or 5
    Given I have a positive "<integer>"
    When I find sum of all multiples of 3 or 5 below "<integer>"
    Then The result should be equal to "<sum>"

    Examples:
      | integer | sum |
      | 10      | 23  |
      | 20      | 78  |
```

> Unlike with Gherkin data tables, Robot Framework does support scenario outlines and solution is available in robot/test.
