"""
EWB Phishing URL Awareness Checker
Defensive learning only: this program inspects URL text and never opens links.
"""

import ipaddress
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Return warning messages for selected URL-text clues."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement 1: malformed URL text is handled without crashing.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Validate the address as an actual IPv4 address, not just four number groups.
    try:
        ipaddress.IPv4Address(host)
        is_ipv4 = True
    except ipaddress.AddressValueError:
        is_ipv4 = False

    if is_ipv4:
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement 2: keep the tool running for multiple samples; q exits.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        if findings and not findings[0].startswith(
            ("No URL entered", "Could not identify", "This text is not valid",
             "No listed warning")
        ):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
