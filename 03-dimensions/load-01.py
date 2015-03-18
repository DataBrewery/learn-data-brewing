# -*- encoding: utf-8 -*-
"""
Dimensions – Loading
====================

How to load a dimension table from a CSV file with a simple transformation.


New concepts: select(), iteration, insert(), execution
"""

import sqlalchemy as sa
import csv


MAPPING = {
    # FIXME: add example mapping here
}

CONNECTION = "sqlite:///data.sqlite"


def load():
    engine = sa.create_engine(CONNECTION)
    metadata = sa.MetaData(bind=engine)

    # table = metadata.Table("customer", reflect=True)

    with open("data/customer.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            # do the mapping
            # insert the row
            pass

if __name__ == "__main__":
    load()
