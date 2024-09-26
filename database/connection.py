import psycopg2 as dbdriver
from config import settings
import logging

def execute_query(vql):
    cnxn_str = (
        f"user={settings.DENODO_USER} password={settings.DENODO_PASSWORD} "
        f"host={settings.DENODO_HOST} dbname={settings.DENODO_DATABASE} port={settings.DENODO_PORT}"
    )
    try:
        with dbdriver.connect(cnxn_str) as cnxn:
            with cnxn.cursor() as cur:
                cur.execute(vql)
                results = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
        return results, columns
    except dbdriver.Error as e:
        logging.error(f"Erro ao executar a consulta: {e}")
        raise