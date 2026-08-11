import json


INPUT_FILE = "sample_logs.json"
OUTPUT_FILE = "enriched_logs.json"


# Sample GeoIP information for the test IPs
GEOIP_DATA = {
    "185.220.101.42": {
        "country": "Germany",
        "region": "Europe"
    },
    "45.155.205.233": {
        "country": "United States",
        "region": "North America"
    },
    "192.168.1.10": {
        "country": "India",
        "region": "Asia"
    }
}


def load_logs(filename):
    """Load raw logs from a JSON file."""

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format: {filename}")
        return []


def get_location(ip):
    """Return location information for an IP address."""

    return GEOIP_DATA.get(
        ip,
        {
            "country": "Unknown",
            "region": "Unknown"
        }
    )


def identify_device(user_agent):
    """Identify the device type from the user-agent string."""

    user_agent = user_agent.lower()

    if "windows" in user_agent:
        return "Windows"

    if "android" in user_agent:
        return "Android"

    if "iphone" in user_agent:
        return "iPhone"

    if "macintosh" in user_agent:
        return "macOS"

    if "linux" in user_agent:
        return "Linux"

    return "Unknown"


def assign_severity(event, failed_attempts):
    """Assign severity based on the event and repeated activity."""

    event = event.lower()

    if failed_attempts >= 5:
        return "High"

    if "failed login" in event:
        return "Medium"

    if "blocked" in event or "suspicious" in event:
        return "High"

    return "Low"


def enrich_logs(logs):
    """Add useful security context to each log."""

    enriched_logs = []

    for log in logs:

        ip = log.get("ip", "Unknown")
        user_agent = log.get("user_agent", "")
        event = log.get("event", "Unknown")
        failed_attempts = log.get("failed_attempts", 0)

        location = get_location(ip)
        device = identify_device(user_agent)
        severity = assign_severity(event, failed_attempts)

        enriched_log = {
            **log,
            "country": location["country"],
            "region": location["region"],
            "device_type": device,
            "severity": severity
        }

        enriched_logs.append(enriched_log)

    return enriched_logs


def save_logs(logs, filename):
    """Save enriched logs to a JSON file."""

    with open(filename, "w") as file:
        json.dump(logs, file, indent=4)

    print(f"[+] Enriched logs saved to {filename}")


def main():

    print("[*] Starting Log Enrichment System...")

    logs = load_logs(INPUT_FILE)

    if not logs:
        print("[!] No logs available for processing.")
        return

    enriched_logs = enrich_logs(logs)

    save_logs(enriched_logs, OUTPUT_FILE)

    print(f"[+] Enriched {len(enriched_logs)} log events.")

    print("\n[+] Enrichment Summary:")

    for log in enriched_logs:
        print(
            f"    {log['ip']} | "
            f"{log['event']} | "
            f"{log['country']} | "
            f"{log['device_type']} | "
            f"{log['severity']}"
        )


if __name__ == "__main__":
    main()