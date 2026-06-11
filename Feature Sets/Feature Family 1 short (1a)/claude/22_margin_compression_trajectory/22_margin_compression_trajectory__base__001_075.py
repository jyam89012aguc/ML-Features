"""margin_compression_trajectory base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about margin compression (continued in __base__076_150.py for 150 total).
Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no forward-looking shifts. Functions consume named pandas Series whose
index is the family-agnostic time index supplied by the harness.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _consec_decline_streak(s):
    decl = (s < s.shift(1)).astype(float)
    grp = (decl == 0).cumsum()
    return decl.groupby(grp).cumsum()


def _sign_flip_count(s, n):
    sgn = np.sign(s.diff())
    flip = (sgn * sgn.shift(1) < 0).astype(float)
    return flip.rolling(n, min_periods=max(n // 3, 2)).sum()


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: Margin levels (001-020) ----

def f22_mctj_001_gm_q(revenue, gp):
    return _safe_div(gp, revenue)


def f22_mctj_002_om_q(revenue, opinc):
    return _safe_div(opinc, revenue)


def f22_mctj_003_ebitdam_q(revenue, ebitda):
    return _safe_div(ebitda, revenue)


def f22_mctj_004_nm_q(revenue, netinc):
    return _safe_div(netinc, revenue)


def f22_mctj_005_cogs_to_rev_q(revenue, cogs):
    return _safe_div(cogs, revenue)


def f22_mctj_006_sgna_to_rev_q(revenue, sgna):
    return _safe_div(sgna, revenue)


def f22_mctj_007_opex_to_rev_q(revenue, opex):
    return _safe_div(opex, revenue)


def f22_mctj_008_gm_ttm(revenue, gp):
    return _safe_div(_ttm(gp), _ttm(revenue))


def f22_mctj_009_om_ttm(revenue, opinc):
    return _safe_div(_ttm(opinc), _ttm(revenue))


def f22_mctj_010_ebitdam_ttm(revenue, ebitda):
    return _safe_div(_ttm(ebitda), _ttm(revenue))


def f22_mctj_011_nm_ttm(revenue, netinc):
    return _safe_div(_ttm(netinc), _ttm(revenue))


def f22_mctj_012_gm_minus_om(revenue, gp, opinc):
    return _safe_div(gp, revenue) - _safe_div(opinc, revenue)


def f22_mctj_013_gm_minus_ebitdam(revenue, gp, ebitda):
    return _safe_div(gp, revenue) - _safe_div(ebitda, revenue)


def f22_mctj_014_om_minus_nm(revenue, opinc, netinc):
    return _safe_div(opinc, revenue) - _safe_div(netinc, revenue)


def f22_mctj_015_gm_minus_nm(revenue, gp, netinc):
    return _safe_div(gp, revenue) - _safe_div(netinc, revenue)


def f22_mctj_016_margin_stack_score(revenue, gp, opinc, ebitda, netinc):
    return (_safe_div(gp, revenue) + _safe_div(opinc, revenue)
            + _safe_div(ebitda, revenue) + _safe_div(netinc, revenue))


def f22_mctj_017_margin_quartile_dispersion(revenue, gp, opinc, ebitda, netinc):
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    em = _safe_div(ebitda, revenue)
    nm = _safe_div(netinc, revenue)
    return (gm - om) + (om - em) + (em - nm)


def f22_mctj_018_gm_to_om_ratio(revenue, gp, opinc):
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    return _safe_div(om, gm)


def f22_mctj_019_om_to_nm_ratio(revenue, opinc, netinc):
    om = _safe_div(opinc, revenue)
    nm = _safe_div(netinc, revenue)
    return _safe_div(nm, om)


def f22_mctj_020_ebitdam_to_nm_ratio(revenue, ebitda, netinc):
    em = _safe_div(ebitda, revenue)
    nm = _safe_div(netinc, revenue)
    return _safe_div(nm, em)


# ---- Block B: Margin QoQ/YoY changes (021-045) ----

def f22_mctj_021_gm_qoq_change(revenue, gp):
    return _safe_div(gp, revenue).diff()


def f22_mctj_022_om_qoq_change(revenue, opinc):
    return _safe_div(opinc, revenue).diff()


def f22_mctj_023_ebitdam_qoq_change(revenue, ebitda):
    return _safe_div(ebitda, revenue).diff()


def f22_mctj_024_nm_qoq_change(revenue, netinc):
    return _safe_div(netinc, revenue).diff()


def f22_mctj_025_gm_yoy_change(revenue, gp):
    s = _safe_div(gp, revenue)
    return s - s.shift(4)


def f22_mctj_026_om_yoy_change(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s - s.shift(4)


def f22_mctj_027_ebitdam_yoy_change(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s - s.shift(4)


def f22_mctj_028_nm_yoy_change(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s - s.shift(4)


def f22_mctj_029_gm_2y_change(revenue, gp):
    s = _safe_div(gp, revenue)
    return s - s.shift(8)


def f22_mctj_030_om_2y_change(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s - s.shift(8)


def f22_mctj_031_ebitdam_2y_change(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s - s.shift(8)


def f22_mctj_032_nm_2y_change(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s - s.shift(8)


def f22_mctj_033_cogs_to_rev_qoq_change(revenue, cogs):
    return _safe_div(cogs, revenue).diff()


def f22_mctj_034_cogs_to_rev_yoy_change(revenue, cogs):
    s = _safe_div(cogs, revenue)
    return s - s.shift(4)


def f22_mctj_035_sgna_to_rev_qoq_change(revenue, sgna):
    return _safe_div(sgna, revenue).diff()


def f22_mctj_036_sgna_to_rev_yoy_change(revenue, sgna):
    s = _safe_div(sgna, revenue)
    return s - s.shift(4)


def f22_mctj_037_opex_to_rev_yoy_change(revenue, opex):
    s = _safe_div(opex, revenue)
    return s - s.shift(4)


def f22_mctj_038_gm_ttm_yoy_change(revenue, gp):
    s = _safe_div(_ttm(gp), _ttm(revenue))
    return s - s.shift(4)


def f22_mctj_039_om_ttm_yoy_change(revenue, opinc):
    s = _safe_div(_ttm(opinc), _ttm(revenue))
    return s - s.shift(4)


def f22_mctj_040_ebitdam_ttm_yoy_change(revenue, ebitda):
    s = _safe_div(_ttm(ebitda), _ttm(revenue))
    return s - s.shift(4)


def f22_mctj_041_nm_ttm_yoy_change(revenue, netinc):
    s = _safe_div(_ttm(netinc), _ttm(revenue))
    return s - s.shift(4)


def f22_mctj_042_gm_ttm_2y_change(revenue, gp):
    s = _safe_div(_ttm(gp), _ttm(revenue))
    return s - s.shift(8)


def f22_mctj_043_om_ttm_2y_change(revenue, opinc):
    s = _safe_div(_ttm(opinc), _ttm(revenue))
    return s - s.shift(8)


def f22_mctj_044_ebitdam_ttm_2y_change(revenue, ebitda):
    s = _safe_div(_ttm(ebitda), _ttm(revenue))
    return s - s.shift(8)


def f22_mctj_045_nm_ttm_2y_change(revenue, netinc):
    s = _safe_div(_ttm(netinc), _ttm(revenue))
    return s - s.shift(8)


# ---- Block C: Margin slopes (046-065) ----

def f22_mctj_046_gm_4q_slope(revenue, gp):
    return _rolling_slope(_safe_div(gp, revenue), 4, min_periods=2)


def f22_mctj_047_gm_8q_slope(revenue, gp):
    return _rolling_slope(_safe_div(gp, revenue), 8, min_periods=3)


def f22_mctj_048_gm_12q_slope(revenue, gp):
    return _rolling_slope(_safe_div(gp, revenue), 12, min_periods=4)


def f22_mctj_049_om_4q_slope(revenue, opinc):
    return _rolling_slope(_safe_div(opinc, revenue), 4, min_periods=2)


def f22_mctj_050_om_8q_slope(revenue, opinc):
    return _rolling_slope(_safe_div(opinc, revenue), 8, min_periods=3)


def f22_mctj_051_om_12q_slope(revenue, opinc):
    return _rolling_slope(_safe_div(opinc, revenue), 12, min_periods=4)


def f22_mctj_052_ebitdam_4q_slope(revenue, ebitda):
    return _rolling_slope(_safe_div(ebitda, revenue), 4, min_periods=2)


def f22_mctj_053_ebitdam_8q_slope(revenue, ebitda):
    return _rolling_slope(_safe_div(ebitda, revenue), 8, min_periods=3)


def f22_mctj_054_ebitdam_12q_slope(revenue, ebitda):
    return _rolling_slope(_safe_div(ebitda, revenue), 12, min_periods=4)


def f22_mctj_055_nm_4q_slope(revenue, netinc):
    return _rolling_slope(_safe_div(netinc, revenue), 4, min_periods=2)


def f22_mctj_056_nm_8q_slope(revenue, netinc):
    return _rolling_slope(_safe_div(netinc, revenue), 8, min_periods=3)


def f22_mctj_057_nm_12q_slope(revenue, netinc):
    return _rolling_slope(_safe_div(netinc, revenue), 12, min_periods=4)


def f22_mctj_058_gm_4q_minus_8q_slope_diff(revenue, gp):
    s = _safe_div(gp, revenue)
    return _rolling_slope(s, 4, min_periods=2) - _rolling_slope(s, 8, min_periods=3)


def f22_mctj_059_om_4q_minus_8q_slope_diff(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return _rolling_slope(s, 4, min_periods=2) - _rolling_slope(s, 8, min_periods=3)


def f22_mctj_060_ebitdam_4q_minus_8q_slope_diff(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return _rolling_slope(s, 4, min_periods=2) - _rolling_slope(s, 8, min_periods=3)


def f22_mctj_061_nm_4q_minus_8q_slope_diff(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return _rolling_slope(s, 4, min_periods=2) - _rolling_slope(s, 8, min_periods=3)


def f22_mctj_062_gm_ttm_8q_slope(revenue, gp):
    return _rolling_slope(_safe_div(_ttm(gp), _ttm(revenue)), 8, min_periods=3)


def f22_mctj_063_om_ttm_8q_slope(revenue, opinc):
    return _rolling_slope(_safe_div(_ttm(opinc), _ttm(revenue)), 8, min_periods=3)


def f22_mctj_064_ebitdam_ttm_8q_slope(revenue, ebitda):
    return _rolling_slope(_safe_div(_ttm(ebitda), _ttm(revenue)), 8, min_periods=3)


def f22_mctj_065_nm_ttm_8q_slope(revenue, netinc):
    return _rolling_slope(_safe_div(_ttm(netinc), _ttm(revenue)), 8, min_periods=3)


# ---- Block D-partial: Margin trajectories/extremes (066-075) ----

def f22_mctj_066_gm_drawdown_from_8q_max(revenue, gp):
    s = _safe_div(gp, revenue)
    return s - s.rolling(8, min_periods=3).max()


def f22_mctj_067_gm_drawdown_from_12q_max(revenue, gp):
    s = _safe_div(gp, revenue)
    return s - s.rolling(12, min_periods=4).max()


def f22_mctj_068_om_drawdown_from_8q_max(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s - s.rolling(8, min_periods=3).max()


def f22_mctj_069_om_drawdown_from_12q_max(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s - s.rolling(12, min_periods=4).max()


def f22_mctj_070_ebitdam_drawdown_from_8q_max(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s - s.rolling(8, min_periods=3).max()


def f22_mctj_071_nm_drawdown_from_8q_max(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s - s.rolling(8, min_periods=3).max()


def f22_mctj_072_gm_recovery_from_8q_min(revenue, gp):
    s = _safe_div(gp, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_073_om_recovery_from_8q_min(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_074_ebitdam_recovery_from_8q_min(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_075_nm_recovery_from_8q_min(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s - s.rolling(8, min_periods=3).min()


# ============================================================
#                        REGISTRY
# ============================================================

MARGIN_COMPRESSION_TRAJECTORY_BASE_REGISTRY_001_075 = {
    "f22_mctj_001_gm_q": {"inputs": ["revenue", "gp"], "func": f22_mctj_001_gm_q},
    "f22_mctj_002_om_q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_002_om_q},
    "f22_mctj_003_ebitdam_q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_003_ebitdam_q},
    "f22_mctj_004_nm_q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_004_nm_q},
    "f22_mctj_005_cogs_to_rev_q": {"inputs": ["revenue", "cogs"], "func": f22_mctj_005_cogs_to_rev_q},
    "f22_mctj_006_sgna_to_rev_q": {"inputs": ["revenue", "sgna"], "func": f22_mctj_006_sgna_to_rev_q},
    "f22_mctj_007_opex_to_rev_q": {"inputs": ["revenue", "opex"], "func": f22_mctj_007_opex_to_rev_q},
    "f22_mctj_008_gm_ttm": {"inputs": ["revenue", "gp"], "func": f22_mctj_008_gm_ttm},
    "f22_mctj_009_om_ttm": {"inputs": ["revenue", "opinc"], "func": f22_mctj_009_om_ttm},
    "f22_mctj_010_ebitdam_ttm": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_010_ebitdam_ttm},
    "f22_mctj_011_nm_ttm": {"inputs": ["revenue", "netinc"], "func": f22_mctj_011_nm_ttm},
    "f22_mctj_012_gm_minus_om": {"inputs": ["revenue", "gp", "opinc"], "func": f22_mctj_012_gm_minus_om},
    "f22_mctj_013_gm_minus_ebitdam": {"inputs": ["revenue", "gp", "ebitda"], "func": f22_mctj_013_gm_minus_ebitdam},
    "f22_mctj_014_om_minus_nm": {"inputs": ["revenue", "opinc", "netinc"], "func": f22_mctj_014_om_minus_nm},
    "f22_mctj_015_gm_minus_nm": {"inputs": ["revenue", "gp", "netinc"], "func": f22_mctj_015_gm_minus_nm},
    "f22_mctj_016_margin_stack_score": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_016_margin_stack_score},
    "f22_mctj_017_margin_quartile_dispersion": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_017_margin_quartile_dispersion},
    "f22_mctj_018_gm_to_om_ratio": {"inputs": ["revenue", "gp", "opinc"], "func": f22_mctj_018_gm_to_om_ratio},
    "f22_mctj_019_om_to_nm_ratio": {"inputs": ["revenue", "opinc", "netinc"], "func": f22_mctj_019_om_to_nm_ratio},
    "f22_mctj_020_ebitdam_to_nm_ratio": {"inputs": ["revenue", "ebitda", "netinc"], "func": f22_mctj_020_ebitdam_to_nm_ratio},
    "f22_mctj_021_gm_qoq_change": {"inputs": ["revenue", "gp"], "func": f22_mctj_021_gm_qoq_change},
    "f22_mctj_022_om_qoq_change": {"inputs": ["revenue", "opinc"], "func": f22_mctj_022_om_qoq_change},
    "f22_mctj_023_ebitdam_qoq_change": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_023_ebitdam_qoq_change},
    "f22_mctj_024_nm_qoq_change": {"inputs": ["revenue", "netinc"], "func": f22_mctj_024_nm_qoq_change},
    "f22_mctj_025_gm_yoy_change": {"inputs": ["revenue", "gp"], "func": f22_mctj_025_gm_yoy_change},
    "f22_mctj_026_om_yoy_change": {"inputs": ["revenue", "opinc"], "func": f22_mctj_026_om_yoy_change},
    "f22_mctj_027_ebitdam_yoy_change": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_027_ebitdam_yoy_change},
    "f22_mctj_028_nm_yoy_change": {"inputs": ["revenue", "netinc"], "func": f22_mctj_028_nm_yoy_change},
    "f22_mctj_029_gm_2y_change": {"inputs": ["revenue", "gp"], "func": f22_mctj_029_gm_2y_change},
    "f22_mctj_030_om_2y_change": {"inputs": ["revenue", "opinc"], "func": f22_mctj_030_om_2y_change},
    "f22_mctj_031_ebitdam_2y_change": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_031_ebitdam_2y_change},
    "f22_mctj_032_nm_2y_change": {"inputs": ["revenue", "netinc"], "func": f22_mctj_032_nm_2y_change},
    "f22_mctj_033_cogs_to_rev_qoq_change": {"inputs": ["revenue", "cogs"], "func": f22_mctj_033_cogs_to_rev_qoq_change},
    "f22_mctj_034_cogs_to_rev_yoy_change": {"inputs": ["revenue", "cogs"], "func": f22_mctj_034_cogs_to_rev_yoy_change},
    "f22_mctj_035_sgna_to_rev_qoq_change": {"inputs": ["revenue", "sgna"], "func": f22_mctj_035_sgna_to_rev_qoq_change},
    "f22_mctj_036_sgna_to_rev_yoy_change": {"inputs": ["revenue", "sgna"], "func": f22_mctj_036_sgna_to_rev_yoy_change},
    "f22_mctj_037_opex_to_rev_yoy_change": {"inputs": ["revenue", "opex"], "func": f22_mctj_037_opex_to_rev_yoy_change},
    "f22_mctj_038_gm_ttm_yoy_change": {"inputs": ["revenue", "gp"], "func": f22_mctj_038_gm_ttm_yoy_change},
    "f22_mctj_039_om_ttm_yoy_change": {"inputs": ["revenue", "opinc"], "func": f22_mctj_039_om_ttm_yoy_change},
    "f22_mctj_040_ebitdam_ttm_yoy_change": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_040_ebitdam_ttm_yoy_change},
    "f22_mctj_041_nm_ttm_yoy_change": {"inputs": ["revenue", "netinc"], "func": f22_mctj_041_nm_ttm_yoy_change},
    "f22_mctj_042_gm_ttm_2y_change": {"inputs": ["revenue", "gp"], "func": f22_mctj_042_gm_ttm_2y_change},
    "f22_mctj_043_om_ttm_2y_change": {"inputs": ["revenue", "opinc"], "func": f22_mctj_043_om_ttm_2y_change},
    "f22_mctj_044_ebitdam_ttm_2y_change": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_044_ebitdam_ttm_2y_change},
    "f22_mctj_045_nm_ttm_2y_change": {"inputs": ["revenue", "netinc"], "func": f22_mctj_045_nm_ttm_2y_change},
    "f22_mctj_046_gm_4q_slope": {"inputs": ["revenue", "gp"], "func": f22_mctj_046_gm_4q_slope},
    "f22_mctj_047_gm_8q_slope": {"inputs": ["revenue", "gp"], "func": f22_mctj_047_gm_8q_slope},
    "f22_mctj_048_gm_12q_slope": {"inputs": ["revenue", "gp"], "func": f22_mctj_048_gm_12q_slope},
    "f22_mctj_049_om_4q_slope": {"inputs": ["revenue", "opinc"], "func": f22_mctj_049_om_4q_slope},
    "f22_mctj_050_om_8q_slope": {"inputs": ["revenue", "opinc"], "func": f22_mctj_050_om_8q_slope},
    "f22_mctj_051_om_12q_slope": {"inputs": ["revenue", "opinc"], "func": f22_mctj_051_om_12q_slope},
    "f22_mctj_052_ebitdam_4q_slope": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_052_ebitdam_4q_slope},
    "f22_mctj_053_ebitdam_8q_slope": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_053_ebitdam_8q_slope},
    "f22_mctj_054_ebitdam_12q_slope": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_054_ebitdam_12q_slope},
    "f22_mctj_055_nm_4q_slope": {"inputs": ["revenue", "netinc"], "func": f22_mctj_055_nm_4q_slope},
    "f22_mctj_056_nm_8q_slope": {"inputs": ["revenue", "netinc"], "func": f22_mctj_056_nm_8q_slope},
    "f22_mctj_057_nm_12q_slope": {"inputs": ["revenue", "netinc"], "func": f22_mctj_057_nm_12q_slope},
    "f22_mctj_058_gm_4q_minus_8q_slope_diff": {"inputs": ["revenue", "gp"], "func": f22_mctj_058_gm_4q_minus_8q_slope_diff},
    "f22_mctj_059_om_4q_minus_8q_slope_diff": {"inputs": ["revenue", "opinc"], "func": f22_mctj_059_om_4q_minus_8q_slope_diff},
    "f22_mctj_060_ebitdam_4q_minus_8q_slope_diff": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_060_ebitdam_4q_minus_8q_slope_diff},
    "f22_mctj_061_nm_4q_minus_8q_slope_diff": {"inputs": ["revenue", "netinc"], "func": f22_mctj_061_nm_4q_minus_8q_slope_diff},
    "f22_mctj_062_gm_ttm_8q_slope": {"inputs": ["revenue", "gp"], "func": f22_mctj_062_gm_ttm_8q_slope},
    "f22_mctj_063_om_ttm_8q_slope": {"inputs": ["revenue", "opinc"], "func": f22_mctj_063_om_ttm_8q_slope},
    "f22_mctj_064_ebitdam_ttm_8q_slope": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_064_ebitdam_ttm_8q_slope},
    "f22_mctj_065_nm_ttm_8q_slope": {"inputs": ["revenue", "netinc"], "func": f22_mctj_065_nm_ttm_8q_slope},
    "f22_mctj_066_gm_drawdown_from_8q_max": {"inputs": ["revenue", "gp"], "func": f22_mctj_066_gm_drawdown_from_8q_max},
    "f22_mctj_067_gm_drawdown_from_12q_max": {"inputs": ["revenue", "gp"], "func": f22_mctj_067_gm_drawdown_from_12q_max},
    "f22_mctj_068_om_drawdown_from_8q_max": {"inputs": ["revenue", "opinc"], "func": f22_mctj_068_om_drawdown_from_8q_max},
    "f22_mctj_069_om_drawdown_from_12q_max": {"inputs": ["revenue", "opinc"], "func": f22_mctj_069_om_drawdown_from_12q_max},
    "f22_mctj_070_ebitdam_drawdown_from_8q_max": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_070_ebitdam_drawdown_from_8q_max},
    "f22_mctj_071_nm_drawdown_from_8q_max": {"inputs": ["revenue", "netinc"], "func": f22_mctj_071_nm_drawdown_from_8q_max},
    "f22_mctj_072_gm_recovery_from_8q_min": {"inputs": ["revenue", "gp"], "func": f22_mctj_072_gm_recovery_from_8q_min},
    "f22_mctj_073_om_recovery_from_8q_min": {"inputs": ["revenue", "opinc"], "func": f22_mctj_073_om_recovery_from_8q_min},
    "f22_mctj_074_ebitdam_recovery_from_8q_min": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_074_ebitdam_recovery_from_8q_min},
    "f22_mctj_075_nm_recovery_from_8q_min": {"inputs": ["revenue", "netinc"], "func": f22_mctj_075_nm_recovery_from_8q_min},
}
