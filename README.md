# selenium-language-v1
Task: running autotests for different interface languages

We want the online store, we are developing, to work equally well for users from any country.
To ensure that the solution works with support for different languages, we plan to run a set of autotests for each language. 
As an autotest developer, you need to implement a solution that will allow you to run autotests for different user languages ​​by passing the desired language on the command line.

1) Create a GitHub repository that will contain the conftest.py and test_items.py files.
2) Add a handler to the conftest.py file that reads the language parameter from the command line.
3) In the conftest.py file, implement the logic for launching a browser with the specified user language.
   The browser must be declared in the "browser" fixture and passed to the test as a parameter.
4) In the test_items.py file, write a test that checks that the product page on the site contains an "add to cart" button.
   For example, you can check a product available at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5) The test should be run with the language parameter using the following command: pytest --language=es test_items.py
and pass successfully. It is enough that the code works only for the Chrome browser.
