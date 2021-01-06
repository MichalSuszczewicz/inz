@fixture.web
Feature: Open page

    @smoke
    Scenario: Page is accessible and displayed

        Given I am on wi zut home page
        Then I see wi zut title "Wydział Informatyki"
    @sanity @smoke
    Scenario: Page is accessible and displayed

        Given I am on wi zut home page
        Then I see wi zut title "Wydział Informatykii"