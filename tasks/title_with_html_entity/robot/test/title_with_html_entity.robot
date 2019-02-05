*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
Verify Title with HTML Entity
    Open Browser    http://www.wordpress.org    firefox
    Title Should Be    Blog Tool, Publishing Platform, and CMS — WordPress
    Close Browser