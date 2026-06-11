"""
38_volatility_regime — Extended Features 001-075
Domain: volatility clustering and regime-shift detection — vol-of-vol states,
        GARCH-like persistence proxies on novel windows, regime-duration counters,
        vol percentile regimes, vol-ratio regime flags, z-scores, range-vol
        extensions, volume-vol interaction extensions, tail-risk regimes,
        Yang-Zhang estimator, ultra-short and ultra-long vol windows.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_var(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).var()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _ewm_var(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).var()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _abs_ret(s: pd.Series) -> pd.Series:
    return _log_ret(s).abs()


def _sq_ret(s: pd.Series) -> pd.Series:
    return _log_ret(s) ** 2


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _rolling_corr(a: pd.Series, b: pd.Series, w: int) -> pd.Series:
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Vol-of-vol (vol of the vol series itself) ---

def vrg_ext_001_vol_of_vol_5d_21d(close: pd.Series) -> pd.Series:
    """Std of 5-day realized vol over rolling 21-day window (vol-of-vol, short horizon)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return _rolling_std(v5, _TD_MON)


def vrg_ext_002_vol_of_vol_21d_63d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol over rolling 63-day window (vol-of-vol, medium horizon)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _rolling_std(v21, _TD_QTR)


def vrg_ext_003_vol_of_vol_21d_252d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol over rolling 252-day window (vol-of-vol, long horizon)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _rolling_std(v21, _TD_YEAR)


