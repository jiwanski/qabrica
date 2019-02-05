from lettuce import *
from src import is_this_a_triangle


@step(u'I have three possible sides of a triangle and its expected validity')
def step_1(step):
    world.numbers = step.hashes


@step(u'I check whether a triangle can be formed')
def step_2(step):
    world.outcomes = []
    for row in world.numbers:
        a = int(row['a'])
        b = int(row['b'])
        c = int(row['c'])
        result = row['result']
        outcome = is_this_a_triangle.is_triangle(a, b, c)
        world.outcomes.append([result, str(outcome)])


@step(u'The result should reflect triangle validity')
def step_3(step):
    for row in world.outcomes:
        assert row[0] == row[1]
