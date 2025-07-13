import pandas as pd
from sqlalchemy import create_engine
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
# Read csv file
df = pd.read_csv("sales_data.csv")

# Show first few rows of the dataframe
print(df.head())


username = "root"
password = "Pajuodele95@"
host = "127.0.0.1"
port = 3306
database = "Pardavimai"


engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}", echo=False
)