from typing import Dict
from flask_login import UserMixin
from psycopg2 import sql
from BandTinder import login_manager, conn, cur


class ModelUserMixin(dict, UserMixin):
    @property
    def id(self):
        return self.pk


@login_manager.user_loader
def load_user(user_id):
    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE pk = %s
    """)
    cur.execute(user_sql, (int(user_id),))
    user_data = cur.fetchone()
    
    return User(user_data) if user_data else None


class User(ModelUserMixin):
    def __init__(self, user_data: Dict):
        super(User, self).__init__(user_data)
        self.pk = user_data.get('pk')
        self.email = user_data.get('email')
        self.full_name = user_data.get('full_name')
        self.user_name = user_data.get('user_name')
        self.password = user_data.get('password')
        self.birth_date = user_data.get('birth_date')
        self.located_in = user_data.get('located_in')