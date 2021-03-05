
 @fixture.web
 Feature: header is visible

    Background:
        Given wi zut webpage is opened

    Scenario: header is displayed properly
        When user check header
        Then user see title "Wydział Informatyki"




