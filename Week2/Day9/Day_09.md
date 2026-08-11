# Day 9 – Log Enrichment System

## Overview

This project implements a basic log enrichment system using Python.

The system takes raw security events stored in JSON format and adds useful context to each event, including location information, device type, and severity. The enriched events are then saved as a structured JSON file for further security analysis.

## Objectives

- Understand the concept of log enrichment in a SOC environment
- Work with raw security logs stored in JSON
- Add contextual information to security events
- Identify device types from user-agent information
- Assign severity based on event activity
- Generate structured enriched logs using Python

## Enrichment Pipeline

```text
Raw Security Logs
        ↓
Read JSON Input
        ↓
IP / Event / User-Agent Extraction
        ↓
Location Enrichment
        ↓
Device Type Identification
        ↓
Severity Classification
        ↓
Enriched JSON Output
```
## Project structure


```text
Day9/
├── log_enrichment.py
├── sample_logs.json
├── enriched_logs.json
└── Day9.md
```

## Technologies Used
Python 3
JSON
File Handling
Dictionaries
Conditional Logic
Git / GitHub

## Enrichment Fields

The system adds the following information to the original logs:

Country
Region
Device Type
Severity
## Severity Levels

Low – Normal or low-risk activity

Medium – Activity that may require further investigation

High – Activity considered more suspicious based on the rules implemented in the project

## How It Works

The script reads each event from sample_logs.json and processes the available information.

Location

The source IP is checked against a local sample mapping to obtain country and region information.

Device Type

The user_agent field is examined to identify common platforms such as Windows, Linux, Android, iPhone, and macOS.

Severity

A rule-based approach is used to classify events. Repeated failed attempts and blocked or suspicious activity can result in a higher severity level.

## How to Run

Navigate to the Day 9 directory:

cd D:\Jagspire\Week2\Day9

Run the script:

python log_enrichment.py

The script reads:

sample_logs.json

and generates:

enriched_logs.json

## Sample Output
[*] Starting Log Enrichment System...
[+] Enriched logs saved to enriched_logs.json
[+] Enriched 4 log events.

[+] Enrichment Summary:
    185.220.101.42 | Failed Login | Germany | Windows | High
    45.155.205.233 | Successful Login | United States | Linux | Low
    192.168.1.10 | File Access | India | Android | Low
    185.220.101.42 | Blocked Access | Germany | Windows | High

## GeoIP Implementation

For this project, a small local mapping is used to demonstrate the concept of GeoIP enrichment.

The mapping provides sample country and region information for the IP addresses used in the test dataset.

This is not a live GeoIP lookup. In a production SOC environment, a trusted and regularly updated GeoIP database or service would be more appropriate.

## Security Relevance

Log enrichment helps security analysts understand events by adding context to otherwise raw log data.

Information such as source location, device type, and severity can make it easier to investigate events, prioritize suspicious activity, and correlate security alerts.

The enriched logs from this project can also serve as input for later security-processing tasks such as risk scoring and anomaly detection.

## Limitations
The GeoIP information is based on a local sample dataset.
Device identification uses simple user-agent matching.
Severity classification is rule-based.
The system does not determine whether an IP address is actually malicious.
The project uses a small sample dataset rather than live security logs.
## Future Improvements
Integrate a real GeoIP database or API
Add IP reputation checking
Improve device and operating-system detection
Add more severity rules
Detect repeated activity across multiple events
Connect the enriched logs to the Day 10 risk-scoring module
Add anomaly detection in later stages of the project

## Learning Outcome

This project helped me understand how raw security logs can be enriched with additional context using Python.

I practiced working with JSON files, functions, dictionaries, file handling, user-agent analysis, and rule-based severity classification. It also gave me a better understanding of how log enrichment can support security monitoring and investigation in a SOC environment.