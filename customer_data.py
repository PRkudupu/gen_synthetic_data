import random
from faker import Faker
import json

# Initialize Faker with various locales
locales = ['en_US', 'en_GB', 'fr_FR', 'de_DE', 'es_ES', 'it_IT', 'ja_JP', 'zh_CN', 'ar_AE', 'hi_IN']
fake = Faker(locales)

# Function to create a single synthetic record
def create_record(customer_id):
    # Choose a random locale for variety in names
    fake = Faker(random.choice(locales))
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 90)
    weight = random.randint(100, 250)  # Random weight in pounds
    return {
        "CustomerID": customer_id,
        "FirstName": first_name,
        "LastName": last_name,
        "Age": age,
        "Weight": weight
    }

# Create 1000 records
records = [create_record(100001 + i) for i in range(1000)]

# Write records to a JSON file
output_file = 'output/customer_data.json'
with open(output_file, 'w') as f:
    json.dump(records, f, indent=4)

# Display the first 10 records for verification
for record in records[:10]:
    print(record)

# Optional: If you need to process it further, you can convert it to a pandas DataFrame or save it to a file.
"""
### Explanation:
- **Faker Library**: This script uses the Faker library with multiple locales to ensure that names are generated from a broad array of cultures.
- **CustomerID**: A unique ID is assigned to each customer, starting from 100001.
- **Names**: First and last names are generated using different locales to simulate diversity.
- **Age**: Randomly assigns an age between 18 and 90 years, representative of a wide age range.
- **Weight**: Randomly assigns a weight in pounds from a typical range for adults.

### Instructions:
1. **Install Required Library**: Make sure to install the `Faker` library using pip: `pip install Faker`.
2. **Run the Script**: Execute the script in your Python environment.
3. **Verify Output**: The script prints the first 10 records for a quick inspection. Adjust the printed range or any part of the logic to suit your specific needs.
"""