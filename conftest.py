import pytest
import smtplib

###################### conftest.py: sharing fixture functions¶ ##########################################

# the smtplib module defines an SMTP client session object that can be used
# to send mail to any internet machine with an SMTP listener daemon
# class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

@pytest.fixture(scope="function")
def smtp_connection():
	print("begin stmtp")
	smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

	yield smtp_connection
	print("teardown stmtp")
	smtp_connection.close()

###################### Fixture Finalization: Add Finalizer ##########################################


# Both yield and add finalier methods work similiarly by calling their code
# after the test ends, but addfinalier has two key differences over yield:
# it is posible to register multiple finalizer functions
# finalizers will always be called regardless if the fixture setup code
# raises an exception-- this is handy to properly close all resrouces created
# by a fixture even if one of them fails to be created
@pytest.fixture(scope="module")
def smtp_connection(request):
	print("begin stmtp")
	smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

	def fin():
		print("teardown smto_connection")
		smtp_connection.close()

	request.addfinalizer(fin)
	return smtp_connection



#################################### Fctories as Fixtures ###############################################
@pytest.fixture
def make_customer_record():

	def _make_customer_record(name):
		return {
		"name": name,
		"orders": []
		}

	return _make_customer_record


# if the data created by the factory requries managing, the fixture can take care of that:
# wont actually run though becuase we dont have a models with a Customer class
# @pytest.fixture
# def make_customer_record():

# 	created_records = []

# 	def _make_customer_record(name):
# 		record = models.Customer(name=name, orders=[])
# 		created_records.append(record)
# 		return record

# 	yield _make_customer_record
# 	for record in created_records:
# 		record.destory()


#################################### Parametrizing Fixtures ###############################################
@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
	smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
	yield smtp_connection
	print("finalizing {}".format(smtp_connection))
	smtp_connection.close()
