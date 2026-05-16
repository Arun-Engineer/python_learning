import asyncio
import time

# Sync Version
def fetch_sync(name: str) -> str:
    print(f" starting {name}")
    time.sleep(1)
    print(f" done {name}")
    print(f"result-{name}")

# Async Version
async def fetch_async(name: str) -> str:
    print(f" starting {name}")
    await asyncio.sleep(1)
    print(f" done {name}")
    return f"result-{name}"