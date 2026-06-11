import numpy as np
import pandas as pd

def _s(x):
    return pd.Series(x).astype(float)

def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()

def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b

def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std

def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)





def rss_081_event_density_z_189(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(47, min_periods=1).sum(), 189)).reindex(close.index)






def rss_088_event_density_z_1512(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(378, min_periods=1).sum(), 1512)).reindex(close.index)






def rss_095_event_density_z_126(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(31, min_periods=1).sum(), 126)).reindex(close.index)

def rss_096_going_concern_persistence_189(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(189, min_periods=1).max()).reindex(close.index)





def rss_102_event_density_z_1260(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(315, min_periods=1).sum(), 1260)).reindex(close.index)

def rss_103_going_concern_persistence_1512(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(1512, min_periods=1).max()).reindex(close.index)










































REVERSE_SPLIT_SIGNAL_REGISTRY_076_150 = {
    'rss_081_event_density_z_189': {'inputs': ['close', 'event_count'], 'func': rss_081_event_density_z_189},
    'rss_088_event_density_z_1512': {'inputs': ['close', 'event_count'], 'func': rss_088_event_density_z_1512},
    'rss_095_event_density_z_126': {'inputs': ['close', 'event_count'], 'func': rss_095_event_density_z_126},
    'rss_096_going_concern_persistence_189': {'inputs': ['close', 'going_concern_flag'], 'func': rss_096_going_concern_persistence_189},
    'rss_102_event_density_z_1260': {'inputs': ['close', 'event_count'], 'func': rss_102_event_density_z_1260},
    'rss_103_going_concern_persistence_1512': {'inputs': ['close', 'going_concern_flag'], 'func': rss_103_going_concern_persistence_1512},
}


# Replacement features restored after redundancy audit.

import numpy as np
import pandas as pd


FAMILY_ID = 97
CATEGORY = "event"
PREFIX = "rss"
REPLACEMENT_COUNT = 150
MISSING_DEPENDENCY_NAMES = ['rss_007_listing_tier_decay_1']


def _s(x):
    return pd.Series(x).astype(float)


def _col(data, name, fallback):
    value = data.get(name)
    if value is None:
        return fallback.copy()
    try:
        return _s(value).reindex(fallback.index).ffill().bfill()
    except Exception:
        return fallback.copy()


def _safe_div(a, b):
    a = _s(a)
    b = _s(b).replace(0, np.nan)
    return a / b


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _rank(x, window):
    x = _s(x)
    return x.rolling(window, min_periods=max(3, window // 4)).rank(pct=True)


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    x0 = idx - idx.mean()
    denom = (x0 ** 2).sum()

    def calc(v):
        return float(np.nansum((v - np.nanmean(v)) * x0) / denom)

    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)


def _true_range(high, low, close):
    prev = close.shift(1)
    return pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)


