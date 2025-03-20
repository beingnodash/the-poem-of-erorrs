import module_b
from loguru import logger
def function_a():
    logger.info("Function love in module_love")
    module_b.function_b()

function_a()