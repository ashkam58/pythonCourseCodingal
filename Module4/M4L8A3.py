# M4L8A3: Get the Country Code
# Activity 3: Dictionaries - Safe lookup using .get() with fallback values

country_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}

# Search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))

# Search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
