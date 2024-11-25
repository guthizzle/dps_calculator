from stats.gear_stats import GearStats

def main():
    # setting stats for Player
    player_levels = {
        "attack": 99,
        "strength": 99,
        "defence": 99,
        "magic": 99,
        "ranged": 99,
        "prayer": 99,
        "mining": 99,
        "herblore": 99
    }
    
    player_gear_stats = GearStats()
    
    # Set player gear stats
    # replace with ui
    player_gear_stats.set_stat("stabAcc",15)
    
    weapon_stats = {
        "stabAcc": 0,
        "slashAcc": 0,
        "crushAcc": 0,
        "magicAcc": 0,
        "rangedAcc": 0,
        "speed": 4,
    }
    
    
    # create Player() - pass it off/def stats & levels
    
    
    
    
    # create NPC() - same
    
    #
    # dpsEngine.dps(player, NPC)
    # dpsEngine.dps()
    
    
    pass

if __name__ == "__main__":
    main()
    