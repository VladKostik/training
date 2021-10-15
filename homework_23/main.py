from homework_23 import UsersRepository, User

if __name__ == '__main__':
    users_repository = UsersRepository()
    users_repository.get_all()
    users_repository.add_one(User(id='A005', name='Jameson', age=18,
                                  email='jameson@mail.com'))
    # users_repository.del_one_by_email('g_goose@mail.com')
    users_repository.update_by_id('A001', 'name', 'Jackie')
    users_repository.get_all()
