from behave import given, when, then
from falcon.testing import TestClient

from files import app
from grappa import should


@given("our service is running correctly")
def our_service_is_running_correctly(context):
    context.app = app()
    context.client = TestClient(context.app)


@when("we get the ping endpoint")
def we_get_the_ping_endpont(context):
    context.resp = context.client.simulate_get("/ping")


@then("we get a ping response")
def we_get_a_ping_response(context):
    context.resp.status_code | should.be.equal.to(200)
    context.resp.text | should.be.equal.to("pong")
