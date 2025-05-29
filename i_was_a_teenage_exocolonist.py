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
    exocolonist_include_difficult_dating: ExocolonistIncludeDifficultDating

class ExocolonistGame(Game):
    name = "I Was A Teenage Exocolonist"
    
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
            ),
            GameObjectiveTemplate(
                label="Save Tobin",
                data={},
            ),
            GameObjectiveTemplate(
                label="Save Eudot",
                data={},
            ),
            GameObjectiveTemplate(
                label="Save Mom",
                data={},
            ),
            GameObjectiveTemplate(
                label="Save Dad",
                data={},
            ),
            GameObjectiveTemplate(
                label="Delete previous choices",
                data={},
            ),
        ]

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        return [
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
            GameObjectiveTemplate(
                label="Date DATE",
                data = {
                    "DATE": (self.dates, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=3
            ),

            # Everything below here is weighted 1 higher because there are so many options above
            # Pets
            GameObjectiveTemplate(
                label="Find the PET pet",
                data = {
                    "PET": (self.pets, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Find the PET pets",
                data = {
                    "PET": (self.pets, 2),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Find the PET pets",
                data = {
                    "PET": (self.pets, 3),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Find the PET pets",
                data = {
                    "PET": (self.pets, 4),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Find 2 pets",
                data = {
                },
                is_time_consuming = False,
                is_difficult = True,
                weight=2
            ),


            # Skills
            GameObjectiveTemplate(
                label="Max a single COLOR skill",
                data = {
                    "COLOR": (self.colors, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=6
            ),
            GameObjectiveTemplate(
                label="Max two COLOR skills",
                data = {
                    "COLOR": (self.colors, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Max the SKILL skill",
                data = {
                    "SKILL": (self.skills, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=6
            ),
            GameObjectiveTemplate(
                label="Receive perk #1 in SKILL",
                data = {
                    "SKILL": (self.skills, 2),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=6
            ),
            GameObjectiveTemplate(
                label="Receive perk #1 in SKILL",
                data = {
                    "SKILL": (self.skills, 3),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=5
            ),
            GameObjectiveTemplate(
                label="Receive perk #2 in SKILL",
                data = {
                    "SKILL": (self.skills, 2),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight=4
            ),
        ]


    @staticmethod
    def colors() -> List[str]:
        return [
            "Yellow",
            "Blue",
            "Red"
        ]

    @staticmethod
    def skills() -> List[str]:
        return [
            "Empathy",
            "Creativity",
            "Bravery",
            "Persuasion",
            "Reasoning",
            "Organization",
            "Engineering",
            "Biology",
            "Toughness",
            "Perception",
            "Animals",
            "Combat"
        ]
    
    @staticmethod
    def pets() -> List[str]:
        return [
            "Vriki",
            "Hopeye",
            "Unisaur",
            "Robot"
        ]

    @property
    def include_helios_friends(self) -> bool:
        return bool(self.archipelago_options.exocolonist_include_helios_friends.value)

    @property
    def include_helios_dates(self) -> bool:
        return bool(self.archipelago_options.exocolonist_include_helios_dates.value)

    @property
    def include_difficult_dating(self) -> bool:
        return bool(self.archipelago_options.exocolonist_include_difficult_dating.value)

    @functools.cached_property
    def stratos_friends(self) -> List[str]:
        return [
            "Anemone",
            "Cal",
            "Tammy",
            "Tangent",
            "Dys",
            "Marz",
            "Sym"
        ]

    @functools.cached_property
    def helios_friends(self) -> List[str]:
        return [
            "Vace",
            "Nomi",
            "Rex",
            "Sym"
        ]

    @functools.cached_property
    def stratos_dates(self) -> List[str]:
        return [
            "Anemone",
            "Tangent",
            "Dys",
            "Marz",
            "Sym"
        ]

    @functools.cached_property
    def stratos_difficult_dates(self) -> List[str]:
        return [
            "Cal",
            "Tammy",
        ]

    @functools.cached_property
    def helios_dates(self) -> List[str]:
        return [
            "Vace",
            "Rex",
            "Sym"
        ]

    @functools.cached_property
    def helios_difficult_dates(self) -> List[str]:
        return [
            "Nomi",
        ]

    def friends(self) -> List[str]:
        friends: List[str] = self.stratos_friends[:]

        if self.include_helios_friends:
            friends.extend(self.helios_friends[:])

        return sorted(friends)

    def dates(self) -> List[str]:
        dates: List[str] = self.stratos_dates[:]

        if self.include_helios_dates:
            dates.extend(self.helios_dates[:])
            if self.include_difficult_dating:
                dates.extend(self.helios_difficult_dates[:])
        if self.include_difficult_dating:
            dates.extend(self.stratos_difficult_dates)

        return sorted(dates)

class ExocolonistIncludeHeliosFriends(Toggle):
    """
    Indicates whether to include Helios characters as friendship checks.
    """

    display_name = "Exocolonist Include Helios Friends"

class ExocolonistIncludeDifficultDating(Toggle):
    """
    Indicates whether to include characters that are difficult to date as checks.
    """

    display_name = "Exocolonist Include Difficult Dating"

class ExocolonistIncludeHeliosDates(Toggle):
    """
    Indicates whether to include Helios characters as date checks.
    """

    display_name = "Exocolonist Include Helios Dates"