Feature: Login functionality
  Scenario: Successful Login With Valid Credentials
    Given user is on the login page
    When user enters valid username and password
    And user clicks on login button
    Then user should navigated to the product page


  Scenario: Invalid login [invalid creadentials]
    Given user is on the login page
    When user enters invalid creadentials
    And user clicks on login button
    Then user should show error