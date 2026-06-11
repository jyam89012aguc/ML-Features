"""dilution_death_spiral base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for toxic-convert/penny-tier detection.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: composite (SF1 quarterly + SEP daily, pre-aligned upstream). PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
QQTRS = 4


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


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


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f48_ddsp_151_toxic_convertible_signature_q(sharesbas: pd.Series, debtc: pd.Series) -> pd.Series:
    """+1 if sharesbas yoy > 0.5 AND debtc yoy < -0.3 (convert-to-equity mechanism). Uses 4q lag (quarterly cadence)."""
    if sharesbas is None or debtc is None:
        return pd.Series(np.nan)
    sb_yoy = _safe_div(sharesbas - sharesbas.shift(QQTRS), sharesbas.shift(QQTRS).abs())
    dc_yoy = _safe_div(debtc - debtc.shift(QQTRS), debtc.shift(QQTRS).abs())
    cond = (sb_yoy > 0.5) & (dc_yoy < -0.3)
    out = cond.astype(float)
    return out.where(sb_yoy.notna() & dc_yoy.notna(), np.nan)


def f48_ddsp_152_sub_5_dollar_spiral_indicator(sharesbas: pd.Series, close: pd.Series) -> pd.Series:
    """+1 if close < 5 AND sharesbas yoy > 0.3 AND close 63d return < -0.3. sharesbas yoy on 252d lag (daily SEP)."""
    if sharesbas is None or close is None:
        return pd.Series(np.nan)
    sb_yoy = _safe_div(sharesbas - sharesbas.shift(YDAYS), sharesbas.shift(YDAYS).abs())
    close_63d_ret = _safe_div(close - close.shift(QDAYS), close.shift(QDAYS).abs())
    cond = (close < 5.0) & (sb_yoy > 0.3) & (close_63d_ret < -0.3)
    out = cond.astype(float)
    return out.where(close.notna() & sb_yoy.notna() & close_63d_ret.notna(), np.nan)


def f48_ddsp_153_listing_tier_risk_indicator(marketcap: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """+1 if marketcap < 50M for 4 consecutive q AND sharesbas yoy > 0.2. 4q via 252d-equivalent rolling (~63d × 4)."""
    if marketcap is None or sharesbas is None:
        return pd.Series(np.nan)
    # 4 consecutive q in daily series ≈ 4 × 63d = 252d. Use rolling max of marketcap over 252d.
    mc_max_4q = marketcap.rolling(YDAYS, min_periods=int(YDAYS * 0.5)).max()
    below_50m = mc_max_4q < 50_000_000
    sb_yoy = _safe_div(sharesbas - sharesbas.shift(YDAYS), sharesbas.shift(YDAYS).abs())
    cond = below_50m & (sb_yoy > 0.2)
    out = cond.astype(float)
    return out.where(mc_max_4q.notna() & sb_yoy.notna(), np.nan)


def f48_ddsp_154_penny_quote_detector(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 if close < 1 AND (close × volume).rolling(21).mean() > 1M (active penny-pump regime)."""
    if close is None or volume is None:
        return pd.Series(np.nan)
    dollar_vol = close * volume
    mean_dv_21d = dollar_vol.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (close < 1.0) & (mean_dv_21d > 1_000_000)
    out = cond.astype(float)
    return out.where(close.notna() & mean_dv_21d.notna(), np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

DILUTION_DEATH_SPIRAL_BASE_REGISTRY_151_225 = {
    "f48_ddsp_151_toxic_convertible_signature_q": {"inputs": ["sharesbas", "debtc"], "func": f48_ddsp_151_toxic_convertible_signature_q},
    "f48_ddsp_152_sub_5_dollar_spiral_indicator": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_152_sub_5_dollar_spiral_indicator},
    "f48_ddsp_153_listing_tier_risk_indicator": {"inputs": ["marketcap", "sharesbas"], "func": f48_ddsp_153_listing_tier_risk_indicator},
    "f48_ddsp_154_penny_quote_detector": {"inputs": ["close", "volume"], "func": f48_ddsp_154_penny_quote_detector},
}
