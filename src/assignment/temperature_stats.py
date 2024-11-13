def get_temperature_stats(file_path):
    """
    in given file each line will represent city name and temperature in celsius separated by comma

    return a dictionary with following keys
    - hottest_city: name of the city with highest temperature
    - coldest_city: name of the city with lowest temperature
    - average_temperature: average temperature of all cities
    - temperature_range: difference between highest and lowest temperature
    """
    cities_temp = {}
    with open(file_path, 'r') as f:
        for line in f:
            city, temp = line.strip().split(',')
            cities_temp[city] = temp

    max_temp = -100
    max_temp_city = ""
    min_temp = +100
    min_temp_city = ""
    total_temp = 0

    for city, temp in cities_temp.items():
        temp = float(temp)
        total_temp += temp

        if temp > max_temp:
            max_temp = float(temp)
            max_temp_city = city

        if temp < min_temp:
            min_temp = temp
            min_temp_city = city

    avr_temp = total_temp / len(cities_temp)
    temp_range = max_temp - min_temp

    temperature_stats = {
        "hottest_city": max_temp_city,
        "coldest_city": min_temp_city,
        "average_temperature": avr_temp,
        "temperature_range": temp_range,
    }

    return temperature_stats
