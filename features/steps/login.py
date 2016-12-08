# coding=UTF-8
# __author__ == ypochien

from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from machete import Machete, Utility


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
    # py3k : data = bytes.fromhex('0203020203')
    alive = '0203020203'.decode('hex')
    context.machete.send(alive)


@then("ALIVE receive")
def step_impl(context):
    expected = '0203020203'.decode('hex')
    assert_that(expected, equal_to(context.machete.recv()))


@step('送出登入資訊"{login_id}"和密碼"{password}"')
def step_impl(context, login_id, password):
    login_data = Utility.make_login_msg(login_id, password)
    context.machete.send(login_data)

@then("收到登入成功")
def step_impl(context):
    print(context.machete.recv())
