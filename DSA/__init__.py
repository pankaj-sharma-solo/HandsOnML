import logging
import time

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(name)s - %(message)s", level=logging.DEBUG)

class StopWatch:
    log = logging.getLogger('StopWatch')

    START_TIME = 0
    END_TIME = 0

    @classmethod
    def start(cls):
        cls.START_TIME = time.time()*1000
        cls.log.info(f"Start Time: {cls.START_TIME}")

    @classmethod
    def stop(cls):
        cls.END_TIME = time.time()*1000
        cls.log.info(f"End Time: {cls.END_TIME}")

    @classmethod
    def elapsed(cls):
        cls.log.info(f"Time Elapsed: {cls.END_TIME - cls.START_TIME} ms")