
import random
from tabulate import tabulate

# ============================================================================
#                              PLAYER
# ============================================================================


class Player:
    """
    ANVÄNDAREN
    """

    def __init__(self, player_avatar: list[tuple[str, str]]) -> None:

        # Player Status
        self.name: str = player_avatar[0][1]
        self.player_lift: int = 3
        self.player_hp: int = 10
        self.player_damage: int = random.randint(5, 10)
        self.player_lvl: int = 1
        self.player_armor: str = random.choice(['Heavyarmor', 'Lightarmor'])
        self.player_inventory: dict = {
            'item 1': None,
            'item 2': None,
            'item 3': None,
            'item 4': None,
            'item 5': None,
        }

        # Player Looks
        self.skin_color: str = player_avatar[1][1]
        self.hair_color: str = player_avatar[2][1]
        self.body_shape: str = player_avatar[3][1]
        self.eye_color: str = player_avatar[4][1]
        self.height: str = player_avatar[5][1]
        self.weight: str = player_avatar[6][1]

    def print_player_stats(self):
        """
        Prints out a table of how the player looks
        """
        table_stats_data = [
            ["Player Stats", ""],
            ["Name", self.name],
            ["Life", self.player_lift],
            ["Level", self.player_lvl],
            ["Health", self.player_hp],
            ["Damage", self.player_damage],
            ["Armor", self.player_armor]
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER STATS
        print(tabulate(table_stats_data, headers="firstrow", tablefmt="psql"))

    def print_player_avatar(self):
        """
        Prints out a player avatar looks
        """

        table_stats_avatar = [
            ["Avatar", ""],
            ["Skin color", self.skin_color],
            ["Hair color", self.hair_color],
            ["Body shape", self.body_shape],
            ["Eye color", self.eye_color],
            ["Height", self.height],
            ["Weight", self.weight],
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER LOOKS
        print(tabulate(table_stats_avatar, headers="firstrow", tablefmt="psql"))


# ============================================================================
#                               MONSTER
# ============================================================================


class Monster:
    """

    MONSTER FOR A PLAYER, EMENY THAT PLAYER WILL FIGHT IN THE GAME

    """

    def __init__(self, moster_level: int) -> None:
        self.moster_level = moster_level

        match moster_level:
            case 1:
                self.name: str = "Bob"
                self.health: int = 10
                self.damage: int = random.randint(1, 10)
                self.armor: int = 0
            case 2:
                self.name: str = "Bob 2.0"
                self.health: int = 25
                self.damage: int = random.randint(1, 15)
                self.armor: int = random.randint(1, 3)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass


# ============================================================================
#                               MONSTER
# ============================================================================

def luck_calculation() -> list[float]:
    """
    HOW MUCH LUCK THE GAME HAVE
    """
    damage_boost_luck: float = 0
    armor_boost_luck: float = 0
    health_boost_luck: float = 0

    damage_boost_luck = random.random()
    armor_boost_luck = random.random()
    health_boost_luck = random.random()
    summa = sum([damage_boost_luck, health_boost_luck, armor_boost_luck])

    damage_boost_luck = damage_boost_luck / summa
    health_boost_luck = health_boost_luck / summa
    armor_boost_luck = armor_boost_luck / summa

    stats_boost_porcentage = [damage_boost_luck,
                              health_boost_luck, armor_boost_luck]
    return stats_boost_porcentage


class Item(object):
    """
    item
    """

    def __init__(self, rarity: str, item_name: str) -> None:
        self.rarity = rarity
        self.item_name = item_name

        self.damage_boost: int = 0
        self.health_boost: int = 0
        self.armor_boost: int = 0

    def __str__(self) -> str:
        return f"""

    This artefact is called {self.item_name} and has rarity of {self.rarity}

    Effected:

        Damage Multiplier : {self.damage_boost}
        Max Health Boost  : {self.health_boost} %
        Armor Boost       : {self.armor_boost} %
    """

    def genatate_stat(self):
        """
        somthing
        """
        number_of_stats: int = 0
        effect: int = 0
        match self.rarity:
            case "rare":
                number_of_stats = 1
                effect = random.randrange(0, 10)
            case "epic":
                number_of_stats = 2
                effect = random.randrange(0, 10)
            case "legendary":
                number_of_stats = 3
                effect = random.randrange(0, 10)

        damage_boost_luck = luck_calculation()[0]
        health_boost_luck = luck_calculation()[1]
        armor_boost_luck = luck_calculation()[2]

        user_luck = random.random()

        disctance_between_user_and_damage_luck = abs(
            user_luck-damage_boost_luck)
        disctance_between_user_and_heath_luck = abs(
            user_luck-health_boost_luck)
        disctance_between_user_and_armor_luck = abs(
            user_luck-armor_boost_luck)

        for _ in range(number_of_stats):
            if disctance_between_user_and_damage_luck > disctance_between_user_and_heath_luck and disctance_between_user_and_damage_luck > disctance_between_user_and_armor_luck:
                print("damage")
                self.damage_boost += effect
            elif disctance_between_user_and_heath_luck > disctance_between_user_and_damage_luck and disctance_between_user_and_heath_luck > disctance_between_user_and_armor_luck:
                print("health")
                self.health_boost += effect
            elif disctance_between_user_and_armor_luck > disctance_between_user_and_damage_luck and disctance_between_user_and_armor_luck > disctance_between_user_and_heath_luck:
                print("armor")
                self.armor_boost += effect

            damage_boost_luck = luck_calculation()[0]
            health_boost_luck = luck_calculation()[1]
            armor_boost_luck = luck_calculation()[2]

            user_luck = random.random()

            disctance_between_user_and_damage_luck = abs(
                user_luck-damage_boost_luck)
            disctance_between_user_and_heath_luck = abs(
                user_luck-health_boost_luck)
            disctance_between_user_and_armor_luck = abs(
                user_luck-armor_boost_luck)


if __name__ == "__main__":
    item1 = Item("epic", "hi")

    item1.genatate_stat()

    print(item1)
