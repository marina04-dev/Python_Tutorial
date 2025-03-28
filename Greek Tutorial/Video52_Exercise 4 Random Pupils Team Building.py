from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())


N = 30
pupils = set()
for number in range(N):
    pupils.add("pupil" + str(number))
print(pupils)

list_pupils = list(pupils)
math_teams = set()
while _ in range(N//2):
    pos1 = randrange(0,len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0,len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1,pupil2)
    math_teams.add(team)
print("Math teams: " + str(math_teams)

list_pupils = list(pupils)
geography_teams = set()
while _ in range(N//2):
    pos1 = randrange(0,len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0,len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1,pupil2)
    geography_teams.add(team)
print("Geography teams: " + str(geography_teams)
