#!/usr/bin/python3



import time
import asyncio

from jk_asyncio_syncasync import *




class MyProgram(object):

	@make_async
	def synchroneousMethod(self):
		print("Beginning synchroneous task ...")
		time.sleep(2)
		print("Synchroneous task completed.")
	#

	async def main(self):
		await self.synchroneousMethod()
	#

#



p = MyProgram()



#asyncio.run(main())									# since python 3.7
asyncio.get_event_loop().run_until_complete(p.main())	# till python 3.6




