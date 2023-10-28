from validators import validate_yes_no_input


def get_user_input():
    battery_level = int(input("Please enter current battery level: "))

    command_input_message = (
        "Pick an option: \n"
        + "(1): Spot Cleaning\n"
        + "(2): General Cleaning\n"
        + "(3): Do Nothing\n"
        + "(4): Shutdown\n"
        + "Your choice: "
    )

    command_input = int(input(command_input_message))
    while command_input < 1 or command_input > 4:
        command_input = int(input(command_input_message))

    spot_cleaning, general_cleaning = False, False
    match (command_input):
        case 1:
            spot_cleaning = True
            general_cleaning = False
        case 2:
            spot_cleaning = False
            general_cleaning = True
        case 3:
            spot_cleaning = False
            general_cleaning = False

    is_spot_dirty = False
    if general_cleaning:
        is_spot_dirty_input = input("Is Current Spot Dusty? [y/n] ")
        while validate_yes_no_input(is_spot_dirty_input):
            is_spot_dirty_input = input(
                "Invalid response! Is Current Spot Dusty? [y/n] "
            )
        is_spot_dirty = is_spot_dirty_input == "y"

    return battery_level, spot_cleaning, general_cleaning, is_spot_dirty
