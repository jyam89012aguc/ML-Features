"""short_interest_structure D1 features 076_150 — order-1 derivative wrappers.

Each function inlines the corresponding base computation and appends .diff()
1 times to produce the k-th derivative of that signal. Inputs and PIT
discipline are identical to __base__076_150.py.
NaN-stub policy: all-NaN inputs return pd.Series(np.nan, index=input.index).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _winsorize(s, lower=0.01, upper=0.99, window=252, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    lo = s.rolling(window, min_periods=min_periods).quantile(lower)
    hi = s.rolling(window, min_periods=min_periods).quantile(upper)
    return s.clip(lower=lo, upper=hi)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _all_nan_stub(*series):
    base = next((x for x in series if isinstance(x, pd.Series)), None)
    if base is None:
        return None
    if all(isinstance(x, pd.Series) and x.isna().all() for x in series):
        return pd.Series(np.nan, index=base.index)
    return None


# ============================================================
#               D1 FEATURES 076_150
# ============================================================


def f16_sint_076_corr_log_si_log_close_252d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_log(shortinterest).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(close))).diff()


def f16_sint_077_corr_log_si_log_close_1260d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_log(shortinterest).rolling(1260, min_periods=YDAYS).corr(_safe_log(close))).diff()


def f16_sint_078_corr_si_volume_252d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(volume)).diff()


def f16_sint_079_corr_dtc_volume_252d_d1(daystocover: pd.Series, volume: pd.Series) -> pd.Series:
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).corr(volume)).diff()


def f16_sint_080_corr_si_to_float_close_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series, close: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_f.rolling(YDAYS, min_periods=QDAYS).corr(close)).diff()


def f16_sint_081_si_mean_to_median_ratio_252d_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    md = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(m, md)).diff()


def f16_sint_082_si_mean_to_median_ratio_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    md = shortinterest.rolling(1260, min_periods=YDAYS).median()
    return (_safe_div(m, md)).diff()


def f16_sint_083_dtc_mean_to_median_ratio_252d_d1(daystocover: pd.Series) -> pd.Series:
    m = daystocover.rolling(YDAYS, min_periods=QDAYS).mean()
    md = daystocover.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(m, md)).diff()


def f16_sint_084_log_si_mean_to_median_ratio_252d_d1(shortinterest: pd.Series) -> pd.Series:
    ls = _safe_log(shortinterest)
    m = ls.rolling(YDAYS, min_periods=QDAYS).mean()
    md = ls.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(m, md)).diff()


def f16_sint_085_si_skew_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).skew()).diff()


def f16_sint_086_si_skew_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(1260, min_periods=YDAYS).skew()).diff()


def f16_sint_087_dtc_skew_252d_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).skew()).diff()


def f16_sint_088_dtc_skew_1260d_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.rolling(1260, min_periods=YDAYS).skew()).diff()


def f16_sint_089_si_to_5y_median_d1(shortinterest: pd.Series) -> pd.Series:
    med = shortinterest.rolling(1260, min_periods=YDAYS).median()
    return (_safe_div(shortinterest, med)).diff()


def f16_sint_090_si_to_5y_mean_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    return (_safe_div(shortinterest, m)).diff()


def f16_sint_091_si_to_5y_max_d1(shortinterest: pd.Series) -> pd.Series:
    rmax = shortinterest.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(shortinterest, rmax)).diff()


def f16_sint_092_dtc_to_5y_median_d1(daystocover: pd.Series) -> pd.Series:
    med = daystocover.rolling(1260, min_periods=YDAYS).median()
    return (_safe_div(daystocover, med)).diff()


def f16_sint_093_dtc_to_5y_max_d1(daystocover: pd.Series) -> pd.Series:
    rmax = daystocover.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(daystocover, rmax)).diff()


def f16_sint_094_si_to_float_to_5y_median_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    med = si_f.rolling(1260, min_periods=YDAYS).median()
    return (_safe_div(si_f, med)).diff()


def f16_sint_095_squeeze_risk_dtc_x_sipct_d1(shortinterest: pd.Series, daystocover: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    si_pct = _rolling_rank_pct(shortinterest, YDAYS)
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    log_dv = _safe_log(dv)
    return (_safe_div(daystocover * si_pct, 1.0 + log_dv.abs())).diff()


def f16_sint_096_squeeze_risk_log_dtc_x_si_float_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (np.log1p(daystocover.clip(lower=0)) * si_f).diff()


def f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    dtc_z = _rolling_zscore(daystocover, YDAYS)
    return (dtc_z * si_f).diff()


def f16_sint_098_short_stress_composite_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    z_si = _rolling_zscore(shortinterest, YDAYS)
    z_dtc = _rolling_zscore(daystocover, YDAYS)
    z_sif = _rolling_zscore(si_f, YDAYS)
    return ((z_si + z_dtc + z_sif) / 3.0).diff()


def f16_sint_099_short_stress_composite_1260d_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    z_si = _rolling_zscore(shortinterest, 1260)
    z_dtc = _rolling_zscore(daystocover, 1260)
    z_sif = _rolling_zscore(si_f, 1260)
    return ((z_si + z_dtc + z_sif) / 3.0).diff()


def f16_sint_100_short_crowdedness_score_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_pct = _rolling_rank_pct(shortinterest, YDAYS)
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_pct * si_f * np.log1p(daystocover.clip(lower=0))).diff()


def f16_sint_101_short_extremity_score_252d_d1(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    a = _rolling_rank_pct(shortinterest, YDAYS)
    b = _rolling_rank_pct(daystocover, YDAYS)
    return (pd.concat([a, b], axis=1).max(axis=1)).diff()


def f16_sint_102_short_extremity_score_1260d_d1(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    a = _rolling_rank_pct(shortinterest, 1260)
    b = _rolling_rank_pct(daystocover, 1260)
    return (pd.concat([a, b], axis=1).max(axis=1)).diff()


def f16_sint_103_si_extreme_crowded_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_104_si_extreme_crowded_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_105_dtc_extreme_crowded_252d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, YDAYS)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_106_dtc_extreme_crowded_1260d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, 1260)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_107_si_above_2sd_state_252d_d1(shortinterest: pd.Series) -> pd.Series:
    z = _rolling_zscore(shortinterest, YDAYS)
    return ((z >= 2.0).astype(float).where(z.notna(), np.nan)).diff()


def f16_sint_108_dtc_above_2sd_state_252d_d1(daystocover: pd.Series) -> pd.Series:
    z = _rolling_zscore(daystocover, YDAYS)
    return ((z >= 2.0).astype(float).where(z.notna(), np.nan)).diff()


def f16_sint_109_si_to_float_extreme_state_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    pct = _rolling_rank_pct(si_f, YDAYS)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_110_si_to_float_extreme_state_1260d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    pct = _rolling_rank_pct(si_f, 1260)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_111_dtc_x_float_extreme_state_252d_d1(daystocover: pd.Series, sharesbas: pd.Series) -> pd.Series:
    ratio = _safe_div(daystocover, sharesbas)
    pct = _rolling_rank_pct(ratio, YDAYS)
    return ((pct >= 0.95).astype(float).where(pct.notna(), np.nan)).diff()


def f16_sint_112_combined_extreme_regime_252d_d1(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    a = _rolling_rank_pct(shortinterest, YDAYS)
    b = _rolling_rank_pct(daystocover, YDAYS)
    out = ((a >= 0.95) & (b >= 0.95)).astype(float)
    return (out.where(a.notna() & b.notna(), np.nan)).diff()


def f16_sint_113_si_delta_autocorr_lag1_252d_d1(shortinterest: pd.Series) -> pd.Series:
    d = shortinterest.diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))).diff()


def f16_sint_114_si_delta_autocorr_lag5_252d_d1(shortinterest: pd.Series) -> pd.Series:
    d = shortinterest.diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(5))).diff()


def f16_sint_115_si_delta_autocorr_lag21_252d_d1(shortinterest: pd.Series) -> pd.Series:
    d = shortinterest.diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(21))).diff()


def f16_sint_116_dtc_delta_autocorr_lag1_252d_d1(daystocover: pd.Series) -> pd.Series:
    d = daystocover.diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))).diff()


def f16_sint_117_log_si_delta_autocorr_lag1_252d_d1(shortinterest: pd.Series) -> pd.Series:
    d = _safe_log(shortinterest).diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))).diff()


def f16_sint_118_log_si_delta_autocorr_lag5_252d_d1(shortinterest: pd.Series) -> pd.Series:
    d = _safe_log(shortinterest).diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(5))).diff()


def f16_sint_119_si_to_float_delta_autocorr_lag1_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    d = si_f.diff()
    return (d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))).diff()


def f16_sint_120_si_persistence_acf_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(21))).diff()


def f16_sint_121_si_dollar_exposure_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (shortinterest * close).diff()


def f16_sint_122_log_si_dollar_exposure_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_log(shortinterest * close)).diff()


def f16_sint_123_si_dollar_exposure_to_mcap_proxy_d1(shortinterest: pd.Series, close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    num = shortinterest * close
    den = sharesbas * close
    return (_safe_div(num, den)).diff()


def f16_sint_124_si_dollar_exposure_rank_pct_252d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(shortinterest * close, YDAYS)).diff()


def f16_sint_125_si_dollar_exposure_zscore_252d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest * close, YDAYS)).diff()


def f16_sint_126_si_dollar_to_avg_dollar_volume_21d_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return (_safe_div(shortinterest * close, dv)).diff()


def f16_sint_127_si_rank_stability_corr_63d_lag5_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(QDAYS, min_periods=MDAYS).corr(shortinterest.shift(5))).diff()


def f16_sint_128_si_rank_stability_corr_252d_lag21_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(21))).diff()


def f16_sint_129_dtc_rank_stability_corr_252d_lag21_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).corr(daystocover.shift(21))).diff()


def f16_sint_130_si_self_corr_lag63_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(QDAYS))).diff()


def f16_sint_131_si_to_avg_volume_252d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    avgv = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(shortinterest, avgv)).diff()


def f16_sint_132_si_to_volume_today_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return (_safe_div(shortinterest, volume)).diff()


def f16_sint_133_si_to_avg_dollar_volume_63d_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(shortinterest, dv)).diff()


def f16_sint_134_si_to_avg_dollar_volume_252d_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(shortinterest, dv)).diff()


def f16_sint_135_log_si_to_avg_volume_21d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return (_safe_log(_safe_div(shortinterest, avgv))).diff()


def f16_sint_136_si_to_volume_zscore_252d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    ratio = _safe_div(shortinterest, avgv)
    return (_rolling_zscore(ratio, YDAYS)).diff()


def f16_sint_137_si_to_float_log_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_log(_safe_div(shortinterest, sharesbas))).diff()


def f16_sint_138_si_to_float_winsorized_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_winsorize(si_f, 0.01, 0.99, YDAYS)).diff()


def f16_sint_139_si_to_float_capped_at_1_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_f.clip(lower=0.0, upper=1.0)).diff()


def f16_sint_140_one_minus_si_to_float_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas).clip(lower=0.0, upper=1.0)
    return (1.0 - si_f).diff()


def f16_sint_141_si_to_float_squared_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_f ** 2).diff()


def f16_sint_142_si_to_float_x_dtc_composite_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_f * daystocover).diff()


def f16_sint_143_zscore_composite_si_dtc_252d_d1(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest, YDAYS) + _rolling_zscore(daystocover, YDAYS)).diff()


def f16_sint_144_zscore_composite_si_dtc_1260d_d1(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest, 1260) + _rolling_zscore(daystocover, 1260)).diff()


def f16_sint_145_zscore_composite_si_float_dtc_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_rolling_zscore(si_f, YDAYS) + _rolling_zscore(daystocover, YDAYS)).diff()


def f16_sint_146_stress_index_max_of_three_d1(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    a = _rolling_zscore(shortinterest, YDAYS)
    b = _rolling_zscore(daystocover, YDAYS)
    c = _rolling_zscore(si_f, YDAYS)
    return (pd.concat([a, b, c], axis=1).max(axis=1)).diff()


def f16_sint_147_days_since_si_252d_high_d1(shortinterest: pd.Series) -> pd.Series:
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)).diff()


def f16_sint_148_days_since_si_1260d_high_d1(shortinterest: pd.Series) -> pd.Series:
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return (shortinterest.rolling(1260, min_periods=YDAYS).apply(_bsm, raw=True)).diff()


def f16_sint_149_days_since_dtc_252d_high_d1(daystocover: pd.Series) -> pd.Series:
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)).diff()


def f16_sint_150_days_since_si_252d_low_d1(shortinterest: pd.Series) -> pd.Series:
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmin(w))
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)).diff()


# ============================================================
#                     REGISTRY
# ============================================================

SHORT_INTEREST_STRUCTURE_D1_REGISTRY_076_150 = {
    "f16_sint_076_corr_log_si_log_close_252d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_076_corr_log_si_log_close_252d_d1},
    "f16_sint_077_corr_log_si_log_close_1260d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_077_corr_log_si_log_close_1260d_d1},
    "f16_sint_078_corr_si_volume_252d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_078_corr_si_volume_252d_d1},
    "f16_sint_079_corr_dtc_volume_252d_d1": {"inputs": ["daystocover", "volume"], "func": f16_sint_079_corr_dtc_volume_252d_d1},
    "f16_sint_080_corr_si_to_float_close_252d_d1": {"inputs": ["shortinterest", "sharesbas", "close"], "func": f16_sint_080_corr_si_to_float_close_252d_d1},
    "f16_sint_081_si_mean_to_median_ratio_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_081_si_mean_to_median_ratio_252d_d1},
    "f16_sint_082_si_mean_to_median_ratio_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_082_si_mean_to_median_ratio_1260d_d1},
    "f16_sint_083_dtc_mean_to_median_ratio_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_083_dtc_mean_to_median_ratio_252d_d1},
    "f16_sint_084_log_si_mean_to_median_ratio_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_084_log_si_mean_to_median_ratio_252d_d1},
    "f16_sint_085_si_skew_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_085_si_skew_252d_d1},
    "f16_sint_086_si_skew_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_086_si_skew_1260d_d1},
    "f16_sint_087_dtc_skew_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_087_dtc_skew_252d_d1},
    "f16_sint_088_dtc_skew_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_088_dtc_skew_1260d_d1},
    "f16_sint_089_si_to_5y_median_d1": {"inputs": ["shortinterest"], "func": f16_sint_089_si_to_5y_median_d1},
    "f16_sint_090_si_to_5y_mean_d1": {"inputs": ["shortinterest"], "func": f16_sint_090_si_to_5y_mean_d1},
    "f16_sint_091_si_to_5y_max_d1": {"inputs": ["shortinterest"], "func": f16_sint_091_si_to_5y_max_d1},
    "f16_sint_092_dtc_to_5y_median_d1": {"inputs": ["daystocover"], "func": f16_sint_092_dtc_to_5y_median_d1},
    "f16_sint_093_dtc_to_5y_max_d1": {"inputs": ["daystocover"], "func": f16_sint_093_dtc_to_5y_max_d1},
    "f16_sint_094_si_to_float_to_5y_median_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_094_si_to_float_to_5y_median_d1},
    "f16_sint_095_squeeze_risk_dtc_x_sipct_d1": {"inputs": ["shortinterest", "daystocover", "close", "volume"], "func": f16_sint_095_squeeze_risk_dtc_x_sipct_d1},
    "f16_sint_096_squeeze_risk_log_dtc_x_si_float_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_096_squeeze_risk_log_dtc_x_si_float_d1},
    "f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float_d1},
    "f16_sint_098_short_stress_composite_252d_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_098_short_stress_composite_252d_d1},
    "f16_sint_099_short_stress_composite_1260d_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_099_short_stress_composite_1260d_d1},
    "f16_sint_100_short_crowdedness_score_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_100_short_crowdedness_score_d1},
    "f16_sint_101_short_extremity_score_252d_d1": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_101_short_extremity_score_252d_d1},
    "f16_sint_102_short_extremity_score_1260d_d1": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_102_short_extremity_score_1260d_d1},
    "f16_sint_103_si_extreme_crowded_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_103_si_extreme_crowded_252d_d1},
    "f16_sint_104_si_extreme_crowded_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_104_si_extreme_crowded_1260d_d1},
    "f16_sint_105_dtc_extreme_crowded_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_105_dtc_extreme_crowded_252d_d1},
    "f16_sint_106_dtc_extreme_crowded_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_106_dtc_extreme_crowded_1260d_d1},
    "f16_sint_107_si_above_2sd_state_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_107_si_above_2sd_state_252d_d1},
    "f16_sint_108_dtc_above_2sd_state_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_108_dtc_above_2sd_state_252d_d1},
    "f16_sint_109_si_to_float_extreme_state_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_109_si_to_float_extreme_state_252d_d1},
    "f16_sint_110_si_to_float_extreme_state_1260d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_110_si_to_float_extreme_state_1260d_d1},
    "f16_sint_111_dtc_x_float_extreme_state_252d_d1": {"inputs": ["daystocover", "sharesbas"], "func": f16_sint_111_dtc_x_float_extreme_state_252d_d1},
    "f16_sint_112_combined_extreme_regime_252d_d1": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_112_combined_extreme_regime_252d_d1},
    "f16_sint_113_si_delta_autocorr_lag1_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_113_si_delta_autocorr_lag1_252d_d1},
    "f16_sint_114_si_delta_autocorr_lag5_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_114_si_delta_autocorr_lag5_252d_d1},
    "f16_sint_115_si_delta_autocorr_lag21_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_115_si_delta_autocorr_lag21_252d_d1},
    "f16_sint_116_dtc_delta_autocorr_lag1_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_116_dtc_delta_autocorr_lag1_252d_d1},
    "f16_sint_117_log_si_delta_autocorr_lag1_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_117_log_si_delta_autocorr_lag1_252d_d1},
    "f16_sint_118_log_si_delta_autocorr_lag5_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_118_log_si_delta_autocorr_lag5_252d_d1},
    "f16_sint_119_si_to_float_delta_autocorr_lag1_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_119_si_to_float_delta_autocorr_lag1_252d_d1},
    "f16_sint_120_si_persistence_acf_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_120_si_persistence_acf_252d_d1},
    "f16_sint_121_si_dollar_exposure_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_121_si_dollar_exposure_d1},
    "f16_sint_122_log_si_dollar_exposure_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_122_log_si_dollar_exposure_d1},
    "f16_sint_123_si_dollar_exposure_to_mcap_proxy_d1": {"inputs": ["shortinterest", "close", "sharesbas"], "func": f16_sint_123_si_dollar_exposure_to_mcap_proxy_d1},
    "f16_sint_124_si_dollar_exposure_rank_pct_252d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_124_si_dollar_exposure_rank_pct_252d_d1},
    "f16_sint_125_si_dollar_exposure_zscore_252d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_125_si_dollar_exposure_zscore_252d_d1},
    "f16_sint_126_si_dollar_to_avg_dollar_volume_21d_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_126_si_dollar_to_avg_dollar_volume_21d_d1},
    "f16_sint_127_si_rank_stability_corr_63d_lag5_d1": {"inputs": ["shortinterest"], "func": f16_sint_127_si_rank_stability_corr_63d_lag5_d1},
    "f16_sint_128_si_rank_stability_corr_252d_lag21_d1": {"inputs": ["shortinterest"], "func": f16_sint_128_si_rank_stability_corr_252d_lag21_d1},
    "f16_sint_129_dtc_rank_stability_corr_252d_lag21_d1": {"inputs": ["daystocover"], "func": f16_sint_129_dtc_rank_stability_corr_252d_lag21_d1},
    "f16_sint_130_si_self_corr_lag63_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_130_si_self_corr_lag63_252d_d1},
    "f16_sint_131_si_to_avg_volume_252d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_131_si_to_avg_volume_252d_d1},
    "f16_sint_132_si_to_volume_today_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_132_si_to_volume_today_d1},
    "f16_sint_133_si_to_avg_dollar_volume_63d_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_133_si_to_avg_dollar_volume_63d_d1},
    "f16_sint_134_si_to_avg_dollar_volume_252d_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_134_si_to_avg_dollar_volume_252d_d1},
    "f16_sint_135_log_si_to_avg_volume_21d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_135_log_si_to_avg_volume_21d_d1},
    "f16_sint_136_si_to_volume_zscore_252d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_136_si_to_volume_zscore_252d_d1},
    "f16_sint_137_si_to_float_log_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_137_si_to_float_log_d1},
    "f16_sint_138_si_to_float_winsorized_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_138_si_to_float_winsorized_252d_d1},
    "f16_sint_139_si_to_float_capped_at_1_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_139_si_to_float_capped_at_1_d1},
    "f16_sint_140_one_minus_si_to_float_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_140_one_minus_si_to_float_d1},
    "f16_sint_141_si_to_float_squared_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_141_si_to_float_squared_d1},
    "f16_sint_142_si_to_float_x_dtc_composite_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_142_si_to_float_x_dtc_composite_d1},
    "f16_sint_143_zscore_composite_si_dtc_252d_d1": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_143_zscore_composite_si_dtc_252d_d1},
    "f16_sint_144_zscore_composite_si_dtc_1260d_d1": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_144_zscore_composite_si_dtc_1260d_d1},
    "f16_sint_145_zscore_composite_si_float_dtc_252d_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_145_zscore_composite_si_float_dtc_252d_d1},
    "f16_sint_146_stress_index_max_of_three_d1": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_146_stress_index_max_of_three_d1},
    "f16_sint_147_days_since_si_252d_high_d1": {"inputs": ["shortinterest"], "func": f16_sint_147_days_since_si_252d_high_d1},
    "f16_sint_148_days_since_si_1260d_high_d1": {"inputs": ["shortinterest"], "func": f16_sint_148_days_since_si_1260d_high_d1},
    "f16_sint_149_days_since_dtc_252d_high_d1": {"inputs": ["daystocover"], "func": f16_sint_149_days_since_dtc_252d_high_d1},
    "f16_sint_150_days_since_si_252d_low_d1": {"inputs": ["shortinterest"], "func": f16_sint_150_days_since_si_252d_low_d1},
}
