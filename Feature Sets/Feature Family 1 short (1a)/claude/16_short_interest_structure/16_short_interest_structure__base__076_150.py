"""short_interest_structure base features 076-150 — Pipeline 1a-inverse short-side blowup family.

75 distinct STRUCTURE hypotheses, continued from __base__001_075.py.
Inputs: NSIR (shortinterest, daystocover), SEP (volume, close), SF1 (sharesbas).
NaN-stub policy: all-NaN inputs return pd.Series(np.nan, index=input.index).
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
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
#                BASE FEATURES 076-150
# ============================================================


def f16_sint_076_corr_log_si_log_close_252d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr between log SI and log close — proportional co-movement."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return _safe_log(shortinterest).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(close))


def f16_sint_077_corr_log_si_log_close_1260d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 1260d corr between log SI and log close."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return _safe_log(shortinterest).rolling(1260, min_periods=YDAYS).corr(_safe_log(close))


def f16_sint_078_corr_si_volume_252d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr between SI and volume — flow-with-shorts co-occurrence."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(volume)


def f16_sint_079_corr_dtc_volume_252d(daystocover: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr between DTC and volume."""
    stub = _all_nan_stub(daystocover, volume)
    if stub is not None:
        return stub
    return daystocover.rolling(YDAYS, min_periods=QDAYS).corr(volume)


