from abc import ABC, abstractmethod
from enum import Enum

class LogLevel(str,Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'

class Logger(ABC):
    @abstractmethod
    def log(self, level:LogLevel, msg:str, e:Exception=None):
        ...

class ConsoleLogger(Logger):
    def log(self, level:LogLevel, msg:str, e:Exception=None):
        print(f"{level}: {msg}")
        if e:
            print(e)

class NullLogger(Logger):
    def log(self, level:LogLevel, msg:str, e:Exception=None):
        pass

class Log:
    levels: list[LogLevel] = [LogLevel.WARN,LogLevel.ERROR]
    logger:Logger = ConsoleLogger()

    def debug_enabled():
        return LogLevel.DEBUG in Log.levels
    def info_enabled():
        return LogLevel.INFO in Log.levels
    def warn_enabled():
        return LogLevel.WARN in Log.levels
    def error_enabled():
        return LogLevel.ERROR in Log.levels

    def debug(msg:str):
        if Log.debug_enabled():
            Log.logger.log(LogLevel.DEBUG, msg)
    def info(msg:str):
        if Log.info_enabled():
            Log.logger.log(LogLevel.INFO, msg)
    def warn(msg:str, e:Exception=None):
        if Log.warn_enabled():
            Log.logger.log(LogLevel.WARN, msg, e)
    def error(msg:str, e:Exception=None):
        if Log.error_enabled():
            Log.logger.log(LogLevel.ERROR, msg, e)
