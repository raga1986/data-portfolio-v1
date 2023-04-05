import psycopg2
import pandas as pd

# connect to redshift

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password): # this method connects to redshift and extracts customer transactions data.
    connect=connect_to_redshift(dbname, host, port, user, password)
    query = """
    select ot.*,
           case when sd.description = '?' or sd.description is null then 'Unknown' 
           else sd.description 
           end as description
    from bootcamp1.online_transactions ot
    left join bootcamp1.stock_description sd on ot.stock_code = sd.stock_code
    where quantity > 0
    and customer_id<> ''
    and ot.stock_code not in ('BANK CHARGES','POSTAGE','D','M','CRUK')
    """

    online_trans = pd.read_sql(query,connect)
    print(f"The number of invoices extracted is {online_trans.shape[0]}")

    return online_trans




