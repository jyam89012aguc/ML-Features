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

def icv_003_fcf_burn_to_cash_63(close, fcf, cash):
    close = _s(close)
    fcf = _align_quarterly_to_daily(fcf, close)
    cash = _align_quarterly_to_daily(cash, close)
    return (-_safe_div(fcf, cash).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)

def icv_004_debt_to_equity_84(close, equity, debt):
    close = _s(close)
    equity = _align_quarterly_to_daily(equity, close)
    debt = _align_quarterly_to_daily(debt, close)
    return (_safe_div(debt, equity).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(close.index)

def icv_005_debt_to_assets_126(close, debt, assets):
    close = _s(close)
    debt = _align_quarterly_to_daily(debt, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(debt, assets).rolling(126, min_periods=max(3, 126//4)).mean()).reindex(close.index)

def icv_007_interest_coverage_stress_252(close, ebit, interest_expense):
    close = _s(close)
    ebit = _align_quarterly_to_daily(ebit, close)
    interest_expense = _align_quarterly_to_daily(interest_expense, close)
    return (-_safe_div(ebit, interest_expense).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)

def icv_012_accrual_gap_1260(close, netinc, fcf, assets):
    close = _s(close)
    netinc = _align_quarterly_to_daily(netinc, close)
    fcf = _align_quarterly_to_daily(fcf, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(netinc - fcf, assets).rolling(1260, min_periods=max(3, 1260//4)).mean()).reindex(close.index)


def icv_016_debt_to_equity_21(close, equity, debt):
    close = _s(close)
    equity = _align_quarterly_to_daily(equity, close)
    debt = _align_quarterly_to_daily(debt, close)
    return (_safe_div(debt, equity).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)

def icv_017_debt_to_assets_42(close, debt, assets):
    close = _s(close)
    debt = _align_quarterly_to_daily(debt, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(debt, assets).rolling(42, min_periods=max(3, 42//4)).mean()).reindex(close.index)

def icv_019_interest_coverage_stress_84(close, ebit, interest_expense):
    close = _s(close)
    ebit = _align_quarterly_to_daily(ebit, close)
    interest_expense = _align_quarterly_to_daily(interest_expense, close)
    return (-_safe_div(ebit, interest_expense).rolling(84, min_periods=max(3, 84//4)).mean()).reindex(close.index)

def icv_024_accrual_gap_504(close, netinc, fcf, assets):
    close = _s(close)
    netinc = _align_quarterly_to_daily(netinc, close)
    fcf = _align_quarterly_to_daily(fcf, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(netinc - fcf, assets).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(close.index)

def icv_027_fcf_burn_to_cash_1260(close, fcf, cash):
    close = _s(close)
    fcf = _align_quarterly_to_daily(fcf, close)
    cash = _align_quarterly_to_daily(cash, close)
    return (-_safe_div(fcf, cash).rolling(1260, min_periods=max(3, 1260//4)).mean()).reindex(close.index)

def icv_028_debt_to_equity_1512(close, equity, debt):
    close = _s(close)
    equity = _align_quarterly_to_daily(equity, close)
    debt = _align_quarterly_to_daily(debt, close)
    return (_safe_div(debt, equity).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)

def icv_029_debt_to_assets_63(close, debt, assets):
    close = _s(close)
    debt = _align_quarterly_to_daily(debt, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(debt, assets).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)

def icv_031_interest_coverage_stress_21(close, ebit, interest_expense):
    close = _s(close)
    ebit = _align_quarterly_to_daily(ebit, close)
    interest_expense = _align_quarterly_to_daily(interest_expense, close)
    return (-_safe_div(ebit, interest_expense).rolling(21, min_periods=max(3, 21//4)).mean()).reindex(close.index)

def icv_036_accrual_gap_189(close, netinc, fcf, assets):
    close = _s(close)
    netinc = _align_quarterly_to_daily(netinc, close)
    fcf = _align_quarterly_to_daily(fcf, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(netinc - fcf, assets).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(close.index)

def icv_039_fcf_burn_to_cash_504(close, fcf, cash):
    close = _s(close)
    fcf = _align_quarterly_to_daily(fcf, close)
    cash = _align_quarterly_to_daily(cash, close)
    return (-_safe_div(fcf, cash).rolling(504, min_periods=max(3, 504//4)).mean()).reindex(close.index)

def icv_040_debt_to_equity_756(close, equity, debt):
    close = _s(close)
    equity = _align_quarterly_to_daily(equity, close)
    debt = _align_quarterly_to_daily(debt, close)
    return (_safe_div(debt, equity).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(close.index)

def icv_041_debt_to_assets_1008(close, debt, assets):
    close = _s(close)
    debt = _align_quarterly_to_daily(debt, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(debt, assets).rolling(1008, min_periods=max(3, 1008//4)).mean()).reindex(close.index)

def icv_043_interest_coverage_stress_1512(close, ebit, interest_expense):
    close = _s(close)
    ebit = _align_quarterly_to_daily(ebit, close)
    interest_expense = _align_quarterly_to_daily(interest_expense, close)
    return (-_safe_div(ebit, interest_expense).rolling(1512, min_periods=max(3, 1512//4)).mean()).reindex(close.index)

def icv_048_accrual_gap_63(close, netinc, fcf, assets):
    close = _s(close)
    netinc = _align_quarterly_to_daily(netinc, close)
    fcf = _align_quarterly_to_daily(fcf, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(netinc - fcf, assets).rolling(63, min_periods=max(3, 63//4)).mean()).reindex(close.index)

def icv_051_fcf_burn_to_cash_189(close, fcf, cash):
    close = _s(close)
    fcf = _align_quarterly_to_daily(fcf, close)
    cash = _align_quarterly_to_daily(cash, close)
    return (-_safe_div(fcf, cash).rolling(189, min_periods=max(3, 189//4)).mean()).reindex(close.index)

def icv_052_debt_to_equity_252(close, equity, debt):
    close = _s(close)
    equity = _align_quarterly_to_daily(equity, close)
    debt = _align_quarterly_to_daily(debt, close)
    return (_safe_div(debt, equity).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)

def icv_053_debt_to_assets_378(close, debt, assets):
    close = _s(close)
    debt = _align_quarterly_to_daily(debt, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(debt, assets).rolling(378, min_periods=max(3, 378//4)).mean()).reindex(close.index)

def icv_055_interest_coverage_stress_756(close, ebit, interest_expense):
    close = _s(close)
    ebit = _align_quarterly_to_daily(ebit, close)
    interest_expense = _align_quarterly_to_daily(interest_expense, close)
    return (-_safe_div(ebit, interest_expense).rolling(756, min_periods=max(3, 756//4)).mean()).reindex(close.index)

def icv_060_accrual_gap_252(close, netinc, fcf, assets):
    close = _s(close)
    netinc = _align_quarterly_to_daily(netinc, close)
    fcf = _align_quarterly_to_daily(fcf, close)
    assets = _align_quarterly_to_daily(assets, close)
    return (_safe_div(netinc - fcf, assets).rolling(252, min_periods=max(3, 252//4)).mean()).reindex(close.index)








INTEREST_COVERAGE_REGISTRY_001_075 = {
    'icv_003_fcf_burn_to_cash_63': {'inputs': ['close', 'fcf', 'cash'], 'func': icv_003_fcf_burn_to_cash_63},
    'icv_004_debt_to_equity_84': {'inputs': ['close', 'equity', 'debt'], 'func': icv_004_debt_to_equity_84},
    'icv_005_debt_to_assets_126': {'inputs': ['close', 'debt', 'assets'], 'func': icv_005_debt_to_assets_126},
    'icv_007_interest_coverage_stress_252': {'inputs': ['close', 'ebit', 'interest_expense'], 'func': icv_007_interest_coverage_stress_252},
    'icv_012_accrual_gap_1260': {'inputs': ['close', 'netinc', 'fcf', 'assets'], 'func': icv_012_accrual_gap_1260},
    'icv_016_debt_to_equity_21': {'inputs': ['close', 'equity', 'debt'], 'func': icv_016_debt_to_equity_21},
    'icv_017_debt_to_assets_42': {'inputs': ['close', 'debt', 'assets'], 'func': icv_017_debt_to_assets_42},
    'icv_019_interest_coverage_stress_84': {'inputs': ['close', 'ebit', 'interest_expense'], 'func': icv_019_interest_coverage_stress_84},
    'icv_024_accrual_gap_504': {'inputs': ['close', 'netinc', 'fcf', 'assets'], 'func': icv_024_accrual_gap_504},
    'icv_027_fcf_burn_to_cash_1260': {'inputs': ['close', 'fcf', 'cash'], 'func': icv_027_fcf_burn_to_cash_1260},
    'icv_028_debt_to_equity_1512': {'inputs': ['close', 'equity', 'debt'], 'func': icv_028_debt_to_equity_1512},
    'icv_029_debt_to_assets_63': {'inputs': ['close', 'debt', 'assets'], 'func': icv_029_debt_to_assets_63},
    'icv_031_interest_coverage_stress_21': {'inputs': ['close', 'ebit', 'interest_expense'], 'func': icv_031_interest_coverage_stress_21},
    'icv_036_accrual_gap_189': {'inputs': ['close', 'netinc', 'fcf', 'assets'], 'func': icv_036_accrual_gap_189},
    'icv_039_fcf_burn_to_cash_504': {'inputs': ['close', 'fcf', 'cash'], 'func': icv_039_fcf_burn_to_cash_504},
    'icv_040_debt_to_equity_756': {'inputs': ['close', 'equity', 'debt'], 'func': icv_040_debt_to_equity_756},
    'icv_041_debt_to_assets_1008': {'inputs': ['close', 'debt', 'assets'], 'func': icv_041_debt_to_assets_1008},
    'icv_043_interest_coverage_stress_1512': {'inputs': ['close', 'ebit', 'interest_expense'], 'func': icv_043_interest_coverage_stress_1512},
    'icv_048_accrual_gap_63': {'inputs': ['close', 'netinc', 'fcf', 'assets'], 'func': icv_048_accrual_gap_63},
    'icv_051_fcf_burn_to_cash_189': {'inputs': ['close', 'fcf', 'cash'], 'func': icv_051_fcf_burn_to_cash_189},
    'icv_052_debt_to_equity_252': {'inputs': ['close', 'equity', 'debt'], 'func': icv_052_debt_to_equity_252},
    'icv_053_debt_to_assets_378': {'inputs': ['close', 'debt', 'assets'], 'func': icv_053_debt_to_assets_378},
    'icv_055_interest_coverage_stress_756': {'inputs': ['close', 'ebit', 'interest_expense'], 'func': icv_055_interest_coverage_stress_756},
    'icv_060_accrual_gap_252': {'inputs': ['close', 'netinc', 'fcf', 'assets'], 'func': icv_060_accrual_gap_252},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "fundamental"
_BASEFILL_FAMILY_ID = 66


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


def icv_basefill_001(**data):
    return _bf_compute(1, **data)


def icv_basefill_002(**data):
    return _bf_compute(2, **data)


def icv_basefill_006(**data):
    return _bf_compute(6, **data)


def icv_basefill_008(**data):
    return _bf_compute(8, **data)


def icv_basefill_009(**data):
    return _bf_compute(9, **data)


def icv_basefill_010(**data):
    return _bf_compute(10, **data)


def icv_basefill_011(**data):
    return _bf_compute(11, **data)


def icv_basefill_013(**data):
    return _bf_compute(13, **data)


def icv_basefill_014(**data):
    return _bf_compute(14, **data)


def icv_basefill_015(**data):
    return _bf_compute(15, **data)


def icv_basefill_018(**data):
    return _bf_compute(18, **data)


def icv_basefill_020(**data):
    return _bf_compute(20, **data)


def icv_basefill_021(**data):
    return _bf_compute(21, **data)


def icv_basefill_022(**data):
    return _bf_compute(22, **data)


def icv_basefill_023(**data):
    return _bf_compute(23, **data)


def icv_basefill_025(**data):
    return _bf_compute(25, **data)


def icv_basefill_026(**data):
    return _bf_compute(26, **data)


def icv_basefill_030(**data):
    return _bf_compute(30, **data)


def icv_basefill_032(**data):
    return _bf_compute(32, **data)


def icv_basefill_033(**data):
    return _bf_compute(33, **data)


def icv_basefill_034(**data):
    return _bf_compute(34, **data)


def icv_basefill_035(**data):
    return _bf_compute(35, **data)


def icv_basefill_037(**data):
    return _bf_compute(37, **data)


def icv_basefill_038(**data):
    return _bf_compute(38, **data)


def icv_basefill_042(**data):
    return _bf_compute(42, **data)


def icv_basefill_044(**data):
    return _bf_compute(44, **data)


def icv_basefill_045(**data):
    return _bf_compute(45, **data)


def icv_basefill_046(**data):
    return _bf_compute(46, **data)


def icv_basefill_047(**data):
    return _bf_compute(47, **data)


def icv_basefill_049(**data):
    return _bf_compute(49, **data)


def icv_basefill_050(**data):
    return _bf_compute(50, **data)


def icv_basefill_054(**data):
    return _bf_compute(54, **data)


def icv_basefill_056(**data):
    return _bf_compute(56, **data)


def icv_basefill_057(**data):
    return _bf_compute(57, **data)


def icv_basefill_058(**data):
    return _bf_compute(58, **data)


def icv_basefill_059(**data):
    return _bf_compute(59, **data)


def icv_basefill_061(**data):
    return _bf_compute(61, **data)


def icv_basefill_062(**data):
    return _bf_compute(62, **data)


def icv_basefill_063(**data):
    return _bf_compute(63, **data)


def icv_basefill_064(**data):
    return _bf_compute(64, **data)


def icv_basefill_065(**data):
    return _bf_compute(65, **data)


def icv_basefill_066(**data):
    return _bf_compute(66, **data)


def icv_basefill_067(**data):
    return _bf_compute(67, **data)


def icv_basefill_068(**data):
    return _bf_compute(68, **data)


def icv_basefill_069(**data):
    return _bf_compute(69, **data)


def icv_basefill_070(**data):
    return _bf_compute(70, **data)


def icv_basefill_071(**data):
    return _bf_compute(71, **data)


def icv_basefill_072(**data):
    return _bf_compute(72, **data)


def icv_basefill_073(**data):
    return _bf_compute(73, **data)


def icv_basefill_074(**data):
    return _bf_compute(74, **data)


def icv_basefill_075(**data):
    return _bf_compute(75, **data)

INTEREST_COVERAGE_REGISTRY_001_075.update({
    'icv_basefill_001': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_001},
    'icv_basefill_002': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_002},
    'icv_basefill_006': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_006},
    'icv_basefill_008': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_008},
    'icv_basefill_009': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_009},
    'icv_basefill_010': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_010},
    'icv_basefill_011': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_011},
    'icv_basefill_013': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_013},
    'icv_basefill_014': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_014},
    'icv_basefill_015': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_015},
    'icv_basefill_018': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_018},
    'icv_basefill_020': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_020},
    'icv_basefill_021': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_021},
    'icv_basefill_022': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_022},
    'icv_basefill_023': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_023},
    'icv_basefill_025': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_025},
    'icv_basefill_026': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_026},
    'icv_basefill_030': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_030},
    'icv_basefill_032': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_032},
    'icv_basefill_033': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_033},
    'icv_basefill_034': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_034},
    'icv_basefill_035': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_035},
    'icv_basefill_037': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_037},
    'icv_basefill_038': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_038},
    'icv_basefill_042': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_042},
    'icv_basefill_044': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_044},
    'icv_basefill_045': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_045},
    'icv_basefill_046': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_046},
    'icv_basefill_047': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_047},
    'icv_basefill_049': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_049},
    'icv_basefill_050': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_050},
    'icv_basefill_054': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_054},
    'icv_basefill_056': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_056},
    'icv_basefill_057': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_057},
    'icv_basefill_058': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_058},
    'icv_basefill_059': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_059},
    'icv_basefill_061': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_061},
    'icv_basefill_062': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_062},
    'icv_basefill_063': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_063},
    'icv_basefill_064': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_064},
    'icv_basefill_065': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_065},
    'icv_basefill_066': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_066},
    'icv_basefill_067': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_067},
    'icv_basefill_068': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_068},
    'icv_basefill_069': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_069},
    'icv_basefill_070': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_070},
    'icv_basefill_071': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_071},
    'icv_basefill_072': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_072},
    'icv_basefill_073': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_073},
    'icv_basefill_074': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_074},
    'icv_basefill_075': {'inputs': ['close', 'revenue', 'netinc', 'fcf', 'assets', 'debt', 'equity', 'cashneq', 'ebit', 'gp'], 'func': icv_basefill_075},
})
