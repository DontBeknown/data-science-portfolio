"""Download the source datasets into the local, git-ignored data directory."""

from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import shutil


ROOT = Path(__file__).resolve().parent
LA_QUERY = urlencode({
    "$select": "dr_no,date_occ,time_occ,area_name,status_desc",
    "$where": (
        "date_occ >= '2023-01-01T00:00:00' AND date_occ < '2024-01-01T00:00:00' "
        "AND area_name in ('Central','Hollywood','Pacific')"
    ),
    "$order": "dr_no",
    "$limit": 50000,
})
SOURCES = {
    "superstore.xlsx": (
        "https://raw.githubusercontent.com/PacktPublishing/"
        "Getting-Started-with-Tableau-2019.2/master/Chapter03/Sample-Superstore.xlsx"
    ),
    "la-crime-2023.csv": f"https://data.lacity.org/resource/2nrs-mtv8.csv?{LA_QUERY}",
    "telco-churn.csv": (
        "https://raw.githubusercontent.com/IBM/watsonx-ai-samples/master/"
        "cpd4.5/data/customer_churn/WA_FnUseC_TelcoCustomerChurn.csv"
    ),
}


def main():
    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    for name, url in SOURCES.items():
        destination = data_dir / name
        if destination.exists():
            print(f"Cached {name}")
            continue
        pending = destination.with_suffix(destination.suffix + ".part")
        try:
            with urlopen(url, timeout=60) as response, pending.open("wb") as output:
                shutil.copyfileobj(response, output)
            pending.replace(destination)
        finally:
            pending.unlink(missing_ok=True)
        print(f"Downloaded {name}")


if __name__ == "__main__":
    main()
