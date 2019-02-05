from behave import given, when, then
from ...src import multiples_of_3_or_5
from hamcrest import assert_that, equal_to, greater_than


@given(u'I have a positive "{number}"')
def step_impl(context, number):
    context.number = int(number)
    assert_that(context.number, greater_than(0))


@when(u'I find sum of all multiples of 3 or 5 below "{number}"')
def step_impl(context, number):
    context.number = int(number)
    context.result = multiples_of_3_or_5.solution(context.number)


@then(u'The result should be equal to "{result}"')
def step_impl(context, result):
    assert_that(context.result, equal_to(int(result)))
