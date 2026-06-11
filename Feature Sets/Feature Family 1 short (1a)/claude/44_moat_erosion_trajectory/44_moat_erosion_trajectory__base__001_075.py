"""moat_erosion_trajectory base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: slow grinding decay of competitive advantage at the peak — gross
and operating margin compression, return-on-capital deterioration, asset
turnover slowdown, pricing-power loss. Long-horizon (3y, 5y) emphasis
since moat erosion is a multi-year phenomenon. Continued in __base__076_150.py
for 150 total. Inputs: SF1 ARQ columns forward-filled to daily. PIT-clean.
"""
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


def _rolling_slope_r2(s, n, min_periods=None):
    """Rolling R^2 of a linear fit of s vs time over window n."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _r2(w):
        if np.isnan(w).any():
            valid = ~np.isnan(w)
            if valid.sum() < min_periods:
                return np.nan
            xv = np.arange(len(w))[valid].astype(float)
            wv = w[valid]
        else:
            xv = np.arange(len(w)).astype(float)
            wv = w
        xm = xv.mean(); wm = wv.mean()
        sxx = ((xv - xm) ** 2).sum()
        swy = ((wv - wm) ** 2).sum()
        sxy = ((xv - xm) * (wv - wm)).sum()
        if sxx == 0 or swy == 0:
            return np.nan
        return float((sxy ** 2) / (sxx * swy))
    return s.rolling(n, min_periods=min_periods).apply(_r2, raw=True)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f44_mert_001_gp_margin_level(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin = gp / revenue — raw gross-margin level."""
    return _safe_div(gp, revenue)


