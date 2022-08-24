Book Store: to execute the tests with default url write "python -m pytest test_b.py"
To execute the test with your url write : python -m pytest test_b.py --url "<your-url>"

Pet Shop : to execute the tests with default url write "python -m pytest test_p.py"
To execute the test with your url write : python -m pytest test_p.py --url "<your-url>"

Some of the test fail because of a bug in the swagger, but most pass


To run allure report write: python -m pytest --alluredir="<yourlocation>" <testname>
Than write on the cmd : allure serve <yourlocation>

Book Store Test Report:

<img width="800" alt="screenshot test_b" src="https://user-images.githubusercontent.com/97604250/186412660-4aa0c345-af39-4701-a837-944a0cc87725.png">


Pet Store Test Report:

<img width="798" alt="screenshot test_p" src="https://user-images.githubusercontent.com/97604250/186412769-8d16f558-0141-4e9a-9c05-409a9ed6e181.png">