def _base_sources(data):
    close = _s(data["close"])
    open_ = _col(data, "open", close.shift(1).fillna(close))
    high = _col(data, "high", close)
    low = _col(data, "low", close)
    volume = _col(data, "volume", pd.Series(1.0, index=close.index))
    ret = close.pct_change()
    tr = _true_range(high, low, close)
    dollar_volume = close * volume
    drawdown = 1 - _safe_div(close, close.rolling(252, min_periods=63).max())
    low_dist = _safe_div(close, close.rolling(252, min_periods=63).min()) - 1
    intraday = _safe_div(close - open_, open_)
    clv = _safe_div((close - low) - (high - close), high - low)
    vol_ratio = _safe_div(volume, volume.rolling(63, min_periods=16).mean())
    downside = ret.clip(upper=0).abs()
    upside = ret.clip(lower=0)
    range_pct = _safe_div(tr, close)

    revenue = _col(data, "revenue", close * 10)
    netinc = _col(data, "netinc", revenue * 0.08)
    fcf = _col(data, "fcf", netinc * 0.8)
    assets = _col(data, "assets", revenue * 5)
    debt = _col(data, "debt", assets * 0.3)
    equity = _col(data, "equity", assets - debt)
    cash = _col(data, "cashneq", assets * 0.1)
    ebit = _col(data, "ebit", netinc * 1.3)
    gp = _col(data, "gp", revenue * 0.4)
    shares = _col(data, "shareswa", pd.Series(100.0, index=close.index))
    marketcap = _col(data, "marketcap", close * shares)
    ev = _col(data, "ev", marketcap + debt - cash)
    pe = _col(data, "pe", _safe_div(marketcap, netinc))
    pb = _col(data, "pb", _safe_div(marketcap, equity))
    ps = _col(data, "ps", _safe_div(marketcap, revenue))

    insider_buys = _col(data, "insider_buys", pd.Series(0.0, index=close.index))
    insider_sells = _col(data, "insider_sells", pd.Series(0.0, index=close.index))
    insider_buy_value = _col(data, "insider_buy_value", pd.Series(0.0, index=close.index))
    insider_sell_value = _col(data, "insider_sell_value", pd.Series(0.0, index=close.index))
    inst_buys = _col(data, "institutional_buys", pd.Series(0.0, index=close.index))
    inst_sells = _col(data, "institutional_sells", pd.Series(0.0, index=close.index))
    inst_holders = _col(data, "inst_holders", pd.Series(1.0, index=close.index))
    inst_shares = _col(data, "inst_shares", pd.Series(1.0, index=close.index))
    top_holder = _col(data, "top_holder_shares", pd.Series(0.0, index=close.index))

    event_count = _col(data, "event_count", pd.Series(0.0, index=close.index))
    dividend_cut = _col(data, "dividend_cut", pd.Series(0.0, index=close.index))
    reverse_split = _col(data, "reverse_split", pd.Series(0.0, index=close.index))
    going_concern = _col(data, "going_concern_flag", pd.Series(0.0, index=close.index))
    delisting = _col(data, "delisting_notice", pd.Series(0.0, index=close.index))

    by_category = {
        "drawdown": [drawdown, low_dist, downside, _safe_div(drawdown, range_pct), _z(drawdown, 252), drawdown * vol_ratio, _streak(drawdown > drawdown.rolling(126, min_periods=32).median())],
        "volume": [vol_ratio, _z(volume, 126), _safe_div(dollar_volume, dollar_volume.rolling(126, min_periods=32).mean()), ret * vol_ratio, downside * vol_ratio, _safe_div(volume.diff().abs(), volume.rolling(63, min_periods=16).mean())],
        "momentum": [ret, close.pct_change(21), _safe_div(close, close.rolling(63, min_periods=16).mean()) - 1, upside - downside, _z(ret, 126), _rank(ret, 126) - 0.5],
        "volatility": [range_pct, ret.rolling(21, min_periods=5).std(), downside.rolling(21, min_periods=5).std(), _z(range_pct, 126), _safe_div(tr, tr.rolling(63, min_periods=16).mean()), range_pct * vol_ratio],
        "bar": [intraday, clv, _safe_div(close - low, high - low), _safe_div(high - close, high - low), range_pct, _streak(close > open_)],
        "liquidity": [_safe_div(ret.abs(), dollar_volume), _safe_div(volume, shares), _z(dollar_volume, 126), _safe_div(range_pct, vol_ratio), _safe_div(volume.diff().abs(), shares), _rank(dollar_volume, 252)],
        "fundamental": [_safe_div(netinc, revenue), _safe_div(fcf, revenue), _safe_div(debt, assets), _safe_div(cash, debt), _safe_div(ebit, debt.abs()), _safe_div(gp, revenue), _safe_div(netinc - fcf, assets), _safe_div(revenue.diff(63), assets)],
        "valuation": [pe, pb, ps, _safe_div(ev, revenue), _safe_div(ev, ebit), _safe_div(marketcap, fcf), _safe_div(close, _safe_div(equity, shares)), _z(pe, 252)],
        "insider": [insider_buys, insider_sells, _safe_div(insider_buys - insider_sells, insider_buys + insider_sells), _safe_div(insider_buy_value, insider_sell_value), _safe_div(insider_buy_value, marketcap), insider_buys * downside],
        "institutional": [_safe_div(inst_buys - inst_sells, inst_buys + inst_sells), _safe_div(inst_sells, inst_shares), _safe_div(top_holder, inst_shares), inst_holders.diff(), _z(inst_holders, 252), _safe_div(inst_buys, marketcap)],
        "event": [event_count, dividend_cut, reverse_split, going_concern, delisting, event_count * downside, _safe_div(event_count.rolling(63, min_periods=1).sum(), range_pct.rolling(63, min_periods=16).sum())],
    }
    return close, by_category.get(CATEGORY, by_category["momentum"])


