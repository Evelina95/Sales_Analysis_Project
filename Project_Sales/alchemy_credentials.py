from sqlalchemy import create_engine
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# --------------------------------

username = "vartotojas1"
password = "yt4#fr!Wq1ev1Uo0iu%l"
host = "213.159.46.172"
port = 21898
database = "Evelina"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}", echo=False
)