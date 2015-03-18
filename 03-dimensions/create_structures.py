# -*- encoding: utf-8 -*-
"""
Dimensions – Preparation
========================

This script prepares the structures for the module 'Dimensions'. You don't
necessarily have to understand it at this point.

Warning: this script is destructive – rebuilds all structures that are being
used by this module.
"""

import sqlalchemy as sa
import csv


CONNECTION = "sqlite:///data.sqlite"


def create_structures():
    engine = sa.create_engine(CONNECTION)
    md = sa.MetaData(bind=engine)

    # TODO: create tables. drop them if they already exist
    # table = Table("customer", md, ...)
    # table = Table("product", md, ...)
    # table = Table("customer_type_map", md, ...)

    md.create_all()


if __name__ == "__main__":
    create_structures()
