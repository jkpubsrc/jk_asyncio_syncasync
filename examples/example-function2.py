#!/usr/bin/python3



import time
import asyncio

from jk_asyncio_syncasync import *





@make_async
def synchroneousFunction():
	print("Beginning synchroneous task ...")
	time.sleep(2)
	print("Synchroneous task completed.")
#



async def main():
	await synchroneousFunction()
#



#asyncio.run(main())									# since python 3.7
asyncio.get_event_loop().run_until_complete(main())		# till python 3.6




