Feature: psegameshop login

    How to login psegameshop fail version

    Scenario: login with invalid account
    Given I open the login page
    When I enter invalid email
    And I enter invalid password
    And I click login button
    Then Fail login