"""pricing_power_loss_signal d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _yoy_pct(s, periods=QQTRS):
    return _safe_div(s - s.shift(periods), s.shift(periods))


def f42_pplo_151_unit_volume_vs_asp_decomposition_yoy_d1(revenue: pd.Series, cor: pd.Series, inventory: pd.Series) -> pd.Series:
    vol_proxy = _safe_div(revenue, inventory)
    price_proxy = _safe_div(revenue, cor)
    return (_yoy_pct(vol_proxy) - _yoy_pct(price_proxy)).diff()


def f42_pplo_152_discount_promo_intensity_timing_4q_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    gp_prev = gp.shift(1)
    rev_prev = revenue.shift(1)
    d_gp_pct = _safe_div(gp - gp_prev, gp_prev)
    d_rev_pct = _safe_div(revenue - rev_prev, rev_prev)
    flag = ((d_gp_pct < -0.05) & (d_rev_pct > 0.05)).astype(float)
    return flag.rolling(QQTRS, min_periods=2).sum().diff()


def f42_pplo_153_price_war_capitulation_indicator_d1(revenue: pd.Series, cor: pd.Series, inventory: pd.Series) -> pd.Series:
    price_proxy = _safe_div(revenue, cor)
    vol_proxy = _safe_div(revenue, inventory)
    price_yoy = _yoy_pct(price_proxy)
    vol_yoy = _yoy_pct(vol_proxy)
    flag = ((price_yoy < -0.05) & (vol_yoy > 0.10)).astype(float)
    mask = price_yoy.isna() | vol_yoy.isna()
    return flag.where(~mask, np.nan).diff()


PRICING_POWER_LOSS_SIGNAL_D1_REGISTRY_151_225 = {
    "f42_pplo_151_unit_volume_vs_asp_decomposition_yoy_d1": {"inputs": ["revenue", "cor", "inventory"], "func": f42_pplo_151_unit_volume_vs_asp_decomposition_yoy_d1},
    "f42_pplo_152_discount_promo_intensity_timing_4q_d1": {"inputs": ["revenue", "gp"], "func": f42_pplo_152_discount_promo_intensity_timing_4q_d1},
    "f42_pplo_153_price_war_capitulation_indicator_d1": {"inputs": ["revenue", "cor", "inventory"], "func": f42_pplo_153_price_war_capitulation_indicator_d1},
}
