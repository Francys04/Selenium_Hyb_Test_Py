# for messages =>pytest captures log messages at the WARNING level or higher.
# These log messages can be redirected to various destinations, including the console or log files.
# test execution, including debug messages, error traces, and other log records.

import logging
# application log can include your own messages integrated with messages from third-party modules

class LogGen:
    @staticmethod
    def loggen():
        # specify filename=logfile, format of project
        logging.basicConfig(filename=".\\Logs\\automation.log", level=logging.DEBUG, force=True,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
                            )

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger