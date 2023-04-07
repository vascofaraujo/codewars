class DefaultWarrior:
    def __init__(self):
        self._level = 1
        self._rank = "Pushover"
        self._experience = 100
        self.achievements = []
        self.possible_ranks = [
            "Pushover",
            "Novice",
            "Fighter",
            "Warrior",
            "Veteran",
            "Sage",
            "Elite",
            "Conqueror",
            "Champion",
            "Master",
            "Greatest",
        ]


class Warrior(DefaultWarrior):
    def __init__(self):
        super().__init__()

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value > 100:
            self._level = 100
        else:
            self._level = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
        self._level = self.possible_ranks.index(value) * 10
        self._experience = self._level * 100

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value > 10000:
            self._experience = 10000
        else:
            self._experience = value
        self._level = int(self._experience / 100)
        self._rank = self.possible_ranks[int(self._level // 10)]

    def achievements(self):
        return self.achievements

    def _get_experience(self, experience):
        self._experience = self._experience + experience

    def _get_level(self):
        if self._experience >= 10000:
            self._level = 100
            self._experience = 10000
        else:
            self._level = int(self._experience / 100)

    def _get_rank(self):
        self._rank = self.possible_ranks[int(self._level // 10)]

    def _get_rank_index(self, enemy_level):
        enemy_rank = self.possible_ranks[int(enemy_level // 10)]
        return self.possible_ranks.index(self._rank), self.possible_ranks.index(
            enemy_rank
        )

    def training(self, *args):
        if self._level < args[0][2]:
            return "Not strong enough"
        self.achievements.append(args[0][0])
        self._get_experience(args[0][1])
        self._get_level()
        self._get_rank()
        return args[0][0]

    def battle(self, enemy_level):
        if enemy_level > 100 or enemy_level < 1:
            return "Invalid level"
        warrior_rank, enemy_rank = self._get_rank_index(enemy_level)
        if (warrior_rank < enemy_rank) and (self._level <= enemy_level - 5):
            return "You've been defeated"
        if self._level == enemy_level:
            self._experience += 10
        if self._level == enemy_level + 1:
            self._experience += 5
        if self._level >= enemy_level + 2:
            self._experience += 0
        if self._level < enemy_level:
            diff = enemy_level - self._level
            self._experience += 20 * diff * diff
        old_level = self._level
        self._get_level()
        self._get_rank()
        # old_level = self._level
        if old_level >= enemy_level + 2:
            return "Easy fight"
        if old_level == enemy_level or old_level == enemy_level + 1:
            return "A good fight"
        if old_level < enemy_level:
            return "An intense fight"


if __name__ == "__main__":
    bruce_lee = Warrior()
    # print(bruce_lee.level)  # => 1
    # print(bruce_lee.experience)  # => 100
    # print(bruce_lee.rank)  # => "Pushover"
    # print(bruce_lee.achievements)  # => []

    # bruce_lee.experience = 1000000
    print(bruce_lee.level)
    print(bruce_lee.experience)
    print(
        bruce_lee.training(["Defeated Chuck Norris", 9000, 1])
    )  # => "Defeated Chuck Norris"
    print(bruce_lee.experience)  # => 9100

    print(bruce_lee.level)  # => 91
    print(bruce_lee.rank)  # => "Master"
    # print(bruce_lee.battle(90))    # => "A good fight"
    # print(bruce_lee.experience)    # => 9105
    # print(bruce_lee.achievements)  # => ["defeated chuck norris"]
