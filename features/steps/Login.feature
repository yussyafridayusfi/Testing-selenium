Feature: psegameshop login

    How to login psegameshop

    Scenario: login with valid account
    Given I open the login page
    When I enter valid email
    And I enter valid password
    And I click login button
    Then Successfully login