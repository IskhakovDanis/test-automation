from support.assertions_msg import AssertionsMsg


class Assertions:


    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionsMsg.ERROR_EQUAL.format(actual, expected)