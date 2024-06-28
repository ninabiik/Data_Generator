import csv
import random
from datetime import datetime, timedelta


def generate_mock_data(num_records):
    mock_data = []

    for _ in range(num_records):
        today = datetime.now()
        datatime = today - timedelta(days=random.randint(0, 365))
        duration = random.randint(1, 100)
        caller_mobile_num = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 999)}"
        callee_mobile_num = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 999)}"

        mock_data.append((datatime, duration, caller_mobile_num, callee_mobile_num))

    return mock_data


def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['datatime', 'duration', 'caller_mobile_num', 'callee_mobile_num'])
        writer.writerows(data)
    print("data saved")


mock_data = generate_mock_data(100)
save_to_csv(mock_data, 'test_call_logs')
