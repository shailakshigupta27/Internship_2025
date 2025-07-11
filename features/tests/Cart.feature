# Created by shailakshigupta at 6/15/25
Feature: Test for Cart functionality
  # Enter feature description here

  Scenario: User can view the  cart
    Given Open target.com
    When Click on cart icon
    Then “Your cart is empty” message is shown
    Then Verify Cart page opened


  Scenario: User can add product to cart
    Given Open target.com
    When Input Cup into search field
    And Click on Add to Cart
    And Again Click on Add to Cart in side navigation
    And Click view cart
    Then Verify number of items in the cart is 1 item