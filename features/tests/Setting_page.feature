# Created by shailakshigupta at 7/16/25
Feature: Setting page functionality
  # Enter feature description here

  Scenario:User can open change password page
    Given Open main reelly page
    #When Click sign in
    When Log in to the page
    And Click on the settings option
    And Click on the Change password option
    And Verify the right page opens
    And Add some test password to the input fields
    Then Verify the “Change password” button is available