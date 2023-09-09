import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.pool_executor.hw29 import make_site_screenshot

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Parse browser name for Selenium.')
    parser.add_argument('--browser',
                        choices=['firefox', 'chrome'],
                        default='firefox',
                        help='Choose browser (default is  firefox)')

    args = parser.parse_args()
    browser = args.browser

    urls = ['https://google.com.ua', 'https://www.youtube.com/', 'https://hotline.ua/',
            'https://github.com/', 'https://docs.python.org/3.11/']

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(make_site_screenshot, url, browser) for url in urls]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Something went wrong. Issue in future result: {e}")
