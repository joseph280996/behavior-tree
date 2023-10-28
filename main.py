#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from behavior_tree import tree_root
from utils import get_user_input
from globals import (
    BATTERY_LEVEL,
    GENERAL_CLEANING,
    SPOT_CLEANING,
    DUSTY_SPOT_SENSOR,
    HOME_PATH,
)

battery_level, spot_cleaning, general_cleaning, is_spot_dirty = get_user_input()

# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(HOME_PATH, "")
current_blackboard.set_in_environment(BATTERY_LEVEL, battery_level)
current_blackboard.set_in_environment(GENERAL_CLEANING, general_cleaning)
current_blackboard.set_in_environment(SPOT_CLEANING, spot_cleaning)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, is_spot_dirty)

done = False
is_all_tasks_done = True
cycle = 0

while not done:
    # Each cycle in this while-loop is equivalent to 1 second time

    # Step 1: Change the environment
    #   - change the battery level
    #   - Simulate the response of the dusty spot sensor
    #   - Simulate user input commands

    cycle += 1
    print(f"\n\nCycle #{cycle}:")

    current_battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, 0)
    current_blackboard.set_in_environment(BATTERY_LEVEL, current_battery_level - 1)

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)
    is_all_tasks_done = not current_blackboard.get_in_environment(
        SPOT_CLEANING, False
    ) and not current_blackboard.get_in_environment(GENERAL_CLEANING, False)

    # Step 3: Determine if your solution must terminate
    if is_all_tasks_done:
        done = True
