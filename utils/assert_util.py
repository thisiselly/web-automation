import logging

from utils.logs_util import logger


class AssertUtil:
    def assertion(self, expect_result, compare_method, actual_result, message = None):
        """
        :param expect_result:
        :param compare_method:
        :param actual_result:
        :return:
        """
        logger.info(f"start assertion, expect: {expect_result}, compare method: {compare_method}, actual:{actual_result}")
        try:
            if compare_method == "==":
                assert expect_result == actual_result
            elif compare_method == "!=":
                assert expect_result != actual_result
            elif compare_method == ">":
                assert expect_result > actual_result
            elif compare_method == "<":
                assert expect_result < actual_result
            elif compare_method == "in":
                assert expect_result in actual_result
            elif compare_method == "not in":
                assert expect_result not in actual_result
            else:
                try:
                    raise NameError(f"method {compare_method} not found")
                except Exception as e:
                    logger.error(e)
                    raise

        except AssertionError as e:
            logger.error(f"assertion fail by reason:{e}")
            if message:
                logger.error(f"fail message: {message}")
            raise

verification = AssertUtil()
