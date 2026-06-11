"""
107_change_point_detection — Base Features 076-150
Domain: structural-break / regime-shift detection in return and price series —
        before/after contrasts, CUSUM on high/low/volume, rolling OLS-based break
        tests, percentile-rank of break statistics, Bayesian-style break probability
        proxies, multi-series break confluence, price-level regime detection.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
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


def _cusum_pos(s: pd.Series, w: int) -> pd.Series:
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        sv = 0.0
        for x in clean:
            sv = max(0.0, sv + (x - mu))
        return sv
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_fn, raw=True)


def _cusum_neg(s: pd.Series, w: int) -> pd.Series:
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        sv = 0.0
        for x in clean:
            sv = min(0.0, sv + (x - mu))
        return sv
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_fn, raw=True)


def _mean_shift_stat(s: pd.Series, half: int) -> pd.Series:
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _var_shift_stat(s: pd.Series, half: int) -> pd.Series:
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        var_b = clean[:mid].var()
        var_a = clean[mid:].var()
        if var_b < _EPS:
            return 0.0
        return np.log((var_a + _EPS) / (var_b + _EPS))
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _linslope(s: pd.Series, w: int) -> pd.Series:
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


def _before_after_contrast(s: pd.Series, half: int) -> pd.Series:
    """Ratio of after-mean to before-mean (before=prior half bars, after=trailing half)."""
    w = 2 * half
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        mu_b = clean[:mid].mean()
        mu_a = clean[mid:].mean()
        if abs(mu_b) < _EPS:
            return np.nan
        return mu_a / mu_b
    return s.rolling(w, min_periods=max(4, half)).apply(_fn, raw=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Before/after contrasts on returns and price ---

def cpd_076_before_after_return_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-21d mean return to prior-21d mean return (after/before)."""
    return _before_after_contrast(_log_returns(close), _TD_MON)


def cpd_077_before_after_return_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-63d mean return to prior-63d mean return."""
    return _before_after_contrast(_log_returns(close), _TD_QTR)


def cpd_078_before_after_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-21d return std to prior-21d return std (vol regime shift)."""
    w = 2 * _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 4:
            return np.nan
        n = len(clean)
        mid = n // 2
        std_b = clean[:mid].std()
        std_a = clean[mid:].std()
        if std_b < _EPS:
            return np.nan
        return std_a / (std_b + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_MON)).apply(_fn, raw=True)


def cpd_079_before_after_vol_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-63d return std to prior-63d return std."""
    w = 2 * _TD_QTR
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 4:
            return np.nan
        n = len(clean)
        mid = n // 2
        std_b = clean[:mid].std()
        std_a = clean[mid:].std()
        if std_b < _EPS:
            return np.nan
        return std_a / (std_b + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_QTR)).apply(_fn, raw=True)


def cpd_080_before_after_price_level_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-21d mean price to prior-21d mean price."""
    return _before_after_contrast(close, _TD_MON)


def cpd_081_before_after_price_level_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of trailing-63d mean price to prior-63d mean price."""
    return _before_after_contrast(close, _TD_QTR)


def cpd_082_before_after_return_diff_21d(close: pd.Series) -> pd.Series:
    """Difference in mean return: trailing-21d minus prior-21d."""
    r = _log_returns(close)
    after  = _rolling_mean(r, _TD_MON)
    before = _rolling_mean(r, _TD_MON).shift(_TD_MON)
    return after - before


def cpd_083_before_after_return_diff_63d(close: pd.Series) -> pd.Series:
    """Difference in mean return: trailing-63d minus prior-63d."""
    r = _log_returns(close)
    after  = _rolling_mean(r, _TD_QTR)
    before = _rolling_mean(r, _TD_QTR).shift(_TD_QTR)
    return after - before


def cpd_084_before_after_vol_diff_21d(close: pd.Series) -> pd.Series:
    """Difference in return volatility: trailing-21d std minus prior-21d std."""
    r = _log_returns(close)
    std_a = _rolling_std(r, _TD_MON)
    std_b = _rolling_std(r, _TD_MON).shift(_TD_MON)
    return std_a - std_b


def cpd_085_before_after_vol_diff_63d(close: pd.Series) -> pd.Series:
    """Difference in return volatility: trailing-63d std minus prior-63d std."""
    r = _log_returns(close)
    std_a = _rolling_std(r, _TD_QTR)
    std_b = _rolling_std(r, _TD_QTR).shift(_TD_QTR)
    return std_a - std_b


# --- Group I (086-095): CUSUM on high/low/volume series ---

def cpd_086_cusum_pos_high_21d(high: pd.Series) -> pd.Series:
    """Upper CUSUM on log-returns of daily high over 21-day window."""
    r = np.log(high / high.shift(1))
    return _cusum_pos(r, _TD_MON)


def cpd_087_cusum_neg_low_21d(low: pd.Series) -> pd.Series:
    """Lower CUSUM on log-returns of daily low over 21-day window."""
    r = np.log(low / low.shift(1))
    return _cusum_neg(r, _TD_MON)


def cpd_088_cusum_neg_low_63d(low: pd.Series) -> pd.Series:
    """Lower CUSUM on log-returns of daily low over 63-day window."""
    r = np.log(low / low.shift(1))
    return _cusum_neg(r, _TD_QTR)


def cpd_089_cusum_pos_vol_21d(volume: pd.Series) -> pd.Series:
    """Upper CUSUM on log-volume changes over 21-day window."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _cusum_pos(r, _TD_MON)


