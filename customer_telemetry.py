import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import csv

fake = Faker()

def random_time():
    hour = random.randint(5, 22)
    minute = random.randint(0, 59)
    return f"{hour:02}:{minute:02}:00"

def generate_start_end_times():
    start_time = datetime.strptime(random_time(), "%H:%M:%S")
    duration = random.randint(10, 90)  # minutes
    end_time = start_time + timedelta(minutes=duration)
    return start_time, end_time

def generate_record(customer_id, age, weight):
    start_time, end_time = generate_start_end_times()
    random_date_str = fake.date_this_year(before_today=True, after_today=False).strftime("%m%d%y")
    start_time_str = f"{random_date_str} {start_time.strftime('%H:%M:%S')}"
    end_time_str = f"{random_date_str} {end_time.strftime('%H:%M:%S')}"

    avg_hr = random.randint(135, 172)
    max_hr = random.randint(max(avg_hr, 135), 180)
    avg_mph = random.randint(10, 20)
    max_mph = random.randint(avg_mph, 50)
    avg_oxygen = random.choice([random.randint(94, 99), random.randint(90, 94)])
    elevation_gain = random.randint(0, 4000)

    # Calculate KCal
    duration_minutes = (end_time - start_time).seconds / 60
    kcal = int((duration_minutes / 30.0) * (380 * weight / 200) * (avg_mph / 10) * (1 + elevation_gain / 2500))

    return {
        "CustomerID": customer_id,
        "StartTime": start_time_str,
        "EndTime": end_time_str,
        "AvgHR": avg_hr,
        "MaxHR": max_hr,
        "AvgMPH": avg_mph,
        "MaxMPH": max_mph,
        "AvgOxygen": avg_oxygen,
        "ElevationGain": elevation_gain,
        "KCal": kcal,
        "Weight": weight,
        "Age": age
    }

# Make sure this file actually exists and matches the columns you expect:
# CustomerID,FirstName,LastName,Age,Weight
customer_df = pd.read_csv('output/customer_data.csv', sep=',')

records = []
for _ in range(10000):
    customer_row = customer_df.sample(1).iloc[0]
    record = generate_record(customer_row['CustomerID'], customer_row['Age'], customer_row['Weight'])
    records.append(record)

df = pd.DataFrame(records)

# Save to a new CSV
df.to_csv('output/customer_telemetry_data.csv', index=False)

print("Synthetic dataset generated and saved to 'output/customer_telemetry_data.csv'")
