@fixture.web
Feature: Logowanie

    Background:
        Given strona wi zut jest otwarta
    @sanity
    Scenario Outline: logowanie zlymi danymi
        When uzytkownik kliknie przycisk logowania
        Then uzytkownik widzi strone logowania
        When uzytkownik wpisze login "<login>"
        And uzytkownik wpisze haslo "<haslo>"
        And uzytkownik kliknie przycisk "Zaloguj"
        Then zostaje wyswietlony komunikat o bledzie "Nieprawidłowa nazwa użytkownika lub hasło albo nie masz u nas jeszcze konta"

        Examples: bledne_dane
            | login      | haslo              |
            | test       | test               |
            | nrindeksu_3| qwertyuiop         |
            | ze spacja  | haslobezspacji     |
