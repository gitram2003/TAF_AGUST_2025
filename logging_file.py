import logging



logging.basicConfig(
    filename='log_file.txt',
    filemode='a',
    format='%(asctime)s, %(levelname)s %(message)s',
    level=logging.DEBUG
)

