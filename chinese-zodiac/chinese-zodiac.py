rat_year = [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020, 2032]
ox_year = [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021, 2033]
tiger_year = [1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022, 2034]
rabbit_year = [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023, 2035]
dragon_year = [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024, 2036]
snake_year = [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025, 2037]
horse_year = [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038]
goat_year = [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027, 2039]
monkey_year = [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028, 2040]
rooster_year = [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029, 2041]
dog_year = [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030, 2042]
pig_year = [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031, 2043]

list_zodiac_year = {
    'Rat': rat_year,
    'Ox': ox_year,
    'Tiger': tiger_year,
    'Rabbit': rabbit_year,
    'Dragon': dragon_year,
    'Snake': snake_year,
    'Horse': horse_year,
    'Goat': goat_year,
    'Monkey': monkey_year,
    'Rooster': rooster_year,
    'Dog': dog_year,
    'Pig': pig_year,
}

user_year = int(input ("Please key in the year you born: "))

found = False
for list_zodiac, years in list_zodiac_year.items():
    if user_year in years:
        print(f"{user_year} year Chinese zodiac - {list_zodiac}")
        found = True
        break
if not found:
    print("Please enter valid year. Example key in '1992'")

