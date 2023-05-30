from app.socket_server.auction_events import Auction


class GameEvent(Auction):
	async def on_player_auction(self, sid):
		...
