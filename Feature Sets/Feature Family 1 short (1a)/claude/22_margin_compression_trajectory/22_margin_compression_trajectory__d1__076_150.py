"""margin_compression_trajectory d1 features 076-150 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained;
helpers redefined locally per HANDOFF. PIT-clean: right-anchored rolling, explicit min_periods.
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
#                    D1 FEATURES 076-150
# ============================================================

def f22_mctj_076_gm_consec_decline_streak_d1(revenue, gp):
    return (_consec_decline_streak(_safe_div(gp, revenue))).diff()


def f22_mctj_077_om_consec_decline_streak_d1(revenue, opinc):
    return (_consec_decline_streak(_safe_div(opinc, revenue))).diff()


def f22_mctj_078_ebitdam_consec_decline_streak_d1(revenue, ebitda):
    return (_consec_decline_streak(_safe_div(ebitda, revenue))).diff()


def f22_mctj_079_nm_consec_decline_streak_d1(revenue, netinc):
    return (_consec_decline_streak(_safe_div(netinc, revenue))).diff()


def f22_mctj_080_gm_4q_min_minus_max_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    return (s.rolling(4, min_periods=2).min() - s.rolling(4, min_periods=2).max()).diff()


def f22_mctj_081_om_4q_min_minus_max_d1(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return (s.rolling(4, min_periods=2).min() - s.rolling(4, min_periods=2).max()).diff()


def f22_mctj_082_gm_8q_min_minus_max_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    return (s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()).diff()


def f22_mctj_083_om_8q_min_minus_max_d1(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return (s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()).diff()


def f22_mctj_084_ebitdam_8q_min_minus_max_d1(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return (s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()).diff()


def f22_mctj_085_nm_8q_min_minus_max_d1(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return (s.rolling(8, min_periods=3).min() - s.rolling(8, min_periods=3).max()).diff()


def f22_mctj_086_gm_below_8q_mean_count_8q_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return ((s < m).astype(float).rolling(8, min_periods=3).sum()).diff()


def f22_mctj_087_om_below_8q_mean_count_8q_d1(revenue, opinc):
    s = _safe_div(opinc, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return ((s < m).astype(float).rolling(8, min_periods=3).sum()).diff()


def f22_mctj_088_ebitdam_below_8q_mean_count_8q_d1(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return ((s < m).astype(float).rolling(8, min_periods=3).sum()).diff()


def f22_mctj_089_nm_below_8q_mean_count_8q_d1(revenue, netinc):
    s = _safe_div(netinc, revenue)
    m = s.rolling(8, min_periods=3).mean()
    return ((s < m).astype(float).rolling(8, min_periods=3).sum()).diff()


def f22_mctj_090_gm_below_neg_count_8q_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    return ((s < 0).astype(float).rolling(8, min_periods=3).sum()).diff()


def f22_mctj_091_cogs_to_rev_4q_slope_d1(revenue, cogs):
    return (_rolling_slope(_safe_div(cogs, revenue), 4, min_periods=2)).diff()


def f22_mctj_092_cogs_to_rev_8q_slope_d1(revenue, cogs):
    return (_rolling_slope(_safe_div(cogs, revenue), 8, min_periods=3)).diff()


def f22_mctj_093_cogs_to_rev_drawup_from_8q_min_d1(revenue, cogs):
    s = _safe_div(cogs, revenue)
    return (s - s.rolling(8, min_periods=3).min()).diff()


def f22_mctj_094_cogs_to_rev_zscore_8q_d1(revenue, cogs):
    return (_rolling_zscore(_safe_div(cogs, revenue), 8, min_periods=3)).diff()


def f22_mctj_095_opex_to_rev_4q_slope_d1(revenue, opex):
    return (_rolling_slope(_safe_div(opex, revenue), 4, min_periods=2)).diff()


def f22_mctj_096_opex_to_rev_8q_slope_d1(revenue, opex):
    return (_rolling_slope(_safe_div(opex, revenue), 8, min_periods=3)).diff()


def f22_mctj_097_opex_to_rev_drawup_from_8q_min_d1(revenue, opex):
    s = _safe_div(opex, revenue)
    return (s - s.rolling(8, min_periods=3).min()).diff()


def f22_mctj_098_opex_to_rev_zscore_8q_d1(revenue, opex):
    return (_rolling_zscore(_safe_div(opex, revenue), 8, min_periods=3)).diff()


def f22_mctj_099_sgna_to_rev_4q_slope_d1(revenue, sgna):
    return (_rolling_slope(_safe_div(sgna, revenue), 4, min_periods=2)).diff()


def f22_mctj_100_sgna_to_rev_8q_slope_d1(revenue, sgna):
    return (_rolling_slope(_safe_div(sgna, revenue), 8, min_periods=3)).diff()


def f22_mctj_101_sgna_to_rev_drawup_from_8q_min_d1(revenue, sgna):
    s = _safe_div(sgna, revenue)
    return (s - s.rolling(8, min_periods=3).min()).diff()


def f22_mctj_102_sgna_to_rev_zscore_8q_d1(revenue, sgna):
    return (_rolling_zscore(_safe_div(sgna, revenue), 8, min_periods=3)).diff()


def f22_mctj_103_cost_intensity_composite_d1(revenue, cogs, opex, sgna):
    return (_safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)).diff()


def f22_mctj_104_cost_intensity_composite_qoq_change_d1(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return (s.diff()).diff()


def f22_mctj_105_cost_intensity_composite_8q_slope_d1(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return (_rolling_slope(s, 8, min_periods=3)).diff()


def f22_mctj_106_cost_intensity_composite_drawup_from_8q_min_d1(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return (s - s.rolling(8, min_periods=3).min()).diff()


def f22_mctj_107_cost_intensity_composite_zscore_8q_d1(revenue, cogs, opex, sgna):
    s = _safe_div(cogs, revenue) + _safe_div(opex, revenue) + _safe_div(sgna, revenue)
    return (_rolling_zscore(s, 8, min_periods=3)).diff()


def f22_mctj_108_cogs_growth_minus_rev_growth_yoy_d1(revenue, cogs):
    return (_yoy_pct(cogs) - _yoy_pct(revenue)).diff()


def f22_mctj_109_opex_growth_minus_rev_growth_yoy_d1(revenue, opex):
    return (_yoy_pct(opex) - _yoy_pct(revenue)).diff()


def f22_mctj_110_sgna_growth_minus_rev_growth_yoy_d1(revenue, sgna):
    return (_yoy_pct(sgna) - _yoy_pct(revenue)).diff()


def f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct_d1(revenue, cogs):
    return (_qoq_pct(cogs) - _qoq_pct(revenue)).diff()


def f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct_d1(revenue, opex):
    return (_qoq_pct(opex) - _qoq_pct(revenue)).diff()


def f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct_d1(revenue, sgna):
    return (_qoq_pct(sgna) - _qoq_pct(revenue)).diff()


def f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q_d1(revenue, cogs):
    s = _safe_div(cogs, revenue)
    return (_rolling_zscore(s - s.shift(4), 8, min_periods=3)).diff()


def f22_mctj_115_opex_to_rev_yoy_change_zscore_8q_d1(revenue, opex):
    s = _safe_div(opex, revenue)
    return (_rolling_zscore(s - s.shift(4), 8, min_periods=3)).diff()


def f22_mctj_116_gm_std_8q_d1(revenue, gp):
    return (_safe_div(gp, revenue).rolling(8, min_periods=3).std()).diff()


def f22_mctj_117_om_std_8q_d1(revenue, opinc):
    return (_safe_div(opinc, revenue).rolling(8, min_periods=3).std()).diff()


def f22_mctj_118_ebitdam_std_8q_d1(revenue, ebitda):
    return (_safe_div(ebitda, revenue).rolling(8, min_periods=3).std()).diff()


def f22_mctj_119_nm_std_8q_d1(revenue, netinc):
    return (_safe_div(netinc, revenue).rolling(8, min_periods=3).std()).diff()


def f22_mctj_120_gm_std_12q_d1(revenue, gp):
    return (_safe_div(gp, revenue).rolling(12, min_periods=4).std()).diff()


def f22_mctj_121_om_std_12q_d1(revenue, opinc):
    return (_safe_div(opinc, revenue).rolling(12, min_periods=4).std()).diff()


def f22_mctj_122_gm_qoq_change_std_8q_d1(revenue, gp):
    return (_safe_div(gp, revenue).diff().rolling(8, min_periods=3).std()).diff()


def f22_mctj_123_om_qoq_change_std_8q_d1(revenue, opinc):
    return (_safe_div(opinc, revenue).diff().rolling(8, min_periods=3).std()).diff()


def f22_mctj_124_ebitdam_qoq_change_std_8q_d1(revenue, ebitda):
    return (_safe_div(ebitda, revenue).diff().rolling(8, min_periods=3).std()).diff()


def f22_mctj_125_nm_qoq_change_std_8q_d1(revenue, netinc):
    return (_safe_div(netinc, revenue).diff().rolling(8, min_periods=3).std()).diff()


def f22_mctj_126_gm_abs_change_mean_8q_d1(revenue, gp):
    return (_safe_div(gp, revenue).diff().abs().rolling(8, min_periods=3).mean()).diff()


def f22_mctj_127_om_abs_change_mean_8q_d1(revenue, opinc):
    return (_safe_div(opinc, revenue).diff().abs().rolling(8, min_periods=3).mean()).diff()


def f22_mctj_128_gm_sign_flip_count_8q_d1(revenue, gp):
    return (_sign_flip_count(_safe_div(gp, revenue), 8)).diff()


def f22_mctj_129_om_sign_flip_count_8q_d1(revenue, opinc):
    return (_sign_flip_count(_safe_div(opinc, revenue), 8)).diff()


def f22_mctj_130_ebitdam_sign_flip_count_8q_d1(revenue, ebitda):
    return (_sign_flip_count(_safe_div(ebitda, revenue), 8)).diff()


def f22_mctj_131_gm_inflection_neg_4q_d1(revenue, gp):
    slp = _rolling_slope(_safe_div(gp, revenue), 4, min_periods=2)
    return (((slp.shift(4) > 0) & (slp < 0)).astype(float)).diff()


def f22_mctj_132_om_inflection_neg_4q_d1(revenue, opinc):
    slp = _rolling_slope(_safe_div(opinc, revenue), 4, min_periods=2)
    return (((slp.shift(4) > 0) & (slp < 0)).astype(float)).diff()


def f22_mctj_133_ebitdam_inflection_neg_4q_d1(revenue, ebitda):
    slp = _rolling_slope(_safe_div(ebitda, revenue), 4, min_periods=2)
    return (((slp.shift(4) > 0) & (slp < 0)).astype(float)).diff()


def f22_mctj_134_nm_inflection_neg_4q_d1(revenue, netinc):
    slp = _rolling_slope(_safe_div(netinc, revenue), 4, min_periods=2)
    return (((slp.shift(4) > 0) & (slp < 0)).astype(float)).diff()


def f22_mctj_135_gm_step_down_size_8q_d1(revenue, gp):
    return (_safe_div(gp, revenue).diff().rolling(8, min_periods=3).min()).diff()


def f22_mctj_136_om_step_down_size_8q_d1(revenue, opinc):
    return (_safe_div(opinc, revenue).diff().rolling(8, min_periods=3).min()).diff()


def f22_mctj_137_ebitdam_step_down_size_8q_d1(revenue, ebitda):
    return (_safe_div(ebitda, revenue).diff().rolling(8, min_periods=3).min()).diff()


def f22_mctj_138_nm_step_down_size_8q_d1(revenue, netinc):
    return (_safe_div(netinc, revenue).diff().rolling(8, min_periods=3).min()).diff()


def f22_mctj_139_gm_cliff_indicator_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return ((ch < (-2.0 * sd)).astype(float)).diff()


def f22_mctj_140_om_cliff_indicator_d1(revenue, opinc):
    s = _safe_div(opinc, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return ((ch < (-2.0 * sd)).astype(float)).diff()


def f22_mctj_141_ebitdam_cliff_indicator_d1(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return ((ch < (-2.0 * sd)).astype(float)).diff()


def f22_mctj_142_nm_cliff_indicator_d1(revenue, netinc):
    s = _safe_div(netinc, revenue)
    ch = s.diff()
    sd = s.rolling(8, min_periods=3).std()
    return ((ch < (-2.0 * sd)).astype(float)).diff()


def f22_mctj_143_gm_chow_proxy_8q_d1(revenue, gp):
    s = _safe_div(gp, revenue)
    return (s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()).diff()


def f22_mctj_144_om_chow_proxy_8q_d1(revenue, opinc):
    s = _safe_div(opinc, revenue)
    return (s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()).diff()


def f22_mctj_145_ebitdam_chow_proxy_8q_d1(revenue, ebitda):
    s = _safe_div(ebitda, revenue)
    return (s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()).diff()


def f22_mctj_146_nm_chow_proxy_8q_d1(revenue, netinc):
    s = _safe_div(netinc, revenue)
    return (s.rolling(4, min_periods=2).mean() - s.shift(4).rolling(4, min_periods=2).mean()).diff()


def f22_mctj_147_margin_full_stack_compression_count_8q_d1(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    flag = ((gm_d < 0) & (om_d < 0) & (em_d < 0) & (nm_d < 0)).astype(float)
    return (flag.rolling(8, min_periods=3).sum()).diff()


def f22_mctj_148_margin_compression_breadth_d1(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    return ((gm_d < 0).astype(float) + (om_d < 0).astype(float)
            + (em_d < 0).astype(float) + (nm_d < 0).astype(float)).diff()


def f22_mctj_149_margin_compression_persistence_d1(revenue, gp, opinc, ebitda, netinc):
    gm_d = _safe_div(gp, revenue).diff()
    om_d = _safe_div(opinc, revenue).diff()
    em_d = _safe_div(ebitda, revenue).diff()
    nm_d = _safe_div(netinc, revenue).diff()
    breadth = ((gm_d < 0).astype(float) + (om_d < 0).astype(float)
               + (em_d < 0).astype(float) + (nm_d < 0).astype(float))
    full = (breadth == 4).astype(float)
    grp = (full == 0).cumsum()
    return (full.groupby(grp).cumsum()).diff()


def f22_mctj_150_margin_terminal_signal_d1(revenue, gp, opinc, ebitda, netinc):
    gm_s = _rolling_slope(_safe_div(gp, revenue), 8, min_periods=3)
    om_s = _rolling_slope(_safe_div(opinc, revenue), 8, min_periods=3)
    em_s = _rolling_slope(_safe_div(ebitda, revenue), 8, min_periods=3)
    nm_s = _rolling_slope(_safe_div(netinc, revenue), 8, min_periods=3)
    return (((gm_s < 0) & (om_s < 0) & (em_s < 0) & (nm_s < 0)).astype(float)).diff()


# ============================================================
#                        REGISTRY
# ============================================================

MARGIN_COMPRESSION_TRAJECTORY_D1_REGISTRY_076_150 = {
    "f22_mctj_076_gm_consec_decline_streak_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_076_gm_consec_decline_streak_d1},
    "f22_mctj_077_om_consec_decline_streak_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_077_om_consec_decline_streak_d1},
    "f22_mctj_078_ebitdam_consec_decline_streak_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_078_ebitdam_consec_decline_streak_d1},
    "f22_mctj_079_nm_consec_decline_streak_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_079_nm_consec_decline_streak_d1},
    "f22_mctj_080_gm_4q_min_minus_max_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_080_gm_4q_min_minus_max_d1},
    "f22_mctj_081_om_4q_min_minus_max_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_081_om_4q_min_minus_max_d1},
    "f22_mctj_082_gm_8q_min_minus_max_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_082_gm_8q_min_minus_max_d1},
    "f22_mctj_083_om_8q_min_minus_max_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_083_om_8q_min_minus_max_d1},
    "f22_mctj_084_ebitdam_8q_min_minus_max_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_084_ebitdam_8q_min_minus_max_d1},
    "f22_mctj_085_nm_8q_min_minus_max_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_085_nm_8q_min_minus_max_d1},
    "f22_mctj_086_gm_below_8q_mean_count_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_086_gm_below_8q_mean_count_8q_d1},
    "f22_mctj_087_om_below_8q_mean_count_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_087_om_below_8q_mean_count_8q_d1},
    "f22_mctj_088_ebitdam_below_8q_mean_count_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_088_ebitdam_below_8q_mean_count_8q_d1},
    "f22_mctj_089_nm_below_8q_mean_count_8q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_089_nm_below_8q_mean_count_8q_d1},
    "f22_mctj_090_gm_below_neg_count_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_090_gm_below_neg_count_8q_d1},
    "f22_mctj_091_cogs_to_rev_4q_slope_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_091_cogs_to_rev_4q_slope_d1},
    "f22_mctj_092_cogs_to_rev_8q_slope_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_092_cogs_to_rev_8q_slope_d1},
    "f22_mctj_093_cogs_to_rev_drawup_from_8q_min_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_093_cogs_to_rev_drawup_from_8q_min_d1},
    "f22_mctj_094_cogs_to_rev_zscore_8q_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_094_cogs_to_rev_zscore_8q_d1},
    "f22_mctj_095_opex_to_rev_4q_slope_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_095_opex_to_rev_4q_slope_d1},
    "f22_mctj_096_opex_to_rev_8q_slope_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_096_opex_to_rev_8q_slope_d1},
    "f22_mctj_097_opex_to_rev_drawup_from_8q_min_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_097_opex_to_rev_drawup_from_8q_min_d1},
    "f22_mctj_098_opex_to_rev_zscore_8q_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_098_opex_to_rev_zscore_8q_d1},
    "f22_mctj_099_sgna_to_rev_4q_slope_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_099_sgna_to_rev_4q_slope_d1},
    "f22_mctj_100_sgna_to_rev_8q_slope_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_100_sgna_to_rev_8q_slope_d1},
    "f22_mctj_101_sgna_to_rev_drawup_from_8q_min_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_101_sgna_to_rev_drawup_from_8q_min_d1},
    "f22_mctj_102_sgna_to_rev_zscore_8q_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_102_sgna_to_rev_zscore_8q_d1},
    "f22_mctj_103_cost_intensity_composite_d1": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_103_cost_intensity_composite_d1},
    "f22_mctj_104_cost_intensity_composite_qoq_change_d1": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_104_cost_intensity_composite_qoq_change_d1},
    "f22_mctj_105_cost_intensity_composite_8q_slope_d1": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_105_cost_intensity_composite_8q_slope_d1},
    "f22_mctj_106_cost_intensity_composite_drawup_from_8q_min_d1": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_106_cost_intensity_composite_drawup_from_8q_min_d1},
    "f22_mctj_107_cost_intensity_composite_zscore_8q_d1": {"inputs": ["revenue", "cogs", "opex", "sgna"], "func": f22_mctj_107_cost_intensity_composite_zscore_8q_d1},
    "f22_mctj_108_cogs_growth_minus_rev_growth_yoy_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_108_cogs_growth_minus_rev_growth_yoy_d1},
    "f22_mctj_109_opex_growth_minus_rev_growth_yoy_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_109_opex_growth_minus_rev_growth_yoy_d1},
    "f22_mctj_110_sgna_growth_minus_rev_growth_yoy_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_110_sgna_growth_minus_rev_growth_yoy_d1},
    "f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_111_cogs_qoq_pct_minus_rev_qoq_pct_d1},
    "f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_112_opex_qoq_pct_minus_rev_qoq_pct_d1},
    "f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct_d1": {"inputs": ["revenue", "sgna"], "func": f22_mctj_113_sgna_qoq_pct_minus_rev_qoq_pct_d1},
    "f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q_d1": {"inputs": ["revenue", "cogs"], "func": f22_mctj_114_cogs_to_rev_yoy_change_zscore_8q_d1},
    "f22_mctj_115_opex_to_rev_yoy_change_zscore_8q_d1": {"inputs": ["revenue", "opex"], "func": f22_mctj_115_opex_to_rev_yoy_change_zscore_8q_d1},
    "f22_mctj_116_gm_std_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_116_gm_std_8q_d1},
    "f22_mctj_117_om_std_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_117_om_std_8q_d1},
    "f22_mctj_118_ebitdam_std_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_118_ebitdam_std_8q_d1},
    "f22_mctj_119_nm_std_8q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_119_nm_std_8q_d1},
    "f22_mctj_120_gm_std_12q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_120_gm_std_12q_d1},
    "f22_mctj_121_om_std_12q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_121_om_std_12q_d1},
    "f22_mctj_122_gm_qoq_change_std_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_122_gm_qoq_change_std_8q_d1},
    "f22_mctj_123_om_qoq_change_std_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_123_om_qoq_change_std_8q_d1},
    "f22_mctj_124_ebitdam_qoq_change_std_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_124_ebitdam_qoq_change_std_8q_d1},
    "f22_mctj_125_nm_qoq_change_std_8q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_125_nm_qoq_change_std_8q_d1},
    "f22_mctj_126_gm_abs_change_mean_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_126_gm_abs_change_mean_8q_d1},
    "f22_mctj_127_om_abs_change_mean_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_127_om_abs_change_mean_8q_d1},
    "f22_mctj_128_gm_sign_flip_count_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_128_gm_sign_flip_count_8q_d1},
    "f22_mctj_129_om_sign_flip_count_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_129_om_sign_flip_count_8q_d1},
    "f22_mctj_130_ebitdam_sign_flip_count_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_130_ebitdam_sign_flip_count_8q_d1},
    "f22_mctj_131_gm_inflection_neg_4q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_131_gm_inflection_neg_4q_d1},
    "f22_mctj_132_om_inflection_neg_4q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_132_om_inflection_neg_4q_d1},
    "f22_mctj_133_ebitdam_inflection_neg_4q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_133_ebitdam_inflection_neg_4q_d1},
    "f22_mctj_134_nm_inflection_neg_4q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_134_nm_inflection_neg_4q_d1},
    "f22_mctj_135_gm_step_down_size_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_135_gm_step_down_size_8q_d1},
    "f22_mctj_136_om_step_down_size_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_136_om_step_down_size_8q_d1},
    "f22_mctj_137_ebitdam_step_down_size_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_137_ebitdam_step_down_size_8q_d1},
    "f22_mctj_138_nm_step_down_size_8q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_138_nm_step_down_size_8q_d1},
    "f22_mctj_139_gm_cliff_indicator_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_139_gm_cliff_indicator_d1},
    "f22_mctj_140_om_cliff_indicator_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_140_om_cliff_indicator_d1},
    "f22_mctj_141_ebitdam_cliff_indicator_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_141_ebitdam_cliff_indicator_d1},
    "f22_mctj_142_nm_cliff_indicator_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_142_nm_cliff_indicator_d1},
    "f22_mctj_143_gm_chow_proxy_8q_d1": {"inputs": ["revenue", "gp"], "func": f22_mctj_143_gm_chow_proxy_8q_d1},
    "f22_mctj_144_om_chow_proxy_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_144_om_chow_proxy_8q_d1},
    "f22_mctj_145_ebitdam_chow_proxy_8q_d1": {"inputs": ["revenue", "ebitda"], "func": f22_mctj_145_ebitdam_chow_proxy_8q_d1},
    "f22_mctj_146_nm_chow_proxy_8q_d1": {"inputs": ["revenue", "netinc"], "func": f22_mctj_146_nm_chow_proxy_8q_d1},
    "f22_mctj_147_margin_full_stack_compression_count_8q_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_147_margin_full_stack_compression_count_8q_d1},
    "f22_mctj_148_margin_compression_breadth_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_148_margin_compression_breadth_d1},
    "f22_mctj_149_margin_compression_persistence_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_149_margin_compression_persistence_d1},
    "f22_mctj_150_margin_terminal_signal_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f22_mctj_150_margin_terminal_signal_d1},
}
