from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class ExocolonistArchipelagoOptions:
    exocolonist_include_helios_friends: ExocolonistIncludeHeliosFriends
    exocolonist_include_helios_dates: ExocolonistIncludeHeliosDates

class ExocolonistGame(Game):
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW
    ]

    is_adult_only_or_unrated = False

    options_cls = ExocolonistArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Save Tammy",
                data={},
            )
        ]

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Reach friendship level 20 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 20 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 2),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 40 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 40 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 2),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 60 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 60 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 2),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 80 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Reach friendship level 100 with FRIEND",
                data = {
                    "FRIEND": (self.friends, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=3
            ),
        ]


    @staticmethod
    def colors() -> List[str]:
        return [
            "Yellow",
            "Blue",
            "Red"
        ]

    @property
    def include_helios_friends(self) -> bool:
        return bool(self.archipelago_options.exocolonist_include_helios_friends.value)

    @property
    def include_helios_dates(self) -> bool:
        return bool(self.archipelago_options.exocolonist_include_helios_dates.value)

    @functools.cached_property
    def stratos_friends() -> List[str]:
        return [
            "Anemone",
            "Cal",
            "Tammy",
            "Tangent"
            "Dys",
            "Marz"
        ]

    @functools.cached_property
    def helios_friends() -> List[str]:
        return [
            "Vace",
            "Nomi",
            "Rex",
            "Sym"
        ]

    def friends(self) -> List[str]:
        friends: List[str] = self.stratos_friends[:]

        if self.include_helios_friends:
            friends.extend(self.helios_friends[:])

        return sorted(friends)

class ExocolonistIncludeHeliosFriends(Toggle):
    """
    Indicates whether to include Helios characters as friendship checks.
    """

    display_name = "Exocolonist Include Helios Friends"

class ExocolonistIncludeHeliosDates(Toggle):
    """
    Indicates whether to include Helios characters as date checks.
    """

    display_name = "Exocolonist Include Helios Dates"