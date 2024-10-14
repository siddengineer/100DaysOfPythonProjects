import os
import time
import logging

logging.basicConfig(filename='logs/access_log.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

if not os.path.exists('logs'):
    os.makedirs('logs')

while True:
    print("Monitoring files...")
    time.sleep(5)  # Simulate work
