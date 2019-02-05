Feature: Testing is_this_a_triangle() function

  Scenario: Is this a triangle?
    Given I have three possible sides of a triangle and its expected validity
        | a | b | c | result |
        | 5 | 6 | 7 | True   |
        | 4 | 8 | 2 | False  |
    When I check whether a triangle can be formed
    Then The result should reflect triangle validity
