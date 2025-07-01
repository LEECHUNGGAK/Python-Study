import logging
import threading
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)


def thread_function(name):
    logging.info(f"스레드 {name}: 시작")
    time.sleep(2)
    logging.info(f"스레드 {name}: 종료")


if __name__ == "__main__":
    logging.info("메인: 스레드 생성 전")

    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("메인: 스레드 시작 전")

    x.start()
    logging.info("메인: 스레드가 종료되기까지 대기")

    logging.info("메인: 종료")
