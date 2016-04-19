from datetime import date


def get_next_leap_year(start_year):
    year = start_year + 1
    while True:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    # divisible by 100 and 400 is leap year
                    return year
                else:
                    # divisible by 100 and not 400 is not
                    year += 1
                    continue
            return year
        year += 1


def get_leap_year_iter(start_year):
    year = start_year
    while True:
        leap_year = get_next_leap_year(year)
        year = leap_year
        yield year


def get_next_n_leap_years(n):
    current_year = date.today().year
    leap_years = []
    for idx, year in enumerate(get_leap_year_iter(current_year)):
        leap_years.append(year)
        if idx == n - 1:
            return leap_years


leap_years = get_next_n_leap_years(20)
print "{!r}".format(leap_years)


    
