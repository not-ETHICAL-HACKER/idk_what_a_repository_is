import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

logging.info("Program started")
logging.warning("Something might be wrong")
logging.error("An error occurred")

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Program started")
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("System crash")

