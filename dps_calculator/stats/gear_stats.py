class GearStats:
    def __init__(self):
        """
        Initialize GearStats with default values.
        """
        self.stats = {
            # Offensive stats
            "stabAcc": 0, "slashAcc": 0, "crushAcc": 0,
            "magicAcc": 0, "rangedAcc": 0,
            
            # Defensive stats
            "stabDef": 0, "slashDef": 0, "crushDef": 0,
            "magicDef": 0, "rangedDef": 0,
            
            # Strength stats
            "meleeStr": 0, "rangedStr": 0, "magicStr": 0,
            
            # Defense ratings for NPCs' specific range defences
            "rangedDefLight": 0, "rangedDefStandard": 0, "rangedDefHeavy": 0,
            
            # Elemental weaknesses for NPCs (if applicable)
            "fireWeakness": 0, "waterWeakness": 0, "earthWeakness": 0, "airWeakness": 0,
            
            # Could add other stuff such as flat armour
            
        }

    def set_stat(self, stat_name: str, value: int) -> None:
        """
        Set a specific stat value.

        Args:
            stat_name (str): Name of the stat to set.
            value (int): Value to assign to the stat.
        """
        if stat_name in self.stats:
            self.stats[stat_name] = value
        else:
            raise ValueError(f"Stat '{stat_name}' is not valid.")

    def get_stat(self, stat_name: str) -> int:
        """
        Get a specific stat value.

        Args:
            stat_name (str): Name of the stat to retrieve.
        
        Returns:
            int: Value of the stat.
        """
        return self.stats.get(stat_name, 0)

    def rais_stat(self, stat_name: str, value: int) -> None:
        """
        Add a bonus to an existing stat value.

        Args:
            stat_name (str): Name of the stat to modify.
            bonus (int): Bonus value to add.
        """
        if stat_name in self.stats:
            self.stats[stat_name] += value
        else:
            raise ValueError(f"Stat '{stat_name}' is not valid.")
        
    def lower_stat(self, stat_name: str, value: int) -> None:
        """
        Removes a value from an existing stat value.
        
        Args:
            stat_name (str): Name of the stat to modify.
            bonus (int): Value to lower stat by.
        """
        if stat_name in self.stats:
            self.stats[stat_name] -= value
        else:
            raise ValueError(f"Stat '{stat_name}' is not valid.")

    def __str__(self):
        """String representation of the gear stats."""
        return f"GearStats({self.stats})"
