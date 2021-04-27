#!/usr/bin/env python
"""csv2sqlite
Convert csvs to sqlite tables. Works with new or existing databases and
new or existing tables.
Usage:
    csv2sqlite CSV DATABASE TABLENAME
    csv2sqlite (-h | --help)
    csv2sqlite --version
Options:
    -h --help     Show this screen.
    --version     Show version.
"""

#csv2sqlite data.csv database.db tablename
#csv2sqlite houses.csv sqlite3.db houses

from __future__ import print_function
import sqlite3
import csv
import os
from decimal import Decimal, InvalidOperation
from docopt import docopt

def data_generator(csv_path):
    with open(csv_path, 'rt',encoding="utf-8") as fh:
        cr = csv.reader(fh, delimiter=',', quotechar='"')
        next(cr)  # skip header
        for row in cr:
            yield row


def create_table_sql(csv_path, table):
    with open(csv_path, 'rt',encoding="UTF-8") as fh:
        cr = csv.reader(fh, delimiter=',', quotechar='"')
        header = next(cr)
        cols = []
        # just check first row
        for i, val in enumerate(next(cr)):
            key = header[i]

            # special case, stupid headers on fvsclimattrs
            if key.startswith("20") and key.endswith("PST"):
                key = "StandID"

            try:
                Decimal(val)
                nt = 'REAL'
                try:
                    int(val)
                    nt = "INTEGER"
                except ValueError:
                    pass
            except InvalidOperation:
                # string
                nt = "TEXT"
            cols.append('"%s" %s' % (key, nt))
        sql = "CREATE TABLE %s(%s);" % (table, ',\n'.join(cols))
    print(sql)
    return sql


if __name__ == "__main__":
    args = docopt(__doc__, version='1.0')

    INCSV = args['CSV']
    DATABASE = args['DATABASE']
    TABLE = args['TABLENAME']

    if not os.path.exists(INCSV):
        raise Exception("%s doesn't exist" % INCSV)

    if not os.path.exists(DATABASE):
        print("WARNING: Database %s doesn't exist; creating new db" % DATABASE)

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    table_query = """SELECT name FROM sqlite_master WHERE type='table' AND name='%s';""" % (TABLE,)
    cur.execute(table_query)
    table_exists = len(cur.fetchall())

    if table_exists == 0:
        print("Creating table")
        sql = create_table_sql(INCSV, TABLE)
        cur.execute(sql)
    else:
        print("Table exists; Trying to insert into existing table")

    columns_query = "PRAGMA table_info(%s)" % TABLE
    cur.execute(columns_query)
    numcol = len(cur.fetchall())

    print("Inserting data into table")
    sql = "INSERT INTO %s VALUES (%s);" % (TABLE, ",".join("?"*numcol))
    cur.executemany(sql, data_generator(INCSV))

    con.commit()
    cur.close()