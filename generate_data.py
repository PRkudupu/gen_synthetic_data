import random
import datetime
import json
import os

def generate_time():
    # Generate a random time between 05:00:00 to 23:00:00
    start_hour = random.randint(5, 22)
    start_minute = random.randint(0, 59)
    
    start_time = datetime.time(start_hour, start_minute)
    
    # Duration between 10 to 90 minutes, most around 30 minutes
    duration = int(random.triangular(10, 90, 30))
    
    end_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(minutes=duration)).time()
    
    return (start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S"))

def calculate_kcal(start_hour, duration, avg_mph, elevation_gain, weight):
    # A simplified calculation for KCal
    # Base calorie consumption
    kcal = 0.2 * weight * (duration/60) * ((avg_mph/5) + (elevation_gain/500))
    return int(kcal)

def generate_record(customer_id):
    start_time, end_time = generate_time()
    avg_hr = random.randint(135, 172)
    max_hr = random.randint(max(avg_hr, 135), 180)
    avg_mph = random.randint(10, 20)
    max_mph = random.randint(avg_mph, 50)
    avg_oxygen = random.choice([random.randint(94, 99)] + [90] * 5)  # more likely to be 94-99
    elevation_gain = random.randint(0, 4000)
    weight = random.randint(100, 250)  # Assuming a weight range
    age = random.randint(16, 76)
    
    end_hour = int(end_time.split(':')[0])
    start_hour = int(start_time.split(':')[0])
    
    duration = (end_hour*60 + int(end_time.split(':')[1])) - (start_hour*60 + int(start_time.split(':')[1]))
    
    # Calculate KCal with a simplified model
    kcal = calculate_kcal(start_hour, duration, avg_mph, elevation_gain, weight)
    
    return {
        "CustomerID": customer_id,
        "StartTime": "022224 " + start_time,
        "EndTime": "022224 " + end_time,
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

# Generate 1000 records
data = [generate_record(100401 + i) for i in range(1000)]

# Ensure the output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Output as JSON string to a file
output_file_path = os.path.join(output_dir, "generated_data.json")
with open(output_file_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Data has been written to {output_file_path}")
