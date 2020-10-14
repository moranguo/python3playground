"""
yield和addfinalizer方法都是在测试完成后呼叫相应的代码。
但是addfinalizer不同的是：
    1)它可以注册多个终结函数。
    2)这些终结方法总是会被执行，无论在之前的setup code有没有抛出错误。
    这个方法对于正确关闭所有的fixture创建的资源非常便利，即使其在创建或获取时失败
"""
import smtplib
import pytest


def test1(smtp_connection):
    assert isinstance(smtp_connection, smtplib.SMTP)
    print("发送邮件成功！")


if __name__ == "__main__":
    pytest.main(["-s", "-v", "fixture_yield_addfinalizer.py"])