def f16_sint_080_corr_si_to_float_close_252d(shortinterest: pd.Series, sharesbas: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr between SI/float and close."""
    stub = _all_nan_stub(shortinterest, sharesbas, close)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return si_f.rolling(YDAYS, min_periods=QDAYS).corr(close)


def f16_sint_081_si_mean_to_median_ratio_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d mean/median ratio of SI — distributional skew signal."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    md = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(m, md)


def f16_sint_082_si_mean_to_median_ratio_1260d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 1260d mean/median ratio of SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    md = shortinterest.rolling(1260, min_periods=YDAYS).median()
    return _safe_div(m, md)


def f16_sint_083_dtc_mean_to_median_ratio_252d(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d mean/median ratio of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    m = daystocover.rolling(YDAYS, min_periods=QDAYS).mean()
    md = daystocover.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(m, md)


def f16_sint_084_log_si_mean_to_median_ratio_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d mean/median ratio of log SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    ls = _safe_log(shortinterest)
    m = ls.rolling(YDAYS, min_periods=QDAYS).mean()
    md = ls.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(m, md)


def f16_sint_085_si_skew_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d skewness of SI distribution."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).skew()


def f16_sint_086_si_skew_1260d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 1260d skewness of SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(1260, min_periods=YDAYS).skew()


def f16_sint_087_dtc_skew_252d(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d skewness of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.rolling(YDAYS, min_periods=QDAYS).skew()


def f16_sint_088_dtc_skew_1260d(daystocover: pd.Series) -> pd.Series:
    """Rolling 1260d skewness of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.rolling(1260, min_periods=YDAYS).skew()


def f16_sint_089_si_to_5y_median(shortinterest: pd.Series) -> pd.Series:
    """SI / 5y trailing median — crowdedness ratio."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    med = shortinterest.rolling(1260, min_periods=YDAYS).median()
    return _safe_div(shortinterest, med)


def f16_sint_090_si_to_5y_mean(shortinterest: pd.Series) -> pd.Series:
    """SI / 5y trailing mean."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    return _safe_div(shortinterest, m)


def f16_sint_091_si_to_5y_max(shortinterest: pd.Series) -> pd.Series:
    """SI / 5y trailing max — proximity to historical extreme."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    rmax = shortinterest.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(shortinterest, rmax)


def f16_sint_092_dtc_to_5y_median(daystocover: pd.Series) -> pd.Series:
    """DTC / 5y trailing median."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    med = daystocover.rolling(1260, min_periods=YDAYS).median()
    return _safe_div(daystocover, med)


def f16_sint_093_dtc_to_5y_max(daystocover: pd.Series) -> pd.Series:
    """DTC / 5y trailing max."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    rmax = daystocover.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(daystocover, rmax)


def f16_sint_094_si_to_float_to_5y_median(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """SI/float / 5y trailing median of SI/float."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    med = si_f.rolling(1260, min_periods=YDAYS).median()
    return _safe_div(si_f, med)


def f16_sint_095_squeeze_risk_dtc_x_sipct(shortinterest: pd.Series, daystocover: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """DTC * SI_rank_pct_252d / (1 + log_dollar_volume_21d) — composite squeeze risk."""
    stub = _all_nan_stub(shortinterest, daystocover, close, volume)
    if stub is not None:
        return stub
    si_pct = _rolling_rank_pct(shortinterest, YDAYS)
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    log_dv = _safe_log(dv)
    return _safe_div(daystocover * si_pct, 1.0 + log_dv.abs())


def f16_sint_096_squeeze_risk_log_dtc_x_si_float(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """log(1 + DTC) * SI/float — magnitude-aware squeeze score."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return np.log1p(daystocover.clip(lower=0)) * si_f


def f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """DTC_z(252) * SI/float — relative-extremeness-weighted squeeze score."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    dtc_z = _rolling_zscore(daystocover, YDAYS)
    return dtc_z * si_f


def f16_sint_098_short_stress_composite_252d(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Mean of z_SI, z_DTC, z_SI/float over 252d — joint stress."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    z_si = _rolling_zscore(shortinterest, YDAYS)
    z_dtc = _rolling_zscore(daystocover, YDAYS)
    z_sif = _rolling_zscore(si_f, YDAYS)
    return (z_si + z_dtc + z_sif) / 3.0


def f16_sint_099_short_stress_composite_1260d(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Mean of z_SI, z_DTC, z_SI/float over 1260d."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    z_si = _rolling_zscore(shortinterest, 1260)
    z_dtc = _rolling_zscore(daystocover, 1260)
    z_sif = _rolling_zscore(si_f, 1260)
    return (z_si + z_dtc + z_sif) / 3.0


def f16_sint_100_short_crowdedness_score(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """SI_rank_pct_252d * SI/float * log1p(DTC) — three-factor crowdedness."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_pct = _rolling_rank_pct(shortinterest, YDAYS)
    si_f = _safe_div(shortinterest, sharesbas)
    return si_pct * si_f * np.log1p(daystocover.clip(lower=0))


def f16_sint_101_short_extremity_score_252d(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Max(SI_rank_pct_252d, DTC_rank_pct_252d) — extremity in either dimension."""
    stub = _all_nan_stub(shortinterest, daystocover)
    if stub is not None:
        return stub
    a = _rolling_rank_pct(shortinterest, YDAYS)
    b = _rolling_rank_pct(daystocover, YDAYS)
    return pd.concat([a, b], axis=1).max(axis=1)


def f16_sint_102_short_extremity_score_1260d(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Max(SI_rank_pct_1260d, DTC_rank_pct_1260d)."""
    stub = _all_nan_stub(shortinterest, daystocover)
    if stub is not None:
        return stub
    a = _rolling_rank_pct(shortinterest, 1260)
    b = _rolling_rank_pct(daystocover, 1260)
    return pd.concat([a, b], axis=1).max(axis=1)


def f16_sint_103_si_extreme_crowded_252d(shortinterest: pd.Series) -> pd.Series:
    """Binary regime: 1 when SI rank-pct (252d) >= 0.95."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_104_si_extreme_crowded_1260d(shortinterest: pd.Series) -> pd.Series:
    """Binary regime: 1 when SI rank-pct (1260d) >= 0.95."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_105_dtc_extreme_crowded_252d(daystocover: pd.Series) -> pd.Series:
    """Binary regime: 1 when DTC rank-pct (252d) >= 0.95."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, YDAYS)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_106_dtc_extreme_crowded_1260d(daystocover: pd.Series) -> pd.Series:
    """Binary regime: 1 when DTC rank-pct (1260d) >= 0.95."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, 1260)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_107_si_above_2sd_state_252d(shortinterest: pd.Series) -> pd.Series:
    """1 when SI z(252d) >= 2.0 — tail-event regime."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    z = _rolling_zscore(shortinterest, YDAYS)
    return (z >= 2.0).astype(float).where(z.notna(), np.nan)


def f16_sint_108_dtc_above_2sd_state_252d(daystocover: pd.Series) -> pd.Series:
    """1 when DTC z(252d) >= 2.0."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    z = _rolling_zscore(daystocover, YDAYS)
    return (z >= 2.0).astype(float).where(z.notna(), np.nan)


def f16_sint_109_si_to_float_extreme_state_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """1 when SI/float rank-pct (252d) >= 0.95."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    pct = _rolling_rank_pct(si_f, YDAYS)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_110_si_to_float_extreme_state_1260d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """1 when SI/float rank-pct (1260d) >= 0.95."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    pct = _rolling_rank_pct(si_f, 1260)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_111_dtc_x_float_extreme_state_252d(daystocover: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """1 when DTC/sharesbas rank-pct (252d) >= 0.95 — DTC adjusted for float size regime."""
    stub = _all_nan_stub(daystocover, sharesbas)
    if stub is not None:
        return stub
    ratio = _safe_div(daystocover, sharesbas)
    pct = _rolling_rank_pct(ratio, YDAYS)
    return (pct >= 0.95).astype(float).where(pct.notna(), np.nan)


def f16_sint_112_combined_extreme_regime_252d(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    """1 when BOTH SI and DTC are in 95th pct (252d) — combined extreme."""
    stub = _all_nan_stub(shortinterest, daystocover)
    if stub is not None:
        return stub
    a = _rolling_rank_pct(shortinterest, YDAYS)
    b = _rolling_rank_pct(daystocover, YDAYS)
    out = ((a >= 0.95) & (b >= 0.95)).astype(float)
    return out.where(a.notna() & b.notna(), np.nan)


def f16_sint_113_si_delta_autocorr_lag1_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of SI deltas at lag 1 — change-persistence structure."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    d = shortinterest.diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))


def f16_sint_114_si_delta_autocorr_lag5_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of SI deltas at lag 5."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    d = shortinterest.diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(5))


def f16_sint_115_si_delta_autocorr_lag21_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of SI deltas at lag 21."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    d = shortinterest.diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(21))


def f16_sint_116_dtc_delta_autocorr_lag1_252d(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of DTC deltas at lag 1."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    d = daystocover.diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))


def f16_sint_117_log_si_delta_autocorr_lag1_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of log-SI deltas at lag 1."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    d = _safe_log(shortinterest).diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))


def f16_sint_118_log_si_delta_autocorr_lag5_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of log-SI deltas at lag 5."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    d = _safe_log(shortinterest).diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(5))


def f16_sint_119_si_to_float_delta_autocorr_lag1_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of SI/float deltas at lag 1."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    d = si_f.diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))


def f16_sint_120_si_persistence_acf_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d autocorr of SI levels at lag 21 — level-persistence."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(21))


def f16_sint_121_si_dollar_exposure(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """SI shares * close = dollar value of short exposure."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return shortinterest * close


def f16_sint_122_log_si_dollar_exposure(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """log(SI * close) — log dollar short exposure."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return _safe_log(shortinterest * close)


def f16_sint_123_si_dollar_exposure_to_mcap_proxy(shortinterest: pd.Series, close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """(SI * close) / (sharesbas * close) = SI / sharesbas — short exposure share of mcap."""
    stub = _all_nan_stub(shortinterest, close, sharesbas)
    if stub is not None:
        return stub
    num = shortinterest * close
    den = sharesbas * close
    return _safe_div(num, den)


def f16_sint_124_si_dollar_exposure_rank_pct_252d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rank-pct of dollar SI exposure within own 252d window."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return _rolling_rank_pct(shortinterest * close, YDAYS)


def f16_sint_125_si_dollar_exposure_zscore_252d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of dollar SI exposure within own 252d window."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest * close, YDAYS)


def f16_sint_126_si_dollar_to_avg_dollar_volume_21d(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(SI * close) / avg 21d (close * volume) — dollar-DTC."""
    stub = _all_nan_stub(shortinterest, close, volume)
    if stub is not None:
        return stub
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return _safe_div(shortinterest * close, dv)


def f16_sint_127_si_rank_stability_corr_63d_lag5(shortinterest: pd.Series) -> pd.Series:
    """Rolling 63d Pearson corr between SI(t) and SI(t-5) — short-horizon stability."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(QDAYS, min_periods=MDAYS).corr(shortinterest.shift(5))


def f16_sint_128_si_rank_stability_corr_252d_lag21(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d Pearson corr between SI(t) and SI(t-21)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(21))


def f16_sint_129_dtc_rank_stability_corr_252d_lag21(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d Pearson corr between DTC(t) and DTC(t-21)."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.rolling(YDAYS, min_periods=QDAYS).corr(daystocover.shift(21))


def f16_sint_130_si_self_corr_lag63_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d corr between SI and SI lagged 63d — quarterly persistence."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(shortinterest.shift(QDAYS))


def f16_sint_131_si_to_avg_volume_252d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """SI divided by 252d avg volume — annual-horizon DTC proxy."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    avgv = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(shortinterest, avgv)


def f16_sint_132_si_to_volume_today(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """SI / today's volume — instantaneous turnover-of-shorts pressure."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    return _safe_div(shortinterest, volume)


def f16_sint_133_si_to_avg_dollar_volume_63d(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """SI shares / 63d avg dollar volume — quarterly dollar-DTC."""
    stub = _all_nan_stub(shortinterest, close, volume)
    if stub is not None:
        return stub
    dv = (close * volume).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(shortinterest, dv)


def f16_sint_134_si_to_avg_dollar_volume_252d(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """SI shares / 252d avg dollar volume."""
    stub = _all_nan_stub(shortinterest, close, volume)
    if stub is not None:
        return stub
    dv = (close * volume).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(shortinterest, dv)


def f16_sint_135_log_si_to_avg_volume_21d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """log(SI / avg21d volume)."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return _safe_log(_safe_div(shortinterest, avgv))


def f16_sint_136_si_to_volume_zscore_252d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of SI / avg21d volume — relative-DTC regime."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    ratio = _safe_div(shortinterest, avgv)
    return _rolling_zscore(ratio, YDAYS)


def f16_sint_137_si_to_float_log(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """log(SI / sharesbas)."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    return _safe_log(_safe_div(shortinterest, sharesbas))


def f16_sint_138_si_to_float_winsorized_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Winsorized SI/float (1-99 pct, 252d)."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _winsorize(si_f, 0.01, 0.99, YDAYS)


def f16_sint_139_si_to_float_capped_at_1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """SI/float clipped at [0, 1] — true utilization bound."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return si_f.clip(lower=0.0, upper=1.0)


def f16_sint_140_one_minus_si_to_float(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """1 - SI/float (capped) — remaining-float slack."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas).clip(lower=0.0, upper=1.0)
    return 1.0 - si_f


def f16_sint_141_si_to_float_squared(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """(SI/float)^2 — nonlinearity in float utilization."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return si_f ** 2


def f16_sint_142_si_to_float_x_dtc_composite(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """(SI/float) * DTC — multiplicative float-utilization-and-illiquidity composite."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return si_f * daystocover


def f16_sint_143_zscore_composite_si_dtc_252d(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Sum of z-scores (252d) of SI and DTC."""
    stub = _all_nan_stub(shortinterest, daystocover)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest, YDAYS) + _rolling_zscore(daystocover, YDAYS)


def f16_sint_144_zscore_composite_si_dtc_1260d(shortinterest: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Sum of z-scores (1260d) of SI and DTC."""
    stub = _all_nan_stub(shortinterest, daystocover)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest, 1260) + _rolling_zscore(daystocover, 1260)


def f16_sint_145_zscore_composite_si_float_dtc_252d(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """z_SI/float(252) + z_DTC(252)."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _rolling_zscore(si_f, YDAYS) + _rolling_zscore(daystocover, YDAYS)


def f16_sint_146_stress_index_max_of_three(shortinterest: pd.Series, sharesbas: pd.Series, daystocover: pd.Series) -> pd.Series:
    """Max of z_SI(252), z_DTC(252), z_SI/float(252) — worst-dimension regime."""
    stub = _all_nan_stub(shortinterest, sharesbas, daystocover)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    a = _rolling_zscore(shortinterest, YDAYS)
    b = _rolling_zscore(daystocover, YDAYS)
    c = _rolling_zscore(si_f, YDAYS)
    return pd.concat([a, b, c], axis=1).max(axis=1)


def f16_sint_147_days_since_si_252d_high(shortinterest: pd.Series) -> pd.Series:
    """Bars since SI 252d rolling max — state (not change)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f16_sint_148_days_since_si_1260d_high(shortinterest: pd.Series) -> pd.Series:
    """Bars since SI 1260d rolling max."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return shortinterest.rolling(1260, min_periods=YDAYS).apply(_bsm, raw=True)


def f16_sint_149_days_since_dtc_252d_high(daystocover: pd.Series) -> pd.Series:
    """Bars since DTC 252d rolling max."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return daystocover.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f16_sint_150_days_since_si_252d_low(shortinterest: pd.Series) -> pd.Series:
    """Bars since SI 252d rolling min — state."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return (len(w) - 1) - int(np.nanargmin(w))
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


# ============================================================
#                     REGISTRY
# ============================================================

SHORT_INTEREST_STRUCTURE_BASE_REGISTRY_076_150 = {
    "f16_sint_076_corr_log_si_log_close_252d": {"inputs": ["shortinterest", "close"], "func": f16_sint_076_corr_log_si_log_close_252d},
    "f16_sint_077_corr_log_si_log_close_1260d": {"inputs": ["shortinterest", "close"], "func": f16_sint_077_corr_log_si_log_close_1260d},
    "f16_sint_078_corr_si_volume_252d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_078_corr_si_volume_252d},
    "f16_sint_079_corr_dtc_volume_252d": {"inputs": ["daystocover", "volume"], "func": f16_sint_079_corr_dtc_volume_252d},
    "f16_sint_080_corr_si_to_float_close_252d": {"inputs": ["shortinterest", "sharesbas", "close"], "func": f16_sint_080_corr_si_to_float_close_252d},
    "f16_sint_081_si_mean_to_median_ratio_252d": {"inputs": ["shortinterest"], "func": f16_sint_081_si_mean_to_median_ratio_252d},
    "f16_sint_082_si_mean_to_median_ratio_1260d": {"inputs": ["shortinterest"], "func": f16_sint_082_si_mean_to_median_ratio_1260d},
    "f16_sint_083_dtc_mean_to_median_ratio_252d": {"inputs": ["daystocover"], "func": f16_sint_083_dtc_mean_to_median_ratio_252d},
    "f16_sint_084_log_si_mean_to_median_ratio_252d": {"inputs": ["shortinterest"], "func": f16_sint_084_log_si_mean_to_median_ratio_252d},
    "f16_sint_085_si_skew_252d": {"inputs": ["shortinterest"], "func": f16_sint_085_si_skew_252d},
    "f16_sint_086_si_skew_1260d": {"inputs": ["shortinterest"], "func": f16_sint_086_si_skew_1260d},
    "f16_sint_087_dtc_skew_252d": {"inputs": ["daystocover"], "func": f16_sint_087_dtc_skew_252d},
    "f16_sint_088_dtc_skew_1260d": {"inputs": ["daystocover"], "func": f16_sint_088_dtc_skew_1260d},
    "f16_sint_089_si_to_5y_median": {"inputs": ["shortinterest"], "func": f16_sint_089_si_to_5y_median},
    "f16_sint_090_si_to_5y_mean": {"inputs": ["shortinterest"], "func": f16_sint_090_si_to_5y_mean},
    "f16_sint_091_si_to_5y_max": {"inputs": ["shortinterest"], "func": f16_sint_091_si_to_5y_max},
    "f16_sint_092_dtc_to_5y_median": {"inputs": ["daystocover"], "func": f16_sint_092_dtc_to_5y_median},
    "f16_sint_093_dtc_to_5y_max": {"inputs": ["daystocover"], "func": f16_sint_093_dtc_to_5y_max},
    "f16_sint_094_si_to_float_to_5y_median": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_094_si_to_float_to_5y_median},
    "f16_sint_095_squeeze_risk_dtc_x_sipct": {"inputs": ["shortinterest", "daystocover", "close", "volume"], "func": f16_sint_095_squeeze_risk_dtc_x_sipct},
    "f16_sint_096_squeeze_risk_log_dtc_x_si_float": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_096_squeeze_risk_log_dtc_x_si_float},
    "f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_097_squeeze_risk_dtc_zscore_x_si_to_float},
    "f16_sint_098_short_stress_composite_252d": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_098_short_stress_composite_252d},
    "f16_sint_099_short_stress_composite_1260d": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_099_short_stress_composite_1260d},
    "f16_sint_100_short_crowdedness_score": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_100_short_crowdedness_score},
    "f16_sint_101_short_extremity_score_252d": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_101_short_extremity_score_252d},
    "f16_sint_102_short_extremity_score_1260d": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_102_short_extremity_score_1260d},
    "f16_sint_103_si_extreme_crowded_252d": {"inputs": ["shortinterest"], "func": f16_sint_103_si_extreme_crowded_252d},
    "f16_sint_104_si_extreme_crowded_1260d": {"inputs": ["shortinterest"], "func": f16_sint_104_si_extreme_crowded_1260d},
    "f16_sint_105_dtc_extreme_crowded_252d": {"inputs": ["daystocover"], "func": f16_sint_105_dtc_extreme_crowded_252d},
    "f16_sint_106_dtc_extreme_crowded_1260d": {"inputs": ["daystocover"], "func": f16_sint_106_dtc_extreme_crowded_1260d},
    "f16_sint_107_si_above_2sd_state_252d": {"inputs": ["shortinterest"], "func": f16_sint_107_si_above_2sd_state_252d},
    "f16_sint_108_dtc_above_2sd_state_252d": {"inputs": ["daystocover"], "func": f16_sint_108_dtc_above_2sd_state_252d},
    "f16_sint_109_si_to_float_extreme_state_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_109_si_to_float_extreme_state_252d},
    "f16_sint_110_si_to_float_extreme_state_1260d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_110_si_to_float_extreme_state_1260d},
    "f16_sint_111_dtc_x_float_extreme_state_252d": {"inputs": ["daystocover", "sharesbas"], "func": f16_sint_111_dtc_x_float_extreme_state_252d},
    "f16_sint_112_combined_extreme_regime_252d": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_112_combined_extreme_regime_252d},
    "f16_sint_113_si_delta_autocorr_lag1_252d": {"inputs": ["shortinterest"], "func": f16_sint_113_si_delta_autocorr_lag1_252d},
    "f16_sint_114_si_delta_autocorr_lag5_252d": {"inputs": ["shortinterest"], "func": f16_sint_114_si_delta_autocorr_lag5_252d},
    "f16_sint_115_si_delta_autocorr_lag21_252d": {"inputs": ["shortinterest"], "func": f16_sint_115_si_delta_autocorr_lag21_252d},
    "f16_sint_116_dtc_delta_autocorr_lag1_252d": {"inputs": ["daystocover"], "func": f16_sint_116_dtc_delta_autocorr_lag1_252d},
    "f16_sint_117_log_si_delta_autocorr_lag1_252d": {"inputs": ["shortinterest"], "func": f16_sint_117_log_si_delta_autocorr_lag1_252d},
    "f16_sint_118_log_si_delta_autocorr_lag5_252d": {"inputs": ["shortinterest"], "func": f16_sint_118_log_si_delta_autocorr_lag5_252d},
    "f16_sint_119_si_to_float_delta_autocorr_lag1_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_119_si_to_float_delta_autocorr_lag1_252d},
    "f16_sint_120_si_persistence_acf_252d": {"inputs": ["shortinterest"], "func": f16_sint_120_si_persistence_acf_252d},
    "f16_sint_121_si_dollar_exposure": {"inputs": ["shortinterest", "close"], "func": f16_sint_121_si_dollar_exposure},
    "f16_sint_122_log_si_dollar_exposure": {"inputs": ["shortinterest", "close"], "func": f16_sint_122_log_si_dollar_exposure},
    "f16_sint_123_si_dollar_exposure_to_mcap_proxy": {"inputs": ["shortinterest", "close", "sharesbas"], "func": f16_sint_123_si_dollar_exposure_to_mcap_proxy},
    "f16_sint_124_si_dollar_exposure_rank_pct_252d": {"inputs": ["shortinterest", "close"], "func": f16_sint_124_si_dollar_exposure_rank_pct_252d},
    "f16_sint_125_si_dollar_exposure_zscore_252d": {"inputs": ["shortinterest", "close"], "func": f16_sint_125_si_dollar_exposure_zscore_252d},
    "f16_sint_126_si_dollar_to_avg_dollar_volume_21d": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_126_si_dollar_to_avg_dollar_volume_21d},
    "f16_sint_127_si_rank_stability_corr_63d_lag5": {"inputs": ["shortinterest"], "func": f16_sint_127_si_rank_stability_corr_63d_lag5},
    "f16_sint_128_si_rank_stability_corr_252d_lag21": {"inputs": ["shortinterest"], "func": f16_sint_128_si_rank_stability_corr_252d_lag21},
    "f16_sint_129_dtc_rank_stability_corr_252d_lag21": {"inputs": ["daystocover"], "func": f16_sint_129_dtc_rank_stability_corr_252d_lag21},
    "f16_sint_130_si_self_corr_lag63_252d": {"inputs": ["shortinterest"], "func": f16_sint_130_si_self_corr_lag63_252d},
    "f16_sint_131_si_to_avg_volume_252d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_131_si_to_avg_volume_252d},
    "f16_sint_132_si_to_volume_today": {"inputs": ["shortinterest", "volume"], "func": f16_sint_132_si_to_volume_today},
    "f16_sint_133_si_to_avg_dollar_volume_63d": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_133_si_to_avg_dollar_volume_63d},
    "f16_sint_134_si_to_avg_dollar_volume_252d": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_134_si_to_avg_dollar_volume_252d},
    "f16_sint_135_log_si_to_avg_volume_21d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_135_log_si_to_avg_volume_21d},
    "f16_sint_136_si_to_volume_zscore_252d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_136_si_to_volume_zscore_252d},
    "f16_sint_137_si_to_float_log": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_137_si_to_float_log},
    "f16_sint_138_si_to_float_winsorized_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_138_si_to_float_winsorized_252d},
    "f16_sint_139_si_to_float_capped_at_1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_139_si_to_float_capped_at_1},
    "f16_sint_140_one_minus_si_to_float": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_140_one_minus_si_to_float},
    "f16_sint_141_si_to_float_squared": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_141_si_to_float_squared},
    "f16_sint_142_si_to_float_x_dtc_composite": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_142_si_to_float_x_dtc_composite},
    "f16_sint_143_zscore_composite_si_dtc_252d": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_143_zscore_composite_si_dtc_252d},
    "f16_sint_144_zscore_composite_si_dtc_1260d": {"inputs": ["shortinterest", "daystocover"], "func": f16_sint_144_zscore_composite_si_dtc_1260d},
    "f16_sint_145_zscore_composite_si_float_dtc_252d": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_145_zscore_composite_si_float_dtc_252d},
    "f16_sint_146_stress_index_max_of_three": {"inputs": ["shortinterest", "sharesbas", "daystocover"], "func": f16_sint_146_stress_index_max_of_three},
    "f16_sint_147_days_since_si_252d_high": {"inputs": ["shortinterest"], "func": f16_sint_147_days_since_si_252d_high},
    "f16_sint_148_days_since_si_1260d_high": {"inputs": ["shortinterest"], "func": f16_sint_148_days_since_si_1260d_high},
    "f16_sint_149_days_since_dtc_252d_high": {"inputs": ["daystocover"], "func": f16_sint_149_days_since_dtc_252d_high},
    "f16_sint_150_days_since_si_252d_low": {"inputs": ["shortinterest"], "func": f16_sint_150_days_since_si_252d_low},
}
