# Test Results

Python version used: Python 3.13.5 | Operating system: Generated and checked in the project environment | Date: 2026-10-28

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | **PASS** |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain.; Uses HTTP. HTTPS alone does not prove trust. | **PASS** |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; inspect carefully.; Uses HTTP. HTTPS alone does not prove trust. | **PASS** |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | **PASS** |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | **PASS** |

## Notes
- The five workbook sample strings were checked against the program's output.
- The program only inspects the text; it does not visit any URL or make network requests.
- A result with no listed warning signs is not proof that a URL is safe.
