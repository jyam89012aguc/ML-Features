"""pricing_power_loss_signal base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for value-capture-share / pricing-power loss detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly fundamentals only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
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


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f42_pplo_151_unit_volume_vs_asp_decomposition_yoy(revenue: pd.Series, cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """Volume proxy = revenue/inventory (turnover); Price proxy = revenue/cor. Yoy_pct(vol) - Yoy_pct(price)."""
    vol_proxy = _safe_div(revenue, inventory)
    price_proxy = _safe_div(revenue, cor)
    return _yoy_pct(vol_proxy) - _yoy_pct(price_proxy)


def f42_pplo_152_discount_promo_intensity_timing_4q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Sliding 4q count of quarters where Δgp/gp < -0.05 AND Δrevenue/revenue > 0.05 (margin sacrificed for top-line)."""
    gp_prev = gp.shift(1)
    rev_prev = revenue.shift(1)
    d_gp_pct = _safe_div(gp - gp_prev, gp_prev)
    d_rev_pct = _safe_div(revenue - rev_prev, rev_prev)
    flag = ((d_gp_pct < -0.05) & (d_rev_pct > 0.05)).astype(float)
    return flag.rolling(QQTRS, min_periods=2).sum()


def f42_pplo_153_price_war_capitulation_indicator(revenue: pd.Series, cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """+1 if (revenue/cor) yoy < -0.05 AND (revenue/inventory) yoy > 0.10 (ASP down AND volume up — capitulation pricing)."""
    price_proxy = _safe_div(revenue, cor)
    vol_proxy = _safe_div(revenue, inventory)
    price_yoy = _yoy_pct(price_proxy)
    vol_yoy = _yoy_pct(vol_proxy)
    flag = ((price_yoy < -0.05) & (vol_yoy > 0.10)).astype(float)
    # preserve NaN where either input was insufficient
    mask = price_yoy.isna() | vol_yoy.isna()
    return flag.where(~mask, np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

PRICING_POWER_LOSS_SIGNAL_BASE_REGISTRY_151_225 = {
    "f42_pplo_151_unit_volume_vs_asp_decomposition_yoy": {"inputs": ["revenue", "cor", "inventory"], "func": f42_pplo_151_unit_volume_vs_asp_decomposition_yoy},
    "f42_pplo_152_discount_promo_intensity_timing_4q": {"inputs": ["revenue", "gp"], "func": f42_pplo_152_discount_promo_intensity_timing_4q},
    "f42_pplo_153_price_war_capitulation_indicator": {"inputs": ["revenue", "cor", "inventory"], "func": f42_pplo_153_price_war_capitulation_indicator},
}
