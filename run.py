import random
import time
from datetime import datetime

from app import main

CHECK_INTERVAL_MIN = 170
CHECK_INTERVAL_MAX = 210


while True:

    print("=" * 70)
    print(datetime.now().strftime("[%H:%M:%S] Checking Vinted..."))

    main()

    wait = random.randint(
        CHECK_INTERVAL_MIN,
        CHECK_INTERVAL_MAX,
    )

    print(f"Sleeping {wait} seconds...\n")

    time.sleep(wait)