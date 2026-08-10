import json

INPUT_FILE = "Sample_Threat_data.json"
OUTPUT_FILE = "ioc_output.json"


def read_data():
    """Read threat intelligence data from the JSON file."""
    try:
        with open(INPUT_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] {INPUT_FILE} was not found.")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] {INPUT_FILE} contains invalid JSON.")
        return []


def classify_indicator(value):
    """Identify whether an indicator is an IP, domain, URL, or unknown."""

    if value.startswith(("http://", "https://")):
        return "url"

    parts = value.split(".")

    if len(parts) == 4 and all(part.isdigit() for part in parts):
        return "ip"

    if "." in value:
        return "domain"

    return "unknown"


def process_data(data):
    """Add IOC type information to each threat record."""

    processed_data = []

    for threat in data:
        indicator = threat.get("indicator", "").strip()

        if not indicator:
            continue

        record = {
            "indicator": indicator,
            "ioc_type": classify_indicator(indicator),
            "threat": threat.get("threat", "Unknown"),
            "severity": threat.get("severity", "Unknown"),
            "source": threat.get("source", "Unknown")
        }

        processed_data.append(record)

    return processed_data


def save_data(data):
    """Save the processed threat intelligence data."""

    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"[+] Output saved to {OUTPUT_FILE}")


def display_summary(data):
    """Display a simple summary of identified IOCs."""

    print("\nIOC Summary")
    print("-" * 40)

    for threat in data:
        print(
            f"{threat['ioc_type'].upper():8} "
            f"| {threat['indicator']} "
            f"| {threat['severity']}"
        )


def main():
    print("[*] Starting Threat Intelligence Processor...")

    data = read_data()

    if not data:
        print("[!] No threat data available.")
        return

    processed_data = process_data(data)

    save_data(processed_data)

    print(f"[+] Processed {len(processed_data)} indicators.")

    display_summary(processed_data)

    print("\n[+] Processing completed.")


if __name__ == "__main__":
    main()