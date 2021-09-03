import peewee
import os

db_dir = '/var/opt/keys'

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db = peewee.SqliteDatabase(db_dir + '/keys.db')


class Character(peewee.Model):
    character_name = peewee.CharField()
    character_realm = peewee.CharField()
    character_class = peewee.CharField(null=True)
    character_item_level = peewee.FloatField(null=True)
    dungeon_name = peewee.CharField(null=True)
    dungeon_level = peewee.IntegerField(null=True)
    dungeon_reset_time = peewee.IntegerField(null=True)

    class Meta:
        primary_key = peewee.CompositeKey('character_name', 'character_realm')
        database = db


db.connect()
db.create_tables([Character])
db.close()
