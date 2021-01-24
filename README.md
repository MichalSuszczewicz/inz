# Web and Mobile automation framework based on Page Object with Behave

## Table of contents
* [General Info](#general-info)
* [Requirements](#Requirements)
* [Run commands](#run-commands)

## General info
This project was created for engineer thesis purposes. It allows to create tests for Web and Mobile platforms in scope of 1 project

## Requirements
* Python 3.7
* Selenium
* Appium 1.14.0
* Behave 1.2.6
* Chromedriver compatible with Browser version
* Geckodriver compatible with Browser version
* Allure 2.13.7

## Run commands

To run this project for all test and all platforms
````
$ behave
````

To run this project for all web tests on default browser (Google Chrome)
````
$ behave --tags=fixture.web
````

To run this project for all web tests on Google Chrome
````
$ behave --tags=fixture.web -D profile=chrome
````

To run this project for all web tests on Mozilla Firefox
````
$ behave --tags=fixture.web -D profile=firefox
````

To run this project for all mobile tests on default mobile device (Android)
````
$ behave --tags=fixture.mobile
````

To run this project for all mobile tests on Android device
````
$ behave --tags=fixture.mobile -D profile=android
````

To run this project for all mobile tests on iOS device
````
$ behave --tags=fixture.mobile -D profile=ios
````

To run this project for selected platform and profile, but only with specific tests sets, combine above commands with tag parameter, that represents desired test set, for example:

````
--tags=smoke
````

````
$ behave --tags=fixture.web -D profile=firefox --tags=smoke
````

To run this project with allure report format use command:

````
$ behafe -f allure_behave.formatter:AllureFormatter -o allure/results ./features
````

To generate report after test execution run:

````
$ allure generate allure/results/ -o allure/reports/ --clean
````