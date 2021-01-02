Feature: Open page

    @pass
    Scenario: Page is accessible and displayed

        Given I am on wi zut page
        Then I see wi zut title "Wydział Informatyki"
#    @fail
#    Scenario: Page is accessible and displayed
#
#        Given I am on wi zut page
#        Then I see wi zut title "Wydział Informatykii"