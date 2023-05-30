import json

import aiohttp
from understat import Understat
import httpx

class PlayerData:
	def __init__(self, session):
		self.session = session

	@classmethod
	async def get_session(cls):
		async with aiohttp.ClientSession() as session:
			understat = Understat(session)

		return understat

	@classmethod
	async def get_players(cls):
		understat = await cls.get_session()
		data = await understat.get_league_players("epl", 2018, {"team_title": "Manchester United"})
		print(json.dumps(data))



