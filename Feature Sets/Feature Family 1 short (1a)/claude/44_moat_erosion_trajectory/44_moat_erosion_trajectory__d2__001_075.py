"""moat_erosion_trajectory d2 features 001_075 — 2nd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff() so the output is the second bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
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
        xm = xv.mean()
        wm = wv.mean()
        sxx = ((xv - xm) ** 2).sum()
        swy = ((wv - wm) ** 2).sum()
        sxy = ((xv - xm) * (wv - wm)).sum()
        if sxx == 0 or swy == 0:
            return np.nan
        return float(sxy ** 2 / (sxx * swy))
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

def f44_mert_001_gp_margin_level_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff().diff()

def f44_mert_002_gp_margin_change_yoy_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff(YDAYS).diff().diff()

def f44_mert_003_gp_margin_change_2y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff(DDAYS_2Y).diff().diff()

def f44_mert_004_gp_margin_change_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_005_gp_margin_zscore_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(gp, revenue), DDAYS_5Y).diff().diff()

def f44_mert_006_gp_margin_rank_pct_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y).diff().diff()

def f44_mert_007_gp_margin_log_distance_to_5y_max_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    mx = gm.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_safe_log(gm) - _safe_log(mx)).diff().diff()

def f44_mert_008_days_since_gp_margin_max_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _days_since_max(_safe_div(gp, revenue), DDAYS_5Y).diff().diff()

def f44_mert_009_gp_margin_decline_streak_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    m = gm.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (gm < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_010_gp_margin_negative_diff_count_8q_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    flag = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_011_gp_margin_negative_diff_count_20q_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    flag = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_012_gp_margin_acceleration_4q_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff(YDAYS).diff(YDAYS).diff().diff()

def f44_mert_013_gp_margin_volatility_8q_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std().diff().diff()

def f44_mert_014_gp_margin_volatility_zscore_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    v = _safe_div(gp, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _rolling_zscore(v, DDAYS_5Y).diff().diff()

def f44_mert_015_gp_margin_below_5y_mean_streak_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    m = gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (gm < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_016_gp_margin_2y_minus_5y_baseline_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    return (gm.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()).diff().diff()

def f44_mert_017_gp_margin_smoothed_ema_thrust_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    return (_ema(gm, QDAYS) - _ema(gm, YDAYS)).diff().diff()

def f44_mert_018_gp_margin_below_p25_count_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    thr = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = (gm < thr).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_019_gp_margin_compression_rate_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(gp, revenue), DDAYS_5Y).diff().diff()

def f44_mert_020_gp_margin_compression_r2_5y_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope_r2(_safe_div(gp, revenue), DDAYS_5Y).diff().diff()

def f44_mert_021_opinc_margin_level_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff().diff()

def f44_mert_022_opinc_margin_change_yoy_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff(YDAYS).diff().diff()

def f44_mert_023_opinc_margin_change_2y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff(DDAYS_2Y).diff().diff()

def f44_mert_024_opinc_margin_change_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_025_opinc_margin_zscore_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(opinc, revenue), DDAYS_5Y).diff().diff()

def f44_mert_026_opinc_margin_rank_pct_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_rank_pct(_safe_div(opinc, revenue), DDAYS_5Y).diff().diff()

def f44_mert_027_opinc_margin_log_distance_to_5y_max_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    om = _safe_div(opinc, revenue)
    mx = om.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_safe_log_signed(om) - _safe_log_signed(mx)).diff().diff()

def f44_mert_028_days_since_opinc_margin_max_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _days_since_max(_safe_div(opinc, revenue), DDAYS_5Y).diff().diff()

def f44_mert_029_opinc_margin_decline_streak_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    om = _safe_div(opinc, revenue)
    m = om.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (om < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_030_opinc_margin_acceleration_4q_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff(YDAYS).diff(YDAYS).diff().diff()

def f44_mert_031_opinc_margin_volatility_8q_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std().diff().diff()

def f44_mert_032_opinc_margin_below_5y_mean_streak_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    om = _safe_div(opinc, revenue)
    m = om.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (om < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_033_opinc_margin_2y_minus_5y_baseline_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    om = _safe_div(opinc, revenue)
    return (om.rolling(DDAYS_2Y, min_periods=YDAYS).mean() - om.rolling(DDAYS_5Y, min_periods=YDAYS).mean()).diff().diff()

def f44_mert_034_opinc_margin_compression_rate_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(opinc, revenue), DDAYS_5Y).diff().diff()

def f44_mert_035_opinc_margin_compression_r2_5y_d2(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope_r2(_safe_div(opinc, revenue), DDAYS_5Y).diff().diff()

def f44_mert_036_ebitda_margin_level_d2(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebitda, revenue).diff().diff()

def f44_mert_037_ebitda_margin_change_5y_d2(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebitda, revenue).diff(DDAYS_5Y).diff().diff()

def f44_mert_038_ebitda_margin_zscore_5y_d2(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(ebitda, revenue), DDAYS_5Y).diff().diff()

def f44_mert_039_ebitda_margin_log_distance_to_5y_max_d2(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    em = _safe_div(ebitda, revenue)
    mx = em.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_safe_log_signed(em) - _safe_log_signed(mx)).diff().diff()

def f44_mert_040_ebitda_margin_compression_rate_5y_d2(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(ebitda, revenue), DDAYS_5Y).diff().diff()

def f44_mert_041_roic_proxy_level_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(opinc, debt + equity).diff().diff()

def f44_mert_042_roic_change_yoy_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(opinc, debt + equity).diff(YDAYS).diff().diff()

def f44_mert_043_roic_change_5y_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(opinc, debt + equity).diff(DDAYS_5Y).diff().diff()

def f44_mert_044_roic_zscore_5y_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(opinc, debt + equity), DDAYS_5Y).diff().diff()

def f44_mert_045_roic_decline_streak_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(opinc, debt + equity)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_046_roic_compression_rate_5y_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(opinc, debt + equity), DDAYS_5Y).diff().diff()

def f44_mert_047_roe_level_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(netinc, equity).diff().diff()

def f44_mert_048_roe_change_yoy_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(netinc, equity).diff(YDAYS).diff().diff()

def f44_mert_049_roe_change_5y_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(netinc, equity).diff(DDAYS_5Y).diff().diff()

def f44_mert_050_roe_zscore_5y_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(netinc, equity), DDAYS_5Y).diff().diff()

def f44_mert_051_roe_decline_streak_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(netinc, equity)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_052_roa_level_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(netinc, assets).diff().diff()

def f44_mert_053_roa_change_yoy_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(netinc, assets).diff(YDAYS).diff().diff()

def f44_mert_054_roa_change_5y_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(netinc, assets).diff(DDAYS_5Y).diff().diff()

def f44_mert_055_roa_zscore_5y_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(netinc, assets), DDAYS_5Y).diff().diff()

def f44_mert_056_roa_decline_streak_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    r = _safe_div(netinc, assets)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_057_return_metrics_compound_decel_count_5y_d2(opinc: pd.Series, netinc: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    roic = _safe_div(opinc, debt + equity)
    roe = _safe_div(netinc, equity)
    roa = _safe_div(netinc, assets)
    m_roic = roic.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    m_roe = roe.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    m_roa = roa.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((roic < m_roic) & (roe < m_roe) & (roa < m_roa)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_058_roic_below_long_mean_streak_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(opinc, debt + equity)
    m = r.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (r < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_059_roic_minus_2y_baseline_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(opinc, debt + equity)
    return (r - r.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff().diff()

def f44_mert_060_roic_consecutive_decline_count_8q_d2(opinc: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(opinc, debt + equity)
    flag = (r < r.shift(QDAYS)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff()

def f44_mert_061_revenue_per_assets_level_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(revenue, assets).diff().diff()

def f44_mert_062_revenue_per_assets_change_yoy_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(revenue, assets).diff(YDAYS).diff().diff()

def f44_mert_063_revenue_per_assets_change_5y_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(revenue, assets).diff(DDAYS_5Y).diff().diff()

def f44_mert_064_revenue_per_assets_zscore_5y_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(revenue, assets), DDAYS_5Y).diff().diff()

def f44_mert_065_revenue_per_assets_decline_streak_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    t = _safe_div(revenue, assets)
    m = t.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (t < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_066_revenue_per_assets_compression_rate_5y_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(revenue, assets), DDAYS_5Y).diff().diff()

def f44_mert_067_revenue_per_ppe_level_d2(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    return _safe_div(revenue, ppnetbasis).diff().diff()

def f44_mert_068_revenue_per_ppe_change_5y_d2(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    return _safe_div(revenue, ppnetbasis).diff(DDAYS_5Y).diff().diff()

def f44_mert_069_revenue_per_ppe_zscore_5y_d2(revenue: pd.Series, ppnetbasis: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(revenue, ppnetbasis), DDAYS_5Y).diff().diff()

def f44_mert_070_revenue_per_share_level_d2(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    return _safe_div(revenue, shareswadil).diff().diff()

def f44_mert_071_revenue_per_share_change_5y_d2(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    return _safe_log(_safe_div(revenue, shareswadil)).diff(DDAYS_5Y).diff().diff()

def f44_mert_072_revenue_per_share_zscore_5y_d2(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_log(_safe_div(revenue, shareswadil)), DDAYS_5Y).diff().diff()

def f44_mert_073_revenue_per_share_decline_streak_d2(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    rps = _safe_div(revenue, shareswadil)
    m = rps.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (rps < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff()

def f44_mert_074_capital_turnover_proxy_level_d2(revenue: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(revenue, debt + equity).diff().diff()

def f44_mert_075_capital_turnover_change_5y_d2(revenue: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(revenue, debt + equity).diff(DDAYS_5Y).diff().diff()
MOAT_EROSION_TRAJECTORY_D2_REGISTRY_001_075 = {'f44_mert_001_gp_margin_level_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_001_gp_margin_level_d2}, 'f44_mert_002_gp_margin_change_yoy_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_002_gp_margin_change_yoy_d2}, 'f44_mert_003_gp_margin_change_2y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_003_gp_margin_change_2y_d2}, 'f44_mert_004_gp_margin_change_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_004_gp_margin_change_5y_d2}, 'f44_mert_005_gp_margin_zscore_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_005_gp_margin_zscore_5y_d2}, 'f44_mert_006_gp_margin_rank_pct_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_006_gp_margin_rank_pct_5y_d2}, 'f44_mert_007_gp_margin_log_distance_to_5y_max_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_007_gp_margin_log_distance_to_5y_max_d2}, 'f44_mert_008_days_since_gp_margin_max_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_008_days_since_gp_margin_max_5y_d2}, 'f44_mert_009_gp_margin_decline_streak_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_009_gp_margin_decline_streak_d2}, 'f44_mert_010_gp_margin_negative_diff_count_8q_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_010_gp_margin_negative_diff_count_8q_d2}, 'f44_mert_011_gp_margin_negative_diff_count_20q_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_011_gp_margin_negative_diff_count_20q_d2}, 'f44_mert_012_gp_margin_acceleration_4q_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_012_gp_margin_acceleration_4q_d2}, 'f44_mert_013_gp_margin_volatility_8q_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_013_gp_margin_volatility_8q_d2}, 'f44_mert_014_gp_margin_volatility_zscore_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_014_gp_margin_volatility_zscore_5y_d2}, 'f44_mert_015_gp_margin_below_5y_mean_streak_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_015_gp_margin_below_5y_mean_streak_d2}, 'f44_mert_016_gp_margin_2y_minus_5y_baseline_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_016_gp_margin_2y_minus_5y_baseline_d2}, 'f44_mert_017_gp_margin_smoothed_ema_thrust_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_017_gp_margin_smoothed_ema_thrust_d2}, 'f44_mert_018_gp_margin_below_p25_count_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_018_gp_margin_below_p25_count_5y_d2}, 'f44_mert_019_gp_margin_compression_rate_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_019_gp_margin_compression_rate_5y_d2}, 'f44_mert_020_gp_margin_compression_r2_5y_d2': {'inputs': ['gp', 'revenue'], 'func': f44_mert_020_gp_margin_compression_r2_5y_d2}, 'f44_mert_021_opinc_margin_level_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_021_opinc_margin_level_d2}, 'f44_mert_022_opinc_margin_change_yoy_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_022_opinc_margin_change_yoy_d2}, 'f44_mert_023_opinc_margin_change_2y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_023_opinc_margin_change_2y_d2}, 'f44_mert_024_opinc_margin_change_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_024_opinc_margin_change_5y_d2}, 'f44_mert_025_opinc_margin_zscore_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_025_opinc_margin_zscore_5y_d2}, 'f44_mert_026_opinc_margin_rank_pct_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_026_opinc_margin_rank_pct_5y_d2}, 'f44_mert_027_opinc_margin_log_distance_to_5y_max_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_027_opinc_margin_log_distance_to_5y_max_d2}, 'f44_mert_028_days_since_opinc_margin_max_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_028_days_since_opinc_margin_max_5y_d2}, 'f44_mert_029_opinc_margin_decline_streak_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_029_opinc_margin_decline_streak_d2}, 'f44_mert_030_opinc_margin_acceleration_4q_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_030_opinc_margin_acceleration_4q_d2}, 'f44_mert_031_opinc_margin_volatility_8q_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_031_opinc_margin_volatility_8q_d2}, 'f44_mert_032_opinc_margin_below_5y_mean_streak_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_032_opinc_margin_below_5y_mean_streak_d2}, 'f44_mert_033_opinc_margin_2y_minus_5y_baseline_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_033_opinc_margin_2y_minus_5y_baseline_d2}, 'f44_mert_034_opinc_margin_compression_rate_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_034_opinc_margin_compression_rate_5y_d2}, 'f44_mert_035_opinc_margin_compression_r2_5y_d2': {'inputs': ['opinc', 'revenue'], 'func': f44_mert_035_opinc_margin_compression_r2_5y_d2}, 'f44_mert_036_ebitda_margin_level_d2': {'inputs': ['ebitda', 'revenue'], 'func': f44_mert_036_ebitda_margin_level_d2}, 'f44_mert_037_ebitda_margin_change_5y_d2': {'inputs': ['ebitda', 'revenue'], 'func': f44_mert_037_ebitda_margin_change_5y_d2}, 'f44_mert_038_ebitda_margin_zscore_5y_d2': {'inputs': ['ebitda', 'revenue'], 'func': f44_mert_038_ebitda_margin_zscore_5y_d2}, 'f44_mert_039_ebitda_margin_log_distance_to_5y_max_d2': {'inputs': ['ebitda', 'revenue'], 'func': f44_mert_039_ebitda_margin_log_distance_to_5y_max_d2}, 'f44_mert_040_ebitda_margin_compression_rate_5y_d2': {'inputs': ['ebitda', 'revenue'], 'func': f44_mert_040_ebitda_margin_compression_rate_5y_d2}, 'f44_mert_041_roic_proxy_level_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_041_roic_proxy_level_d2}, 'f44_mert_042_roic_change_yoy_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_042_roic_change_yoy_d2}, 'f44_mert_043_roic_change_5y_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_043_roic_change_5y_d2}, 'f44_mert_044_roic_zscore_5y_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_044_roic_zscore_5y_d2}, 'f44_mert_045_roic_decline_streak_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_045_roic_decline_streak_d2}, 'f44_mert_046_roic_compression_rate_5y_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_046_roic_compression_rate_5y_d2}, 'f44_mert_047_roe_level_d2': {'inputs': ['netinc', 'equity'], 'func': f44_mert_047_roe_level_d2}, 'f44_mert_048_roe_change_yoy_d2': {'inputs': ['netinc', 'equity'], 'func': f44_mert_048_roe_change_yoy_d2}, 'f44_mert_049_roe_change_5y_d2': {'inputs': ['netinc', 'equity'], 'func': f44_mert_049_roe_change_5y_d2}, 'f44_mert_050_roe_zscore_5y_d2': {'inputs': ['netinc', 'equity'], 'func': f44_mert_050_roe_zscore_5y_d2}, 'f44_mert_051_roe_decline_streak_d2': {'inputs': ['netinc', 'equity'], 'func': f44_mert_051_roe_decline_streak_d2}, 'f44_mert_052_roa_level_d2': {'inputs': ['netinc', 'assets'], 'func': f44_mert_052_roa_level_d2}, 'f44_mert_053_roa_change_yoy_d2': {'inputs': ['netinc', 'assets'], 'func': f44_mert_053_roa_change_yoy_d2}, 'f44_mert_054_roa_change_5y_d2': {'inputs': ['netinc', 'assets'], 'func': f44_mert_054_roa_change_5y_d2}, 'f44_mert_055_roa_zscore_5y_d2': {'inputs': ['netinc', 'assets'], 'func': f44_mert_055_roa_zscore_5y_d2}, 'f44_mert_056_roa_decline_streak_d2': {'inputs': ['netinc', 'assets'], 'func': f44_mert_056_roa_decline_streak_d2}, 'f44_mert_057_return_metrics_compound_decel_count_5y_d2': {'inputs': ['opinc', 'netinc', 'assets', 'equity', 'debt'], 'func': f44_mert_057_return_metrics_compound_decel_count_5y_d2}, 'f44_mert_058_roic_below_long_mean_streak_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_058_roic_below_long_mean_streak_d2}, 'f44_mert_059_roic_minus_2y_baseline_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_059_roic_minus_2y_baseline_d2}, 'f44_mert_060_roic_consecutive_decline_count_8q_d2': {'inputs': ['opinc', 'debt', 'equity'], 'func': f44_mert_060_roic_consecutive_decline_count_8q_d2}, 'f44_mert_061_revenue_per_assets_level_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_061_revenue_per_assets_level_d2}, 'f44_mert_062_revenue_per_assets_change_yoy_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_062_revenue_per_assets_change_yoy_d2}, 'f44_mert_063_revenue_per_assets_change_5y_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_063_revenue_per_assets_change_5y_d2}, 'f44_mert_064_revenue_per_assets_zscore_5y_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_064_revenue_per_assets_zscore_5y_d2}, 'f44_mert_065_revenue_per_assets_decline_streak_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_065_revenue_per_assets_decline_streak_d2}, 'f44_mert_066_revenue_per_assets_compression_rate_5y_d2': {'inputs': ['revenue', 'assets'], 'func': f44_mert_066_revenue_per_assets_compression_rate_5y_d2}, 'f44_mert_067_revenue_per_ppe_level_d2': {'inputs': ['revenue', 'ppnetbasis'], 'func': f44_mert_067_revenue_per_ppe_level_d2}, 'f44_mert_068_revenue_per_ppe_change_5y_d2': {'inputs': ['revenue', 'ppnetbasis'], 'func': f44_mert_068_revenue_per_ppe_change_5y_d2}, 'f44_mert_069_revenue_per_ppe_zscore_5y_d2': {'inputs': ['revenue', 'ppnetbasis'], 'func': f44_mert_069_revenue_per_ppe_zscore_5y_d2}, 'f44_mert_070_revenue_per_share_level_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f44_mert_070_revenue_per_share_level_d2}, 'f44_mert_071_revenue_per_share_change_5y_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f44_mert_071_revenue_per_share_change_5y_d2}, 'f44_mert_072_revenue_per_share_zscore_5y_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f44_mert_072_revenue_per_share_zscore_5y_d2}, 'f44_mert_073_revenue_per_share_decline_streak_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f44_mert_073_revenue_per_share_decline_streak_d2}, 'f44_mert_074_capital_turnover_proxy_level_d2': {'inputs': ['revenue', 'debt', 'equity'], 'func': f44_mert_074_capital_turnover_proxy_level_d2}, 'f44_mert_075_capital_turnover_change_5y_d2': {'inputs': ['revenue', 'debt', 'equity'], 'func': f44_mert_075_capital_turnover_change_5y_d2}}
