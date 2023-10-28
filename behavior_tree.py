#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

from bt_library import Timer, Selection

from conditions.battery_less_than_30 import BatteryLessThan30
from globals import GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR
from decorators import UntilFail
from composites import Sequence, Priority
from conditions import FlagCheck
from tasks import Dock, FindHome, GoHome, CleanSpot, DoneSpot, CleanFloor, DoneGeneral, DoNothing

# Instantiate the tree according to the assignment.

########################################################################################################################

battery_check_sequence = Sequence([BatteryLessThan30(), FindHome(), GoHome(), Dock()])
spot_cleaning_sequence = Sequence([FlagCheck(SPOT_CLEANING), Timer(20, CleanSpot()), DoneSpot()])
dusty_spot_cleaning_sequence = Sequence([FlagCheck(DUSTY_SPOT_SENSOR), Timer(35, CleanSpot())])
general_cleaning_priority = Priority([dusty_spot_cleaning_sequence, UntilFail(CleanFloor())])
general_cleaning_sequence = Sequence([FlagCheck(GENERAL_CLEANING), Sequence([general_cleaning_priority, DoneGeneral()])])
cleaning_selection = Selection([spot_cleaning_sequence, general_cleaning_sequence])

tree_root = Priority([battery_check_sequence, cleaning_selection, DoNothing()])