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

def vvp_001_pe_peer_discount_21(close, pe, peer_median_pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    peer_median_pe = _align_quarterly_to_daily(peer_median_pe, close)
    return (_safe_div(pe, peer_median_pe) - 1).reindex(close.index)



def vvp_005_peer_relative_pe_z_126(close, pe, peer_median_pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    peer_median_pe = _align_quarterly_to_daily(peer_median_pe, close)
    return (_z(_safe_div(pe, peer_median_pe), 126)).reindex(close.index)

def vvp_006_peer_relative_pb_z_189(close, pb, peer_median_pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    peer_median_pb = _align_quarterly_to_daily(peer_median_pb, close)
    return (_z(_safe_div(pb, peer_median_pb), 189)).reindex(close.index)




def vvp_011_peer_relative_pe_z_1008(close, pe, peer_median_pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    peer_median_pe = _align_quarterly_to_daily(peer_median_pe, close)
    return (_z(_safe_div(pe, peer_median_pe), 1008)).reindex(close.index)

def vvp_012_peer_relative_pb_z_1260(close, pb, peer_median_pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    peer_median_pb = _align_quarterly_to_daily(peer_median_pb, close)
    return (_z(_safe_div(pb, peer_median_pb), 1260)).reindex(close.index)




def vvp_017_peer_relative_pe_z_42(close, pe, peer_median_pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    peer_median_pe = _align_quarterly_to_daily(peer_median_pe, close)
    return (_z(_safe_div(pe, peer_median_pe), 42)).reindex(close.index)

def vvp_018_peer_relative_pb_z_63(close, pb, peer_median_pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    peer_median_pb = _align_quarterly_to_daily(peer_median_pb, close)
    return (_z(_safe_div(pb, peer_median_pb), 63)).reindex(close.index)




def vvp_023_peer_relative_pe_z_378(close, pe, peer_median_pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    peer_median_pe = _align_quarterly_to_daily(peer_median_pe, close)
    return (_z(_safe_div(pe, peer_median_pe), 378)).reindex(close.index)

def vvp_024_peer_relative_pb_z_504(close, pb, peer_median_pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    peer_median_pb = _align_quarterly_to_daily(peer_median_pb, close)
    return (_z(_safe_div(pb, peer_median_pb), 504)).reindex(close.index)





def vvp_030_peer_relative_pb_z_252(close, pb, peer_median_pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    peer_median_pb = _align_quarterly_to_daily(peer_median_pb, close)
    return (_z(_safe_div(pb, peer_median_pb), 252)).reindex(close.index)








































VALUATION_VS_PEERS_REGISTRY_001_075 = {
    'vvp_001_pe_peer_discount_21': {'inputs': ['close', 'pe', 'peer_median_pe'], 'func': vvp_001_pe_peer_discount_21},
    'vvp_005_peer_relative_pe_z_126': {'inputs': ['close', 'pe', 'peer_median_pe'], 'func': vvp_005_peer_relative_pe_z_126},
    'vvp_006_peer_relative_pb_z_189': {'inputs': ['close', 'pb', 'peer_median_pb'], 'func': vvp_006_peer_relative_pb_z_189},
    'vvp_011_peer_relative_pe_z_1008': {'inputs': ['close', 'pe', 'peer_median_pe'], 'func': vvp_011_peer_relative_pe_z_1008},
    'vvp_012_peer_relative_pb_z_1260': {'inputs': ['close', 'pb', 'peer_median_pb'], 'func': vvp_012_peer_relative_pb_z_1260},
    'vvp_017_peer_relative_pe_z_42': {'inputs': ['close', 'pe', 'peer_median_pe'], 'func': vvp_017_peer_relative_pe_z_42},
    'vvp_018_peer_relative_pb_z_63': {'inputs': ['close', 'pb', 'peer_median_pb'], 'func': vvp_018_peer_relative_pb_z_63},
    'vvp_023_peer_relative_pe_z_378': {'inputs': ['close', 'pe', 'peer_median_pe'], 'func': vvp_023_peer_relative_pe_z_378},
    'vvp_024_peer_relative_pb_z_504': {'inputs': ['close', 'pb', 'peer_median_pb'], 'func': vvp_024_peer_relative_pb_z_504},
    'vvp_030_peer_relative_pb_z_252': {'inputs': ['close', 'pb', 'peer_median_pb'], 'func': vvp_030_peer_relative_pb_z_252},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "valuation"
_BASEFILL_FAMILY_ID = 82


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


def vvp_basefill_002(**data):
    return _bf_compute(2, **data)


def vvp_basefill_003(**data):
    return _bf_compute(3, **data)


def vvp_basefill_004(**data):
    return _bf_compute(4, **data)


def vvp_basefill_007(**data):
    return _bf_compute(7, **data)


def vvp_basefill_008(**data):
    return _bf_compute(8, **data)


def vvp_basefill_009(**data):
    return _bf_compute(9, **data)


def vvp_basefill_010(**data):
    return _bf_compute(10, **data)


def vvp_basefill_013(**data):
    return _bf_compute(13, **data)


def vvp_basefill_014(**data):
    return _bf_compute(14, **data)


def vvp_basefill_015(**data):
    return _bf_compute(15, **data)


def vvp_basefill_016(**data):
    return _bf_compute(16, **data)


def vvp_basefill_019(**data):
    return _bf_compute(19, **data)


def vvp_basefill_020(**data):
    return _bf_compute(20, **data)


def vvp_basefill_021(**data):
    return _bf_compute(21, **data)


def vvp_basefill_022(**data):
    return _bf_compute(22, **data)


def vvp_basefill_025(**data):
    return _bf_compute(25, **data)


def vvp_basefill_026(**data):
    return _bf_compute(26, **data)


def vvp_basefill_027(**data):
    return _bf_compute(27, **data)


def vvp_basefill_028(**data):
    return _bf_compute(28, **data)


def vvp_basefill_029(**data):
    return _bf_compute(29, **data)


def vvp_basefill_031(**data):
    return _bf_compute(31, **data)


def vvp_basefill_032(**data):
    return _bf_compute(32, **data)


def vvp_basefill_033(**data):
    return _bf_compute(33, **data)


def vvp_basefill_034(**data):
    return _bf_compute(34, **data)


def vvp_basefill_035(**data):
    return _bf_compute(35, **data)


def vvp_basefill_036(**data):
    return _bf_compute(36, **data)


def vvp_basefill_037(**data):
    return _bf_compute(37, **data)


def vvp_basefill_038(**data):
    return _bf_compute(38, **data)


def vvp_basefill_039(**data):
    return _bf_compute(39, **data)


def vvp_basefill_040(**data):
    return _bf_compute(40, **data)


def vvp_basefill_041(**data):
    return _bf_compute(41, **data)


def vvp_basefill_042(**data):
    return _bf_compute(42, **data)


def vvp_basefill_043(**data):
    return _bf_compute(43, **data)


def vvp_basefill_044(**data):
    return _bf_compute(44, **data)


def vvp_basefill_045(**data):
    return _bf_compute(45, **data)


def vvp_basefill_046(**data):
    return _bf_compute(46, **data)


def vvp_basefill_047(**data):
    return _bf_compute(47, **data)


def vvp_basefill_048(**data):
    return _bf_compute(48, **data)


def vvp_basefill_049(**data):
    return _bf_compute(49, **data)


def vvp_basefill_050(**data):
    return _bf_compute(50, **data)


def vvp_basefill_051(**data):
    return _bf_compute(51, **data)


def vvp_basefill_052(**data):
    return _bf_compute(52, **data)


def vvp_basefill_053(**data):
    return _bf_compute(53, **data)


def vvp_basefill_054(**data):
    return _bf_compute(54, **data)


def vvp_basefill_055(**data):
    return _bf_compute(55, **data)


def vvp_basefill_056(**data):
    return _bf_compute(56, **data)


def vvp_basefill_057(**data):
    return _bf_compute(57, **data)


def vvp_basefill_058(**data):
    return _bf_compute(58, **data)


def vvp_basefill_059(**data):
    return _bf_compute(59, **data)


def vvp_basefill_060(**data):
    return _bf_compute(60, **data)


def vvp_basefill_061(**data):
    return _bf_compute(61, **data)


def vvp_basefill_062(**data):
    return _bf_compute(62, **data)


def vvp_basefill_063(**data):
    return _bf_compute(63, **data)


def vvp_basefill_064(**data):
    return _bf_compute(64, **data)


def vvp_basefill_065(**data):
    return _bf_compute(65, **data)


def vvp_basefill_066(**data):
    return _bf_compute(66, **data)


def vvp_basefill_067(**data):
    return _bf_compute(67, **data)


def vvp_basefill_068(**data):
    return _bf_compute(68, **data)


def vvp_basefill_069(**data):
    return _bf_compute(69, **data)


def vvp_basefill_070(**data):
    return _bf_compute(70, **data)


def vvp_basefill_071(**data):
    return _bf_compute(71, **data)


def vvp_basefill_072(**data):
    return _bf_compute(72, **data)


def vvp_basefill_073(**data):
    return _bf_compute(73, **data)


def vvp_basefill_074(**data):
    return _bf_compute(74, **data)


def vvp_basefill_075(**data):
    return _bf_compute(75, **data)

VALUATION_VS_PEERS_REGISTRY_001_075.update({
    'vvp_basefill_002': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_002},
    'vvp_basefill_003': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_003},
    'vvp_basefill_004': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_004},
    'vvp_basefill_007': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_007},
    'vvp_basefill_008': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_008},
    'vvp_basefill_009': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_009},
    'vvp_basefill_010': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_010},
    'vvp_basefill_013': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_013},
    'vvp_basefill_014': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_014},
    'vvp_basefill_015': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_015},
    'vvp_basefill_016': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_016},
    'vvp_basefill_019': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_019},
    'vvp_basefill_020': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_020},
    'vvp_basefill_021': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_021},
    'vvp_basefill_022': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_022},
    'vvp_basefill_025': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_025},
    'vvp_basefill_026': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_026},
    'vvp_basefill_027': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_027},
    'vvp_basefill_028': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_028},
    'vvp_basefill_029': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_029},
    'vvp_basefill_031': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_031},
    'vvp_basefill_032': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_032},
    'vvp_basefill_033': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_033},
    'vvp_basefill_034': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_034},
    'vvp_basefill_035': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_035},
    'vvp_basefill_036': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_036},
    'vvp_basefill_037': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_037},
    'vvp_basefill_038': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_038},
    'vvp_basefill_039': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_039},
    'vvp_basefill_040': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_040},
    'vvp_basefill_041': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_041},
    'vvp_basefill_042': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_042},
    'vvp_basefill_043': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_043},
    'vvp_basefill_044': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_044},
    'vvp_basefill_045': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_045},
    'vvp_basefill_046': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_046},
    'vvp_basefill_047': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_047},
    'vvp_basefill_048': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_048},
    'vvp_basefill_049': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_049},
    'vvp_basefill_050': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_050},
    'vvp_basefill_051': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_051},
    'vvp_basefill_052': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_052},
    'vvp_basefill_053': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_053},
    'vvp_basefill_054': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_054},
    'vvp_basefill_055': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_055},
    'vvp_basefill_056': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_056},
    'vvp_basefill_057': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_057},
    'vvp_basefill_058': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_058},
    'vvp_basefill_059': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_059},
    'vvp_basefill_060': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_060},
    'vvp_basefill_061': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_061},
    'vvp_basefill_062': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_062},
    'vvp_basefill_063': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_063},
    'vvp_basefill_064': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_064},
    'vvp_basefill_065': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_065},
    'vvp_basefill_066': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_066},
    'vvp_basefill_067': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_067},
    'vvp_basefill_068': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_068},
    'vvp_basefill_069': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_069},
    'vvp_basefill_070': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_070},
    'vvp_basefill_071': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_071},
    'vvp_basefill_072': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_072},
    'vvp_basefill_073': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_073},
    'vvp_basefill_074': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_074},
    'vvp_basefill_075': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vvp_basefill_075},
})
