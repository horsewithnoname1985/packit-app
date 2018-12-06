from behave import given, when, then
import random
import string

from features.support import database as database_helper
from packit_app.elements import User, Name, Male

helper = database_helper.DatabaseHelper()


# DEFINING STATES

@given(u'the application contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_all_elements()
    assert content == []
    print(str(content))


@given(u'the application contains a {gender} user named {name}')
def user_must_exist_after_creation(context, gender, name):
    context.user_table.clean_all_content()
    context.user = User(name=name, gender=gender)
    create_new_user(context, gender, name)
    user_does_exist(context, gender, name)


# FOR REMOVING & ADDING NEW ENTRIES

@when(u'the {gender} user named {name} is deleted')
def delete_user(context, name, gender):
    context.user = User(name=name, gender=gender)
    context.user_table.delete_element(context.user)


@when(u'a new {gender} user named {name} is created')
def create_new_user(context, gender, name):
    context.user = User(name=name, gender=gender)
    added_new_user = context.user_table.add_element(context.user)
    if not added_new_user:
        context.user_table.raised_errors.append('UserAlreadyExisting')
    # context.user_settings_table = create_user_settings_table(context.user)


@when(u'{amount:d} individual new users are created')
def create_multiple_random_users(context, amount: int):
    for i in range(amount):
        name = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=10))
        gender = random.choice(['male', 'female'])
        context.user = User(name=name, gender=gender)

        context.user_table.add_element(context.user)


@when(
    u'a quantity of {quantity:f} is assigned to all predefined clothes and conditions')
def set_all_default_clothes_quantity(context, quantity: float):

    raise NotImplementedError(
        u'STEP: When a quantity of <quantity> is assigned to all predefined clothes and conditions')


# FOR CHECKING ENTRIES

@then(u'the application contains a {gender} user named {name}')
def user_does_exist(context, gender, name):
    # user_data = context.user_table.get_single_element(
    #     User(name=name, gender=gender))
    # user_data = context.user_table.get_elements(
    #     Name.get_query(name), Male.get_query())
    # user_data = context.user_table.get_elements(
    #     name=name, gender=gender)
    user_data = context.user_table.get_elements(User(name=name, gender=gender)
                                                .get_default_values())
    assert user_data != {}, "User does not exist in users table"
    helper.print_table(context.user_table.table_name)


@then(u'there is no {gender} user named {name} in the application')
def user_does_not_exist(context, gender, name):
    user_data = context.user_table.get_single_element(
        User(name=name, gender=gender))
    assert user_data == {}, "User is not suppose to exist in users table"
    helper.print_table(context.user_table.table_name)


@then(u'there is only one {gender} user named {name} in the application')
def user_does_exist_once(context, gender, name):
    user_does_exist(context, gender, name)


@then(u'the application contains {amount:d} users')
def step_impl(context, amount):
    user_data = context.user_table.get_all_elements()
    assert len(user_data) == amount


@then(
    u'a quantity of {quantity:f} is assigned for all default clothes of the {gender] user named {name}')
def step_impl(context, gender, name):
    raise NotImplementedError(
        u'STEP: Then a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>')
