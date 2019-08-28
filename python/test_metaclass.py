import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = '!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return "{}(name={}, hp={}, ac={}, attacks={}".format(self.__class__.__name__, self.name, self.hp,
                                                             self.ac, self.attacks)


x = yaml.load("""
!Monster
name: Cave spider
hp: [2,6] # 2db
ac: 16
attacks: [BITE, HURT]
""")

print(x)
print(dir(x))

# m = Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])
# print(yaml.dump(m))