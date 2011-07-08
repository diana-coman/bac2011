#!/usr/bin/env python
import logging
import logging.config
import sqlite3
import sys

from elev import Elev
from utils import get_data_from_file

def create_table(conn, tbl_name):
    f = ('%s %s' % (i, 'numeric(4,2)' if '_scris' in i else 'varchar(100)')
            for i in Elev._fields)
    conn.execute('CREATE TABLE %s (%s)' % (tbl_name, ",".join(f)))

def main():
    con = sqlite3.connect('/tmp/bac2011.sqlite',
            detect_types=sqlite3.PARSE_DECLTYPES)
    create_table(con, 'rezultate')
    insert_query = 'INSERT INTO rezultate VALUES(%s)' % \
            (','.join('?'*len(Elev._fields)),)

    with con:
        with open(sys.argv[1], 'rt') as f:
            for i in get_data_from_file(f):
                con.execute(insert_query, i)

if __name__ == '__main__':
    logging.config.fileConfig('logging.ini')
    main()
