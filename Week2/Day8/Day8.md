# Day 8 – Threat Intelligence & Data Collection

## Overview

Today I worked on the basics of threat intelligence and how security data can be handled programmatically.

For the practical task, I created a Python script that reads sample threat data from a JSON file and examines each indicator. The script identifies whether an indicator is an IP address, domain, URL, or an unknown value, and then stores the processed information in a separate JSON file.

The main goal was to understand how raw security data can be organized into a format that is easier to work with.

---

## Objectives

- Understand what threat intelligence means in cybersecurity
- Learn how security data can be represented using JSON
- Understand the purpose of Indicators of Compromise (IOCs)
- Identify common types of indicators
- Practice reading and writing JSON files with Python
- Organize raw threat data into a structured format
- Handle basic input-file and JSON errors

---

## IOC Types

The script checks each indicator and assigns one of the following categories:

- **IP Address** – IPv4-style addresses such as `185.10.20.30`
- **Domain** – Domain names such as `example.com`
- **URL** – Web addresses beginning with `http://` or `https://`
- **Unknown** – Values that do not match the supported formats

The classification is only used to organize the data. It does not decide whether an indicator is actually malicious.

---

## Project Structure

Day8/
├── Threat_data.py
├── sample_threat_data.json
├── ioc_output.json
└── Day_08.md

## How it Works
```text
Threat Intelligence Dataset
          ↓
      JSON Input
          ↓
     Python Parser
          ↓
      IOC Detection
          ↓
    Structured JSON
```


## Technologies Used

* Python 
* JSON
* File Handling
* Git
* GitHub

## How to Run

Clone the repository and navigate to the project directory:

cd Day_08

Run the Python script:

python Threat_Data.py

## Sample Output


[*] Starting Threat Intelligence Processor...
[+] Output saved to ioc_output.json
[+] Processed 3 indicators.

IOC Summary
----------------------------------------
IP       | 185.10.20.30 | High
DOMAIN   | malicious-example.com | High


[+] Processing completed.

## Security Relevance

Threat intelligence is useful when investigating suspicious activity because indicators such as IP addresses, domains, and URLs can provide starting points for security analysis.

For example, an analyst investigating a suspicious login could extract an IP address from a log and compare it with known threat intelligence. Similar checks can be performed for suspicious domains or URLs.

This project covers only the initial data-processing stage. The indicators produced here could later be passed to other security processes such as log enrichment, reputation checking, or threat scoring.

## Limitations

The project currently works with a local sample dataset and does not retrieve information from a live threat intelligence service.

The indicator classification is also basic. It identifies the general format of an indicator but does not verify its reputation or determine whether it is malicious.

For example, an IP address being classified as an IP does not mean that the address is malicious.

## Future Improvements

The project can be extended in several ways:

* Connect the script to a real threat intelligence API
* Improve IP address validation
* Add support for file hashes
* Check indicators against reputation services
* Remove duplicate indicators
* Add timestamps to threat records
* Add confidence levels to indicators
* Include more IOC formats
* Use the processed data as input for the Day 9 log enrichment task

## Learning Outcome

The main takeaway was understanding the first step of turning security data into something structured and useful for further analysis.