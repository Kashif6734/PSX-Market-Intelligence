import pandas as pd
import glob
import os

def run_psx_etl(clean_path="data_clean", sector_file="data_raw/sectors.csv", index_file="data_clean/KSE100.csv"):
    print("🚀 Starting PSX ETL Pipeline...")

    # ---------------------------
    # 1. LOAD COMPANY FILES
    # ---------------------------
    company_files = glob.glob(clean_path + "/*.csv")

    # remove index file from list
    company_files = [f for f in company_files if "kse100" not in f.lower()]

    company_data_list = []

    for file in company_files:
        df = pd.read_csv(file)

        # Extract ticker name from filename
        ticker = os.path.basename(file).replace(".csv", "").upper()
        df["Ticker"] = ticker

        # Fix Date format
        df["Date"] = pd.to_datetime(df["Date"], format="mixed", dayfirst=True, errors="coerce")
        df = df.dropna(subset=["Date"])  # remove invalid dates

        company_data_list.append(df)

    # Combine all companies
    company_df = pd.concat(company_data_list, ignore_index=True)
    print("✔ Loaded company data:", company_df.shape)



    # ---------------------------
    # 2. LOAD SECTOR FILE
    # ---------------------------
    sector_df = pd.read_csv(sector_file)
    sector_df["Ticker"] = sector_df["Ticker"].str.upper()  # standardize

    print("✔ Loaded sector data:", sector_df.shape)



    # ---------------------------
    # 3. LOAD KSE100 INDEX FILE
    # ---------------------------
    index_df = pd.read_csv(index_file)
    
    # REMOVE ALL SPACES FROM COLUMN NAMES
    index_df.columns = index_df.columns.str.strip()
    
    # Fix date
    index_df["Date"] = pd.to_datetime(index_df["Date"], format="mixed", dayfirst=True, errors="coerce")
    
    # Rename KSE100 column if needed
    if "KSE 100 Index" in index_df.columns:
        index_df = index_df.rename(columns={"KSE 100 Index": "KSE100_Close"})

    print("✔ Loaded index data:", index_df.shape)
    print("Index columns:", index_df.columns)



    # ---------------------------
    # 4. MERGE COMPANY DATA WITH INDEX
    # ---------------------------
    merged_df = company_df.merge(
        index_df[["Date", "KSE100_Close"]],
        on="Date",
        how="left"
    )

    # Fill missing KSE100 values
    merged_df["KSE100_Close"] = merged_df["KSE100_Close"].ffill().bfill()

    print("✔ Merged with index")



    # ---------------------------
    # 5. MERGE WITH SECTOR DATA
    # ---------------------------
    merged_df = merged_df.merge(sector_df, on="Ticker", how="left")

    print("✔ Merged with sector info")



    # ---------------------------
    # 6. SAVE FINAL OUTPUT
    # ---------------------------
    os.makedirs("final_output", exist_ok=True)
    output_file = "final_output/psx_final_dataset.csv"

    merged_df.to_csv(output_file, index=False)

    print(f"🎉 ETL Completed! Final dataset saved as: {output_file}")

    return merged_df



# ---------------------------
# RUN PIPELINE
# ---------------------------
final_df = run_psx_etl()
final_df.head()
