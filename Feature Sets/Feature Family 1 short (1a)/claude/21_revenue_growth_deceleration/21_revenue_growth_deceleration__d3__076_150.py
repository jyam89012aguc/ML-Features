"""revenue_growth_deceleration d3 features 076-150 - order-3 difference (jerk) of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF.
"""
"""revenue_growth_deceleration base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Second half of the 150-feature deceleration hypothesis set. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no forward-looking shifts. Quarterly cadence.
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
def _cagr(s, lag, years):
    den = s.shift(lag)
    ratio = _safe_div(s, den)
    ratio = ratio.where(ratio > 0, np.nan)
    return ratio.pow(1.0 / years) - 1.0
def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()
def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()
def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()
def _rolling_autocorr(s, window, lag=1, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 3)
    def _ac(w):
        if np.isnan(w).any():
            valid = ~np.isnan(w)
            if valid.sum() < min_periods:
                return np.nan
            ww = w[valid]
        else:
            ww = w
        if len(ww) <= lag + 1:
            return np.nan
        a = ww[:-lag]; b = ww[lag:]
        am = a.mean(); bm = b.mean()
        num = ((a - am) * (b - bm)).sum()
        da = ((a - am) ** 2).sum()
        db = ((b - bm) ** 2).sum()
        d = np.sqrt(da * db)
        return num / d if d > 0 else np.nan
    return s.rolling(window, min_periods=min_periods).apply(_ac, raw=True)
def _rolling_ar1_residual(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 3)
    sl = s.shift(1)
    def _resid(idx):
        i = int(idx[-1])
        lo = max(0, i - window + 1)
        y = s.values[lo:i + 1]
        x = sl.values[lo:i + 1]
        mask = ~(np.isnan(y) | np.isnan(x))
        if mask.sum() < min_periods:
            return np.nan
        y2 = y[mask]; x2 = x[mask]
        xm = x2.mean(); ym = y2.mean()
        num = ((x2 - xm) * (y2 - ym)).sum()
        den = ((x2 - xm) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = ym - slope * xm
        last_y = y[-1]; last_x = x[-1]
        if np.isnan(last_y) or np.isnan(last_x):
            return np.nan
        return last_y - intercept - slope * last_x
    idx_series = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    return idx_series.rolling(window, min_periods=min_periods).apply(_resid, raw=True)
def _rolling_ar1_neg_slope(s, window, min_periods=None):
    """Return negative AR(1) slope of s on s.shift(1) over window; mean-reversion speed proxy."""
    if min_periods is None:
        min_periods = max(window // 2, 3)
    sl = s.shift(1)
    def _ns(idx):
        i = int(idx[-1])
        lo = max(0, i - window + 1)
        y = s.values[lo:i + 1]
        x = sl.values[lo:i + 1]
        mask = ~(np.isnan(y) | np.isnan(x))
        if mask.sum() < min_periods:
            return np.nan
        y2 = y[mask]; x2 = x[mask]
        xm = x2.mean(); ym = y2.mean()
        num = ((x2 - xm) * (y2 - ym)).sum()
        den = ((x2 - xm) ** 2).sum()
        if den == 0:
            return np.nan
        return -(num / den)
    idx_series = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    return idx_series.rolling(window, min_periods=min_periods).apply(_ns, raw=True)

def f21_rgdc_076_rev_growth_choppiness_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    d = yoy.diff()
    sgn_flip = ((np.sign(d) * np.sign(d.shift(1))) < 0).astype(float)
    return (sgn_flip.rolling(12, min_periods=4).sum()).diff().diff().diff()


def f21_rgdc_077_rev_growth_runlength_avg_positive_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    pos = (yoy > 0).fillna(False).astype(int)
    streak = _consec_true_streak(yoy > 0)
    # Average streak length over qtrs where pos==1 in last 8q
    num = (streak * pos).rolling(8, min_periods=1).sum()
    den = pos.rolling(8, min_periods=1).sum().replace(0, np.nan)
    return (num / den).diff().diff().diff()


def f21_rgdc_078_rev_growth_runlength_avg_negative_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    neg = (yoy < 0).fillna(False).astype(int)
    streak = _consec_true_streak(yoy < 0)
    num = (streak * neg).rolling(8, min_periods=1).sum()
    den = neg.rolling(8, min_periods=1).sum().replace(0, np.nan)
    return (num / den).diff().diff().diff()


def f21_rgdc_079_rev_growth_volatility_ratio_4q_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    s4 = yoy.rolling(4, min_periods=2).std()
    s8 = yoy.rolling(8, min_periods=3).std()
    return (_safe_div(s4, s8)).diff().diff().diff()


def f21_rgdc_080_rev_growth_amplitude_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy.rolling(8, min_periods=3).max() - yoy.rolling(8, min_periods=3).min()).diff().diff().diff()


def f21_rgdc_081_rev_yoy_pct_inflection_neg_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sl = _rolling_slope(yoy, 4)
    cond = (sl.shift(4) > 0) & (sl < 0)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_082_rev_yoy_pct_inflection_neg_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sl = _rolling_slope(yoy, 8)
    cond = (sl.shift(8) > 0) & (sl < 0)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_083_rev_qoq_pct_inflection_neg_4q_d3(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    sl = _rolling_slope(qoq, 4)
    cond = (sl.shift(4) > 0) & (sl < 0)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_084_rev_growth_chow_proxy_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    last4 = yoy.rolling(4, min_periods=2).mean()
    prior4 = yoy.shift(4).rolling(4, min_periods=2).mean()
    return (last4 - prior4).diff().diff().diff()


def f21_rgdc_085_rev_growth_chow_proxy_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    last6 = yoy.rolling(6, min_periods=2).mean()
    prior6 = yoy.shift(6).rolling(6, min_periods=2).mean()
    return (last6 - prior6).diff().diff().diff()


def f21_rgdc_086_rev_growth_quandt_proxy_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    def _q(w):
        if np.isnan(w).all():
            return np.nan
        best = 0.0
        n = len(w)
        for k in range(2, n - 1):
            a = w[:k]; b = w[k:]
            ma = np.nanmean(a) if (~np.isnan(a)).any() else np.nan
            mb = np.nanmean(b) if (~np.isnan(b)).any() else np.nan
            if np.isnan(ma) or np.isnan(mb):
                continue
            d = abs(ma - mb)
            if d > best:
                best = d
        return best
    return (yoy.rolling(8, min_periods=4).apply(_q, raw=True)).diff().diff().diff()


def f21_rgdc_087_rev_growth_quandt_proxy_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    def _q(w):
        if np.isnan(w).all():
            return np.nan
        best = 0.0
        n = len(w)
        for k in range(2, n - 1):
            a = w[:k]; b = w[k:]
            ma = np.nanmean(a) if (~np.isnan(a)).any() else np.nan
            mb = np.nanmean(b) if (~np.isnan(b)).any() else np.nan
            if np.isnan(ma) or np.isnan(mb):
                continue
            d = abs(ma - mb)
            if d > best:
                best = d
        return best
    return (yoy.rolling(12, min_periods=5).apply(_q, raw=True)).diff().diff().diff()


def f21_rgdc_088_rev_yoy_pct_break_below_zero_count_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    cond = (yoy <= 0) & (yoy.shift(1) > 0)
    return (_rolling_count(cond, 8)).diff().diff().diff()


def f21_rgdc_089_rev_yoy_pct_first_break_below_zero_indicator_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    cond = (yoy <= 0) & (yoy.shift(1) > 0)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_090_rev_yoy_pct_first_break_below_pos5_indicator_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    cond = (yoy <= 0.05) & (yoy.shift(1) > 0.05)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_091_rev_yoy_pct_break_below_12q_mean_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    m = yoy.rolling(12, min_periods=4).mean()
    return ((yoy < m).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_092_rev_growth_regime_shift_score_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    cur = yoy.rolling(4, min_periods=2).mean()
    prior = yoy.shift(4).rolling(4, min_periods=2).mean()
    return ((cur - prior).abs()).diff().diff().diff()


def f21_rgdc_093_rev_growth_cliff_indicator_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    d = yoy.diff()
    sd = yoy.rolling(8, min_periods=3).std()
    return ((d < -2.0 * sd).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_094_rev_growth_cliff_count_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    d = yoy.diff()
    sd = yoy.rolling(8, min_periods=3).std()
    cliff = (d < -2.0 * sd)
    return (_rolling_count(cliff, 4)).diff().diff().diff()


def f21_rgdc_095_rev_growth_step_down_size_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy.diff().rolling(4, min_periods=2).min()).diff().diff().diff()


def f21_rgdc_096_rev_growth_step_down_size_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy.diff().rolling(8, min_periods=3).min()).diff().diff().diff()


def f21_rgdc_097_rev_growth_cliff_after_smooth_indicator_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd4 = yoy.rolling(4, min_periods=2).std()
    thresh = sd4.expanding(min_periods=4).median()
    d = yoy.diff()
    smooth_prev = sd4.shift(1) < thresh
    big_drop = d < -2.0 * sd4
    return ((smooth_prev & big_drop).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_098_rev_growth_smoothed_break_score_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    cur = yoy.ewm(span=4, adjust=False, min_periods=2).mean()
    prior = yoy.shift(4).ewm(span=4, adjust=False, min_periods=2).mean()
    return ((cur - prior).abs()).diff().diff().diff()


def f21_rgdc_099_rev_growth_phase_shift_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sl = _rolling_slope(yoy, 4)
    cur = np.sign(sl)
    prev = np.sign(sl.shift(4))
    return ((cur != prev).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_100_rev_growth_phase_shift_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sl = _rolling_slope(yoy, 8)
    cur = np.sign(sl)
    prev = np.sign(sl.shift(8))
    return ((cur != prev).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_101_rev_qoq_residual_ar1_8q_d3(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return (_rolling_ar1_residual(qoq, 8)).diff().diff().diff()


def f21_rgdc_102_rev_yoy_residual_ar1_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_ar1_residual(yoy, 8)).diff().diff().diff()


def f21_rgdc_103_rev_yoy_residual_zscore_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    resid = _rolling_ar1_residual(yoy, 8)
    return (_rolling_zscore(resid, 8)).diff().diff().diff()


def f21_rgdc_104_rev_log_growth_4q_sum_d3(revenue):
    r = _safe_div(revenue, revenue.shift(4))
    r = r.where(r > 0, np.nan)
    return (np.log(r)).diff().diff().diff()


def f21_rgdc_105_rev_log_growth_8q_sum_d3(revenue):
    r = _safe_div(revenue, revenue.shift(8))
    r = r.where(r > 0, np.nan)
    return (np.log(r)).diff().diff().diff()


def f21_rgdc_106_rev_log_growth_12q_sum_d3(revenue):
    r = _safe_div(revenue, revenue.shift(12))
    r = r.where(r > 0, np.nan)
    return (np.log(r)).diff().diff().diff()


def f21_rgdc_107_rev_log_rev_8q_slope_d3(revenue):
    return (_rolling_slope(_safe_log(revenue), 8)).diff().diff().diff()


def f21_rgdc_108_rev_log_rev_12q_slope_d3(revenue):
    return (_rolling_slope(_safe_log(revenue), 12)).diff().diff().diff()


def f21_rgdc_109_rev_log_rev_4q_vs_8q_slope_diff_d3(revenue):
    lr = _safe_log(revenue)
    return (_rolling_slope(lr, 4) - _rolling_slope(lr, 8)).diff().diff().diff()


def f21_rgdc_110_rev_log_rev_8q_vs_12q_slope_diff_d3(revenue):
    lr = _safe_log(revenue)
    return (_rolling_slope(lr, 8) - _rolling_slope(lr, 12)).diff().diff().diff()


def f21_rgdc_111_rev_growth_lag1_autocorr_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_autocorr(yoy, 8, lag=1)).diff().diff().diff()


def f21_rgdc_112_rev_growth_lag1_autocorr_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_autocorr(yoy, 12, lag=1)).diff().diff().diff()


def f21_rgdc_113_rev_growth_lag2_autocorr_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_autocorr(yoy, 8, lag=2)).diff().diff().diff()


def f21_rgdc_114_rev_growth_mean_reversion_speed_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_ar1_neg_slope(yoy, 8)).diff().diff().diff()


def f21_rgdc_115_rev_growth_mean_reversion_speed_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_ar1_neg_slope(yoy, 12)).diff().diff().diff()


def f21_rgdc_116_rev_growth_below_zero_dwell_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    streak = _consec_true_streak(yoy < 0)
    return (streak.clip(upper=8)).diff().diff().diff()


def f21_rgdc_117_rev_growth_above_zero_dwell_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    streak = _consec_true_streak(yoy > 0)
    return (streak.clip(upper=8)).diff().diff().diff()


def f21_rgdc_118_rev_log_rev_drawdown_from_8q_max_d3(revenue):
    lr = _safe_log(revenue)
    return (lr - lr.rolling(8, min_periods=3).max()).diff().diff().diff()


def f21_rgdc_119_rev_log_rev_drawdown_from_12q_max_d3(revenue):
    lr = _safe_log(revenue)
    return (lr - lr.rolling(12, min_periods=4).max()).diff().diff().diff()


def f21_rgdc_120_rev_log_rev_drawdown_duration_8q_d3(revenue):
    lr = _safe_log(revenue)
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return (len(w) - 1) - idx
    return (lr.rolling(8, min_periods=3).apply(_bsm, raw=True)).diff().diff().diff()


def f21_rgdc_121_rev_yoy_pct_smooth_then_break_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd4 = yoy.rolling(4, min_periods=2).std()
    thresh = sd4.expanding(min_periods=4).median()
    d = yoy.diff()
    smooth_prev = sd4.shift(1) < thresh
    big_drop = d < -1.0 * sd4
    return ((smooth_prev & big_drop).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_122_rev_yoy_pct_smooth_then_break_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd8 = yoy.rolling(8, min_periods=3).std()
    thresh = sd8.expanding(min_periods=4).median()
    d = yoy.diff()
    smooth_prev = sd8.shift(1) < thresh
    big_drop = d < -1.0 * sd8
    return ((smooth_prev & big_drop).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_123_rev_growth_decay_rate_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_slope(yoy, 4)).diff().diff().diff()


def f21_rgdc_124_rev_growth_decay_rate_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_slope(yoy, 8)).diff().diff().diff()


def f21_rgdc_125_rev_growth_decay_rate_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_slope(yoy, 12)).diff().diff().diff()


def f21_rgdc_126_rev_growth_half_life_proxy_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    slope = _rolling_slope(yoy, 8)
    return (_safe_div(pd.Series(np.log(0.5), index=revenue.index), slope)).diff().diff().diff()


def f21_rgdc_127_rev_growth_decay_acceleration_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_slope(yoy, 4).diff()).diff().diff().diff()


def f21_rgdc_128_rev_growth_failed_recovery_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    prior_drop = (yoy.shift(4) - yoy.shift(8)) < 0
    no_recovery = (yoy - yoy.shift(4)) <= 0
    return ((prior_drop & no_recovery).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_129_rev_growth_failed_recovery_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    prior_drop = (yoy.shift(8) - yoy.shift(16)) < 0
    no_recovery = (yoy - yoy.shift(8)) <= 0
    return ((prior_drop & no_recovery).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_130_rev_growth_two_step_down_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    down = (yoy.diff() < 0).fillna(False).astype(float)
    cnt = down.rolling(4, min_periods=2).sum()
    return ((cnt >= 2).astype(float)).diff().diff().diff()


def f21_rgdc_131_rev_growth_three_step_down_6q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    down = (yoy.diff() < 0).fillna(False).astype(float)
    cnt = down.rolling(6, min_periods=3).sum()
    return ((cnt >= 3).astype(float)).diff().diff().diff()


def f21_rgdc_132_rev_yoy_minus_self_12q_median_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy - yoy.rolling(12, min_periods=4).median()).diff().diff().diff()


def f21_rgdc_133_rev_yoy_minus_self_8q_median_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy - yoy.rolling(8, min_periods=3).median()).diff().diff().diff()


def f21_rgdc_134_rev_yoy_below_4q_min_count_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    rmin = yoy.rolling(4, min_periods=2).min()
    at_min = (yoy <= rmin + 1e-12)
    return (_rolling_count(at_min, 4)).diff().diff().diff()


def f21_rgdc_135_rev_yoy_below_8q_min_count_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    rmin = yoy.rolling(8, min_periods=3).min()
    at_min = (yoy <= rmin + 1e-12)
    return (_rolling_count(at_min, 8)).diff().diff().diff()


def f21_rgdc_136_rev_yoy_in_lowest_quartile_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    q25 = yoy.rolling(8, min_periods=4).quantile(0.25)
    return ((yoy <= q25).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_137_rev_yoy_in_highest_quartile_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    q75 = yoy.rolling(8, min_periods=4).quantile(0.75)
    return ((yoy >= q75).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_138_rev_growth_consistency_index_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd = yoy.rolling(8, min_periods=3).std()
    m = yoy.rolling(8, min_periods=3).mean().abs().replace(0, np.nan)
    return (1.0 - sd / m).diff().diff().diff()


def f21_rgdc_139_rev_growth_consistency_index_12q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd = yoy.rolling(12, min_periods=4).std()
    m = yoy.rolling(12, min_periods=4).mean().abs().replace(0, np.nan)
    return (1.0 - sd / m).diff().diff().diff()


def f21_rgdc_140_rev_growth_compression_index_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    rng = yoy.rolling(4, min_periods=2).max() - yoy.rolling(4, min_periods=2).min()
    m = yoy.rolling(4, min_periods=2).mean().abs().replace(0, np.nan)
    return (rng / m).diff().diff().diff()


def f21_rgdc_141_rev_growth_compression_index_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    rng = yoy.rolling(8, min_periods=3).max() - yoy.rolling(8, min_periods=3).min()
    m = yoy.rolling(8, min_periods=3).mean().abs().replace(0, np.nan)
    return (rng / m).diff().diff().diff()


def f21_rgdc_142_rev_growth_step_change_intensity_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd = yoy.rolling(8, min_periods=3).std().replace(0, np.nan)
    return (yoy.diff().abs() / sd).diff().diff().diff()


def f21_rgdc_143_rev_growth_persistence_below_5pct_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_frac(yoy < 0.05, 4)).diff().diff().diff()


def f21_rgdc_144_rev_growth_persistence_below_5pct_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_frac(yoy < 0.05, 8)).diff().diff().diff()


def f21_rgdc_145_rev_growth_persistence_below_10pct_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_frac(yoy < 0.10, 8)).diff().diff().diff()


def f21_rgdc_146_rev_growth_persistence_negative_4q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_frac(yoy < 0, 4)).diff().diff().diff()


def f21_rgdc_147_rev_growth_persistence_negative_8q_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (_rolling_frac(yoy < 0, 8)).diff().diff().diff()


def f21_rgdc_148_rev_topline_collapse_index_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    sl = _rolling_slope(yoy, 4)
    return (((yoy < 0) & (qoq < 0) & (sl < 0)).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_149_rev_topline_recovery_failed_index_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    prior_drop = (yoy.shift(2) - yoy.shift(6)) < -0.05
    no_rec = (yoy - yoy.shift(2)) <= 0
    return ((prior_drop & no_rec).fillna(False).astype(float)).diff().diff().diff()


def f21_rgdc_150_rev_growth_terminal_signal_d3(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sl = _rolling_slope(yoy, 8)
    pers = _rolling_frac(yoy < 0, 4)
    cond = (yoy < -0.10) & (sl < -0.05) & (pers >= 1.0)
    return (cond.fillna(False).astype(float)).diff().diff().diff()


# ========================================================
#                        REGISTRY
# ========================================================

REVENUE_GROWTH_DECELERATION_D3_REGISTRY_076_150 = {
    "f21_rgdc_076_rev_growth_choppiness_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_076_rev_growth_choppiness_12q_d3},
    "f21_rgdc_077_rev_growth_runlength_avg_positive_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_077_rev_growth_runlength_avg_positive_8q_d3},
    "f21_rgdc_078_rev_growth_runlength_avg_negative_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_078_rev_growth_runlength_avg_negative_8q_d3},
    "f21_rgdc_079_rev_growth_volatility_ratio_4q_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_079_rev_growth_volatility_ratio_4q_8q_d3},
    "f21_rgdc_080_rev_growth_amplitude_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_080_rev_growth_amplitude_8q_d3},
    "f21_rgdc_081_rev_yoy_pct_inflection_neg_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_081_rev_yoy_pct_inflection_neg_4q_d3},
    "f21_rgdc_082_rev_yoy_pct_inflection_neg_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_082_rev_yoy_pct_inflection_neg_8q_d3},
    "f21_rgdc_083_rev_qoq_pct_inflection_neg_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_083_rev_qoq_pct_inflection_neg_4q_d3},
    "f21_rgdc_084_rev_growth_chow_proxy_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_084_rev_growth_chow_proxy_8q_d3},
    "f21_rgdc_085_rev_growth_chow_proxy_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_085_rev_growth_chow_proxy_12q_d3},
    "f21_rgdc_086_rev_growth_quandt_proxy_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_086_rev_growth_quandt_proxy_8q_d3},
    "f21_rgdc_087_rev_growth_quandt_proxy_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_087_rev_growth_quandt_proxy_12q_d3},
    "f21_rgdc_088_rev_yoy_pct_break_below_zero_count_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_088_rev_yoy_pct_break_below_zero_count_8q_d3},
    "f21_rgdc_089_rev_yoy_pct_first_break_below_zero_indicator_d3": {"inputs": ["revenue"], "func": f21_rgdc_089_rev_yoy_pct_first_break_below_zero_indicator_d3},
    "f21_rgdc_090_rev_yoy_pct_first_break_below_pos5_indicator_d3": {"inputs": ["revenue"], "func": f21_rgdc_090_rev_yoy_pct_first_break_below_pos5_indicator_d3},
    "f21_rgdc_091_rev_yoy_pct_break_below_12q_mean_d3": {"inputs": ["revenue"], "func": f21_rgdc_091_rev_yoy_pct_break_below_12q_mean_d3},
    "f21_rgdc_092_rev_growth_regime_shift_score_d3": {"inputs": ["revenue"], "func": f21_rgdc_092_rev_growth_regime_shift_score_d3},
    "f21_rgdc_093_rev_growth_cliff_indicator_d3": {"inputs": ["revenue"], "func": f21_rgdc_093_rev_growth_cliff_indicator_d3},
    "f21_rgdc_094_rev_growth_cliff_count_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_094_rev_growth_cliff_count_4q_d3},
    "f21_rgdc_095_rev_growth_step_down_size_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_095_rev_growth_step_down_size_4q_d3},
    "f21_rgdc_096_rev_growth_step_down_size_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_096_rev_growth_step_down_size_8q_d3},
    "f21_rgdc_097_rev_growth_cliff_after_smooth_indicator_d3": {"inputs": ["revenue"], "func": f21_rgdc_097_rev_growth_cliff_after_smooth_indicator_d3},
    "f21_rgdc_098_rev_growth_smoothed_break_score_d3": {"inputs": ["revenue"], "func": f21_rgdc_098_rev_growth_smoothed_break_score_d3},
    "f21_rgdc_099_rev_growth_phase_shift_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_099_rev_growth_phase_shift_4q_d3},
    "f21_rgdc_100_rev_growth_phase_shift_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_100_rev_growth_phase_shift_8q_d3},
    "f21_rgdc_101_rev_qoq_residual_ar1_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_101_rev_qoq_residual_ar1_8q_d3},
    "f21_rgdc_102_rev_yoy_residual_ar1_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_102_rev_yoy_residual_ar1_8q_d3},
    "f21_rgdc_103_rev_yoy_residual_zscore_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_103_rev_yoy_residual_zscore_8q_d3},
    "f21_rgdc_104_rev_log_growth_4q_sum_d3": {"inputs": ["revenue"], "func": f21_rgdc_104_rev_log_growth_4q_sum_d3},
    "f21_rgdc_105_rev_log_growth_8q_sum_d3": {"inputs": ["revenue"], "func": f21_rgdc_105_rev_log_growth_8q_sum_d3},
    "f21_rgdc_106_rev_log_growth_12q_sum_d3": {"inputs": ["revenue"], "func": f21_rgdc_106_rev_log_growth_12q_sum_d3},
    "f21_rgdc_107_rev_log_rev_8q_slope_d3": {"inputs": ["revenue"], "func": f21_rgdc_107_rev_log_rev_8q_slope_d3},
    "f21_rgdc_108_rev_log_rev_12q_slope_d3": {"inputs": ["revenue"], "func": f21_rgdc_108_rev_log_rev_12q_slope_d3},
    "f21_rgdc_109_rev_log_rev_4q_vs_8q_slope_diff_d3": {"inputs": ["revenue"], "func": f21_rgdc_109_rev_log_rev_4q_vs_8q_slope_diff_d3},
    "f21_rgdc_110_rev_log_rev_8q_vs_12q_slope_diff_d3": {"inputs": ["revenue"], "func": f21_rgdc_110_rev_log_rev_8q_vs_12q_slope_diff_d3},
    "f21_rgdc_111_rev_growth_lag1_autocorr_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_111_rev_growth_lag1_autocorr_8q_d3},
    "f21_rgdc_112_rev_growth_lag1_autocorr_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_112_rev_growth_lag1_autocorr_12q_d3},
    "f21_rgdc_113_rev_growth_lag2_autocorr_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_113_rev_growth_lag2_autocorr_8q_d3},
    "f21_rgdc_114_rev_growth_mean_reversion_speed_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_114_rev_growth_mean_reversion_speed_8q_d3},
    "f21_rgdc_115_rev_growth_mean_reversion_speed_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_115_rev_growth_mean_reversion_speed_12q_d3},
    "f21_rgdc_116_rev_growth_below_zero_dwell_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_116_rev_growth_below_zero_dwell_8q_d3},
    "f21_rgdc_117_rev_growth_above_zero_dwell_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_117_rev_growth_above_zero_dwell_8q_d3},
    "f21_rgdc_118_rev_log_rev_drawdown_from_8q_max_d3": {"inputs": ["revenue"], "func": f21_rgdc_118_rev_log_rev_drawdown_from_8q_max_d3},
    "f21_rgdc_119_rev_log_rev_drawdown_from_12q_max_d3": {"inputs": ["revenue"], "func": f21_rgdc_119_rev_log_rev_drawdown_from_12q_max_d3},
    "f21_rgdc_120_rev_log_rev_drawdown_duration_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_120_rev_log_rev_drawdown_duration_8q_d3},
    "f21_rgdc_121_rev_yoy_pct_smooth_then_break_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_121_rev_yoy_pct_smooth_then_break_4q_d3},
    "f21_rgdc_122_rev_yoy_pct_smooth_then_break_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_122_rev_yoy_pct_smooth_then_break_8q_d3},
    "f21_rgdc_123_rev_growth_decay_rate_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_123_rev_growth_decay_rate_4q_d3},
    "f21_rgdc_124_rev_growth_decay_rate_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_124_rev_growth_decay_rate_8q_d3},
    "f21_rgdc_125_rev_growth_decay_rate_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_125_rev_growth_decay_rate_12q_d3},
    "f21_rgdc_126_rev_growth_half_life_proxy_d3": {"inputs": ["revenue"], "func": f21_rgdc_126_rev_growth_half_life_proxy_d3},
    "f21_rgdc_127_rev_growth_decay_acceleration_d3": {"inputs": ["revenue"], "func": f21_rgdc_127_rev_growth_decay_acceleration_d3},
    "f21_rgdc_128_rev_growth_failed_recovery_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_128_rev_growth_failed_recovery_4q_d3},
    "f21_rgdc_129_rev_growth_failed_recovery_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_129_rev_growth_failed_recovery_8q_d3},
    "f21_rgdc_130_rev_growth_two_step_down_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_130_rev_growth_two_step_down_4q_d3},
    "f21_rgdc_131_rev_growth_three_step_down_6q_d3": {"inputs": ["revenue"], "func": f21_rgdc_131_rev_growth_three_step_down_6q_d3},
    "f21_rgdc_132_rev_yoy_minus_self_12q_median_d3": {"inputs": ["revenue"], "func": f21_rgdc_132_rev_yoy_minus_self_12q_median_d3},
    "f21_rgdc_133_rev_yoy_minus_self_8q_median_d3": {"inputs": ["revenue"], "func": f21_rgdc_133_rev_yoy_minus_self_8q_median_d3},
    "f21_rgdc_134_rev_yoy_below_4q_min_count_d3": {"inputs": ["revenue"], "func": f21_rgdc_134_rev_yoy_below_4q_min_count_d3},
    "f21_rgdc_135_rev_yoy_below_8q_min_count_d3": {"inputs": ["revenue"], "func": f21_rgdc_135_rev_yoy_below_8q_min_count_d3},
    "f21_rgdc_136_rev_yoy_in_lowest_quartile_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_136_rev_yoy_in_lowest_quartile_8q_d3},
    "f21_rgdc_137_rev_yoy_in_highest_quartile_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_137_rev_yoy_in_highest_quartile_8q_d3},
    "f21_rgdc_138_rev_growth_consistency_index_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_138_rev_growth_consistency_index_8q_d3},
    "f21_rgdc_139_rev_growth_consistency_index_12q_d3": {"inputs": ["revenue"], "func": f21_rgdc_139_rev_growth_consistency_index_12q_d3},
    "f21_rgdc_140_rev_growth_compression_index_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_140_rev_growth_compression_index_4q_d3},
    "f21_rgdc_141_rev_growth_compression_index_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_141_rev_growth_compression_index_8q_d3},
    "f21_rgdc_142_rev_growth_step_change_intensity_d3": {"inputs": ["revenue"], "func": f21_rgdc_142_rev_growth_step_change_intensity_d3},
    "f21_rgdc_143_rev_growth_persistence_below_5pct_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_143_rev_growth_persistence_below_5pct_4q_d3},
    "f21_rgdc_144_rev_growth_persistence_below_5pct_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_144_rev_growth_persistence_below_5pct_8q_d3},
    "f21_rgdc_145_rev_growth_persistence_below_10pct_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_145_rev_growth_persistence_below_10pct_8q_d3},
    "f21_rgdc_146_rev_growth_persistence_negative_4q_d3": {"inputs": ["revenue"], "func": f21_rgdc_146_rev_growth_persistence_negative_4q_d3},
    "f21_rgdc_147_rev_growth_persistence_negative_8q_d3": {"inputs": ["revenue"], "func": f21_rgdc_147_rev_growth_persistence_negative_8q_d3},
    "f21_rgdc_148_rev_topline_collapse_index_d3": {"inputs": ["revenue"], "func": f21_rgdc_148_rev_topline_collapse_index_d3},
    "f21_rgdc_149_rev_topline_recovery_failed_index_d3": {"inputs": ["revenue"], "func": f21_rgdc_149_rev_topline_recovery_failed_index_d3},
    "f21_rgdc_150_rev_growth_terminal_signal_d3": {"inputs": ["revenue"], "func": f21_rgdc_150_rev_growth_terminal_signal_d3},
}
