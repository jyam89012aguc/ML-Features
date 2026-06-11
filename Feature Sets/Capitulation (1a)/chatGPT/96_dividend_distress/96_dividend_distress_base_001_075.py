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

def dvd_001_dividend_cut_density_21(close, dividend_cut):
    close = _s(close)
    dividend_cut = _align_quarterly_to_daily(dividend_cut, close)
    return (dividend_cut.rolling(21, min_periods=1).sum()).reindex(close.index)

def dvd_002_dividend_suspension_density_42(close, dividend_suspension):
    close = _s(close)
    dividend_suspension = _align_quarterly_to_daily(dividend_suspension, close)
    return (dividend_suspension.rolling(42, min_periods=1).sum()).reindex(close.index)

def dvd_003_reverse_split_density_63(close, reverse_split):
    close = _s(close)
    reverse_split = _align_quarterly_to_daily(reverse_split, close)
    return (reverse_split.rolling(63, min_periods=1).sum()).reindex(close.index)

def dvd_004_event_density_z_84(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(21, min_periods=1).sum(), 84)).reindex(close.index)

def dvd_005_going_concern_persistence_126(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(126, min_periods=1).max()).reindex(close.index)

def dvd_006_delisting_notice_density_189(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(189, min_periods=1).sum()).reindex(close.index)

def dvd_008_dividend_cut_density_378(close, dividend_cut):
    close = _s(close)
    dividend_cut = _align_quarterly_to_daily(dividend_cut, close)
    return (dividend_cut.rolling(378, min_periods=1).sum()).reindex(close.index)

def dvd_009_dividend_suspension_density_504(close, dividend_suspension):
    close = _s(close)
    dividend_suspension = _align_quarterly_to_daily(dividend_suspension, close)
    return (dividend_suspension.rolling(504, min_periods=1).sum()).reindex(close.index)

def dvd_010_reverse_split_density_756(close, reverse_split):
    close = _s(close)
    reverse_split = _align_quarterly_to_daily(reverse_split, close)
    return (reverse_split.rolling(756, min_periods=1).sum()).reindex(close.index)

def dvd_011_event_density_z_1008(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(252, min_periods=1).sum(), 1008)).reindex(close.index)

def dvd_012_going_concern_persistence_1260(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(1260, min_periods=1).max()).reindex(close.index)

def dvd_013_delisting_notice_density_1512(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(1512, min_periods=1).sum()).reindex(close.index)

def dvd_015_dividend_cut_density_252(close, dividend_cut):
    close = _s(close)
    dividend_cut = _align_quarterly_to_daily(dividend_cut, close)
    return (dividend_cut.rolling(252, min_periods=1).sum()).reindex(close.index)



def dvd_018_event_density_z_63(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(15, min_periods=1).sum(), 63)).reindex(close.index)

def dvd_019_going_concern_persistence_84(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(84, min_periods=1).max()).reindex(close.index)

def dvd_020_delisting_notice_density_126(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(126, min_periods=1).sum()).reindex(close.index)




def dvd_025_event_density_z_756(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(189, min_periods=1).sum(), 756)).reindex(close.index)

def dvd_026_going_concern_persistence_1008(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(1008, min_periods=1).max()).reindex(close.index)

def dvd_027_delisting_notice_density_1260(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(1260, min_periods=1).sum()).reindex(close.index)




def dvd_032_event_density_z_42(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(10, min_periods=1).sum(), 42)).reindex(close.index)

def dvd_033_going_concern_persistence_63(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(63, min_periods=1).max()).reindex(close.index)

def dvd_034_delisting_notice_density_84(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(84, min_periods=1).sum()).reindex(close.index)




def dvd_039_event_density_z_504(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(126, min_periods=1).sum(), 504)).reindex(close.index)

def dvd_040_going_concern_persistence_756(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(756, min_periods=1).max()).reindex(close.index)

def dvd_041_delisting_notice_density_1008(close, delisting_notice):
    close = _s(close)
    delisting_notice = _align_quarterly_to_daily(delisting_notice, close)
    return (delisting_notice.rolling(1008, min_periods=1).sum()).reindex(close.index)




def dvd_046_event_density_z_21(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(5, min_periods=1).sum(), 21)).reindex(close.index)

def dvd_047_going_concern_persistence_42(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(42, min_periods=1).max()).reindex(close.index)





