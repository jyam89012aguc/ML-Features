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

def mip_002_zero_volume_frequency_10_002(volume):
    volume = _s(volume)
    return ((volume <= 0).astype(float).rolling(10, min_periods=max(3, 10//4)).mean()).reindex(volume.index)

def mip_003_spread_proxy_21_003(high, low):
    high = _s(high)
    low = _s(low)
    return (_safe_div(high - low, (high + low) / 2).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(high.index)

def mip_004_trading_intensity_42_004(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(42, min_periods=max(3, 42//4)).mean())).reindex(volume.index)

def mip_006_price_level_distress_84_006(close):
    close = _s(close)
    return (_safe_div(1, close).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(close.index)

def mip_008_zero_volume_frequency_189_008(volume):
    volume = _s(volume)
    return ((volume <= 0).astype(float).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(volume.index)

def mip_009_spread_proxy_252_009(high, low):
    high = _s(high)
    low = _s(low)
    return (_safe_div(high - low, (high + low) / 2).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(high.index)

def mip_010_trading_intensity_378_010(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(378, min_periods=max(3, 378//4)).mean())).reindex(volume.index)

def mip_012_price_level_distress_756_012(close):
    close = _s(close)
    return (_safe_div(1, close).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(close.index)

def mip_014_zero_volume_frequency_1260_014(volume):
    volume = _s(volume)
    return ((volume <= 0).astype(float).rolling(1260, min_periods=max(3, 1260//4)).mean()).reindex(volume.index)

def mip_015_spread_proxy_1512_015(high, low):
    high = _s(high)
    low = _s(low)
    return (_safe_div(high - low, (high + low) / 2).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(high.index)

def mip_016_trading_intensity_5_016(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(5, min_periods=max(3, 5//4)).mean())).reindex(volume.index)

def mip_018_price_level_distress_21_018(close):
    close = _s(close)
    return (_safe_div(1, close).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)

def mip_020_zero_volume_frequency_63_020(volume):
    volume = _s(volume)
    return ((volume <= 0).astype(float).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(volume.index)

def mip_021_spread_proxy_84_021(high, low):
    high = _s(high)
    low = _s(low)
    return (_safe_div(high - low, (high + low) / 2).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(high.index)

def mip_022_trading_intensity_126_022(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(126, min_periods=max(3, 126//4)).mean())).reindex(volume.index)

def mip_024_price_level_distress_252_024(close):
    close = _s(close)
    return (_safe_div(1, close).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)

def mip_026_zero_volume_frequency_504_026(volume):
    volume = _s(volume)
    return ((volume <= 0).astype(float).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(volume.index)

def mip_027_spread_proxy_756_027(high, low):
    high = _s(high)
    low = _s(low)
    return (_safe_div(high - low, (high + low) / 2).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(high.index)

def mip_028_trading_intensity_1008_028(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).mean())).reindex(volume.index)

def mip_030_price_level_distress_1512_030(close):
    close = _s(close)
    return (_safe_div(1, close).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)
































MARKET_IMPACT_PROXY_REGISTRY_001_075 = {
    'mip_002_zero_volume_frequency_10_002': {'inputs': ['volume'], 'func': mip_002_zero_volume_frequency_10_002},
    'mip_003_spread_proxy_21_003': {'inputs': ['high', 'low'], 'func': mip_003_spread_proxy_21_003},
    'mip_004_trading_intensity_42_004': {'inputs': ['volume'], 'func': mip_004_trading_intensity_42_004},
    'mip_006_price_level_distress_84_006': {'inputs': ['close'], 'func': mip_006_price_level_distress_84_006},
    'mip_008_zero_volume_frequency_189_008': {'inputs': ['volume'], 'func': mip_008_zero_volume_frequency_189_008},
    'mip_009_spread_proxy_252_009': {'inputs': ['high', 'low'], 'func': mip_009_spread_proxy_252_009},
    'mip_010_trading_intensity_378_010': {'inputs': ['volume'], 'func': mip_010_trading_intensity_378_010},
    'mip_012_price_level_distress_756_012': {'inputs': ['close'], 'func': mip_012_price_level_distress_756_012},
    'mip_014_zero_volume_frequency_1260_014': {'inputs': ['volume'], 'func': mip_014_zero_volume_frequency_1260_014},
    'mip_015_spread_proxy_1512_015': {'inputs': ['high', 'low'], 'func': mip_015_spread_proxy_1512_015},
    'mip_016_trading_intensity_5_016': {'inputs': ['volume'], 'func': mip_016_trading_intensity_5_016},
    'mip_018_price_level_distress_21_018': {'inputs': ['close'], 'func': mip_018_price_level_distress_21_018},
    'mip_020_zero_volume_frequency_63_020': {'inputs': ['volume'], 'func': mip_020_zero_volume_frequency_63_020},
    'mip_021_spread_proxy_84_021': {'inputs': ['high', 'low'], 'func': mip_021_spread_proxy_84_021},
    'mip_022_trading_intensity_126_022': {'inputs': ['volume'], 'func': mip_022_trading_intensity_126_022},
    'mip_024_price_level_distress_252_024': {'inputs': ['close'], 'func': mip_024_price_level_distress_252_024},
    'mip_026_zero_volume_frequency_504_026': {'inputs': ['volume'], 'func': mip_026_zero_volume_frequency_504_026},
    'mip_027_spread_proxy_756_027': {'inputs': ['high', 'low'], 'func': mip_027_spread_proxy_756_027},
    'mip_028_trading_intensity_1008_028': {'inputs': ['volume'], 'func': mip_028_trading_intensity_1008_028},
    'mip_030_price_level_distress_1512_030': {'inputs': ['close'], 'func': mip_030_price_level_distress_1512_030},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "liquidity"
_BASEFILL_FAMILY_ID = 59


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


def mip_basefill_001(**data):
    return _bf_compute(1, **data)


def mip_basefill_005(**data):
    return _bf_compute(5, **data)


def mip_basefill_007(**data):
    return _bf_compute(7, **data)


def mip_basefill_011(**data):
    return _bf_compute(11, **data)


def mip_basefill_013(**data):
    return _bf_compute(13, **data)


def mip_basefill_017(**data):
    return _bf_compute(17, **data)


def mip_basefill_019(**data):
    return _bf_compute(19, **data)


def mip_basefill_023(**data):
    return _bf_compute(23, **data)


def mip_basefill_025(**data):
    return _bf_compute(25, **data)


def mip_basefill_029(**data):
    return _bf_compute(29, **data)


def mip_basefill_031(**data):
    return _bf_compute(31, **data)


def mip_basefill_032(**data):
    return _bf_compute(32, **data)


def mip_basefill_033(**data):
    return _bf_compute(33, **data)


def mip_basefill_034(**data):
    return _bf_compute(34, **data)


def mip_basefill_035(**data):
    return _bf_compute(35, **data)


def mip_basefill_036(**data):
    return _bf_compute(36, **data)


def mip_basefill_037(**data):
    return _bf_compute(37, **data)


def mip_basefill_038(**data):
    return _bf_compute(38, **data)


def mip_basefill_039(**data):
    return _bf_compute(39, **data)


def mip_basefill_040(**data):
    return _bf_compute(40, **data)


def mip_basefill_041(**data):
    return _bf_compute(41, **data)


def mip_basefill_042(**data):
    return _bf_compute(42, **data)


def mip_basefill_043(**data):
    return _bf_compute(43, **data)


def mip_basefill_044(**data):
    return _bf_compute(44, **data)


def mip_basefill_045(**data):
    return _bf_compute(45, **data)


def mip_basefill_046(**data):
    return _bf_compute(46, **data)


def mip_basefill_047(**data):
    return _bf_compute(47, **data)


def mip_basefill_048(**data):
    return _bf_compute(48, **data)


def mip_basefill_049(**data):
    return _bf_compute(49, **data)


def mip_basefill_050(**data):
    return _bf_compute(50, **data)


def mip_basefill_051(**data):
    return _bf_compute(51, **data)


def mip_basefill_052(**data):
    return _bf_compute(52, **data)


def mip_basefill_053(**data):
    return _bf_compute(53, **data)


def mip_basefill_054(**data):
    return _bf_compute(54, **data)


def mip_basefill_055(**data):
    return _bf_compute(55, **data)


def mip_basefill_056(**data):
    return _bf_compute(56, **data)


def mip_basefill_057(**data):
    return _bf_compute(57, **data)


def mip_basefill_058(**data):
    return _bf_compute(58, **data)


def mip_basefill_059(**data):
    return _bf_compute(59, **data)


def mip_basefill_060(**data):
    return _bf_compute(60, **data)


def mip_basefill_061(**data):
    return _bf_compute(61, **data)


def mip_basefill_062(**data):
    return _bf_compute(62, **data)


def mip_basefill_063(**data):
    return _bf_compute(63, **data)


def mip_basefill_064(**data):
    return _bf_compute(64, **data)


def mip_basefill_065(**data):
    return _bf_compute(65, **data)


def mip_basefill_066(**data):
    return _bf_compute(66, **data)


def mip_basefill_067(**data):
    return _bf_compute(67, **data)


def mip_basefill_068(**data):
    return _bf_compute(68, **data)


def mip_basefill_069(**data):
    return _bf_compute(69, **data)


def mip_basefill_070(**data):
    return _bf_compute(70, **data)


def mip_basefill_071(**data):
    return _bf_compute(71, **data)


def mip_basefill_072(**data):
    return _bf_compute(72, **data)


def mip_basefill_073(**data):
    return _bf_compute(73, **data)


def mip_basefill_074(**data):
    return _bf_compute(74, **data)


def mip_basefill_075(**data):
    return _bf_compute(75, **data)

MARKET_IMPACT_PROXY_REGISTRY_001_075.update({
    'mip_basefill_001': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_001},
    'mip_basefill_005': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_005},
    'mip_basefill_007': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_007},
    'mip_basefill_011': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_011},
    'mip_basefill_013': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_013},
    'mip_basefill_017': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_017},
    'mip_basefill_019': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_019},
    'mip_basefill_023': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_023},
    'mip_basefill_025': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_025},
    'mip_basefill_029': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_029},
    'mip_basefill_031': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_031},
    'mip_basefill_032': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_032},
    'mip_basefill_033': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_033},
    'mip_basefill_034': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_034},
    'mip_basefill_035': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_035},
    'mip_basefill_036': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_036},
    'mip_basefill_037': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_037},
    'mip_basefill_038': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_038},
    'mip_basefill_039': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_039},
    'mip_basefill_040': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_040},
    'mip_basefill_041': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_041},
    'mip_basefill_042': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_042},
    'mip_basefill_043': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_043},
    'mip_basefill_044': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_044},
    'mip_basefill_045': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_045},
    'mip_basefill_046': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_046},
    'mip_basefill_047': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_047},
    'mip_basefill_048': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_048},
    'mip_basefill_049': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_049},
    'mip_basefill_050': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_050},
    'mip_basefill_051': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_051},
    'mip_basefill_052': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_052},
    'mip_basefill_053': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_053},
    'mip_basefill_054': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_054},
    'mip_basefill_055': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_055},
    'mip_basefill_056': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_056},
    'mip_basefill_057': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_057},
    'mip_basefill_058': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_058},
    'mip_basefill_059': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_059},
    'mip_basefill_060': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_060},
    'mip_basefill_061': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_061},
    'mip_basefill_062': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_062},
    'mip_basefill_063': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_063},
    'mip_basefill_064': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_064},
    'mip_basefill_065': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_065},
    'mip_basefill_066': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_066},
    'mip_basefill_067': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_067},
    'mip_basefill_068': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_068},
    'mip_basefill_069': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_069},
    'mip_basefill_070': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_070},
    'mip_basefill_071': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_071},
    'mip_basefill_072': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_072},
    'mip_basefill_073': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_073},
    'mip_basefill_074': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_074},
    'mip_basefill_075': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_basefill_075},
})


# Basefill overrides for pre-existing duplicate or constant base features.


def mip_002_zero_volume_frequency_10_002(**data):
    return _bf_compute(2076, **data)


def mip_008_zero_volume_frequency_189_008(**data):
    return _bf_compute(2093, **data)


def mip_014_zero_volume_frequency_1260_014(**data):
    return _bf_compute(2110, **data)


def mip_020_zero_volume_frequency_63_020(**data):
    return _bf_compute(2127, **data)


def mip_026_zero_volume_frequency_504_026(**data):
    return _bf_compute(2144, **data)

MARKET_IMPACT_PROXY_REGISTRY_001_075.update({
    'mip_002_zero_volume_frequency_10_002': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_002_zero_volume_frequency_10_002},
    'mip_008_zero_volume_frequency_189_008': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_008_zero_volume_frequency_189_008},
    'mip_014_zero_volume_frequency_1260_014': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_014_zero_volume_frequency_1260_014},
    'mip_020_zero_volume_frequency_63_020': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_020_zero_volume_frequency_63_020},
    'mip_026_zero_volume_frequency_504_026': {'inputs': ['close', 'high', 'low', 'volume', 'shareswa'], 'func': mip_026_zero_volume_frequency_504_026},
})
