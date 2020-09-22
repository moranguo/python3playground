import logging
import uuid

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s [%(filename)s:%(lineno)d] - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

logger = logging.getLogger('ComponentName')


def do_something(log_uuid=None):
    logger.info("This is a test info log,%s" % log_uuid)
    logger.warning("This is a warn log,%s" % log_uuid)
    logger.debug("This is a debug info log,%s" % log_uuid)


if __name__ == "__main__":
    UUID = uuid.uuid5(uuid.NAMESPACE_DNS, "name")
    do_something(UUID)
