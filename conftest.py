import pytest
import smptlib

# the smtplib module defines an SMTP client session object that can be used
# to send mail to any internet machine with an SMTP listener daemon
# class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

@pytest.fixture(scope="module")
def smtp_connection():
	return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)