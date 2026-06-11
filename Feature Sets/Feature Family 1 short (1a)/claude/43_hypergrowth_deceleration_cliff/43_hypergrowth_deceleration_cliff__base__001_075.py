"""hypergrowth_deceleration_cliff base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: stocks that sustained hyper-growth (revenue YoY >> 30%) and are
transitioning into a sudden flattening / outright decline ("the cliff").
Captures multi-horizon growth rates, deceleration magnitude, compound
deceleration across revenue/gp/opinc/ebitda/netinc/fcf, and hypergrowth-
state indicators. Continued in __base__076_150.py for 150 total.

Inputs: SF1 ARQ columns forward-filled to daily — `revenue`, `gp`, `cor`,
`opinc`, `ebitda`, `netinc`, `fcf`, `ncfo`. PIT-clean: right-anchored
rolling, explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

QDAYS = 63           # 1 quarter
YDAYS = 252          # 4 quarters / 1 year
DDAYS_2Y = 504       # 8 quarters / 2 years
DDAYS_3Y = 756       # 12 quarters / 3 years
DDAYS_5Y = 1260      # 20 quarters / 5 years
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
    idx = num.index if hasattr(num, "index") else None
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
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
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


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f43_hdcl_001_revenue_yoy_growth_log(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_252d_ago) — canonical YoY revenue growth rate."""
    return _safe_log(revenue).diff(YDAYS)


def f43_hdcl_002_revenue_3y_cagr_log(revenue: pd.Series) -> pd.Series:
    """3y log change / 3 = annualized 3y log CAGR — long-horizon baseline."""
    return _safe_log(revenue).diff(DDAYS_3Y) / 3.0


def f43_hdcl_003_revenue_5y_cagr_log(revenue: pd.Series) -> pd.Series:
    """5y log change / 5 = annualized 5y log CAGR."""
    return _safe_log(revenue).diff(DDAYS_5Y) / 5.0


def f43_hdcl_004_revenue_yoy_minus_3y_cagr(revenue: pd.Series) -> pd.Series:
    """YoY growth minus 3y CAGR — recent vs medium-run pace (negative = decelerating)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    cagr3 = _safe_log(revenue).diff(DDAYS_3Y) / 3.0
    return yoy - cagr3


def f43_hdcl_005_revenue_yoy_minus_5y_cagr(revenue: pd.Series) -> pd.Series:
    """YoY growth minus 5y CAGR — recent vs long-run pace."""
    yoy = _safe_log(revenue).diff(YDAYS)
    cagr5 = _safe_log(revenue).diff(DDAYS_5Y) / 5.0
    return yoy - cagr5


def f43_hdcl_006_revenue_qoq_growth_log(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_63d_ago) — sequential quarterly growth."""
    return _safe_log(revenue).diff(QDAYS)


def f43_hdcl_007_revenue_qoq_2q_diff(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_126d_ago) — 2-quarter sequential change."""
    return _safe_log(revenue).diff(QDAYS * 2)


def f43_hdcl_008_revenue_growth_rate_change_1y(revenue: pd.Series) -> pd.Series:
    """Current YoY growth − YoY growth 252d ago — 1y change in growth RATE."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy - yoy.shift(YDAYS)


def f43_hdcl_009_revenue_growth_rate_change_2y(revenue: pd.Series) -> pd.Series:
    """Current YoY growth − YoY growth 504d ago — 2y change in growth rate."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy - yoy.shift(DDAYS_2Y)


def f43_hdcl_010_revenue_growth_rate_acceleration_4q(revenue: pd.Series) -> pd.Series:
    """Δ in QoQ growth across 4 quarters — sequential acceleration over a year."""
    qoq = _safe_log(revenue).diff(QDAYS)
    return qoq - qoq.shift(YDAYS)


def f43_hdcl_011_revenue_growth_volatility_8q(revenue: pd.Series) -> pd.Series:
    """Std of QoQ growth over trailing 8q — quarterly growth-rate wobble."""
    qoq = _safe_log(revenue).diff(QDAYS)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f43_hdcl_012_revenue_yoy_max_in_5y_minus_current(revenue: pd.Series) -> pd.Series:
    """5y-rolling max of YoY growth − current YoY — distance below 5y peak growth (>=0)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max() - yoy


