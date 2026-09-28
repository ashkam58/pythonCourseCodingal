# M4L3A3: Get the Country Code
# Activity 3: Dictionaries - Safe lookup using .get() with fallback values

country_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}

print("Country code for India -")
print(country_code.get('India', 'Not Found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
