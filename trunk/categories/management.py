
from django.db import connection
from django.db.models import signals
from django.dispatch import dispatcher

from categories.models import Category
from categories import models as categories_app

def create_root_node(app, created_models, verbosity,**kwargs):
    if Category in created_models:
        if verbosity >= 2:
            print 'Creating root Category node'
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO %(table)s
            (name, slug, lft, rgt, sort_order)
        VALUES
            ('Root', 'root', 1, 2, 0)
        """ % dict(table=connection.ops.quote_name(Category._meta.db_table)))
signal=signals.post_syncdb
signal.connect(create_root_node, sender=categories_app)
