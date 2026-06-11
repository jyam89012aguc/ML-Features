"""profitability_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for profitability quality detection.
This file carries indices 151-155 (5 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 fundamentals only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


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


def _ttm(s):
    return s.rolling(QQTRS, min_periods=1).sum()


def _avg4(s):
    return s.rolling(QQTRS, min_periods=1).mean()


# ============================================================
#                    FEATURES 151-155
# ============================================================


def f12_psnp_151_pre_sbc_operating_margin_ttm(revenue: pd.Series, opinc: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """(opinc_ttm + sbcomp_ttm) / revenue_ttm — operating margin before stock-based comp dilution."""
    return _safe_div(_ttm(opinc) + _ttm(sbcomp), _ttm(revenue))


def f12_psnp_152_gaap_vs_adjusted_gap_ratio_ttm(netinc: pd.Series, opinc: pd.Series) -> pd.Series:
    """(opinc_ttm − netinc_ttm) / |opinc_ttm| — gap between operating earnings and bottom line."""
    op_ttm = _ttm(opinc)
    ni_ttm = _ttm(netinc)
    return _safe_div(op_ttm - ni_ttm, op_ttm.abs())


def f12_psnp_153_return_on_new_capital_yoy(opinc: pd.Series, assets: pd.Series, debt: pd.Series, equity: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Δ(opinc_ttm × (1-0.25)) over 4q / Δ(invested_capital) over 4q. IC = debt+equity−cashneq."""
    nopat_ttm = _ttm(opinc) * (1.0 - 0.25)
    ic = debt + equity - cashneq
    return _safe_div(nopat_ttm - nopat_ttm.shift(QQTRS), ic - ic.shift(QQTRS))


def f12_psnp_154_normalized_eps_proxy_trend_extrapolated(opinc: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Predicted EPS proxy (opinc_ttm/shareswadil) from 8q OLS trend minus the reported value."""
    eps_proxy = _safe_div(_ttm(opinc), shareswadil)

    def _predict(w):
        valid = ~np.isnan(w)
        if valid.sum() < 4:
            return np.nan
        x = np.arange(len(w), dtype=float)
        xv = x[valid]
        yv = w[valid]
        n = xv.size
        sx = xv.sum()
        sy = yv.sum()
        sxx = (xv * xv).sum()
        sxy = (xv * yv).sum()
        denom = n * sxx - sx * sx
        if denom == 0 or not np.isfinite(denom):
            return np.nan
        slope = (n * sxy - sx * sy) / denom
        intercept = (sy - slope * sx) / n
        # extrapolate to current bar (last index in window)
        return float(intercept + slope * (len(w) - 1))

    predicted = eps_proxy.rolling(QQTRS_2Y, min_periods=4).apply(_predict, raw=True)
    return predicted - eps_proxy


def f12_psnp_155_earnings_accel_then_collapse_flag_8q(netinc: pd.Series) -> pd.Series:
    """+1 if netinc rose ≥4 consecutive q AND most recent q drop > 2× stddev of prior 4q changes."""
    d = netinc.diff()
    # "rose ≥4 consecutive q" — require diffs at lags 2,3,4,5 (prior 4 quarters before the latest) all > 0
    rose4 = (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0)
    # stddev of prior 4q changes (the lagged window) — exclude the current diff
    prior4_std = d.shift(1).rolling(QQTRS, min_periods=3).std()
    most_recent_drop = -d  # positive when drop
    collapse = most_recent_drop > (2.0 * prior4_std)
    flag = (rose4 & collapse).astype(float)
    return flag


# ============================================================
#                    REGISTRY
# ============================================================

PROFITABILITY_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f12_psnp_151_pre_sbc_operating_margin_ttm": {"inputs": ["revenue", "opinc", "sbcomp"], "func": f12_psnp_151_pre_sbc_operating_margin_ttm},
    "f12_psnp_152_gaap_vs_adjusted_gap_ratio_ttm": {"inputs": ["netinc", "opinc"], "func": f12_psnp_152_gaap_vs_adjusted_gap_ratio_ttm},
    "f12_psnp_153_return_on_new_capital_yoy": {"inputs": ["opinc", "assets", "debt", "equity", "cashneq"], "func": f12_psnp_153_return_on_new_capital_yoy},
    "f12_psnp_154_normalized_eps_proxy_trend_extrapolated": {"inputs": ["opinc", "shareswadil"], "func": f12_psnp_154_normalized_eps_proxy_trend_extrapolated},
    "f12_psnp_155_earnings_accel_then_collapse_flag_8q": {"inputs": ["netinc"], "func": f12_psnp_155_earnings_accel_then_collapse_flag_8q},
}