def f43_hdcl_013_days_since_revenue_yoy_max_5y(revenue: pd.Series) -> pd.Series:
    """Bars since YoY growth touched its 5y rolling max — recency of peak-growth period."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _days_since_max(yoy, DDAYS_5Y)


def f43_hdcl_014_revenue_yoy_streak_above_30pct(revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of YoY > 0.30 log — sustained hypergrowth run."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.30).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y(revenue: pd.Series) -> pd.Series:
    """Days in last 5y where YoY > 0.30 / QDAYS ≈ count of hypergrowth quarters."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.30).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum() / QDAYS


def f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y(revenue: pd.Series) -> pd.Series:
    """Days in last 5y where YoY > 0.50 / QDAYS — extreme hypergrowth count."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.50).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum() / QDAYS


def f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q(revenue: pd.Series) -> pd.Series:
    """Current streak of bars where YoY < (YoY 63d ago) — sequential growth-rate decline."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < yoy.shift(QDAYS)).astype(int)
    return _streak_above_zero(flag, YDAYS)


def f43_hdcl_018_revenue_log_diff_3q(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_189d_ago) — 3-quarter cumulative growth."""
    return _safe_log(revenue).diff(QDAYS * 3)


def f43_hdcl_019_revenue_log_diff_6q(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_378d_ago) — 6-quarter cumulative growth."""
    return _safe_log(revenue).diff(QDAYS * 6)


def f43_hdcl_020_revenue_log_diff_8q(revenue: pd.Series) -> pd.Series:
    """log(revenue/revenue_504d_ago) — 8-quarter (2y) cumulative growth."""
    return _safe_log(revenue).diff(DDAYS_2Y)


def f43_hdcl_021_revenue_sequential_decline_indicator_2q(revenue: pd.Series) -> pd.Series:
    """1 if QoQ < 0 AND QoQ at 63d ago < 0 (two consecutive negative QoQ quarters)."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = ((qoq < 0) & (qoq.shift(QDAYS) < 0)).astype(float)
    return flag.where(qoq.notna() & qoq.shift(QDAYS).notna(), np.nan)


def f43_hdcl_022_revenue_yoy_below_long_mean_count_8q(revenue: pd.Series) -> pd.Series:
    """Bars in last 504d (8q) where YoY growth is below its 5y mean — sub-baseline persistence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m5y = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (yoy < m5y).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator(revenue: pd.Series) -> pd.Series:
    """1 if at any point in last 5y revenue YoY was in top decile of its 5y distribution."""
    yoy = _safe_log(revenue).diff(YDAYS)
    thr = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.9)
    flag = (yoy >= thr).astype(float)
    cnt = flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan)


def f43_hdcl_024_revenue_yoy_zscore_5y(revenue: pd.Series) -> pd.Series:
    """Z-score of current YoY growth vs its 5y distribution."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_zscore(yoy, DDAYS_5Y)


def f43_hdcl_025_revenue_yoy_rank_pct_5y(revenue: pd.Series) -> pd.Series:
    """Percentile rank of current YoY growth in trailing-5y distribution."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_rank_pct(yoy, DDAYS_5Y)


def f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log(revenue: pd.Series) -> pd.Series:
    """log(current YoY / max YoY in trailing 5y) — log-space drop from peak growth (≤0)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _safe_log_signed(yoy) - _safe_log_signed(yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max())


def f43_hdcl_027_revenue_yoy_vs_2y_avg_change(revenue: pd.Series) -> pd.Series:
    """Current YoY − rolling-2y mean of YoY — recent vs short-history baseline."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy - yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_028_revenue_qoq_minus_yoy_divergence(revenue: pd.Series) -> pd.Series:
    """4*QoQ growth − YoY — sequential pace gap (negative = sequential weakness)."""
    qoq = _safe_log(revenue).diff(QDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    return 4.0 * qoq - yoy


def f43_hdcl_029_revenue_growth_2nd_derivative_yoy(revenue: pd.Series) -> pd.Series:
    """Second 252d diff of log revenue — YoY-of-YoY acceleration."""
    return _safe_log(revenue).diff(YDAYS).diff(YDAYS)


def f43_hdcl_030_revenue_growth_2nd_derivative_qoq(revenue: pd.Series) -> pd.Series:
    """Second 63d diff of log revenue — QoQ-of-QoQ acceleration."""
    return _safe_log(revenue).diff(QDAYS).diff(QDAYS)


def f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q(revenue: pd.Series) -> pd.Series:
    """Mean over 8q of min(growth-rate Δ, 0) — pure decel intensity."""
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS).clip(upper=0.0)
    return accel.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_032_revenue_yoy_decline_speed_8q(revenue: pd.Series) -> pd.Series:
    """Regression slope of YoY growth over 8q (2y) — long-run trajectory of growth rate."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_2Y)


def f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore(revenue: pd.Series) -> pd.Series:
    """Z-score of [trailing-2y mean YoY − trailing-5y mean YoY] vs 5y distribution of itself."""
    yoy = _safe_log(revenue).diff(YDAYS)
    diff = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return _rolling_zscore(diff, DDAYS_5Y)


def f43_hdcl_034_revenue_yoy_below_p25_streak(revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of YoY below trailing-5y p25 — sub-baseline residence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    thr = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = (yoy < thr).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg(revenue: pd.Series) -> pd.Series:
    """4q log change − rolling-8q mean of 4q log change — short vs medium pace."""
    d4 = _safe_log(revenue).diff(YDAYS)
    return d4 - d4.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_036_revenue_growth_decel_3q_minus_1q(revenue: pd.Series) -> pd.Series:
    """(YoY now) − (YoY 189d ago) — 3-quarter window growth change."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy - yoy.shift(QDAYS * 3)


