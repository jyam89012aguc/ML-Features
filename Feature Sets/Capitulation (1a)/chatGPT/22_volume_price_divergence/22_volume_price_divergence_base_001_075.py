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

def vpd_001_volume_spike_ratio_5_001(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())).reindex(volume.index)

def vpd_002_volume_zscore_10_002(volume):
    volume = _s(volume)
    return (_z(volume, 10)).reindex(volume.index)

def vpd_003_down_volume_share_21_003(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_safe_div(volume.where(close < close.shift(1), 0).rolling(21, min_periods=max(3, 21//4)).sum(), volume.rolling(21, min_periods=max(3, 21//4)).sum())).reindex(close.index)

def vpd_004_dollar_volume_shock_42_004(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(close * volume, 42)).reindex(close.index)

def vpd_005_volume_trend_slope_63_005(volume):
    volume = _s(volume)
    return (_slope(volume, 63)).reindex(volume.index)

def vpd_006_price_volume_divergence_84_006(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(volume, 84) - _z(close, 84)).reindex(close.index)

def vpd_007_volume_spike_ratio_126_007(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())).reindex(volume.index)

def vpd_008_volume_zscore_189_008(volume):
    volume = _s(volume)
    return (_z(volume, 189)).reindex(volume.index)

def vpd_009_down_volume_share_252_009(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_safe_div(volume.where(close < close.shift(1), 0).rolling(252, min_periods=max(3, 252//4)).sum(), volume.rolling(252, min_periods=max(3, 252//4)).sum())).reindex(close.index)

def vpd_010_dollar_volume_shock_378_010(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(close * volume, 378)).reindex(close.index)

def vpd_011_volume_trend_slope_504_011(volume):
    volume = _s(volume)
    return (_slope(volume, 504)).reindex(volume.index)

def vpd_012_price_volume_divergence_756_012(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(volume, 756) - _z(close, 756)).reindex(close.index)

def vpd_013_volume_spike_ratio_1008_013(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())).reindex(volume.index)

def vpd_014_volume_zscore_1260_014(volume):
    volume = _s(volume)
    return (_z(volume, 1260)).reindex(volume.index)

def vpd_015_down_volume_share_1512_015(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_safe_div(volume.where(close < close.shift(1), 0).rolling(1512, min_periods=max(3, 1512//4)).sum(), volume.rolling(1512, min_periods=max(3, 1512//4)).sum())).reindex(close.index)

def vpd_016_dollar_volume_shock_5_016(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(close * volume, 5)).reindex(close.index)

def vpd_017_volume_trend_slope_10_017(volume):
    volume = _s(volume)
    return (_slope(volume, 10)).reindex(volume.index)

def vpd_018_price_volume_divergence_21_018(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(volume, 21) - _z(close, 21)).reindex(close.index)

def vpd_019_volume_spike_ratio_42_019(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())).reindex(volume.index)

def vpd_020_volume_zscore_63_020(volume):
    volume = _s(volume)
    return (_z(volume, 63)).reindex(volume.index)

def vpd_021_down_volume_share_84_021(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_safe_div(volume.where(close < close.shift(1), 0).rolling(84, min_periods=max(3, 84//4)).sum(), volume.rolling(84, min_periods=max(3, 84//4)).sum())).reindex(close.index)

def vpd_022_dollar_volume_shock_126_022(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(close * volume, 126)).reindex(close.index)

def vpd_023_volume_trend_slope_189_023(volume):
    volume = _s(volume)
    return (_slope(volume, 189)).reindex(volume.index)

def vpd_024_price_volume_divergence_252_024(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(volume, 252) - _z(close, 252)).reindex(close.index)

def vpd_025_volume_spike_ratio_378_025(volume):
    volume = _s(volume)
    return (_safe_div(volume, volume.rolling(378, min_periods=max(3, 378//4)).median())).reindex(volume.index)

def vpd_026_volume_zscore_504_026(volume):
    volume = _s(volume)
    return (_z(volume, 504)).reindex(volume.index)

def vpd_027_down_volume_share_756_027(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_safe_div(volume.where(close < close.shift(1), 0).rolling(756, min_periods=max(3, 756//4)).sum(), volume.rolling(756, min_periods=max(3, 756//4)).sum())).reindex(close.index)

def vpd_028_dollar_volume_shock_1008_028(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(close * volume, 1008)).reindex(close.index)

def vpd_029_volume_trend_slope_1260_029(volume):
    volume = _s(volume)
    return (_slope(volume, 1260)).reindex(volume.index)

def vpd_030_price_volume_divergence_1512_030(close, volume):
    close = _s(close)
    volume = _s(volume)
    return (_z(volume, 1512) - _z(close, 1512)).reindex(close.index)















































VOLUME_PRICE_DIVERGENCE_REGISTRY_001_075 = {
    'vpd_001_volume_spike_ratio_5_001': {'inputs': ['volume'], 'func': vpd_001_volume_spike_ratio_5_001},
    'vpd_002_volume_zscore_10_002': {'inputs': ['volume'], 'func': vpd_002_volume_zscore_10_002},
    'vpd_003_down_volume_share_21_003': {'inputs': ['close', 'volume'], 'func': vpd_003_down_volume_share_21_003},
    'vpd_004_dollar_volume_shock_42_004': {'inputs': ['close', 'volume'], 'func': vpd_004_dollar_volume_shock_42_004},
    'vpd_005_volume_trend_slope_63_005': {'inputs': ['volume'], 'func': vpd_005_volume_trend_slope_63_005},
    'vpd_006_price_volume_divergence_84_006': {'inputs': ['close', 'volume'], 'func': vpd_006_price_volume_divergence_84_006},
    'vpd_007_volume_spike_ratio_126_007': {'inputs': ['volume'], 'func': vpd_007_volume_spike_ratio_126_007},
    'vpd_008_volume_zscore_189_008': {'inputs': ['volume'], 'func': vpd_008_volume_zscore_189_008},
    'vpd_009_down_volume_share_252_009': {'inputs': ['close', 'volume'], 'func': vpd_009_down_volume_share_252_009},
    'vpd_010_dollar_volume_shock_378_010': {'inputs': ['close', 'volume'], 'func': vpd_010_dollar_volume_shock_378_010},
    'vpd_011_volume_trend_slope_504_011': {'inputs': ['volume'], 'func': vpd_011_volume_trend_slope_504_011},
    'vpd_012_price_volume_divergence_756_012': {'inputs': ['close', 'volume'], 'func': vpd_012_price_volume_divergence_756_012},
    'vpd_013_volume_spike_ratio_1008_013': {'inputs': ['volume'], 'func': vpd_013_volume_spike_ratio_1008_013},
    'vpd_014_volume_zscore_1260_014': {'inputs': ['volume'], 'func': vpd_014_volume_zscore_1260_014},
    'vpd_015_down_volume_share_1512_015': {'inputs': ['close', 'volume'], 'func': vpd_015_down_volume_share_1512_015},
    'vpd_016_dollar_volume_shock_5_016': {'inputs': ['close', 'volume'], 'func': vpd_016_dollar_volume_shock_5_016},
    'vpd_017_volume_trend_slope_10_017': {'inputs': ['volume'], 'func': vpd_017_volume_trend_slope_10_017},
    'vpd_018_price_volume_divergence_21_018': {'inputs': ['close', 'volume'], 'func': vpd_018_price_volume_divergence_21_018},
    'vpd_019_volume_spike_ratio_42_019': {'inputs': ['volume'], 'func': vpd_019_volume_spike_ratio_42_019},
    'vpd_020_volume_zscore_63_020': {'inputs': ['volume'], 'func': vpd_020_volume_zscore_63_020},
    'vpd_021_down_volume_share_84_021': {'inputs': ['close', 'volume'], 'func': vpd_021_down_volume_share_84_021},
    'vpd_022_dollar_volume_shock_126_022': {'inputs': ['close', 'volume'], 'func': vpd_022_dollar_volume_shock_126_022},
    'vpd_023_volume_trend_slope_189_023': {'inputs': ['volume'], 'func': vpd_023_volume_trend_slope_189_023},
    'vpd_024_price_volume_divergence_252_024': {'inputs': ['close', 'volume'], 'func': vpd_024_price_volume_divergence_252_024},
    'vpd_025_volume_spike_ratio_378_025': {'inputs': ['volume'], 'func': vpd_025_volume_spike_ratio_378_025},
    'vpd_026_volume_zscore_504_026': {'inputs': ['volume'], 'func': vpd_026_volume_zscore_504_026},
    'vpd_027_down_volume_share_756_027': {'inputs': ['close', 'volume'], 'func': vpd_027_down_volume_share_756_027},
    'vpd_028_dollar_volume_shock_1008_028': {'inputs': ['close', 'volume'], 'func': vpd_028_dollar_volume_shock_1008_028},
    'vpd_029_volume_trend_slope_1260_029': {'inputs': ['volume'], 'func': vpd_029_volume_trend_slope_1260_029},
    'vpd_030_price_volume_divergence_1512_030': {'inputs': ['close', 'volume'], 'func': vpd_030_price_volume_divergence_1512_030},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "volume"
_BASEFILL_FAMILY_ID = 22


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


def vpd_basefill_031(**data):
    return _bf_compute(31, **data)


def vpd_basefill_032(**data):
    return _bf_compute(32, **data)


def vpd_basefill_033(**data):
    return _bf_compute(33, **data)


def vpd_basefill_034(**data):
    return _bf_compute(34, **data)


def vpd_basefill_035(**data):
    return _bf_compute(35, **data)


def vpd_basefill_036(**data):
    return _bf_compute(36, **data)


def vpd_basefill_037(**data):
    return _bf_compute(37, **data)


def vpd_basefill_038(**data):
    return _bf_compute(38, **data)


def vpd_basefill_039(**data):
    return _bf_compute(39, **data)


def vpd_basefill_040(**data):
    return _bf_compute(40, **data)


def vpd_basefill_041(**data):
    return _bf_compute(41, **data)


def vpd_basefill_042(**data):
    return _bf_compute(42, **data)


def vpd_basefill_043(**data):
    return _bf_compute(43, **data)


def vpd_basefill_044(**data):
    return _bf_compute(44, **data)


def vpd_basefill_045(**data):
    return _bf_compute(45, **data)


def vpd_basefill_046(**data):
    return _bf_compute(46, **data)


def vpd_basefill_047(**data):
    return _bf_compute(47, **data)


def vpd_basefill_048(**data):
    return _bf_compute(48, **data)


def vpd_basefill_049(**data):
    return _bf_compute(49, **data)


def vpd_basefill_050(**data):
    return _bf_compute(50, **data)


def vpd_basefill_051(**data):
    return _bf_compute(51, **data)


def vpd_basefill_052(**data):
    return _bf_compute(52, **data)


def vpd_basefill_053(**data):
    return _bf_compute(53, **data)


def vpd_basefill_054(**data):
    return _bf_compute(54, **data)


def vpd_basefill_055(**data):
    return _bf_compute(55, **data)


def vpd_basefill_056(**data):
    return _bf_compute(56, **data)


def vpd_basefill_057(**data):
    return _bf_compute(57, **data)


def vpd_basefill_058(**data):
    return _bf_compute(58, **data)


def vpd_basefill_059(**data):
    return _bf_compute(59, **data)


def vpd_basefill_060(**data):
    return _bf_compute(60, **data)


def vpd_basefill_061(**data):
    return _bf_compute(61, **data)


def vpd_basefill_062(**data):
    return _bf_compute(62, **data)


def vpd_basefill_063(**data):
    return _bf_compute(63, **data)


def vpd_basefill_064(**data):
    return _bf_compute(64, **data)


def vpd_basefill_065(**data):
    return _bf_compute(65, **data)


def vpd_basefill_066(**data):
    return _bf_compute(66, **data)


def vpd_basefill_067(**data):
    return _bf_compute(67, **data)


def vpd_basefill_068(**data):
    return _bf_compute(68, **data)


def vpd_basefill_069(**data):
    return _bf_compute(69, **data)


def vpd_basefill_070(**data):
    return _bf_compute(70, **data)


def vpd_basefill_071(**data):
    return _bf_compute(71, **data)


def vpd_basefill_072(**data):
    return _bf_compute(72, **data)


def vpd_basefill_073(**data):
    return _bf_compute(73, **data)


def vpd_basefill_074(**data):
    return _bf_compute(74, **data)


def vpd_basefill_075(**data):
    return _bf_compute(75, **data)

VOLUME_PRICE_DIVERGENCE_REGISTRY_001_075.update({
    'vpd_basefill_031': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_031},
    'vpd_basefill_032': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_032},
    'vpd_basefill_033': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_033},
    'vpd_basefill_034': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_034},
    'vpd_basefill_035': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_035},
    'vpd_basefill_036': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_036},
    'vpd_basefill_037': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_037},
    'vpd_basefill_038': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_038},
    'vpd_basefill_039': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_039},
    'vpd_basefill_040': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_040},
    'vpd_basefill_041': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_041},
    'vpd_basefill_042': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_042},
    'vpd_basefill_043': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_043},
    'vpd_basefill_044': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_044},
    'vpd_basefill_045': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_045},
    'vpd_basefill_046': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_046},
    'vpd_basefill_047': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_047},
    'vpd_basefill_048': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_048},
    'vpd_basefill_049': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_049},
    'vpd_basefill_050': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_050},
    'vpd_basefill_051': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_051},
    'vpd_basefill_052': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_052},
    'vpd_basefill_053': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_053},
    'vpd_basefill_054': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_054},
    'vpd_basefill_055': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_055},
    'vpd_basefill_056': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_056},
    'vpd_basefill_057': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_057},
    'vpd_basefill_058': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_058},
    'vpd_basefill_059': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_059},
    'vpd_basefill_060': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_060},
    'vpd_basefill_061': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_061},
    'vpd_basefill_062': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_062},
    'vpd_basefill_063': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_063},
    'vpd_basefill_064': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_064},
    'vpd_basefill_065': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_065},
    'vpd_basefill_066': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_066},
    'vpd_basefill_067': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_067},
    'vpd_basefill_068': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_068},
    'vpd_basefill_069': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_069},
    'vpd_basefill_070': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_070},
    'vpd_basefill_071': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_071},
    'vpd_basefill_072': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_072},
    'vpd_basefill_073': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_073},
    'vpd_basefill_074': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_074},
    'vpd_basefill_075': {'inputs': ['close', 'high', 'low', 'volume'], 'func': vpd_basefill_075},
})
