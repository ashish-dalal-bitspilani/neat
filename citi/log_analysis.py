from collections import defaultdict
from datetime import datetime

log_type_counts = defaultdict(int)
hourly_counts = defaultdict(int)

file_path = "C:/Users/91702/Desktop/log.csv"

with open(file_path, "r") as file:
    next(file)
    for line in file:
        # split the line into fields
        column_values = line.strip().split(',')
        datetime_obj = datetime.strptime(column_values[0].strip(), "%d-%m-%Y %H:%M:%S")
        log_type = column_values[1].strip()
        log_type_counts[log_type] += 1

        hour_key = datetime_obj.strftime("%d-%m-%Y %H:00")
        hourly_counts[hour_key] += 1

print("Log Type Counts :")
for logtype, count in log_type_counts.items():
    print(f"{logtype} : {count}")

print("Hourly Type Counts :")
for hour, count in sorted(hourly_counts.items()):
    print(f"{hour} : {count}")