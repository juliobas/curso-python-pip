import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv("data.csv")
    continents = list(set(map(lambda x: x['Continent'], data)))
    for continent in continents:
        print(continent)
    
    continent_select = input("Type one continent: ")

    data = list(filter(lambda x: x['Continent'] == continent_select, data))
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(continent_select, countries, percentages)

    country = input("Type country: ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)
    else:
        print("No data found")

if __name__ == '__main__':
    run()