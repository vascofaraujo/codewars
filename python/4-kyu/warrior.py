class DefaultWarrior():
    def __init__(self):
        self.level = 1
        self.rank = "Pushover"
        self.experience = 100
        self.achievements = []
        self.possible_ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

class Warrior(DefaultWarrior):
    def __init__(self):
        super().__init__()

    def level(self):
        return self.level

    def rank(self):
        return self.rank

    def experience(self):
        return self.experience

    def achievements(self):
        return self.achievements

    def _get_experience(self, experience):
        self.experience = self.experience + experience if self.experience+experience <= 100*100 else 100

    def _get_level(self):
        if self.experience >= 10000:
            self.level = 100
            self.experience = 10000
        else:
            self.level = int(self.experience / 100)

    def _get_rank(self):
        self.rank = self.possible_ranks[int(self.level//10)]

    def _get_rank_index(self, enemy_level):
        enemy_rank = self.possible_ranks[int(enemy_level//10)]
        return self.possible_ranks.index(self.rank), self.possible_ranks.index(enemy_rank)

    def training(self, *args):
        if self.level < args[0][2]:
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
        if (warrior_rank < enemy_rank )and (self.level < enemy_level-5):
            return "You've been defeated"
        if self.level == enemy_level:
            self.experience += 10
        if self.level == enemy_level+1:
            self.experience += 5
        if self.level >= enemy_level+2:
            self.experience += 0
        if self.level < enemy_level:
            diff = enemy_level - self.level
            self.experience += (20 * diff * diff)
        old_level = self.level
        self._get_level()
        self._get_rank()
        if old_level > enemy_level+2:
            return "Easy fight"
        if old_level == enemy_level or old_level == enemy_level+1:
            return "A good fight"
        if old_level < enemy_level:
            return "An intense fight"


if __name__ == '__main__':
    bruce_lee = Warrior()
    print(bruce_lee.level)         # => 1
    print(bruce_lee.experience)    # => 100
    print(bruce_lee.rank)          # => "Pushover"
    print(bruce_lee.achievements)  # => []
    bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
    print(bruce_lee.experience)    # => 9100

    print(bruce_lee.level)         # => 91
    print(bruce_lee.rank)          # => "Master"
    print(bruce_lee.battle(90))    # => "A good fight"
    print(bruce_lee.experience)    # => 9105
    print(bruce_lee.achievements)  # => ["defeated chuck norris"]
