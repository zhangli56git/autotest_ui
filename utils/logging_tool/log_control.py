#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/3/28 10:56
# @Author : 余少琪
"""
日志封装，可设置不同等级的日志颜色
"""
import logging
from logging import handlers
from typing import Text
import colorlog
import time

from selenium.common import exceptions

from conf.setting import path_sure


class LogHandler:
    """ 日志打印封装"""
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(
            self,
            filename: Text,
            level: Text = "info",
            when: Text = "D",
            fmt: Text = "%(levelname)-8s%(asctime)s%(name)s:%(filename)s:%(lineno)d %(message)s"
    ):
        self.logger = logging.getLogger(filename)

        formatter = self.log_color()

        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        screen_output = logging.StreamHandler()
        # 设置屏幕上显示的格式
        screen_output.setFormatter(formatter)
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        time_rotating = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=3,
            encoding='utf-8'
        )
        # 设置文件里写入的格式
        time_rotating.setFormatter(format_str)
        # 把对象加到logger里
        self.logger.addHandler(screen_output)
        self.logger.addHandler(time_rotating)
        self.log_path = path_sure('\\logs\\log.log')

    @classmethod
    def log_color(cls):
        """ 设置日志颜色 """
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }

        formatter = colorlog.ColoredFormatter(
            # 打印格式并右对齐
            '%(log_color)s[%(asctime)s] [%(name)s] [%(levelname)s] :%(message)s',
            log_colors=log_colors_config
        )
        return formatter


now_time_day = time.strftime("%Y-%m-%d", time.localtime())
INFO = LogHandler(path_sure(f"\\logs\\info-{now_time_day}.log"), level='info')
ERROR = LogHandler(path_sure(f"\\logs\\error-{now_time_day}.log"), level='error')
DEBUG = LogHandler(path_sure(f"\\logs\\debug-{now_time_day}.log"), level='debug')
CRITICAL = LogHandler(path_sure(f"\\logs\\critical-{now_time_day}.log"), level='critical')
WARNING = LogHandler(path_sure(f'\\logs\\warning-{now_time_day}.log'), level='warning')

if __name__ == '__main__':
    INFO.logger.info("info")
    ERROR.logger.error("error")
    DEBUG.logger.debug("debug")
    CRITICAL.logger.critical("critical")
    WARNING.logger.warning("warning")
