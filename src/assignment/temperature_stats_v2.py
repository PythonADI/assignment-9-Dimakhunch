def get_temperature_stats_v2(file_path):
    """
    in given file each line will represent city name and temperature in celsius separated by comma
    each city can have multiple entries in the file

    return a dictionary with following keys
    - hottest_city: name of the city with highest temperature
    - coldest_city: name of the city with lowest temperature
    - average_temperature: average temperature of all cities
    - temperature_range: difference between highest and lowest temperature
    """
    # wrtie your code here
    cities_temp = {}

    with open(file_path, 'r') as f:
        for line in f:
            city, temp = line.strip().split(',')
            temp = float(temp)

            if city not in cities_temp:
                cities_temp[city] = []
            cities_temp[city].append(temp)

    max_temp = -100
    max_temp_city = ""
    min_temp = 100
    min_temp_city = ""
    total_temp = 0
    total_count = 0

    for city, temps in cities_temp.items():
        avg_city_temp = sum(temps) / len(temps)
        total_temp += avg_city_temp
        total_count += 1

        if avg_city_temp > max_temp:
            max_temp = avg_city_temp
            max_temp_city = city

        if avg_city_temp < min_temp:
            min_temp = avg_city_temp
            min_temp_city = city

    average_temperature = total_temp / total_count

    temperature_range = max_temp - min_temp

    temperature_stats_v2 = {
        "hottest_city": max_temp_city,
        "coldest_city": min_temp_city,
        "average_temperature": average_temperature,
        "temperature_range": temperature_range
    }

    return temperature_stats_v2
