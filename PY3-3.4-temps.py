import osa

def convert_temperature (value_temp, from_unit, to_unit='degreeCelsius'):
    URL1 = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client1 = osa.client.Client(URL1)
    response1 = client1.service.ConvertTemp(value_temp, FromUnit=from_unit, ToUnit=to_unit)
    return response1
    # print(response1)
file = './temps.txt'

def average(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum/len(num_list)

temperature_list = []
with open(file) as f:
    for line in f:
        temperature = convert_temperature(line.split(' ')[0], 'degreeFahrenheit')
        temperature_list.append(temperature)
print(round(average(temperature_list),1))

# for temperature in temperature_list:
