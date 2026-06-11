import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f34_value_creation_proxy(roic, de):
    # roic - implied debt-weighted cost (de/(1+de) * 0.06 + 1/(1+de) * 0.10)
    debt_share = de / (1.0 + de.abs())
    eq_share = 1.0 - debt_share
    wacc = debt_share * 0.06 + eq_share * 0.10
    return roic - wacc


def _f34_excess_return_proxy(roic, roa, de):
    debt_share = de / (1.0 + de.abs())
    eq_share = 1.0 - debt_share
    cost = debt_share * 0.06 + eq_share * 0.10
    return (roic - cost) + 0.3 * (roic - roa)


def _f34_economic_profit_signal(roic, invcap, w):
    # economic profit proxy = (roic - 0.08) * invcap
    ep = (roic - 0.08) * invcap
    return _mean(ep, w)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_base_v001_signal(roic, de, closeadj):
    result = _f34_value_creation_proxy(roic, de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_21d_base_v002_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_63d_base_v003_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_126d_base_v004_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_252d_base_v005_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_504d_base_v006_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_5d_base_v007_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_10d_base_v008_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_42d_base_v009_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_189d_base_v010_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_378d_base_v011_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_base_v012_signal(roic, roa, de, closeadj):
    result = _f34_excess_return_proxy(roic, roa, de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_21d_base_v013_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_63d_base_v014_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_126d_base_v015_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_252d_base_v016_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_504d_base_v017_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_5d_base_v018_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_42d_base_v019_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_189d_base_v020_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_378d_base_v021_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_21d_base_v022_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_63d_base_v023_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_126d_base_v024_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 126) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_252d_base_v025_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_504d_base_v026_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 504) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_5d_base_v027_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 5) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_42d_base_v028_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 42) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_189d_base_v029_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 189) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_378d_base_v030_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 378) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_63d_base_v031_signal(roic, de, closeadj):
    result = _std(_f34_value_creation_proxy(roic, de), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_252d_base_v032_signal(roic, de, closeadj):
    result = _std(_f34_value_creation_proxy(roic, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_504d_base_v033_signal(roic, de, closeadj):
    result = _std(_f34_value_creation_proxy(roic, de), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_z_63d_base_v034_signal(roic, de, closeadj):
    result = _z(_f34_value_creation_proxy(roic, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_z_252d_base_v035_signal(roic, de, closeadj):
    result = _z(_f34_value_creation_proxy(roic, de), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_std_63d_base_v036_signal(roic, roa, de, closeadj):
    result = _std(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_std_252d_base_v037_signal(roic, roa, de, closeadj):
    result = _std(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_z_63d_base_v038_signal(roic, roa, de, closeadj):
    result = _z(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_z_252d_base_v039_signal(roic, roa, de, closeadj):
    result = _z(_f34_excess_return_proxy(roic, roa, de), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_std_63d_base_v040_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = _std(base, 63) * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_std_252d_base_v041_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = _std(base, 252) * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_ema_63d_base_v042_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_ema_252d_base_v043_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_ema_63d_base_v044_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_ema_252d_base_v045_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_ema_63d_base_v046_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = base.ewm(span=63, min_periods=20).mean() * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_ema_252d_base_v047_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = base.ewm(span=252, min_periods=60).mean() * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_63d_base_v048_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_252d_base_v049_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_63d_base_v050_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_252d_base_v051_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_63d_base_v052_signal(roic, invcap, closeadj):
    base = _f34_economic_profit_signal(roic, invcap, 63)
    result = (base - base.shift(63)) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_252d_base_v053_signal(roic, invcap, closeadj):
    base = _f34_economic_profit_signal(roic, invcap, 252)
    result = (base - base.shift(252)) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xprice_63d_base_v054_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xprice_252d_base_v055_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xprice_63d_base_v056_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xprice_252d_base_v057_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xprice_63d_base_v058_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 63) * closeadj / 1e9 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xprice_252d_base_v059_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / 1e9 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_rank_63d_base_v060_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_rank_252d_base_v061_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_rank_63d_base_v062_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_rank_252d_base_v063_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_rank_63d_base_v064_signal(roic, invcap, closeadj):
    base = _f34_economic_profit_signal(roic, invcap, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_rank_252d_base_v065_signal(roic, invcap, closeadj):
    base = _f34_economic_profit_signal(roic, invcap, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sign_63d_base_v066_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    pos = (base > 0).astype(float)
    result = _mean(pos, 63) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sign_252d_base_v067_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    pos = (base > 0).astype(float)
    result = _mean(pos, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_sign_63d_base_v068_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    pos = (base > 0).astype(float)
    result = _mean(pos, 63) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_sign_252d_base_v069_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    pos = (base > 0).astype(float)
    result = _mean(pos, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sq_63d_base_v070_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = _mean(base * base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sq_252d_base_v071_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_compositeq_63d_base_v072_signal(roic, roa, de, invcap, closeadj):
    a = _mean(_f34_value_creation_proxy(roic, de), 63)
    b = _mean(_f34_excess_return_proxy(roic, roa, de), 63)
    c = _f34_economic_profit_signal(roic, invcap, 63) / 1e9
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_compositeq_252d_base_v073_signal(roic, roa, de, invcap, closeadj):
    a = _mean(_f34_value_creation_proxy(roic, de), 252)
    b = _mean(_f34_excess_return_proxy(roic, roa, de), 252)
    c = _f34_economic_profit_signal(roic, invcap, 252) / 1e9
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xde_63d_base_v074_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xde_252d_base_v075_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_base_v001_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_21d_base_v002_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_63d_base_v003_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_126d_base_v004_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_252d_base_v005_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_504d_base_v006_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_5d_base_v007_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_10d_base_v008_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_42d_base_v009_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_189d_base_v010_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_378d_base_v011_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_base_v012_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_21d_base_v013_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_63d_base_v014_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_126d_base_v015_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_252d_base_v016_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_504d_base_v017_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_5d_base_v018_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_42d_base_v019_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_189d_base_v020_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_378d_base_v021_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_21d_base_v022_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_63d_base_v023_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_126d_base_v024_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_252d_base_v025_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_504d_base_v026_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_5d_base_v027_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_42d_base_v028_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_189d_base_v029_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_378d_base_v030_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_63d_base_v031_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_252d_base_v032_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_std_504d_base_v033_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_z_63d_base_v034_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_z_252d_base_v035_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_std_63d_base_v036_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_std_252d_base_v037_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_z_63d_base_v038_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_z_252d_base_v039_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_std_63d_base_v040_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_std_252d_base_v041_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_ema_63d_base_v042_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_ema_252d_base_v043_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_ema_63d_base_v044_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_ema_252d_base_v045_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_ema_63d_base_v046_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_ema_252d_base_v047_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_63d_base_v048_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_252d_base_v049_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_63d_base_v050_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_252d_base_v051_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_63d_base_v052_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_252d_base_v053_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xprice_63d_base_v054_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xprice_252d_base_v055_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xprice_63d_base_v056_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xprice_252d_base_v057_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xprice_63d_base_v058_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xprice_252d_base_v059_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_rank_63d_base_v060_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_rank_252d_base_v061_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_rank_63d_base_v062_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_rank_252d_base_v063_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_rank_63d_base_v064_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_rank_252d_base_v065_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sign_63d_base_v066_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sign_252d_base_v067_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_sign_63d_base_v068_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_sign_252d_base_v069_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sq_63d_base_v070_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sq_252d_base_v071_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_compositeq_63d_base_v072_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_compositeq_252d_base_v073_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xde_63d_base_v074_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xde_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_ROIC_VS_WACC_SPREAD_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roa  = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    de   = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    invcap = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")

    cols = {
        "closeadj": closeadj, "roa": roa, "roic": roic, "de": de, "invcap": invcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_value_creation_proxy", "_f34_excess_return_proxy", "_f34_economic_profit_signal")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f34_roic_vs_wacc_spread_proxy_base_001_075_claude: {n_features} features pass")