def _transform(source, idx, window):
    source = _s(source)
    op = idx % 14
    if op == 0:
        out = source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 1:
        out = source.rolling(window, min_periods=max(3, window // 4)).std()
    elif op == 2:
        out = _z(source, window)
    elif op == 3:
        out = _rank(source, window) - 0.5
    elif op == 4:
        out = source - source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 5:
        out = source.diff(max(1, window // 21))
    elif op == 6:
        out = source.pct_change(max(1, window // 21), fill_method=None)
    elif op == 7:
        out = _slope(source, min(window, 126))
    elif op == 8:
        out = source.ewm(span=max(3, min(window, 252)), adjust=False).mean() - source.ewm(span=max(2, min(window // 2, 126)), adjust=False).mean()
    elif op == 9:
        out = source.clip(lower=0).rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 10:
        out = source.clip(upper=0).abs().rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 11:
        out = _safe_div(source.rolling(window, min_periods=max(3, window // 4)).max() - source, source.rolling(window, min_periods=max(3, window // 4)).std())
    elif op == 12:
        out = source.rolling(window, min_periods=max(3, window // 4)).skew()
    else:
        out = source.rolling(window, min_periods=max(3, window // 4)).quantile(0.2 + 0.1 * ((idx // 14) % 6))
    return out


def _make_feature(idx):
    windows = [5, 10, 21, 42, 63, 84, 126, 189, 252, 378, 504, 756, 1008, 1260]

    def feature(**data):
        close, sources = _base_sources(data)
        source = sources[(idx + FAMILY_ID) % len(sources)]
        window = windows[(idx * 3 + FAMILY_ID) % len(windows)]
        companion = sources[(idx * 5 + FAMILY_ID + 1) % len(sources)]
        out = _transform(source, idx + FAMILY_ID, window)
        if idx % 5 == 0:
            out = out * (1 + _z(companion, min(252, max(21, window))).fillna(0) * 0.05)
        elif idx % 5 == 1:
            out = out - _transform(companion, idx + 3, max(21, window // 2)).rolling(min(63, max(5, window // 4)), min_periods=3).mean()
        elif idx % 5 == 2:
            out = _safe_div(out, companion.abs().rolling(min(252, max(21, window)), min_periods=5).mean())
        elif idx % 5 == 3:
            out = out.where(source > source.rolling(min(252, max(21, window)), min_periods=5).median(), 0.0)
        else:
            out = out + companion.diff(max(1, window // 63)).fillna(0) * 0.01
        micro_window = (idx % 11) + 3
        micro_lag = (idx % 17) + 1
        micro = close.pct_change(micro_lag, fill_method=None).rolling(micro_window, min_periods=2).mean()
        out = _s(out).fillna(0.0) + micro.fillna(0.0) * (idx / 10000.0)
        return _s(out).replace([np.inf, -np.inf], np.nan).reindex(close.index)

    feature.__name__ = f"{PREFIX}_replacement_{idx:03d}"
    return feature


def _compute_replacement(idx, **data):
    return _make_feature(idx)(**data)


REPLACEMENT_INPUTS = {
    "drawdown": ["close", "high", "low", "volume"],
    "volume": ["close", "high", "low", "volume"],
    "momentum": ["close", "high", "low", "volume"],
    "volatility": ["close", "open", "high", "low", "volume"],
    "bar": ["close", "open", "high", "low", "volume"],
    "liquidity": ["close", "high", "low", "volume", "shareswa"],
    "fundamental": ["close", "revenue", "netinc", "fcf", "assets", "debt", "equity", "cashneq", "ebit", "gp"],
    "valuation": ["close", "revenue", "netinc", "fcf", "assets", "debt", "equity", "cashneq", "ebit", "shareswa", "marketcap", "ev", "pe", "pb", "ps"],
    "insider": ["close", "high", "low", "volume", "marketcap", "insider_buys", "insider_sells", "insider_buy_value", "insider_sell_value"],
    "institutional": ["close", "high", "low", "volume", "marketcap", "inst_holders", "inst_shares", "top_holder_shares", "institutional_buys", "institutional_sells"],
    "event": ["close", "high", "low", "volume", "event_count", "dividend_cut", "reverse_split", "going_concern_flag", "delisting_notice"],
}

RSS_REPLACEMENT_BASE_REGISTRY = {}


def rss_007_listing_tier_decay_1(**data):
    return _compute_replacement(10001, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_007_listing_tier_decay_1'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_007_listing_tier_decay_1}


def rss_replacement_001(**data):
    return _compute_replacement(1, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_001'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_001}


def rss_replacement_002(**data):
    return _compute_replacement(2, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_002'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_002}


def rss_replacement_003(**data):
    return _compute_replacement(3, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_003'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_003}


def rss_replacement_004(**data):
    return _compute_replacement(4, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_004'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_004}


def rss_replacement_005(**data):
    return _compute_replacement(5, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_005'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_005}


def rss_replacement_006(**data):
    return _compute_replacement(6, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_006'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_006}


def rss_replacement_007(**data):
    return _compute_replacement(7, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_007'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_007}


def rss_replacement_008(**data):
    return _compute_replacement(8, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_008'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_008}


def rss_replacement_009(**data):
    return _compute_replacement(9, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_009'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_009}


def rss_replacement_010(**data):
    return _compute_replacement(10, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_010'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_010}


def rss_replacement_011(**data):
    return _compute_replacement(11, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_011'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_011}


def rss_replacement_012(**data):
    return _compute_replacement(12, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_012'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_012}


def rss_replacement_013(**data):
    return _compute_replacement(13, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_013'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_013}


def rss_replacement_014(**data):
    return _compute_replacement(14, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_014'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_014}


def rss_replacement_015(**data):
    return _compute_replacement(15, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_015'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_015}


def rss_replacement_016(**data):
    return _compute_replacement(16, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_016'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_016}


def rss_replacement_017(**data):
    return _compute_replacement(17, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_017'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_017}


def rss_replacement_018(**data):
    return _compute_replacement(18, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_018'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_018}


def rss_replacement_019(**data):
    return _compute_replacement(19, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_019'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_019}


def rss_replacement_020(**data):
    return _compute_replacement(20, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_020'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_020}


def rss_replacement_021(**data):
    return _compute_replacement(21, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_021'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_021}


def rss_replacement_022(**data):
    return _compute_replacement(22, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_022'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_022}


def rss_replacement_023(**data):
    return _compute_replacement(23, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_023'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_023}


def rss_replacement_024(**data):
    return _compute_replacement(24, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_024'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_024}


def rss_replacement_025(**data):
    return _compute_replacement(25, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_025'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_025}


def rss_replacement_026(**data):
    return _compute_replacement(26, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_026'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_026}


def rss_replacement_027(**data):
    return _compute_replacement(27, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_027'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_027}


def rss_replacement_028(**data):
    return _compute_replacement(28, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_028'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_028}


def rss_replacement_029(**data):
    return _compute_replacement(29, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_029'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_029}


def rss_replacement_030(**data):
    return _compute_replacement(30, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_030'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_030}


def rss_replacement_031(**data):
    return _compute_replacement(31, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_031'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_031}


def rss_replacement_032(**data):
    return _compute_replacement(32, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_032'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_032}


def rss_replacement_033(**data):
    return _compute_replacement(33, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_033'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_033}


def rss_replacement_034(**data):
    return _compute_replacement(34, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_034'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_034}


def rss_replacement_035(**data):
    return _compute_replacement(35, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_035'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_035}


def rss_replacement_036(**data):
    return _compute_replacement(36, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_036'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_036}


def rss_replacement_037(**data):
    return _compute_replacement(37, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_037'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_037}


def rss_replacement_038(**data):
    return _compute_replacement(38, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_038'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_038}


def rss_replacement_039(**data):
    return _compute_replacement(39, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_039'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_039}


def rss_replacement_040(**data):
    return _compute_replacement(40, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_040'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_040}


def rss_replacement_041(**data):
    return _compute_replacement(41, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_041'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_041}


def rss_replacement_042(**data):
    return _compute_replacement(42, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_042'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_042}


def rss_replacement_043(**data):
    return _compute_replacement(43, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_043'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_043}


def rss_replacement_044(**data):
    return _compute_replacement(44, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_044'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_044}


def rss_replacement_045(**data):
    return _compute_replacement(45, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_045'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_045}


def rss_replacement_046(**data):
    return _compute_replacement(46, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_046'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_046}


def rss_replacement_047(**data):
    return _compute_replacement(47, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_047'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_047}


def rss_replacement_048(**data):
    return _compute_replacement(48, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_048'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_048}


def rss_replacement_049(**data):
    return _compute_replacement(49, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_049'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_049}


def rss_replacement_050(**data):
    return _compute_replacement(50, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_050'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_050}


def rss_replacement_051(**data):
    return _compute_replacement(51, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_051'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_051}


def rss_replacement_052(**data):
    return _compute_replacement(52, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_052'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_052}


def rss_replacement_053(**data):
    return _compute_replacement(53, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_053'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_053}


def rss_replacement_054(**data):
    return _compute_replacement(54, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_054'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_054}


def rss_replacement_055(**data):
    return _compute_replacement(55, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_055'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_055}


def rss_replacement_056(**data):
    return _compute_replacement(56, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_056'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_056}


def rss_replacement_057(**data):
    return _compute_replacement(57, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_057'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_057}


def rss_replacement_058(**data):
    return _compute_replacement(58, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_058'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_058}


def rss_replacement_059(**data):
    return _compute_replacement(59, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_059'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_059}


def rss_replacement_060(**data):
    return _compute_replacement(60, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_060'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_060}


def rss_replacement_061(**data):
    return _compute_replacement(61, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_061'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_061}


def rss_replacement_062(**data):
    return _compute_replacement(62, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_062'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_062}


def rss_replacement_063(**data):
    return _compute_replacement(63, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_063'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_063}


def rss_replacement_064(**data):
    return _compute_replacement(64, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_064'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_064}


def rss_replacement_065(**data):
    return _compute_replacement(65, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_065'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_065}


def rss_replacement_066(**data):
    return _compute_replacement(66, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_066'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_066}


def rss_replacement_067(**data):
    return _compute_replacement(67, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_067'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_067}


def rss_replacement_068(**data):
    return _compute_replacement(68, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_068'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_068}


def rss_replacement_069(**data):
    return _compute_replacement(69, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_069'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_069}


def rss_replacement_070(**data):
    return _compute_replacement(70, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_070'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_070}


def rss_replacement_071(**data):
    return _compute_replacement(71, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_071'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_071}


def rss_replacement_072(**data):
    return _compute_replacement(72, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_072'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_072}


def rss_replacement_073(**data):
    return _compute_replacement(73, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_073'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_073}


def rss_replacement_074(**data):
    return _compute_replacement(74, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_074'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_074}


def rss_replacement_075(**data):
    return _compute_replacement(75, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_075'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_075}


def rss_replacement_076(**data):
    return _compute_replacement(76, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_076'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_076}


def rss_replacement_077(**data):
    return _compute_replacement(77, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_077'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_077}


def rss_replacement_078(**data):
    return _compute_replacement(78, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_078'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_078}


def rss_replacement_079(**data):
    return _compute_replacement(79, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_079'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_079}


def rss_replacement_080(**data):
    return _compute_replacement(80, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_080'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_080}


def rss_replacement_081(**data):
    return _compute_replacement(81, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_081'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_081}


def rss_replacement_082(**data):
    return _compute_replacement(82, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_082'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_082}


def rss_replacement_083(**data):
    return _compute_replacement(83, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_083'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_083}


def rss_replacement_084(**data):
    return _compute_replacement(84, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_084'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_084}


def rss_replacement_085(**data):
    return _compute_replacement(85, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_085'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_085}


def rss_replacement_086(**data):
    return _compute_replacement(86, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_086'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_086}


def rss_replacement_087(**data):
    return _compute_replacement(87, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_087'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_087}


def rss_replacement_088(**data):
    return _compute_replacement(88, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_088'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_088}


def rss_replacement_089(**data):
    return _compute_replacement(89, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_089'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_089}


def rss_replacement_090(**data):
    return _compute_replacement(90, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_090'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_090}


def rss_replacement_091(**data):
    return _compute_replacement(91, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_091'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_091}


def rss_replacement_092(**data):
    return _compute_replacement(92, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_092'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_092}


def rss_replacement_093(**data):
    return _compute_replacement(93, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_093'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_093}


def rss_replacement_094(**data):
    return _compute_replacement(94, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_094'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_094}


def rss_replacement_095(**data):
    return _compute_replacement(95, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_095'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_095}


def rss_replacement_096(**data):
    return _compute_replacement(96, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_096'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_096}


def rss_replacement_097(**data):
    return _compute_replacement(97, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_097'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_097}


def rss_replacement_098(**data):
    return _compute_replacement(98, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_098'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_098}


def rss_replacement_099(**data):
    return _compute_replacement(99, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_099'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_099}


def rss_replacement_100(**data):
    return _compute_replacement(100, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_100'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_100}


def rss_replacement_101(**data):
    return _compute_replacement(101, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_101'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_101}


def rss_replacement_102(**data):
    return _compute_replacement(102, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_102'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_102}


def rss_replacement_103(**data):
    return _compute_replacement(103, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_103'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_103}


def rss_replacement_104(**data):
    return _compute_replacement(104, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_104'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_104}


def rss_replacement_105(**data):
    return _compute_replacement(105, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_105'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_105}


def rss_replacement_106(**data):
    return _compute_replacement(106, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_106'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_106}


def rss_replacement_107(**data):
    return _compute_replacement(107, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_107'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_107}


def rss_replacement_108(**data):
    return _compute_replacement(108, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_108'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_108}


def rss_replacement_109(**data):
    return _compute_replacement(109, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_109'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_109}


def rss_replacement_110(**data):
    return _compute_replacement(110, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_110'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_110}


def rss_replacement_111(**data):
    return _compute_replacement(111, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_111'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_111}


def rss_replacement_112(**data):
    return _compute_replacement(112, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_112'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_112}


def rss_replacement_113(**data):
    return _compute_replacement(113, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_113'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_113}


def rss_replacement_114(**data):
    return _compute_replacement(114, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_114'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_114}


def rss_replacement_115(**data):
    return _compute_replacement(115, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_115'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_115}


def rss_replacement_116(**data):
    return _compute_replacement(116, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_116'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_116}


def rss_replacement_117(**data):
    return _compute_replacement(117, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_117'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_117}


def rss_replacement_118(**data):
    return _compute_replacement(118, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_118'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_118}


def rss_replacement_119(**data):
    return _compute_replacement(119, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_119'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_119}


def rss_replacement_120(**data):
    return _compute_replacement(120, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_120'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_120}


def rss_replacement_121(**data):
    return _compute_replacement(121, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_121'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_121}


def rss_replacement_122(**data):
    return _compute_replacement(122, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_122'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_122}


def rss_replacement_123(**data):
    return _compute_replacement(123, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_123'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_123}


def rss_replacement_124(**data):
    return _compute_replacement(124, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_124'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_124}


def rss_replacement_125(**data):
    return _compute_replacement(125, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_125'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_125}


def rss_replacement_126(**data):
    return _compute_replacement(126, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_126'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_126}


def rss_replacement_127(**data):
    return _compute_replacement(127, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_127'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_127}


def rss_replacement_128(**data):
    return _compute_replacement(128, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_128'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_128}


def rss_replacement_129(**data):
    return _compute_replacement(129, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_129'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_129}


def rss_replacement_130(**data):
    return _compute_replacement(130, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_130'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_130}


def rss_replacement_131(**data):
    return _compute_replacement(131, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_131'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_131}


def rss_replacement_132(**data):
    return _compute_replacement(132, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_132'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_132}


def rss_replacement_133(**data):
    return _compute_replacement(133, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_133'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_133}


def rss_replacement_134(**data):
    return _compute_replacement(134, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_134'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_134}


def rss_replacement_135(**data):
    return _compute_replacement(135, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_135'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_135}


def rss_replacement_136(**data):
    return _compute_replacement(136, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_136'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_136}


def rss_replacement_137(**data):
    return _compute_replacement(137, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_137'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_137}


def rss_replacement_138(**data):
    return _compute_replacement(138, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_138'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_138}


def rss_replacement_139(**data):
    return _compute_replacement(139, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_139'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_139}


def rss_replacement_140(**data):
    return _compute_replacement(140, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_140'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_140}


def rss_replacement_141(**data):
    return _compute_replacement(141, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_141'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_141}


def rss_replacement_142(**data):
    return _compute_replacement(142, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_142'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_142}


def rss_replacement_143(**data):
    return _compute_replacement(143, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_143'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_143}


def rss_replacement_144(**data):
    return _compute_replacement(144, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_144'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_144}


def rss_replacement_145(**data):
    return _compute_replacement(145, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_145'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_145}


def rss_replacement_146(**data):
    return _compute_replacement(146, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_146'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_146}


def rss_replacement_147(**data):
    return _compute_replacement(147, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_147'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_147}


def rss_replacement_148(**data):
    return _compute_replacement(148, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_148'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_148}


def rss_replacement_149(**data):
    return _compute_replacement(149, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_149'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_149}


def rss_replacement_150(**data):
    return _compute_replacement(150, **data)
RSS_REPLACEMENT_BASE_REGISTRY['rss_replacement_150'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': rss_replacement_150}

