from behave import given, when, then, register_type

from features.support import custom_type_parser
from packit_app.table_elements import User, UserGarmentSetting, Garment
from packit_app.table_fields import UserID, UserGarmentSettingsID, GarmentID

users = []

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)


# register_type(UserGarmentSetting=custom_type_parser.parse_user_garment_setting)

# REMOVE & ADD NEW

@when(u'{clothing_type} is added to {gender} user {name}')
def add_singular_clothing_piece_to_user(context, clothing_type, gender, name):
    raise NotImplementedError(u'STEP: When scarf is added to user <name>')
    # print("adding new clothing piece to user...")


@when(u'{clothing_type} are added to user {name}')
def add_plural_clothing_piece_to_user(context, clothing_type, name):
    raise NotImplementedError(u'STEP: When scarf is added to user <name>')


# (RE)SET VALUE

@when(u'quantity for {clothing_type} is set to {quantity} for each '
      u'temperature')
def set_clothing_piece_quantity_all_conditions(context, clothing_type,
                                               quantity):
    # print("setting clothing type quantity equally for each condition ...")
    raise NotImplementedError()


@when(u'quantity for {clothing_type} is set to {quantity} for {condition}')
def set_clothing_piece_quantity_single_condition(context, clothing_type,
                                                 quantity, condition):
    # print("setting quantity for clothing type for single condition ...")
    raise NotImplementedError()


# CHECK ENTRY
@given(u'user {username:Username} has an entry for {garment_name:GarmentName}')
def check_user_clothing_entry_exists(context, username, garment_name):
    context.garment = Garment(context.gender_id, garment_name)
    context.username = username
    context.user_id = UserID(context.user_table.get_matching_element(
            User(username, context.gender_id))[UserID.column_name])
    context.garment_id = GarmentID(
            context.garment_table.add_element(context.garment))
    user_garment_setting_id = context.user_garment_settings_table.add_element(
            UserGarmentSetting(context.user_id, context.garment_id))
    context.user_garment_setting_id = UserGarmentSettingsID(
            user_garment_setting_id)

    result = context.user_garment_settings_table.get_matching_elements(
            context.user_garment_setting_id)

    assert len(result) == 1, "Cannot find user garment settings in the table"


@then(u'{clothing_piece} is added to {name} with {quantity} for each '
      u'temperature')
def check_clothing_piece_quantity_all_temperatures(context, clothing_piece,
                                                   name, quantity):
    # print("checking clothing type quantity set equally for all conditions
    # ...")
    raise NotImplementedError()


@then(u'user {name} has set a quantity of {quantity} for {condition}')
def check_clothing_piece_quantity_single_condition(context, name, quantity,
                                                   condition):
    # print("checking clothing type quantity set for single condition ...")
    raise NotImplementedError()
