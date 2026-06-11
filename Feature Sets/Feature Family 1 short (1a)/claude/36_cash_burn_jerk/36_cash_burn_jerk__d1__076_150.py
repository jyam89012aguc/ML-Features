"""cash_burn_jerk d1 features 076_150 — short blowup pipeline 1a-inverse.

Cash-flow jerk pattern detection: turning points, cliffs, regime shifts in the third difference of cash-flow trajectories.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
SF1 quarterly cadence (lags 1, 4, 8, 12, 16, 20 quarters).
"""
import numpy as np
import pandas as pd


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


def _rolling_mad_z(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median().replace(0, np.nan)
    return (s - med) / (1.4826 * mad)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


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


def _sign_safe(s):
    return np.sign(s).where(s.notna(), np.nan)


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()


def _max_consec_true(b, window):
    return _consec_true_streak(b).rolling(window, min_periods=1).max()


def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()


def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()


def _winsorize(s, lo=0.1, hi=0.9, window=8, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    qlo = s.rolling(window, min_periods=min_periods).quantile(lo)
    qhi = s.rolling(window, min_periods=min_periods).quantile(hi)
    return s.clip(lower=qlo, upper=qhi)


def _jerk(s):
    """Quarter-over-quarter-over-quarter-over-quarter jerk (third diff)."""
    return s.diff().diff().diff()


def _accel(s):
    return s.diff().diff()


def _gm(revenue, gp):
    return _safe_div(gp, revenue.abs())


def _om(revenue, opinc):
    return _safe_div(opinc, revenue.abs())


def _em(revenue, ebitda):
    return _safe_div(ebitda, revenue.abs())


def _nm(revenue, netinc):
    return _safe_div(netinc, revenue.abs())


def _gm_ttm(revenue, gp):
    return _safe_div(_ttm(gp), _ttm(revenue).abs())


def _om_ttm(revenue, opinc):
    return _safe_div(_ttm(opinc), _ttm(revenue).abs())


def _em_ttm(revenue, ebitda):
    return _safe_div(_ttm(ebitda), _ttm(revenue).abs())


def _nm_ttm(revenue, netinc):
    return _safe_div(_ttm(netinc), _ttm(revenue).abs())


def _cusum(s, window):
    """Rolling CUSUM around mean — peak absolute excursion in window."""
    m = s.rolling(window, min_periods=max(window // 3, 2)).mean()
    dev = s - m
    return dev.rolling(window, min_periods=max(window // 3, 2)).apply(
        lambda w: float(np.nanmax(np.abs(np.nancumsum(w)))) if not np.all(np.isnan(w)) else np.nan, raw=True
    )


# ============================================================
#                    D1 FEATURES 076-150
# ============================================================

def f36_cbjk_076_ncfo_jerk_q_since_min_12q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return (j.rolling(12, min_periods=4).apply(_b, raw=True)).diff()


def f36_cbjk_077_fcf_jerk_q_since_min_12q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return (j.rolling(12, min_periods=4).apply(_b, raw=True)).diff()


def f36_cbjk_078_cashneq_jerk_q_since_min_12q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return (j.rolling(12, min_periods=4).apply(_b, raw=True)).diff()


def f36_cbjk_079_ncfo_a_jerk_q_since_min_12q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return (j.rolling(12, min_periods=4).apply(_b, raw=True)).diff()


def f36_cbjk_080_fcf_a_jerk_q_since_min_12q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return (j.rolling(12, min_periods=4).apply(_b, raw=True)).diff()


def f36_cbjk_081_ncfo_jerk_cusum_12q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    return (_cusum(j, 12)).diff()


def f36_cbjk_082_fcf_jerk_cusum_12q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    return (_cusum(j, 12)).diff()


def f36_cbjk_083_cashneq_jerk_cusum_12q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    return (_cusum(j, 12)).diff()


def f36_cbjk_084_ncfo_a_jerk_cusum_12q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return (_cusum(j, 12)).diff()


def f36_cbjk_085_fcf_a_jerk_cusum_12q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    return (_cusum(j, 12)).diff()


def f36_cbjk_086_ncfo_jerk_mean_shift_t_4q_vs_12q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return ((m4 - m12) / s12).diff()


def f36_cbjk_087_fcf_jerk_mean_shift_t_4q_vs_12q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return ((m4 - m12) / s12).diff()


def f36_cbjk_088_cashneq_jerk_mean_shift_t_4q_vs_12q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return ((m4 - m12) / s12).diff()


def f36_cbjk_089_ncfo_a_jerk_mean_shift_t_4q_vs_12q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return ((m4 - m12) / s12).diff()


def f36_cbjk_090_fcf_a_jerk_mean_shift_t_4q_vs_12q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return ((m4 - m12) / s12).diff()


def f36_cbjk_091_ncfo_jerk_variance_jump_4q_vs_12q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    return (_safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())).diff()


def f36_cbjk_092_fcf_jerk_variance_jump_4q_vs_12q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    return (_safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())).diff()


def f36_cbjk_093_cashneq_jerk_variance_jump_4q_vs_12q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    return (_safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())).diff()


def f36_cbjk_094_ncfo_a_jerk_variance_jump_4q_vs_12q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return (_safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())).diff()


def f36_cbjk_095_fcf_a_jerk_variance_jump_4q_vs_12q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    return (_safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())).diff()


