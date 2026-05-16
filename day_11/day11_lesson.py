import asyncio
import time
import requests
import httpx
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

#===================================================================
#SYNC VERSION - What you've been doing
#===================================================================

def fetch_sync(city_url: str) -> dict:
    response = requests.get(city_url, timeout= 5)
    return response.json()

def run_sync():
    cities = [
        ("Mumbai", "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&current=temperature_2m"),
        ("Chennai", "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m"),
        ("Delhi", "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=28.61&current=temperature_2m"),
        ("Chennai", "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current=temperature_2m")
    ]

    logger.info("====SYNC version starting====")
    start = time.time()

    results =[]
    for name, url in cities:
        logger.info("   fetching  %s", name)
        data = fetch_sync(url)
        temp = data["current"]["temperature_2m"]
        results.append((name, temp))
        logger.info("   done %s: %.1fdegC", name, temp)

        elapsed = time.time() - start
        logger.info ("====SYNC done in %.2f seconds ====", elapsed)
        return results
    
#============================================================================
# ASYNC VERSION - what we're learning today
#============================================================================

async def fetch_async(client: httpx.AsyncClient, name: str, url:str) -> tuple[str, float]:
    logger.info("  starting %s", name)
    response = await client.get(url, timeout= 10)
    data = response.json()
    temp = data["current"]["temperature_2m"]
    logger.info("   done %s: %.1fdegC", name, temp)
    return name, temp
    

async def run_async():
    cities = [
        ("Mumbai", "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&current=temperature_2m"),
        ("Chennai", "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m"),
        ("Delhi", "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=28.61&current=temperature_2m"),
        ("Chennai", "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current=temperature_2m")
    ]
    
    logger.info("====ASYNC version starting====")
    start = time.time()

    async with httpx.AsyncClient() as client:
        # This is the magic - gather runs all coroutines concurrently
        tasks = [fetch_async(client, name, url) for name, url in cities]
        results = await asyncio.gather(*tasks)

    elapsed = time.time() - start
    logger.info("====ASYNC done in %.2f seconds ====", elapsed)
    return results

#===============================================================================
# RUN BOTH AND COMPARE
#===============================================================================

if __name__=="__main__":
    sync_results = run_sync()
    print(sync_results)
    print()
    asyncio.run(run_async())