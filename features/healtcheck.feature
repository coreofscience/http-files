Feature: Health check

  Health check is a simple endpoint that allows us to check that the
  application is running correctly.

  Scenario: Healty service

    Given our service is running correctly
    When we get the ping endpoint
    Then we get a ping response
