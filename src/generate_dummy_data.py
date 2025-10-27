import random
from datetime import date, timedelta, datetime
import os
import csv

# Transportasi "estimation_days": [1, 2, 3]
expense_categories = [
    {
        "name": "Transportasi",
        "subcategories": [
            {"name": "Bensin", "prices": [10000, 15000, 20000]},
            {"name": "Parkir", "prices": [2000, 5000, 10000]},
            {"name": "Tol", "prices": [8000, 15000, 25000]},
            {"name": "Transportasi Online", "prices": [15000, 25000, 40000]},
            {"name": "Tiket Umum", "prices": [5000, 10000, 20000]}
        ]
    },
    {
        "name": "Makanan & Minuman",
        "subcategories": [
            {"name": "Makan di Luar", "prices": [15000, 25000, 40000],},
            {"name": "Belanja Harian", "prices": [50000, 75000, 100000],},
            {"name": "Minuman", "prices": [5000, 10000, 20000]},
            {"name": "Cemilan", "prices": [5000, 15000]}
        ]
    },
    {
        "name": "Kebutuhan Rumah Tangga",
        "subcategories": [
            {"name": "Listrik", "prices": [50000, 100000, 200000]},
            {"name": "Internet", "prices": [150000, 300000]},
            {"name": "Peralatan Rumah", "prices": [25000, 50000, 100000]}
        ]
    },
    {
        "name": "Hiburan & Gaya Hidup",
        "subcategories": [
            {"name": "Streaming", "prices": [50000, 100000]},
            {"name": "Game", "prices": [10000, 50000, 100000]},
            {"name": "Hobi", "prices": [25000, 75000, 150000]},
            {"name": "Jalan-jalan", "prices": [100000, 300000, 500000]}
        ]
    }
]

files = os.listdir("data")
filter_files = [f for f in files if f.startswith("data_") and f.endswith(".csv")]
number_files = [f.split("_")[1].split(".")[0] for f in filter_files] if filter_files else []
last_file = f"data_{max(number_files)}.csv" if number_files else None
next_file = f"data_{int(max(number_files))+1}.csv" if last_file else "data_1.csv"

if not last_file:
    next_day = date.today()
else:
    with open(f"data/{last_file}", "r") as f:
        reader = csv.DictReader(f)
        dates = [datetime.strptime(row["date"], "%Y-%m-%d").date() for row in reader]
        next_day = max(dates) + timedelta(days=1)
        
    
dates = [next_day]

amount_dates = random.randint(0,2)
if  amount_dates != 0:
    for i in range(1, amount_dates+1):
        dates.append(next_day+timedelta(days=i))

data = []
for date in dates:
    for i in range(random.randint(3,5)):
        category = random.choice(expense_categories)
        subcategory = random.choice(category["subcategories"])
        price = random.choice(subcategory["prices"])
        #estimation_day = random.choice(subcategory.get("estimation_days")) if subcategory.get("estimation_days") else 0
        
        data.append({
            "date": date,
            "category": category["name"],
            "subcategory": subcategory["name"],
            "price": price,
            #"estimation_day": estimation_day,
        })
        
        with open(f"data/{next_file}", mode="w") as f:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)

print(f"File {next_file} berhasil di buat")