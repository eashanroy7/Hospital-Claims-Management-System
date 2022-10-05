from config.database import DBConnection
from models.employee import UserModel

class EmployeeRepository:
    ''' Manage all queries about employees '''
    def __init__(self, db):
        self.db = db

    def find_doctor_id(self, info: str):
        doctor = self.db.session\
            .query(UserModel.id)\
            .filter(
                UserModel.name == str(info),
                UserModel.type == 'doctor'
            ).first()
        return doctor

    def register_user(self, name, user, password):
        with DBConnection() as db:
            user_info = UserModel(
                name=name,
                user=user,
                password=password,
                type='attendant'
            )
            db.session.add(user_info)
            db.session.commit()

    def find_by_login(self, user):
        # Está sendo usado no registro
        with DBConnection() as db:
            query = db.session\
                .query(UserModel.user)\
                .filter(UserModel.user == user)\
                .first()
            return query

    def find_password(self, user):
        # vai ser utilizado no login
        # vai encontrar o user e o password com base no user
        with DBConnection() as db:
            query = db.session\
                .query(UserModel.password)\
                    .filter(UserModel.user == user)\
                    .first()
            return query
