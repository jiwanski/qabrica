Feature: Testing multiples_of_3_or_5() function

  Scenario Outline: Multiples of 3 or 5
    Given I have a positive "<integer>"
    When I find sum of all multiples of 3 or 5 below "<integer>"
    Then The result should be equal to "<sum>"

    Examples:
      | integer | sum |
      | 10      | 23  |
      | 20      | 78  |
