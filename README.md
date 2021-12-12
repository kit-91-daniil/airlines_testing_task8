Implementation Test Automation Framework to testing RyanAir compaty website

# 1) Clone repository: 

$ clone https://github.com/kit-91-daniil/airlines_testing_task8.git

# 2) From the command line in the project's root directory run: 

$ pipenv install

# 3) For launch tests use commands:

# Flights search:
$ python -m pytest -k flight_search --alluredir=allure_reports/

# Car hire:
$ python -m pytest -k car_hire --alluredir=allure_reports/

# Search hotel
$ python -m pytest -k hotels_search --alluredir=allure_reports/

# Cheap flights search
$ python -m pytest -k cheap_flights_search --alluredir=allure_reports/

# Transfer search
$ python -m pytest -k transfer_search --alluredir=allure_reports/

# OR for launch all the tests
$ python -m pytest -v --alluredir=allure_reports/

# To open allure reports use command below:
$ allure serve allure_reports/