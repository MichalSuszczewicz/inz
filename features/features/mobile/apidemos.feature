@fixture.mobile
Feature: Open app

    @pass
    Scenario: app is opened and interactive

        Given App is opened
        Then I see app title "API Demos"
        And I can navigate through the app
#    @fail
#    Scenario: Page is accessible and displayed
#
#        Given I am on wi zut page
#        Then I see wi zut title "Wydział Informatykii"