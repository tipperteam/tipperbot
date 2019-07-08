import os
from tipperbot.utils.env import get_property
from tipperbot.utils.log import get_logger
import pandas as pd
from enum import Enum

class Tables(str,Enum):
    USER = "users",
    WALLET = "wallet",
    CUR_SLIP = "current_slip"

DATA_DIR = get_property("DATA_DIR")

logger = get_logger()

db = {}

def load_tables():
    for table_file in os.listdir(DATA_DIR):
        table = table_file[:-len(".parquet")]
        logger.info("Importing table {}".format(table))
        db[table] = pd.read_parquet(os.path.join(DATA_DIR,table_file))
        logger.info("\tImported {} records.".format(len(db[table])))

def persist_tables(tables=None):
    if tables is None:
        tables = list(db.keys())
    if type(tables) is not list:
        tables = [tables]
    for t in tables:
        logger.info("Persisting table {}.".format(t))
        db[t].to_parquet(os.path.join(DATA_DIR,"{}.parquet".format(t)))
        logger.info("\tDone")

def clear_db():
    logger.warning("Clearing database.")
    for table in db:
        db[table] = pd.DataFrame(columns=db[table].columns)
    logger.info("Database is empty!")

def append(table, instance):
    if table not in db:
        db[table] = pd.DataFrame(columns=list(instance.keys()))
    db[table] = db[table].append(instance,ignore_index=True)
    persist_tables(table)

def get(table):
    tb =  db.get(table,None)
    if tb is not None:
        tb = tb.copy()
    return tb