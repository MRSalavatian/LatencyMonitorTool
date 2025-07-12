import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from datetime import datetime

urls = [
    "http://www.Aparat.com",
    "http://www.Divar.ir",
    "http://www.BMI.ir",
    "http://www.Digikala.com",
    "http://www.Google.com",
    "http://www.Yahoo.Com",
    "http://www.Chess.Com",
    "http://www.Facebook.Com",
    "http://www.X.Com"
]

timeout_sec = 5     # Timeout for getting response from site
col_width = 10      # Column width
wait_time = 5000    # Time between tests (in milliseconds)

headers_http = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

def clean_name(url):
    url = url.replace("https://", "").replace("http://", "")
    url = url.replace("www.", "")
    parts = url.split(".")
    return parts[0]

def check_url(url):
    try:
        start_time = time.time()
        r = requests.head(url, headers=headers_http, timeout=timeout_sec)
        r.raise_for_status()
        end_time = time.time()
        delay = (end_time - start_time) * 1000
        return "{:.2f} ms".format(delay)
    except:
        return "Timeout"

def print_progress_bar(iteration, total, length=30):
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f"\rWaiting: |{bar}| {iteration}/{total} ms", end='', flush=True)

headers = [clean_name(u).ljust(col_width) for u in urls]

print("https://github.com/MRSalavatian - Www.PuleElec.ir")
print("To exit the terminal, press `Ctrl + C`")
print("Time".ljust(8) + " | " + " | ".join(headers))

while True:
    results = [None] * len(urls)

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_index = {executor.submit(check_url, url): idx for idx, url in enumerate(urls)}

        for future in as_completed(future_to_index):
            idx = future_to_index[future]
            results[idx] = future.result()

    values = [r.ljust(col_width) for r in results]
    now_str = datetime.now().strftime("%H:%M:%S")
    print(f"{now_str} | " + " | ".join(values))
 


    for i in range(wait_time + 1):
        print_progress_bar(i, wait_time)
        time.sleep(0.001)

    print('\r' + ' ' * 60 + '\r', end='', flush=True)
