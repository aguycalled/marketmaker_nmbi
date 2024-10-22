from libc.stdint cimport int64_t

from hummingbot.market.market_base cimport MarketBase
from hummingbot.core.data_type.transaction_tracker cimport TransactionTracker


cdef class HitBtcMarket(MarketBase):
    cdef:
        object _async_scheduler
        object _data_source_type
        object _ev_loop
        object _hitbtc_auth
        dict _in_flight_orders
        double _last_poll_timestamp
        double _last_timestamp
        public object _order_tracker_task
        object _poll_notifier
        double _poll_interval
        object _shared_client
        public object _status_polling_task
        dict _trading_rules
        public object _trading_rules_polling_task
        TransactionTracker _tx_tracker

    cdef c_did_timeout_tx(self, str tracking_id)
    cdef c_start_tracking_order(self,
                                str client_order_id,
                                str exchange_order_id,
                                str trading_pair,
                                object order_type,
                                object trade_type,
                                object price,
                                object amount)
    cdef c_stop_tracking_order(self, str order_id)
