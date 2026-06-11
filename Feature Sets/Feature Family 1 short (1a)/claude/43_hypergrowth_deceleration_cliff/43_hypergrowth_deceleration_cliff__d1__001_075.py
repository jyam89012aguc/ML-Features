"""hypergrowth_deceleration_cliff d1 features 001_075 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
import numpy as np
import pandas as pd
QDAYS = 63
YDAYS = 252
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260
MDAYS = 21
WDAYS = 5

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_log_signed(s):
    """Log of |s|+1 with sign — for series that cross zero (fcf, netinc)."""
    return np.sign(s) * np.log1p(s.abs())

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)

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

def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)

def _max_streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        best = cur = 0
        for v in w:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag_series.rolling(window, min_periods=min_periods).apply(_ms, raw=True)

def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)

def f43_hdcl_001_revenue_yoy_growth_log_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(YDAYS).diff()

def f43_hdcl_002_revenue_3y_cagr_log_d1(revenue: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(DDAYS_3Y) / 3.0).diff()

def f43_hdcl_003_revenue_5y_cagr_log_d1(revenue: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(DDAYS_5Y) / 5.0).diff()

def f43_hdcl_004_revenue_yoy_minus_3y_cagr_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    cagr3 = _safe_log(revenue).diff(DDAYS_3Y) / 3.0
    return (yoy - cagr3).diff()

def f43_hdcl_005_revenue_yoy_minus_5y_cagr_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    cagr5 = _safe_log(revenue).diff(DDAYS_5Y) / 5.0
    return (yoy - cagr5).diff()

def f43_hdcl_006_revenue_qoq_growth_log_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(QDAYS).diff()

def f43_hdcl_007_revenue_qoq_2q_diff_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(QDAYS * 2).diff()

def f43_hdcl_008_revenue_growth_rate_change_1y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy - yoy.shift(YDAYS)).diff()

def f43_hdcl_009_revenue_growth_rate_change_2y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy - yoy.shift(DDAYS_2Y)).diff()

def f43_hdcl_010_revenue_growth_rate_acceleration_4q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    return (qoq - qoq.shift(YDAYS)).diff()

def f43_hdcl_011_revenue_growth_volatility_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).std().diff()

def f43_hdcl_012_revenue_yoy_max_in_5y_minus_current_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max() - yoy).diff()

def f43_hdcl_013_days_since_revenue_yoy_max_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _days_since_max(yoy, DDAYS_5Y).diff()

def f43_hdcl_014_revenue_yoy_streak_above_30pct_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.3).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.3).astype(float)
    return (flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum() / QDAYS).diff()

def f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.5).astype(float)
    return (flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum() / QDAYS).diff()

def f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < yoy.shift(QDAYS)).astype(int)
    return _streak_above_zero(flag, YDAYS).diff()

def f43_hdcl_018_revenue_log_diff_3q_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(QDAYS * 3).diff()

def f43_hdcl_019_revenue_log_diff_6q_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(QDAYS * 6).diff()

def f43_hdcl_020_revenue_log_diff_8q_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(DDAYS_2Y).diff()

def f43_hdcl_021_revenue_sequential_decline_indicator_2q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = ((qoq < 0) & (qoq.shift(QDAYS) < 0)).astype(float)
    return flag.where(qoq.notna() & qoq.shift(QDAYS).notna(), np.nan).diff()

def f43_hdcl_022_revenue_yoy_below_long_mean_count_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m5y = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (yoy < m5y).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    thr = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.9)
    flag = (yoy >= thr).astype(float)
    cnt = flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan).diff()

def f43_hdcl_024_revenue_yoy_zscore_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_zscore(yoy, DDAYS_5Y).diff()

def f43_hdcl_025_revenue_yoy_rank_pct_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_rank_pct(yoy, DDAYS_5Y).diff()

def f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (_safe_log_signed(yoy) - _safe_log_signed(yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max())).diff()

def f43_hdcl_027_revenue_yoy_vs_2y_avg_change_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy - yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff()

def f43_hdcl_028_revenue_qoq_minus_yoy_divergence_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    return (4.0 * qoq - yoy).diff()

def f43_hdcl_029_revenue_growth_2nd_derivative_yoy_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(YDAYS).diff(YDAYS).diff()

def f43_hdcl_030_revenue_growth_2nd_derivative_qoq_d1(revenue: pd.Series) -> pd.Series:
    return _safe_log(revenue).diff(QDAYS).diff(QDAYS).diff()

def f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q_d1(revenue: pd.Series) -> pd.Series:
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS).clip(upper=0.0)
    return accel.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_032_revenue_yoy_decline_speed_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_2Y).diff()

def f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    diff = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return _rolling_zscore(diff, DDAYS_5Y).diff()

def f43_hdcl_034_revenue_yoy_below_p25_streak_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    thr = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = (yoy < thr).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg_d1(revenue: pd.Series) -> pd.Series:
    d4 = _safe_log(revenue).diff(YDAYS)
    return (d4 - d4.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff()

def f43_hdcl_036_revenue_growth_decel_3q_minus_1q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy - yoy.shift(QDAYS * 3)).diff()

def f43_hdcl_037_revenue_growth_dispersion_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    p75 = qoq.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    p25 = qoq.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    return (p75 - p25).diff()

def f43_hdcl_038_revenue_growth_kurtosis_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_k, raw=True).diff()

def f43_hdcl_039_revenue_growth_skewness_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sk, raw=True).diff()

def f43_hdcl_040_revenue_yoy_change_acceleration_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.diff(YDAYS).diff(YDAYS).diff()

def f43_hdcl_041_revenue_yoy_4q_window_min_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy.rolling(YDAYS, min_periods=QDAYS).mean() - yoy).diff()

def f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy.rolling(QDAYS * 2, min_periods=QDAYS).mean() - yoy).diff()

def f43_hdcl_044_revenue_yoy_negative_count_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_045_revenue_max_2q_drawdown_intensity_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy - yoy.shift(QDAYS * 2)
    return drop.rolling(DDAYS_5Y, min_periods=YDAYS).min().diff()

def f43_hdcl_046_gp_yoy_growth_log_d1(gp: pd.Series) -> pd.Series:
    return _safe_log(gp).diff(YDAYS).diff()

def f43_hdcl_047_opinc_yoy_growth_log_d1(opinc: pd.Series) -> pd.Series:
    return _safe_log_signed(opinc).diff(YDAYS).diff()

def f43_hdcl_048_ebitda_yoy_growth_log_d1(ebitda: pd.Series) -> pd.Series:
    return _safe_log_signed(ebitda).diff(YDAYS).diff()

def f43_hdcl_049_netinc_yoy_growth_log_d1(netinc: pd.Series) -> pd.Series:
    return _safe_log_signed(netinc).diff(YDAYS).diff()

def f43_hdcl_050_fcf_yoy_change_signed_log_d1(fcf: pd.Series) -> pd.Series:
    return _safe_log_signed(fcf).diff(YDAYS).diff()

def f43_hdcl_051_revenue_yoy_minus_gp_yoy_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(YDAYS) - _safe_log(gp).diff(YDAYS)).diff()

def f43_hdcl_052_revenue_yoy_minus_opinc_yoy_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(YDAYS) - _safe_log_signed(opinc).diff(YDAYS)).diff()

def f43_hdcl_053_revenue_yoy_minus_ebitda_yoy_d1(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(YDAYS) - _safe_log_signed(ebitda).diff(YDAYS)).diff()

def f43_hdcl_054_revenue_yoy_minus_netinc_yoy_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    return (_safe_log(revenue).diff(YDAYS) - _safe_log_signed(netinc).diff(YDAYS)).diff()

def f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q_d1(revenue: pd.Series, gp: pd.Series, opinc: pd.Series) -> pd.Series:
    r_yoy = _safe_log(revenue).diff(YDAYS)
    g_yoy = _safe_log(gp).diff(YDAYS)
    o_yoy = _safe_log_signed(opinc).diff(YDAYS)
    rm = r_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    gm = g_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    om = o_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((r_yoy < rm) & (g_yoy < gm) & (o_yoy < om)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    r_yoy = _safe_log(revenue).diff(YDAYS)
    o_yoy = _safe_log_signed(opinc).diff(YDAYS)
    f_yoy = _safe_log_signed(fcf).diff(YDAYS)
    rm = r_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    om = o_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    fm = f_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((r_yoy < rm) & (o_yoy < om) & (f_yoy < fm)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_057_gp_growth_below_revenue_growth_streak_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    flag = (_safe_log(gp).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_058_opinc_growth_below_revenue_growth_streak_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(opinc).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_059_netinc_growth_below_revenue_growth_streak_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(netinc).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_060_fcf_growth_below_revenue_growth_streak_d1(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(fcf).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_061_metric_decel_breadth_4q_d1(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    series_list = [_safe_log(revenue).diff(YDAYS), _safe_log(gp).diff(YDAYS), _safe_log_signed(opinc).diff(YDAYS), _safe_log_signed(ebitda).diff(YDAYS), _safe_log_signed(netinc).diff(YDAYS), _safe_log_signed(fcf).diff(YDAYS)]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m_4q = s.rolling(YDAYS, min_periods=QDAYS).mean()
        m_5y = s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
        total = total + (m_4q < m_5y).astype(float)
        valid = valid & m_4q.notna() & m_5y.notna()
    return total.where(valid, np.nan).diff()

def f43_hdcl_062_metric_decel_breadth_8q_d1(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    series_list = [_safe_log(revenue).diff(YDAYS), _safe_log(gp).diff(YDAYS), _safe_log_signed(opinc).diff(YDAYS), _safe_log_signed(ebitda).diff(YDAYS), _safe_log_signed(netinc).diff(YDAYS), _safe_log_signed(fcf).diff(YDAYS)]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m_8q = s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
        m_5y = s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
        total = total + (m_8q < m_5y).astype(float)
        valid = valid & m_8q.notna() & m_5y.notna()
    return total.where(valid, np.nan).diff()

def f43_hdcl_063_compound_yoy_decel_acceleration_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    r = _safe_log(revenue).diff(YDAYS).diff(YDAYS)
    o = _safe_log_signed(opinc).diff(YDAYS).diff(YDAYS)
    f = _safe_log_signed(fcf).diff(YDAYS).diff(YDAYS)
    return ((r + o + f) / 3.0).diff()

def f43_hdcl_064_yoy_growth_compound_zscore_252d_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    z_r = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    z_o = _rolling_zscore(_safe_log_signed(opinc).diff(YDAYS), DDAYS_5Y)
    z_f = _rolling_zscore(_safe_log_signed(fcf).diff(YDAYS), DDAYS_5Y)
    return ((z_r + z_o + z_f) / 3.0).diff()

def f43_hdcl_065_ebitda_yoy_decline_streak_d1(ebitda: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(ebitda).diff(YDAYS) < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_066_netinc_yoy_decline_streak_d1(netinc: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(netinc).diff(YDAYS) < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_067_opinc_yoy_change_rate_d1(opinc: pd.Series) -> pd.Series:
    yoy = _safe_log_signed(opinc).diff(YDAYS)
    return (yoy - yoy.shift(YDAYS)).diff()

def f43_hdcl_068_fcf_yoy_change_acceleration_d1(fcf: pd.Series) -> pd.Series:
    return _safe_log_signed(fcf).diff(YDAYS).diff(YDAYS).diff()

def f43_hdcl_069_revenue_to_netinc_growth_gap_zscore_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    gap = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(netinc).diff(YDAYS)
    return _rolling_zscore(gap, DDAYS_5Y).diff()

def f43_hdcl_070_revenue_to_fcf_growth_gap_zscore_d1(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    gap = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(fcf).diff(YDAYS)
    return _rolling_zscore(gap, DDAYS_5Y).diff()

def f43_hdcl_071_sustained_hypergrowth_indicator_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.3).astype(float)
    cnt = flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return (cnt >= 8 * QDAYS).astype(float).where(cnt.notna(), np.nan).diff()

def f43_hdcl_072_sustained_hypergrowth_indicator_3y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.3).astype(float)
    cnt = flag.rolling(DDAYS_3Y, min_periods=YDAYS).sum()
    return (cnt >= 6 * QDAYS).astype(float).where(cnt.notna(), np.nan).diff()

def f43_hdcl_073_quarters_above_hypergrowth_then_below_count_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy <= 0.1) & (yoy.shift(YDAYS) > 0.3)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_074_transition_from_hypergrowth_to_normal_recency_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy <= 0.1) & (yoy.shift(YDAYS) > 0.3)).astype(float)
    return _recency_since_event(flag, DDAYS_5Y).diff()

def f43_hdcl_075_hypergrowth_peak_to_current_drop_pct_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_div(mx - yoy, mx).diff()
HYPERGROWTH_DECELERATION_CLIFF_D1_REGISTRY_001_075 = {'f43_hdcl_001_revenue_yoy_growth_log_d1': {'inputs': ['revenue'], 'func': f43_hdcl_001_revenue_yoy_growth_log_d1}, 'f43_hdcl_002_revenue_3y_cagr_log_d1': {'inputs': ['revenue'], 'func': f43_hdcl_002_revenue_3y_cagr_log_d1}, 'f43_hdcl_003_revenue_5y_cagr_log_d1': {'inputs': ['revenue'], 'func': f43_hdcl_003_revenue_5y_cagr_log_d1}, 'f43_hdcl_004_revenue_yoy_minus_3y_cagr_d1': {'inputs': ['revenue'], 'func': f43_hdcl_004_revenue_yoy_minus_3y_cagr_d1}, 'f43_hdcl_005_revenue_yoy_minus_5y_cagr_d1': {'inputs': ['revenue'], 'func': f43_hdcl_005_revenue_yoy_minus_5y_cagr_d1}, 'f43_hdcl_006_revenue_qoq_growth_log_d1': {'inputs': ['revenue'], 'func': f43_hdcl_006_revenue_qoq_growth_log_d1}, 'f43_hdcl_007_revenue_qoq_2q_diff_d1': {'inputs': ['revenue'], 'func': f43_hdcl_007_revenue_qoq_2q_diff_d1}, 'f43_hdcl_008_revenue_growth_rate_change_1y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_008_revenue_growth_rate_change_1y_d1}, 'f43_hdcl_009_revenue_growth_rate_change_2y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_009_revenue_growth_rate_change_2y_d1}, 'f43_hdcl_010_revenue_growth_rate_acceleration_4q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_010_revenue_growth_rate_acceleration_4q_d1}, 'f43_hdcl_011_revenue_growth_volatility_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_011_revenue_growth_volatility_8q_d1}, 'f43_hdcl_012_revenue_yoy_max_in_5y_minus_current_d1': {'inputs': ['revenue'], 'func': f43_hdcl_012_revenue_yoy_max_in_5y_minus_current_d1}, 'f43_hdcl_013_days_since_revenue_yoy_max_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_013_days_since_revenue_yoy_max_5y_d1}, 'f43_hdcl_014_revenue_yoy_streak_above_30pct_d1': {'inputs': ['revenue'], 'func': f43_hdcl_014_revenue_yoy_streak_above_30pct_d1}, 'f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y_d1}, 'f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y_d1}, 'f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q_d1}, 'f43_hdcl_018_revenue_log_diff_3q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_018_revenue_log_diff_3q_d1}, 'f43_hdcl_019_revenue_log_diff_6q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_019_revenue_log_diff_6q_d1}, 'f43_hdcl_020_revenue_log_diff_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_020_revenue_log_diff_8q_d1}, 'f43_hdcl_021_revenue_sequential_decline_indicator_2q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_021_revenue_sequential_decline_indicator_2q_d1}, 'f43_hdcl_022_revenue_yoy_below_long_mean_count_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_022_revenue_yoy_below_long_mean_count_8q_d1}, 'f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator_d1}, 'f43_hdcl_024_revenue_yoy_zscore_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_024_revenue_yoy_zscore_5y_d1}, 'f43_hdcl_025_revenue_yoy_rank_pct_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_025_revenue_yoy_rank_pct_5y_d1}, 'f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log_d1': {'inputs': ['revenue'], 'func': f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log_d1}, 'f43_hdcl_027_revenue_yoy_vs_2y_avg_change_d1': {'inputs': ['revenue'], 'func': f43_hdcl_027_revenue_yoy_vs_2y_avg_change_d1}, 'f43_hdcl_028_revenue_qoq_minus_yoy_divergence_d1': {'inputs': ['revenue'], 'func': f43_hdcl_028_revenue_qoq_minus_yoy_divergence_d1}, 'f43_hdcl_029_revenue_growth_2nd_derivative_yoy_d1': {'inputs': ['revenue'], 'func': f43_hdcl_029_revenue_growth_2nd_derivative_yoy_d1}, 'f43_hdcl_030_revenue_growth_2nd_derivative_qoq_d1': {'inputs': ['revenue'], 'func': f43_hdcl_030_revenue_growth_2nd_derivative_qoq_d1}, 'f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q_d1}, 'f43_hdcl_032_revenue_yoy_decline_speed_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_032_revenue_yoy_decline_speed_8q_d1}, 'f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore_d1': {'inputs': ['revenue'], 'func': f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore_d1}, 'f43_hdcl_034_revenue_yoy_below_p25_streak_d1': {'inputs': ['revenue'], 'func': f43_hdcl_034_revenue_yoy_below_p25_streak_d1}, 'f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg_d1': {'inputs': ['revenue'], 'func': f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg_d1}, 'f43_hdcl_036_revenue_growth_decel_3q_minus_1q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_036_revenue_growth_decel_3q_minus_1q_d1}, 'f43_hdcl_037_revenue_growth_dispersion_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_037_revenue_growth_dispersion_8q_d1}, 'f43_hdcl_038_revenue_growth_kurtosis_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_038_revenue_growth_kurtosis_8q_d1}, 'f43_hdcl_039_revenue_growth_skewness_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_039_revenue_growth_skewness_8q_d1}, 'f43_hdcl_040_revenue_yoy_change_acceleration_d1': {'inputs': ['revenue'], 'func': f43_hdcl_040_revenue_yoy_change_acceleration_d1}, 'f43_hdcl_041_revenue_yoy_4q_window_min_d1': {'inputs': ['revenue'], 'func': f43_hdcl_041_revenue_yoy_4q_window_min_d1}, 'f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now_d1': {'inputs': ['revenue'], 'func': f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now_d1}, 'f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now_d1': {'inputs': ['revenue'], 'func': f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now_d1}, 'f43_hdcl_044_revenue_yoy_negative_count_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_044_revenue_yoy_negative_count_8q_d1}, 'f43_hdcl_045_revenue_max_2q_drawdown_intensity_d1': {'inputs': ['revenue'], 'func': f43_hdcl_045_revenue_max_2q_drawdown_intensity_d1}, 'f43_hdcl_046_gp_yoy_growth_log_d1': {'inputs': ['gp'], 'func': f43_hdcl_046_gp_yoy_growth_log_d1}, 'f43_hdcl_047_opinc_yoy_growth_log_d1': {'inputs': ['opinc'], 'func': f43_hdcl_047_opinc_yoy_growth_log_d1}, 'f43_hdcl_048_ebitda_yoy_growth_log_d1': {'inputs': ['ebitda'], 'func': f43_hdcl_048_ebitda_yoy_growth_log_d1}, 'f43_hdcl_049_netinc_yoy_growth_log_d1': {'inputs': ['netinc'], 'func': f43_hdcl_049_netinc_yoy_growth_log_d1}, 'f43_hdcl_050_fcf_yoy_change_signed_log_d1': {'inputs': ['fcf'], 'func': f43_hdcl_050_fcf_yoy_change_signed_log_d1}, 'f43_hdcl_051_revenue_yoy_minus_gp_yoy_d1': {'inputs': ['revenue', 'gp'], 'func': f43_hdcl_051_revenue_yoy_minus_gp_yoy_d1}, 'f43_hdcl_052_revenue_yoy_minus_opinc_yoy_d1': {'inputs': ['revenue', 'opinc'], 'func': f43_hdcl_052_revenue_yoy_minus_opinc_yoy_d1}, 'f43_hdcl_053_revenue_yoy_minus_ebitda_yoy_d1': {'inputs': ['revenue', 'ebitda'], 'func': f43_hdcl_053_revenue_yoy_minus_ebitda_yoy_d1}, 'f43_hdcl_054_revenue_yoy_minus_netinc_yoy_d1': {'inputs': ['revenue', 'netinc'], 'func': f43_hdcl_054_revenue_yoy_minus_netinc_yoy_d1}, 'f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q_d1': {'inputs': ['revenue', 'gp', 'opinc'], 'func': f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q_d1}, 'f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q_d1}, 'f43_hdcl_057_gp_growth_below_revenue_growth_streak_d1': {'inputs': ['revenue', 'gp'], 'func': f43_hdcl_057_gp_growth_below_revenue_growth_streak_d1}, 'f43_hdcl_058_opinc_growth_below_revenue_growth_streak_d1': {'inputs': ['revenue', 'opinc'], 'func': f43_hdcl_058_opinc_growth_below_revenue_growth_streak_d1}, 'f43_hdcl_059_netinc_growth_below_revenue_growth_streak_d1': {'inputs': ['revenue', 'netinc'], 'func': f43_hdcl_059_netinc_growth_below_revenue_growth_streak_d1}, 'f43_hdcl_060_fcf_growth_below_revenue_growth_streak_d1': {'inputs': ['revenue', 'fcf'], 'func': f43_hdcl_060_fcf_growth_below_revenue_growth_streak_d1}, 'f43_hdcl_061_metric_decel_breadth_4q_d1': {'inputs': ['revenue', 'gp', 'opinc', 'ebitda', 'netinc', 'fcf'], 'func': f43_hdcl_061_metric_decel_breadth_4q_d1}, 'f43_hdcl_062_metric_decel_breadth_8q_d1': {'inputs': ['revenue', 'gp', 'opinc', 'ebitda', 'netinc', 'fcf'], 'func': f43_hdcl_062_metric_decel_breadth_8q_d1}, 'f43_hdcl_063_compound_yoy_decel_acceleration_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_063_compound_yoy_decel_acceleration_d1}, 'f43_hdcl_064_yoy_growth_compound_zscore_252d_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_064_yoy_growth_compound_zscore_252d_d1}, 'f43_hdcl_065_ebitda_yoy_decline_streak_d1': {'inputs': ['ebitda'], 'func': f43_hdcl_065_ebitda_yoy_decline_streak_d1}, 'f43_hdcl_066_netinc_yoy_decline_streak_d1': {'inputs': ['netinc'], 'func': f43_hdcl_066_netinc_yoy_decline_streak_d1}, 'f43_hdcl_067_opinc_yoy_change_rate_d1': {'inputs': ['opinc'], 'func': f43_hdcl_067_opinc_yoy_change_rate_d1}, 'f43_hdcl_068_fcf_yoy_change_acceleration_d1': {'inputs': ['fcf'], 'func': f43_hdcl_068_fcf_yoy_change_acceleration_d1}, 'f43_hdcl_069_revenue_to_netinc_growth_gap_zscore_d1': {'inputs': ['revenue', 'netinc'], 'func': f43_hdcl_069_revenue_to_netinc_growth_gap_zscore_d1}, 'f43_hdcl_070_revenue_to_fcf_growth_gap_zscore_d1': {'inputs': ['revenue', 'fcf'], 'func': f43_hdcl_070_revenue_to_fcf_growth_gap_zscore_d1}, 'f43_hdcl_071_sustained_hypergrowth_indicator_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_071_sustained_hypergrowth_indicator_5y_d1}, 'f43_hdcl_072_sustained_hypergrowth_indicator_3y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_072_sustained_hypergrowth_indicator_3y_d1}, 'f43_hdcl_073_quarters_above_hypergrowth_then_below_count_d1': {'inputs': ['revenue'], 'func': f43_hdcl_073_quarters_above_hypergrowth_then_below_count_d1}, 'f43_hdcl_074_transition_from_hypergrowth_to_normal_recency_d1': {'inputs': ['revenue'], 'func': f43_hdcl_074_transition_from_hypergrowth_to_normal_recency_d1}, 'f43_hdcl_075_hypergrowth_peak_to_current_drop_pct_d1': {'inputs': ['revenue'], 'func': f43_hdcl_075_hypergrowth_peak_to_current_drop_pct_d1}}
