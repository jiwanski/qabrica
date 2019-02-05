*** Settings ***
Library    ../../src/multiples_of_3_or_5.py


*** Test Cases ***
Scenario: Testing multiples_of_3_or_5
    [Template]  Scenario Outline: multiples of 3 or 5

    # Examples:
    # integer  sum
    10       23
    20       78


*** Keywords ***
Scenario Outline: multiples of 3 or 5
    [Arguments]  ${integer}  ${sum}
    Given I have a positive ${integer}
    When I find sum of all multiples of 3 or 5 below ${integer}
    Then The result should be equal to ${sum}


# steps implementation
I have a positive ${x}
    Should Be True     ${x} > 0


I find sum of all multiples of 3 or 5 below ${x}
    ${number}=  Convert To Integer	${x}
    ${result}=  solution  ${number}
    Set Test Variable  ${result}


The result should be equal to ${sum}
    Should Be Equal As Integers  ${result}  ${sum}
