# Created by shailakshigupta at 6/1/25
Feature: Test scenarios for target website
  # Enter feature description here

  Scenario: User can view the  cart
    Given Open target.com
    When Click account drop-down
    And Click sign in or create account
    Then "Enter your email or mobile number to continue" message is shown

