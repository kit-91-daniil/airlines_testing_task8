Feature: flight, car, hotel search

  @flight_search
  Scenario Outline: Verify user can find tickets for flight in specified dates

    Given I am on the main page
    When I open the 'flights' tab
    And I perform search : from '<origin_airport>' to '<destination_airport>' in next dates: departure '<depart_year_month_day>', return '<return_year_month_day>' and click the 'Search' button
    Then flight page should be displayed with title containing Flights
    Then I should see flights from '<origin_airport>' to '<destination_airport>' and arrival price

    Examples:
      | origin_airport | destination_airport| depart_year_month_day | return_year_month_day |
      | Budapest-BUD   | Copenhagen-CPH     | 2021-12-14            | 2021-12-17            |
      | Berlin-BER     | Marseille-MRS      | 2021-12-14            | 2021-12-16            |
      | Prague-PRG     | Riga-RIX           | 2021-12-18            | 2021-12-22            |

  @car_hire
  Scenario Outline: Verify user can hire a car

    Given I am on the main page
    When I open the 'car hire' tab
    And I perform search : from '<pick_up_location>' in next period: from '<pick_up_year_month_day>' '<pick_up_time>' to '<drop_off_year_month_day>' '<drop_off_time>' and click the 'Let's go' button
    Then Car Hire page should be displayed with header containing 'Car Hire'

      Examples:
      | pick_up_location | pick_up_year_month_day | pick_up_time | drop_off_year_month_day | drop_off_time |
      | Budapest-BUD     | 2021-12-14             | 10:00        | 2021-12-17              | 10:00         |
      | Berlin-BER       | 2021-12-15             | 10:30        | 2021-12-16              | 10:30         |
      | Prague-PRG       | 2021-12-18             | 12:00        | 2021-12-20              | 12:00         |

  @hotels_search
  Scenario Outline: Verify user can search a hotel

    Given I am on the main page
    When I open the 'hotels' tab
    And I perform search: '<hotel>' in next period: from '<check_in_year_month_day>' to '<check_out_year_month_day>' and click the 'Search' button
    Then Rooms page should be displayed with Rooms logo
    And I should see '<hotel>' and period: from '<check_in_year_month_day>' to '<check_out_year_month_day>'

      Examples:
      | hotel                 | check_in_year_month_day| check_out_year_month_day |
      | Minsk Marriott Hotel  | 2021-12-14             | 2021-12-17               |
      | Aqua-Minsk Hotel      | 2021-12-13             | 2021-12-14               |
      | President Hotel Minsk | 2021-12-18             | 2021-12-20               |

  @cheap_flights_search
  Scenario Outline: Verify user can search cheap flight

    Given I am on the main page
    When I open Plan menu
    And click Fare Finder link
    And I Perform search: from '<origin_airport>' to '<destination_airport>' with budget under '<budget>' and click Let's Go button
    Then I should see '<destination_airport>' and flight price less than '<budget>'

    Examples:
    | origin_airport     | destination_airport     | budget |
    | Lviv-LWO           | Budapest-BUD            | 20     |
    | Madrid-MAD         | Cologne-CGN             | 20     |
    | Manchester-MAN     | Ibiza-IBZ               | 20     |

  @transfer_search
  Scenario Outline: Verify user can search transfer

    Given I am on the main page
    When I open Plan menu
    And click 'Search Bus and Train link'
    And I Perform search: Pick Country '<pick_up_country>', start from '<pick_up_point>' going to '<drop_off_point>' on '<departure_date>' '<departure_time>' and click Search button
    Then I should see transfer options: date '<departure_date>', time '<departure_time>' and price

    Examples:
    | pick_up_country | pick_up_point | drop_off_point | departure_date | departure_time |
    | Greece          | Chania-CHQ    | Adele          | 2021-12-19     | 10:00          |
    | Montenegro      | Tivat-TIV     | Budva          | 2021-12-19     | 10:00          |
    | Montenegro      | Tivat-TIV     | Cetinje        | 2021-12-20     | 10:00          |

