# -k 参数是按照文件名、类名、方法名来模糊匹配的
pytest -k xxxPattern

# 运行choose_case_by_k下的所有用例
pytest -v
pytest -v -k "test_*.py"

# 运行test_k.py下的所有的测试, 按照文件名称全匹配
pytest -v -k "test_k.py"

# 按照文件名称部分匹配
pytest -v -k "test_k2"

# 按照类名匹配
pytest -v -k "TestSample"
pytest -v -k "TestSampleC"

# 按照方法名匹配
pytest -v -k "test_a_method"
pytest -v -k "test_a_method2"