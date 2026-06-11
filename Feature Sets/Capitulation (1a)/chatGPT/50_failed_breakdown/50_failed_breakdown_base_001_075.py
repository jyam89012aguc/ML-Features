import numpy as np
import pandas as pd

def _s(x):
    return pd.Series(x).astype(float)

def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b

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

def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)

def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)

def fbd_001_gap_down_frequency_5_001(close, open):
    close = _s(close)
    open = _s(open)
    return ((open < close.shift(1)).astype(float).rolling(5, min_periods=max(3, 5//4)).mean()).reindex(close.index)

def fbd_002_gap_magnitude_10_002(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(open - close.shift(1), close.shift(1)).rolling(10, min_periods=max(3, 10//4)).mean()).reindex(close.index)

def fbd_003_open_close_pressure_21_003(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(close - open, open).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)

def fbd_004_lower_wick_ratio_42_004(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(np.minimum(open, close) - low, high - low).rolling(42, min_periods=max(3, 42//4)).mean()).reindex(close.index)

def fbd_005_upper_wick_ratio_63_005(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(high - np.maximum(open, close), high - low).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)

def fbd_006_body_to_range_84_006(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div((close - open).abs(), high - low).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(close.index)

def fbd_007_gap_down_frequency_126_007(close, open):
    close = _s(close)
    open = _s(open)
    return ((open < close.shift(1)).astype(float).rolling(126, min_periods=max(3, 126//4)).mean()).reindex(close.index)

def fbd_008_gap_magnitude_189_008(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(open - close.shift(1), close.shift(1)).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(close.index)

def fbd_009_open_close_pressure_252_009(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(close - open, open).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)

def fbd_010_lower_wick_ratio_378_010(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(np.minimum(open, close) - low, high - low).rolling(378, min_periods=max(3, 378//4)).mean()).reindex(close.index)

def fbd_011_upper_wick_ratio_504_011(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(high - np.maximum(open, close), high - low).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(close.index)

def fbd_012_body_to_range_756_012(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div((close - open).abs(), high - low).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(close.index)

def fbd_013_gap_down_frequency_1008_013(close, open):
    close = _s(close)
    open = _s(open)
    return ((open < close.shift(1)).astype(float).rolling(1008, min_periods=max(3, 1008//4)).mean()).reindex(close.index)

def fbd_014_gap_magnitude_1260_014(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(open - close.shift(1), close.shift(1)).rolling(1260, min_periods=max(3, 1260//4)).mean()).reindex(close.index)

def fbd_015_open_close_pressure_1512_015(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(close - open, open).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)

def fbd_016_lower_wick_ratio_5_016(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(np.minimum(open, close) - low, high - low).rolling(5, min_periods=max(3, 5//4)).mean()).reindex(close.index)

def fbd_017_upper_wick_ratio_10_017(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(high - np.maximum(open, close), high - low).rolling(10, min_periods=max(3, 10//4)).mean()).reindex(close.index)

def fbd_018_body_to_range_21_018(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div((close - open).abs(), high - low).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)

def fbd_019_gap_down_frequency_42_019(close, open):
    close = _s(close)
    open = _s(open)
    return ((open < close.shift(1)).astype(float).rolling(42, min_periods=max(3, 42//4)).mean()).reindex(close.index)

def fbd_020_gap_magnitude_63_020(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(open - close.shift(1), close.shift(1)).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)

def fbd_021_open_close_pressure_84_021(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(close - open, open).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(close.index)

def fbd_022_lower_wick_ratio_126_022(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(np.minimum(open, close) - low, high - low).rolling(126, min_periods=max(3, 126//4)).mean()).reindex(close.index)

def fbd_023_upper_wick_ratio_189_023(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(high - np.maximum(open, close), high - low).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(close.index)

def fbd_024_body_to_range_252_024(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div((close - open).abs(), high - low).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)

def fbd_025_gap_down_frequency_378_025(close, open):
    close = _s(close)
    open = _s(open)
    return ((open < close.shift(1)).astype(float).rolling(378, min_periods=max(3, 378//4)).mean()).reindex(close.index)

def fbd_026_gap_magnitude_504_026(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(open - close.shift(1), close.shift(1)).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(close.index)

def fbd_027_open_close_pressure_756_027(close, open):
    close = _s(close)
    open = _s(open)
    return (_safe_div(close - open, open).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(close.index)

def fbd_028_lower_wick_ratio_1008_028(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(np.minimum(open, close) - low, high - low).rolling(1008, min_periods=max(3, 1008//4)).mean()).reindex(close.index)

def fbd_029_upper_wick_ratio_1260_029(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div(high - np.maximum(open, close), high - low).rolling(1260, min_periods=max(3, 1260//4)).mean()).reindex(close.index)

def fbd_030_body_to_range_1512_030(close, high, low, open):
    close = _s(close)
    high = _s(high)
    low = _s(low)
    open = _s(open)
    return (_safe_div((close - open).abs(), high - low).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)















































FAILED_BREAKDOWN_REGISTRY_001_075 = {
    'fbd_001_gap_down_frequency_5_001': {'inputs': ['close', 'open'], 'func': fbd_001_gap_down_frequency_5_001},
    'fbd_002_gap_magnitude_10_002': {'inputs': ['close', 'open'], 'func': fbd_002_gap_magnitude_10_002},
    'fbd_003_open_close_pressure_21_003': {'inputs': ['close', 'open'], 'func': fbd_003_open_close_pressure_21_003},
    'fbd_004_lower_wick_ratio_42_004': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_004_lower_wick_ratio_42_004},
    'fbd_005_upper_wick_ratio_63_005': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_005_upper_wick_ratio_63_005},
    'fbd_006_body_to_range_84_006': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_006_body_to_range_84_006},
    'fbd_007_gap_down_frequency_126_007': {'inputs': ['close', 'open'], 'func': fbd_007_gap_down_frequency_126_007},
    'fbd_008_gap_magnitude_189_008': {'inputs': ['close', 'open'], 'func': fbd_008_gap_magnitude_189_008},
    'fbd_009_open_close_pressure_252_009': {'inputs': ['close', 'open'], 'func': fbd_009_open_close_pressure_252_009},
    'fbd_010_lower_wick_ratio_378_010': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_010_lower_wick_ratio_378_010},
    'fbd_011_upper_wick_ratio_504_011': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_011_upper_wick_ratio_504_011},
    'fbd_012_body_to_range_756_012': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_012_body_to_range_756_012},
    'fbd_013_gap_down_frequency_1008_013': {'inputs': ['close', 'open'], 'func': fbd_013_gap_down_frequency_1008_013},
    'fbd_014_gap_magnitude_1260_014': {'inputs': ['close', 'open'], 'func': fbd_014_gap_magnitude_1260_014},
    'fbd_015_open_close_pressure_1512_015': {'inputs': ['close', 'open'], 'func': fbd_015_open_close_pressure_1512_015},
    'fbd_016_lower_wick_ratio_5_016': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_016_lower_wick_ratio_5_016},
    'fbd_017_upper_wick_ratio_10_017': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_017_upper_wick_ratio_10_017},
    'fbd_018_body_to_range_21_018': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_018_body_to_range_21_018},
    'fbd_019_gap_down_frequency_42_019': {'inputs': ['close', 'open'], 'func': fbd_019_gap_down_frequency_42_019},
    'fbd_020_gap_magnitude_63_020': {'inputs': ['close', 'open'], 'func': fbd_020_gap_magnitude_63_020},
    'fbd_021_open_close_pressure_84_021': {'inputs': ['close', 'open'], 'func': fbd_021_open_close_pressure_84_021},
    'fbd_022_lower_wick_ratio_126_022': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_022_lower_wick_ratio_126_022},
    'fbd_023_upper_wick_ratio_189_023': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_023_upper_wick_ratio_189_023},
    'fbd_024_body_to_range_252_024': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_024_body_to_range_252_024},
    'fbd_025_gap_down_frequency_378_025': {'inputs': ['close', 'open'], 'func': fbd_025_gap_down_frequency_378_025},
    'fbd_026_gap_magnitude_504_026': {'inputs': ['close', 'open'], 'func': fbd_026_gap_magnitude_504_026},
    'fbd_027_open_close_pressure_756_027': {'inputs': ['close', 'open'], 'func': fbd_027_open_close_pressure_756_027},
    'fbd_028_lower_wick_ratio_1008_028': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_028_lower_wick_ratio_1008_028},
    'fbd_029_upper_wick_ratio_1260_029': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_029_upper_wick_ratio_1260_029},
    'fbd_030_body_to_range_1512_030': {'inputs': ['close', 'high', 'low', 'open'], 'func': fbd_030_body_to_range_1512_030},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "bar"
_BASEFILL_FAMILY_ID = 50


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


def fbd_basefill_031(**data):
    return _bf_compute(31, **data)


def fbd_basefill_032(**data):
    return _bf_compute(32, **data)


def fbd_basefill_033(**data):
    return _bf_compute(33, **data)


def fbd_basefill_034(**data):
    return _bf_compute(34, **data)


def fbd_basefill_035(**data):
    return _bf_compute(35, **data)


def fbd_basefill_036(**data):
    return _bf_compute(36, **data)


def fbd_basefill_037(**data):
    return _bf_compute(37, **data)


def fbd_basefill_038(**data):
    return _bf_compute(38, **data)


def fbd_basefill_039(**data):
    return _bf_compute(39, **data)


def fbd_basefill_040(**data):
    return _bf_compute(40, **data)


def fbd_basefill_041(**data):
    return _bf_compute(41, **data)


def fbd_basefill_042(**data):
    return _bf_compute(42, **data)


def fbd_basefill_043(**data):
    return _bf_compute(43, **data)


def fbd_basefill_044(**data):
    return _bf_compute(44, **data)


def fbd_basefill_045(**data):
    return _bf_compute(45, **data)


def fbd_basefill_046(**data):
    return _bf_compute(46, **data)


def fbd_basefill_047(**data):
    return _bf_compute(47, **data)


def fbd_basefill_048(**data):
    return _bf_compute(48, **data)


def fbd_basefill_049(**data):
    return _bf_compute(49, **data)


def fbd_basefill_050(**data):
    return _bf_compute(50, **data)


def fbd_basefill_051(**data):
    return _bf_compute(51, **data)


def fbd_basefill_052(**data):
    return _bf_compute(52, **data)


def fbd_basefill_053(**data):
    return _bf_compute(53, **data)


def fbd_basefill_054(**data):
    return _bf_compute(54, **data)


def fbd_basefill_055(**data):
    return _bf_compute(55, **data)


def fbd_basefill_056(**data):
    return _bf_compute(56, **data)


def fbd_basefill_057(**data):
    return _bf_compute(57, **data)


def fbd_basefill_058(**data):
    return _bf_compute(58, **data)


def fbd_basefill_059(**data):
    return _bf_compute(59, **data)


def fbd_basefill_060(**data):
    return _bf_compute(60, **data)


def fbd_basefill_061(**data):
    return _bf_compute(61, **data)


def fbd_basefill_062(**data):
    return _bf_compute(62, **data)


def fbd_basefill_063(**data):
    return _bf_compute(63, **data)


def fbd_basefill_064(**data):
    return _bf_compute(64, **data)


def fbd_basefill_065(**data):
    return _bf_compute(65, **data)


def fbd_basefill_066(**data):
    return _bf_compute(66, **data)


def fbd_basefill_067(**data):
    return _bf_compute(67, **data)


def fbd_basefill_068(**data):
    return _bf_compute(68, **data)


def fbd_basefill_069(**data):
    return _bf_compute(69, **data)


def fbd_basefill_070(**data):
    return _bf_compute(70, **data)


def fbd_basefill_071(**data):
    return _bf_compute(71, **data)


def fbd_basefill_072(**data):
    return _bf_compute(72, **data)


def fbd_basefill_073(**data):
    return _bf_compute(73, **data)


def fbd_basefill_074(**data):
    return _bf_compute(74, **data)


def fbd_basefill_075(**data):
    return _bf_compute(75, **data)

FAILED_BREAKDOWN_REGISTRY_001_075.update({
    'fbd_basefill_031': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_031},
    'fbd_basefill_032': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_032},
    'fbd_basefill_033': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_033},
    'fbd_basefill_034': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_034},
    'fbd_basefill_035': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_035},
    'fbd_basefill_036': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_036},
    'fbd_basefill_037': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_037},
    'fbd_basefill_038': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_038},
    'fbd_basefill_039': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_039},
    'fbd_basefill_040': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_040},
    'fbd_basefill_041': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_041},
    'fbd_basefill_042': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_042},
    'fbd_basefill_043': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_043},
    'fbd_basefill_044': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_044},
    'fbd_basefill_045': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_045},
    'fbd_basefill_046': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_046},
    'fbd_basefill_047': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_047},
    'fbd_basefill_048': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_048},
    'fbd_basefill_049': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_049},
    'fbd_basefill_050': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_050},
    'fbd_basefill_051': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_051},
    'fbd_basefill_052': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_052},
    'fbd_basefill_053': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_053},
    'fbd_basefill_054': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_054},
    'fbd_basefill_055': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_055},
    'fbd_basefill_056': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_056},
    'fbd_basefill_057': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_057},
    'fbd_basefill_058': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_058},
    'fbd_basefill_059': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_059},
    'fbd_basefill_060': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_060},
    'fbd_basefill_061': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_061},
    'fbd_basefill_062': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_062},
    'fbd_basefill_063': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_063},
    'fbd_basefill_064': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_064},
    'fbd_basefill_065': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_065},
    'fbd_basefill_066': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_066},
    'fbd_basefill_067': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_067},
    'fbd_basefill_068': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_068},
    'fbd_basefill_069': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_069},
    'fbd_basefill_070': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_070},
    'fbd_basefill_071': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_071},
    'fbd_basefill_072': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_072},
    'fbd_basefill_073': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_073},
    'fbd_basefill_074': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_074},
    'fbd_basefill_075': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': fbd_basefill_075},
})