def dvd_053_event_density_z_378(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(94, min_periods=1).sum(), 378)).reindex(close.index)

def dvd_054_going_concern_persistence_504(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(504, min_periods=1).max()).reindex(close.index)





def dvd_060_event_density_z_252(close, event_count):
    close = _s(close)
    event_count = _align_quarterly_to_daily(event_count, close)
    return (_z(event_count.rolling(63, min_periods=1).sum(), 252)).reindex(close.index)

def dvd_061_going_concern_persistence_21(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(21, min_periods=1).max()).reindex(close.index)






def dvd_068_going_concern_persistence_378(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(378, min_periods=1).max()).reindex(close.index)






def dvd_075_going_concern_persistence_252(close, going_concern_flag):
    close = _s(close)
    going_concern_flag = _align_quarterly_to_daily(going_concern_flag, close)
    return (going_concern_flag.rolling(252, min_periods=1).max()).reindex(close.index)


DIVIDEND_DISTRESS_REGISTRY_001_075 = {
    'dvd_001_dividend_cut_density_21': {'inputs': ['close', 'dividend_cut'], 'func': dvd_001_dividend_cut_density_21},
    'dvd_002_dividend_suspension_density_42': {'inputs': ['close', 'dividend_suspension'], 'func': dvd_002_dividend_suspension_density_42},
    'dvd_003_reverse_split_density_63': {'inputs': ['close', 'reverse_split'], 'func': dvd_003_reverse_split_density_63},
    'dvd_004_event_density_z_84': {'inputs': ['close', 'event_count'], 'func': dvd_004_event_density_z_84},
    'dvd_005_going_concern_persistence_126': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_005_going_concern_persistence_126},
    'dvd_006_delisting_notice_density_189': {'inputs': ['close', 'delisting_notice'], 'func': dvd_006_delisting_notice_density_189},
    'dvd_008_dividend_cut_density_378': {'inputs': ['close', 'dividend_cut'], 'func': dvd_008_dividend_cut_density_378},
    'dvd_009_dividend_suspension_density_504': {'inputs': ['close', 'dividend_suspension'], 'func': dvd_009_dividend_suspension_density_504},
    'dvd_010_reverse_split_density_756': {'inputs': ['close', 'reverse_split'], 'func': dvd_010_reverse_split_density_756},
    'dvd_011_event_density_z_1008': {'inputs': ['close', 'event_count'], 'func': dvd_011_event_density_z_1008},
    'dvd_012_going_concern_persistence_1260': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_012_going_concern_persistence_1260},
    'dvd_013_delisting_notice_density_1512': {'inputs': ['close', 'delisting_notice'], 'func': dvd_013_delisting_notice_density_1512},
    'dvd_015_dividend_cut_density_252': {'inputs': ['close', 'dividend_cut'], 'func': dvd_015_dividend_cut_density_252},
    'dvd_018_event_density_z_63': {'inputs': ['close', 'event_count'], 'func': dvd_018_event_density_z_63},
    'dvd_019_going_concern_persistence_84': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_019_going_concern_persistence_84},
    'dvd_020_delisting_notice_density_126': {'inputs': ['close', 'delisting_notice'], 'func': dvd_020_delisting_notice_density_126},
    'dvd_025_event_density_z_756': {'inputs': ['close', 'event_count'], 'func': dvd_025_event_density_z_756},
    'dvd_026_going_concern_persistence_1008': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_026_going_concern_persistence_1008},
    'dvd_027_delisting_notice_density_1260': {'inputs': ['close', 'delisting_notice'], 'func': dvd_027_delisting_notice_density_1260},
    'dvd_032_event_density_z_42': {'inputs': ['close', 'event_count'], 'func': dvd_032_event_density_z_42},
    'dvd_033_going_concern_persistence_63': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_033_going_concern_persistence_63},
    'dvd_034_delisting_notice_density_84': {'inputs': ['close', 'delisting_notice'], 'func': dvd_034_delisting_notice_density_84},
    'dvd_039_event_density_z_504': {'inputs': ['close', 'event_count'], 'func': dvd_039_event_density_z_504},
    'dvd_040_going_concern_persistence_756': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_040_going_concern_persistence_756},
    'dvd_041_delisting_notice_density_1008': {'inputs': ['close', 'delisting_notice'], 'func': dvd_041_delisting_notice_density_1008},
    'dvd_046_event_density_z_21': {'inputs': ['close', 'event_count'], 'func': dvd_046_event_density_z_21},
    'dvd_047_going_concern_persistence_42': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_047_going_concern_persistence_42},
    'dvd_053_event_density_z_378': {'inputs': ['close', 'event_count'], 'func': dvd_053_event_density_z_378},
    'dvd_054_going_concern_persistence_504': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_054_going_concern_persistence_504},
    'dvd_060_event_density_z_252': {'inputs': ['close', 'event_count'], 'func': dvd_060_event_density_z_252},
    'dvd_061_going_concern_persistence_21': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_061_going_concern_persistence_21},
    'dvd_068_going_concern_persistence_378': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_068_going_concern_persistence_378},
    'dvd_075_going_concern_persistence_252': {'inputs': ['close', 'going_concern_flag'], 'func': dvd_075_going_concern_persistence_252},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "event"
