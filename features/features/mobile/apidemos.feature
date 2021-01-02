@fixture.mobile
Feature: Open app

    @pass
    Scenario: app is opened

        Given I am on wi zut page
        Then I see wi zut title "Wydział Informatyki"
#    @fail
#    Scenario: Page is accessible and displayed
#
#        Given I am on wi zut page
#        Then I see wi zut title "Wydział Informatykii"