"""margin_compression_trajectory base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py with 75 additional hypotheses (decline streaks, cost
intensity, volatility, and inflection composites). PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no forward-looking shifts.
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


def _consec_true_streak(b):
    bf = b.fillna(False).astype(float)
    grp = (bf == 0).cumsum()
    return bf.groupby(grp).cumsum()


def _sign_flip_count(s, n):
    sgn = np.sign(s.diff())
    flip = (sgn * sgn.shift(1) < 0).astype(float)
    return flip.rolling(n, min_periods=max(n // 3, 2)).sum()


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block D (continued): decline streaks, min/max spreads, below-mean counts (076-090) ----

def f22_mctj_076_gm_consec_decline_streak(revenue, gp):
    return _consec_decline_streak(_safe_div(gp, revenue))


def f22_mctj_077_om_consec_decline_streak(revenue, opinc):
    return _consec_decline_streak(_safe_div(opinc, revenue))


def f22_mctj_078_ebitdam_consec_decline_streak(revenue, ebitda):
    return _consec_decline_streak(_safe_div(ebitda, revenue))


def f22_mctj_079_nm_consec_decline_streak(revenue, netinc):
    return _consec_decline_streak(_safe_div(netinc, revenue))


def f22_mctj_080_gm_4q_min_minus_max(revenue, gp):
    s = _safe_div(gp, revenue)
    return s.rolling(4, min_periods=2).min() - s.rolling(4, min_periods=2).max()


def f22_mctj_081_om_4q_min_minus_max(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s.rolling(4, min_periods=2).min() - s.rolling(4, min_periods=2).max()


def f22_mctj_082_gm_8q_min_minus_max(revenue, gp):
    s = _safe_div(gp, revenue)
    return s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()


def f22_mctj_083_om_8q_min_minus_max(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()


def f22_mctj_084_ebitdam_8q_min_minus_max(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()


def f22_mctj_085_nm_8q_min_minus_max(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()


def f22_mctj_086_gm_below_8q_mean_count_8q(revenue, gp):
    s = _safe_div(gp, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return (s < m).astype(float).rolling(8, min_periods=3).sum()


def f22_mctj_087_om_below_8q_mean_count_8q(revenue, opinc):
    s = _safe_div(opinc, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return (s < m).astype(float).rolling(8, min_periods=3).sum()


def f22_mctj_088_ebitdam_below_8q_mean_count_8q(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return (s < m).astype(float).rolling(8, min_periods=3).sum()


def f22_mctj_089_nm_below_8q_mean_count_8q(revenue, netinc):
    s = _safe_div(netinc, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return (s < m).astype(float).rolling(8, min_periods=3).sum()


def f22_mctj_090_gm_below_neg_count_8q(revenue, gp):
    s = _safe_div(gp, revenue)
    return (s < 0).astype(float).rolling(8, min_periods=3).sum()


# ---- Block E: cost-side intensity (091-115) ----

def f22_mctj_091_cogs_to_rev_4q_slope(revenue, cogs):
    return _rolling_slope(_safe_div(cogs, revenue), 4, min_periods=2)


def f22_mctj_092_cogs_to_rev_8q_slope(revenue, cogs):
    return _rolling_slope(_safe_div(cogs, revenue), 8, min_periods=3)


def f22_mctj_093_cogs_to_rev_drawup_from_8q_min(revenue, cogs):
    s = _safe_div(cogs, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_094_cogs_to_rev_zscore_8q(revenue, cogs):
    return _rolling_zscore(_safe_div(cogs, revenue), 8, min_periods=3)


def f22_mctj_095_opex_to_rev_4q_slope(revenue, opex):
    return _rolling_slope(_safe_div(opex, revenue), 4, min_periods=2)


def f22_mctj_096_opex_to_rev_8q_slope(revenue, opex):
    return _rolling_slope(_safe_div(opex, revenue), 8, min_periods=3)


def f22_mctj_097_opex_to_rev_drawup_from_8q_min(revenue, opex):
    s = _safe_div(opex, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_098_opex_to_rev_zscore_8q(revenue, opex):
    return _rolling_zscore(_safe_div(opex, revenue), 8, min_periods=3)


def f22_mctj_099_sgna_to_rev_4q_slope(revenue, sgna):
    return _rolling_slope(_safe_div(sgna, revenue), 4, min_periods=2)


def f22_mctj_100_sgna_to_rev_8q_slope(revenue, sgna):
    return _rolling_slope(_safe_div(sgna, revenue), 8, min_periods=3)


def f22_mctj_101_sgna_to_rev_drawup_from_8q_min(revenue, sgna):
    s = _safe_div(sgna, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_102_sgna_to_rev_zscore_8q(revenue, sgna):
    return _rolling_zscore(_safe_div(sgna, revenue), 8, min_periods=3)


def f22_mctj_103_cost_intensity_composite(revenue, cogs, opex, sgna):
    return (_safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue))


def f22_mctj_104_cost_intensity_composite_qoq_change(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return s.diff()


def f22_mctj_105_cost_intensity_composite_8q_slope(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return _rolling_slope(s, 8, min_periods=3)


def f22_mctj_106_cost_intensity_composite_drawup_from_8q_min(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return s - s.rolling(8, min_periods=3).min()


def f22_mctj_107_cost_intensity_composite_zscore_8q(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return _rolling_zscore(s, 8, min_periods=3)


def f22_mctj_108_cogs_growth_minus_rev_growth_yoy(revenue, cogs):
    return _yoy_pct(cogs) - _yoy_pct(revenue)


def f22_mctj_109_opex_growth_minus_rev_growth_yoy(revenue, opex):
    return _yoy_pct(opex) - _yoy_pct(revenue)


def f22_mctj_110_sgna_growth_minus_rev_growth_yoy(revenue, sgna):
    return _yoy_pct(sgna) - _yoy_pct(revenue)


def f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct(revenue, cogs):
    return _qoq_pct(cogs) - _qoq_pct(revenue)


def f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct(revenue, opex):
    return _qoq_pct(opex) - _qoq_pct(revenue)


def f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct(revenue, sgna):
    return _qoq_pct(sgna) - _qoq_pct(revenue)


def f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q(revenue, cogs):
    s = _safe_div(cogs, revenue)
    return _rolling_zscore(s - s.shift(4), 8, min_periods=3)


def f22_mctj_115_opex_to_rev_yoy_change_zscore_8q(revenue, opex):
    s = _safe_div(opex, revenue)
    return _rolling_zscore(s - s.shift(4), 8, min_periods=3)


# ---- Block F: Margin volatility / quality (116-130) ----

def f22_mctj_116_gm_std_8q(revenue, gp):
    return _safe_div(gp, revenue).rolling(8, min_periods=3).std()


def f22_mctj_117_om_std_8q(revenue, opinc):
    return _safe_div(opinc, revenue).rolling(8, min_periods=3).std()


def f22_mctj_118_ebitdam_std_8q(revenue, ebitda):
    return _safe_div(ebitda, revenue).rolling(8, min_periods=3).std()


def f22_mctj_119_nm_std_8q(revenue, netinc):
    return _safe_div(netinc, revenue).rolling(8, min_periods=3).std()


def f22_mctj_120_gm_std_12q(revenue, gp):
    return _safe_div(gp, revenue).rolling(12, min_periods=4).std()


def f22_mctj_121_om_std_12q(revenue, opinc):
    return _safe_div(opinc, revenue).rolling(12, min_periods=4).std()


def f22_mctj_122_gm_qoq_change_std_8q(revenue, gp):
    return _safe_div(gp, revenue).diff().rolling(8, min_periods=3).std()


def f22_mctj_123_om_qoq_change_std_8q(revenue, opinc):
    return _safe_div(opinc, revenue).diff().rolling(8, min_periods=3).std()


def f22_mctj_124_ebitdam_qoq_change_std_8q(revenue, ebitda):
    return _safe_div(ebitda, revenue).diff().rolling(8, min_periods=3).std()


def f22_mctj_125_nm_qoq_change_std_8q(revenue, netinc):
    return _safe_div(netinc, revenue).diff().rolling(8, min_periods=3).std()


def f22_mctj_126_gm_abs_change_mean_8q(revenue, gp):
    return _safe_div(gp, revenue).diff().abs().rolling(8, min_periods=3).mean()


def f22_mctj_127_om_abs_change_mean_8q(revenue, opinc):
    return _safe_div(opinc, revenue).diff().abs().rolling(8, min_periods=3).mean()


def f22_mctj_128_gm_sign_flip_count_8q(revenue, gp):
    return _sign_flip_count(_safe_div(gp, revenue), 8)


def f22_mctj_129_om_sign_flip_count_8q(revenue, opinc):
    return _sign_flip_count(_safe_div(opinc, revenue), 8)


def f22_mctj_130_ebitdam_sign_flip_count_8q(revenue, ebitda):
    return _sign_flip_count(_safe_div(ebitda, revenue), 8)


# ---- Block G: Inflection / breakpoint composites (131-150) ----

def f22_mctj_131_gm_inflection_neg_4q(revenue, gp):
    slp = _rolling_slope(_safe_div(gp, revenue), 4, min_periods=2)
    return ((slp.shift(4) > 0) & (slp < 0)).astype(float)


def f22_mctj_132_om_inflection_neg_4q(revenue, opinc):
    slp = _rolling_slope(_safe_div(opinc, revenue), 4, min_periods=2)
    return ((slp.shift(4) > 0) & (slp < 0)).astype(float)


def f22_mctj_133_ebitdam_inflection_neg_4q(revenue, ebitda):
    slp = _rolling_slope(_safe_div(ebitda, revenue), 4, min_periods=2)
    return ((slp.shift(4) > 0) & (slp < 0)).astype(float)


def f22_mctj_134_nm_inflection_neg_4q(revenue, netinc):
    slp = _rolling_slope(_safe_div(netinc, revenue), 4, min_periods=2)
    return ((slp.shift(4) > 0) & (slp < 0)).astype(float)


def f22_mctj_135_gm_step_down_size_8q(revenue, gp):
    return _safe_div(gp, revenue).diff().rolling(8, min_periods=3).min()


def f22_mctj_136_om_step_down_size_8q(revenue, opinc):
    return _safe_div(opinc, revenue).diff().rolling(8, min_periods=3).min()


def f22_mctj_137_ebitdam_step_down_size_8q(revenue, ebitda):
    return _safe_div(ebitda, revenue).diff().rolling(8, min_periods=3).min()


def f22_mctj_138_nm_step_down_size_8q(revenue, netinc):
    return _safe_div(netinc, revenue).diff().rolling(8, min_periods=3).min()


def f22_mctj_139_gm_cliff_indicator(revenue, gp):
    s = _safe_div(gp, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return (ch < (-2.0 * sd)).astype(float)


def f22_mctj_140_om_cliff_indicator(revenue, opinc):
    s = _safe_div(opinc, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return (ch < (-2.0 * sd)).astype(float)


def f22_mctj_141_ebitdam_cliff_indicator(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return (ch < (-2.0 * sd)).astype(float)


def f22_mctj_142_nm_cliff_indicator(revenue, netinc):
    s = _safe_div(netinc, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return (ch < (-2.0 * sd)).astype(float)


def f22_mctj_143_gm_chow_proxy_8q(revenue, gp):
    s = _safe_div(gp, revenue)
    return s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()


def f22_mctj_144_om_chow_proxy_8q(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()


def f22_mctj_145_ebitdam_chow_proxy_8q(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()


def f22_mctj_146_nm_chow_proxy_8q(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()


def f22_mctj_147_margin_full_stack_compression_count_8q(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    flag = ((gm_d < 0) & (om_d < 0) & (em_d < 0) & (nm_d < 0)).astype(float)
    return flag.rolling(8, min_periods=3).sum()


def f22_mctj_148_margin_compression_breadth(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    return ((gm_d < 0).astype(float) + (om_d < 0).astype(float)
            + (em_d < 0).astype(float) + (nm_d < 0).astype(float))


def f22_mctj_149_margin_compression_persistence(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    breadth = ((gm_d < 0).astype(float) + (om_d < 0).astype(float)
               + (em_d < 0).astype(float) + (nm_d < 0).astype(float))
    full = (breadth == 4).astype(float)
    grp = (full == 0).cumsum()
    return full.groupby(grp).cumsum()


def f22_mctj_150_margin_terminal_signal(revenue, gp, opinc, ebitda, netinc):
    gm_s = _rolling_slope(_safe_div(gp, revenue), 8, min_periods=3)
    om_s = _rolling_slope(_safe_div(opinc, revenue), 8, min_periods=3)
    em_s = _rolling_slope(_safe_div(ebitda, revenue), 8, min_periods=3)
    nm_s = _rolling_slope(_safe_div(netinc, revenue), 8, min_periods=3)
    return ((gm_s < 0) & (om_s < 0) & (em_s < 0) & (nm_s < 0)).astype(float)


# ============================================================
#                        REGISTRY
# ============================================================

MARGIN_COMPRESSION_TRAJECTORY_BASE_REGISTRY_076_150 = {
    "f22_mctj_076_gm_consec_decline_streak": {"inputs": ["revenue", "gp"], "func": f22_mctj_076_gm_consec_decline_streak},
    "f22_mctj_077_om_consec_decline_streak": {"inputs": ["revenue", "opinc"], "func": f22_mctj_077_om_consec_decline_streak},
    "f22_mctj_078_ebitdam_consec_decline_streak": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_078_ebitdam_consec_decline_streak},
    "f22_mctj_079_nm_consec_decline_streak": {"inputs": ["revenue", "netinc"], "func": f22_mctj_079_nm_consec_decline_streak},
    "f22_mctj_080_gm_4q_min_minus_max": {"inputs": ["revenue", "gp"], "func": f22_mctj_080_gm_4q_min_minus_max},
    "f22_mctj_081_om_4q_min_minus_max": {"inputs": ["revenue", "opinc"], "func": f22_mctj_081_om_4q_min_minus_max},
    "f22_mctj_082_gm_8q_min_minus_max": {"inputs": ["revenue", "gp"], "func": f22_mctj_082_gm_8q_min_minus_max},
    "f22_mctj_083_om_8q_min_minus_max": {"inputs": ["revenue", "opinc"], "func": f22_mctj_083_om_8q_min_minus_max},
    "f22_mctj_084_ebitdam_8q_min_minus_max": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_084_ebitdam_8q_min_minus_max},
    "f22_mctj_085_nm_8q_min_minus_max": {"inputs": ["revenue", "netinc"], "func": f22_mctj_085_nm_8q_min_minus_max},
    "f22_mctj_086_gm_below_8q_mean_count_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_086_gm_below_8q_mean_count_8q},
    "f22_mctj_087_om_below_8q_mean_count_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_087_om_below_8q_mean_count_8q},
    "f22_mctj_088_ebitdam_below_8q_mean_count_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_088_ebitdam_below_8q_mean_count_8q},
    "f22_mctj_089_nm_below_8q_mean_count_8q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_089_nm_below_8q_mean_count_8q},
    "f22_mctj_090_gm_below_neg_count_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_090_gm_below_neg_count_8q},
    "f22_mctj_091_cogs_to_rev_4q_slope": {"inputs": ["revenue", "cogs"], "func": f22_mctj_091_cogs_to_rev_4q_slope},
    "f22_mctj_092_cogs_to_rev_8q_slope": {"inputs": ["revenue", "cogs"], "func": f22_mctj_092_cogs_to_rev_8q_slope},
    "f22_mctj_093_cogs_to_rev_drawup_from_8q_min": {"inputs": ["revenue", "cogs"], "func": f22_mctj_093_cogs_to_rev_drawup_from_8q_min},
    "f22_mctj_094_cogs_to_rev_zscore_8q": {"inputs": ["revenue", "cogs"], "func": f22_mctj_094_cogs_to_rev_zscore_8q},
    "f22_mctj_095_opex_to_rev_4q_slope": {"inputs": ["revenue", "opex"], "func": f22_mctj_095_opex_to_rev_4q_slope},
    "f22_mctj_096_opex_to_rev_8q_slope": {"inputs": ["revenue", "opex"], "func": f22_mctj_096_opex_to_rev_8q_slope},
    "f22_mctj_097_opex_to_rev_drawup_from_8q_min": {"inputs": ["revenue", "opex"], "func": f22_mctj_097_opex_to_rev_drawup_from_8q_min},
    "f22_mctj_098_opex_to_rev_zscore_8q": {"inputs": ["revenue", "opex"], "func": f22_mctj_098_opex_to_rev_zscore_8q},
    "f22_mctj_099_sgna_to_rev_4q_slope": {"inputs": ["revenue", "sgna"], "func": f22_mctj_099_sgna_to_rev_4q_slope},
    "f22_mctj_100_sgna_to_rev_8q_slope": {"inputs": ["revenue", "sgna"], "func": f22_mctj_100_sgna_to_rev_8q_slope},
    "f22_mctj_101_sgna_to_rev_drawup_from_8q_min": {"inputs": ["revenue", "sgna"], "func": f22_mctj_101_sgna_to_rev_drawup_from_8q_min},
    "f22_mctj_102_sgna_to_rev_zscore_8q": {"inputs": ["revenue", "sgna"], "func": f22_mctj_102_sgna_to_rev_zscore_8q},
    "f22_mctj_103_cost_intensity_composite": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_103_cost_intensity_composite},
    "f22_mctj_104_cost_intensity_composite_qoq_change": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_104_cost_intensity_composite_qoq_change},
    "f22_mctj_105_cost_intensity_composite_8q_slope": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_105_cost_intensity_composite_8q_slope},
    "f22_mctj_106_cost_intensity_composite_drawup_from_8q_min": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_106_cost_intensity_composite_drawup_from_8q_min},
    "f22_mctj_107_cost_intensity_composite_zscore_8q": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_107_cost_intensity_composite_zscore_8q},
    "f22_mctj_108_cogs_growth_minus_rev_growth_yoy": {"inputs": ["revenue", "cogs"], "func": f22_mctj_108_cogs_growth_minus_rev_growth_yoy},
    "f22_mctj_109_opex_growth_minus_rev_growth_yoy": {"inputs": ["revenue", "opex"], "func": f22_mctj_109_opex_growth_minus_rev_growth_yoy},
    "f22_mctj_110_sgna_growth_minus_rev_growth_yoy": {"inputs": ["revenue", "sgna"], "func": f22_mctj_110_sgna_growth_minus_rev_growth_yoy},
    "f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct": {"inputs": ["revenue", "cogs"], "func": f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct},
    "f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct": {"inputs": ["revenue", "opex"], "func": f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct},
    "f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct": {"inputs": ["revenue", "sgna"], "func": f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct},
    "f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q": {"inputs": ["revenue", "cogs"], "func": f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q},
    "f22_mctj_115_opex_to_rev_yoy_change_zscore_8q": {"inputs": ["revenue", "opex"], "func": f22_mctj_115_opex_to_rev_yoy_change_zscore_8q},
    "f22_mctj_116_gm_std_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_116_gm_std_8q},
    "f22_mctj_117_om_std_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_117_om_std_8q},
    "f22_mctj_118_ebitdam_std_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_118_ebitdam_std_8q},
    "f22_mctj_119_nm_std_8q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_119_nm_std_8q},
    "f22_mctj_120_gm_std_12q": {"inputs": ["revenue", "gp"], "func": f22_mctj_120_gm_std_12q},
    "f22_mctj_121_om_std_12q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_121_om_std_12q},
    "f22_mctj_122_gm_qoq_change_std_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_122_gm_qoq_change_std_8q},
    "f22_mctj_123_om_qoq_change_std_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_123_om_qoq_change_std_8q},
    "f22_mctj_124_ebitdam_qoq_change_std_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_124_ebitdam_qoq_change_std_8q},
    "f22_mctj_125_nm_qoq_change_std_8q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_125_nm_qoq_change_std_8q},
    "f22_mctj_126_gm_abs_change_mean_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_126_gm_abs_change_mean_8q},
    "f22_mctj_127_om_abs_change_mean_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_127_om_abs_change_mean_8q},
    "f22_mctj_128_gm_sign_flip_count_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_128_gm_sign_flip_count_8q},
    "f22_mctj_129_om_sign_flip_count_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_129_om_sign_flip_count_8q},
    "f22_mctj_130_ebitdam_sign_flip_count_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_130_ebitdam_sign_flip_count_8q},
    "f22_mctj_131_gm_inflection_neg_4q": {"inputs": ["revenue", "gp"], "func": f22_mctj_131_gm_inflection_neg_4q},
    "f22_mctj_132_om_inflection_neg_4q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_132_om_inflection_neg_4q},
    "f22_mctj_133_ebitdam_inflection_neg_4q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_133_ebitdam_inflection_neg_4q},
    "f22_mctj_134_nm_inflection_neg_4q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_134_nm_inflection_neg_4q},
    "f22_mctj_135_gm_step_down_size_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_135_gm_step_down_size_8q},
    "f22_mctj_136_om_step_down_size_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_136_om_step_down_size_8q},
    "f22_mctj_137_ebitdam_step_down_size_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_137_ebitdam_step_down_size_8q},
    "f22_mctj_138_nm_step_down_size_8q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_138_nm_step_down_size_8q},
    "f22_mctj_139_gm_cliff_indicator": {"inputs": ["revenue", "gp"], "func": f22_mctj_139_gm_cliff_indicator},
    "f22_mctj_140_om_cliff_indicator": {"inputs": ["revenue", "opinc"], "func": f22_mctj_140_om_cliff_indicator},
    "f22_mctj_141_ebitdam_cliff_indicator": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_141_ebitdam_cliff_indicator},
    "f22_mctj_142_nm_cliff_indicator": {"inputs": ["revenue", "netinc"], "func": f22_mctj_142_nm_cliff_indicator},
    "f22_mctj_143_gm_chow_proxy_8q": {"inputs": ["revenue", "gp"], "func": f22_mctj_143_gm_chow_proxy_8q},
    "f22_mctj_144_om_chow_proxy_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_144_om_chow_proxy_8q},
    "f22_mctj_145_ebitdam_chow_proxy_8q": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_145_ebitdam_chow_proxy_8q},
    "f22_mctj_146_nm_chow_proxy_8q": {"inputs": ["revenue", "netinc"], "func": f22_mctj_146_nm_chow_proxy_8q},
    "f22_mctj_147_margin_full_stack_compression_count_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_147_margin_full_stack_compression_count_8q},
    "f22_mctj_148_margin_compression_breadth": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_148_margin_compression_breadth},
    "f22_mctj_149_margin_compression_persistence": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_149_margin_compression_persistence},
    "f22_mctj_150_margin_terminal_signal": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_150_margin_terminal_signal},
}
