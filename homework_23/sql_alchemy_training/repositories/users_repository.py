from sqlalchemy import delete
from homework_23.sql_alchemy_training.models.user import User
from homework_23.sql_alchemy_training.session import session


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        result = self.__session.query(User).all()
        for unit in result:
            print(unit)

    def add_one(self, user: User):
        self.__session.add(user)
        self.__session.commit()

    def del_one_by_email(self, user_email: str) -> None:
        action = delete(User).where(User.email == user_email).\
            execution_options(synchronize_session='fetch')
        self.__session.execute(action)
        self.__session.commit()

    def update_by_id(self, user_id: str, column: str, user_email: str) -> None:
        self.__session.query(User).filter(User.id == user_id).update(
            {column: user_email}, synchronize_session='fetch'
        )
        self.__session.commit()
