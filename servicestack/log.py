from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class LogLevel(str, Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'


class Logger(ABC):
    @abstractmethod
    def log(self, level: LogLevel, msg: str, e: Exception = None):
        ...


class ConsoleLogger(Logger):
    def log(self, level: LogLevel, msg: str, e: Exception = None):
        print(f"{level}: {msg}")
        if e:
            print(e)


class NullLogger(Logger):
    def log(self, level: LogLevel, msg: str, e: Exception = None):
        pass


class Log:
    levels: List[LogLevel] = [LogLevel.WARN, LogLevel.ERROR]
    logger: Logger = ConsoleLogger()

    @staticmethod
    def debug_enabled():
        return LogLevel.DEBUG in Log.levels

    @staticmethod
    def info_enabled():
        return LogLevel.INFO in Log.levels

    @staticmethod
    def warn_enabled():
        return LogLevel.WARN in Log.levels

    @staticmethod
    def error_enabled():
        return LogLevel.ERROR in Log.levels

    @staticmethod
    def debug(msg: str):
        if Log.debug_enabled():
            Log.logger.log(LogLevel.DEBUG, msg)

    @staticmethod
    def info(msg: str):
        if Log.info_enabled():
            Log.logger.log(LogLevel.INFO, msg)

    @staticmethod
    def warn(msg: str, e: Exception = None):
        if Log.warn_enabled():
            Log.logger.log(LogLevel.WARN, msg, e)

    @staticmethod
    def error(msg: str, e: Exception = None):
        if Log.error_enabled():
            Log.logger.log(LogLevel.ERROR, msg, e)


# Log.levels.append(LogLevel.DEBUG)
