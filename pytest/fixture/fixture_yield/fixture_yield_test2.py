import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.163.com") as smtp:
        # yield也可以配合with语句使用
        yield smtp  # provide the fixture value
        print("\ntear down smtp in with context")


def test1(smtp):
    assert isinstance(smtp, smtplib.SMTP)
    print("发送邮件成功！")


if __name__ == "__main__":
    pytest.main(["-s", "-v", "fixture_yield_test2.py"])
