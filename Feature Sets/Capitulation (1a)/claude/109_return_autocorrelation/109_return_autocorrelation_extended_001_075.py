"""
109_return_autocorrelation — Extended Features 001-075
Domain: autocorrelation and serial-dependence structure of returns — deeper variants including
        regime-conditional AC, multi-scale AC patterns, AC of downside/upside returns separately,
        volume-return cross-AC, overlapping VR, DFA-like scaling, multi-lag composites,
        AC stability metrics, and capitulation-specific serial-structure signals
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation. NaN-safe."""
    def _ac(x):
        arr = x[~np.isnan(x)]
        if len(arr) < max(lag + 2, w // 2):
            return np.nan
        if len(arr) <= lag:
            return np.nan
        x1 = arr[:-lag]
        x2 = arr[lag:]
        if len(x1) < 2:
            return np.nan
        m1, m2 = x1.mean(), x2.mean()
        num = ((x1 - m1) * (x2 - m2)).mean()
        den = x1.std(ddof=0) * x2.std(ddof=0)
        if den < _EPS:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).apply(_ac, raw=True)


def _variance_ratio(s: pd.Series, w: int, k: int) -> pd.Series:
    """Rolling variance ratio. NaN-safe."""
    def _vr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(k + 2, w // 2):
            return np.nan
        var1 = np.var(arr[1:] - arr[:-1], ddof=1) if n > 1 else np.nan
        if n < k + 1:
            return np.nan
        kret = arr[k:] - arr[:-k]
        vark = np.var(kret, ddof=1) if len(kret) > 1 else np.nan
        if var1 is None or np.isnan(var1) or var1 < _EPS:
            return np.nan
        return vark / (k * var1)
    return s.rolling(w, min_periods=max(k + 2, w // 2)).apply(_vr, raw=True)


def _hurst_rs(s: pd.Series, w: int) -> pd.Series:
    """Rolling R/S Hurst exponent. NaN-safe."""
    def _h(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(8, w // 2):
            return np.nan
        mean = arr.mean()
        deviations = arr - mean
        cumdev = np.cumsum(deviations)
        r = cumdev.max() - cumdev.min()
        s_std = arr.std(ddof=1)
        if s_std < _EPS or r <= 0:
            return np.nan
        return np.log(r / s_std) / np.log(n)
    return s.rolling(w, min_periods=max(8, w // 2)).apply(_h, raw=True)


def _runs_ratio(s: pd.Series, w: int) -> pd.Series:
    """Rolling runs ratio."""
    def _rr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(4, w // 2):
            return np.nan
        signs = np.sign(arr)
        runs = 1
        for i in range(1, n):
            if signs[i] != signs[i - 1]:
                runs += 1
        n_pos = np.sum(signs > 0)
        n_neg = np.sum(signs < 0)
        if n_pos == 0 or n_neg == 0:
            return np.nan
        expected = (2.0 * n_pos * n_neg / n) + 1.0
        if expected < _EPS:
            return np.nan
        return runs / expected
    return s.rolling(w, min_periods=max(4, w // 2)).apply(_rr, raw=True)


def _ljung_box_stat(s: pd.Series, w: int, max_lag: int) -> pd.Series:
    """Rolling Ljung-Box Q-statistic."""
    def _lb(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(max_lag + 2, w // 2):
            return np.nan
        q = 0.0
        for k in range(1, max_lag + 1):
            x1 = arr[:-k]
            x2 = arr[k:]
            m1, m2 = x1.mean(), x2.mean()
            num = ((x1 - m1) * (x2 - m2)).mean()
            den = x1.std(ddof=0) * x2.std(ddof=0)
            rk = num / den if den > _EPS else 0.0
            q += rk ** 2 / (n - k)
        return n * (n + 2) * q
    return s.rolling(w, min_periods=max(max_lag + 2, w // 2)).apply(_lb, raw=True)


def _rolling_corr(x: pd.Series, y: pd.Series, w: int) -> pd.Series:
    """Rolling Pearson correlation between x and y. NaN-safe."""
    def _corr(idx):
        return np.nan
    return x.rolling(w, min_periods=max(3, w // 2)).corr(y)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Asymmetric AC — downside vs upside returns ---

def rac_ext_001_down_ret_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """AC at lag 1 of negative log-returns only (zeroed on up days) over 63d window."""
    r = _log_returns(close)
    down = r.where(r < 0, 0.0)
    return _rolling_autocorr(down, _TD_QTR, 1)


def rac_ext_002_up_ret_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """AC at lag 1 of positive log-returns only (zeroed on down days) over 63d window."""
    r = _log_returns(close)
    up = r.where(r > 0, 0.0)
    return _rolling_autocorr(up, _TD_QTR, 1)


def rac_ext_003_down_minus_up_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Down-return AC lag 1 minus up-return AC lag 1 over 63d (asymmetric serial structure)."""
    r = _log_returns(close)
    down = r.where(r < 0, 0.0)
    up = r.where(r > 0, 0.0)
    return _rolling_autocorr(down, _TD_QTR, 1) - _rolling_autocorr(up, _TD_QTR, 1)


def rac_ext_004_extreme_down_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """AC of returns below bottom-quintile threshold at lag 1 over 63d window."""
    r = _log_returns(close)
    threshold = r.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).quantile(0.2)
    extreme_down = r.where(r < threshold, 0.0)
    return _rolling_autocorr(extreme_down, _TD_QTR, 1)


def rac_ext_005_down_sign_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Sign AC at lag 1 restricted to negative-return days over 63d window."""
    r = _log_returns(close)
    down_sign = np.sign(r).where(r < 0, 0.0)
    return _rolling_autocorr(down_sign, _TD_QTR, 1)


def rac_ext_006_vr_2_down_days_63d(close: pd.Series) -> pd.Series:
    """VR(k=2) computed only on down-day log-prices over 63d window."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    down_lp = lp.where(r < 0, np.nan)
    return _variance_ratio(down_lp, _TD_QTR, 2)


def rac_ext_007_abs_ac_down_ret_lag1_63d(close: pd.Series) -> pd.Series:
    """|AC lag 1| of |down-returns| over 63d (volatility clustering on down days)."""
    r = _log_returns(close)
    down_abs = r.abs().where(r < 0, 0.0)
    return _rolling_autocorr(down_abs, _TD_QTR, 1)


def rac_ext_008_down_ret_runs_ratio_63d(close: pd.Series) -> pd.Series:
    """Runs ratio of sign applied only to non-zero down-days over 63d window."""
    r = _log_returns(close)
    down = r.where(r < 0, np.nan)
    return _runs_ratio(down, _TD_QTR)


def rac_ext_009_down_ret_lb_q4_63d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q(4) of returns floored at 0 (down-side only) over 63d window."""
    r = _log_returns(close)
    down = r.where(r < 0, 0.0)
    return _ljung_box_stat(down, _TD_QTR, 4)


def rac_ext_010_ac_lag1_63d_down_regime(close: pd.Series) -> pd.Series:
    """AC lag 1 (63d) multiplied by sign of 21d price trend (regime-conditional AC)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    trend = np.sign(_rolling_mean(r, _TD_MON))
    return ac * trend


# --- Group B (011-020): Multi-scale variance ratio patterns ---

def rac_ext_011_vr_term_structure_2_5_10_63d(close: pd.Series) -> pd.Series:
    """VR term structure slope: OLS slope of [VR(2), VR(5), VR(10)] over 63d."""
    lp = np.log(close.replace(0, np.nan))
    vr2 = _variance_ratio(lp, _TD_QTR, 2)
    vr5 = _variance_ratio(lp, _TD_QTR, 5)
    vr10 = _variance_ratio(lp, _TD_QTR, 10)
    # Slope of (2,5,10) -> (vr2, vr5, vr10): approximated as (vr10-vr2)/8
    return _safe_div(vr10 - vr2, pd.Series(8.0, index=close.index))


def rac_ext_012_vr_2_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day VR(k=2) to 252-day VR(k=2) (short vs long regime comparison)."""
    lp = np.log(close.replace(0, np.nan))
    vr63 = _variance_ratio(lp, _TD_QTR, 2)
    vr252 = _variance_ratio(lp, _TD_YEAR, 2)
    return _safe_div(vr63, vr252.clip(lower=_EPS))


def rac_ext_013_vr_5_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day VR(k=5) to 252-day VR(k=5)."""
    lp = np.log(close.replace(0, np.nan))
    vr63 = _variance_ratio(lp, _TD_QTR, 5)
    vr252 = _variance_ratio(lp, _TD_YEAR, 5)
    return _safe_div(vr63, vr252.clip(lower=_EPS))


def rac_ext_014_vr_cross_scale_convexity_126d(close: pd.Series) -> pd.Series:
    """VR convexity: VR(10) - 2*VR(5) + VR(2) over 126d (curvature of VR term structure)."""
    lp = np.log(close.replace(0, np.nan))
    vr2 = _variance_ratio(lp, _TD_HALF, 2)
    vr5 = _variance_ratio(lp, _TD_HALF, 5)
    vr10 = _variance_ratio(lp, _TD_HALF, 10)
    return vr10 - 2.0 * vr5 + vr2


def rac_ext_015_vr_2_weekly_agg_63d(close: pd.Series) -> pd.Series:
    """VR(k=2) of weekly-aggregated returns over 63-day window."""
    r = _log_returns(close)
    weekly = r.rolling(5, min_periods=3).sum()
    lp_weekly = weekly.cumsum()
    return _variance_ratio(lp_weekly, _TD_QTR, 2)


def rac_ext_016_vr_5_monthly_agg_252d(close: pd.Series) -> pd.Series:
    """VR(k=5) of monthly-aggregated returns over 252-day window."""
    r = _log_returns(close)
    monthly = r.rolling(_TD_MON, min_periods=10).sum()
    lp_monthly = monthly.cumsum()
    return _variance_ratio(lp_monthly, _TD_YEAR, 5)


def rac_ext_017_vr_2_high_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """VR(k=2) of log(high/low) range series over 63d (range-based VR)."""
    rng = np.log((high / low.replace(0, np.nan)).replace(0, np.nan))
    lp = rng.cumsum()
    return _variance_ratio(lp, _TD_QTR, 2)


def rac_ext_018_vr_overlapping_5_126d(close: pd.Series) -> pd.Series:
    """Overlapping VR(k=5) over 126d: uses (n-4) overlapping 5-day returns."""
    def _ovlp_vr5(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < 10:
            return np.nan
        r1 = arr[1:] - arr[:-1]
        var1 = np.var(r1, ddof=1) if len(r1) > 1 else np.nan
        if var1 is None or np.isnan(var1) or var1 < _EPS:
            return np.nan
        r5 = arr[5:] - arr[:-5]
        # overlapping variance estimate
        vk = 0.0
        for j in range(len(r5)):
            vk += r5[j] ** 2
        vk = vk / (len(r5) - 1) if len(r5) > 1 else np.nan
        if vk is None or np.isnan(vk):
            return np.nan
        return vk / (5 * var1)
    lp = np.log(close.replace(0, np.nan))
    return lp.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(_ovlp_vr5, raw=True)


def rac_ext_019_vr_5_vs_hurst_63d(close: pd.Series) -> pd.Series:
    """Product of VR(k=5) and Hurst R/S over 63d (amplified persistence indicator)."""
    lp = np.log(close.replace(0, np.nan))
    r = _log_returns(close)
    vr = _variance_ratio(lp, _TD_QTR, 5)
    h = _hurst_rs(r, _TD_QTR)
    return vr * h


def rac_ext_020_vr_2_min_expanding(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day VR(k=2) (all-time minimum variance ratio)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    return vr.expanding(min_periods=_TD_QTR).min()


# --- Group C (021-030): AC of alternative return definitions ---

def rac_ext_021_log_hl_ratio_ac_lag1_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC lag 1 of log(high/low) daily range over 63d window."""
    rng = np.log((high / low.replace(0, np.nan)).replace(0, np.nan))
    return _rolling_autocorr(rng, _TD_QTR, 1)


def rac_ext_022_log_hl_ratio_ac_lag1_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC lag 1 of log(high/low) daily range over 126d window."""
    rng = np.log((high / low.replace(0, np.nan)).replace(0, np.nan))
    return _rolling_autocorr(rng, _TD_HALF, 1)


def rac_ext_023_open_ret_ac_lag1_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """AC lag 1 of open-to-open returns over 63d window."""
    oo = np.log((open_ / open_.shift(1)).replace(0, np.nan))
    return _rolling_autocorr(oo, _TD_QTR, 1)


def rac_ext_024_gap_ac_lag2_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """AC at lag 2 of overnight gap returns over 63d window."""
    gap = np.log((open_ / close.shift(1)).replace(0, np.nan))
    return _rolling_autocorr(gap, _TD_QTR, 2)


def rac_ext_025_intraday_ret_ac_lag1_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """AC lag 1 of intraday (open-to-close) returns over 63d window."""
    oc = np.log((close / open_).replace(0, np.nan))
    return _rolling_autocorr(oc, _TD_QTR, 1)


def rac_ext_026_volume_ret_joint_ac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """AC lag 1 of (return * log-volume) product series over 63d (return-volume joint AC)."""
    r = _log_returns(close)
    lv = np.log(volume.replace(0, np.nan))
    rvol = r * lv
    return _rolling_autocorr(rvol, _TD_QTR, 1)


def rac_ext_027_volume_ret_cross_lag2_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cross-correlation: current volume vs return 2 days ago over 63d."""
    r = _log_returns(close)
    lv = np.log(volume.replace(0, np.nan))
    return _rolling_autocorr(lv - r.shift(2), _TD_QTR, 1)


def rac_ext_028_squared_ret_ac_lag5_63d(close: pd.Series) -> pd.Series:
    """AC of squared returns at lag 5 over 63d (weekly volatility clustering)."""
    r = _log_returns(close)
    return _rolling_autocorr(r ** 2, _TD_QTR, 5)


def rac_ext_029_abs_ret_ac_lag5_126d(close: pd.Series) -> pd.Series:
    """AC of |returns| at lag 5 over 126d."""
    r = _log_returns(close)
    return _rolling_autocorr(r.abs(), _TD_HALF, 5)


def rac_ext_030_abs_ret_ac_lag21_252d(close: pd.Series) -> pd.Series:
    """AC of |returns| at lag 21 over 252d (monthly volatility-clustering memory)."""
    r = _log_returns(close)
    return _rolling_autocorr(r.abs(), _TD_YEAR, 21)


# --- Group D (031-040): AC stability and regime metrics ---

def rac_ext_031_ac_lag1_std_63d_252d(close: pd.Series) -> pd.Series:
    """Rolling std of 21-day lag-1 AC over 252-day window (AC instability)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_std(ac, _TD_YEAR)


def rac_ext_032_vr5_std_252d(close: pd.Series) -> pd.Series:
    """Rolling std of 63-day VR(k=5) over 252-day window (VR instability)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 5)
    return _rolling_std(vr, _TD_YEAR)


def rac_ext_033_hurst_std_252d(close: pd.Series) -> pd.Series:
    """Rolling std of 63-day Hurst R/S over 252-day window (Hurst instability)."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return _rolling_std(h, _TD_YEAR)


def rac_ext_034_ac_lag1_regime_change_63d(close: pd.Series) -> pd.Series:
    """Number of sign-changes in 21-day lag-1 AC over 63-day window (regime flipping count)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    sign_changes = (np.sign(ac) != np.sign(ac.shift(1))).astype(float)
    return _rolling_sum(sign_changes, _TD_QTR)


def rac_ext_035_vr5_regime_change_63d(close: pd.Series) -> pd.Series:
    """Number of times VR(k=5) 63d crosses 1.0 over 63-day window (VR regime flips)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 5)
    cross = (np.sign(vr - 1.0) != np.sign((vr - 1.0).shift(1))).astype(float)
    return _rolling_sum(cross, _TD_QTR)


def rac_ext_036_days_ac_lag1_extreme_neg_63d(close: pd.Series) -> pd.Series:
    """Count of days in 63d window where 21d lag-1 AC < -0.2 (deep mean-reversion)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_sum((ac < -0.2).astype(float), _TD_QTR)


def rac_ext_037_days_hurst_below_04_252d(close: pd.Series) -> pd.Series:
    """Count of days in 252d window where 63d Hurst R/S < 0.4 (strong anti-persistence)."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return _rolling_sum((h < 0.4).astype(float), _TD_YEAR)


def rac_ext_038_serial_struct_stability_252d(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of 21d lag-1 AC over 252d (AC stability over year)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    mean_ac = _rolling_mean(ac, _TD_YEAR)
    return _rolling_mean((ac - mean_ac).abs(), _TD_YEAR)


def rac_ext_039_hurst_pct_rank_252d_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 63-day Hurst R/S."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return h.expanding(min_periods=_TD_QTR).rank(pct=True)


def rac_ext_040_vr2_pct_rank_252d_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 63-day VR(k=2)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    return vr.expanding(min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Composite and interaction features ---

def rac_ext_041_anti_persist_regime_days_252d(close: pd.Series) -> pd.Series:
    """Days in 252d window where anti-persistence composite (AC+VR+Hurst) < 0."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    neg_ac = -_rolling_autocorr(r, _TD_QTR, 1).fillna(0.0)
    neg_vr = (1.0 - _variance_ratio(lp, _TD_QTR, 5).fillna(1.0))
    neg_h = (0.5 - _hurst_rs(r, _TD_QTR).fillna(0.5))
    score = neg_ac + neg_vr + neg_h
    return _rolling_sum((score > 0).astype(float), _TD_YEAR)


def rac_ext_042_triple_agree_mean_rev_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: AC<0 AND VR<1 AND Hurst<0.5 all simultaneously (strong mean-reversion)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    vr = _variance_ratio(lp, _TD_QTR, 5)
    h = _hurst_rs(r, _TD_QTR)
    return ((ac < 0) & (vr < 1.0) & (h < 0.5)).astype(float)


def rac_ext_043_triple_agree_persist_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: AC>0 AND VR>1 AND Hurst>0.5 all simultaneously (strong persistence)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    vr = _variance_ratio(lp, _TD_QTR, 5)
    h = _hurst_rs(r, _TD_QTR)
    return ((ac > 0) & (vr > 1.0) & (h > 0.5)).astype(float)


def rac_ext_044_consec_days_triple_mean_rev_63d(close: pd.Series) -> pd.Series:
    """Consecutive days with triple-agree mean-reversion (AC<0 & VR<1 & H<0.5) using 63d."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    vr = _variance_ratio(lp, _TD_QTR, 5)
    h = _hurst_rs(r, _TD_QTR)
    cond = (ac < 0) & (vr < 1.0) & (h < 0.5)
    return _consec_streak(cond)


def rac_ext_045_lb_q4_63d_times_abs_ac_lag1(close: pd.Series) -> pd.Series:
    """Product of LB(4) 63d Q-stat and |lag-1 AC| (joint signal strength)."""
    r = _log_returns(close)
    lb = _ljung_box_stat(r, _TD_QTR, 4)
    ac_abs = _rolling_autocorr(r, _TD_QTR, 1).abs()
    return lb * ac_abs


def rac_ext_046_hurst_times_runs_ratio_63d(close: pd.Series) -> pd.Series:
    """Product of Hurst R/S and runs ratio over 63d (agreement of serial structure metrics)."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    rr = _runs_ratio(r, _TD_QTR)
    return h * rr


def rac_ext_047_ac_lag1_times_lb_q4_ratio_63d(close: pd.Series) -> pd.Series:
    """AC lag 1 (63d) scaled by LB Q(4)/4 (AC magnitude weighted by test strength)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    lb_norm = _ljung_box_stat(r, _TD_QTR, 4) / 4.0
    return ac * lb_norm


def rac_ext_048_vr5_126d_times_hurst_126d(close: pd.Series) -> pd.Series:
    """Product of VR(k=5) 126d and Hurst 126d (amplified long-horizon persistence)."""
    lp = np.log(close.replace(0, np.nan))
    r = _log_returns(close)
    vr = _variance_ratio(lp, _TD_HALF, 5)
    h = _hurst_rs(r, _TD_HALF)
    return vr * h


def rac_ext_049_mean_rev_intensity_63d(close: pd.Series) -> pd.Series:
    """Mean-reversion intensity: depth of AC below 0, depth of VR below 1, depth of H below 0.5."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    neg_ac_depth = (-_rolling_autocorr(r, _TD_QTR, 1)).clip(lower=0.0).fillna(0.0)
    neg_vr_depth = (1.0 - _variance_ratio(lp, _TD_QTR, 5)).clip(lower=0.0).fillna(0.0)
    neg_h_depth = (0.5 - _hurst_rs(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    return neg_ac_depth + neg_vr_depth + neg_h_depth


def rac_ext_050_persist_intensity_63d(close: pd.Series) -> pd.Series:
    """Persistence intensity: depth of AC above 0, depth of VR above 1, depth of H above 0.5."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    pos_ac_depth = _rolling_autocorr(r, _TD_QTR, 1).clip(lower=0.0).fillna(0.0)
    pos_vr_depth = (_variance_ratio(lp, _TD_QTR, 5) - 1.0).clip(lower=0.0).fillna(0.0)
    pos_h_depth = (_hurst_rs(r, _TD_QTR) - 0.5).clip(lower=0.0).fillna(0.0)
    return pos_ac_depth + pos_vr_depth + pos_h_depth


# --- Group F (051-063): DFA-like, multi-period AC patterns, higher-lag composites ---

def rac_ext_051_ac_lag1_below_lag2_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: |AC lag 1| > |AC lag 2| over 63d (monotone AC decay from lag 1)."""
    r = _log_returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1).abs()
    ac2 = _rolling_autocorr(r, _TD_QTR, 2).abs()
    return (ac1 > ac2).astype(float)


def rac_ext_052_ac_sum_even_lags_63d(close: pd.Series) -> pd.Series:
    """Sum of AC at even lags (2, 4) over 63d (alternating pattern signature)."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in [2, 4]:
        total = total + _rolling_autocorr(r, _TD_QTR, lag).fillna(0.0)
    return total


def rac_ext_053_ac_sum_odd_lags_63d(close: pd.Series) -> pd.Series:
    """Sum of AC at odd lags (1, 3, 5) over 63d."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in [1, 3, 5]:
        total = total + _rolling_autocorr(r, _TD_QTR, lag).fillna(0.0)
    return total


def rac_ext_054_ac_lag_crossover_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: AC lag 1 changed sign from previous 21d value (AC crossover event)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return (np.sign(ac) != np.sign(ac.shift(_TD_MON))).astype(float)


def rac_ext_055_hurst_acf_lag1_divergence_63d(close: pd.Series) -> pd.Series:
    """Divergence: Hurst R/S (63d) minus AC_lag1 (63d) — do metrics agree?"""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return h - ac


def rac_ext_056_vr5_vs_ac_lag1_divergence_63d(close: pd.Series) -> pd.Series:
    """Divergence: VR(k=5) 63d minus AC lag 1 63d (VR vs direct AC comparison)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 5)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return vr - ac


def rac_ext_057_ac_lag1_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day lag-1 AC within its 252-day distribution."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_ext_058_hurst_rs_21d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over 21-day window (short-horizon memory)."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_MON)


def rac_ext_059_hurst_rs_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day Hurst R/S vs its 252-day distribution."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_MON)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def rac_ext_060_lb_q8_63d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q(8) of log-returns over 63-day window (8 lags serial dependence)."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_QTR, 8)


def rac_ext_061_lb_q4_63d_per_unit_var(close: pd.Series) -> pd.Series:
    """LB Q(4) 63d divided by return variance (size-adjusted serial dependence)."""
    r = _log_returns(close)
    lb = _ljung_box_stat(r, _TD_QTR, 4)
    var = _rolling_std(r, _TD_QTR) ** 2
    return _safe_div(lb, var.clip(lower=_EPS))


def rac_ext_062_runs_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Difference: 21-day runs ratio minus 63-day runs ratio."""
    r = _log_returns(close)
    rr21 = _runs_ratio(r, _TD_MON)
    rr63 = _runs_ratio(r, _TD_QTR)
    return rr21 - rr63


def rac_ext_063_abs_ret_lb_q4_63d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q(4) of |log-returns| over 63d (volatility clustering test statistic)."""
    r = _log_returns(close)
    return _ljung_box_stat(r.abs(), _TD_QTR, 4)


# --- Group G (064-075): Capitulation-specific serial signals ---

def rac_ext_064_down_streak_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """AC lag 1 of daily down-streak lengths over 63d (serial structure of loss runs)."""
    r = _log_returns(close)
    down_streak = _consec_streak(r < 0).astype(float)
    return _rolling_autocorr(down_streak, _TD_QTR, 1)


def rac_ext_065_down_depth_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """AC lag 1 of cumulative drawdown depth over 63d (persistence of drawdown deepening)."""
    r = _log_returns(close)
    cum = r.cumsum()
    drawdown = cum - cum.rolling(_TD_QTR, min_periods=1).max()
    return _rolling_autocorr(drawdown, _TD_QTR, 1)


def rac_ext_066_vr2_down_days_126d(close: pd.Series) -> pd.Series:
    """VR(k=2) computed only on days with negative log-returns over 126d."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    down_lp = lp.where(r < 0, np.nan)
    return _variance_ratio(down_lp, _TD_HALF, 2)


def rac_ext_067_hurst_down_days_63d(close: pd.Series) -> pd.Series:
    """R/S Hurst of negative log-returns (zeroed on up days) over 63d."""
    r = _log_returns(close)
    down = r.where(r < 0, 0.0)
    return _hurst_rs(down, _TD_QTR)


def rac_ext_068_mean_rev_intensity_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day mean-reversion intensity score vs its 252-day distribution."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    neg_ac = (-_rolling_autocorr(r, _TD_MON, 1)).clip(lower=0.0).fillna(0.0)
    neg_vr = (1.0 - _variance_ratio(lp, _TD_MON, 2)).clip(lower=0.0).fillna(0.0)
    score = neg_ac + neg_vr
    m = _rolling_mean(score, _TD_YEAR)
    s = _rolling_std(score, _TD_YEAR)
    return _safe_div(score - m, s)


def rac_ext_069_capitulation_serial_score_63d(close: pd.Series) -> pd.Series:
    """Composite capitulation serial score: large down-AC + mean-reversion VR + anti-Hurst."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac_comp = (-_rolling_autocorr(r, _TD_QTR, 1)).clip(lower=0.0).fillna(0.0)
    vr_comp = (1.0 - _variance_ratio(lp, _TD_QTR, 5)).clip(lower=0.0).fillna(0.0)
    h_comp = (0.5 - _hurst_rs(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    rr_comp = (1.0 - _runs_ratio(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    return ac_comp + vr_comp + h_comp + rr_comp


def rac_ext_070_consec_mean_rev_triple_agree_252d(close: pd.Series) -> pd.Series:
    """Count of triple-agree mean-reversion days (AC<0 & VR<1 & H<0.5) in trailing 252d."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    vr = _variance_ratio(lp, _TD_QTR, 5)
    h = _hurst_rs(r, _TD_QTR)
    flag = ((ac < 0) & (vr < 1.0) & (h < 0.5)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def rac_ext_071_ac_lag1_63d_new_low_252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63-day lag-1 AC is at its lowest level in the trailing 252 days."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    prev_min = ac.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (ac < prev_min).astype(float)


def rac_ext_072_vr5_126d_new_low_252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 126-day VR(k=5) is at its lowest level in the trailing 252 days."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_HALF, 5)
    prev_min = vr.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (vr < prev_min).astype(float)


def rac_ext_073_serial_struct_diff_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Composite serial structure 21d minus 252d: how much shorter-window diverges from long."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac21 = _rolling_autocorr(r, _TD_MON, 1).fillna(0.0)
    vr21 = (_variance_ratio(lp, _TD_MON, 2).fillna(1.0) - 1.0)
    short = ac21 + vr21
    ac252 = _rolling_autocorr(r, _TD_YEAR, 1).fillna(0.0)
    vr252 = (_variance_ratio(lp, _TD_YEAR, 5).fillna(1.0) - 1.0)
    long_ = ac252 + vr252
    return short - long_


def rac_ext_074_capitulation_serial_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the 63d capitulation serial score vs its 252d distribution."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac_comp = (-_rolling_autocorr(r, _TD_QTR, 1)).clip(lower=0.0).fillna(0.0)
    vr_comp = (1.0 - _variance_ratio(lp, _TD_QTR, 5)).clip(lower=0.0).fillna(0.0)
    h_comp = (0.5 - _hurst_rs(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    rr_comp = (1.0 - _runs_ratio(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    score = ac_comp + vr_comp + h_comp + rr_comp
    m = _rolling_mean(score, _TD_YEAR)
    s = _rolling_std(score, _TD_YEAR)
    return _safe_div(score - m, s)


def rac_ext_075_mean_rev_score_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of the 63d capitulation serial score."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac_comp = (-_rolling_autocorr(r, _TD_QTR, 1)).clip(lower=0.0).fillna(0.0)
    vr_comp = (1.0 - _variance_ratio(lp, _TD_QTR, 5)).clip(lower=0.0).fillna(0.0)
    h_comp = (0.5 - _hurst_rs(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    rr_comp = (1.0 - _runs_ratio(r, _TD_QTR)).clip(lower=0.0).fillna(0.0)
    score = ac_comp + vr_comp + h_comp + rr_comp
    return score.expanding(min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_AUTOCORRELATION_EXTENDED_REGISTRY_001_075 = {
    "rac_ext_001_down_ret_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_001_down_ret_ac_lag1_63d},
    "rac_ext_002_up_ret_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_002_up_ret_ac_lag1_63d},
    "rac_ext_003_down_minus_up_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_003_down_minus_up_ac_lag1_63d},
    "rac_ext_004_extreme_down_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_004_extreme_down_ac_lag1_63d},
    "rac_ext_005_down_sign_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_005_down_sign_ac_lag1_63d},
    "rac_ext_006_vr_2_down_days_63d": {"inputs": ["close"], "func": rac_ext_006_vr_2_down_days_63d},
    "rac_ext_007_abs_ac_down_ret_lag1_63d": {"inputs": ["close"], "func": rac_ext_007_abs_ac_down_ret_lag1_63d},
    "rac_ext_008_down_ret_runs_ratio_63d": {"inputs": ["close"], "func": rac_ext_008_down_ret_runs_ratio_63d},
    "rac_ext_009_down_ret_lb_q4_63d": {"inputs": ["close"], "func": rac_ext_009_down_ret_lb_q4_63d},
    "rac_ext_010_ac_lag1_63d_down_regime": {"inputs": ["close"], "func": rac_ext_010_ac_lag1_63d_down_regime},
    "rac_ext_011_vr_term_structure_2_5_10_63d": {"inputs": ["close"], "func": rac_ext_011_vr_term_structure_2_5_10_63d},
    "rac_ext_012_vr_2_63d_vs_252d_ratio": {"inputs": ["close"], "func": rac_ext_012_vr_2_63d_vs_252d_ratio},
    "rac_ext_013_vr_5_63d_vs_252d_ratio": {"inputs": ["close"], "func": rac_ext_013_vr_5_63d_vs_252d_ratio},
    "rac_ext_014_vr_cross_scale_convexity_126d": {"inputs": ["close"], "func": rac_ext_014_vr_cross_scale_convexity_126d},
    "rac_ext_015_vr_2_weekly_agg_63d": {"inputs": ["close"], "func": rac_ext_015_vr_2_weekly_agg_63d},
    "rac_ext_016_vr_5_monthly_agg_252d": {"inputs": ["close"], "func": rac_ext_016_vr_5_monthly_agg_252d},
    "rac_ext_017_vr_2_high_low_63d": {"inputs": ["close", "high", "low"], "func": rac_ext_017_vr_2_high_low_63d},
    "rac_ext_018_vr_overlapping_5_126d": {"inputs": ["close"], "func": rac_ext_018_vr_overlapping_5_126d},
    "rac_ext_019_vr_5_vs_hurst_63d": {"inputs": ["close"], "func": rac_ext_019_vr_5_vs_hurst_63d},
    "rac_ext_020_vr_2_min_expanding": {"inputs": ["close"], "func": rac_ext_020_vr_2_min_expanding},
    "rac_ext_021_log_hl_ratio_ac_lag1_63d": {"inputs": ["close", "high", "low"], "func": rac_ext_021_log_hl_ratio_ac_lag1_63d},
    "rac_ext_022_log_hl_ratio_ac_lag1_126d": {"inputs": ["close", "high", "low"], "func": rac_ext_022_log_hl_ratio_ac_lag1_126d},
    "rac_ext_023_open_ret_ac_lag1_63d": {"inputs": ["close", "open"], "func": rac_ext_023_open_ret_ac_lag1_63d},
    "rac_ext_024_gap_ac_lag2_63d": {"inputs": ["close", "open"], "func": rac_ext_024_gap_ac_lag2_63d},
    "rac_ext_025_intraday_ret_ac_lag1_63d": {"inputs": ["close", "open"], "func": rac_ext_025_intraday_ret_ac_lag1_63d},
    "rac_ext_026_volume_ret_joint_ac_63d": {"inputs": ["close", "volume"], "func": rac_ext_026_volume_ret_joint_ac_63d},
    "rac_ext_027_volume_ret_cross_lag2_63d": {"inputs": ["close", "volume"], "func": rac_ext_027_volume_ret_cross_lag2_63d},
    "rac_ext_028_squared_ret_ac_lag5_63d": {"inputs": ["close"], "func": rac_ext_028_squared_ret_ac_lag5_63d},
    "rac_ext_029_abs_ret_ac_lag5_126d": {"inputs": ["close"], "func": rac_ext_029_abs_ret_ac_lag5_126d},
    "rac_ext_030_abs_ret_ac_lag21_252d": {"inputs": ["close"], "func": rac_ext_030_abs_ret_ac_lag21_252d},
    "rac_ext_031_ac_lag1_std_63d_252d": {"inputs": ["close"], "func": rac_ext_031_ac_lag1_std_63d_252d},
    "rac_ext_032_vr5_std_252d": {"inputs": ["close"], "func": rac_ext_032_vr5_std_252d},
    "rac_ext_033_hurst_std_252d": {"inputs": ["close"], "func": rac_ext_033_hurst_std_252d},
    "rac_ext_034_ac_lag1_regime_change_63d": {"inputs": ["close"], "func": rac_ext_034_ac_lag1_regime_change_63d},
    "rac_ext_035_vr5_regime_change_63d": {"inputs": ["close"], "func": rac_ext_035_vr5_regime_change_63d},
    "rac_ext_036_days_ac_lag1_extreme_neg_63d": {"inputs": ["close"], "func": rac_ext_036_days_ac_lag1_extreme_neg_63d},
    "rac_ext_037_days_hurst_below_04_252d": {"inputs": ["close"], "func": rac_ext_037_days_hurst_below_04_252d},
    "rac_ext_038_serial_struct_stability_252d": {"inputs": ["close"], "func": rac_ext_038_serial_struct_stability_252d},
    "rac_ext_039_hurst_pct_rank_252d_expanding": {"inputs": ["close"], "func": rac_ext_039_hurst_pct_rank_252d_expanding},
    "rac_ext_040_vr2_pct_rank_252d_expanding": {"inputs": ["close"], "func": rac_ext_040_vr2_pct_rank_252d_expanding},
    "rac_ext_041_anti_persist_regime_days_252d": {"inputs": ["close"], "func": rac_ext_041_anti_persist_regime_days_252d},
    "rac_ext_042_triple_agree_mean_rev_flag_63d": {"inputs": ["close"], "func": rac_ext_042_triple_agree_mean_rev_flag_63d},
    "rac_ext_043_triple_agree_persist_flag_63d": {"inputs": ["close"], "func": rac_ext_043_triple_agree_persist_flag_63d},
    "rac_ext_044_consec_days_triple_mean_rev_63d": {"inputs": ["close"], "func": rac_ext_044_consec_days_triple_mean_rev_63d},
    "rac_ext_045_lb_q4_63d_times_abs_ac_lag1": {"inputs": ["close"], "func": rac_ext_045_lb_q4_63d_times_abs_ac_lag1},
    "rac_ext_046_hurst_times_runs_ratio_63d": {"inputs": ["close"], "func": rac_ext_046_hurst_times_runs_ratio_63d},
    "rac_ext_047_ac_lag1_times_lb_q4_ratio_63d": {"inputs": ["close"], "func": rac_ext_047_ac_lag1_times_lb_q4_ratio_63d},
    "rac_ext_048_vr5_126d_times_hurst_126d": {"inputs": ["close"], "func": rac_ext_048_vr5_126d_times_hurst_126d},
    "rac_ext_049_mean_rev_intensity_63d": {"inputs": ["close"], "func": rac_ext_049_mean_rev_intensity_63d},
    "rac_ext_050_persist_intensity_63d": {"inputs": ["close"], "func": rac_ext_050_persist_intensity_63d},
    "rac_ext_051_ac_lag1_below_lag2_flag_63d": {"inputs": ["close"], "func": rac_ext_051_ac_lag1_below_lag2_flag_63d},
    "rac_ext_052_ac_sum_even_lags_63d": {"inputs": ["close"], "func": rac_ext_052_ac_sum_even_lags_63d},
    "rac_ext_053_ac_sum_odd_lags_63d": {"inputs": ["close"], "func": rac_ext_053_ac_sum_odd_lags_63d},
    "rac_ext_054_ac_lag_crossover_flag_63d": {"inputs": ["close"], "func": rac_ext_054_ac_lag_crossover_flag_63d},
    "rac_ext_055_hurst_acf_lag1_divergence_63d": {"inputs": ["close"], "func": rac_ext_055_hurst_acf_lag1_divergence_63d},
    "rac_ext_056_vr5_vs_ac_lag1_divergence_63d": {"inputs": ["close"], "func": rac_ext_056_vr5_vs_ac_lag1_divergence_63d},
    "rac_ext_057_ac_lag1_21d_pct_rank_252d": {"inputs": ["close"], "func": rac_ext_057_ac_lag1_21d_pct_rank_252d},
    "rac_ext_058_hurst_rs_21d": {"inputs": ["close"], "func": rac_ext_058_hurst_rs_21d},
    "rac_ext_059_hurst_rs_21d_zscore_252d": {"inputs": ["close"], "func": rac_ext_059_hurst_rs_21d_zscore_252d},
    "rac_ext_060_lb_q8_63d": {"inputs": ["close"], "func": rac_ext_060_lb_q8_63d},
    "rac_ext_061_lb_q4_63d_per_unit_var": {"inputs": ["close"], "func": rac_ext_061_lb_q4_63d_per_unit_var},
    "rac_ext_062_runs_ratio_21d_vs_63d": {"inputs": ["close"], "func": rac_ext_062_runs_ratio_21d_vs_63d},
    "rac_ext_063_abs_ret_lb_q4_63d": {"inputs": ["close"], "func": rac_ext_063_abs_ret_lb_q4_63d},
    "rac_ext_064_down_streak_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_064_down_streak_ac_lag1_63d},
    "rac_ext_065_down_depth_ac_lag1_63d": {"inputs": ["close"], "func": rac_ext_065_down_depth_ac_lag1_63d},
    "rac_ext_066_vr2_down_days_126d": {"inputs": ["close"], "func": rac_ext_066_vr2_down_days_126d},
    "rac_ext_067_hurst_down_days_63d": {"inputs": ["close"], "func": rac_ext_067_hurst_down_days_63d},
    "rac_ext_068_mean_rev_intensity_21d_zscore_252d": {"inputs": ["close"], "func": rac_ext_068_mean_rev_intensity_21d_zscore_252d},
    "rac_ext_069_capitulation_serial_score_63d": {"inputs": ["close"], "func": rac_ext_069_capitulation_serial_score_63d},
    "rac_ext_070_consec_mean_rev_triple_agree_252d": {"inputs": ["close"], "func": rac_ext_070_consec_mean_rev_triple_agree_252d},
    "rac_ext_071_ac_lag1_63d_new_low_252d_flag": {"inputs": ["close"], "func": rac_ext_071_ac_lag1_63d_new_low_252d_flag},
    "rac_ext_072_vr5_126d_new_low_252d_flag": {"inputs": ["close"], "func": rac_ext_072_vr5_126d_new_low_252d_flag},
    "rac_ext_073_serial_struct_diff_21d_vs_252d": {"inputs": ["close"], "func": rac_ext_073_serial_struct_diff_21d_vs_252d},
    "rac_ext_074_capitulation_serial_zscore_252d": {"inputs": ["close"], "func": rac_ext_074_capitulation_serial_zscore_252d},
    "rac_ext_075_mean_rev_score_expanding_pct_rank": {"inputs": ["close"], "func": rac_ext_075_mean_rev_score_expanding_pct_rank},
}