def cpd_090_cusum_neg_vol_21d(volume: pd.Series) -> pd.Series:
    """Lower CUSUM on log-volume changes over 21-day window."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _cusum_neg(r, _TD_MON)


def cpd_091_mean_shift_stat_high_21d(high: pd.Series) -> pd.Series:
    """Mean-shift stat on high log-returns, half=21."""
    return _mean_shift_stat(np.log(high / high.shift(1)), _TD_MON)


def cpd_092_mean_shift_stat_low_21d(low: pd.Series) -> pd.Series:
    """Mean-shift stat on low log-returns, half=21."""
    return _mean_shift_stat(np.log(low / low.shift(1)), _TD_MON)


def cpd_093_mean_shift_stat_vol_21d(volume: pd.Series) -> pd.Series:
    """Mean-shift stat on log-volume changes, half=21."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _mean_shift_stat(r, _TD_MON)


def cpd_094_var_shift_stat_high_21d(high: pd.Series) -> pd.Series:
    """Variance-shift stat on high log-returns, half=21."""
    return _var_shift_stat(np.log(high / high.shift(1)), _TD_MON)


def cpd_095_var_shift_stat_low_21d(low: pd.Series) -> pd.Series:
    """Variance-shift stat on low log-returns, half=21."""
    return _var_shift_stat(np.log(low / low.shift(1)), _TD_MON)


# --- Group J (096-105): OLS-based structural-break tests ---

def cpd_096_ols_slope_change_21d(close: pd.Series) -> pd.Series:
    """Change in OLS slope: trailing-21d slope minus prior-21d slope of log-price."""
    lp = np.log(close.clip(lower=_EPS))
    slope_now  = _linslope(lp, _TD_MON)
    slope_prev = _linslope(lp, _TD_MON).shift(_TD_MON)
    return slope_now - slope_prev


def cpd_097_ols_slope_change_63d(close: pd.Series) -> pd.Series:
    """Change in OLS slope: trailing-63d slope minus prior-63d slope of log-price."""
    lp = np.log(close.clip(lower=_EPS))
    slope_now  = _linslope(lp, _TD_QTR)
    slope_prev = _linslope(lp, _TD_QTR).shift(_TD_QTR)
    return slope_now - slope_prev


