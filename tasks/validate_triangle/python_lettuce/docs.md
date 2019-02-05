# how to run

Open terminal in **validate_triangle** directory and execute:

```
lettuce python_lettuce/features/is_this_a_triangle.feature
```

## sample output

```shell
Feature: Testing is_this_a_triangle() function                                # python_lettuce/features/is_this_a_triangle.feature:1

  Scenario: Is this a triangle?                                               # python_lettuce/features/is_this_a_triangle.feature:3
    Given I have three possible sides of a triangle and its expected validity #     Given I have three possible sides of a triangle and its expected validity # python_lettuce/features/steps/is_this_a_triangle.py:6
      | a | b | c | result |
      | 5 | 6 | 7 | True   |
      | 4 | 8 | 2 | False  |
    When I check whether a triangle can be formed                             #     When I check whether a triangle can be formed                             # python_lettuce/features/steps/is_this_a_triangle.py:11
    Then The result should reflect triangle validity                          #     Then The result should reflect triangle validity                          # python_lettuce/features/steps/is_this_a_triangle.py:23

1 feature (1 passed)
1 scenario (1 passed)
3 steps (3 passed)
```