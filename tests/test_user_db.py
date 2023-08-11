from src.user_db import User


def test_add_user(test_db):
    new_user = User('John', 30, 'john@ukr.net')
    test_db.add_user(new_user)

    result = test_db.fetch_all('SELECT * FROM users WHERE email = ?',
                               (new_user.email,))
    assert len(result) > 0, "User is not added"


def test_delete_user(test_db):
    new_user = User('John1', 32, 'john1@ukr.net')
    test_db.add_user(new_user)

    added_user = test_db.fetch_all('SELECT id FROM users WHERE email = ?',
                                   (new_user.email,))[0]
    added_user_id = added_user[0]

    test_db.delete_user_by_id(added_user_id)

    result = test_db.fetch_all('SELECT * FROM users WHERE email = ?',
                               (new_user.email,))
    assert len(result) == 0, "User is not deleted"

    # assert len(result) == 0, "Not added user"


def test_get_user_by_id(test_db):
    new_user = User('John1', 32, 'john1@ukr.net')
    test_db.add_user(new_user)

    added_user = test_db.fetch_all('SELECT id FROM users WHERE email = ?',
                                   (new_user.email,))[0]
    added_user_id = added_user[0]

    user_from_db = test_db.get_user_by_id(added_user_id)

    # print(user_from_db)
    assert new_user.email == user_from_db.email


def test_get_all_users(test_db):
    new_user_1 = User('John1', 32, 'john1@ukr.net')
    test_db.add_user(new_user_1)

    new_user_2 = User('John2', 29, 'john2@ukr.net')
    test_db.add_user(new_user_2)

    added_users = test_db.get_users()

    assert (new_user_1.email == added_users[0].email) and \
           (new_user_2.email == added_users[1].email)


def test_update_user(test_db):
    new_user = User('John1', 32, 'john1@ukr.net')
    test_db.add_user(new_user)

    user_from_db = test_db.get_user_by_id(1)
    new_user_name = "Super John"
    user_from_db.name = new_user_name

    test_db.update_user_by_id(user_from_db)
    updated_user = test_db.get_user_by_id(1)

    assert new_user_name == updated_user.name
