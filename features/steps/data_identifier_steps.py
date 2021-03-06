import random
import string

from behave import given, when, then, register_type
from features.support import database_helper as database_helper
from features.support import custom_type_parser
from packit_app.table_elements import User
from packit_app.table_fields import Username, GenderID, UserID

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)

helper = database_helper.DatabaseHelper()


@then(u'the application contains {amount:d} users')
def check_proper_amount_of_users_exists(context, amount):
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount


@given(u'the application contains a {gender:Gender} user '
       u'named {username:Username}')
def check_users_table_contains_certain_user(context, gender, username):
    # clear_users_table(context)
    context.user_table.clean_all_content()
    create_new_user(context, gender=gender, username=username)
    context.gender_id = GenderID(context.gender_table.get_primary_key(gender))
    user_data = context.user_table.get_matching_elements(context.gender_id,
                                                         username)
    assert len(user_data) == 1, "Requested user does not exist!"
    context.username = username
    context.user_id = UserID(context.user_table.get_primary_key(
            User(username, context.gender_id)))


@then(u'there is only one {gender:Gender} user named {username:Username} '
      u'in the application')
@then(u'the application contains a {gender:Gender} user '
      u'named {username:Username}')
def check_user_does_exist_once(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    user_data = context.user_table.get_matching_elements(
            GenderID(gender_id), username)
    assert len(user_data) > 0, \
        "{0} user named {1} does not exists".format(gender.value, username)
    assert len(user_data) < 2, \
        "{0} user named {1} exists more than once".format(gender.value,
                                                          username)


@then(u'there is no {gender:Gender} user named {username:Username} '
      u'in the application')
def check_user_does_not_exist(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    user_data = context.user_table.get_matching_elements(
            GenderID(gender_id), username)
    assert user_data == [], "User is not suppose to exist in users table"


# @given(u'the application contains no users')
# def clear_users_table(context):
#     context.user_table.clean_all_content()
#     content = context.user_table.get_matching_elements()
#     assert content == [], "User table was not cleared!"


@when(u'a new {gender:Gender} user named {username:Username} is created')
def create_new_user(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    context.user_id = context.user_table.add_element(
            User(username=username, gender_id=GenderID(gender_id)))
    user_data = context.user_table.get_matching_elements(
            username, GenderID(gender_id))
    assert len(user_data) == 1, "User was supposed to be added, but wasn't."


@when(u'{amount:d} individual new users are created')
def create_multiple_random_users(context, amount: int):
    for i in range(amount):
        name = Username(''.join(
                random.choices(string.ascii_lowercase + string.digits, k=10)))
        gender_id = random.choice([GenderID(1), GenderID(2)])
        context.user_table.add_element(
                User(username=name, gender_id=gender_id))


@when(u'the {gender:Gender} user named {username:Username} is deleted')
def delete_user(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    context.user_table.delete_element(
            User(username=username, gender_id=GenderID(gender_id)))
    user_data = context.user_table.get_matching_elements(
            GenderID(gender_id), username)
    assert len(user_data) == 0, "User has not been deleted!"
