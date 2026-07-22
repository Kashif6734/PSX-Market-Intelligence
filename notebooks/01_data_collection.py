import yfinance as yf
import os
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(
    filename="logs/downloading_psx_data.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="a"
)
# Silence noisy libraries
logging.getLogger("yfinance").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("peewee").setLevel(logging.WARNING)
companies = ["OGDC.KA", "PPL.KA", "HBL.KA", "MCB.KA", "LUCK.KA", "DGKC.KA"]
save_path = "data_raw"
start_date = "2020-01-01"
end_date = "2025-11-28"
MAX_RETRIES = 3

def download_ticker(ticker):
    """Download one ticker with retry logic"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Downloading {ticker} (Attempt {attempt})...")
            data = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                auto_adjust=True,
                progress=False
            )

            if data.empty:
                raise ValueError("No data returned")

            file_name = f"{ticker.replace('.KA', '')}.csv"
            os.makedirs(save_path, exist_ok=True)
            data.to_csv(f"{save_path}/{file_name}")

            logging.info(f"{ticker} downloaded successfully.")
            return f"✅ {ticker} done"

        except Exception as e:
            logging.warning(f"{ticker} failed on attempt {attempt}: {e}")
            time.sleep(2)  # wait before retry
    
    logging.error(f"{ticker} failed after {MAX_RETRIES} attempts.")
    return f"❌ {ticker} failed"


def download_raw_data():
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_ticker, ticker) for ticker in companies]

        for future in as_completed(futures):
            print(future.result())

    total_time = (time.time() - start_time) / 60
    
    logging.info(f"All downloads completed in {total_time:.2f} minutes.")
    print(f"\n🎉 All downloads completed in {total_time:.2f} minutes.")

if __name__== '__main__':
    download_raw_data()
