# 判断两个值是否相等
def assert_equal(actual, expected, msg=None):
    """
    :param actual: 实际值
    :param expected: 预期值
    :param msg: 信息
    :return: None
    """
    try:
        assert actual == expected
    except AssertionError:
        if msg is None:
            msg = "实际值: %s, 预期值: %s" % (actual, expected)
        raise AssertionError(msg)


# 判断两个值是否不相等
def assert_not_equal(actual, expected, msg=None):
    """
    :param actual: 实际值
    :param expected: 预期值
    :param msg: 信息
    :return: None
    """
    try:
        assert actual != expected
    except AssertionError:
        if msg is None:
            msg = "实际值: %s, 预期值: %s" % (actual, expected)
        raise AssertionError(msg)


# 判断实际值是否在预期值中
def assert_in(actual, expect, msg=None):
    """
    :param actual: 实际值
    :param expect: 预期值
    :param msg: 信息
    :return: None
    """
    try:
        assert actual in expect
    except AssertionError:
        if msg is None:
            msg = "实际值: %s, 预期值: %s" % (actual, expect)
        raise AssertionError(msg)


'''
后续在这里添加断言方法
'''