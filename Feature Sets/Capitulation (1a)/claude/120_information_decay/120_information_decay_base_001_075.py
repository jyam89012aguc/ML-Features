"""
120_information_decay — Base Features 001-075
Domain: information decay — decay rate and half-life of return autocorrelation,
        mutual information at increasing lags, shock-persistence, EWM half-life,
        rate at which momentum signals lose predictive structure, memory length
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _returns(close: pd.Series) -> pd.Series:
    """Simple log returns; NaN-safe."""
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation at given lag over window w. NaN-safe."""
    def _ac(x):
        x = x[~np.isnan(x)]
        if len(x) < lag + 3:
            return np.nan
        x0 = x[:-lag]
        x1 = x[lag:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    return s.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _decay_rate_from_two_lags(ac_lag1: pd.Series, ac_lag2: pd.Series) -> pd.Series:
    """
    Estimate exponential decay rate lambda from two autocorrelations:
    ac_lag2 / ac_lag1 gives the per-lag decay factor; lambda = -log(ratio).
    NaN where inputs are non-positive or ratio >= 1.
    """
    ratio = _safe_div(ac_lag2.abs(), ac_lag1.abs().clip(lower=_EPS))
    ratio_clipped = ratio.clip(lower=_EPS, upper=1.0 - _EPS)
    return -np.log(ratio_clipped)


def _halflife_from_decay(decay_rate: pd.Series) -> pd.Series:
    """Half-life in days from exponential decay rate lambda: hl = log(2)/lambda."""
    return np.log(2.0) / decay_rate.clip(lower=_EPS)


def _ewm_halflife_estimate(s: pd.Series, w: int) -> pd.Series:
    """
    Estimate EWM half-life by fitting AC(1) on rolling window:
    alpha = 1 - AC(1), halflife = log(2)/log(1/(1-alpha)) ~= log(2)/(-log(1-alpha)).
    """
    ac1 = _rolling_autocorr(s, w, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Autocorrelation decay rate estimates at multiple lags ---

def idc_001_ac_decay_lag1_lag2_63d(close: pd.Series) -> pd.Series:
    """Decay rate estimated from AC(1) and AC(2) of returns over 63-day window."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_002_ac_decay_lag1_lag2_126d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(1)/AC(2) of returns over 126-day window."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1)
    ac2 = _rolling_autocorr(r, _TD_HALF, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_003_ac_decay_lag1_lag2_252d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(1)/AC(2) of returns over 252-day window."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_YEAR, 1)
    ac2 = _rolling_autocorr(r, _TD_YEAR, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_004_ac_decay_lag2_lag4_63d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(2)/AC(4) of returns over 63-day window."""
    r = _returns(close)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    ac4 = _rolling_autocorr(r, _TD_QTR, 4)
    return _decay_rate_from_two_lags(ac2, ac4)


def idc_005_ac_decay_lag2_lag4_126d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(2)/AC(4) of returns over 126-day window."""
    r = _returns(close)
    ac2 = _rolling_autocorr(r, _TD_HALF, 2)
    ac4 = _rolling_autocorr(r, _TD_HALF, 4)
    return _decay_rate_from_two_lags(ac2, ac4)


def idc_006_halflife_ac_decay_63d(close: pd.Series) -> pd.Series:
    """Half-life (days) of return autocorrelation from 63-day AC(1)/AC(2) decay rate."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_007_halflife_ac_decay_126d(close: pd.Series) -> pd.Series:
    """Half-life of return autocorrelation from 126-day AC(1)/AC(2) decay rate."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1)
    ac2 = _rolling_autocorr(r, _TD_HALF, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_008_halflife_ac_decay_252d(close: pd.Series) -> pd.Series:
    """Half-life of return autocorrelation from 252-day AC(1)/AC(2) decay rate."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_YEAR, 1)
    ac2 = _rolling_autocorr(r, _TD_YEAR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_009_ac_lag1_returns_63d(close: pd.Series) -> pd.Series:
    """AC(1) of log returns over 63-day rolling window (level, not decay rate)."""
    return _rolling_autocorr(_returns(close), _TD_QTR, 1)


def idc_010_ac_lag1_returns_126d(close: pd.Series) -> pd.Series:
    """AC(1) of log returns over 126-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_HALF, 1)


def idc_011_ac_lag2_returns_63d(close: pd.Series) -> pd.Series:
    """AC(2) of log returns over 63-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_QTR, 2)


def idc_012_ac_lag3_returns_63d(close: pd.Series) -> pd.Series:
    """AC(3) of log returns over 63-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_QTR, 3)


def idc_013_ac_lag5_returns_63d(close: pd.Series) -> pd.Series:
    """AC(5) (weekly lag) of log returns over 63-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_QTR, 5)


def idc_014_ac_lag5_returns_126d(close: pd.Series) -> pd.Series:
    """AC(5) of log returns over 126-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_HALF, 5)


def idc_015_ac_lag10_returns_126d(close: pd.Series) -> pd.Series:
    """AC(10) of log returns over 126-day rolling window."""
    return _rolling_autocorr(_returns(close), _TD_HALF, 10)


# --- Group B (016-030): EWM half-life and span estimates ---

def idc_016_ewm_halflife_21d(close: pd.Series) -> pd.Series:
    """EWM half-life estimate fitted on 21-day returns window."""
    return _ewm_halflife_estimate(_returns(close), _TD_MON)


def idc_017_ewm_halflife_63d(close: pd.Series) -> pd.Series:
    """EWM half-life estimate fitted on 63-day returns window."""
    return _ewm_halflife_estimate(_returns(close), _TD_QTR)


def idc_018_ewm_halflife_126d(close: pd.Series) -> pd.Series:
    """EWM half-life estimate fitted on 126-day returns window."""
    return _ewm_halflife_estimate(_returns(close), _TD_HALF)


def idc_019_ewm_halflife_252d(close: pd.Series) -> pd.Series:
    """EWM half-life estimate fitted on 252-day returns window."""
    return _ewm_halflife_estimate(_returns(close), _TD_YEAR)


def idc_020_ewm_halflife_vs_21d_mean(close: pd.Series) -> pd.Series:
    """63-day EWM half-life minus its 21-day moving average (deviation from recent norm)."""
    hl = _ewm_halflife_estimate(_returns(close), _TD_QTR)
    return hl - _rolling_mean(hl, _TD_MON)


def idc_021_ewm_halflife_abs_vol_21d(close: pd.Series) -> pd.Series:
    """EWM half-life fitted on absolute log-returns over 21-day window (vol persistence)."""
    ar = _returns(close).abs()
    return _ewm_halflife_estimate(ar, _TD_MON)


def idc_022_ewm_halflife_abs_vol_63d(close: pd.Series) -> pd.Series:
    """EWM half-life fitted on absolute log-returns over 63-day window."""
    ar = _returns(close).abs()
    return _ewm_halflife_estimate(ar, _TD_QTR)


def idc_023_ewm_halflife_abs_vol_126d(close: pd.Series) -> pd.Series:
    """EWM half-life fitted on absolute log-returns over 126-day window."""
    ar = _returns(close).abs()
    return _ewm_halflife_estimate(ar, _TD_HALF)


def idc_024_ewm_halflife_sq_vol_63d(close: pd.Series) -> pd.Series:
    """EWM half-life fitted on squared log-returns over 63-day window (variance persistence)."""
    sq = _returns(close) ** 2
    return _ewm_halflife_estimate(sq, _TD_QTR)


def idc_025_ewm_halflife_sq_vol_252d(close: pd.Series) -> pd.Series:
    """EWM half-life fitted on squared log-returns over 252-day window."""
    sq = _returns(close) ** 2
    return _ewm_halflife_estimate(sq, _TD_YEAR)


def idc_026_ewm_span_from_ac1_63d(close: pd.Series) -> pd.Series:
    """EWM span = 2/alpha - 1 derived from AC(1) over 63-day window."""
    ac1 = _rolling_autocorr(_returns(close), _TD_QTR, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return (2.0 / alpha) - 1.0


def idc_027_ewm_span_from_ac1_126d(close: pd.Series) -> pd.Series:
    """EWM span derived from AC(1) over 126-day window."""
    ac1 = _rolling_autocorr(_returns(close), _TD_HALF, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return (2.0 / alpha) - 1.0


def idc_028_ewm_halflife_ratio_21d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day EWM half-life to 252-day EWM half-life (short vs long memory)."""
    hl21 = _ewm_halflife_estimate(_returns(close), _TD_MON)
    hl252 = _ewm_halflife_estimate(_returns(close), _TD_YEAR)
    return _safe_div(hl21, hl252.clip(lower=_EPS))


def idc_029_ewm_halflife_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day EWM half-life to 252-day EWM half-life."""
    hl63 = _ewm_halflife_estimate(_returns(close), _TD_QTR)
    hl252 = _ewm_halflife_estimate(_returns(close), _TD_YEAR)
    return _safe_div(hl63, hl252.clip(lower=_EPS))


def idc_030_ewm_halflife_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day EWM half-life in trailing 252-day distribution."""
    hl = _ewm_halflife_estimate(_returns(close), _TD_QTR)
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (031-045): Shock persistence / impulse response decay ---

def idc_031_shock_persistence_5d_63d(close: pd.Series) -> pd.Series:
    """
    Shock persistence: correlation of current return with return 5 days ago
    measured over trailing 63-day window. Measures how much a 5-day-old shock lingers.
    """
    return _rolling_autocorr(_returns(close), _TD_QTR, _TD_WEEK)


def idc_032_shock_persistence_10d_63d(close: pd.Series) -> pd.Series:
    """Correlation of current return with return 10 days ago (63-day window)."""
    return _rolling_autocorr(_returns(close), _TD_QTR, 10)


def idc_033_shock_persistence_21d_126d(close: pd.Series) -> pd.Series:
    """Correlation of current return with return 21 days ago (126-day window)."""
    return _rolling_autocorr(_returns(close), _TD_HALF, _TD_MON)


def idc_034_shock_persistence_ratio_5d_to_1d(close: pd.Series) -> pd.Series:
    """Ratio of AC(5) to AC(1) over 63 days — how much persistence remains at week lag."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac5 = _rolling_autocorr(r, _TD_QTR, 5)
    return _safe_div(ac5.abs(), ac1.abs().clip(lower=_EPS))


def idc_035_shock_persistence_ratio_10d_to_1d(close: pd.Series) -> pd.Series:
    """Ratio of AC(10) to AC(1) over 126 days — persistence at 2-week lag."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1)
    ac10 = _rolling_autocorr(r, _TD_HALF, 10)
    return _safe_div(ac10.abs(), ac1.abs().clip(lower=_EPS))


def idc_036_impulse_decay_vol_5d_to_21d(close: pd.Series) -> pd.Series:
    """
    Impulse-response decay of volatility: ratio of 5-day realized vol
    to 21-day realized vol — how fast the volatility shock dissipates.
    """
    r = _returns(close)
    vol5 = r.rolling(_TD_WEEK, min_periods=2).std()
    vol21 = r.rolling(_TD_MON, min_periods=5).std()
    return _safe_div(vol5, vol21.clip(lower=_EPS))


def idc_037_impulse_decay_vol_5d_to_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 63-day realized vol."""
    r = _returns(close)
    vol5 = r.rolling(_TD_WEEK, min_periods=2).std()
    vol63 = r.rolling(_TD_QTR, min_periods=10).std()
    return _safe_div(vol5, vol63.clip(lower=_EPS))


def idc_038_impulse_decay_vol_21d_to_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day realized vol to 63-day realized vol."""
    r = _returns(close)
    vol21 = r.rolling(_TD_MON, min_periods=5).std()
    vol63 = r.rolling(_TD_QTR, min_periods=15).std()
    return _safe_div(vol21, vol63.clip(lower=_EPS))


def idc_039_impulse_decay_abs_return_5d_to_21d(close: pd.Series) -> pd.Series:
    """Ratio of mean absolute return over 5d vs 21d — speed of return shock decay."""
    r = _returns(close).abs()
    m5 = _rolling_mean(r, _TD_WEEK)
    m21 = _rolling_mean(r, _TD_MON)
    return _safe_div(m5, m21.clip(lower=_EPS))


def idc_040_impulse_decay_abs_return_21d_to_126d(close: pd.Series) -> pd.Series:
    """Ratio of mean absolute return over 21d vs 126d."""
    r = _returns(close).abs()
    m21 = _rolling_mean(r, _TD_MON)
    m126 = _rolling_mean(r, _TD_HALF)
    return _safe_div(m21, m126.clip(lower=_EPS))


def idc_041_return_memory_halflife_ols_63d(close: pd.Series) -> pd.Series:
    """
    Estimate memory half-life from OLS fit of log|AC(k)| vs lag k for k=1..5
    over trailing 63-day window. Returns half-life = log(2)/slope_magnitude.
    """
    def _hl(x):
        x = x[~np.isnan(x)]
        if len(x) < 15:
            return np.nan
        lags = [1, 2, 3, 4, 5]
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs) & (np.abs(acs) > _EPS)
        if valid.sum() < 2:
            return np.nan
        lags_v = np.array(lags)[valid]
        log_ac = np.log(np.abs(acs[valid]) + _EPS)
        if lags_v.std() < _EPS:
            return np.nan
        slope = np.polyfit(lags_v, log_ac, 1)[0]
        if slope >= 0:
            return np.nan
        return float(np.log(2.0) / (-slope))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _hl(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_042_return_memory_halflife_ols_126d(close: pd.Series) -> pd.Series:
    """Memory half-life from OLS fit of log|AC(k)| vs k=1..10 over 126-day window."""
    def _hl(x):
        x = x[~np.isnan(x)]
        if len(x) < 25:
            return np.nan
        lags = [1, 2, 3, 5, 7, 10]
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs) & (np.abs(acs) > _EPS)
        if valid.sum() < 2:
            return np.nan
        lags_v = np.array(lags)[valid]
        log_ac = np.log(np.abs(acs[valid]) + _EPS)
        if lags_v.std() < _EPS:
            return np.nan
        slope = np.polyfit(lags_v, log_ac, 1)[0]
        if slope >= 0:
            return np.nan
        return float(np.log(2.0) / (-slope))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _hl(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_043_ac_lag1_abs_returns_63d(close: pd.Series) -> pd.Series:
    """AC(1) of absolute returns over 63-day window (vol clustering persistence)."""
    return _rolling_autocorr(_returns(close).abs(), _TD_QTR, 1)


def idc_044_ac_lag1_abs_returns_126d(close: pd.Series) -> pd.Series:
    """AC(1) of absolute returns over 126-day window."""
    return _rolling_autocorr(_returns(close).abs(), _TD_HALF, 1)


def idc_045_ac_lag5_abs_returns_126d(close: pd.Series) -> pd.Series:
    """AC(5) of absolute returns over 126-day window (weekly vol persistence)."""
    return _rolling_autocorr(_returns(close).abs(), _TD_HALF, 5)


# --- Group D (046-060): Momentum signal decay ---

def idc_046_mom5_decay_ratio_to_mom21(close: pd.Series) -> pd.Series:
    """Ratio of 5-day momentum magnitude to 21-day: high ratio = fast-decaying signal."""
    mom5 = close.pct_change(_TD_WEEK).abs()
    mom21 = close.pct_change(_TD_MON).abs()
    return _safe_div(mom5, mom21.clip(lower=_EPS))


def idc_047_mom5_decay_ratio_to_mom63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day momentum magnitude to 63-day momentum magnitude."""
    mom5 = close.pct_change(_TD_WEEK).abs()
    mom63 = close.pct_change(_TD_QTR).abs()
    return _safe_div(mom5, mom63.clip(lower=_EPS))


def idc_048_mom21_decay_ratio_to_mom126(close: pd.Series) -> pd.Series:
    """Ratio of 21-day momentum magnitude to 126-day momentum magnitude."""
    mom21 = close.pct_change(_TD_MON).abs()
    mom126 = close.pct_change(_TD_HALF).abs()
    return _safe_div(mom21, mom126.clip(lower=_EPS))


def idc_049_signed_mom5_vs_mom21_decay(close: pd.Series) -> pd.Series:
    """Signed: 5-day momentum minus 21-day momentum (sign flip = decay of short signal)."""
    return close.pct_change(_TD_WEEK) - close.pct_change(_TD_MON)


def idc_050_signed_mom21_vs_mom63_decay(close: pd.Series) -> pd.Series:
    """Signed: 21-day momentum minus 63-day momentum."""
    return close.pct_change(_TD_MON) - close.pct_change(_TD_QTR)


def idc_051_mom_decay_ac1_of_5d_returns_63d(close: pd.Series) -> pd.Series:
    """AC(1) of 5-day non-overlapping returns over 63-day window (weekly momentum decay)."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_autocorr(r5, _TD_QTR, 1)


def idc_052_mom_decay_ac1_of_21d_returns_126d(close: pd.Series) -> pd.Series:
    """AC(1) of 21-day returns over 126-day window (monthly momentum decay)."""
    r21 = close.pct_change(_TD_MON)
    return _rolling_autocorr(r21, _TD_HALF, 1)


def idc_053_mom_decay_slope_5d_to_21d_returns_63d(close: pd.Series) -> pd.Series:
    """
    OLS slope of AC(k) for k=1..4 using 5-day cumulative returns over 63-day window.
    Negative slope = momentum decaying with lag.
    """
    def _slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 12:
            return np.nan
        lags = [1, 2, 3, 4]
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs)
        if valid.sum() < 2:
            return np.nan
        lags_v = np.array(lags, dtype=float)[valid]
        acs_v = acs[valid]
        if lags_v.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags_v, acs_v, 1)[0])
    r5 = close.pct_change(_TD_WEEK).values
    n = len(r5)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _slope(r5[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_054_ewm5_vs_ewm21_decay(close: pd.Series) -> pd.Series:
    """EWM(5) price minus EWM(21) price normalized by EWM(21): fast vs slow decay."""
    e5 = _ewm_mean(close, _TD_WEEK)
    e21 = _ewm_mean(close, _TD_MON)
    return _safe_div(e5 - e21, e21.clip(lower=_EPS))


def idc_055_ewm21_vs_ewm63_decay(close: pd.Series) -> pd.Series:
    """EWM(21) price minus EWM(63) price normalized by EWM(63)."""
    e21 = _ewm_mean(close, _TD_MON)
    e63 = _ewm_mean(close, _TD_QTR)
    return _safe_div(e21 - e63, e63.clip(lower=_EPS))


def idc_056_mom_info_half_decay_21d_window(close: pd.Series) -> pd.Series:
    """
    Half-decay of momentum information: ratio of |rolling corr of current 5d return
    with lagged 5d return at lag=5| to |corr at lag=1| over 21-day window.
    """
    r5 = close.pct_change(_TD_WEEK)
    ac1 = _rolling_autocorr(r5, _TD_MON, 1)
    ac5 = _rolling_autocorr(r5, _TD_MON, 5)
    return _safe_div(ac5.abs(), ac1.abs().clip(lower=_EPS))


def idc_057_mom_decay_ewm_diff_vol_21d(close: pd.Series) -> pd.Series:
    """Std of (EWM5 - EWM21) over 21 days: volatility of decay spread."""
    decay = _safe_div(_ewm_mean(close, _TD_WEEK) - _ewm_mean(close, _TD_MON),
                      _ewm_mean(close, _TD_MON).clip(lower=_EPS))
    return _rolling_std(decay, _TD_MON)


def idc_058_mom_decay_ewm_diff_vol_63d(close: pd.Series) -> pd.Series:
    """Std of (EWM5 - EWM21)/EWM21 over 63 days."""
    decay = _safe_div(_ewm_mean(close, _TD_WEEK) - _ewm_mean(close, _TD_MON),
                      _ewm_mean(close, _TD_MON).clip(lower=_EPS))
    return _rolling_std(decay, _TD_QTR)


def idc_059_ac_decay_vol_series_lag1_lag2_63d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(1)/AC(2) of rolling 5-day realized volatility over 63-day window."""
    r = _returns(close)
    vol5 = r.rolling(_TD_WEEK, min_periods=2).std()
    ac1 = _rolling_autocorr(vol5, _TD_QTR, 1)
    ac2 = _rolling_autocorr(vol5, _TD_QTR, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_060_halflife_vol_cluster_63d(close: pd.Series) -> pd.Series:
    """Half-life of volatility clustering from AC(1)/AC(2) of |returns| over 63-day window."""
    ar = _returns(close).abs()
    ac1 = _rolling_autocorr(ar, _TD_QTR, 1)
    ac2 = _rolling_autocorr(ar, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


# --- Group E (061-075): Memory length and autocorrelation structure measures ---

def idc_061_ljung_box_q5_63d(close: pd.Series) -> pd.Series:
    """
    Ljung-Box Q statistic (sum over 5 lags) as a measure of total autocorrelation
    / residual memory over 63-day window.
    """
    def _lb5(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 15:
            return np.nan
        q = 0.0
        for k in range(1, 6):
            if n <= k + 1:
                break
            x0, x1 = x[:-k], x[k:]
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                continue
            rk = float(np.corrcoef(x0, x1)[0, 1])
            q += rk ** 2 / (n - k)
        return float(n * (n + 2) * q)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _lb5(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_062_ljung_box_q10_126d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q statistic (10 lags) over 126-day window."""
    def _lb10(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 25:
            return np.nan
        q = 0.0
        for k in range(1, 11):
            if n <= k + 1:
                break
            x0, x1 = x[:-k], x[k:]
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                continue
            rk = float(np.corrcoef(x0, x1)[0, 1])
            q += rk ** 2 / (n - k)
        return float(n * (n + 2) * q)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _lb10(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_063_ac_sum_lags_1_to_5_63d(close: pd.Series) -> pd.Series:
    """Sum of AC(1)..AC(5) of returns over 63-day window (total short-memory content)."""
    r = _returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(r, _TD_QTR, lag).fillna(0.0)
    return total


def idc_064_ac_abs_sum_lags_1_to_5_63d(close: pd.Series) -> pd.Series:
    """Sum of |AC(k)| for k=1..5 over 63-day window (total absolute memory)."""
    r = _returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(r, _TD_QTR, lag).abs().fillna(0.0)
    return total


def idc_065_ac_abs_sum_lags_1_to_10_126d(close: pd.Series) -> pd.Series:
    """Sum of |AC(k)| for k=1..10 over 126-day window."""
    r = _returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 11):
        total = total + _rolling_autocorr(r, _TD_HALF, lag).abs().fillna(0.0)
    return total


def idc_066_effective_memory_length_63d(close: pd.Series) -> pd.Series:
    """
    Effective memory length: weighted average lag using AC^2(k) as weights for k=1..5
    over 63-day window. Higher = slower decay / longer memory.
    """
    r = _returns(close)
    acs = [_rolling_autocorr(r, _TD_QTR, k) for k in range(1, 6)]
    weights = [a ** 2 for a in acs]
    wsum = sum(w.fillna(0.0) for w in weights)
    wlag = sum((i + 1) * w.fillna(0.0) for i, w in enumerate(weights))
    return _safe_div(wlag, wsum.clip(lower=_EPS))


def idc_067_effective_memory_length_126d(close: pd.Series) -> pd.Series:
    """Effective memory length using AC^2(k) weights for k=1..10 over 126-day window."""
    r = _returns(close)
    acs = [_rolling_autocorr(r, _TD_HALF, k) for k in range(1, 11)]
    weights = [a ** 2 for a in acs]
    wsum = sum(w.fillna(0.0) for w in weights)
    wlag = sum((i + 1) * w.fillna(0.0) for i, w in enumerate(weights))
    return _safe_div(wlag, wsum.clip(lower=_EPS))


def idc_068_ac_lag1_vs_lag5_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio |AC(1)| / |AC(5)| over 63-day window (steepness of short-term AC decay)."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1).abs()
    ac5 = _rolling_autocorr(r, _TD_QTR, 5).abs()
    return _safe_div(ac1, ac5.clip(lower=_EPS))


def idc_069_ac_lag1_vs_lag10_ratio_126d(close: pd.Series) -> pd.Series:
    """Ratio |AC(1)| / |AC(10)| over 126-day window (breadth of memory decay)."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1).abs()
    ac10 = _rolling_autocorr(r, _TD_HALF, 10).abs()
    return _safe_div(ac1, ac10.clip(lower=_EPS))


def idc_070_hurst_exp_63d(close: pd.Series) -> pd.Series:
    """
    Approximate Hurst exponent over 63-day window using R/S analysis on log returns.
    H < 0.5 = anti-persistent (fast decay), H = 0.5 = random, H > 0.5 = persistent.
    """
    def _hurst(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 10:
            return np.nan
        lags = []
        rs_vals = []
        for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
            if w > n:
                continue
            seg = x[:w]
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r_val = dev.max() - dev.min()
            s_val = seg.std()
            if s_val < _EPS:
                continue
            lags.append(np.log(w))
            rs_vals.append(np.log(r_val / s_val))
        if len(lags) < 2:
            return np.nan
        lags, rs_vals = np.array(lags), np.array(rs_vals)
        if lags.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags, rs_vals, 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _hurst(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_071_hurst_exp_126d(close: pd.Series) -> pd.Series:
    """Approximate Hurst exponent over 126-day window using R/S analysis."""
    def _hurst(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 12:
            return np.nan
        lags = []
        rs_vals = []
        for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
            if w > n:
                continue
            seg = x[:w]
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r_val = dev.max() - dev.min()
            s_val = seg.std()
            if s_val < _EPS:
                continue
            lags.append(np.log(w))
            rs_vals.append(np.log(r_val / s_val))
        if len(lags) < 2:
            return np.nan
        lags, rs_vals = np.array(lags), np.array(rs_vals)
        if lags.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags, rs_vals, 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _hurst(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_072_hurst_exp_252d(close: pd.Series) -> pd.Series:
    """Approximate Hurst exponent over 252-day window using R/S analysis."""
    def _hurst(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 16:
            return np.nan
        lags = []
        rs_vals = []
        for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
            if w > n:
                continue
            seg = x[:w]
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r_val = dev.max() - dev.min()
            s_val = seg.std()
            if s_val < _EPS:
                continue
            lags.append(np.log(w))
            rs_vals.append(np.log(r_val / s_val))
        if len(lags) < 2:
            return np.nan
        lags, rs_vals = np.array(lags), np.array(rs_vals)
        if lags.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags, rs_vals, 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_YEAR
    for i in range(w - 1, n):
        result[i] = _hurst(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_073_hurst_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Hurst exponent within its trailing 252-day distribution."""
    h = idc_070_hurst_exp_63d(close)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_074_ac_decay_rate_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day AC decay rate in trailing 252-day distribution."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    return rate.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_075_halflife_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day AC half-life in trailing 252-day distribution."""
    hl = idc_006_halflife_ac_decay_63d(close)
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

INFORMATION_DECAY_REGISTRY_001_075 = {
    "idc_001_ac_decay_lag1_lag2_63d": {"inputs": ["close"], "func": idc_001_ac_decay_lag1_lag2_63d},
    "idc_002_ac_decay_lag1_lag2_126d": {"inputs": ["close"], "func": idc_002_ac_decay_lag1_lag2_126d},
    "idc_003_ac_decay_lag1_lag2_252d": {"inputs": ["close"], "func": idc_003_ac_decay_lag1_lag2_252d},
    "idc_004_ac_decay_lag2_lag4_63d": {"inputs": ["close"], "func": idc_004_ac_decay_lag2_lag4_63d},
    "idc_005_ac_decay_lag2_lag4_126d": {"inputs": ["close"], "func": idc_005_ac_decay_lag2_lag4_126d},
    "idc_006_halflife_ac_decay_63d": {"inputs": ["close"], "func": idc_006_halflife_ac_decay_63d},
    "idc_007_halflife_ac_decay_126d": {"inputs": ["close"], "func": idc_007_halflife_ac_decay_126d},
    "idc_008_halflife_ac_decay_252d": {"inputs": ["close"], "func": idc_008_halflife_ac_decay_252d},
    "idc_009_ac_lag1_returns_63d": {"inputs": ["close"], "func": idc_009_ac_lag1_returns_63d},
    "idc_010_ac_lag1_returns_126d": {"inputs": ["close"], "func": idc_010_ac_lag1_returns_126d},
    "idc_011_ac_lag2_returns_63d": {"inputs": ["close"], "func": idc_011_ac_lag2_returns_63d},
    "idc_012_ac_lag3_returns_63d": {"inputs": ["close"], "func": idc_012_ac_lag3_returns_63d},
    "idc_013_ac_lag5_returns_63d": {"inputs": ["close"], "func": idc_013_ac_lag5_returns_63d},
    "idc_014_ac_lag5_returns_126d": {"inputs": ["close"], "func": idc_014_ac_lag5_returns_126d},
    "idc_015_ac_lag10_returns_126d": {"inputs": ["close"], "func": idc_015_ac_lag10_returns_126d},
    "idc_016_ewm_halflife_21d": {"inputs": ["close"], "func": idc_016_ewm_halflife_21d},
    "idc_017_ewm_halflife_63d": {"inputs": ["close"], "func": idc_017_ewm_halflife_63d},
    "idc_018_ewm_halflife_126d": {"inputs": ["close"], "func": idc_018_ewm_halflife_126d},
    "idc_019_ewm_halflife_252d": {"inputs": ["close"], "func": idc_019_ewm_halflife_252d},
    "idc_020_ewm_halflife_vs_21d_mean": {"inputs": ["close"], "func": idc_020_ewm_halflife_vs_21d_mean},
    "idc_021_ewm_halflife_abs_vol_21d": {"inputs": ["close"], "func": idc_021_ewm_halflife_abs_vol_21d},
    "idc_022_ewm_halflife_abs_vol_63d": {"inputs": ["close"], "func": idc_022_ewm_halflife_abs_vol_63d},
    "idc_023_ewm_halflife_abs_vol_126d": {"inputs": ["close"], "func": idc_023_ewm_halflife_abs_vol_126d},
    "idc_024_ewm_halflife_sq_vol_63d": {"inputs": ["close"], "func": idc_024_ewm_halflife_sq_vol_63d},
    "idc_025_ewm_halflife_sq_vol_252d": {"inputs": ["close"], "func": idc_025_ewm_halflife_sq_vol_252d},
    "idc_026_ewm_span_from_ac1_63d": {"inputs": ["close"], "func": idc_026_ewm_span_from_ac1_63d},
    "idc_027_ewm_span_from_ac1_126d": {"inputs": ["close"], "func": idc_027_ewm_span_from_ac1_126d},
    "idc_028_ewm_halflife_ratio_21d_to_252d": {"inputs": ["close"], "func": idc_028_ewm_halflife_ratio_21d_to_252d},
    "idc_029_ewm_halflife_ratio_63d_to_252d": {"inputs": ["close"], "func": idc_029_ewm_halflife_ratio_63d_to_252d},
    "idc_030_ewm_halflife_pct_rank_252d": {"inputs": ["close"], "func": idc_030_ewm_halflife_pct_rank_252d},
    "idc_031_shock_persistence_5d_63d": {"inputs": ["close"], "func": idc_031_shock_persistence_5d_63d},
    "idc_032_shock_persistence_10d_63d": {"inputs": ["close"], "func": idc_032_shock_persistence_10d_63d},
    "idc_033_shock_persistence_21d_126d": {"inputs": ["close"], "func": idc_033_shock_persistence_21d_126d},
    "idc_034_shock_persistence_ratio_5d_to_1d": {"inputs": ["close"], "func": idc_034_shock_persistence_ratio_5d_to_1d},
    "idc_035_shock_persistence_ratio_10d_to_1d": {"inputs": ["close"], "func": idc_035_shock_persistence_ratio_10d_to_1d},
    "idc_036_impulse_decay_vol_5d_to_21d": {"inputs": ["close"], "func": idc_036_impulse_decay_vol_5d_to_21d},
    "idc_037_impulse_decay_vol_5d_to_63d": {"inputs": ["close"], "func": idc_037_impulse_decay_vol_5d_to_63d},
    "idc_038_impulse_decay_vol_21d_to_63d": {"inputs": ["close"], "func": idc_038_impulse_decay_vol_21d_to_63d},
    "idc_039_impulse_decay_abs_return_5d_to_21d": {"inputs": ["close"], "func": idc_039_impulse_decay_abs_return_5d_to_21d},
    "idc_040_impulse_decay_abs_return_21d_to_126d": {"inputs": ["close"], "func": idc_040_impulse_decay_abs_return_21d_to_126d},
    "idc_041_return_memory_halflife_ols_63d": {"inputs": ["close"], "func": idc_041_return_memory_halflife_ols_63d},
    "idc_042_return_memory_halflife_ols_126d": {"inputs": ["close"], "func": idc_042_return_memory_halflife_ols_126d},
    "idc_043_ac_lag1_abs_returns_63d": {"inputs": ["close"], "func": idc_043_ac_lag1_abs_returns_63d},
    "idc_044_ac_lag1_abs_returns_126d": {"inputs": ["close"], "func": idc_044_ac_lag1_abs_returns_126d},
    "idc_045_ac_lag5_abs_returns_126d": {"inputs": ["close"], "func": idc_045_ac_lag5_abs_returns_126d},
    "idc_046_mom5_decay_ratio_to_mom21": {"inputs": ["close"], "func": idc_046_mom5_decay_ratio_to_mom21},
    "idc_047_mom5_decay_ratio_to_mom63": {"inputs": ["close"], "func": idc_047_mom5_decay_ratio_to_mom63},
    "idc_048_mom21_decay_ratio_to_mom126": {"inputs": ["close"], "func": idc_048_mom21_decay_ratio_to_mom126},
    "idc_049_signed_mom5_vs_mom21_decay": {"inputs": ["close"], "func": idc_049_signed_mom5_vs_mom21_decay},
    "idc_050_signed_mom21_vs_mom63_decay": {"inputs": ["close"], "func": idc_050_signed_mom21_vs_mom63_decay},
    "idc_051_mom_decay_ac1_of_5d_returns_63d": {"inputs": ["close"], "func": idc_051_mom_decay_ac1_of_5d_returns_63d},
    "idc_052_mom_decay_ac1_of_21d_returns_126d": {"inputs": ["close"], "func": idc_052_mom_decay_ac1_of_21d_returns_126d},
    "idc_053_mom_decay_slope_5d_to_21d_returns_63d": {"inputs": ["close"], "func": idc_053_mom_decay_slope_5d_to_21d_returns_63d},
    "idc_054_ewm5_vs_ewm21_decay": {"inputs": ["close"], "func": idc_054_ewm5_vs_ewm21_decay},
    "idc_055_ewm21_vs_ewm63_decay": {"inputs": ["close"], "func": idc_055_ewm21_vs_ewm63_decay},
    "idc_056_mom_info_half_decay_21d_window": {"inputs": ["close"], "func": idc_056_mom_info_half_decay_21d_window},
    "idc_057_mom_decay_ewm_diff_vol_21d": {"inputs": ["close"], "func": idc_057_mom_decay_ewm_diff_vol_21d},
    "idc_058_mom_decay_ewm_diff_vol_63d": {"inputs": ["close"], "func": idc_058_mom_decay_ewm_diff_vol_63d},
    "idc_059_ac_decay_vol_series_lag1_lag2_63d": {"inputs": ["close"], "func": idc_059_ac_decay_vol_series_lag1_lag2_63d},
    "idc_060_halflife_vol_cluster_63d": {"inputs": ["close"], "func": idc_060_halflife_vol_cluster_63d},
    "idc_061_ljung_box_q5_63d": {"inputs": ["close"], "func": idc_061_ljung_box_q5_63d},
    "idc_062_ljung_box_q10_126d": {"inputs": ["close"], "func": idc_062_ljung_box_q10_126d},
    "idc_063_ac_sum_lags_1_to_5_63d": {"inputs": ["close"], "func": idc_063_ac_sum_lags_1_to_5_63d},
    "idc_064_ac_abs_sum_lags_1_to_5_63d": {"inputs": ["close"], "func": idc_064_ac_abs_sum_lags_1_to_5_63d},
    "idc_065_ac_abs_sum_lags_1_to_10_126d": {"inputs": ["close"], "func": idc_065_ac_abs_sum_lags_1_to_10_126d},
    "idc_066_effective_memory_length_63d": {"inputs": ["close"], "func": idc_066_effective_memory_length_63d},
    "idc_067_effective_memory_length_126d": {"inputs": ["close"], "func": idc_067_effective_memory_length_126d},
    "idc_068_ac_lag1_vs_lag5_ratio_63d": {"inputs": ["close"], "func": idc_068_ac_lag1_vs_lag5_ratio_63d},
    "idc_069_ac_lag1_vs_lag10_ratio_126d": {"inputs": ["close"], "func": idc_069_ac_lag1_vs_lag10_ratio_126d},
    "idc_070_hurst_exp_63d": {"inputs": ["close"], "func": idc_070_hurst_exp_63d},
    "idc_071_hurst_exp_126d": {"inputs": ["close"], "func": idc_071_hurst_exp_126d},
    "idc_072_hurst_exp_252d": {"inputs": ["close"], "func": idc_072_hurst_exp_252d},
    "idc_073_hurst_pct_rank_252d": {"inputs": ["close"], "func": idc_073_hurst_pct_rank_252d},
    "idc_074_ac_decay_rate_pct_rank_252d": {"inputs": ["close"], "func": idc_074_ac_decay_rate_pct_rank_252d},
    "idc_075_halflife_pct_rank_252d": {"inputs": ["close"], "func": idc_075_halflife_pct_rank_252d},
}
