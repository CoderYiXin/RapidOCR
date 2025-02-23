# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import logging
from functools import lru_cache


@lru_cache(maxsize=32)
def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fmt = "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
    format_str = logging.Formatter(fmt)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    sh.setFormatter(format_str)
    return logger
