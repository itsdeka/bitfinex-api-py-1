from typing import Type, Tuple, List, Dict, Union, Optional, Any

from .. notification import Notification

JSON = Union[Dict[str, "JSON"], List["JSON"], bool, int, float, str, Type[None]]

#region Type hinting for Rest Public Endpoints

class PlatformStatus():
    OPERATIVE: int

class TradingPairTicker():
    SYMBOL: Optional[str]
    BID: float
    BID_SIZE: float
    ASK: float
    ASK_SIZE: float
    DAILY_CHANGE: float
    DAILY_CHANGE_RELATIVE: float
    LAST_PRICE: float
    VOLUME: float
    HIGH: float
    LOW: float

class FundingCurrencyTicker():
    SYMBOL: Optional[str]
    FRR: float
    BID: float
    BID_PERIOD: int
    BID_SIZE: float
    ASK: float
    ASK_PERIOD: int
    ASK_SIZE: float
    DAILY_CHANGE: float
    DAILY_CHANGE_RELATIVE: float
    LAST_PRICE: float
    VOLUME: float
    HIGH: float
    LOW: float
    FRR_AMOUNT_AVAILABLE: float

class TickersHistory():
    SYMBOL: str
    BID: float
    ASK: float
    MTS: int

class TradingPairTrade():
    ID: int 
    MTS: int 
    AMOUNT: float 
    PRICE: float

class FundingCurrencyTrade():
    ID: int 
    MTS: int 
    AMOUNT: float 
    RATE: float 
    PERIOD: int

class TradingPairBook():
    PRICE: float 
    COUNT: int 
    AMOUNT: float
    
class FundingCurrencyBook():
    RATE: float 
    PERIOD: int 
    COUNT: int 
    AMOUNT: float
        
class TradingPairRawBook():
    ORDER_ID: int
    PRICE: float 
    AMOUNT: float
            
class FundingCurrencyRawBook():
    OFFER_ID: int 
    PERIOD: int 
    RATE: float 
    AMOUNT: float

class Statistic():
    MTS: int
    VALUE: float

class Candle():
    MTS: int
    OPEN: float
    CLOSE: float
    HIGH: float
    LOW: float
    VOLUME: float

class DerivativesStatus():
    KEY: Optional[str]
    MTS: int
    DERIV_PRICE: float
    SPOT_PRICE: float
    INSURANCE_FUND_BALANCE: float
    NEXT_FUNDING_EVT_TIMESTAMP_MS: int
    NEXT_FUNDING_ACCRUED: float
    NEXT_FUNDING_STEP: int
    CURRENT_FUNDING: float
    MARK_PRICE: float
    OPEN_INTEREST: float
    CLAMP_MIN: float
    CLAMP_MAX: float

class Liquidation():
    POS_ID: int
    MTS: int
    SYMBOL: str
    AMOUNT: float
    BASE_PRICE: float
    IS_MATCH: int
    IS_MARKET_SOLD: int
    PRICE_ACQUIRED: float

class Leaderboard():
    MTS: int
    USERNAME: str
    RANKING: int
    VALUE: float
    TWITTER_HANDLE: Optional[str]

class FundingStatistic(): 
    TIMESTAMP: int
    FRR: float
    AVG_PERIOD: float
    FUNDING_AMOUNT: float
    FUNDING_AMOUNT_USED: float
    FUNDING_BELOW_THRESHOLD: float

#endregion

#region Type hinting for Rest Authenticated Endpoints

class Wallet():
    WALLET_TYPE: str
    CURRENCY: str
    BALANCE: float
    UNSETTLED_INTEREST: float
    AVAILABLE_BALANCE: float
    LAST_CHANGE: str
    TRADE_DETAILS: JSON

class Order():
    ID: int
    GID: int
    CID: int
    SYMBOL: str
    MTS_CREATE: int
    MTS_UPDATE: int
    AMOUNT: float
    AMOUNT_ORIG: float
    ORDER_TYPE: str
    TYPE_PREV: str
    MTS_TIF: int
    FLAGS: int
    ORDER_STATUS: str
    PRICE: float
    PRICE_AVG: float
    PRICE_TRAILING: float
    PRICE_AUX_LIMIT: float
    NOTIFY: int
    HIDDEN: int
    PLACED_ID: int
    ROUTING: str
    META: JSON

class FundingOffer():
    ID: int
    SYMBOL: str
    MTS_CREATE: int
    MTS_UPDATE: int
    AMOUNT: float
    AMOUNT_ORIG: float
    OFFER_TYPE: str
    FLAGS: int
    OFFER_STATUS: str
    RATE: float
    PERIOD: int
    NOTIFY: bool
    HIDDEN: int
    RENEW: bool
    STATUS: str
    TEXT: str

class Trade():
    ID: int 
    SYMBOL: str 
    MTS_CREATE: int
    ORDER_ID: int 
    EXEC_AMOUNT: float 
    EXEC_PRICE: float 
    ORDER_TYPE: str 
    ORDER_PRICE: float 
    MAKER:int
    FEE: float
    FEE_CURRENCY: str
    CID: int

class Ledger():
    ID: int
    CURRENCY: str 
    MTS: int
    AMOUNT: float
    BALANCE: float
    description: str

#endregion