def f43_hdcl_037_revenue_growth_dispersion_8q(revenue: pd.Series) -> pd.Series:
    """(p75 − p25) of QoQ growth over 8q — dispersion of sequential growth."""
    qoq = _safe_log(revenue).diff(QDAYS)
    p75 = qoq.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    p25 = qoq.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    return p75 - p25


def f43_hdcl_038_revenue_growth_kurtosis_8q(revenue: pd.Series) -> pd.Series:
    """Excess kurtosis of QoQ growth over 8q — fat-tailed growth regime."""
    qoq = _safe_log(revenue).diff(QDAYS)
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_k, raw=True)


def f43_hdcl_039_revenue_growth_skewness_8q(revenue: pd.Series) -> pd.Series:
    """Skewness of QoQ growth over 8q — negative skew = sudden-drop-prone regime."""
    qoq = _safe_log(revenue).diff(QDAYS)
    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / (sd ** 3))
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sk, raw=True)


def f43_hdcl_040_revenue_yoy_change_acceleration(revenue: pd.Series) -> pd.Series:
    """Second 252d diff of YoY growth rate — change-of-change-of-growth."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.diff(YDAYS).diff(YDAYS)


def f43_hdcl_041_revenue_yoy_4q_window_min(revenue: pd.Series) -> pd.Series:
    """Min YoY growth over trailing 4q (252d) — worst-1y growth-rate reading."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(YDAYS, min_periods=QDAYS).min()


def f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now(revenue: pd.Series) -> pd.Series:
    """Rolling-4q mean YoY − current YoY — if positive, recent is below the 4q average."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(YDAYS, min_periods=QDAYS).mean() - yoy


def f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now(revenue: pd.Series) -> pd.Series:
    """Rolling-2q mean YoY − current YoY — short-window relative deceleration."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(QDAYS * 2, min_periods=QDAYS).mean() - yoy


def f43_hdcl_044_revenue_yoy_negative_count_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q with YoY < 0 — outright revenue decline persistence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_045_revenue_max_2q_drawdown_intensity(revenue: pd.Series) -> pd.Series:
    """Min of (YoY now − YoY 126d ago) over 5y — worst 2q drop in growth rate."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy - yoy.shift(QDAYS * 2)
    return drop.rolling(DDAYS_5Y, min_periods=YDAYS).min()


def f43_hdcl_046_gp_yoy_growth_log(gp: pd.Series) -> pd.Series:
    """log(gp/gp_252d_ago) — gross-profit YoY growth."""
    return _safe_log(gp).diff(YDAYS)


def f43_hdcl_047_opinc_yoy_growth_log(opinc: pd.Series) -> pd.Series:
    """log(opinc/opinc_252d_ago) — operating-income YoY growth (signed-log handles negatives)."""
    return _safe_log_signed(opinc).diff(YDAYS)


def f43_hdcl_048_ebitda_yoy_growth_log(ebitda: pd.Series) -> pd.Series:
    """EBITDA YoY signed-log growth."""
    return _safe_log_signed(ebitda).diff(YDAYS)


def f43_hdcl_049_netinc_yoy_growth_log(netinc: pd.Series) -> pd.Series:
    """Net income YoY signed-log growth."""
    return _safe_log_signed(netinc).diff(YDAYS)


def f43_hdcl_050_fcf_yoy_change_signed_log(fcf: pd.Series) -> pd.Series:
    """FCF YoY signed-log change — handles negative FCF without NaN."""
    return _safe_log_signed(fcf).diff(YDAYS)


def f43_hdcl_051_revenue_yoy_minus_gp_yoy(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Revenue YoY − GP YoY — positive = gross-margin pressure (cost rising faster than revenue)."""
    return _safe_log(revenue).diff(YDAYS) - _safe_log(gp).diff(YDAYS)