def f44_mert_002_gp_margin_change_yoy(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y change in gross margin — annual margin shift."""
    return _safe_div(gp, revenue).diff(YDAYS)


def f44_mert_003_gp_margin_change_2y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y change in gross margin."""
    return _safe_div(gp, revenue).diff(DDAYS_2Y)


def f44_mert_004_gp_margin_change_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in gross margin — long-horizon moat decay signal."""
    return _safe_div(gp, revenue).diff(DDAYS_5Y)


def f44_mert_005_gp_margin_zscore_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of current gross margin vs 5y distribution."""
    return _rolling_zscore(_safe_div(gp, revenue), DDAYS_5Y)


def f44_mert_006_gp_margin_rank_pct_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin in trailing 5y."""
    return _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y)


def f44_mert_007_gp_margin_log_distance_to_5y_max(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """log(current gm / 5y max gm) — distance below 5y peak (≤0)."""
    gm = _safe_div(gp, revenue)
    mx = gm.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_log(gm) - _safe_log(mx)


def f44_mert_008_days_since_gp_margin_max_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars since gross margin hit its 5y rolling max — moat-peak recency."""
    return _days_since_max(_safe_div(gp, revenue), DDAYS_5Y)


def f44_mert_009_gp_margin_decline_streak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where gross margin < its trailing-1y mean."""
    gm = _safe_div(gp, revenue)
    m = gm.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (gm < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_010_gp_margin_negative_diff_count_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q with quarterly Δ gross margin < 0 — compression-quarters count."""
    flag = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f44_mert_011_gp_margin_negative_diff_count_20q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 20q (5y) with quarterly Δ gross margin < 0."""
    flag = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f44_mert_012_gp_margin_acceleration_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second 252d diff of gross margin — change in compression rate."""
    return _safe_div(gp, revenue).diff(YDAYS).diff(YDAYS)


def f44_mert_013_gp_margin_volatility_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Std of quarterly Δ gross margin over trailing 8q — margin-trajectory wobble."""
    return _safe_div(gp, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f44_mert_014_gp_margin_volatility_zscore_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score (vs 5y) of the 8q-rolling vol of gross-margin Δ."""
    v = _safe_div(gp, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _rolling_zscore(v, DDAYS_5Y)


def f44_mert_015_gp_margin_below_5y_mean_streak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where gross margin < its trailing-5y mean."""
    gm = _safe_div(gp, revenue)
    m = gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (gm < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_016_gp_margin_2y_minus_5y_baseline(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y mean gross margin − 5y mean gross margin — recent-vs-long baseline shift."""
    gm = _safe_div(gp, revenue)
    return gm.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f44_mert_017_gp_margin_smoothed_ema_thrust(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """EMA(63d) gm − EMA(252d) gm — smoothed short-vs-long margin gap."""
    gm = _safe_div(gp, revenue)
    return _ema(gm, QDAYS) - _ema(gm, YDAYS)


def f44_mert_018_gp_margin_below_p25_count_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 5y with gross margin below trailing-5y p25 — bottom-quartile residence."""
    gm = _safe_div(gp, revenue)
    thr = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = (gm < thr).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f44_mert_019_gp_margin_compression_rate_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Regression slope of gross margin on time over trailing 5y — long-horizon compression rate."""
    return _rolling_slope(_safe_div(gp, revenue), DDAYS_5Y)


def f44_mert_020_gp_margin_compression_r2_5y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """R^2 of 5y linear fit of gross margin on time — confidence of compression trend."""
    return _rolling_slope_r2(_safe_div(gp, revenue), DDAYS_5Y)


def f44_mert_021_opinc_margin_level(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin = opinc / revenue — raw operating-margin level."""
    return _safe_div(opinc, revenue)


def f44_mert_022_opinc_margin_change_yoy(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y change in operating margin."""
    return _safe_div(opinc, revenue).diff(YDAYS)


def f44_mert_023_opinc_margin_change_2y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y change in operating margin."""
    return _safe_div(opinc, revenue).diff(DDAYS_2Y)


def f44_mert_024_opinc_margin_change_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in operating margin — long-horizon profitability decay."""
    return _safe_div(opinc, revenue).diff(DDAYS_5Y)


def f44_mert_025_opinc_margin_zscore_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating margin vs 5y."""
    return _rolling_zscore(_safe_div(opinc, revenue), DDAYS_5Y)


def f44_mert_026_opinc_margin_rank_pct_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of operating margin vs 5y."""
    return _rolling_rank_pct(_safe_div(opinc, revenue), DDAYS_5Y)


def f44_mert_027_opinc_margin_log_distance_to_5y_max(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """log(current op margin / 5y max op margin) using signed-log for negative margins."""
    om = _safe_div(opinc, revenue)
    mx = om.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_log_signed(om) - _safe_log_signed(mx)


def f44_mert_028_days_since_opinc_margin_max_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars since op-margin hit 5y max."""
    return _days_since_max(_safe_div(opinc, revenue), DDAYS_5Y)


def f44_mert_029_opinc_margin_decline_streak(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where op margin < its trailing-1y mean."""
    om = _safe_div(opinc, revenue)
    m = om.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (om < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_030_opinc_margin_acceleration_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second 252d diff of op margin — change in compression rate."""
    return _safe_div(opinc, revenue).diff(YDAYS).diff(YDAYS)


def f44_mert_031_opinc_margin_volatility_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Std of quarterly Δ op margin over trailing 8q."""
    return _safe_div(opinc, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f44_mert_032_opinc_margin_below_5y_mean_streak(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current streak where op margin < trailing-5y mean."""
    om = _safe_div(opinc, revenue)
    m = om.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (om < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_033_opinc_margin_2y_minus_5y_baseline(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y mean op margin − 5y mean op margin."""
    om = _safe_div(opinc, revenue)
    return om.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - om.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f44_mert_034_opinc_margin_compression_rate_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y regression slope of op margin on time."""
    return _rolling_slope(_safe_div(opinc, revenue), DDAYS_5Y)


def f44_mert_035_opinc_margin_compression_r2_5y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y R^2 of op-margin linear fit — compression-trend confidence."""
    return _rolling_slope_r2(_safe_div(opinc, revenue), DDAYS_5Y)


def f44_mert_036_ebitda_margin_level(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin = ebitda / revenue."""
    return _safe_div(ebitda, revenue)


def f44_mert_037_ebitda_margin_change_5y(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in EBITDA margin."""
    return _safe_div(ebitda, revenue).diff(DDAYS_5Y)


def f44_mert_038_ebitda_margin_zscore_5y(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of EBITDA margin vs 5y."""
    return _rolling_zscore(_safe_div(ebitda, revenue), DDAYS_5Y)


def f44_mert_039_ebitda_margin_log_distance_to_5y_max(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """log(current EBITDA margin / 5y max EBITDA margin), signed-log."""
    em = _safe_div(ebitda, revenue)
    mx = em.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_log_signed(em) - _safe_log_signed(mx)


def f44_mert_040_ebitda_margin_compression_rate_5y(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y regression slope of EBITDA margin on time."""
    return _rolling_slope(_safe_div(ebitda, revenue), DDAYS_5Y)


def f44_mert_041_roic_proxy_level(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """ROIC proxy = opinc / (debt + equity) — return on invested capital."""
    return _safe_div(opinc, debt + equity)


def f44_mert_042_roic_change_yoy(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1y change in ROIC proxy."""
    return _safe_div(opinc, debt + equity).diff(YDAYS)


def f44_mert_043_roic_change_5y(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """5y change in ROIC proxy — long-horizon return-on-capital decay."""
    return _safe_div(opinc, debt + equity).diff(DDAYS_5Y)


def f44_mert_044_roic_zscore_5y(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of ROIC vs 5y distribution."""
    return _rolling_zscore(_safe_div(opinc, debt + equity), DDAYS_5Y)


def f44_mert_045_roic_decline_streak(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Current streak where ROIC < trailing-1y mean."""
    r = _safe_div(opinc, debt + equity)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_046_roic_compression_rate_5y(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """5y regression slope of ROIC on time."""
    return _rolling_slope(_safe_div(opinc, debt + equity), DDAYS_5Y)


def f44_mert_047_roe_level(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """ROE = netinc / equity."""
    return _safe_div(netinc, equity)


def f44_mert_048_roe_change_yoy(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """1y change in ROE."""
    return _safe_div(netinc, equity).diff(YDAYS)


def f44_mert_049_roe_change_5y(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """5y change in ROE."""
    return _safe_div(netinc, equity).diff(DDAYS_5Y)


def f44_mert_050_roe_zscore_5y(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of ROE vs 5y."""
    return _rolling_zscore(_safe_div(netinc, equity), DDAYS_5Y)


def f44_mert_051_roe_decline_streak(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """Current streak where ROE < trailing-1y mean."""
    r = _safe_div(netinc, equity)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_052_roa_level(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """ROA = netinc / assets."""
    return _safe_div(netinc, assets)


def f44_mert_053_roa_change_yoy(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """1y change in ROA."""
    return _safe_div(netinc, assets).diff(YDAYS)


def f44_mert_054_roa_change_5y(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """5y change in ROA."""
    return _safe_div(netinc, assets).diff(DDAYS_5Y)


def f44_mert_055_roa_zscore_5y(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of ROA vs 5y."""
    return _rolling_zscore(_safe_div(netinc, assets), DDAYS_5Y)


def f44_mert_056_roa_decline_streak(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current streak where ROA < trailing-1y mean."""
    r = _safe_div(netinc, assets)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_057_return_metrics_compound_decel_count_5y(opinc: pd.Series, netinc: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """Bars in trailing 5y where ROIC + ROE + ROA are ALL below their trailing-5y means."""
    roic = _safe_div(opinc, debt + equity)
    roe = _safe_div(netinc, equity)
    roa = _safe_div(netinc, assets)
    m_roic = roic.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    m_roe = roe.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    m_roa = roa.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((roic < m_roic) & (roe < m_roe) & (roa < m_roa)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f44_mert_058_roic_below_long_mean_streak(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Current streak where ROIC < its trailing-5y mean — sustained sub-baseline."""
    r = _safe_div(opinc, debt + equity)
    m = r.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_059_roic_minus_2y_baseline(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """ROIC − 2y rolling mean of ROIC — current vs short-history baseline."""
    r = _safe_div(opinc, debt + equity)
    return r - r.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f44_mert_060_roic_consecutive_decline_count_8q(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Bars in trailing 8q where ROIC < ROIC 63d ago — quarter-on-quarter decline count."""
    r = _safe_div(opinc, debt + equity)
    flag = (r < r.shift(QDAYS)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f44_mert_061_revenue_per_assets_level(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Asset turnover = revenue / assets."""
    return _safe_div(revenue, assets)


def f44_mert_062_revenue_per_assets_change_yoy(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """1y change in asset turnover."""
    return _safe_div(revenue, assets).diff(YDAYS)


def f44_mert_063_revenue_per_assets_change_5y(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """5y change in asset turnover — long-horizon efficiency decay."""
    return _safe_div(revenue, assets).diff(DDAYS_5Y)


def f44_mert_064_revenue_per_assets_zscore_5y(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of asset turnover vs 5y."""
    return _rolling_zscore(_safe_div(revenue, assets), DDAYS_5Y)


def f44_mert_065_revenue_per_assets_decline_streak(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Current streak where asset turnover < trailing-1y mean."""
    t = _safe_div(revenue, assets)
    m = t.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (t < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_066_revenue_per_assets_compression_rate_5y(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """5y regression slope of asset turnover on time."""
    return _rolling_slope(_safe_div(revenue, assets), DDAYS_5Y)


def f44_mert_067_revenue_per_ppe_level(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    """Revenue / net PP&E — capital-asset utilization."""
    return _safe_div(revenue, ppnetbasis)


def f44_mert_068_revenue_per_ppe_change_5y(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    """5y change in revenue/PP&E."""
    return _safe_div(revenue, ppnetbasis).diff(DDAYS_5Y)


def f44_mert_069_revenue_per_ppe_zscore_5y(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    """Z-score of revenue/PP&E vs 5y."""
    return _rolling_zscore(_safe_div(revenue, ppnetbasis), DDAYS_5Y)


def f44_mert_070_revenue_per_share_level(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Revenue per diluted share — top-line-per-unit pricing-power proxy."""
    return _safe_div(revenue, shareswadil)


def f44_mert_071_revenue_per_share_change_5y(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """5y log change in revenue per share."""
    return _safe_log(_safe_div(revenue, shareswadil)).diff(DDAYS_5Y)


def f44_mert_072_revenue_per_share_zscore_5y(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Z-score of log(revenue per share) vs 5y."""
    return _rolling_zscore(_safe_log(_safe_div(revenue, shareswadil)), DDAYS_5Y)


def f44_mert_073_revenue_per_share_decline_streak(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Current streak where revenue-per-share < trailing-1y mean of itself."""
    rps = _safe_div(revenue, shareswadil)
    m = rps.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (rps < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f44_mert_074_capital_turnover_proxy_level(revenue: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Capital turnover = revenue / (debt + equity)."""
    return _safe_div(revenue, debt + equity)


def f44_mert_075_capital_turnover_change_5y(revenue: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """5y change in capital turnover."""
    return _safe_div(revenue, debt + equity).diff(DDAYS_5Y)


# ============================================================
#                        REGISTRY
# ============================================================

MOAT_EROSION_TRAJECTORY_BASE_REGISTRY_001_075 = {
    "f44_mert_001_gp_margin_level": {"inputs": ["gp", "revenue"], "func": f44_mert_001_gp_margin_level},
    "f44_mert_002_gp_margin_change_yoy": {"inputs": ["gp", "revenue"], "func": f44_mert_002_gp_margin_change_yoy},
    "f44_mert_003_gp_margin_change_2y": {"inputs": ["gp", "revenue"], "func": f44_mert_003_gp_margin_change_2y},
    "f44_mert_004_gp_margin_change_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_004_gp_margin_change_5y},
    "f44_mert_005_gp_margin_zscore_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_005_gp_margin_zscore_5y},
    "f44_mert_006_gp_margin_rank_pct_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_006_gp_margin_rank_pct_5y},
    "f44_mert_007_gp_margin_log_distance_to_5y_max": {"inputs": ["gp", "revenue"], "func": f44_mert_007_gp_margin_log_distance_to_5y_max},
    "f44_mert_008_days_since_gp_margin_max_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_008_days_since_gp_margin_max_5y},
    "f44_mert_009_gp_margin_decline_streak": {"inputs": ["gp", "revenue"], "func": f44_mert_009_gp_margin_decline_streak},
    "f44_mert_010_gp_margin_negative_diff_count_8q": {"inputs": ["gp", "revenue"], "func": f44_mert_010_gp_margin_negative_diff_count_8q},
    "f44_mert_011_gp_margin_negative_diff_count_20q": {"inputs": ["gp", "revenue"], "func": f44_mert_011_gp_margin_negative_diff_count_20q},
    "f44_mert_012_gp_margin_acceleration_4q": {"inputs": ["gp", "revenue"], "func": f44_mert_012_gp_margin_acceleration_4q},
    "f44_mert_013_gp_margin_volatility_8q": {"inputs": ["gp", "revenue"], "func": f44_mert_013_gp_margin_volatility_8q},
    "f44_mert_014_gp_margin_volatility_zscore_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_014_gp_margin_volatility_zscore_5y},
    "f44_mert_015_gp_margin_below_5y_mean_streak": {"inputs": ["gp", "revenue"], "func": f44_mert_015_gp_margin_below_5y_mean_streak},
    "f44_mert_016_gp_margin_2y_minus_5y_baseline": {"inputs": ["gp", "revenue"], "func": f44_mert_016_gp_margin_2y_minus_5y_baseline},
    "f44_mert_017_gp_margin_smoothed_ema_thrust": {"inputs": ["gp", "revenue"], "func": f44_mert_017_gp_margin_smoothed_ema_thrust},
    "f44_mert_018_gp_margin_below_p25_count_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_018_gp_margin_below_p25_count_5y},
    "f44_mert_019_gp_margin_compression_rate_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_019_gp_margin_compression_rate_5y},
    "f44_mert_020_gp_margin_compression_r2_5y": {"inputs": ["gp", "revenue"], "func": f44_mert_020_gp_margin_compression_r2_5y},
    "f44_mert_021_opinc_margin_level": {"inputs": ["opinc", "revenue"], "func": f44_mert_021_opinc_margin_level},
    "f44_mert_022_opinc_margin_change_yoy": {"inputs": ["opinc", "revenue"], "func": f44_mert_022_opinc_margin_change_yoy},
    "f44_mert_023_opinc_margin_change_2y": {"inputs": ["opinc", "revenue"], "func": f44_mert_023_opinc_margin_change_2y},
    "f44_mert_024_opinc_margin_change_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_024_opinc_margin_change_5y},
    "f44_mert_025_opinc_margin_zscore_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_025_opinc_margin_zscore_5y},
    "f44_mert_026_opinc_margin_rank_pct_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_026_opinc_margin_rank_pct_5y},
    "f44_mert_027_opinc_margin_log_distance_to_5y_max": {"inputs": ["opinc", "revenue"], "func": f44_mert_027_opinc_margin_log_distance_to_5y_max},
    "f44_mert_028_days_since_opinc_margin_max_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_028_days_since_opinc_margin_max_5y},
    "f44_mert_029_opinc_margin_decline_streak": {"inputs": ["opinc", "revenue"], "func": f44_mert_029_opinc_margin_decline_streak},
    "f44_mert_030_opinc_margin_acceleration_4q": {"inputs": ["opinc", "revenue"], "func": f44_mert_030_opinc_margin_acceleration_4q},
    "f44_mert_031_opinc_margin_volatility_8q": {"inputs": ["opinc", "revenue"], "func": f44_mert_031_opinc_margin_volatility_8q},
    "f44_mert_032_opinc_margin_below_5y_mean_streak": {"inputs": ["opinc", "revenue"], "func": f44_mert_032_opinc_margin_below_5y_mean_streak},
    "f44_mert_033_opinc_margin_2y_minus_5y_baseline": {"inputs": ["opinc", "revenue"], "func": f44_mert_033_opinc_margin_2y_minus_5y_baseline},
    "f44_mert_034_opinc_margin_compression_rate_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_034_opinc_margin_compression_rate_5y},
    "f44_mert_035_opinc_margin_compression_r2_5y": {"inputs": ["opinc", "revenue"], "func": f44_mert_035_opinc_margin_compression_r2_5y},
    "f44_mert_036_ebitda_margin_level": {"inputs": ["ebitda", "revenue"], "func": f44_mert_036_ebitda_margin_level},
    "f44_mert_037_ebitda_margin_change_5y": {"inputs": ["ebitda", "revenue"], "func": f44_mert_037_ebitda_margin_change_5y},
    "f44_mert_038_ebitda_margin_zscore_5y": {"inputs": ["ebitda", "revenue"], "func": f44_mert_038_ebitda_margin_zscore_5y},
    "f44_mert_039_ebitda_margin_log_distance_to_5y_max": {"inputs": ["ebitda", "revenue"], "func": f44_mert_039_ebitda_margin_log_distance_to_5y_max},
    "f44_mert_040_ebitda_margin_compression_rate_5y": {"inputs": ["ebitda", "revenue"], "func": f44_mert_040_ebitda_margin_compression_rate_5y},
    "f44_mert_041_roic_proxy_level": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_041_roic_proxy_level},
    "f44_mert_042_roic_change_yoy": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_042_roic_change_yoy},
    "f44_mert_043_roic_change_5y": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_043_roic_change_5y},
    "f44_mert_044_roic_zscore_5y": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_044_roic_zscore_5y},
    "f44_mert_045_roic_decline_streak": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_045_roic_decline_streak},
    "f44_mert_046_roic_compression_rate_5y": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_046_roic_compression_rate_5y},
    "f44_mert_047_roe_level": {"inputs": ["netinc", "equity"], "func": f44_mert_047_roe_level},
    "f44_mert_048_roe_change_yoy": {"inputs": ["netinc", "equity"], "func": f44_mert_048_roe_change_yoy},
    "f44_mert_049_roe_change_5y": {"inputs": ["netinc", "equity"], "func": f44_mert_049_roe_change_5y},
    "f44_mert_050_roe_zscore_5y": {"inputs": ["netinc", "equity"], "func": f44_mert_050_roe_zscore_5y},
    "f44_mert_051_roe_decline_streak": {"inputs": ["netinc", "equity"], "func": f44_mert_051_roe_decline_streak},
    "f44_mert_052_roa_level": {"inputs": ["netinc", "assets"], "func": f44_mert_052_roa_level},
    "f44_mert_053_roa_change_yoy": {"inputs": ["netinc", "assets"], "func": f44_mert_053_roa_change_yoy},
    "f44_mert_054_roa_change_5y": {"inputs": ["netinc", "assets"], "func": f44_mert_054_roa_change_5y},
    "f44_mert_055_roa_zscore_5y": {"inputs": ["netinc", "assets"], "func": f44_mert_055_roa_zscore_5y},
    "f44_mert_056_roa_decline_streak": {"inputs": ["netinc", "assets"], "func": f44_mert_056_roa_decline_streak},
    "f44_mert_057_return_metrics_compound_decel_count_5y": {"inputs": ["opinc", "netinc", "assets", "equity", "debt"], "func": f44_mert_057_return_metrics_compound_decel_count_5y},
    "f44_mert_058_roic_below_long_mean_streak": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_058_roic_below_long_mean_streak},
    "f44_mert_059_roic_minus_2y_baseline": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_059_roic_minus_2y_baseline},
    "f44_mert_060_roic_consecutive_decline_count_8q": {"inputs": ["opinc", "debt", "equity"], "func": f44_mert_060_roic_consecutive_decline_count_8q},
    "f44_mert_061_revenue_per_assets_level": {"inputs": ["revenue", "assets"], "func": f44_mert_061_revenue_per_assets_level},
    "f44_mert_062_revenue_per_assets_change_yoy": {"inputs": ["revenue", "assets"], "func": f44_mert_062_revenue_per_assets_change_yoy},
    "f44_mert_063_revenue_per_assets_change_5y": {"inputs": ["revenue", "assets"], "func": f44_mert_063_revenue_per_assets_change_5y},
    "f44_mert_064_revenue_per_assets_zscore_5y": {"inputs": ["revenue", "assets"], "func": f44_mert_064_revenue_per_assets_zscore_5y},
    "f44_mert_065_revenue_per_assets_decline_streak": {"inputs": ["revenue", "assets"], "func": f44_mert_065_revenue_per_assets_decline_streak},
    "f44_mert_066_revenue_per_assets_compression_rate_5y": {"inputs": ["revenue", "assets"], "func": f44_mert_066_revenue_per_assets_compression_rate_5y},
    "f44_mert_067_revenue_per_ppe_level": {"inputs": ["revenue", "ppnetbasis"], "func": f44_mert_067_revenue_per_ppe_level},
    "f44_mert_068_revenue_per_ppe_change_5y": {"inputs": ["revenue", "ppnetbasis"], "func": f44_mert_068_revenue_per_ppe_change_5y},
    "f44_mert_069_revenue_per_ppe_zscore_5y": {"inputs": ["revenue", "ppnetbasis"], "func": f44_mert_069_revenue_per_ppe_zscore_5y},
    "f44_mert_070_revenue_per_share_level": {"inputs": ["revenue", "shareswadil"], "func": f44_mert_070_revenue_per_share_level},
    "f44_mert_071_revenue_per_share_change_5y": {"inputs": ["revenue", "shareswadil"], "func": f44_mert_071_revenue_per_share_change_5y},
    "f44_mert_072_revenue_per_share_zscore_5y": {"inputs": ["revenue", "shareswadil"], "func": f44_mert_072_revenue_per_share_zscore_5y},
    "f44_mert_073_revenue_per_share_decline_streak": {"inputs": ["revenue", "shareswadil"], "func": f44_mert_073_revenue_per_share_decline_streak},
    "f44_mert_074_capital_turnover_proxy_level": {"inputs": ["revenue", "debt", "equity"], "func": f44_mert_074_capital_turnover_proxy_level},
    "f44_mert_075_capital_turnover_change_5y": {"inputs": ["revenue", "debt", "equity"], "func": f44_mert_075_capital_turnover_change_5y},
}