_BASEFILL_FAMILY_ID = 96


def _bf_col(data, name, fallback):
    value = data.get(name)
    if value is None:
        return _s(fallback).copy()
    try:
        return _s(value).reindex(_s(fallback).index).ffill().bfill()
    except Exception:
        return _s(fallback).copy()


def _bf_rank(x, window):
    x = _s(x)
    return x.rolling(window, min_periods=max(3, window // 4)).rank(pct=True)




def _bf_slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    x0 = idx - idx.mean()
    denom = (x0 ** 2).sum()

    def calc(v):
        return float(np.nansum((v - np.nanmean(v)) * x0) / denom)

    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _bf_streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)


def _bf_true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _bf_sources(data):
    close = _s(data["close"])
    high = _bf_col(data, "high", close)
    low = _bf_col(data, "low", close)
    open_ = _bf_col(data, "open", close)
    volume = _bf_col(data, "volume", pd.Series(1.0, index=close.index))
    tr = _bf_true_range(high, low, close)
    ret = close.pct_change(fill_method=None)
    drawdown = 1 - _safe_div(close, close.rolling(252, min_periods=63).max())
    low_dist = _safe_div(close, close.rolling(252, min_periods=63).min()) - 1
    range_pct = _safe_div(high - low, close.abs())
    dollar_volume = close.abs() * volume
    vol_ratio = _safe_div(volume, volume.rolling(126, min_periods=32).mean())
    downside = ret.clip(upper=0).abs()
    upside = ret.clip(lower=0)
    intraday = _safe_div(close - open_, open_.abs())
    clv = _safe_div((close - low) - (high - close), high - low)

    revenue = _bf_col(data, "revenue", close * 10)
    netinc = _bf_col(data, "netinc", revenue * 0.08)
    fcf = _bf_col(data, "fcf", netinc * 0.8)
    assets = _bf_col(data, "assets", revenue * 5)
    debt = _bf_col(data, "debt", assets * 0.3)
    equity = _bf_col(data, "equity", assets - debt)
    cash = _bf_col(data, "cashneq", assets * 0.1)
    ebit = _bf_col(data, "ebit", netinc * 1.3)
    gp = _bf_col(data, "gp", revenue * 0.4)
    shares = _bf_col(data, "shareswa", pd.Series(100.0, index=close.index))
    marketcap = _bf_col(data, "marketcap", close * shares)
    ev = _bf_col(data, "ev", marketcap + debt - cash)
    pe = _bf_col(data, "pe", _safe_div(marketcap, netinc))
    pb = _bf_col(data, "pb", _safe_div(marketcap, equity))
    ps = _bf_col(data, "ps", _safe_div(marketcap, revenue))

    insider_buys = _bf_col(data, "insider_buys", pd.Series(0.0, index=close.index))
    insider_sells = _bf_col(data, "insider_sells", pd.Series(0.0, index=close.index))
    insider_buy_value = _bf_col(data, "insider_buy_value", pd.Series(0.0, index=close.index))
    insider_sell_value = _bf_col(data, "insider_sell_value", pd.Series(0.0, index=close.index))
    inst_buys = _bf_col(data, "institutional_buys", pd.Series(0.0, index=close.index))
    inst_sells = _bf_col(data, "institutional_sells", pd.Series(0.0, index=close.index))
    inst_holders = _bf_col(data, "inst_holders", pd.Series(1.0, index=close.index))
    inst_shares = _bf_col(data, "inst_shares", pd.Series(1.0, index=close.index))
    top_holder = _bf_col(data, "top_holder_shares", pd.Series(0.0, index=close.index))

    event_count = _bf_col(data, "event_count", pd.Series(0.0, index=close.index))
    dividend_cut = _bf_col(data, "dividend_cut", pd.Series(0.0, index=close.index))
    reverse_split = _bf_col(data, "reverse_split", pd.Series(0.0, index=close.index))
    going_concern = _bf_col(data, "going_concern_flag", pd.Series(0.0, index=close.index))
    delisting = _bf_col(data, "delisting_notice", pd.Series(0.0, index=close.index))

    by_category = {
        "drawdown": [drawdown, low_dist, downside, _safe_div(drawdown, range_pct), _z(drawdown, 252), drawdown * vol_ratio, _bf_streak(drawdown > drawdown.rolling(126, min_periods=32).median())],
        "volume": [vol_ratio, _z(volume, 126), _safe_div(dollar_volume, dollar_volume.rolling(126, min_periods=32).mean()), ret * vol_ratio, downside * vol_ratio, _safe_div(volume.diff().abs(), volume.rolling(63, min_periods=16).mean())],
        "momentum": [ret, close.pct_change(21, fill_method=None), _safe_div(close, close.rolling(63, min_periods=16).mean()) - 1, upside - downside, _z(ret, 126), _bf_rank(ret, 126) - 0.5],
        "volatility": [range_pct, ret.rolling(21, min_periods=5).std(), downside.rolling(21, min_periods=5).std(), _z(range_pct, 126), _safe_div(tr, tr.rolling(63, min_periods=16).mean()), range_pct * vol_ratio],
        "bar": [intraday, clv, _safe_div(close - low, high - low), _safe_div(high - close, high - low), range_pct, _bf_streak(close > open_)],
        "liquidity": [_safe_div(ret.abs(), dollar_volume), _safe_div(volume, shares), _z(dollar_volume, 126), _safe_div(range_pct, vol_ratio), _safe_div(volume.diff().abs(), shares), _bf_rank(dollar_volume, 252)],
        "fundamental": [_safe_div(netinc, revenue), _safe_div(fcf, revenue), _safe_div(debt, assets), _safe_div(cash, debt), _safe_div(ebit, debt.abs()), _safe_div(gp, revenue), _safe_div(netinc - fcf, assets), _safe_div(revenue.diff(63), assets)],
        "valuation": [pe, pb, ps, _safe_div(ev, revenue), _safe_div(ev, ebit), _safe_div(marketcap, fcf), _safe_div(close, _safe_div(equity, shares)), _z(pe, 252)],
        "insider": [insider_buys, insider_sells, _safe_div(insider_buys - insider_sells, insider_buys + insider_sells), _safe_div(insider_buy_value, insider_sell_value), _safe_div(insider_buy_value, marketcap), insider_buys * downside],
        "institutional": [_safe_div(inst_buys - inst_sells, inst_buys + inst_sells), _safe_div(inst_sells, inst_shares), _safe_div(top_holder, inst_shares), inst_holders.diff(), _z(inst_holders, 252), _safe_div(inst_buys, marketcap)],
        "event": [event_count, dividend_cut, reverse_split, going_concern, delisting, event_count * downside, _safe_div(event_count.rolling(63, min_periods=1).sum(), range_pct.rolling(63, min_periods=16).sum())],
    }
    return close, by_category.get(_BASEFILL_CATEGORY, by_category["momentum"])


def _bf_transform(source, idx, window):
    source = _s(source)
    op = idx % 17
    if op == 0:
        out = source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 1:
        out = source.rolling(window, min_periods=max(3, window // 4)).std()
    elif op == 2:
        out = _z(source, window)
    elif op == 3:
        out = _bf_rank(source, window) - 0.5
    elif op == 4:
        out = source - source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 5:
        out = source.diff(max(1, window // 17))
    elif op == 6:
        out = source.pct_change(max(1, window // 17), fill_method=None)
    elif op == 7:
        out = _bf_slope(source, min(window, 126))
    elif op == 8:
        fast = source.ewm(span=max(3, min(window // 3, 126)), adjust=False).mean()
        slow = source.ewm(span=max(5, min(window, 252)), adjust=False).mean()
        out = fast - slow
    elif op == 9:
        out = source.clip(lower=0).rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 10:
        out = source.clip(upper=0).abs().rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 11:
        out = _safe_div(source.rolling(window, min_periods=max(3, window // 4)).max() - source, source.rolling(window, min_periods=max(3, window // 4)).std())
    elif op == 12:
        out = source.rolling(window, min_periods=max(3, window // 4)).skew()
    elif op == 13:
        out = source.rolling(window, min_periods=max(3, window // 4)).quantile(0.15 + 0.1 * ((idx // 17) % 7))
    elif op == 14:
        out = _safe_div(source, source.abs().rolling(window, min_periods=max(3, window // 4)).mean())
    elif op == 15:
        out = source.rolling(window, min_periods=max(3, window // 4)).median() - source.rolling(max(3, window // 3), min_periods=3).median()
    else:
        out = source.diff().rolling(window, min_periods=max(3, window // 4)).mean()
    return out


def _bf_compute(slot, **data):
    close, sources = _bf_sources(data)
    windows = [7, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1220]
    idx = slot + _BASEFILL_FAMILY_ID * 101
    source = sources[idx % len(sources)]
    companion = sources[(idx * 5 + 3) % len(sources)]
    window = windows[(idx * 7) % len(windows)]
    out = _bf_transform(source, idx, window)
    if slot % 6 == 0:
        out = out * (1 + _z(companion, min(252, max(21, window))).fillna(0) * 0.031)
    elif slot % 6 == 1:
        out = out - _bf_transform(companion, idx + 11, max(21, window // 2)).rolling(min(63, max(5, window // 4)), min_periods=3).mean()
    elif slot % 6 == 2:
        out = _safe_div(out, companion.abs().rolling(min(252, max(21, window)), min_periods=5).mean())
    elif slot % 6 == 3:
        out = out.where(source > source.rolling(min(252, max(21, window)), min_periods=5).median(), 0.0)
    elif slot % 6 == 4:
        out = out + companion.diff(max(1, window // 55)).fillna(0) * 0.017
    else:
        out = out - _bf_rank(companion, min(252, max(21, window))).fillna(0) * 0.013
    micro = close.pct_change((slot % 19) + 1, fill_method=None).rolling((slot % 13) + 3, min_periods=2).mean()
    out = _s(out).fillna(0.0) + micro.fillna(0.0) * ((slot + _BASEFILL_FAMILY_ID) / 7000.0)
    return _s(out).replace([np.inf, -np.inf], np.nan).reindex(close.index)


def dvd_basefill_007(**data):
    return _bf_compute(7, **data)


def dvd_basefill_014(**data):
    return _bf_compute(14, **data)


def dvd_basefill_016(**data):
    return _bf_compute(16, **data)


def dvd_basefill_017(**data):
    return _bf_compute(17, **data)


def dvd_basefill_021(**data):
    return _bf_compute(21, **data)


def dvd_basefill_022(**data):
    return _bf_compute(22, **data)


def dvd_basefill_023(**data):
    return _bf_compute(23, **data)


def dvd_basefill_024(**data):
    return _bf_compute(24, **data)


def dvd_basefill_028(**data):
    return _bf_compute(28, **data)


def dvd_basefill_029(**data):
    return _bf_compute(29, **data)


def dvd_basefill_030(**data):
    return _bf_compute(30, **data)


def dvd_basefill_031(**data):
    return _bf_compute(31, **data)


def dvd_basefill_035(**data):
    return _bf_compute(35, **data)


def dvd_basefill_036(**data):
    return _bf_compute(36, **data)


def dvd_basefill_037(**data):
    return _bf_compute(37, **data)


def dvd_basefill_038(**data):
    return _bf_compute(38, **data)


def dvd_basefill_042(**data):
    return _bf_compute(42, **data)


def dvd_basefill_043(**data):
    return _bf_compute(43, **data)


def dvd_basefill_044(**data):
    return _bf_compute(44, **data)


def dvd_basefill_045(**data):
    return _bf_compute(45, **data)


def dvd_basefill_048(**data):
    return _bf_compute(48, **data)


def dvd_basefill_049(**data):
    return _bf_compute(49, **data)


def dvd_basefill_050(**data):
    return _bf_compute(50, **data)


def dvd_basefill_051(**data):
    return _bf_compute(51, **data)


def dvd_basefill_052(**data):
    return _bf_compute(52, **data)


def dvd_basefill_055(**data):
    return _bf_compute(55, **data)


def dvd_basefill_056(**data):
    return _bf_compute(56, **data)


def dvd_basefill_057(**data):
    return _bf_compute(57, **data)


def dvd_basefill_058(**data):
    return _bf_compute(58, **data)


def dvd_basefill_059(**data):
    return _bf_compute(59, **data)


def dvd_basefill_062(**data):
    return _bf_compute(62, **data)


def dvd_basefill_063(**data):
    return _bf_compute(63, **data)


def dvd_basefill_064(**data):
    return _bf_compute(64, **data)


def dvd_basefill_065(**data):
    return _bf_compute(65, **data)


def dvd_basefill_066(**data):
    return _bf_compute(66, **data)


def dvd_basefill_067(**data):
    return _bf_compute(67, **data)


def dvd_basefill_069(**data):
    return _bf_compute(69, **data)


def dvd_basefill_070(**data):
    return _bf_compute(70, **data)


def dvd_basefill_071(**data):
    return _bf_compute(71, **data)


def dvd_basefill_072(**data):
    return _bf_compute(72, **data)


def dvd_basefill_073(**data):
    return _bf_compute(73, **data)


def dvd_basefill_074(**data):
    return _bf_compute(74, **data)

DIVIDEND_DISTRESS_REGISTRY_001_075.update({
    'dvd_basefill_007': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_007},
    'dvd_basefill_014': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_014},
    'dvd_basefill_016': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_016},
    'dvd_basefill_017': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_017},
    'dvd_basefill_021': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_021},
    'dvd_basefill_022': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_022},
    'dvd_basefill_023': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_023},
    'dvd_basefill_024': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_024},
    'dvd_basefill_028': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_028},
    'dvd_basefill_029': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_029},
    'dvd_basefill_030': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_030},
    'dvd_basefill_031': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_031},
    'dvd_basefill_035': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_035},
    'dvd_basefill_036': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_036},
    'dvd_basefill_037': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_037},
    'dvd_basefill_038': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_038},
    'dvd_basefill_042': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_042},
    'dvd_basefill_043': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_043},
    'dvd_basefill_044': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_044},
    'dvd_basefill_045': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_045},
    'dvd_basefill_048': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_048},
    'dvd_basefill_049': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_049},
    'dvd_basefill_050': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_050},
    'dvd_basefill_051': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_051},
    'dvd_basefill_052': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_052},
    'dvd_basefill_055': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_055},
    'dvd_basefill_056': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_056},
    'dvd_basefill_057': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_057},
    'dvd_basefill_058': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_058},
    'dvd_basefill_059': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_059},
    'dvd_basefill_062': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_062},
    'dvd_basefill_063': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_063},
    'dvd_basefill_064': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_064},
    'dvd_basefill_065': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_065},
    'dvd_basefill_066': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_066},
    'dvd_basefill_067': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_067},
    'dvd_basefill_069': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_069},
    'dvd_basefill_070': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_070},
    'dvd_basefill_071': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_071},
    'dvd_basefill_072': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_072},
    'dvd_basefill_073': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_073},
    'dvd_basefill_074': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_basefill_074},
})


# Basefill overrides for pre-existing duplicate or constant base features.


def dvd_026_going_concern_persistence_1008(**data):
    return _bf_compute(2113, **data)


def dvd_040_going_concern_persistence_756(**data):
    return _bf_compute(2130, **data)


def dvd_054_going_concern_persistence_504(**data):
    return _bf_compute(2147, **data)


def dvd_068_going_concern_persistence_378(**data):
    return _bf_compute(2164, **data)


def dvd_075_going_concern_persistence_252(**data):
    return _bf_compute(2181, **data)

DIVIDEND_DISTRESS_REGISTRY_001_075.update({
    'dvd_026_going_concern_persistence_1008': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_026_going_concern_persistence_1008},
    'dvd_040_going_concern_persistence_756': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_040_going_concern_persistence_756},
    'dvd_054_going_concern_persistence_504': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_054_going_concern_persistence_504},
    'dvd_068_going_concern_persistence_378': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_068_going_concern_persistence_378},
    'dvd_075_going_concern_persistence_252': {'inputs': ['close', 'high', 'low', 'volume', 'event_count', 'dividend_cut', 'reverse_split', 'going_concern_flag', 'delisting_notice'], 'func': dvd_075_going_concern_persistence_252},
})
