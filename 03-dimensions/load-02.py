# -*- encoding: utf-8 -*-
"""
Dimensions – Loading
====================

How to load a dimension table from a source table
with SQL CASE statement mapping.

New concept: table columns, CASE SQL statement

"""

import sqlalchemy as sa
import csv


CUSTOMER_TYPE_MAPPING = {
    # FIXME: add example mapping here
}

PRODUCT_TYPE_MAPPING = {
    # FIXME: add another mapping here
}

CONNECTION = "sqlite:///data.sqlite"


def load():
    engine = sa.create_engine(CONNECTION)
    metadata = sa.MetaData(bind=engine)

    table = metadata.Table("customer", reflect=True)

    target_type = sa.case(CUSTOMER_TYPE_MAPPING,
                          else_="unknown")

    selection = [table.c.id, table.c.name, table.c.type]

    source = sa.select(selection, from_obj=table)

    ...

if __name__ == "__main__":
    load()
