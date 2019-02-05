# how to run

Open terminal in **multiples_of_3_or_5** directory and execute:

```
behave python_behave/features/multiples_of_3_or_5.feature
```

## sample output

```shell
Feature: Testing multiples_of_3_or_5() function # python_behave/features/multiples_of_3_or_5.feature:1

  Scenario Outline: Multiples of 3 or 5 -- @1.1                     # python_behave/features/multiples_of_3_or_5.feature:10
    Given I have a positive "10"                                    # python_behave/features/steps/multiples_of_3_or_5.py:6 0.000s
    When I find sum of all multiples of 3 or 5 below "10"           # python_behave/features/steps/multiples_of_3_or_5.py:12 0.000s
    Then The result should be equal to "23"                         # python_behave/features/steps/multiples_of_3_or_5.py:18 0.000s

  Scenario Outline: Multiples of 3 or 5 -- @1.2                     # python_behave/features/multiples_of_3_or_5.feature:11
    Given I have a positive "20"                                    # python_behave/features/steps/multiples_of_3_or_5.py:6 0.000s
    When I find sum of all multiples of 3 or 5 below "20"           # python_behave/features/steps/multiples_of_3_or_5.py:12 0.000s
    Then The result should be equal to "78"                         # python_behave/features/steps/multiples_of_3_or_5.py:18 0.000s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s

```