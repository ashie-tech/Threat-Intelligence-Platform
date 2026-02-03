import csv
from datetime import datetime

SOURCE_NAME = "sample_feed"
THREAT_TYPE = "brute_force"


with open("malicious_ips.txt", "r") as file:
    ip_list = [ip.strip() for ip in file if ip.strip()]

ip_frequency = {}
for ip in ip_list:
    ip_frequency[ip] = ip_frequency.get(ip, 0)+1


def get_confidence(count):
    if count >= 4:
        return "hgh"
    elif count >= 2:
        return "medium"
    else:
        return "low"


with open("threat_data_new.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["ip", "threat_type", "confidence_level",
                    "source", "date_collected"])

    for ip, count in ip_frequency.items():
        writer.writerow(
            [ip, THREAT_TYPE, get_confidence(count), SOURCE_NAME, datetime.now().strftime("%Y-%m-%d")])

print("Threat intelligence with confidence scoring saved")