def f43_hdcl_052_revenue_yoy_minus_opinc_yoy(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Revenue YoY − operating-income YoY — operating-leverage breakdown when positive."""
    return _safe_log(revenue).diff(YDAYS) - _safe_log_signed(opinc).diff(YDAYS)


def f43_hdcl_053_revenue_yoy_minus_ebitda_yoy(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Revenue YoY − EBITDA YoY — EBITDA-margin compression when positive."""
    return _safe_log(revenue).diff(YDAYS) - _safe_log_signed(ebitda).diff(YDAYS)


def f43_hdcl_054_revenue_yoy_minus_netinc_yoy(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Revenue YoY − net-income YoY — bottom-line leverage breakdown."""
    return _safe_log(revenue).diff(YDAYS) - _safe_log_signed(netinc).diff(YDAYS)


def f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series) -> pd.Series:
    """Bars in trailing 8q where YoY of all THREE (revenue, gp, opinc) is below their respective 5y means."""
    r_yoy = _safe_log(revenue).diff(YDAYS)
    g_yoy = _safe_log(gp).diff(YDAYS)
    o_yoy = _safe_log_signed(opinc).diff(YDAYS)
    rm = r_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    gm = g_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    om = o_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((r_yoy < rm) & (g_yoy < gm) & (o_yoy < om)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Bars in trailing 8q where YoY of revenue, opinc, and fcf are all below their respective 5y means."""
    r_yoy = _safe_log(revenue).diff(YDAYS)
    o_yoy = _safe_log_signed(opinc).diff(YDAYS)
    f_yoy = _safe_log_signed(fcf).diff(YDAYS)
    rm = r_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    om = o_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    fm = f_yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((r_yoy < rm) & (o_yoy < om) & (f_yoy < fm)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_057_gp_growth_below_revenue_growth_streak(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where GP YoY < revenue YoY — gross-margin pressure persistence."""
    flag = (_safe_log(gp).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_058_opinc_growth_below_revenue_growth_streak(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where opinc YoY < revenue YoY — operating leverage breakdown."""
    flag = (_safe_log_signed(opinc).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_059_netinc_growth_below_revenue_growth_streak(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where netinc YoY < revenue YoY — bottom-line leverage breakdown."""
    flag = (_safe_log_signed(netinc).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_060_fcf_growth_below_revenue_growth_streak(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where FCF YoY < revenue YoY — cash-leverage breakdown."""
    flag = (_safe_log_signed(fcf).diff(YDAYS) < _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_061_metric_decel_breadth_4q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Count of metrics (rev,gp,opinc,ebitda,netinc,fcf) whose 4q-trailing-mean YoY is below 5y mean — breadth of decel."""
    series_list = [
        _safe_log(revenue).diff(YDAYS),
        _safe_log(gp).diff(YDAYS),
        _safe_log_signed(opinc).diff(YDAYS),
        _safe_log_signed(ebitda).diff(YDAYS),
        _safe_log_signed(netinc).diff(YDAYS),
        _safe_log_signed(fcf).diff(YDAYS),
    ]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m_4q = s.rolling(YDAYS, min_periods=QDAYS).mean()
        m_5y = s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
        total = total + (m_4q < m_5y).astype(float)
        valid = valid & m_4q.notna() & m_5y.notna()
    return total.where(valid, np.nan)


def f43_hdcl_062_metric_decel_breadth_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Count of metrics whose 8q-trailing-mean YoY is below 5y mean — 8q breadth of decel."""
    series_list = [
        _safe_log(revenue).diff(YDAYS),
        _safe_log(gp).diff(YDAYS),
        _safe_log_signed(opinc).diff(YDAYS),
        _safe_log_signed(ebitda).diff(YDAYS),
        _safe_log_signed(netinc).diff(YDAYS),
        _safe_log_signed(fcf).diff(YDAYS),
    ]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        m_8q = s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
        m_5y = s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
        total = total + (m_8q < m_5y).astype(float)
        valid = valid & m_8q.notna() & m_5y.notna()
    return total.where(valid, np.nan)


def f43_hdcl_063_compound_yoy_decel_acceleration(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Average of (YoY-of-YoY) accelerations for revenue, opinc, fcf — composite acceleration of growth."""
    r = _safe_log(revenue).diff(YDAYS).diff(YDAYS)
    o = _safe_log_signed(opinc).diff(YDAYS).diff(YDAYS)
    f = _safe_log_signed(fcf).diff(YDAYS).diff(YDAYS)
    return (r + o + f) / 3.0


def f43_hdcl_064_yoy_growth_compound_zscore_252d(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean of z-scores (vs 5y) of revenue/opinc/fcf YoY — composite growth z-position."""
    z_r = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    z_o = _rolling_zscore(_safe_log_signed(opinc).diff(YDAYS), DDAYS_5Y)
    z_f = _rolling_zscore(_safe_log_signed(fcf).diff(YDAYS), DDAYS_5Y)
    return (z_r + z_o + z_f) / 3.0


def f43_hdcl_065_ebitda_yoy_decline_streak(ebitda: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where EBITDA YoY < 0 — outright EBITDA decline persistence."""
    flag = (_safe_log_signed(ebitda).diff(YDAYS) < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_066_netinc_yoy_decline_streak(netinc: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where netinc YoY < 0 — net-income decline persistence."""
    flag = (_safe_log_signed(netinc).diff(YDAYS) < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_067_opinc_yoy_change_rate(opinc: pd.Series) -> pd.Series:
    """Current opinc YoY − opinc YoY 252d ago — 1y change in operating-income growth rate."""
    yoy = _safe_log_signed(opinc).diff(YDAYS)
    return yoy - yoy.shift(YDAYS)


def f43_hdcl_068_fcf_yoy_change_acceleration(fcf: pd.Series) -> pd.Series:
    """Second 252d diff of signed-log FCF — change-of-change of FCF YoY."""
    return _safe_log_signed(fcf).diff(YDAYS).diff(YDAYS)


def f43_hdcl_069_revenue_to_netinc_growth_gap_zscore(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Z-score (vs 5y) of (revenue YoY − netinc YoY) — bottom-line leverage gap extremity."""
    gap = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(netinc).diff(YDAYS)
    return _rolling_zscore(gap, DDAYS_5Y)


def f43_hdcl_070_revenue_to_fcf_growth_gap_zscore(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Z-score (vs 5y) of (revenue YoY − fcf YoY) — cash-leverage gap extremity."""
    gap = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(fcf).diff(YDAYS)
    return _rolling_zscore(gap, DDAYS_5Y)


def f43_hdcl_071_sustained_hypergrowth_indicator_5y(revenue: pd.Series) -> pd.Series:
    """1 if at least 8 quarters worth of bars in last 5y had YoY > 0.30 (sustained hypergrowth history)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.30).astype(float)
    cnt = flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return (cnt >= 8 * QDAYS).astype(float).where(cnt.notna(), np.nan)


def f43_hdcl_072_sustained_hypergrowth_indicator_3y(revenue: pd.Series) -> pd.Series:
    """1 if at least 6 quarters worth of bars in last 3y had YoY > 0.30."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0.30).astype(float)
    cnt = flag.rolling(DDAYS_3Y, min_periods=YDAYS).sum()
    return (cnt >= 6 * QDAYS).astype(float).where(cnt.notna(), np.nan)


def f43_hdcl_073_quarters_above_hypergrowth_then_below_count(revenue: pd.Series) -> pd.Series:
    """Bars in last 5y where YoY ≤ 0.10 AND prior (YoY 252d ago) > 0.30 — transition events."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy <= 0.10) & (yoy.shift(YDAYS) > 0.30)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f43_hdcl_074_transition_from_hypergrowth_to_normal_recency(revenue: pd.Series) -> pd.Series:
    """Bars since the last hypergrowth → normal transition event within 5y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy <= 0.10) & (yoy.shift(YDAYS) > 0.30)).astype(float)
    return _recency_since_event(flag, DDAYS_5Y)


def f43_hdcl_075_hypergrowth_peak_to_current_drop_pct(revenue: pd.Series) -> pd.Series:
    """(max-5y YoY − current YoY) / max-5y YoY — fraction drop from peak hypergrowth (clipped ≥0)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_div(mx - yoy, mx)


# ============================================================
#                        REGISTRY
# ============================================================

HYPERGROWTH_DECELERATION_CLIFF_BASE_REGISTRY_001_075 = {
    "f43_hdcl_001_revenue_yoy_growth_log": {"inputs": ["revenue"], "func": f43_hdcl_001_revenue_yoy_growth_log},
    "f43_hdcl_002_revenue_3y_cagr_log": {"inputs": ["revenue"], "func": f43_hdcl_002_revenue_3y_cagr_log},
    "f43_hdcl_003_revenue_5y_cagr_log": {"inputs": ["revenue"], "func": f43_hdcl_003_revenue_5y_cagr_log},
    "f43_hdcl_004_revenue_yoy_minus_3y_cagr": {"inputs": ["revenue"], "func": f43_hdcl_004_revenue_yoy_minus_3y_cagr},
    "f43_hdcl_005_revenue_yoy_minus_5y_cagr": {"inputs": ["revenue"], "func": f43_hdcl_005_revenue_yoy_minus_5y_cagr},
    "f43_hdcl_006_revenue_qoq_growth_log": {"inputs": ["revenue"], "func": f43_hdcl_006_revenue_qoq_growth_log},
    "f43_hdcl_007_revenue_qoq_2q_diff": {"inputs": ["revenue"], "func": f43_hdcl_007_revenue_qoq_2q_diff},
    "f43_hdcl_008_revenue_growth_rate_change_1y": {"inputs": ["revenue"], "func": f43_hdcl_008_revenue_growth_rate_change_1y},
    "f43_hdcl_009_revenue_growth_rate_change_2y": {"inputs": ["revenue"], "func": f43_hdcl_009_revenue_growth_rate_change_2y},
    "f43_hdcl_010_revenue_growth_rate_acceleration_4q": {"inputs": ["revenue"], "func": f43_hdcl_010_revenue_growth_rate_acceleration_4q},
    "f43_hdcl_011_revenue_growth_volatility_8q": {"inputs": ["revenue"], "func": f43_hdcl_011_revenue_growth_volatility_8q},
    "f43_hdcl_012_revenue_yoy_max_in_5y_minus_current": {"inputs": ["revenue"], "func": f43_hdcl_012_revenue_yoy_max_in_5y_minus_current},
    "f43_hdcl_013_days_since_revenue_yoy_max_5y": {"inputs": ["revenue"], "func": f43_hdcl_013_days_since_revenue_yoy_max_5y},
    "f43_hdcl_014_revenue_yoy_streak_above_30pct": {"inputs": ["revenue"], "func": f43_hdcl_014_revenue_yoy_streak_above_30pct},
    "f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y": {"inputs": ["revenue"], "func": f43_hdcl_015_quarters_with_revenue_yoy_above_30pct_count_5y},
    "f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y": {"inputs": ["revenue"], "func": f43_hdcl_016_quarters_with_revenue_yoy_above_50pct_count_5y},
    "f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q": {"inputs": ["revenue"], "func": f43_hdcl_017_revenue_yoy_consecutive_decline_count_4q},
    "f43_hdcl_018_revenue_log_diff_3q": {"inputs": ["revenue"], "func": f43_hdcl_018_revenue_log_diff_3q},
    "f43_hdcl_019_revenue_log_diff_6q": {"inputs": ["revenue"], "func": f43_hdcl_019_revenue_log_diff_6q},
    "f43_hdcl_020_revenue_log_diff_8q": {"inputs": ["revenue"], "func": f43_hdcl_020_revenue_log_diff_8q},
    "f43_hdcl_021_revenue_sequential_decline_indicator_2q": {"inputs": ["revenue"], "func": f43_hdcl_021_revenue_sequential_decline_indicator_2q},
    "f43_hdcl_022_revenue_yoy_below_long_mean_count_8q": {"inputs": ["revenue"], "func": f43_hdcl_022_revenue_yoy_below_long_mean_count_8q},
    "f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator": {"inputs": ["revenue"], "func": f43_hdcl_023_revenue_top_decile_growth_in_5y_indicator},
    "f43_hdcl_024_revenue_yoy_zscore_5y": {"inputs": ["revenue"], "func": f43_hdcl_024_revenue_yoy_zscore_5y},
    "f43_hdcl_025_revenue_yoy_rank_pct_5y": {"inputs": ["revenue"], "func": f43_hdcl_025_revenue_yoy_rank_pct_5y},
    "f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log": {"inputs": ["revenue"], "func": f43_hdcl_026_revenue_yoy_minus_peak_yoy_5y_log},
    "f43_hdcl_027_revenue_yoy_vs_2y_avg_change": {"inputs": ["revenue"], "func": f43_hdcl_027_revenue_yoy_vs_2y_avg_change},
    "f43_hdcl_028_revenue_qoq_minus_yoy_divergence": {"inputs": ["revenue"], "func": f43_hdcl_028_revenue_qoq_minus_yoy_divergence},
    "f43_hdcl_029_revenue_growth_2nd_derivative_yoy": {"inputs": ["revenue"], "func": f43_hdcl_029_revenue_growth_2nd_derivative_yoy},
    "f43_hdcl_030_revenue_growth_2nd_derivative_qoq": {"inputs": ["revenue"], "func": f43_hdcl_030_revenue_growth_2nd_derivative_qoq},
    "f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q": {"inputs": ["revenue"], "func": f43_hdcl_031_revenue_growth_acceleration_negative_intensity_8q},
    "f43_hdcl_032_revenue_yoy_decline_speed_8q": {"inputs": ["revenue"], "func": f43_hdcl_032_revenue_yoy_decline_speed_8q},
    "f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore": {"inputs": ["revenue"], "func": f43_hdcl_033_revenue_growth_2y_vs_5y_baseline_zscore},
    "f43_hdcl_034_revenue_yoy_below_p25_streak": {"inputs": ["revenue"], "func": f43_hdcl_034_revenue_yoy_below_p25_streak},
    "f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg": {"inputs": ["revenue"], "func": f43_hdcl_035_revenue_log_diff_4q_minus_8q_avg},
    "f43_hdcl_036_revenue_growth_decel_3q_minus_1q": {"inputs": ["revenue"], "func": f43_hdcl_036_revenue_growth_decel_3q_minus_1q},
    "f43_hdcl_037_revenue_growth_dispersion_8q": {"inputs": ["revenue"], "func": f43_hdcl_037_revenue_growth_dispersion_8q},
    "f43_hdcl_038_revenue_growth_kurtosis_8q": {"inputs": ["revenue"], "func": f43_hdcl_038_revenue_growth_kurtosis_8q},
    "f43_hdcl_039_revenue_growth_skewness_8q": {"inputs": ["revenue"], "func": f43_hdcl_039_revenue_growth_skewness_8q},
    "f43_hdcl_040_revenue_yoy_change_acceleration": {"inputs": ["revenue"], "func": f43_hdcl_040_revenue_yoy_change_acceleration},
    "f43_hdcl_041_revenue_yoy_4q_window_min": {"inputs": ["revenue"], "func": f43_hdcl_041_revenue_yoy_4q_window_min},
    "f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now": {"inputs": ["revenue"], "func": f43_hdcl_042_revenue_yoy_4q_avg_minus_yoy_now},
    "f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now": {"inputs": ["revenue"], "func": f43_hdcl_043_revenue_yoy_2q_avg_minus_yoy_now},
    "f43_hdcl_044_revenue_yoy_negative_count_8q": {"inputs": ["revenue"], "func": f43_hdcl_044_revenue_yoy_negative_count_8q},
    "f43_hdcl_045_revenue_max_2q_drawdown_intensity": {"inputs": ["revenue"], "func": f43_hdcl_045_revenue_max_2q_drawdown_intensity},
    "f43_hdcl_046_gp_yoy_growth_log": {"inputs": ["gp"], "func": f43_hdcl_046_gp_yoy_growth_log},
    "f43_hdcl_047_opinc_yoy_growth_log": {"inputs": ["opinc"], "func": f43_hdcl_047_opinc_yoy_growth_log},
    "f43_hdcl_048_ebitda_yoy_growth_log": {"inputs": ["ebitda"], "func": f43_hdcl_048_ebitda_yoy_growth_log},
    "f43_hdcl_049_netinc_yoy_growth_log": {"inputs": ["netinc"], "func": f43_hdcl_049_netinc_yoy_growth_log},
    "f43_hdcl_050_fcf_yoy_change_signed_log": {"inputs": ["fcf"], "func": f43_hdcl_050_fcf_yoy_change_signed_log},
    "f43_hdcl_051_revenue_yoy_minus_gp_yoy": {"inputs": ["revenue", "gp"], "func": f43_hdcl_051_revenue_yoy_minus_gp_yoy},
    "f43_hdcl_052_revenue_yoy_minus_opinc_yoy": {"inputs": ["revenue", "opinc"], "func": f43_hdcl_052_revenue_yoy_minus_opinc_yoy},
    "f43_hdcl_053_revenue_yoy_minus_ebitda_yoy": {"inputs": ["revenue", "ebitda"], "func": f43_hdcl_053_revenue_yoy_minus_ebitda_yoy},
    "f43_hdcl_054_revenue_yoy_minus_netinc_yoy": {"inputs": ["revenue", "netinc"], "func": f43_hdcl_054_revenue_yoy_minus_netinc_yoy},
    "f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q": {"inputs": ["revenue", "gp", "opinc"], "func": f43_hdcl_055_compound_deceleration_revenue_gp_opinc_count_8q},
    "f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_056_compound_deceleration_revenue_opinc_fcf_count_8q},
    "f43_hdcl_057_gp_growth_below_revenue_growth_streak": {"inputs": ["revenue", "gp"], "func": f43_hdcl_057_gp_growth_below_revenue_growth_streak},
    "f43_hdcl_058_opinc_growth_below_revenue_growth_streak": {"inputs": ["revenue", "opinc"], "func": f43_hdcl_058_opinc_growth_below_revenue_growth_streak},
    "f43_hdcl_059_netinc_growth_below_revenue_growth_streak": {"inputs": ["revenue", "netinc"], "func": f43_hdcl_059_netinc_growth_below_revenue_growth_streak},
    "f43_hdcl_060_fcf_growth_below_revenue_growth_streak": {"inputs": ["revenue", "fcf"], "func": f43_hdcl_060_fcf_growth_below_revenue_growth_streak},
    "f43_hdcl_061_metric_decel_breadth_4q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc", "fcf"], "func": f43_hdcl_061_metric_decel_breadth_4q},
    "f43_hdcl_062_metric_decel_breadth_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc", "fcf"], "func": f43_hdcl_062_metric_decel_breadth_8q},
    "f43_hdcl_063_compound_yoy_decel_acceleration": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_063_compound_yoy_decel_acceleration},
    "f43_hdcl_064_yoy_growth_compound_zscore_252d": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_064_yoy_growth_compound_zscore_252d},
    "f43_hdcl_065_ebitda_yoy_decline_streak": {"inputs": ["ebitda"], "func": f43_hdcl_065_ebitda_yoy_decline_streak},
    "f43_hdcl_066_netinc_yoy_decline_streak": {"inputs": ["netinc"], "func": f43_hdcl_066_netinc_yoy_decline_streak},
    "f43_hdcl_067_opinc_yoy_change_rate": {"inputs": ["opinc"], "func": f43_hdcl_067_opinc_yoy_change_rate},
    "f43_hdcl_068_fcf_yoy_change_acceleration": {"inputs": ["fcf"], "func": f43_hdcl_068_fcf_yoy_change_acceleration},
    "f43_hdcl_069_revenue_to_netinc_growth_gap_zscore": {"inputs": ["revenue", "netinc"], "func": f43_hdcl_069_revenue_to_netinc_growth_gap_zscore},
    "f43_hdcl_070_revenue_to_fcf_growth_gap_zscore": {"inputs": ["revenue", "fcf"], "func": f43_hdcl_070_revenue_to_fcf_growth_gap_zscore},
    "f43_hdcl_071_sustained_hypergrowth_indicator_5y": {"inputs": ["revenue"], "func": f43_hdcl_071_sustained_hypergrowth_indicator_5y},
    "f43_hdcl_072_sustained_hypergrowth_indicator_3y": {"inputs": ["revenue"], "func": f43_hdcl_072_sustained_hypergrowth_indicator_3y},
    "f43_hdcl_073_quarters_above_hypergrowth_then_below_count": {"inputs": ["revenue"], "func": f43_hdcl_073_quarters_above_hypergrowth_then_below_count},
    "f43_hdcl_074_transition_from_hypergrowth_to_normal_recency": {"inputs": ["revenue"], "func": f43_hdcl_074_transition_from_hypergrowth_to_normal_recency},
    "f43_hdcl_075_hypergrowth_peak_to_current_drop_pct": {"inputs": ["revenue"], "func": f43_hdcl_075_hypergrowth_peak_to_current_drop_pct},
}
