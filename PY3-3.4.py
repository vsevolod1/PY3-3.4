import osa


# 1. Температура
def convert_temperature (value_temp, from_unit, to_unit='degreeCelsius'):
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ConvertTemp(value_temp, FromUnit=from_unit, ToUnit=to_unit)
    return response

def average(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum/len(num_list)

def average_temp_file(file):
    temperature_list = []
    with open(file) as f:
        for line in f:
            temperature = convert_temperature(line.split(' ')[0], 'degreeFahrenheit')
            temperature_list.append(temperature)
    return round(average(temperature_list),1)


# 2. Валюты
def conversion_rate(amount, from_currency, to_currency='RUB'):
    URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ConvertToNum(fromCurrency=from_currency, toCurrency=to_currency, amount=amount, rounding=False)
    return response

def total_cost_file(file):
    total_cost = 0
    with open(file) as f:
        for line in f:
            route = line.split()
            route_cost = conversion_rate(float(route[1]), route[2])
            total_cost += route_cost
    return round(total_cost,2)


# 3. Расстояние
def dist_unit(length_value, from_length, to_length_unit='Kilometers'):
    URL = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ChangeLengthUnit(LengthValue=length_value, fromLengthUnit=from_length, toLengthUnit=to_length_unit)
    return response

def total_dist_file(file):
    total_dist = 0
    with open(file) as f:
        for line in f:
            route = line.split()
            route_dist = dist_unit(float(route[1].replace(',','')), route[2].replace('mi', 'Miles'))
            total_dist += route_dist
    return round(total_dist, 2)



print('Средняя температура: {}'.format(average_temp_file('./temps.txt')))
print ('Бюджет на поездку: {}'.format(total_cost_file('./currencies.txt')))
print ('Общее расстояние: {}'.format(total_dist_file('./travel.txt')))
