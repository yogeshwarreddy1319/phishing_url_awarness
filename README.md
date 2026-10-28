# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick where a fake link or message tries to make someone share a password, payment detail, or OTP. This beginner-friendly Python command-line project reads URL text and reports a few visible warning signs. It never opens the URL or sends information anywhere.

## Features
- Detects an `@` symbol in the URL text.
- Flags URLs longer than 100 characters.
- Flags a valid IPv4 address used as the hostname.
- Flags hostnames with 5 or more dot-separated segments.
- Flags hostnames containing `xn--` (punycode marker).
- Flags the `http` scheme.
- Handles malformed URL text without crashing.
- Allows multiple sample checks in one run; type `q` to quit.

## Requirements
- Python 3.10 or later.
- No extra packages are required.

## How to Run
Open a terminal in this folder.

**Windows**
```bash
python phishing_checker.py
```

**macOS / Linux**
```bash
python3 phishing_checker.py
```

Enter one of the sample strings from `tests/test_samples.md`. Type `q` to exit.

## Example Output
```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.

Never enter passwords from unexpected links.
```

## Testing
Five sample strings from the workbook are recorded in [`tests/test_samples.md`](tests/test_samples.md). The test table records expected results, actual program output, and pass/fail.

## Screenshots
![Sample run](screenshots/sample_run.png)

![Test results](screenshots/test_results.png)

## Improvements
1. **Safer malformed-input handling** — URL parsing is inside `try/except`, so malformed input such as `http://[bad` returns a clear message instead of stopping the program. This was checked with a separate malformed-input test.
2. **Repeat-and-quit menu** — the program can inspect multiple sample strings in one run and exits when the user types `q`, `quit`, or `exit`. This was checked by running the program with more than one input and then quitting.

## Limitations
This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware, check a site's reputation, or prove that a URL is safe. No warning signs found does **not** mean a URL is safe. Some legitimate URLs may trigger warnings, and some harmful URLs may trigger none.

## Ethical Use
Use the workbook's reserved sample strings only. Do not collect credentials, send phishing messages, open suspicious links for testing, or scan/probe websites without written authorization. Do not upload passwords, tokens, API keys, or private data.

## Author
[Replace with your name]  
[Replace with your class/batch or course]  
EWB Courses
