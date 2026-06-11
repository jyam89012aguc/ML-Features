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

def vcl_001_pe_compression_z_21(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (-_z(pe, 21)).reindex(close.index)

def vcl_002_pb_compression_z_42(close, pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    return (-_z(pb, 42)).reindex(close.index)

def vcl_003_ps_compression_z_63(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 63)).reindex(close.index)

def vcl_005_ev_marketcap_gap_126(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(126, min_periods=max(3, 126//4)).mean()).reindex(close.index)

def vcl_006_dividend_yield_spike_189(close, dividends):
    close = _s(close)
    dividends = _align_quarterly_to_daily(dividends, close)
    return (_z(_safe_div(dividends, close), 189)).reindex(close.index)

def vcl_007_earnings_yield_spike_252(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 252)).reindex(close.index)

def vcl_008_valuation_history_depth_378(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(378, min_periods=max(3, 378//4)).max())).reindex(close.index)

def vcl_009_pe_compression_z_504(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (-_z(pe, 504)).reindex(close.index)

def vcl_010_pb_compression_z_756(close, pb):
    close = _s(close)
    pb = _align_quarterly_to_daily(pb, close)
    return (-_z(pb, 756)).reindex(close.index)

def vcl_011_ps_compression_z_1008(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 1008)).reindex(close.index)

def vcl_013_ev_marketcap_gap_1512(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)

def vcl_014_dividend_yield_spike_63(close, dividends):
    close = _s(close)
    dividends = _align_quarterly_to_daily(dividends, close)
    return (_z(_safe_div(dividends, close), 63)).reindex(close.index)


def vcl_016_valuation_history_depth_21(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(21, min_periods=max(3, 21//4)).max())).reindex(close.index)



def vcl_019_ps_compression_z_84(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 84)).reindex(close.index)

def vcl_021_ev_marketcap_gap_189(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(close.index)


def vcl_023_earnings_yield_spike_378(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 378)).reindex(close.index)

def vcl_024_valuation_history_depth_504(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(504, min_periods=max(3, 504//4)).max())).reindex(close.index)



def vcl_027_ps_compression_z_1260(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 1260)).reindex(close.index)

def vcl_029_ev_marketcap_gap_63(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)


def vcl_031_earnings_yield_spike_21(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 21)).reindex(close.index)

def vcl_032_valuation_history_depth_42(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(42, min_periods=max(3, 42//4)).max())).reindex(close.index)



def vcl_035_ps_compression_z_126(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 126)).reindex(close.index)

def vcl_037_ev_marketcap_gap_252(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)


def vcl_039_earnings_yield_spike_504(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 504)).reindex(close.index)

def vcl_040_valuation_history_depth_756(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(756, min_periods=max(3, 756//4)).max())).reindex(close.index)



def vcl_043_ps_compression_z_1512(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 1512)).reindex(close.index)



def vcl_047_earnings_yield_spike_42(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 42)).reindex(close.index)

def vcl_048_valuation_history_depth_63(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(63, min_periods=max(3, 63//4)).max())).reindex(close.index)



def vcl_051_ps_compression_z_189(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 189)).reindex(close.index)

def vcl_053_ev_marketcap_gap_378(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(378, min_periods=max(3, 378//4)).mean()).reindex(close.index)


def vcl_055_earnings_yield_spike_756(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 756)).reindex(close.index)

def vcl_056_valuation_history_depth_1008(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(1008, min_periods=max(3, 1008//4)).max())).reindex(close.index)




def vcl_061_ev_marketcap_gap_21(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)



def vcl_064_valuation_history_depth_84(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(84, min_periods=max(3, 84//4)).max())).reindex(close.index)



def vcl_067_ps_compression_z_252(close, ps):
    close = _s(close)
    ps = _align_quarterly_to_daily(ps, close)
    return (-_z(ps, 252)).reindex(close.index)

def vcl_069_ev_marketcap_gap_504(close, ev, marketcap):
    close = _s(close)
    ev = _align_quarterly_to_daily(ev, close)
    marketcap = _align_quarterly_to_daily(marketcap, close)
    return (_safe_div(ev - marketcap, marketcap).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(close.index)


def vcl_071_earnings_yield_spike_1008(close, eps):
    close = _s(close)
    eps = _align_quarterly_to_daily(eps, close)
    return (_z(_safe_div(eps, close), 1008)).reindex(close.index)

def vcl_072_valuation_history_depth_1260(close, pe):
    close = _s(close)
    pe = _align_quarterly_to_daily(pe, close)
    return (_safe_div(pe, pe.rolling(1260, min_periods=max(3, 1260//4)).max())).reindex(close.index)





VALUATION_COLLAPSE_REGISTRY_001_075 = {
    'vcl_001_pe_compression_z_21': {'inputs': ['close', 'pe'], 'func': vcl_001_pe_compression_z_21},
    'vcl_002_pb_compression_z_42': {'inputs': ['close', 'pb'], 'func': vcl_002_pb_compression_z_42},
    'vcl_003_ps_compression_z_63': {'inputs': ['close', 'ps'], 'func': vcl_003_ps_compression_z_63},
    'vcl_005_ev_marketcap_gap_126': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_005_ev_marketcap_gap_126},
    'vcl_006_dividend_yield_spike_189': {'inputs': ['close', 'dividends'], 'func': vcl_006_dividend_yield_spike_189},
    'vcl_007_earnings_yield_spike_252': {'inputs': ['close', 'eps'], 'func': vcl_007_earnings_yield_spike_252},
    'vcl_008_valuation_history_depth_378': {'inputs': ['close', 'pe'], 'func': vcl_008_valuation_history_depth_378},
    'vcl_009_pe_compression_z_504': {'inputs': ['close', 'pe'], 'func': vcl_009_pe_compression_z_504},
    'vcl_010_pb_compression_z_756': {'inputs': ['close', 'pb'], 'func': vcl_010_pb_compression_z_756},
    'vcl_011_ps_compression_z_1008': {'inputs': ['close', 'ps'], 'func': vcl_011_ps_compression_z_1008},
    'vcl_013_ev_marketcap_gap_1512': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_013_ev_marketcap_gap_1512},
    'vcl_014_dividend_yield_spike_63': {'inputs': ['close', 'dividends'], 'func': vcl_014_dividend_yield_spike_63},
    'vcl_016_valuation_history_depth_21': {'inputs': ['close', 'pe'], 'func': vcl_016_valuation_history_depth_21},
    'vcl_019_ps_compression_z_84': {'inputs': ['close', 'ps'], 'func': vcl_019_ps_compression_z_84},
    'vcl_021_ev_marketcap_gap_189': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_021_ev_marketcap_gap_189},
    'vcl_023_earnings_yield_spike_378': {'inputs': ['close', 'eps'], 'func': vcl_023_earnings_yield_spike_378},
    'vcl_024_valuation_history_depth_504': {'inputs': ['close', 'pe'], 'func': vcl_024_valuation_history_depth_504},
    'vcl_027_ps_compression_z_1260': {'inputs': ['close', 'ps'], 'func': vcl_027_ps_compression_z_1260},
    'vcl_029_ev_marketcap_gap_63': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_029_ev_marketcap_gap_63},
    'vcl_031_earnings_yield_spike_21': {'inputs': ['close', 'eps'], 'func': vcl_031_earnings_yield_spike_21},
    'vcl_032_valuation_history_depth_42': {'inputs': ['close', 'pe'], 'func': vcl_032_valuation_history_depth_42},
    'vcl_035_ps_compression_z_126': {'inputs': ['close', 'ps'], 'func': vcl_035_ps_compression_z_126},
    'vcl_037_ev_marketcap_gap_252': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_037_ev_marketcap_gap_252},
    'vcl_039_earnings_yield_spike_504': {'inputs': ['close', 'eps'], 'func': vcl_039_earnings_yield_spike_504},
    'vcl_040_valuation_history_depth_756': {'inputs': ['close', 'pe'], 'func': vcl_040_valuation_history_depth_756},
    'vcl_043_ps_compression_z_1512': {'inputs': ['close', 'ps'], 'func': vcl_043_ps_compression_z_1512},
    'vcl_047_earnings_yield_spike_42': {'inputs': ['close', 'eps'], 'func': vcl_047_earnings_yield_spike_42},
    'vcl_048_valuation_history_depth_63': {'inputs': ['close', 'pe'], 'func': vcl_048_valuation_history_depth_63},
    'vcl_051_ps_compression_z_189': {'inputs': ['close', 'ps'], 'func': vcl_051_ps_compression_z_189},
    'vcl_053_ev_marketcap_gap_378': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_053_ev_marketcap_gap_378},
    'vcl_055_earnings_yield_spike_756': {'inputs': ['close', 'eps'], 'func': vcl_055_earnings_yield_spike_756},
    'vcl_056_valuation_history_depth_1008': {'inputs': ['close', 'pe'], 'func': vcl_056_valuation_history_depth_1008},
    'vcl_061_ev_marketcap_gap_21': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_061_ev_marketcap_gap_21},
    'vcl_064_valuation_history_depth_84': {'inputs': ['close', 'pe'], 'func': vcl_064_valuation_history_depth_84},
    'vcl_067_ps_compression_z_252': {'inputs': ['close', 'ps'], 'func': vcl_067_ps_compression_z_252},
    'vcl_069_ev_marketcap_gap_504': {'inputs': ['close', 'ev', 'marketcap'], 'func': vcl_069_ev_marketcap_gap_504},
    'vcl_071_earnings_yield_spike_1008': {'inputs': ['close', 'eps'], 'func': vcl_071_earnings_yield_spike_1008},
    'vcl_072_valuation_history_depth_1260': {'inputs': ['close', 'pe'], 'func': vcl_072_valuation_history_depth_1260},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "valuation"
_BASEFILL_FAMILY_ID = 77


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


def vcl_basefill_004(**data):
    return _bf_compute(4, **data)


def vcl_basefill_012(**data):
    return _bf_compute(12, **data)


def vcl_basefill_015(**data):
    return _bf_compute(15, **data)


def vcl_basefill_017(**data):
    return _bf_compute(17, **data)


def vcl_basefill_018(**data):
    return _bf_compute(18, **data)


def vcl_basefill_020(**data):
    return _bf_compute(20, **data)


def vcl_basefill_022(**data):
    return _bf_compute(22, **data)


def vcl_basefill_025(**data):
    return _bf_compute(25, **data)


def vcl_basefill_026(**data):
    return _bf_compute(26, **data)


def vcl_basefill_028(**data):
    return _bf_compute(28, **data)


def vcl_basefill_030(**data):
    return _bf_compute(30, **data)


def vcl_basefill_033(**data):
    return _bf_compute(33, **data)


def vcl_basefill_034(**data):
    return _bf_compute(34, **data)


def vcl_basefill_036(**data):
    return _bf_compute(36, **data)


def vcl_basefill_038(**data):
    return _bf_compute(38, **data)


def vcl_basefill_041(**data):
    return _bf_compute(41, **data)


def vcl_basefill_042(**data):
    return _bf_compute(42, **data)


def vcl_basefill_044(**data):
    return _bf_compute(44, **data)


def vcl_basefill_045(**data):
    return _bf_compute(45, **data)


def vcl_basefill_046(**data):
    return _bf_compute(46, **data)


def vcl_basefill_049(**data):
    return _bf_compute(49, **data)


def vcl_basefill_050(**data):
    return _bf_compute(50, **data)


def vcl_basefill_052(**data):
    return _bf_compute(52, **data)


def vcl_basefill_054(**data):
    return _bf_compute(54, **data)


def vcl_basefill_057(**data):
    return _bf_compute(57, **data)


def vcl_basefill_058(**data):
    return _bf_compute(58, **data)


def vcl_basefill_059(**data):
    return _bf_compute(59, **data)


def vcl_basefill_060(**data):
    return _bf_compute(60, **data)


def vcl_basefill_062(**data):
    return _bf_compute(62, **data)


def vcl_basefill_063(**data):
    return _bf_compute(63, **data)


def vcl_basefill_065(**data):
    return _bf_compute(65, **data)


def vcl_basefill_066(**data):
    return _bf_compute(66, **data)


def vcl_basefill_068(**data):
    return _bf_compute(68, **data)


def vcl_basefill_070(**data):
    return _bf_compute(70, **data)


def vcl_basefill_073(**data):
    return _bf_compute(73, **data)


def vcl_basefill_074(**data):
    return _bf_compute(74, **data)


def vcl_basefill_075(**data):
    return _bf_compute(75, **data)

VALUATION_COLLAPSE_REGISTRY_001_075.update({
    'vcl_basefill_004': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_004},
    'vcl_basefill_012': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_012},
    'vcl_basefill_015': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_015},
    'vcl_basefill_017': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_017},
    'vcl_basefill_018': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_018},
    'vcl_basefill_020': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_020},
    'vcl_basefill_022': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_022},
    'vcl_basefill_025': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_025},
    'vcl_basefill_026': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_026},
    'vcl_basefill_028': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_028},
    'vcl_basefill_030': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_030},
    'vcl_basefill_033': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_033},
    'vcl_basefill_034': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_034},
    'vcl_basefill_036': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_036},
    'vcl_basefill_038': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_038},
    'vcl_basefill_041': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_041},
    'vcl_basefill_042': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_042},
    'vcl_basefill_044': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_044},
    'vcl_basefill_045': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_045},
    'vcl_basefill_046': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_046},
    'vcl_basefill_049': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_049},
    'vcl_basefill_050': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_050},
    'vcl_basefill_052': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_052},
    'vcl_basefill_054': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_054},
    'vcl_basefill_057': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_057},
    'vcl_basefill_058': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_058},
    'vcl_basefill_059': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_059},
    'vcl_basefill_060': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_060},
    'vcl_basefill_062': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_062},
    'vcl_basefill_063': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_063},
    'vcl_basefill_065': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_065},
    'vcl_basefill_066': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_066},
    'vcl_basefill_068': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_068},
    'vcl_basefill_070': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_070},
    'vcl_basefill_073': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_073},
    'vcl_basefill_074': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_074},
    'vcl_basefill_075': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'shareswa', 'marketcap', 'ev', 'pe', 'pb', 'ps'], 'func': vcl_basefill_075},
})
