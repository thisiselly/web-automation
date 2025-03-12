import logging

from utils.logs_util import logger

def assert_equal(expected, actual, message=""):
    assert expected == actual, f"{message}, expect:{expected}, actual:{actual}"

def assert_not_equal(expected, actual, message=""):
    assert expected != actual, f"{message}"

def assert_true(condition, message=""):
    assert condition, f"{message}"

def assert_false(condition, message=""):
    assert not condition, f"{message}"

def assert_in(element, container, message=""):
    assert element in container, f"{message}"

def assert_not_in(element, container, message=""):
    assert element not in container, f"{message}"

def assert_greater(expected, actual, message=""):
    assert expected > actual, f"{message}"

def assert_greater_equal(expected, actual, message=""):
    assert expected >= actual, f"{message}"

def assert_less(expected, actual, message=""):
    assert expected < actual, f"{message}"

def assert_less_equal(expected, actual, message=""):
    assert expected <= actual, f"{message}"

# class AssertUtil:
#     def assertion(self, expect_result, compare_method, actual_result, message = None):
#         """
#         :param expect_result:
#         :param compare_method:
#         :param actual_result:
#         :return:
#         """
#         logger.info(f"start assertion, expect: {expect_result}, compare method: {compare_method}, actual:{actual_result}")
#         try:
#             if compare_method == "==":
#                 assert expect_result == actual_result
#             elif compare_method == "!=":
#                 assert expect_result != actual_result
#             elif compare_method == ">":
#                 assert expect_result > actual_result
#             elif compare_method == "<":
#                 assert expect_result < actual_result
#             elif compare_method == "in":
#                 assert expect_result in actual_result
#             elif compare_method == "not in":
#                 assert expect_result not in actual_result
#             else:
#                 try:
#                     raise NameError(f"method {compare_method} not found")
#                 except Exception as e:
#                     logger.error(e)
#                     raise
#
#         except AssertionError as e:
#             logger.error(f"assertion fail by reason:{e}")
#             if message:
#                 logger.error(f"fail message: {message}")
#             raise
#
# verification = AssertUtil()
