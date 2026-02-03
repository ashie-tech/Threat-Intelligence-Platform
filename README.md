# Threat Intelligence Platform (TIP)

## Overview
This project is a basic Threat Intelligence Platform built using Python.  
It collects malicious IP addresses, analyzes their frequency, and assigns
a confidence level based on how often each threat appears.

## Features
- Collects threat indicators (IP addresses)
- Normalizes and deduplicates data
- Assigns confidence levels (low / medium / high)
- Stores structured threat intelligence in CSV format

## Tech Stack
- Python
- CSV
- VS Code

## How It Works
1. Reads malicious IPs from a text-based threat feed
2. Counts occurrences of each IP
3. Assigns confidence based on frequency
4. Outputs intelligence to a CSV file

## Future Improvements
- Integrate real threat feeds (APIs)
- Use a database (SQLite)
- Add a web dashboard (Flask)

## Author
Ashwini Panicker
