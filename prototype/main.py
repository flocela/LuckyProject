class Applicant:
    def __init__(self, skill, luck, luck_weight):
        self.skill       = skill
        self.luck        = luck
        self.weight_luck = luck_weight 
        self.score       = (luck_weight * luck) + ((1 - luck_weight) * skill) 

applicant1 = Applicant(100, 20, .5)

assert applicant1.score == 60
