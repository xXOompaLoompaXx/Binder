from typing import Dict

from flask_login import UserMixin
from psycopg2 import sql

from BandTinder import login_manager, app, conn, cur


class ModelUserMixin(dict, UserMixin):
    @property
    def id(self):
        return self.pk

@login_manager.user_loader
def load_user(user_id):
    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE pk = %s
    """).format(sql.Identifier('pk'))

    cur.execute(user_sql, (int(user_id),))
    return User(cur.fetchone()) if cur.rowcount > 0 else None


class User(ModelUserMixin):
    def __init__(self, user_data: Dict):
        super(User, self).__init__(user_data)
        self.pk = user_data.get('pk')
        self.full_name = user_data.get('full_name')
        self.user_name = user_data.get('user_name')
        self.password = user_data.get('password')

