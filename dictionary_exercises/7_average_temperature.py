#7- A city measures its daily temperature and stores it in a tuple. Create a function that returns the average
#of the temperature.

def average_temperature(stored_temperature_data):
    days_of_sample=len(stored_temperature_data)
    temperature_sums=0
    for temperature in stored_temperature_data:
        temperature_sums+=temperature
    average_temperature = temperature_sums/days_of_sample
    
    return average_temperature