
# Site Latency Checker

**Author:** M.R. Salavatian  
**Website:** [www.PuleElec.ir](http://www.PuleElec.ir)

---

## Overview

Site Latency Checker is a Python tool for monitoring and measuring the response latency of multiple websites concurrently.  
It uses HTTP HEAD requests to quickly check how fast each site responds and displays the results in real time with a progress bar.

---

## Features

- Check multiple websites' response times in parallel.
- Fully configurable list of target websites.
- Supports both HTTP and HTTPS protocols.
- Adjustable request interval and timeout.
- Displays a neat, continuously updating table with response times.
- Lightweight and easy to use.

---

## Requirements

- Python 3.6 or higher
- `requests` library

---

## Installation

1. Clone or download this repository.
2. Install dependencies via pip:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script using Python:

```bash
python LatencyChecker.py
```

By default, the script will continuously check the latency of a predefined list of websites and update the output every few seconds.

> 💡 **To exit the terminal, press `Ctrl + C`.**

---

## Configuration

- **Change websites**: You can edit the `urls` list inside `LatencyChecker.py` to add or remove websites.
- **Use HTTP or HTTPS**: Both protocols are supported. Just include `http://` or `https://` in the URL.
- **Adjust request interval**: Modify the `wait_time` variable (in milliseconds) to set how long to wait between checks.
- **Adjust request timeout**: Change the `timeout_sec` variable to define how long the program should wait for a website to respond before considering it as "Timeout".

---

## Release (Executable File)

A standalone Windows executable `SiteLatencyChecker.exe` is included in the [Releases](https://github.com/MRSalavatian/LatencyMonitorTool/releases) section.  
This executable is built using [PyInstaller](https://www.pyinstaller.org/).

### How to use

1. Go to the [Releases page](https://github.com/MRSalavatian/LatencyMonitorTool/releases).
2. Download the latest `.exe` file.
3. Double-click to run it.

> 💡 **Note:** If you don't have any programming knowledge, you can simply download the EXE file and run it directly — no need to install Python or any additional packages.

---

## Example Output

```
https://github.com/MRSalavatian - Www.PuleElec.ir
Time     | Aparat     | Divar      | BMI        | Digikala   | Google     | Yahoo      | Chess      | Facebook   | X
19:22:26 | 66.40 ms   | 72.66 ms   | 54.26 ms   | 50.42 ms   | 430.27 ms  | 389.95 ms  | 423.91 ms  | 807.20 ms  | 1400.04 ms
19:22:38 | 51.37 ms   | 46.32 ms   | 71.49 ms   | 36.44 ms   | 503.35 ms  | 330.06 ms  | 381.81 ms  | 327.35 ms  | 1365.91 ms
19:22:50 | 50.52 ms   | 46.23 ms   | 38.34 ms   | 45.82 ms   | 557.54 ms  | 1332.16 ms | 390.67 ms  | 362.81 ms  | 1447.50 ms
Waiting: |█████████---------------------| 1575/5000 ms
...
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, contact M.R. Salavatian via [www.PuleElec.ir](http://www.PuleElec.ir).
