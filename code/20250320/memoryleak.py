import psutil
import os
from loguru import logger

def memory_leak():
    data = []
    i = 0
    process = psutil.Process(os.getpid())
    while True:
        data.append(i)
        i += 1
        memory_usage = process.memory_info().rss / (1024 * 1024)
        logger.info(f"当前内存占用：{memory_usage:.2f} MB")

        if memory_usage > 0.9 * psutil.virtual_memory().total / (1024 * 1024): # 90%内存
            logger.error("内存占用超过90%，程序退出")
            break
        elif memory_usage > 0.8 * psutil.virtual_memory().total / (1024 * 1024): # 80%内存
            logger.warning("内存占用超过80%，请注意")

memory_leak()