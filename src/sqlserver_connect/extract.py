import os
import pyodbc
import pandas as pd

server = 'localhost'
database = 'Chinook'
username = 'sa'
password = 'YourStrong@Passw0rd'
driver = '{ODBC Driver 18 for SQL Server}'

# DSN connection string
conn_str = f"""
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    Encrypt=no;
"""

# tao ket noi
conn = pyodbc.connect(conn_str)
print("✅ Kết nối SQL Server thành công.")

# tao thu muc output
output_dir = 'data/csv'
os.makedirs(output_dir, exist_ok=True)

# Danh sach cac bang can trich xuat
tables = [
    'Album', 'Artist', 'Customer', 'Employee',
    'Genre', 'Invoice', 'InvoiceLine',
    'MediaType', 'Playlist', 'PlaylistTrack', 'Track'
]

# trich xuat tung bang ra csv
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    file_path = os.path.join(output_dir, f"{table}.csv")
    df.to_csv(file_path, index=False)
    print(f"Đã lưu bảng {table} → {file_path}")

conn.close()
print("Hoàn tất quá trình extract.")