def f36_cbjk_096_ncfo_jerk_ar1_persistence_8q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    return (j.rolling(8, min_periods=3).corr(j.shift(1))).diff()


def f36_cbjk_097_fcf_jerk_ar1_persistence_8q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    return (j.rolling(8, min_periods=3).corr(j.shift(1))).diff()


def f36_cbjk_098_cashneq_jerk_ar1_persistence_8q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    return (j.rolling(8, min_periods=3).corr(j.shift(1))).diff()


def f36_cbjk_099_ncfo_a_jerk_ar1_persistence_8q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return (j.rolling(8, min_periods=3).corr(j.shift(1))).diff()


def f36_cbjk_100_fcf_a_jerk_ar1_persistence_8q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    return (j.rolling(8, min_periods=3).corr(j.shift(1))).diff()


def f36_cbjk_101_ncfo_jerk_ema_fast_minus_slow_div_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    return (_ema(j, 4) - _ema(j, 12)).diff()


def f36_cbjk_102_fcf_jerk_ema_fast_minus_slow_div_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    return (_ema(j, 4) - _ema(j, 12)).diff()


def f36_cbjk_103_cashneq_jerk_ema_fast_minus_slow_div_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    return (_ema(j, 4) - _ema(j, 12)).diff()


def f36_cbjk_104_ncfo_a_jerk_ema_fast_minus_slow_div_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return (_ema(j, 4) - _ema(j, 12)).diff()


def f36_cbjk_105_fcf_a_jerk_ema_fast_minus_slow_div_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    return (_ema(j, 4) - _ema(j, 12)).diff()


def f36_cbjk_106_ncfo_jerk_ulcer_index_neg_8q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    neg = j.clip(upper=0)
    return (np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())).diff()


def f36_cbjk_107_fcf_jerk_ulcer_index_neg_8q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    neg = j.clip(upper=0)
    return (np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())).diff()


def f36_cbjk_108_cashneq_jerk_ulcer_index_neg_8q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    neg = j.clip(upper=0)
    return (np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())).diff()


def f36_cbjk_109_ncfo_a_jerk_ulcer_index_neg_8q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    neg = j.clip(upper=0)
    return (np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())).diff()


def f36_cbjk_110_fcf_a_jerk_ulcer_index_neg_8q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    neg = j.clip(upper=0)
    return (np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())).diff()


def f36_cbjk_111_ncfo_jerk_event_count_below_q10_16q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return (_rolling_count(j < q10, 16)).diff()


def f36_cbjk_112_fcf_jerk_event_count_below_q10_16q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return (_rolling_count(j < q10, 16)).diff()


def f36_cbjk_113_cashneq_jerk_event_count_below_q10_16q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return (_rolling_count(j < q10, 16)).diff()


def f36_cbjk_114_ncfo_a_jerk_event_count_below_q10_16q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return (_rolling_count(j < q10, 16)).diff()


def f36_cbjk_115_fcf_a_jerk_event_count_below_q10_16q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return (_rolling_count(j < q10, 16)).diff()


def f36_cbjk_116_ncfo_jerk_decline_streak_max_16q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo)
    return (_max_consec_true(j < j.shift(1), 16)).diff()


