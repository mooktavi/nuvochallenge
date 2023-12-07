**Feature: User Account Creation**

  Scenario: Register user with happy path
    Given the registration form is loaded
    When the user enters "John" as the First Name
    And the user enters "Doe" as the Last Name
    And the user enters "01/01/1990" as the Date of Birth
    And the user enters "john.doe@example.com" as the Email
    And the user enters "john.doe@example.com" as the Repeat Email
    And the user enters "P@ssword1" as the Password
    And the user checks the Terms and conditions checkbox
    And the user clicks on the "Register" button
    Then the user should be redirected to the activation instruction page
    And the user should receive an activation email with a link
  
  Scenario: Register with existing email
    Given the registration form is loaded
    And an existing account with email "jane.doe@example.com" is present
    When the user enters "Jane" as the First Name
    And the user enters "Doe" as the Last Name
    And the user enters "02/02/1992" as the Date of Birth
    And the user enters "jane.doe@example.com" as the Email
    And the user enters "jane.doe@example.com" as the Repeat Email
    And the user enters "P@ssw0rd!" as the Password
    And the user checks the Terms and conditions checkbox
    And the user clicks on the "Register" button
    Then the user should be redirected to the login page
    And a message "There is an existing account associated with jane.doe@example.com" is displayed

  Scenario: Register with invalid email format
    Given the registration form is loaded
    When the user enters "New" as the First Name
    And the user enters "User" as the Last Name
    And the user enters "01/01/1995" as the Date of Birth
    And the user enters "invalidemail" as the Email
    And the user enters "invalidemail" as the Repeat Email
    And the user enters "password" as the Password
    And the user checks the Terms and conditions checkbox
    And the user clicks on the "Register" button
    Then an error message "Invalid email" is displayed below the Email text box

  Scenario: Register without filling all mandatory fields
    Given the registration form is loaded
    When the user enters "" as the First Name
    And the user enters "Incomplete" as the Last Name
    And the user enters "" as the Date of Birth
    And the user enters "user@example.com" as the Email
    And the user enters "user@example.com" as the Repeat Email
    And the user enters "P@ssword2" as the Password
    And the user checks the Terms and conditions checkbox
    And the user clicks on the "Register" button
    Then an error message "Please fill in this First Name" is displayed below the First Name text box
    And an error message "Please fill in this Date of Birth" is displayed below the Date of Birth text box

  Scenario: Register with future date of birth
    Given the registration form is loaded
    When the user enters "Futuristic" as the First Name
    And the user enters "User" as the Last Name
    And the user enters a date of birth that is in the future
    And the user enters "future.user@example.com" as the Email
    And the user enters "future.user@example.com" as the Repeat Email
    And the user enters "MyP@ssw0rd" as the Password
    And the user checks the Terms and conditions checkbox
    And the user clicks on the "Register" button
    Then an error message "Selected date exceeds the current date" is displayed

  Scenario: Account activation from same browser
    Given the user has completed the registration form
    And the user has received the activation email
    When the user clicks on the activation link from the same browser
    Then the user is automatically logged in the system

  Scenario: Account activation from different browser
    Given the user has completed the registration form
    And the user has received the activation email
    When the user clicks on the activation link from a different browser
    Then the user is redirected to the login page
    And a welcome message is displayed
    And the email address is pre-populated in the email field