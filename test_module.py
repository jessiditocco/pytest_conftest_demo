# tests for smtp connection fixture in conftest.py
def test_ehlo(smtp_connection):
	response, msg = smtp_connection.ehlo()
	assert response == 250
	# assert b"smtp.gmail.com" in msg
	# assert 0 # for demo purposes

def test_noop(smtp_connection):
	response, msg = smtp_connection.noop()
	assert response == 250
	# assert 0 # for demo purposes

# tests for make_customer fixture in conftest.py
def test_customer_records(make_customer_record):
	customer_1 = make_customer_record("Lisa")
	customer_2 = make_customer_record("Mike")
	customer_3 = make_customer_record("Meredith")