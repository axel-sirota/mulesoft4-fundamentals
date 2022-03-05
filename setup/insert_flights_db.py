import pandas as pd
from sqlalchemy import create_engine
from config import host, port, database, user, password

conn_str = f"postgresql://{user}:{password}@{host}/{database}"
print(conn_str)
engine = create_engine(conn_str)
with open("setup/flights.csv", 'r') as file:
    flights = pd.read_csv(file)
print(flights)
aa_flights = flights[flights.AIRLINE == "AA"]
dl_flights = flights[flights.AIRLINE == "DL"]
aa_flights.to_sql('american_flights', con=engine, index=True, index_label='id', if_exists='replace')
dl_flights.to_sql('delta_flights', con=engine, index=True, index_label='id', if_exists='replace')
