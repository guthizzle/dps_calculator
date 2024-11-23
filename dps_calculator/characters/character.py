from typing import Dict, Optional
from enum import Enum
from enums.weapon_types import WeaponType
from enums.melee_styles import MeleeStyle
from enums.ranged_styles import RangedStyle
from enums.magic_elements import MagicElements
from stats.gear_stats import GearStats


class Character:
    def __init__(self, levels: Dict[str, int], weapon: Dict[str, int], gear_stats: GearStats, weapon_type: WeaponType, style: Optional[Enum] = None) -> None:
        """
        Base class for shared character logic (Player and NPC)
        
        Args:
            levels (dict): Character's skill levels.
            weapon (dict): Weapon stats
            gear_stats (GearStats): Gear stats
            weapon_type (WeaponType): Type of weapon (Melee, Ranged, Magic).
            style (Enum, optional): Combat style (MeleeStyle, RangedStyle, or MagicElement).
        """
        self.levels = levels
        self.weapon = weapon
        self.gear_stats = gear_stats
        self.weapon_type = weapon_type
        
    def get_accuracy(self) -> int:
        """Calculate the character's accuracy stat based on style and weapon type."""
        if self.weapon_type == WeaponType.MELEE:
            if self.style == MeleeStyle.STAB:
                return self.weapon.get("stabAcc", 0) + self.gear_stats.get("stabAcc", 0)
            elif self.style == MeleeStyle.SLASH:
                return self.weapon.get("slashAcc", 0) + self.gear_stats.get("stabAcc", 0)
            elif self.style == MeleeStyle.CRUSH:
                return self.weapon.get("stabAcc", 0) + self.gear_stats.get("stabAcc", 0)
        elif self.weapon_type == WeaponType.RANGED:
            return self.weapon.get("rangedAcc", 0) + self.gear_stats.get("rangedAcc", 0)
        elif self.weapon_type == WeaponType.MAGIC:
            return self.weapon_type.get("magicAcc", 0) + self.gear_stats.get("magicAcc", 0)
        return 0
    
    def get_strength(self) -> int:
        """Get the character's gear strength based on combat style."""
        if self.weapon_type == WeaponType.MELEE:
            return self.gear_stats.get_stat("meleeStr")
        elif self.weapon_type == WeaponType.RANGED:
            return self.gear_stats.get_stat("rangedStr")
        elif self.weapon_type == WeaponType.MAGIC:
            return self.gear_stats.get_stat("magicStr")
        return 0
    
    
    
    
    
    def calculate_defence_roll(self) -> int: # TODO: add weapon obj here for getting the specific typing
        pass