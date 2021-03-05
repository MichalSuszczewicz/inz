
 @fixture.web
 Feature: Log-in

    Background:
        Given wi zut webpage is opened
    @sanity
    Scenario Outline: log-in with incorrect data
        When user clicks log-in button
        Then user see log-in page
        When user type login "<login>"
        And user type pass "<haslo>"
        And user click button "Zaloguj"
        Then error is displayed "Nieprawidłowa nazwa użytkownika lub hasło albo nie masz u nas jeszcze konta"

        Examples: incorrect data
            | login      | haslo              |
            | test       | test               |
            | nrindeksu_3| qwertyuiop         |
            | ze spacja  | haslobezspacji     |



