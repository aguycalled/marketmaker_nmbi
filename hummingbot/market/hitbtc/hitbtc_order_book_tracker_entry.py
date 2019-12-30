from hummingbot.core.data_type.order_book import OrderBook
from hummingbot.core.data_type.order_book_tracker_entry import OrderBookTrackerEntry
from hummingbot.market.hitbtc.hitbtc_active_order_tracker import HitBtcActiveOrderTracker

class HitBtcOrderBookTrackerEntry(OrderBookTrackerEntry):
    def __init__(
        self, symbol: str, timestamp: float, order_book: OrderBook, active_order_tracker: HitBtcActiveOrderTracker
    ):
        self._active_order_tracker = active_order_tracker
        super(HitBtcOrderBookTrackerEntry, self).__init__(symbol, timestamp, order_book)

    def __repr__(self) -> str:
        return (
            f"HitBtcOrderBookTrackerEntry(symbol='{self._symbol}', timestamp='{self._timestamp}', "
            f"order_book='{self._order_book}')"
        )

    @property
    def active_order_tracker(self) -> HitBtcActiveOrderTracker:
        return self._active_order_tracker
