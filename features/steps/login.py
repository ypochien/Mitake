from behave import given, when, then, step
from hamcrest import assert_that, equal_to

from machete import Machete


@given('We have Mitake Server {ip} {port:d}')
def step_impl(context, ip, port):
    context.ip = ip
    context.port = port


@when("Connect to Server")
def step_impl(context):
    context.machete = Machete(context.ip, context.port)
    context.machete.login()


@step("send ALIVE")
def step_impl(context):
    # py3k : data = bytes.fromhex('01AF23')
    alive = '0203020203'.decode('hex')
    context.machete.send(alive)


@then("ALIVE receive")
def step_impl(context):
    expected = '0203020203'.decode('hex')
    assert_that(expected, equal_to(context.machete.recv()))