def cpd_098_ols_intercept_shift_21d(close: pd.Series) -> pd.Series:
    """
    Chow-like intercept shift: difference between current price and predicted
    value from the prior-21d OLS fit extrapolated 21 days forward.
    """
    lp = np.log(close.clip(lower=_EPS))
    def _pred_diff(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_MON):
            return np.nan
        n = len(clean)
        mid = n // 2
        xi_b = np.arange(mid, dtype=float)
        xi_b_m = xi_b.mean()
        y_b = clean[:mid]
        y_b_m = y_b.mean()
        den = ((xi_b - xi_b_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = ((xi_b - xi_b_m) * (y_b - y_b_m)).sum() / den
        intercept = y_b_m - slope * xi_b_m
        predicted = intercept + slope * (n - 1)
        return clean[-1] - predicted
    w = 2 * _TD_MON
    return lp.rolling(w, min_periods=max(4, _TD_MON)).apply(_pred_diff, raw=True)


def cpd_099_ols_intercept_shift_63d(close: pd.Series) -> pd.Series:
    """Chow-like intercept shift using 63-day split window."""
    lp = np.log(close.clip(lower=_EPS))
    def _pred_diff(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_QTR):
            return np.nan
        n = len(clean)
        mid = n // 2
        xi_b = np.arange(mid, dtype=float)
        xi_b_m = xi_b.mean()
        y_b = clean[:mid]
        y_b_m = y_b.mean()
        den = ((xi_b - xi_b_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = ((xi_b - xi_b_m) * (y_b - y_b_m)).sum() / den
        intercept = y_b_m - slope * xi_b_m
        predicted = intercept + slope * (n - 1)
        return clean[-1] - predicted
    w = 2 * _TD_QTR
    return lp.rolling(w, min_periods=max(4, _TD_QTR)).apply(_pred_diff, raw=True)


def cpd_100_residual_variance_ratio_21d(close: pd.Series) -> pd.Series:
    """
    Ratio of residual variance in 2nd half to 1st half of OLS fit on log-price.
    Increase signals structural instability.
    """
    lp = np.log(close.clip(lower=_EPS))
    w = 2 * _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_MON):
            return np.nan
        n = len(clean)
        mid = n // 2
        def _resid_var(y):
            if len(y) < 2:
                return np.nan
            xi = np.arange(len(y), dtype=float)
            xi_m = xi.mean()
            y_m = y.mean()
            den = ((xi - xi_m) ** 2).sum()
            if den == 0:
                return y.var()
            slope = ((xi - xi_m) * (y - y_m)).sum() / den
            intercept = y_m - slope * xi_m
            resid = y - (intercept + slope * xi)
            return resid.var()
        rv_b = _resid_var(clean[:mid])
        rv_a = _resid_var(clean[mid:])
        if rv_b is None or rv_b < _EPS:
            return np.nan
        return (rv_a + _EPS) / (rv_b + _EPS)
    return lp.rolling(w, min_periods=max(4, _TD_MON)).apply(_fn, raw=True)


def cpd_101_ols_slope_break_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: OLS slope change (21d) in absolute value exceeds 1 std of slope changes."""
    sc = cpd_096_ols_slope_change_21d(close)
    thr = _rolling_std(sc, _TD_YEAR)
    return (sc.abs() > thr.clip(lower=_EPS)).astype(float)


def cpd_102_ols_slope_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of OLS slope change (21d) vs trailing 252-day distribution."""
    sc = cpd_096_ols_slope_change_21d(close)
    return _safe_div(sc - _rolling_mean(sc, _TD_YEAR), _rolling_std(sc, _TD_YEAR))


def cpd_103_ols_slope_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of OLS slope change (63d) vs trailing 252-day distribution."""
    sc = cpd_097_ols_slope_change_63d(close)
    return _safe_div(sc - _rolling_mean(sc, _TD_YEAR), _rolling_std(sc, _TD_YEAR))


def cpd_104_cusum_on_ols_residuals_21d(close: pd.Series) -> pd.Series:
    """
    Upper CUSUM applied to OLS residuals of log-price vs time, 21-day window.
    Captures mean drift in residuals indicating break in price trend.
    """
    lp = np.log(close.clip(lower=_EPS))
    def _resids(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        xi = np.arange(len(clean), dtype=float)
        xi_m = xi.mean()
        y_m = clean.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return 0.0
        slope = ((xi - xi_m) * (clean - y_m)).sum() / den
        intercept = y_m - slope * xi_m
        resid = clean - (intercept + slope * xi)
        mu = resid.mean()
        sv = 0.0
        for r in resid:
            sv = max(0.0, sv + (r - mu))
        return sv
    return lp.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_resids, raw=True)


def cpd_105_cusum_on_ols_residuals_63d(close: pd.Series) -> pd.Series:
    """Upper CUSUM on OLS residuals of log-price, 63-day window."""
    lp = np.log(close.clip(lower=_EPS))
    def _resids(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        xi = np.arange(len(clean), dtype=float)
        xi_m = xi.mean()
        y_m = clean.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return 0.0
        slope = ((xi - xi_m) * (clean - y_m)).sum() / den
        intercept = y_m - slope * xi_m
        resid = clean - (intercept + slope * xi)
        mu = resid.mean()
        sv = 0.0
        for r in resid:
            sv = max(0.0, sv + (r - mu))
        return sv
    return lp.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_resids, raw=True)


# --- Group K (106-115): Percentile rank and z-score of break statistics ---

def cpd_106_mean_shift_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of mean-shift stat (half=21) in trailing 252-day distribution."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    return ms.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_107_mean_shift_pct_rank_63d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of mean-shift stat (half=63) in trailing 252-day distribution."""
    ms = _mean_shift_stat(_log_returns(close), _TD_QTR)
    return ms.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_108_var_shift_abs_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of |var-shift stat| (half=21) in trailing 252-day distribution."""
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    return vs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_109_cusum_neg_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of |lower CUSUM| (21d) in trailing 252-day distribution."""
    cs = _cusum_neg(_log_returns(close), _TD_MON).abs()
    return cs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_110_cusum_neg_zscore_21d_252d(close: pd.Series) -> pd.Series:
    """Z-score of |lower CUSUM| (21d) vs trailing 252-day distribution."""
    cs = _cusum_neg(_log_returns(close), _TD_MON).abs()
    return _safe_div(cs - _rolling_mean(cs, _TD_YEAR), _rolling_std(cs, _TD_YEAR))


def cpd_111_mean_shift_zscore_21d_252d(close: pd.Series) -> pd.Series:
    """Z-score of mean-shift stat (half=21) vs trailing 252-day distribution."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    return _safe_div(ms - _rolling_mean(ms, _TD_YEAR), _rolling_std(ms, _TD_YEAR))


def cpd_112_mean_shift_expanding_pct_rank_21d(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of mean-shift stat (half=21)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    return ms.expanding(min_periods=_TD_QTR).rank(pct=True)


def cpd_113_cusum_neg_expanding_pct_rank_21d(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of |lower CUSUM| (21d)."""
    cs = _cusum_neg(_log_returns(close), _TD_MON).abs()
    return cs.expanding(min_periods=_TD_QTR).rank(pct=True)


def cpd_114_combined_shift_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of combined shift stat (half=21) in trailing 252d."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    combined = ms + vs
    return combined.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_115_cusum_pos_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of upper CUSUM (21d) in trailing 252-day distribution."""
    cs = _cusum_pos(_log_returns(close), _TD_MON)
    return cs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group L (116-125): Multi-series break confluence ---

def cpd_116_break_confluence_close_high_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of series (close, high) simultaneously showing mean-shift break (half=21, thr=1)."""
    f_c = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    f_h = (_mean_shift_stat(np.log(high / high.shift(1)), _TD_MON) > 1.0).astype(float)
    return f_c + f_h


def cpd_117_break_confluence_close_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of series (close, low) simultaneously showing mean-shift break."""
    f_c = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    f_l = (_mean_shift_stat(np.log(low / low.shift(1)), _TD_MON) > 1.0).astype(float)
    return f_c + f_l


def cpd_118_break_confluence_close_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of series (close-returns, log-volume change) showing mean-shift break."""
    f_c = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    r_v = np.log((volume + 1) / (volume.shift(1) + 1))
    f_v = (_mean_shift_stat(r_v, _TD_MON) > 1.0).astype(float)
    return f_c + f_v


def cpd_119_break_confluence_all4_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of series (close, high, low, volume) showing mean-shift break (half=21, thr=1)."""
    f_c = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    f_h = (_mean_shift_stat(np.log(high / high.shift(1)), _TD_MON) > 1.0).astype(float)
    f_l = (_mean_shift_stat(np.log(low / low.shift(1)), _TD_MON) > 1.0).astype(float)
    r_v = np.log((volume + 1) / (volume.shift(1) + 1))
    f_v = (_mean_shift_stat(r_v, _TD_MON) > 1.0).astype(float)
    return f_c + f_h + f_l + f_v


def cpd_120_cusum_confluence_close_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """
    Both close-CUSUM and low-CUSUM negative break detected simultaneously (21d).
    """
    r_c = _log_returns(close)
    cs_c = _cusum_neg(r_c, _TD_MON).abs()
    thr_c = _rolling_std(r_c, _TD_MON) * 2.0
    f_c = (cs_c > thr_c.clip(lower=_EPS)).astype(float)
    r_l = np.log(low / low.shift(1))
    cs_l = _cusum_neg(r_l, _TD_MON).abs()
    thr_l = _rolling_std(r_l, _TD_MON) * 2.0
    f_l = (cs_l > thr_l.clip(lower=_EPS)).astype(float)
    return f_c + f_l


def cpd_121_mean_shift_stat_hl_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of mean-shift stats for high and low log-returns, half=21."""
    ms_h = _mean_shift_stat(np.log(high / high.shift(1)), _TD_MON)
    ms_l = _mean_shift_stat(np.log(low / low.shift(1)), _TD_MON)
    return (ms_h + ms_l) / 2.0


def cpd_122_cusum_hl_spread_break_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean-shift stat on log(high/low) spread, half=21 (range-regime break)."""
    spread = np.log((high + _EPS) / (low + _EPS))
    return _mean_shift_stat(spread, _TD_MON)


def cpd_123_cusum_hl_spread_break_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean-shift stat on log(high/low) spread, half=63."""
    spread = np.log((high + _EPS) / (low + _EPS))
    return _mean_shift_stat(spread, _TD_QTR)


def cpd_124_vol_regime_shift_close_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Combined score: mean-shift on close returns + mean-shift on log-volume changes.
    Half=21. Proxy for concurrent price and liquidity regime shift.
    """
    ms_c = _mean_shift_stat(_log_returns(close), _TD_MON)
    r_v = np.log((volume + 1) / (volume.shift(1) + 1))
    ms_v = _mean_shift_stat(r_v, _TD_MON)
    return ms_c + ms_v


def cpd_125_var_shift_hl_spread_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance-shift stat on log(high/low) spread, half=21."""
    spread = np.log((high + _EPS) / (low + _EPS))
    return _var_shift_stat(spread, _TD_MON)


# --- Group M (126-135): Price-level structural-break proxies ---

def cpd_126_price_level_cusum_neg_252d(close: pd.Series) -> pd.Series:
    """Lower CUSUM on log-price over 252-day window (persistent price decline detector)."""
    return _cusum_neg(np.log(close.clip(lower=_EPS)), _TD_YEAR)


def cpd_127_price_level_cusum_neg_126d(close: pd.Series) -> pd.Series:
    """Lower CUSUM on log-price over 126-day window."""
    return _cusum_neg(np.log(close.clip(lower=_EPS)), _TD_HALF)


def cpd_128_price_below_ols_trend_21d(close: pd.Series) -> pd.Series:
    """
    How far current log-price is below the OLS trend fitted on prior 21 days,
    normalized by residual std. Negative = below trend (downward break signal).
    """
    lp = np.log(close.clip(lower=_EPS))
    return cpd_098_ols_intercept_shift_21d(close)


def cpd_129_price_below_ols_trend_63d(close: pd.Series) -> pd.Series:
    """How far current log-price is below the OLS trend fitted on prior 63 days."""
    return cpd_099_ols_intercept_shift_63d(close)


def cpd_130_price_vs_rolling_mean_break_21d(close: pd.Series) -> pd.Series:
    """
    Z-score of (close - rolling_mean_21d) / rolling_std_21d.
    Sharp drop below rolling mean signals mean break.
    """
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    return _safe_div(close - m, s)


def cpd_131_price_vs_rolling_mean_break_63d(close: pd.Series) -> pd.Series:
    """Z-score of (close - rolling_mean_63d) / rolling_std_63d."""
    m = _rolling_mean(close, _TD_QTR)
    s = _rolling_std(close, _TD_QTR)
    return _safe_div(close - m, s)


def cpd_132_price_rolling_min_break_21d(close: pd.Series) -> pd.Series:
    """How far close is below its rolling 21-day minimum (measures negative breakout)."""
    mn = _rolling_min(close, _TD_MON)
    return _safe_div(close - mn, mn.clip(lower=_EPS))


def cpd_133_price_rolling_min_break_252d(close: pd.Series) -> pd.Series:
    """How far close is below its rolling 252-day minimum."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - mn, mn.clip(lower=_EPS))


def cpd_134_price_regime_down_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: z-score of (close - mean_21d) / std_21d < -2.0 (price breaks below range)."""
    z = cpd_130_price_vs_rolling_mean_break_21d(close)
    return (z < -2.0).astype(float)


def cpd_135_price_regime_down_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: z-score of (close - mean_63d) / std_63d < -2.0."""
    z = cpd_131_price_vs_rolling_mean_break_63d(close)
    return (z < -2.0).astype(float)


# --- Group N (136-150): Additional break metrics and derived break scores ---

def cpd_136_break_rate_21d_ewm_decay(close: pd.Series) -> pd.Series:
    """EWM(span=21) of mean-shift break flag (half=21, thr=1) — recency-weighted break rate."""
    flag = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    return flag.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def cpd_137_break_rate_63d_ewm_decay(close: pd.Series) -> pd.Series:
    """EWM(span=63) of mean-shift break flag (half=21, thr=1)."""
    flag = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    return flag.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def cpd_138_cusum_normalized_21d(close: pd.Series) -> pd.Series:
    """Lower CUSUM (21d) normalized by rolling std of returns (scale-invariant)."""
    r = _log_returns(close)
    cs = _cusum_neg(r, _TD_MON).abs()
    s  = _rolling_std(r, _TD_MON)
    return _safe_div(cs, s.clip(lower=_EPS))


def cpd_139_cusum_normalized_63d(close: pd.Series) -> pd.Series:
    """Lower CUSUM (63d) normalized by rolling std of returns."""
    r = _log_returns(close)
    cs = _cusum_neg(r, _TD_QTR).abs()
    s  = _rolling_std(r, _TD_QTR)
    return _safe_div(cs, s.clip(lower=_EPS))


def cpd_140_break_score_composite_21d(close: pd.Series) -> pd.Series:
    """
    Composite break score: mean-shift stat + |var-shift stat| + normalized CUSUM,
    all half/window=21. High value = strong multi-method evidence of structural break.
    """
    r  = _log_returns(close)
    ms = _mean_shift_stat(r, _TD_MON)
    vs = _var_shift_stat(r, _TD_MON).abs()
    cs = _cusum_neg(r, _TD_MON).abs()
    std = _rolling_std(r, _TD_MON)
    cs_norm = _safe_div(cs, std.clip(lower=_EPS))
    return ms + vs + cs_norm.fillna(0.0)


def cpd_141_downward_break_intensity_21d(close: pd.Series) -> pd.Series:
    """Downward break intensity: negative signed mean-shift magnitude clipped to 0+."""
    signed = cpd_017_mean_shift_signed_21d(close)
    return (-signed).clip(lower=0.0)


def cpd_142_downward_break_intensity_63d(close: pd.Series) -> pd.Series:
    """Downward break intensity (half=63): negative signed mean-shift."""
    return (-cpd_018_mean_shift_signed_63d(close)).clip(lower=0.0)


def cpd_017_mean_shift_signed_21d_local(close: pd.Series) -> pd.Series:
    """Local copy of signed mean-shift (half=21) for use within this file."""
    w = 2 * _TD_MON
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_MON):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return (clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_MON)).apply(_stat, raw=True)


def cpd_018_mean_shift_signed_63d_local(close: pd.Series) -> pd.Series:
    """Local copy of signed mean-shift (half=63) for use within this file."""
    w = 2 * _TD_QTR
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_QTR):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return (clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_QTR)).apply(_stat, raw=True)


def cpd_141_downward_break_intensity_21d(close: pd.Series) -> pd.Series:  # noqa: F811
    """Downward break intensity: negative signed mean-shift magnitude clipped to 0+."""
    signed = cpd_017_mean_shift_signed_21d_local(close)
    return (-signed).clip(lower=0.0)


def cpd_142_downward_break_intensity_63d(close: pd.Series) -> pd.Series:  # noqa: F811
    """Downward break intensity (half=63): negative signed mean-shift."""
    return (-cpd_018_mean_shift_signed_63d_local(close)).clip(lower=0.0)


def cpd_143_var_increase_intensity_21d(close: pd.Series) -> pd.Series:
    """Positive variance shift (volatility explosion) magnitude, half=21."""
    return _var_shift_stat(_log_returns(close), _TD_MON).clip(lower=0.0)


def cpd_144_break_persistence_21d(close: pd.Series) -> pd.Series:
    """
    EWM of absolute mean-shift stat (half=21, span=10): how persistent recent
    break signals are.
    """
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    return ms.abs().ewm(span=10, min_periods=5).mean()


def cpd_145_break_persistence_63d(close: pd.Series) -> pd.Series:
    """EWM(span=21) of absolute mean-shift stat (half=63): longer break persistence."""
    ms = _mean_shift_stat(_log_returns(close), _TD_QTR)
    return ms.abs().ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def cpd_146_cusum_acceleration_21d(close: pd.Series) -> pd.Series:
    """5-day change in |lower CUSUM| (21d) — is the CUSUM statistic worsening."""
    cs = _cusum_neg(_log_returns(close), _TD_MON).abs()
    return cs.diff(_TD_WEEK)


def cpd_147_mean_shift_acceleration_21d(close: pd.Series) -> pd.Series:
    """5-day change in mean-shift stat (half=21) — is the break signal strengthening."""
    return _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_WEEK)


def cpd_148_var_shift_acceleration_21d(close: pd.Series) -> pd.Series:
    """5-day change in |var-shift stat| (half=21)."""
    return _var_shift_stat(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)


def cpd_149_break_score_composite_63d(close: pd.Series) -> pd.Series:
    """
    Composite break score (half/window=63): mean-shift + |var-shift| + normalized CUSUM.
    """
    r  = _log_returns(close)
    ms = _mean_shift_stat(r, _TD_QTR)
    vs = _var_shift_stat(r, _TD_QTR).abs()
    cs = _cusum_neg(r, _TD_QTR).abs()
    std = _rolling_std(r, _TD_QTR)
    cs_norm = _safe_div(cs, std.clip(lower=_EPS))
    return ms + vs + cs_norm.fillna(0.0)


def cpd_150_break_score_ewm_composite_21d(close: pd.Series) -> pd.Series:
    """EWM(span=21) of the composite break score (half=21) — smoothed break regime."""
    score = cpd_140_break_score_composite_21d(close)
    return score.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


# ── Registry ──────────────────────────────────────────────────────────────────

CHANGE_POINT_DETECTION_REGISTRY_076_150 = {
    "cpd_076_before_after_return_ratio_21d": {"inputs": ["close"], "func": cpd_076_before_after_return_ratio_21d},
    "cpd_077_before_after_return_ratio_63d": {"inputs": ["close"], "func": cpd_077_before_after_return_ratio_63d},
    "cpd_078_before_after_vol_ratio_21d": {"inputs": ["close"], "func": cpd_078_before_after_vol_ratio_21d},
    "cpd_079_before_after_vol_ratio_63d": {"inputs": ["close"], "func": cpd_079_before_after_vol_ratio_63d},
    "cpd_080_before_after_price_level_ratio_21d": {"inputs": ["close"], "func": cpd_080_before_after_price_level_ratio_21d},
    "cpd_081_before_after_price_level_ratio_63d": {"inputs": ["close"], "func": cpd_081_before_after_price_level_ratio_63d},
    "cpd_082_before_after_return_diff_21d": {"inputs": ["close"], "func": cpd_082_before_after_return_diff_21d},
    "cpd_083_before_after_return_diff_63d": {"inputs": ["close"], "func": cpd_083_before_after_return_diff_63d},
    "cpd_084_before_after_vol_diff_21d": {"inputs": ["close"], "func": cpd_084_before_after_vol_diff_21d},
    "cpd_085_before_after_vol_diff_63d": {"inputs": ["close"], "func": cpd_085_before_after_vol_diff_63d},
    "cpd_086_cusum_pos_high_21d": {"inputs": ["high"], "func": cpd_086_cusum_pos_high_21d},
    "cpd_087_cusum_neg_low_21d": {"inputs": ["low"], "func": cpd_087_cusum_neg_low_21d},
    "cpd_088_cusum_neg_low_63d": {"inputs": ["low"], "func": cpd_088_cusum_neg_low_63d},
    "cpd_089_cusum_pos_vol_21d": {"inputs": ["volume"], "func": cpd_089_cusum_pos_vol_21d},
    "cpd_090_cusum_neg_vol_21d": {"inputs": ["volume"], "func": cpd_090_cusum_neg_vol_21d},
    "cpd_091_mean_shift_stat_high_21d": {"inputs": ["high"], "func": cpd_091_mean_shift_stat_high_21d},
    "cpd_092_mean_shift_stat_low_21d": {"inputs": ["low"], "func": cpd_092_mean_shift_stat_low_21d},
    "cpd_093_mean_shift_stat_vol_21d": {"inputs": ["volume"], "func": cpd_093_mean_shift_stat_vol_21d},
    "cpd_094_var_shift_stat_high_21d": {"inputs": ["high"], "func": cpd_094_var_shift_stat_high_21d},
    "cpd_095_var_shift_stat_low_21d": {"inputs": ["low"], "func": cpd_095_var_shift_stat_low_21d},
    "cpd_096_ols_slope_change_21d": {"inputs": ["close"], "func": cpd_096_ols_slope_change_21d},
    "cpd_097_ols_slope_change_63d": {"inputs": ["close"], "func": cpd_097_ols_slope_change_63d},
    "cpd_098_ols_intercept_shift_21d": {"inputs": ["close"], "func": cpd_098_ols_intercept_shift_21d},
    "cpd_099_ols_intercept_shift_63d": {"inputs": ["close"], "func": cpd_099_ols_intercept_shift_63d},
    "cpd_100_residual_variance_ratio_21d": {"inputs": ["close"], "func": cpd_100_residual_variance_ratio_21d},
    "cpd_101_ols_slope_break_flag_21d": {"inputs": ["close"], "func": cpd_101_ols_slope_break_flag_21d},
    "cpd_102_ols_slope_zscore_21d": {"inputs": ["close"], "func": cpd_102_ols_slope_zscore_21d},
    "cpd_103_ols_slope_zscore_63d": {"inputs": ["close"], "func": cpd_103_ols_slope_zscore_63d},
    "cpd_104_cusum_on_ols_residuals_21d": {"inputs": ["close"], "func": cpd_104_cusum_on_ols_residuals_21d},
    "cpd_105_cusum_on_ols_residuals_63d": {"inputs": ["close"], "func": cpd_105_cusum_on_ols_residuals_63d},
    "cpd_106_mean_shift_pct_rank_21d_252d": {"inputs": ["close"], "func": cpd_106_mean_shift_pct_rank_21d_252d},
    "cpd_107_mean_shift_pct_rank_63d_252d": {"inputs": ["close"], "func": cpd_107_mean_shift_pct_rank_63d_252d},
    "cpd_108_var_shift_abs_pct_rank_21d_252d": {"inputs": ["close"], "func": cpd_108_var_shift_abs_pct_rank_21d_252d},
    "cpd_109_cusum_neg_pct_rank_21d_252d": {"inputs": ["close"], "func": cpd_109_cusum_neg_pct_rank_21d_252d},
    "cpd_110_cusum_neg_zscore_21d_252d": {"inputs": ["close"], "func": cpd_110_cusum_neg_zscore_21d_252d},
    "cpd_111_mean_shift_zscore_21d_252d": {"inputs": ["close"], "func": cpd_111_mean_shift_zscore_21d_252d},
    "cpd_112_mean_shift_expanding_pct_rank_21d": {"inputs": ["close"], "func": cpd_112_mean_shift_expanding_pct_rank_21d},
    "cpd_113_cusum_neg_expanding_pct_rank_21d": {"inputs": ["close"], "func": cpd_113_cusum_neg_expanding_pct_rank_21d},
    "cpd_114_combined_shift_pct_rank_21d_252d": {"inputs": ["close"], "func": cpd_114_combined_shift_pct_rank_21d_252d},
    "cpd_115_cusum_pos_pct_rank_21d_252d": {"inputs": ["close"], "func": cpd_115_cusum_pos_pct_rank_21d_252d},
    "cpd_116_break_confluence_close_high_21d": {"inputs": ["close", "high"], "func": cpd_116_break_confluence_close_high_21d},
    "cpd_117_break_confluence_close_low_21d": {"inputs": ["close", "low"], "func": cpd_117_break_confluence_close_low_21d},
    "cpd_118_break_confluence_close_vol_21d": {"inputs": ["close", "volume"], "func": cpd_118_break_confluence_close_vol_21d},
    "cpd_119_break_confluence_all4_21d": {"inputs": ["close", "high", "low", "volume"], "func": cpd_119_break_confluence_all4_21d},
    "cpd_120_cusum_confluence_close_low_21d": {"inputs": ["close", "low"], "func": cpd_120_cusum_confluence_close_low_21d},
    "cpd_121_mean_shift_stat_hl_avg_21d": {"inputs": ["close", "high", "low"], "func": cpd_121_mean_shift_stat_hl_avg_21d},
    "cpd_122_cusum_hl_spread_break_21d": {"inputs": ["close", "high", "low"], "func": cpd_122_cusum_hl_spread_break_21d},
    "cpd_123_cusum_hl_spread_break_63d": {"inputs": ["close", "high", "low"], "func": cpd_123_cusum_hl_spread_break_63d},
    "cpd_124_vol_regime_shift_close_vol_21d": {"inputs": ["close", "volume"], "func": cpd_124_vol_regime_shift_close_vol_21d},
    "cpd_125_var_shift_hl_spread_21d": {"inputs": ["close", "high", "low"], "func": cpd_125_var_shift_hl_spread_21d},
    "cpd_126_price_level_cusum_neg_252d": {"inputs": ["close"], "func": cpd_126_price_level_cusum_neg_252d},
    "cpd_127_price_level_cusum_neg_126d": {"inputs": ["close"], "func": cpd_127_price_level_cusum_neg_126d},
    "cpd_128_price_below_ols_trend_21d": {"inputs": ["close"], "func": cpd_128_price_below_ols_trend_21d},
    "cpd_129_price_below_ols_trend_63d": {"inputs": ["close"], "func": cpd_129_price_below_ols_trend_63d},
    "cpd_130_price_vs_rolling_mean_break_21d": {"inputs": ["close"], "func": cpd_130_price_vs_rolling_mean_break_21d},
    "cpd_131_price_vs_rolling_mean_break_63d": {"inputs": ["close"], "func": cpd_131_price_vs_rolling_mean_break_63d},
    "cpd_132_price_rolling_min_break_21d": {"inputs": ["close"], "func": cpd_132_price_rolling_min_break_21d},
    "cpd_133_price_rolling_min_break_252d": {"inputs": ["close"], "func": cpd_133_price_rolling_min_break_252d},
    "cpd_134_price_regime_down_flag_21d": {"inputs": ["close"], "func": cpd_134_price_regime_down_flag_21d},
    "cpd_135_price_regime_down_flag_63d": {"inputs": ["close"], "func": cpd_135_price_regime_down_flag_63d},
    "cpd_136_break_rate_21d_ewm_decay": {"inputs": ["close"], "func": cpd_136_break_rate_21d_ewm_decay},
    "cpd_137_break_rate_63d_ewm_decay": {"inputs": ["close"], "func": cpd_137_break_rate_63d_ewm_decay},
    "cpd_138_cusum_normalized_21d": {"inputs": ["close"], "func": cpd_138_cusum_normalized_21d},
    "cpd_139_cusum_normalized_63d": {"inputs": ["close"], "func": cpd_139_cusum_normalized_63d},
    "cpd_140_break_score_composite_21d": {"inputs": ["close"], "func": cpd_140_break_score_composite_21d},
    "cpd_141_downward_break_intensity_21d": {"inputs": ["close"], "func": cpd_141_downward_break_intensity_21d},
    "cpd_142_downward_break_intensity_63d": {"inputs": ["close"], "func": cpd_142_downward_break_intensity_63d},
    "cpd_143_var_increase_intensity_21d": {"inputs": ["close"], "func": cpd_143_var_increase_intensity_21d},
    "cpd_144_break_persistence_21d": {"inputs": ["close"], "func": cpd_144_break_persistence_21d},
    "cpd_145_break_persistence_63d": {"inputs": ["close"], "func": cpd_145_break_persistence_63d},
    "cpd_146_cusum_acceleration_21d": {"inputs": ["close"], "func": cpd_146_cusum_acceleration_21d},
    "cpd_147_mean_shift_acceleration_21d": {"inputs": ["close"], "func": cpd_147_mean_shift_acceleration_21d},
    "cpd_148_var_shift_acceleration_21d": {"inputs": ["close"], "func": cpd_148_var_shift_acceleration_21d},
    "cpd_149_break_score_composite_63d": {"inputs": ["close"], "func": cpd_149_break_score_composite_63d},
    "cpd_150_break_score_ewm_composite_21d": {"inputs": ["close"], "func": cpd_150_break_score_ewm_composite_21d},
}
