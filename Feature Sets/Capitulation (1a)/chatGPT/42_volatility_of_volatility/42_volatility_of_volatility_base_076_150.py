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








































VOLATILITY_OF_VOLATILITY_REGISTRY_076_150 = {
}


# Replacement features restored after redundancy audit.

import numpy as np
import pandas as pd


FAMILY_ID = 42
CATEGORY = "volatility"
PREFIX = "vov"
REPLACEMENT_COUNT = 175
MISSING_DEPENDENCY_NAMES = []


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

VOV_REPLACEMENT_BASE_REGISTRY = {}


def vov_replacement_001(**data):
    return _compute_replacement(1, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_001'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_001}


def vov_replacement_002(**data):
    return _compute_replacement(2, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_002'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_002}


def vov_replacement_003(**data):
    return _compute_replacement(3, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_003'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_003}


def vov_replacement_004(**data):
    return _compute_replacement(4, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_004'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_004}


def vov_replacement_005(**data):
    return _compute_replacement(5, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_005'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_005}


def vov_replacement_006(**data):
    return _compute_replacement(6, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_006'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_006}


def vov_replacement_007(**data):
    return _compute_replacement(7, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_007'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_007}


def vov_replacement_008(**data):
    return _compute_replacement(8, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_008'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_008}


def vov_replacement_009(**data):
    return _compute_replacement(9, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_009'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_009}


def vov_replacement_010(**data):
    return _compute_replacement(10, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_010'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_010}


def vov_replacement_011(**data):
    return _compute_replacement(11, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_011'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_011}


def vov_replacement_012(**data):
    return _compute_replacement(12, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_012'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_012}


def vov_replacement_013(**data):
    return _compute_replacement(13, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_013'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_013}


def vov_replacement_014(**data):
    return _compute_replacement(14, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_014'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_014}


def vov_replacement_015(**data):
    return _compute_replacement(15, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_015'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_015}


def vov_replacement_016(**data):
    return _compute_replacement(16, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_016'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_016}


def vov_replacement_017(**data):
    return _compute_replacement(17, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_017'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_017}


def vov_replacement_018(**data):
    return _compute_replacement(18, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_018'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_018}


def vov_replacement_019(**data):
    return _compute_replacement(19, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_019'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_019}


def vov_replacement_020(**data):
    return _compute_replacement(20, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_020'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_020}


def vov_replacement_021(**data):
    return _compute_replacement(21, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_021'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_021}


def vov_replacement_022(**data):
    return _compute_replacement(22, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_022'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_022}


def vov_replacement_023(**data):
    return _compute_replacement(23, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_023'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_023}


def vov_replacement_024(**data):
    return _compute_replacement(24, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_024'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_024}


def vov_replacement_025(**data):
    return _compute_replacement(25, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_025'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_025}


def vov_replacement_026(**data):
    return _compute_replacement(26, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_026'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_026}


def vov_replacement_027(**data):
    return _compute_replacement(27, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_027'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_027}


def vov_replacement_028(**data):
    return _compute_replacement(28, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_028'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_028}


def vov_replacement_029(**data):
    return _compute_replacement(29, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_029'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_029}


def vov_replacement_030(**data):
    return _compute_replacement(30, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_030'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_030}


def vov_replacement_031(**data):
    return _compute_replacement(31, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_031'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_031}


def vov_replacement_032(**data):
    return _compute_replacement(32, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_032'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_032}


def vov_replacement_033(**data):
    return _compute_replacement(33, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_033'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_033}


def vov_replacement_034(**data):
    return _compute_replacement(34, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_034'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_034}


def vov_replacement_035(**data):
    return _compute_replacement(35, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_035'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_035}


def vov_replacement_036(**data):
    return _compute_replacement(36, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_036'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_036}


def vov_replacement_037(**data):
    return _compute_replacement(37, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_037'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_037}


def vov_replacement_038(**data):
    return _compute_replacement(38, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_038'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_038}


def vov_replacement_039(**data):
    return _compute_replacement(39, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_039'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_039}


def vov_replacement_040(**data):
    return _compute_replacement(40, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_040'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_040}


def vov_replacement_041(**data):
    return _compute_replacement(41, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_041'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_041}


def vov_replacement_042(**data):
    return _compute_replacement(42, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_042'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_042}


def vov_replacement_043(**data):
    return _compute_replacement(43, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_043'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_043}


def vov_replacement_044(**data):
    return _compute_replacement(44, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_044'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_044}


def vov_replacement_045(**data):
    return _compute_replacement(45, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_045'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_045}


def vov_replacement_046(**data):
    return _compute_replacement(46, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_046'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_046}


def vov_replacement_047(**data):
    return _compute_replacement(47, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_047'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_047}


def vov_replacement_048(**data):
    return _compute_replacement(48, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_048'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_048}


def vov_replacement_049(**data):
    return _compute_replacement(49, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_049'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_049}


def vov_replacement_050(**data):
    return _compute_replacement(50, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_050'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_050}


def vov_replacement_051(**data):
    return _compute_replacement(51, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_051'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_051}


def vov_replacement_052(**data):
    return _compute_replacement(52, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_052'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_052}


def vov_replacement_053(**data):
    return _compute_replacement(53, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_053'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_053}


def vov_replacement_054(**data):
    return _compute_replacement(54, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_054'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_054}


def vov_replacement_055(**data):
    return _compute_replacement(55, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_055'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_055}


def vov_replacement_056(**data):
    return _compute_replacement(56, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_056'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_056}


def vov_replacement_057(**data):
    return _compute_replacement(57, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_057'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_057}


def vov_replacement_058(**data):
    return _compute_replacement(58, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_058'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_058}


def vov_replacement_059(**data):
    return _compute_replacement(59, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_059'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_059}


def vov_replacement_060(**data):
    return _compute_replacement(60, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_060'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_060}


def vov_replacement_061(**data):
    return _compute_replacement(61, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_061'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_061}


def vov_replacement_062(**data):
    return _compute_replacement(62, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_062'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_062}


def vov_replacement_063(**data):
    return _compute_replacement(63, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_063'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_063}


def vov_replacement_064(**data):
    return _compute_replacement(64, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_064'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_064}


def vov_replacement_065(**data):
    return _compute_replacement(65, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_065'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_065}


def vov_replacement_066(**data):
    return _compute_replacement(66, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_066'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_066}


def vov_replacement_067(**data):
    return _compute_replacement(67, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_067'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_067}


def vov_replacement_068(**data):
    return _compute_replacement(68, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_068'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_068}


def vov_replacement_069(**data):
    return _compute_replacement(69, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_069'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_069}


def vov_replacement_070(**data):
    return _compute_replacement(70, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_070'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_070}


def vov_replacement_071(**data):
    return _compute_replacement(71, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_071'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_071}


def vov_replacement_072(**data):
    return _compute_replacement(72, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_072'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_072}


def vov_replacement_073(**data):
    return _compute_replacement(73, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_073'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_073}


def vov_replacement_074(**data):
    return _compute_replacement(74, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_074'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_074}


def vov_replacement_075(**data):
    return _compute_replacement(75, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_075'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_075}


def vov_replacement_076(**data):
    return _compute_replacement(76, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_076'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_076}


def vov_replacement_077(**data):
    return _compute_replacement(77, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_077'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_077}


def vov_replacement_078(**data):
    return _compute_replacement(78, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_078'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_078}


def vov_replacement_079(**data):
    return _compute_replacement(79, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_079'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_079}


def vov_replacement_080(**data):
    return _compute_replacement(80, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_080'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_080}


def vov_replacement_081(**data):
    return _compute_replacement(81, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_081'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_081}


def vov_replacement_082(**data):
    return _compute_replacement(82, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_082'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_082}


def vov_replacement_083(**data):
    return _compute_replacement(83, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_083'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_083}


def vov_replacement_084(**data):
    return _compute_replacement(84, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_084'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_084}


def vov_replacement_085(**data):
    return _compute_replacement(85, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_085'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_085}


def vov_replacement_086(**data):
    return _compute_replacement(86, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_086'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_086}


def vov_replacement_087(**data):
    return _compute_replacement(87, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_087'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_087}


def vov_replacement_088(**data):
    return _compute_replacement(88, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_088'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_088}


def vov_replacement_089(**data):
    return _compute_replacement(89, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_089'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_089}


def vov_replacement_090(**data):
    return _compute_replacement(90, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_090'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_090}


def vov_replacement_091(**data):
    return _compute_replacement(91, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_091'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_091}


def vov_replacement_092(**data):
    return _compute_replacement(92, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_092'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_092}


def vov_replacement_093(**data):
    return _compute_replacement(93, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_093'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_093}


def vov_replacement_094(**data):
    return _compute_replacement(94, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_094'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_094}


def vov_replacement_095(**data):
    return _compute_replacement(95, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_095'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_095}


def vov_replacement_096(**data):
    return _compute_replacement(96, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_096'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_096}


def vov_replacement_097(**data):
    return _compute_replacement(97, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_097'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_097}


def vov_replacement_098(**data):
    return _compute_replacement(98, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_098'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_098}


def vov_replacement_099(**data):
    return _compute_replacement(99, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_099'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_099}


def vov_replacement_100(**data):
    return _compute_replacement(100, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_100'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_100}


def vov_replacement_101(**data):
    return _compute_replacement(101, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_101'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_101}


def vov_replacement_102(**data):
    return _compute_replacement(102, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_102'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_102}


def vov_replacement_103(**data):
    return _compute_replacement(103, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_103'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_103}


def vov_replacement_104(**data):
    return _compute_replacement(104, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_104'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_104}


def vov_replacement_105(**data):
    return _compute_replacement(105, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_105'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_105}


def vov_replacement_106(**data):
    return _compute_replacement(106, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_106'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_106}


def vov_replacement_107(**data):
    return _compute_replacement(107, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_107'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_107}


def vov_replacement_108(**data):
    return _compute_replacement(108, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_108'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_108}


def vov_replacement_109(**data):
    return _compute_replacement(109, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_109'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_109}


def vov_replacement_110(**data):
    return _compute_replacement(110, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_110'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_110}


def vov_replacement_111(**data):
    return _compute_replacement(111, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_111'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_111}


def vov_replacement_112(**data):
    return _compute_replacement(112, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_112'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_112}


def vov_replacement_113(**data):
    return _compute_replacement(113, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_113'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_113}


def vov_replacement_114(**data):
    return _compute_replacement(114, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_114'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_114}


def vov_replacement_115(**data):
    return _compute_replacement(115, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_115'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_115}


def vov_replacement_116(**data):
    return _compute_replacement(116, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_116'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_116}


def vov_replacement_117(**data):
    return _compute_replacement(117, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_117'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_117}


def vov_replacement_118(**data):
    return _compute_replacement(118, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_118'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_118}


def vov_replacement_119(**data):
    return _compute_replacement(119, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_119'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_119}


def vov_replacement_120(**data):
    return _compute_replacement(120, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_120'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_120}


def vov_replacement_121(**data):
    return _compute_replacement(121, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_121'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_121}


def vov_replacement_122(**data):
    return _compute_replacement(122, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_122'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_122}


def vov_replacement_123(**data):
    return _compute_replacement(123, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_123'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_123}


def vov_replacement_124(**data):
    return _compute_replacement(124, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_124'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_124}


def vov_replacement_125(**data):
    return _compute_replacement(125, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_125'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_125}


def vov_replacement_126(**data):
    return _compute_replacement(126, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_126'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_126}


def vov_replacement_127(**data):
    return _compute_replacement(127, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_127'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_127}


def vov_replacement_128(**data):
    return _compute_replacement(128, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_128'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_128}


def vov_replacement_129(**data):
    return _compute_replacement(129, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_129'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_129}


def vov_replacement_130(**data):
    return _compute_replacement(130, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_130'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_130}


def vov_replacement_131(**data):
    return _compute_replacement(131, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_131'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_131}


def vov_replacement_132(**data):
    return _compute_replacement(132, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_132'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_132}


def vov_replacement_133(**data):
    return _compute_replacement(133, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_133'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_133}


def vov_replacement_134(**data):
    return _compute_replacement(134, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_134'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_134}


def vov_replacement_135(**data):
    return _compute_replacement(135, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_135'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_135}


def vov_replacement_136(**data):
    return _compute_replacement(136, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_136'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_136}


def vov_replacement_137(**data):
    return _compute_replacement(137, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_137'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_137}


def vov_replacement_138(**data):
    return _compute_replacement(138, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_138'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_138}


def vov_replacement_139(**data):
    return _compute_replacement(139, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_139'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_139}


def vov_replacement_140(**data):
    return _compute_replacement(140, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_140'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_140}


def vov_replacement_141(**data):
    return _compute_replacement(141, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_141'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_141}


def vov_replacement_142(**data):
    return _compute_replacement(142, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_142'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_142}


def vov_replacement_143(**data):
    return _compute_replacement(143, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_143'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_143}


def vov_replacement_144(**data):
    return _compute_replacement(144, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_144'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_144}


def vov_replacement_145(**data):
    return _compute_replacement(145, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_145'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_145}


def vov_replacement_146(**data):
    return _compute_replacement(146, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_146'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_146}


def vov_replacement_147(**data):
    return _compute_replacement(147, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_147'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_147}


def vov_replacement_148(**data):
    return _compute_replacement(148, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_148'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_148}


def vov_replacement_149(**data):
    return _compute_replacement(149, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_149'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_149}


def vov_replacement_150(**data):
    return _compute_replacement(150, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_150'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_150}


def vov_replacement_151(**data):
    return _compute_replacement(151, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_151'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_151}


def vov_replacement_152(**data):
    return _compute_replacement(152, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_152'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_152}


def vov_replacement_153(**data):
    return _compute_replacement(153, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_153'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_153}


def vov_replacement_154(**data):
    return _compute_replacement(154, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_154'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_154}


def vov_replacement_155(**data):
    return _compute_replacement(155, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_155'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_155}


def vov_replacement_156(**data):
    return _compute_replacement(156, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_156'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_156}


def vov_replacement_157(**data):
    return _compute_replacement(157, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_157'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_157}


def vov_replacement_158(**data):
    return _compute_replacement(158, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_158'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_158}


def vov_replacement_159(**data):
    return _compute_replacement(159, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_159'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_159}


def vov_replacement_160(**data):
    return _compute_replacement(160, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_160'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_160}


def vov_replacement_161(**data):
    return _compute_replacement(161, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_161'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_161}


def vov_replacement_162(**data):
    return _compute_replacement(162, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_162'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_162}


def vov_replacement_163(**data):
    return _compute_replacement(163, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_163'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_163}


def vov_replacement_164(**data):
    return _compute_replacement(164, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_164'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_164}


def vov_replacement_165(**data):
    return _compute_replacement(165, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_165'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_165}


def vov_replacement_166(**data):
    return _compute_replacement(166, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_166'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_166}


def vov_replacement_167(**data):
    return _compute_replacement(167, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_167'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_167}


def vov_replacement_168(**data):
    return _compute_replacement(168, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_168'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_168}


def vov_replacement_169(**data):
    return _compute_replacement(169, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_169'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_169}


def vov_replacement_170(**data):
    return _compute_replacement(170, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_170'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_170}


def vov_replacement_171(**data):
    return _compute_replacement(171, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_171'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_171}


def vov_replacement_172(**data):
    return _compute_replacement(172, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_172'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_172}


def vov_replacement_173(**data):
    return _compute_replacement(173, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_173'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_173}


def vov_replacement_174(**data):
    return _compute_replacement(174, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_174'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_174}


def vov_replacement_175(**data):
    return _compute_replacement(175, **data)
VOV_REPLACEMENT_BASE_REGISTRY['vov_replacement_175'] = {'inputs': REPLACEMENT_INPUTS[CATEGORY], 'func': vov_replacement_175}

