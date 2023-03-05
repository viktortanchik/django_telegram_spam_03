#4607065001445

import requests

# Replace `1234567890123` with your barcode
barcode = '5000159461122'

# Query the Open Food Facts API
response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')

# Parse the response and extract product details
if response.status_code == 200:
    data = response.json()
    product_name = data.get('product', {}).get('product_name', 'Unknown')
    ingredients = data.get('product', {}).get('ingredients_text', 'Unknown')
    nutrition = data.get('product', {}).get('nutriments', {})
    energy = nutrition.get('energy_value')
    fat = nutrition.get('fat_value')
    carbs = nutrition.get('carbohydrates_value')
    protein = nutrition.get('proteins_value')

    print(f'Product: {product_name}')
    print(f'Ingredients: {ingredients}')
    print(f'Energy: {energy} kJ')
    print(f'Fat: {fat} g')
    print(f'Carbohydrates: {carbs} g')
    print(f'Protein: {protein} g')
else:
    print('Barcode not found.')
