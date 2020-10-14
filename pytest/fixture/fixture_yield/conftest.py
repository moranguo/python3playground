import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.163.com")

    def fin():
        print("\nteardown smtp_connection")
        smtp_connection.close()
    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value