def f36_cbjk_117_fcf_jerk_decline_streak_max_16q_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    return (_max_consec_true(j < j.shift(1), 16)).diff()


def f36_cbjk_118_cashneq_jerk_decline_streak_max_16q_d1(cashneq: pd.Series) -> pd.Series:
    j = _jerk(cashneq)
    return (_max_consec_true(j < j.shift(1), 16)).diff()


def f36_cbjk_119_ncfo_a_jerk_decline_streak_max_16q_d1(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return (_max_consec_true(j < j.shift(1), 16)).diff()


def f36_cbjk_120_fcf_a_jerk_decline_streak_max_16q_d1(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    return (_max_consec_true(j < j.shift(1), 16)).diff()


def f36_cbjk_121_ncfo_jerk_simultaneous_break_with_capex_8q_d1(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    j_n = _jerk(ncfo); j_c = _jerk(capex)
    cond = (_rolling_zscore(j_n, 8).abs() > 2) & (_rolling_zscore(j_c, 8).abs() > 2)
    return cond.astype(float).rolling(8, min_periods=3).sum().diff()


def f36_cbjk_122_fcf_jerk_runway_cliff_detector_8q_d1(fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    j_f = _jerk(fcf)
    runway = _safe_div(cashneq, fcf.abs())
    cond = (_rolling_zscore(j_f, 8) > 2) & (runway < 4)
    return cond.astype(float).diff()


def f36_cbjk_123_cashneq_jerk_with_debt_rise_8q_d1(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    j_c = _jerk(cashneq)
    debt_yoy = _safe_div(debt.diff(4), debt.shift(4).abs())
    cond = (_rolling_zscore(j_c, 8) < -1) & (debt_yoy > 0.05)
    return cond.astype(float).diff()


def f36_cbjk_124_ncfo_to_assets_jerk_during_revenue_decel_8q_d1(ncfo: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(ncfo, assets.abs()))
    rev_yoy = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    cond = rev_yoy < 0
    return j.abs().where(cond, np.nan).rolling(8, min_periods=3).mean().diff()


def f36_cbjk_125_fcf_to_assets_jerk_with_dilution_event_8q_d1(fcf: pd.Series, assets: pd.Series, sharesbas: pd.Series) -> pd.Series:
    j = _jerk(_safe_div(fcf, assets.abs()))
    shr_yoy = _safe_div(sharesbas.diff(4), sharesbas.shift(4).abs())
    cond = (_rolling_zscore(j, 8) < -1) & (shr_yoy > 0.05)
    return cond.astype(float).diff()


def f36_cbjk_126_ncfo_fcf_jerk_both_neg_count_8q_d1(ncfo: pd.Series, fcf: pd.Series) -> pd.Series:
    j1 = _jerk(ncfo) < 0; j2 = _jerk(fcf) < 0
    return (_rolling_count(j1 & j2, 8)).diff()


def f36_cbjk_127_ncfo_fcf_cashneq_jerk_all_neg_count_12q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    a = _jerk(ncfo) < 0; b = _jerk(fcf) < 0; c = _jerk(cashneq) < 0
    return (_rolling_count(a & b & c, 12)).diff()


def f36_cbjk_128_triple_flow_jerk_concordance_count_8q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    a = _sign_safe(_jerk(ncfo)); b = _sign_safe(_jerk(fcf)); c = _sign_safe(_jerk(cashneq))
    same = (a == b) & (b == c) & a.notna()
    return (_rolling_count(same, 8)).diff()


def f36_cbjk_129_triple_flow_jerk_dispersion_z_8q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    a = _jerk(ncfo); b = _jerk(fcf); c = _jerk(cashneq)
    disp = pd.concat([a, b, c], axis=1).std(axis=1)
    return (_rolling_zscore(disp, 8)).diff()


def f36_cbjk_130_triple_flow_jerk_compound_score_signed_8q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    return (_rolling_zscore(_jerk(ncfo), 8).fillna(0) + _rolling_zscore(_jerk(fcf), 8).fillna(0) + _rolling_zscore(_jerk(cashneq), 8).fillna(0)).diff()


def f36_cbjk_131_ncfo_jerk_minus_revenue_jerk_z_8q_d1(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_rolling_zscore(_jerk(ncfo), 8) - _rolling_zscore(_jerk(revenue), 8)).diff()


def f36_cbjk_132_fcf_jerk_minus_ebitda_jerk_z_8q_d1(fcf: pd.Series, ebitda: pd.Series) -> pd.Series:
    return (_rolling_zscore(_jerk(fcf), 8) - _rolling_zscore(_jerk(ebitda), 8)).diff()


def f36_cbjk_133_ncfo_to_netinc_ratio_jerk_z_8q_d1(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    r = _safe_div(ncfo, netinc.abs())
    return (_rolling_zscore(_jerk(r), 8)).diff()


def f36_cbjk_134_fcf_to_revenue_ratio_jerk_z_8q_d1(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(fcf, revenue.abs())
    return (_rolling_zscore(_jerk(r), 8)).diff()


def f36_cbjk_135_capex_to_revenue_jerk_z_8q_d1(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(capex.abs(), revenue.abs())
    return (_rolling_zscore(_jerk(r), 8)).diff()


def f36_cbjk_136_capex_to_depamor_jerk_z_8q_d1(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    r = _safe_div(capex.abs(), depamor.abs())
    return (_rolling_zscore(_jerk(r), 8)).diff()


def f36_cbjk_137_ncfo_minus_capex_jerk_z_8q_d1(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    impl_fcf = ncfo - capex.abs()
    return (_rolling_zscore(_jerk(impl_fcf), 8)).diff()


def f36_cbjk_138_financing_cash_inflow_jerk_indicator_8q_d1(ncff: pd.Series) -> pd.Series:
    j = _jerk(ncff)
    sd = j.rolling(8, min_periods=3).std()
    return ((j > 2 * sd).astype(float)).diff()


def f36_cbjk_139_financing_cash_inflow_jerk_count_12q_d1(ncff: pd.Series) -> pd.Series:
    j = _jerk(ncff)
    sd = j.rolling(8, min_periods=3).std()
    spike = j > 2 * sd
    return (_rolling_count(spike, 12)).diff()


def f36_cbjk_140_cashneq_jerk_with_ncff_inflow_co_indicator_8q_d1(cashneq: pd.Series, ncff: pd.Series) -> pd.Series:
    a = _jerk(cashneq) < 0; b = _jerk(ncff) > 0
    return (_rolling_count(a & b, 8)).diff()


def f36_cbjk_141_ncfo_jerk_with_neg_ncfo_level_co_indicator_8q_d1(ncfo: pd.Series) -> pd.Series:
    cond = (ncfo < 0) & (_jerk(ncfo) < 0)
    return (_rolling_count(cond, 8)).diff()


def f36_cbjk_142_conditional_fcf_jerk_given_cashneq_q10_8q_d1(fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    cond = cashneq < cashneq.rolling(12, min_periods=4).quantile(0.10)
    return (_jerk(fcf).where(cond, np.nan).rolling(8, min_periods=3).mean()).diff()


def f36_cbjk_143_conditional_ncfo_jerk_given_yoy_rev_neg_8q_d1(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    cond = _yoy_pct(revenue) < 0
    return (_jerk(ncfo).where(cond, np.nan).rolling(8, min_periods=3).mean()).diff()


def f36_cbjk_144_composite_cash_burn_jerk_fragility_5flow_8q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    a = _rolling_zscore((-_jerk(ncfo)).clip(lower=0), 8).fillna(0)
    b = _rolling_zscore((-_jerk(fcf)).clip(lower=0), 8).fillna(0)
    c = _rolling_zscore((-_jerk(cashneq)).clip(lower=0), 8).fillna(0)
    d = _rolling_zscore((-_jerk(_safe_div(ncfo, assets.abs()))).clip(lower=0), 8).fillna(0)
    e = _rolling_zscore((-_jerk(_safe_div(fcf, assets.abs()))).clip(lower=0), 8).fillna(0)
    return (a + b + c + d + e).diff()


def f36_cbjk_145_weighted_multi_flow_jerk_crash_z_clipm3_8q_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    a = _rolling_zscore((-_jerk(ncfo)).clip(lower=0), 8).clip(lower=0, upper=3)
    b = _rolling_zscore((-_jerk(fcf)).clip(lower=0), 8).clip(lower=0, upper=3)
    c = _rolling_zscore((-_jerk(cashneq)).clip(lower=0), 8).clip(lower=0, upper=3)
    return (a.fillna(0) + b.fillna(0) + c.fillna(0)).diff()


def f36_cbjk_146_multi_horizon_jerk_crash_score_fcf_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf); neg = (-j).clip(lower=0)
    return (_rolling_zscore(neg, 8).fillna(0) + _rolling_zscore(neg, 12).fillna(0) + _rolling_zscore(neg, 20).fillna(0)).diff()


def f36_cbjk_147_ewm_decay_jerk_crash_8q_ncfo_neg_d1(ncfo: pd.Series) -> pd.Series:
    return (_ema((-_jerk(ncfo)).clip(lower=0), 8)).diff()


def f36_cbjk_148_logit_cash_burn_jerk_probability_fcf_d1(fcf: pd.Series) -> pd.Series:
    j = _jerk(fcf)
    score = -1.0 * (_rolling_zscore(j, 8).fillna(0) + 0.5 * _rolling_zscore(j, 12).fillna(0) + 0.25 * _rolling_zscore(j, 20).fillna(0))
    return (1.0 / (1.0 + np.exp(-score))).diff()


def f36_cbjk_149_mahalanobis_ncfo_jerk_slope_8q_d1(ncfo: pd.Series) -> pd.Series:
    j = _jerk(ncfo); sl = _rolling_slope(j, 4)
    return (((_rolling_zscore(j, 8).pow(2) + _rolling_zscore(sl, 8).pow(2))).pow(0.5)).diff()


def f36_cbjk_150_cash_burn_jerk_aggregate_score_d1(ncfo: pd.Series, fcf: pd.Series, cashneq: pd.Series, ncff: pd.Series) -> pd.Series:
    j_n = _jerk(ncfo); j_f = _jerk(fcf); j_c = _jerk(cashneq); j_x = _jerk(ncff)
    compound = _rolling_zscore(j_n, 12).fillna(0) + _rolling_zscore(j_f, 12).fillna(0) + _rolling_zscore(j_c, 12).fillna(0)
    streak = _max_consec_true(j_n < 0, 12)
    dd = j_c - j_c.rolling(8, min_periods=3).max()
    return (-_rolling_zscore(compound, 12).fillna(0) + _rolling_zscore(streak, 12).fillna(0) - _rolling_zscore(dd, 12).fillna(0) + _rolling_zscore(j_x, 12).fillna(0)).diff()


CASH_BURN_JERK_D1_REGISTRY_076_150 = {
    "f36_cbjk_076_ncfo_jerk_q_since_min_12q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_076_ncfo_jerk_q_since_min_12q_d1},
    "f36_cbjk_077_fcf_jerk_q_since_min_12q_d1": {"inputs": ["fcf"], "func": f36_cbjk_077_fcf_jerk_q_since_min_12q_d1},
    "f36_cbjk_078_cashneq_jerk_q_since_min_12q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_078_cashneq_jerk_q_since_min_12q_d1},
    "f36_cbjk_079_ncfo_a_jerk_q_since_min_12q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_079_ncfo_a_jerk_q_since_min_12q_d1},
    "f36_cbjk_080_fcf_a_jerk_q_since_min_12q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_080_fcf_a_jerk_q_since_min_12q_d1},
    "f36_cbjk_081_ncfo_jerk_cusum_12q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_081_ncfo_jerk_cusum_12q_d1},
    "f36_cbjk_082_fcf_jerk_cusum_12q_d1": {"inputs": ["fcf"], "func": f36_cbjk_082_fcf_jerk_cusum_12q_d1},
    "f36_cbjk_083_cashneq_jerk_cusum_12q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_083_cashneq_jerk_cusum_12q_d1},
    "f36_cbjk_084_ncfo_a_jerk_cusum_12q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_084_ncfo_a_jerk_cusum_12q_d1},
    "f36_cbjk_085_fcf_a_jerk_cusum_12q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_085_fcf_a_jerk_cusum_12q_d1},
    "f36_cbjk_086_ncfo_jerk_mean_shift_t_4q_vs_12q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_086_ncfo_jerk_mean_shift_t_4q_vs_12q_d1},
    "f36_cbjk_087_fcf_jerk_mean_shift_t_4q_vs_12q_d1": {"inputs": ["fcf"], "func": f36_cbjk_087_fcf_jerk_mean_shift_t_4q_vs_12q_d1},
    "f36_cbjk_088_cashneq_jerk_mean_shift_t_4q_vs_12q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_088_cashneq_jerk_mean_shift_t_4q_vs_12q_d1},
    "f36_cbjk_089_ncfo_a_jerk_mean_shift_t_4q_vs_12q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_089_ncfo_a_jerk_mean_shift_t_4q_vs_12q_d1},
    "f36_cbjk_090_fcf_a_jerk_mean_shift_t_4q_vs_12q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_090_fcf_a_jerk_mean_shift_t_4q_vs_12q_d1},
    "f36_cbjk_091_ncfo_jerk_variance_jump_4q_vs_12q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_091_ncfo_jerk_variance_jump_4q_vs_12q_d1},
    "f36_cbjk_092_fcf_jerk_variance_jump_4q_vs_12q_d1": {"inputs": ["fcf"], "func": f36_cbjk_092_fcf_jerk_variance_jump_4q_vs_12q_d1},
    "f36_cbjk_093_cashneq_jerk_variance_jump_4q_vs_12q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_093_cashneq_jerk_variance_jump_4q_vs_12q_d1},
    "f36_cbjk_094_ncfo_a_jerk_variance_jump_4q_vs_12q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_094_ncfo_a_jerk_variance_jump_4q_vs_12q_d1},
    "f36_cbjk_095_fcf_a_jerk_variance_jump_4q_vs_12q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_095_fcf_a_jerk_variance_jump_4q_vs_12q_d1},
    "f36_cbjk_096_ncfo_jerk_ar1_persistence_8q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_096_ncfo_jerk_ar1_persistence_8q_d1},
    "f36_cbjk_097_fcf_jerk_ar1_persistence_8q_d1": {"inputs": ["fcf"], "func": f36_cbjk_097_fcf_jerk_ar1_persistence_8q_d1},
    "f36_cbjk_098_cashneq_jerk_ar1_persistence_8q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_098_cashneq_jerk_ar1_persistence_8q_d1},
    "f36_cbjk_099_ncfo_a_jerk_ar1_persistence_8q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_099_ncfo_a_jerk_ar1_persistence_8q_d1},
    "f36_cbjk_100_fcf_a_jerk_ar1_persistence_8q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_100_fcf_a_jerk_ar1_persistence_8q_d1},
    "f36_cbjk_101_ncfo_jerk_ema_fast_minus_slow_div_d1": {"inputs": ["ncfo"], "func": f36_cbjk_101_ncfo_jerk_ema_fast_minus_slow_div_d1},
    "f36_cbjk_102_fcf_jerk_ema_fast_minus_slow_div_d1": {"inputs": ["fcf"], "func": f36_cbjk_102_fcf_jerk_ema_fast_minus_slow_div_d1},
    "f36_cbjk_103_cashneq_jerk_ema_fast_minus_slow_div_d1": {"inputs": ["cashneq"], "func": f36_cbjk_103_cashneq_jerk_ema_fast_minus_slow_div_d1},
    "f36_cbjk_104_ncfo_a_jerk_ema_fast_minus_slow_div_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_104_ncfo_a_jerk_ema_fast_minus_slow_div_d1},
    "f36_cbjk_105_fcf_a_jerk_ema_fast_minus_slow_div_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_105_fcf_a_jerk_ema_fast_minus_slow_div_d1},
    "f36_cbjk_106_ncfo_jerk_ulcer_index_neg_8q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_106_ncfo_jerk_ulcer_index_neg_8q_d1},
    "f36_cbjk_107_fcf_jerk_ulcer_index_neg_8q_d1": {"inputs": ["fcf"], "func": f36_cbjk_107_fcf_jerk_ulcer_index_neg_8q_d1},
    "f36_cbjk_108_cashneq_jerk_ulcer_index_neg_8q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_108_cashneq_jerk_ulcer_index_neg_8q_d1},
    "f36_cbjk_109_ncfo_a_jerk_ulcer_index_neg_8q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_109_ncfo_a_jerk_ulcer_index_neg_8q_d1},
    "f36_cbjk_110_fcf_a_jerk_ulcer_index_neg_8q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_110_fcf_a_jerk_ulcer_index_neg_8q_d1},
    "f36_cbjk_111_ncfo_jerk_event_count_below_q10_16q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_111_ncfo_jerk_event_count_below_q10_16q_d1},
    "f36_cbjk_112_fcf_jerk_event_count_below_q10_16q_d1": {"inputs": ["fcf"], "func": f36_cbjk_112_fcf_jerk_event_count_below_q10_16q_d1},
    "f36_cbjk_113_cashneq_jerk_event_count_below_q10_16q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_113_cashneq_jerk_event_count_below_q10_16q_d1},
    "f36_cbjk_114_ncfo_a_jerk_event_count_below_q10_16q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_114_ncfo_a_jerk_event_count_below_q10_16q_d1},
    "f36_cbjk_115_fcf_a_jerk_event_count_below_q10_16q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_115_fcf_a_jerk_event_count_below_q10_16q_d1},
    "f36_cbjk_116_ncfo_jerk_decline_streak_max_16q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_116_ncfo_jerk_decline_streak_max_16q_d1},
    "f36_cbjk_117_fcf_jerk_decline_streak_max_16q_d1": {"inputs": ["fcf"], "func": f36_cbjk_117_fcf_jerk_decline_streak_max_16q_d1},
    "f36_cbjk_118_cashneq_jerk_decline_streak_max_16q_d1": {"inputs": ["cashneq"], "func": f36_cbjk_118_cashneq_jerk_decline_streak_max_16q_d1},
    "f36_cbjk_119_ncfo_a_jerk_decline_streak_max_16q_d1": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_119_ncfo_a_jerk_decline_streak_max_16q_d1},
    "f36_cbjk_120_fcf_a_jerk_decline_streak_max_16q_d1": {"inputs": ["fcf", "assets"], "func": f36_cbjk_120_fcf_a_jerk_decline_streak_max_16q_d1},
    "f36_cbjk_121_ncfo_jerk_simultaneous_break_with_capex_8q_d1": {"inputs": ["ncfo", "capex"], "func": f36_cbjk_121_ncfo_jerk_simultaneous_break_with_capex_8q_d1},
    "f36_cbjk_122_fcf_jerk_runway_cliff_detector_8q_d1": {"inputs": ["fcf", "cashneq"], "func": f36_cbjk_122_fcf_jerk_runway_cliff_detector_8q_d1},
    "f36_cbjk_123_cashneq_jerk_with_debt_rise_8q_d1": {"inputs": ["cashneq", "debt"], "func": f36_cbjk_123_cashneq_jerk_with_debt_rise_8q_d1},
    "f36_cbjk_124_ncfo_to_assets_jerk_during_revenue_decel_8q_d1": {"inputs": ["ncfo", "assets", "revenue"], "func": f36_cbjk_124_ncfo_to_assets_jerk_during_revenue_decel_8q_d1},
    "f36_cbjk_125_fcf_to_assets_jerk_with_dilution_event_8q_d1": {"inputs": ["fcf", "assets", "sharesbas"], "func": f36_cbjk_125_fcf_to_assets_jerk_with_dilution_event_8q_d1},
    "f36_cbjk_126_ncfo_fcf_jerk_both_neg_count_8q_d1": {"inputs": ["ncfo", "fcf"], "func": f36_cbjk_126_ncfo_fcf_jerk_both_neg_count_8q_d1},
    "f36_cbjk_127_ncfo_fcf_cashneq_jerk_all_neg_count_12q_d1": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f36_cbjk_127_ncfo_fcf_cashneq_jerk_all_neg_count_12q_d1},
    "f36_cbjk_128_triple_flow_jerk_concordance_count_8q_d1": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f36_cbjk_128_triple_flow_jerk_concordance_count_8q_d1},
    "f36_cbjk_129_triple_flow_jerk_dispersion_z_8q_d1": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f36_cbjk_129_triple_flow_jerk_dispersion_z_8q_d1},
    "f36_cbjk_130_triple_flow_jerk_compound_score_signed_8q_d1": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f36_cbjk_130_triple_flow_jerk_compound_score_signed_8q_d1},
    "f36_cbjk_131_ncfo_jerk_minus_revenue_jerk_z_8q_d1": {"inputs": ["ncfo", "revenue"], "func": f36_cbjk_131_ncfo_jerk_minus_revenue_jerk_z_8q_d1},
    "f36_cbjk_132_fcf_jerk_minus_ebitda_jerk_z_8q_d1": {"inputs": ["fcf", "ebitda"], "func": f36_cbjk_132_fcf_jerk_minus_ebitda_jerk_z_8q_d1},
    "f36_cbjk_133_ncfo_to_netinc_ratio_jerk_z_8q_d1": {"inputs": ["ncfo", "netinc"], "func": f36_cbjk_133_ncfo_to_netinc_ratio_jerk_z_8q_d1},
    "f36_cbjk_134_fcf_to_revenue_ratio_jerk_z_8q_d1": {"inputs": ["fcf", "revenue"], "func": f36_cbjk_134_fcf_to_revenue_ratio_jerk_z_8q_d1},
    "f36_cbjk_135_capex_to_revenue_jerk_z_8q_d1": {"inputs": ["capex", "revenue"], "func": f36_cbjk_135_capex_to_revenue_jerk_z_8q_d1},
    "f36_cbjk_136_capex_to_depamor_jerk_z_8q_d1": {"inputs": ["capex", "depamor"], "func": f36_cbjk_136_capex_to_depamor_jerk_z_8q_d1},
    "f36_cbjk_137_ncfo_minus_capex_jerk_z_8q_d1": {"inputs": ["ncfo", "capex"], "func": f36_cbjk_137_ncfo_minus_capex_jerk_z_8q_d1},
    "f36_cbjk_138_financing_cash_inflow_jerk_indicator_8q_d1": {"inputs": ["ncff"], "func": f36_cbjk_138_financing_cash_inflow_jerk_indicator_8q_d1},
    "f36_cbjk_139_financing_cash_inflow_jerk_count_12q_d1": {"inputs": ["ncff"], "func": f36_cbjk_139_financing_cash_inflow_jerk_count_12q_d1},
    "f36_cbjk_140_cashneq_jerk_with_ncff_inflow_co_indicator_8q_d1": {"inputs": ["cashneq", "ncff"], "func": f36_cbjk_140_cashneq_jerk_with_ncff_inflow_co_indicator_8q_d1},
    "f36_cbjk_141_ncfo_jerk_with_neg_ncfo_level_co_indicator_8q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_141_ncfo_jerk_with_neg_ncfo_level_co_indicator_8q_d1},
    "f36_cbjk_142_conditional_fcf_jerk_given_cashneq_q10_8q_d1": {"inputs": ["fcf", "cashneq"], "func": f36_cbjk_142_conditional_fcf_jerk_given_cashneq_q10_8q_d1},
    "f36_cbjk_143_conditional_ncfo_jerk_given_yoy_rev_neg_8q_d1": {"inputs": ["ncfo", "revenue"], "func": f36_cbjk_143_conditional_ncfo_jerk_given_yoy_rev_neg_8q_d1},
    "f36_cbjk_144_composite_cash_burn_jerk_fragility_5flow_8q_d1": {"inputs": ["ncfo", "fcf", "cashneq", "assets"], "func": f36_cbjk_144_composite_cash_burn_jerk_fragility_5flow_8q_d1},
    "f36_cbjk_145_weighted_multi_flow_jerk_crash_z_clipm3_8q_d1": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f36_cbjk_145_weighted_multi_flow_jerk_crash_z_clipm3_8q_d1},
    "f36_cbjk_146_multi_horizon_jerk_crash_score_fcf_d1": {"inputs": ["fcf"], "func": f36_cbjk_146_multi_horizon_jerk_crash_score_fcf_d1},
    "f36_cbjk_147_ewm_decay_jerk_crash_8q_ncfo_neg_d1": {"inputs": ["ncfo"], "func": f36_cbjk_147_ewm_decay_jerk_crash_8q_ncfo_neg_d1},
    "f36_cbjk_148_logit_cash_burn_jerk_probability_fcf_d1": {"inputs": ["fcf"], "func": f36_cbjk_148_logit_cash_burn_jerk_probability_fcf_d1},
    "f36_cbjk_149_mahalanobis_ncfo_jerk_slope_8q_d1": {"inputs": ["ncfo"], "func": f36_cbjk_149_mahalanobis_ncfo_jerk_slope_8q_d1},
    "f36_cbjk_150_cash_burn_jerk_aggregate_score_d1": {"inputs": ["ncfo", "fcf", "cashneq", "ncff"], "func": f36_cbjk_150_cash_burn_jerk_aggregate_score_d1},
}
