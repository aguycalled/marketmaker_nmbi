#!/usr/bin/env python
import bz2
import logging
import ujson
import pandas as pd
import hummingbot.market.hitbtc.hitbtc_constants as constants
from hummingbot.market.hitbtc.hitbtc_order_book_message import HitBtcOrderBookMessage

from aiokafka import ConsumerRecord
from sqlalchemy.engine import RowProxy
from typing import (
    Optional,
    Dict,
    List, Any)
from hummingbot.logger import HummingbotLogger
from hummingbot.core.event.events import TradeType
from hummingbot.core.data_type.order_book cimport OrderBook
from hummingbot.core.data_type.order_book_message import (
    OrderBookMessage, OrderBookMessageType
)

_hbaot_logger = None

cdef class HitBtcOrderBook(OrderBook):

    @classmethod
    def logger(cls) -> HummingbotLogger:
        global _hbaot_logger
        if _hbaot_logger is None:
            _hbaot_logger = logging.getLogger(__name__)
        return _hbaot_logger

    @classmethod
    def snapshot_message_from_exchange(cls,
                                       msg: Dict[str, any],
                                       timestamp: float,
                                       metadata: Optional[Dict] = None):
        print("snapshot_message_from_exchange inside func")
        try:
            if metadata: msg.update(metadata)

            bids = [list(item.values()) for item in msg['bid']]
            asks = [list(item.values()) for item in msg['ask']]

            content = {
                "trading_pair": msg["trading_pair"],
                "update_id": timestamp,
                "bids": bids,
                "asks": asks
            }

            return HitBtcOrderBookMessage(
                message_type=OrderBookMessageType.SNAPSHOT,
                content=content,
                timestamp=timestamp
            )
        except Exception as e:
            print(e)
            cls.logger().error(f" snapshot error: {str(e)}", exc_info=True)
            raise e

    @classmethod
    def snapshot_message_from_db(cls, record: RowProxy, metadata: Optional[Dict] = None):
        """
        *used for backtesting
        Convert a row of snapshot data into standard OrderBookMessage format
        :param record: a row of snapshot data from the database
        :return: HitBtcOrderBookMessage
        """
        return HitBtcOrderBookMessage(
            message_type=OrderBookMessageType.SNAPSHOT,
            content=record.json,
            timestamp=record.timestamp
        )

    @classmethod
    def diff_message_from_exchange(cls,
                                   msg: Dict[str, any],
                                   timestamp: Optional[float] = None,
                                   metadata: Optional[Dict] = None):
        """
        Convert json diff data into standard OrderBookMessage format
        :param msg: json diff data from live web socket stream
        :param timestamp: timestamp attached to incoming data
        :return: HitBtcOrderBookMessage
        """
        bids = [list(item.values()) for item in msg['bid']]
        asks = [list(item.values()) for item in msg['ask']]

        content = {
            "trading_pair": msg["symbol"],
            "update_id": timestamp,
            "bids": bids,
            "asks": asks
        }

        if metadata:
            msg.update(metadata)
        return HitBtcOrderBookMessage(
            message_type=OrderBookMessageType.DIFF,
            content=content,
            timestamp=timestamp
        )

    @classmethod
    def diff_message_from_db(cls, record: RowProxy, metadata: Optional[Dict] = None):
        """
        *used for backtesting
        Convert a row of diff data into standard OrderBookMessage format
        :param record: a row of diff data from the database
        :return: HitBtcOrderBookMessage
        """
        return HitBtcOrderBookMessage(
            message_type=OrderBookMessageType.DIFF,
            content=record.json,
            timestamp=record.timestamp
        )

    @classmethod
    def trade_message_from_exchange(cls,
                                    msg: Dict[str, Any],
                                    timestamp: Optional[float] = None,
                                    metadata: Optional[Dict] = None):
        """
        *used for backtesting
        Convert a trade data into standard OrderBookMessage format
        :param record: a trade data from the database
        :return: HitBtcOrderBookMessage
        """

        content = {
            "trading_pair": metadata["trading_pair"],
            "trade_type": float(TradeType.SELL.value) if msg["side"] == "buy" else float(TradeType.BUY.value),
            "trade_id": msg["id"],
            "update_id": timestamp,
            "amount": msg["quantity"],
            "price": msg["price"]
        }

        if metadata:
            msg.update(metadata)
        return HitBtcOrderBookMessage(
            message_type=OrderBookMessageType.TRADE,
            content=content,
            timestamp=timestamp
        )

    @classmethod
    def trade_message_from_db(cls, record: RowProxy, metadata: Optional[Dict] = None):
        """
        *used for backtesting
        Convert a row of trade data into standard OrderBookMessage format
        :param record: a row of trade data from the database
        :return: HitBtcOrderBookMessage
        """
        return HitBtcOrderBookMessage(
            message_type=OrderBookMessageType.TRADE,
            content=record.json,
            timestamp=record.timestamp
        )

    @classmethod
    def from_snapshot(cls, snapshot: OrderBookMessage):
        raise NotImplementedError(constants.EXCHANGE_NAME + " order book needs to retain individual order data.")

    @classmethod
    def restore_from_snapshot_and_diffs(self, snapshot: OrderBookMessage, diffs: List[OrderBookMessage]):
        raise NotImplementedError(constants.EXCHANGE_NAME + " order book needs to retain individual order data.")