def vrg_ext_004_vol_of_vol_zscore_21d_252d(close: pd.Series) -> pd.Series:
    """Z-score of current vol-of-vol (21d/63d) relative to trailing 252d distribution."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    return _safe_div(vov - _rolling_mean(vov, _TD_YEAR), _rolling_std(vov, _TD_YEAR))


def vrg_ext_005_vol_of_vol_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current vol-of-vol (21d/63d) within trailing 252d distribution."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    return vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vrg_ext_006_vol_of_vol_high_regime_flag(close: pd.Series) -> pd.Series:
    """Flag: vol-of-vol (21d/63d) above its own 252-day mean (turbulent vol regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    return (vov > _rolling_mean(vov, _TD_YEAR)).astype(float)


def vrg_ext_007_vol_of_vol_days_in_high_regime(close: pd.Series) -> pd.Series:
    """Consecutive days vol-of-vol (21d/63d) is above its 252-day mean."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    cond = vov > _rolling_mean(vov, _TD_YEAR)
    return _consec_streak(cond)


def vrg_ext_008_vol_of_vol_ewm5_21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM(5) to EWM(21) of squared vol changes (vol-of-vol persistence proxy)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    dv = v21.diff(1) ** 2
    e5 = _ewm_mean(dv, _TD_WEEK)
    e21 = _ewm_mean(dv, _TD_MON)
    return _safe_div(e5, e21)


def vrg_ext_009_vol_of_vol_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of vol-of-vol (21d/63d)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    return vov.expanding(min_periods=_TD_QTR).rank(pct=True)


def vrg_ext_010_vol_of_vol_coefficient_variation(close: pd.Series) -> pd.Series:
    """CV of 21-day realized vol over 63-day window (relative vol instability)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(_rolling_std(v21, _TD_QTR), _rolling_mean(v21, _TD_QTR))


# --- Group B (011-020): Ultra-short and alternative window realized vols ---

def vrg_ext_011_realized_vol_2d(close: pd.Series) -> pd.Series:
    """2-day realized volatility (annualized) — ultra-fast panic signal."""
    r = _log_ret(close)
    return _rolling_std(r, 2) * np.sqrt(_TD_YEAR)


def vrg_ext_012_realized_vol_10d(close: pd.Series) -> pd.Series:
    """10-day realized volatility (annualized) — bi-weekly window."""
    r = _log_ret(close)
    return _rolling_std(r, 10) * np.sqrt(_TD_YEAR)


def vrg_ext_013_realized_vol_42d(close: pd.Series) -> pd.Series:
    """42-day realized volatility (annualized) — 2-month window."""
    r = _log_ret(close)
    return _rolling_std(r, 42) * np.sqrt(_TD_YEAR)


def vrg_ext_014_realized_vol_504d(close: pd.Series) -> pd.Series:
    """504-day realized volatility (annualized) — 2-year window."""
    r = _log_ret(close)
    return _rolling_std(r, 504) * np.sqrt(_TD_YEAR)


def vrg_ext_015_vol_ratio_10d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 10-day to 63-day realized vol (bi-weekly vs quarterly regime)."""
    v10 = _rolling_std(_log_ret(close), 10) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    return _safe_div(v10, v63)


def vrg_ext_016_vol_ratio_10d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 10-day to 252-day realized vol."""
    v10 = _rolling_std(_log_ret(close), 10) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    return _safe_div(v10, v252)


def vrg_ext_017_vol_ratio_42d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 42-day to 252-day realized vol (2-month vs annual regime)."""
    v42 = _rolling_std(_log_ret(close), 42) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    return _safe_div(v42, v252)


def vrg_ext_018_vol_zscore_5d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 5-day vol within trailing 252-day distribution."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return _safe_div(v5 - _rolling_mean(v5, _TD_YEAR), _rolling_std(v5, _TD_YEAR))


def vrg_ext_019_vol_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 63-day vol within trailing 252-day distribution."""
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    return _safe_div(v63 - _rolling_mean(v63, _TD_YEAR), _rolling_std(v63, _TD_YEAR))


def vrg_ext_020_vol_zscore_5d_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of 5-day realized vol."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    m = v5.expanding(min_periods=_TD_WEEK).mean()
    s = v5.expanding(min_periods=_TD_WEEK).std()
    return _safe_div(v5 - m, s)


# --- Group C (021-030): GARCH-like persistence proxies on new windows ---

def vrg_ext_021_garch_persistence_ewm2_10(close: pd.Series) -> pd.Series:
    """EWM(2)/EWM(10) squared-return ratio — ultra-fast GARCH alpha proxy."""
    sq = _sq_ret(close)
    e2 = _ewm_mean(sq, 2)
    e10 = _ewm_mean(sq, 10)
    return _safe_div(e2, e10)


def vrg_ext_022_garch_persistence_ewm10_63(close: pd.Series) -> pd.Series:
    """EWM(10)/EWM(63) squared-return ratio — bi-weekly vs quarterly GARCH persistence."""
    sq = _sq_ret(close)
    e10 = _ewm_mean(sq, 10)
    e63 = _ewm_mean(sq, _TD_QTR)
    return _safe_div(e10, e63)


def vrg_ext_023_garch_persistence_ewm42_252(close: pd.Series) -> pd.Series:
    """EWM(42)/EWM(252) squared-return ratio — 2-month vs annual GARCH persistence."""
    sq = _sq_ret(close)
    e42 = _ewm_mean(sq, 42)
    e252 = _ewm_mean(sq, _TD_YEAR)
    return _safe_div(e42, e252)


def vrg_ext_024_garch_alpha_ewm5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWM(5)/EWM(21) GARCH alpha ratio in trailing 252-day distribution."""
    sq = _sq_ret(close)
    ratio = _safe_div(_ewm_mean(sq, _TD_WEEK), _ewm_mean(sq, _TD_MON))
    return _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR), _rolling_std(ratio, _TD_YEAR))


def vrg_ext_025_garch_beta_proxy_126d(close: pd.Series) -> pd.Series:
    """Rolling GARCH beta proxy: autocorrelation of EWM(5) vol at lag-1 (126d window)."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    return _rolling_corr(ev, ev.shift(1), _TD_HALF)


def vrg_ext_026_garch_persistence_triple_ratio(close: pd.Series) -> pd.Series:
    """Triple GARCH ratio: EWM5/EWM21 * EWM21/EWM63 = EWM5/EWM63 (compound alpha)."""
    sq = _sq_ret(close)
    e5 = _ewm_mean(sq, _TD_WEEK)
    e63 = _ewm_mean(sq, _TD_QTR)
    return _safe_div(e5, e63)


def vrg_ext_027_vol_persistence_autocorr_lag2_21d(close: pd.Series) -> pd.Series:
    """21-day autocorrelation of EWM(5) volatility series at lag-2."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    return _rolling_corr(ev, ev.shift(2), _TD_MON)


def vrg_ext_028_vol_persistence_autocorr_lag5_21d(close: pd.Series) -> pd.Series:
    """21-day autocorrelation of EWM(5) volatility series at lag-5 (weekly)."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    return _rolling_corr(ev, ev.shift(5), _TD_MON)


def vrg_ext_029_vol_persistence_score_3lags_21d(close: pd.Series) -> pd.Series:
    """Mean of lag-1/2/3 autocorrelations of EWM(5) vol (21d) — persistence bundle."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    ac1 = _rolling_corr(ev, ev.shift(1), _TD_MON)
    ac2 = _rolling_corr(ev, ev.shift(2), _TD_MON)
    ac3 = _rolling_corr(ev, ev.shift(3), _TD_MON)
    return (ac1 + ac2 + ac3) / 3.0


def vrg_ext_030_ewm_vol_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWM(21) annualized vol in trailing 252-day distribution."""
    ev = _ewm_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(ev - _rolling_mean(ev, _TD_YEAR), _rolling_std(ev, _TD_YEAR))


# --- Group D (031-040): Regime duration counters (new thresholds / windows) ---

def vrg_ext_031_days_in_high_vol_regime_5_21(close: pd.Series) -> pd.Series:
    """Consecutive days 5-day vol exceeds its 21-day mean (ultra-fast high-vol streak)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    cond = v5 > _rolling_mean(v5, _TD_MON)
    return _consec_streak(cond)


def vrg_ext_032_days_in_high_vol_regime_63_252(close: pd.Series) -> pd.Series:
    """Consecutive days 63-day vol exceeds its 252-day mean (slow-regime duration)."""
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    cond = v63 > _rolling_mean(v63, _TD_YEAR)
    return _consec_streak(cond)


def vrg_ext_033_days_in_extreme_high_vol_3std(close: pd.Series) -> pd.Series:
    """Consecutive days 21d vol above its 252d mean + 3 std (extreme panic regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    cond = v21 > (v_mean + 3 * v_std)
    return _consec_streak(cond)


def vrg_ext_034_high_vol_fraction_21d_window(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where 5-day vol exceeds 252-day mean of 5-day vol."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    flags = (v5 > _rolling_mean(v5, _TD_YEAR)).astype(float)
    return _rolling_mean(flags, _TD_MON)


def vrg_ext_035_high_vol_fraction_126d_window(close: pd.Series) -> pd.Series:
    """Fraction of last 126 days where 21-day vol exceeds its 252-day mean."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    flags = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    return _rolling_mean(flags, _TD_HALF)


def vrg_ext_036_vol_above_3std_flag_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21d vol is above its 252d mean + 3 std (extreme panic threshold)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return (v21 > v_mean + 3 * v_std).astype(float)


def vrg_ext_037_vol_below_2std_flag_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21d vol is below its 252d mean - 2 std (very deep complacency regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return (v21 < v_mean - 2 * v_std).astype(float)


def vrg_ext_038_vol_regime_quartile_flag(close: pd.Series) -> pd.Series:
    """Quartile of current 21d vol in 252d distribution (0=Q1 calm .. 3=Q4 panic)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    q25 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    q50 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.50)
    q75 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    result = pd.Series(0.0, index=close.index)
    result = result.where(v21 < q25, 1.0)
    result = result.where(v21 < q50, 2.0)
    result = result.where(v21 < q75, 3.0)
    # Rebuild cleanly using numpy
    arr = np.zeros(len(v21))
    arr[v21 >= q25.fillna(np.inf)] = 1.0
    arr[v21 >= q50.fillna(np.inf)] = 2.0
    arr[v21 >= q75.fillna(np.inf)] = 3.0
    return pd.Series(arr, index=close.index)


def vrg_ext_039_days_since_vol_regime_shift_up(close: pd.Series) -> pd.Series:
    """Days elapsed since last upward vol regime shift (crossing above 252d mean)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    shift_up = ((above == 1.0) & (above.shift(1) == 0.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_up = idx.where(shift_up == 1.0).ffill().fillna(0.0)
    return (idx - last_up).where(~v21.isna(), np.nan)


def vrg_ext_040_days_since_vol_regime_shift_down(close: pd.Series) -> pd.Series:
    """Days elapsed since last downward vol regime shift (crossing below 252d mean)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    shift_dn = ((above == 0.0) & (above.shift(1) == 1.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_dn = idx.where(shift_dn == 1.0).ffill().fillna(0.0)
    return (idx - last_dn).where(~v21.isna(), np.nan)


# --- Group E (041-050): Yang-Zhang estimator and Parkinson extensions ---

def vrg_ext_041_yang_zhang_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day Yang-Zhang volatility estimator (overnight + open-close, annualized)."""
    k = 0.34 / (1.34 + (_TD_MON + 1) / (_TD_MON - 1))
    log_oc = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    var_oc = _rolling_var(log_oc, _TD_MON)
    var_co = _rolling_var(log_co, _TD_MON)
    var_rs = _rolling_mean(rs, _TD_MON)
    yz_var = var_oc + k * var_co + (1 - k) * var_rs
    return np.sqrt(yz_var.clip(lower=0) * _TD_YEAR)


def vrg_ext_042_yang_zhang_vol_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day Yang-Zhang volatility estimator (annualized)."""
    k = 0.34 / (1.34 + (_TD_WEEK + 1) / (_TD_WEEK - 1))
    log_oc = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    var_oc = _rolling_var(log_oc, _TD_WEEK)
    var_co = _rolling_var(log_co, _TD_WEEK)
    var_rs = _rolling_mean(rs, _TD_WEEK)
    yz_var = var_oc + k * var_co + (1 - k) * var_rs
    return np.sqrt(yz_var.clip(lower=0) * _TD_YEAR)


def vrg_ext_043_yz_vs_close_vol_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21d Yang-Zhang vol to 21d close-to-close vol (estimator divergence)."""
    yz = vrg_ext_041_yang_zhang_vol_21d(close, high, low, open)
    cc = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(yz, cc)


def vrg_ext_044_yz_vol_zscore_21d_in_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21d Yang-Zhang vol within trailing 252d distribution."""
    yz = vrg_ext_041_yang_zhang_vol_21d(close, high, low, open)
    return _safe_div(yz - _rolling_mean(yz, _TD_YEAR), _rolling_std(yz, _TD_YEAR))


def vrg_ext_045_yz_high_vol_flag_21_252(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 21d Yang-Zhang vol exceeds its 252-day mean."""
    yz = vrg_ext_041_yang_zhang_vol_21d(close, high, low, open)
    return (yz > _rolling_mean(yz, _TD_YEAR)).astype(float)


def vrg_ext_046_parkinson_vol_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day Parkinson volatility estimator (annualized)."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk_var = _rolling_mean(log_hl, _TD_QTR) / (4.0 * np.log(2.0))
    return np.sqrt(pk_var * _TD_YEAR)


def vrg_ext_047_parkinson_vol_zscore_21d_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21d Parkinson vol within trailing 252-day distribution."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk21 = np.sqrt(_rolling_mean(log_hl, _TD_MON) / (4.0 * np.log(2.0)) * _TD_YEAR)
    return _safe_div(pk21 - _rolling_mean(pk21, _TD_YEAR), _rolling_std(pk21, _TD_YEAR))


def vrg_ext_048_parkinson_vs_close_vol_ratio_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5d Parkinson vol to 5d close-to-close vol (intraday vs close estimation)."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk5 = np.sqrt(_rolling_mean(log_hl, _TD_WEEK) / (4.0 * np.log(2.0)) * _TD_YEAR)
    cc5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return _safe_div(pk5, cc5)


def vrg_ext_049_rogers_satchell_vol_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63-day Rogers-Satchell volatility estimator (drift-free, annualized)."""
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    return np.sqrt(_rolling_mean(rs, _TD_QTR) * _TD_YEAR)


def vrg_ext_050_rs_vs_gk_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21d Rogers-Satchell vol to 21d Garman-Klass vol (estimator spread)."""
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs_var = _rolling_mean(log_hc * log_ho + log_lc * log_lo, _TD_MON)
    rs21 = np.sqrt(rs_var.clip(lower=0) * _TD_YEAR)
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk_var = _rolling_mean(0.5 * log_hl ** 2 - (2 * np.log(2) - 1) * log_co ** 2, _TD_MON)
    gk21 = np.sqrt(gk_var.clip(lower=0) * _TD_YEAR)
    return _safe_div(rs21, gk21)


# --- Group F (051-060): Volume-regime extensions ---

def vrg_ext_051_vol_volume_corr_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126d correlation between absolute returns and volume (longer-horizon co-clustering)."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, volume, _TD_HALF)


def vrg_ext_052_sq_ret_volume_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d correlation between squared returns and volume (ARCH clustering + volume)."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, volume, _TD_QTR)


def vrg_ext_053_high_vol_high_volume_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d where both abs-return and volume exceed their 21d means."""
    ab = _abs_ret(close)
    flag = ((ab > _rolling_mean(ab, _TD_MON)) & (volume > _rolling_mean(volume, _TD_MON))).astype(float)
    return _rolling_mean(flag, _TD_QTR)


def vrg_ext_054_high_vol_low_volume_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d with high abs-return but low volume (illiquidity vol regime)."""
    ab = _abs_ret(close)
    flag = ((ab > _rolling_mean(ab, _TD_MON)) & (volume < _rolling_mean(volume, _TD_MON))).astype(float)
    return _rolling_mean(flag, _TD_QTR)


def vrg_ext_055_volume_weighted_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted realized vol 21d: std of volume-weighted log-returns (annualized)."""
    r = _log_ret(close)
    vol_sum = _rolling_sum(volume, _TD_MON)
    r_vw = _safe_div(_rolling_sum(r * volume, _TD_MON), vol_sum)
    dev2 = (r - r_vw) ** 2
    vw_var = _safe_div(_rolling_sum(dev2 * volume, _TD_MON), vol_sum)
    return np.sqrt(vw_var.clip(lower=0) * _TD_YEAR)


def vrg_ext_056_volume_weighted_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted realized vol 63d (annualized)."""
    r = _log_ret(close)
    vol_sum = _rolling_sum(volume, _TD_QTR)
    r_vw = _safe_div(_rolling_sum(r * volume, _TD_QTR), vol_sum)
    dev2 = (r - r_vw) ** 2
    vw_var = _safe_div(_rolling_sum(dev2 * volume, _TD_QTR), vol_sum)
    return np.sqrt(vw_var.clip(lower=0) * _TD_YEAR)


def vrg_ext_057_vol_volume_zscore_product_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of vol z-score and volume z-score over 63d (joint extremity score)."""
    ab = _abs_ret(close)
    ab_z = _safe_div(ab - _rolling_mean(ab, _TD_QTR), _rolling_std(ab, _TD_QTR))
    v_z = _safe_div(volume - _rolling_mean(volume, _TD_QTR), _rolling_std(volume, _TD_QTR))
    return ab_z * v_z


def vrg_ext_058_vol_on_high_volume_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean abs-return on high-volume days (volume > 21d mean) in trailing 21d."""
    ab = _abs_ret(close)
    high_vol_day = volume > _rolling_mean(volume, _TD_MON)
    ab_high = ab.where(high_vol_day, np.nan)
    return ab_high.rolling(_TD_MON, min_periods=1).mean()


def vrg_ext_059_vol_on_down_volume_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean abs-return on days with both negative return and above-avg volume (63d)."""
    r = _log_ret(close)
    ab = r.abs()
    panic_day = (r < 0) & (volume > _rolling_mean(volume, _TD_MON))
    ab_panic = ab.where(panic_day, np.nan)
    return ab_panic.rolling(_TD_QTR, min_periods=1).mean()


def vrg_ext_060_vol_volume_regime_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of joint high-vol/high-volume days in trailing 252 days."""
    ab = _abs_ret(close)
    flag = ((ab > _rolling_mean(ab, _TD_MON)) & (volume > _rolling_mean(volume, _TD_MON))).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


# --- Group G (061-075): Tail-risk regimes and composite distress signals ---

def vrg_ext_061_return_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d excess kurtosis of log-returns (fat-tail regime at quarterly window)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vrg_ext_062_return_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d excess kurtosis of log-returns (annual fat-tail regime)."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()


def vrg_ext_063_extreme_return_flag_3std_21d(close: pd.Series) -> pd.Series:
    """Flag: absolute log-return exceeds 3x 21d rolling std (single-day tail event)."""
    r = _log_ret(close)
    threshold = 3.0 * _rolling_std(r, _TD_MON)
    return (r.abs() > threshold).astype(float)


def vrg_ext_064_extreme_return_count_63d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma return events in trailing 63 days."""
    r = _log_ret(close)
    threshold = 3.0 * _rolling_std(r, _TD_MON)
    flags = (r.abs() > threshold).astype(float)
    return _rolling_sum(flags, _TD_QTR)


def vrg_ext_065_extreme_return_count_252d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma return events in trailing 252 days."""
    r = _log_ret(close)
    threshold = 3.0 * _rolling_std(r, _TD_MON)
    flags = (r.abs() > threshold).astype(float)
    return _rolling_sum(flags, _TD_YEAR)


def vrg_ext_066_negative_extreme_return_count_63d(close: pd.Series) -> pd.Series:
    """Count of negative 3-sigma return events in trailing 63 days (downside tail regime)."""
    r = _log_ret(close)
    threshold = 3.0 * _rolling_std(r, _TD_MON)
    flags = (r < -threshold).astype(float)
    return _rolling_sum(flags, _TD_QTR)


def vrg_ext_067_vol_regime_skew_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Diff: 252d high-vol streak days minus 252d low-vol streak days (regime imbalance)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    high_days = _rolling_sum((v21 > v_avg).astype(float), _TD_YEAR)
    low_days = _rolling_sum((v21 <= v_avg).astype(float), _TD_YEAR)
    return high_days - low_days


def vrg_ext_068_vol_regime_new_low_vol_flag_252d(close: pd.Series) -> pd.Series:
    """Flag: current 21d vol is new 252-day low vol (calm complacency breakout)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    prior_min = v21.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return (v21 < prior_min).astype(float)


def vrg_ext_069_vol_regime_new_low_vol_flag_126d(close: pd.Series) -> pd.Series:
    """Flag: current 21d vol is new 126-day low vol."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    prior_min = v21.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()
    return (v21 < prior_min).astype(float)


def vrg_ext_070_vol_regime_composite_distress(close: pd.Series) -> pd.Series:
    """Distress composite: z-score + pct-rank + above-2std flag of 21d vol (3 signals)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    z = _safe_div(v21 - v_mean, v_std)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    above2 = (v21 > v_mean + 2 * v_std).astype(float)
    return z / 3.0 + rank + above2


def vrg_ext_071_vol_mean_reversion_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21d vol deviation from its 63d mean (short-run mean-reversion signal)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(v21 - _rolling_mean(v21, _TD_QTR), _rolling_std(v21, _TD_QTR))


def vrg_ext_072_vol_quartile_regime_252d(close: pd.Series) -> pd.Series:
    """Quintile (0-4) of current 21d vol in trailing 252d distribution."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    q20 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.20)
    q40 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.40)
    q60 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.60)
    q80 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    arr = np.zeros(len(v21))
    arr[v21.values >= q20.fillna(np.inf).values] = 1.0
    arr[v21.values >= q40.fillna(np.inf).values] = 2.0
    arr[v21.values >= q60.fillna(np.inf).values] = 3.0
    arr[v21.values >= q80.fillna(np.inf).values] = 4.0
    return pd.Series(arr, index=close.index)


def vrg_ext_073_vol_regime_count_above_median_21d(close: pd.Series) -> pd.Series:
    """Count of days in last 21d where realized 5d vol exceeds 252d median of 5d vol."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    median252 = _rolling_median(v5, _TD_YEAR)
    flags = (v5 > median252).astype(float)
    return _rolling_sum(flags, _TD_MON)


def vrg_ext_074_vol_regime_count_above_median_63d(close: pd.Series) -> pd.Series:
    """Count of days in last 63d where realized 5d vol exceeds 252d median of 5d vol."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    median252 = _rolling_median(v5, _TD_YEAR)
    flags = (v5 > median252).astype(float)
    return _rolling_sum(flags, _TD_QTR)


def vrg_ext_075_vol_regime_panic_composite(close: pd.Series) -> pd.Series:
    """Panic regime composite: pct-rank of vol + extreme-return flag + vol-of-vol z-score.
    Combines percentile rank of 21d vol, presence of 3-sigma event, and vol-of-vol z-score
    to produce a capitulation stress signal (higher = more distressed)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r = _log_ret(close)
    extreme = (r.abs() > 3.0 * _rolling_std(r, _TD_MON)).astype(float)
    vov = _rolling_std(v21, _TD_QTR)
    vov_z = _safe_div(vov - _rolling_mean(vov, _TD_YEAR), _rolling_std(vov, _TD_YEAR))
    return rank + extreme + vov_z.clip(lower=0)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_EXTENDED_REGISTRY_001_075 = {
    "vrg_ext_001_vol_of_vol_5d_21d": {"inputs": ["close"], "func": vrg_ext_001_vol_of_vol_5d_21d},
    "vrg_ext_002_vol_of_vol_21d_63d": {"inputs": ["close"], "func": vrg_ext_002_vol_of_vol_21d_63d},
    "vrg_ext_003_vol_of_vol_21d_252d": {"inputs": ["close"], "func": vrg_ext_003_vol_of_vol_21d_252d},
    "vrg_ext_004_vol_of_vol_zscore_21d_252d": {"inputs": ["close"], "func": vrg_ext_004_vol_of_vol_zscore_21d_252d},
    "vrg_ext_005_vol_of_vol_pct_rank_252d": {"inputs": ["close"], "func": vrg_ext_005_vol_of_vol_pct_rank_252d},
    "vrg_ext_006_vol_of_vol_high_regime_flag": {"inputs": ["close"], "func": vrg_ext_006_vol_of_vol_high_regime_flag},
    "vrg_ext_007_vol_of_vol_days_in_high_regime": {"inputs": ["close"], "func": vrg_ext_007_vol_of_vol_days_in_high_regime},
    "vrg_ext_008_vol_of_vol_ewm5_21_ratio": {"inputs": ["close"], "func": vrg_ext_008_vol_of_vol_ewm5_21_ratio},
    "vrg_ext_009_vol_of_vol_expanding_pct_rank": {"inputs": ["close"], "func": vrg_ext_009_vol_of_vol_expanding_pct_rank},
    "vrg_ext_010_vol_of_vol_coefficient_variation": {"inputs": ["close"], "func": vrg_ext_010_vol_of_vol_coefficient_variation},
    "vrg_ext_011_realized_vol_2d": {"inputs": ["close"], "func": vrg_ext_011_realized_vol_2d},
    "vrg_ext_012_realized_vol_10d": {"inputs": ["close"], "func": vrg_ext_012_realized_vol_10d},
    "vrg_ext_013_realized_vol_42d": {"inputs": ["close"], "func": vrg_ext_013_realized_vol_42d},
    "vrg_ext_014_realized_vol_504d": {"inputs": ["close"], "func": vrg_ext_014_realized_vol_504d},
    "vrg_ext_015_vol_ratio_10d_63d": {"inputs": ["close"], "func": vrg_ext_015_vol_ratio_10d_63d},
    "vrg_ext_016_vol_ratio_10d_252d": {"inputs": ["close"], "func": vrg_ext_016_vol_ratio_10d_252d},
    "vrg_ext_017_vol_ratio_42d_252d": {"inputs": ["close"], "func": vrg_ext_017_vol_ratio_42d_252d},
    "vrg_ext_018_vol_zscore_5d_in_252d": {"inputs": ["close"], "func": vrg_ext_018_vol_zscore_5d_in_252d},
    "vrg_ext_019_vol_zscore_63d_in_252d": {"inputs": ["close"], "func": vrg_ext_019_vol_zscore_63d_in_252d},
    "vrg_ext_020_vol_zscore_5d_expanding": {"inputs": ["close"], "func": vrg_ext_020_vol_zscore_5d_expanding},
    "vrg_ext_021_garch_persistence_ewm2_10": {"inputs": ["close"], "func": vrg_ext_021_garch_persistence_ewm2_10},
    "vrg_ext_022_garch_persistence_ewm10_63": {"inputs": ["close"], "func": vrg_ext_022_garch_persistence_ewm10_63},
    "vrg_ext_023_garch_persistence_ewm42_252": {"inputs": ["close"], "func": vrg_ext_023_garch_persistence_ewm42_252},
    "vrg_ext_024_garch_alpha_ewm5_zscore_252d": {"inputs": ["close"], "func": vrg_ext_024_garch_alpha_ewm5_zscore_252d},
    "vrg_ext_025_garch_beta_proxy_126d": {"inputs": ["close"], "func": vrg_ext_025_garch_beta_proxy_126d},
    "vrg_ext_026_garch_persistence_triple_ratio": {"inputs": ["close"], "func": vrg_ext_026_garch_persistence_triple_ratio},
    "vrg_ext_027_vol_persistence_autocorr_lag2_21d": {"inputs": ["close"], "func": vrg_ext_027_vol_persistence_autocorr_lag2_21d},
    "vrg_ext_028_vol_persistence_autocorr_lag5_21d": {"inputs": ["close"], "func": vrg_ext_028_vol_persistence_autocorr_lag5_21d},
    "vrg_ext_029_vol_persistence_score_3lags_21d": {"inputs": ["close"], "func": vrg_ext_029_vol_persistence_score_3lags_21d},
    "vrg_ext_030_ewm_vol_zscore_63d_in_252d": {"inputs": ["close"], "func": vrg_ext_030_ewm_vol_zscore_63d_in_252d},
    "vrg_ext_031_days_in_high_vol_regime_5_21": {"inputs": ["close"], "func": vrg_ext_031_days_in_high_vol_regime_5_21},
    "vrg_ext_032_days_in_high_vol_regime_63_252": {"inputs": ["close"], "func": vrg_ext_032_days_in_high_vol_regime_63_252},
    "vrg_ext_033_days_in_extreme_high_vol_3std": {"inputs": ["close"], "func": vrg_ext_033_days_in_extreme_high_vol_3std},
    "vrg_ext_034_high_vol_fraction_21d_window": {"inputs": ["close"], "func": vrg_ext_034_high_vol_fraction_21d_window},
    "vrg_ext_035_high_vol_fraction_126d_window": {"inputs": ["close"], "func": vrg_ext_035_high_vol_fraction_126d_window},
    "vrg_ext_036_vol_above_3std_flag_21_252": {"inputs": ["close"], "func": vrg_ext_036_vol_above_3std_flag_21_252},
    "vrg_ext_037_vol_below_2std_flag_21_252": {"inputs": ["close"], "func": vrg_ext_037_vol_below_2std_flag_21_252},
    "vrg_ext_038_vol_regime_quartile_flag": {"inputs": ["close"], "func": vrg_ext_038_vol_regime_quartile_flag},
    "vrg_ext_039_days_since_vol_regime_shift_up": {"inputs": ["close"], "func": vrg_ext_039_days_since_vol_regime_shift_up},
    "vrg_ext_040_days_since_vol_regime_shift_down": {"inputs": ["close"], "func": vrg_ext_040_days_since_vol_regime_shift_down},
    "vrg_ext_041_yang_zhang_vol_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_041_yang_zhang_vol_21d},
    "vrg_ext_042_yang_zhang_vol_5d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_042_yang_zhang_vol_5d},
    "vrg_ext_043_yz_vs_close_vol_ratio_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_043_yz_vs_close_vol_ratio_21d},
    "vrg_ext_044_yz_vol_zscore_21d_in_252d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_044_yz_vol_zscore_21d_in_252d},
    "vrg_ext_045_yz_high_vol_flag_21_252": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_045_yz_high_vol_flag_21_252},
    "vrg_ext_046_parkinson_vol_63d": {"inputs": ["close", "high", "low"], "func": vrg_ext_046_parkinson_vol_63d},
    "vrg_ext_047_parkinson_vol_zscore_21d_252d": {"inputs": ["close", "high", "low"], "func": vrg_ext_047_parkinson_vol_zscore_21d_252d},
    "vrg_ext_048_parkinson_vs_close_vol_ratio_5d": {"inputs": ["close", "high", "low"], "func": vrg_ext_048_parkinson_vs_close_vol_ratio_5d},
    "vrg_ext_049_rogers_satchell_vol_63d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_049_rogers_satchell_vol_63d},
    "vrg_ext_050_rs_vs_gk_ratio_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_ext_050_rs_vs_gk_ratio_21d},
    "vrg_ext_051_vol_volume_corr_126d": {"inputs": ["close", "volume"], "func": vrg_ext_051_vol_volume_corr_126d},
    "vrg_ext_052_sq_ret_volume_corr_63d": {"inputs": ["close", "volume"], "func": vrg_ext_052_sq_ret_volume_corr_63d},
    "vrg_ext_053_high_vol_high_volume_fraction_63d": {"inputs": ["close", "volume"], "func": vrg_ext_053_high_vol_high_volume_fraction_63d},
    "vrg_ext_054_high_vol_low_volume_fraction_63d": {"inputs": ["close", "volume"], "func": vrg_ext_054_high_vol_low_volume_fraction_63d},
    "vrg_ext_055_volume_weighted_vol_21d": {"inputs": ["close", "volume"], "func": vrg_ext_055_volume_weighted_vol_21d},
    "vrg_ext_056_volume_weighted_vol_63d": {"inputs": ["close", "volume"], "func": vrg_ext_056_volume_weighted_vol_63d},
    "vrg_ext_057_vol_volume_zscore_product_63d": {"inputs": ["close", "volume"], "func": vrg_ext_057_vol_volume_zscore_product_63d},
    "vrg_ext_058_vol_on_high_volume_days_21d": {"inputs": ["close", "volume"], "func": vrg_ext_058_vol_on_high_volume_days_21d},
    "vrg_ext_059_vol_on_down_volume_days_63d": {"inputs": ["close", "volume"], "func": vrg_ext_059_vol_on_down_volume_days_63d},
    "vrg_ext_060_vol_volume_regime_count_252d": {"inputs": ["close", "volume"], "func": vrg_ext_060_vol_volume_regime_count_252d},
    "vrg_ext_061_return_kurtosis_63d": {"inputs": ["close"], "func": vrg_ext_061_return_kurtosis_63d},
    "vrg_ext_062_return_kurtosis_252d": {"inputs": ["close"], "func": vrg_ext_062_return_kurtosis_252d},
    "vrg_ext_063_extreme_return_flag_3std_21d": {"inputs": ["close"], "func": vrg_ext_063_extreme_return_flag_3std_21d},
    "vrg_ext_064_extreme_return_count_63d": {"inputs": ["close"], "func": vrg_ext_064_extreme_return_count_63d},
    "vrg_ext_065_extreme_return_count_252d": {"inputs": ["close"], "func": vrg_ext_065_extreme_return_count_252d},
    "vrg_ext_066_negative_extreme_return_count_63d": {"inputs": ["close"], "func": vrg_ext_066_negative_extreme_return_count_63d},
    "vrg_ext_067_vol_regime_skew_asymmetry_252d": {"inputs": ["close"], "func": vrg_ext_067_vol_regime_skew_asymmetry_252d},
    "vrg_ext_068_vol_regime_new_low_vol_flag_252d": {"inputs": ["close"], "func": vrg_ext_068_vol_regime_new_low_vol_flag_252d},
    "vrg_ext_069_vol_regime_new_low_vol_flag_126d": {"inputs": ["close"], "func": vrg_ext_069_vol_regime_new_low_vol_flag_126d},
    "vrg_ext_070_vol_regime_composite_distress": {"inputs": ["close"], "func": vrg_ext_070_vol_regime_composite_distress},
    "vrg_ext_071_vol_mean_reversion_zscore_63d": {"inputs": ["close"], "func": vrg_ext_071_vol_mean_reversion_zscore_63d},
    "vrg_ext_072_vol_quartile_regime_252d": {"inputs": ["close"], "func": vrg_ext_072_vol_quartile_regime_252d},
    "vrg_ext_073_vol_regime_count_above_median_21d": {"inputs": ["close"], "func": vrg_ext_073_vol_regime_count_above_median_21d},
    "vrg_ext_074_vol_regime_count_above_median_63d": {"inputs": ["close"], "func": vrg_ext_074_vol_regime_count_above_median_63d},
    "vrg_ext_075_vol_regime_panic_composite": {"inputs": ["close"], "func": vrg_ext_075_vol_regime_panic_composite},
}
