"""competitive_displacement_signal base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for customer-loss / pricing-concession displacement.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

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
#                    FEATURES 151-152
# ============================================================


def f45_cdis_151_customer_loss_proxy_ar_writedown(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """+1 if Δreceivables_q < -0.10 × receivables_prev AND revenue yoy < 0 (AR drop + revenue decline = customer-loss writedown pattern)."""
    rec_prev = receivables.shift(1)
    d_rec = receivables - rec_prev
    pct_drop = _safe_div(d_rec, rec_prev)
    rev_yoy = _yoy_pct(revenue)
    flag = ((pct_drop < -0.10) & (rev_yoy < 0)).astype(float)
    mask = pct_drop.isna() | rev_yoy.isna()
    return flag.where(~mask, np.nan)


def f45_cdis_152_pricing_concession_volume_capitulation(revenue: pd.Series, cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """Same logic as f42_pplo_153 framed as competitive-displacement: ASP down (rev/cor yoy < -0.05) AND volume up (rev/inv yoy > 0.10)."""
    price_proxy = _safe_div(revenue, cor)
    vol_proxy = _safe_div(revenue, inventory)
    price_yoy = _yoy_pct(price_proxy)
    vol_yoy = _yoy_pct(vol_proxy)
    flag = ((price_yoy < -0.05) & (vol_yoy > 0.10)).astype(float)
    mask = price_yoy.isna() | vol_yoy.isna()
    return flag.where(~mask, np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

COMPETITIVE_DISPLACEMENT_SIGNAL_BASE_REGISTRY_151_225 = {
    "f45_cdis_151_customer_loss_proxy_ar_writedown": {"inputs": ["receivables", "revenue"], "func": f45_cdis_151_customer_loss_proxy_ar_writedown},
    "f45_cdis_152_pricing_concession_volume_capitulation": {"inputs": ["revenue", "cor", "inventory"], "func": f45_cdis_152_pricing_concession_volume_capitulation},
}
