import concurrent.futures
import logging

def init():
    return True

def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(process)d %(levelname)s - %(message)s")
    logging.info("logging configured")

    logging.info("main ended")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as worker:
        worker.submit(main)
