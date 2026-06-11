"""dilution_rate_trajectory d2 features 001-075 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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

def _ttm(s):
    return s.rolling(4, min_periods=1).sum()

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

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

def _runlen_pos(s):
    pos = (s > 0).astype(float)
    out = pos.copy()
    grp = (pos != pos.shift()).cumsum()
    out = pos.groupby(grp).cumsum()
    return out * pos

def f26_drtj_001_sharesbas_qoq_pct_d2(sharesbas):
    return _qoq_pct(sharesbas).diff().diff()

def f26_drtj_002_sharesbas_yoy_pct_d2(sharesbas):
    return _yoy_pct(sharesbas).diff().diff()

def f26_drtj_003_sharesbas_8q_pct_d2(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(8), sharesbas.shift(8).abs()).diff().diff()

def f26_drtj_004_sharesbas_12q_pct_d2(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(12), sharesbas.shift(12).abs()).diff().diff()

def f26_drtj_005_sharesbas_log_diff_4q_d2(sharesbas):
    return (_safe_log(sharesbas) - _safe_log(sharesbas.shift(4))).diff().diff()

def f26_drtj_006_sharesbas_compound_growth_4q_d2(sharesbas):
    return (_safe_div(sharesbas, sharesbas.shift(4)) ** 0.25 - 1.0).diff().diff()

def f26_drtj_007_sharesbas_avg_qoq_pct_4q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(4, min_periods=2).mean().diff().diff()

def f26_drtj_008_sharesbas_avg_qoq_pct_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).mean().diff().diff()

def f26_drtj_009_sharesbas_max_qoq_pct_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).max().diff().diff()

def f26_drtj_010_sharesbas_consecutive_dil_quarters_d2(sharesbas):
    return _runlen_pos(_qoq_pct(sharesbas)).diff().diff()

def f26_drtj_011_sharesbas_dilution_frequency_8q_d2(sharesbas):
    pos = (_qoq_pct(sharesbas) > 0).astype(float)
    return pos.rolling(8, min_periods=3).mean().diff().diff()

def f26_drtj_012_sharesbas_persistent_dilution_streak_d2(sharesbas):
    return _runlen_pos(_qoq_pct(sharesbas)).diff().diff()

def f26_drtj_013_sharesbas_qoq_skewness_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=4).skew().diff().diff()

def f26_drtj_014_sharesbas_qoq_kurt_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=4).kurt().diff().diff()

def f26_drtj_015_sharesbas_qoq_max_minus_mean_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q.rolling(8, min_periods=3).max() - q.rolling(8, min_periods=3).mean()).diff().diff()

def f26_drtj_016_shareswadil_qoq_pct_d2(shareswadil):
    return _qoq_pct(shareswadil).diff().diff()

def f26_drtj_017_shareswadil_yoy_pct_d2(shareswadil):
    return _yoy_pct(shareswadil).diff().diff()

def f26_drtj_018_shareswadil_8q_pct_d2(shareswadil):
    return _safe_div(shareswadil - shareswadil.shift(8), shareswadil.shift(8).abs()).diff().diff()

def f26_drtj_019_shareswadil_log_diff_4q_d2(shareswadil):
    return (_safe_log(shareswadil) - _safe_log(shareswadil.shift(4))).diff().diff()

def f26_drtj_020_shareswadil_minus_shareswa_share_d2(shareswadil, shareswa):
    return _safe_div(shareswadil - shareswa, shareswa).diff().diff()

def f26_drtj_021_shareswadil_minus_shareswa_yoy_d2(shareswadil, shareswa):
    gap = _safe_div(shareswadil - shareswa, shareswa)
    return (gap - gap.shift(4)).diff().diff()

def f26_drtj_022_shareswadil_minus_shareswa_8q_pct_d2(shareswadil, shareswa):
    gap = shareswadil - shareswa
    return _safe_div(gap - gap.shift(8), gap.shift(8).abs()).diff().diff()

def f26_drtj_023_dilution_gap_zscore_8q_d2(shareswadil, shareswa):
    gap = _safe_div(shareswadil - shareswa, shareswa)
    return _rolling_zscore(gap, 8).diff().diff()

def f26_drtj_024_shareswadil_to_sharesbas_d2(shareswadil, sharesbas):
    return _safe_div(shareswadil, sharesbas).diff().diff()

def f26_drtj_025_shareswadil_to_sharesbas_yoy_change_d2(shareswadil, sharesbas):
    r = _safe_div(shareswadil, sharesbas)
    return (r - r.shift(4)).diff().diff()

def f26_drtj_026_shareswa_to_sharesbas_d2(shareswa, sharesbas):
    return _safe_div(shareswa, sharesbas).diff().diff()

def f26_drtj_027_shareswa_qoq_pct_d2(shareswa):
    return _qoq_pct(shareswa).diff().diff()

def f26_drtj_028_shareswa_yoy_pct_d2(shareswa):
    return _yoy_pct(shareswa).diff().diff()

def f26_drtj_029_shareswa_minus_sharesbas_share_d2(shareswa, sharesbas):
    return _safe_div(shareswa - sharesbas, sharesbas.abs()).diff().diff()

def f26_drtj_030_sharesbas_minus_lag1_to_avg_4q_d2(sharesbas):
    avg = sharesbas.rolling(4, min_periods=2).mean()
    return _safe_div(sharesbas - sharesbas.shift(1), avg.abs()).diff().diff()

def f26_drtj_031_sharesbas_trailing_growth_252d_proxy_d2(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(4), sharesbas.shift(4).abs()).diff().diff()

def f26_drtj_032_sharesbas_3y_cagr_d2(sharesbas):
    r = _safe_div(sharesbas, sharesbas.shift(12))
    return (r ** (1.0 / 3.0) - 1.0).diff().diff()

def f26_drtj_033_sharesbas_5y_cagr_d2(sharesbas):
    r = _safe_div(sharesbas, sharesbas.shift(20))
    return (r ** (1.0 / 5.0) - 1.0).diff().diff()

def f26_drtj_034_sharesbas_secondary_offering_flag_4q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q.rolling(4, min_periods=1).max() > 0.05).astype(float).diff().diff()

def f26_drtj_035_sharesbas_secondary_offering_count_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q > 0.05).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f26_drtj_036_sharesbas_secondary_offering_count_12q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q > 0.05).astype(float).rolling(12, min_periods=4).sum().diff().diff()

def f26_drtj_037_sharesbas_largest_single_qoq_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).max().diff().diff()

def f26_drtj_038_sharesbas_largest_single_qoq_12q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(12, min_periods=4).max().diff().diff()

def f26_drtj_039_sharesbas_largest_single_qoq_20q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(20, min_periods=6).max().diff().diff()

def f26_drtj_040_sharesbas_avg_top2_qoq_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return q.rolling(8, min_periods=3).apply(lambda y: np.nanmean(np.sort(y)[-2:]) if np.isfinite(y).sum() >= 2 else np.nan, raw=True).diff().diff()

def f26_drtj_041_sharesbas_avg_top3_qoq_12q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return q.rolling(12, min_periods=4).apply(lambda y: np.nanmean(np.sort(y)[-3:]) if np.isfinite(y).sum() >= 3 else np.nan, raw=True).diff().diff()

def f26_drtj_042_sharesbas_share_of_growth_from_top1_d2(sharesbas):
    q = _qoq_pct(sharesbas).clip(lower=0)
    top = q.rolling(8, min_periods=3).max()
    tot = q.rolling(8, min_periods=3).sum()
    return _safe_div(top, tot).diff().diff()

def f26_drtj_043_sharesbas_share_of_growth_from_top3_d2(sharesbas):
    q = _qoq_pct(sharesbas).clip(lower=0)
    top3 = q.rolling(12, min_periods=4).apply(lambda y: np.nansum(np.sort(y)[-3:]) if np.isfinite(y).sum() >= 3 else np.nan, raw=True)
    tot = q.rolling(12, min_periods=4).sum()
    return _safe_div(top3, tot).diff().diff()

def f26_drtj_044_sharesbas_diffusion_index_8q_d2(sharesbas):
    return (_qoq_pct(sharesbas) > 0).astype(float).rolling(8, min_periods=3).mean().diff().diff()

def f26_drtj_045_sharesbas_diffusion_index_12q_d2(sharesbas):
    return (_qoq_pct(sharesbas) > 0).astype(float).rolling(12, min_periods=4).mean().diff().diff()

def f26_drtj_046_dilution_vs_revenue_growth_yoy_d2(sharesbas, revenue):
    return (_yoy_pct(sharesbas) - _yoy_pct(_ttm(revenue))).diff().diff()

def f26_drtj_047_dilution_vs_revenue_growth_8q_d2(sharesbas, revenue):
    sbg = _safe_div(sharesbas - sharesbas.shift(8), sharesbas.shift(8).abs())
    rvg = _safe_div(_ttm(revenue) - _ttm(revenue).shift(8), _ttm(revenue).shift(8).abs())
    return (sbg - rvg).diff().diff()

def f26_drtj_048_dilution_per_dollar_revenue_growth_d2(sharesbas, revenue):
    return _safe_div(_yoy_pct(sharesbas), _yoy_pct(_ttm(revenue)).abs()).diff().diff()

def f26_drtj_049_sharesbas_growth_vs_equity_growth_yoy_d2(sharesbas, equity):
    return (_yoy_pct(sharesbas) - _yoy_pct(equity)).diff().diff()

def f26_drtj_050_sharesbas_growth_vs_assets_growth_yoy_d2(sharesbas, assets):
    return (_yoy_pct(sharesbas) - _yoy_pct(assets)).diff().diff()

def f26_drtj_051_sharesbas_growth_vs_fcf_yoy_d2(sharesbas, fcf):
    return (_yoy_pct(sharesbas) - _yoy_pct(_ttm(fcf))).diff().diff()

def f26_drtj_052_ncfcommon_to_marketcap_ttm_d2(ncfcommon, marketcap):
    return _safe_div(_ttm(ncfcommon), marketcap).diff().diff()

def f26_drtj_053_ncfcommon_to_marketcap_yoy_d2(ncfcommon, marketcap):
    r = _safe_div(_ttm(ncfcommon), marketcap)
    return (r - r.shift(4)).diff().diff()

def f26_drtj_054_ncfcommon_positive_quarters_count_8q_d2(ncfcommon):
    return (ncfcommon > 0).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f26_drtj_055_ncfcommon_positive_streak_d2(ncfcommon):
    return _runlen_pos(ncfcommon).diff().diff()

def f26_drtj_056_ncfcommon_avg_8q_d2(ncfcommon):
    return ncfcommon.rolling(8, min_periods=3).mean().diff().diff()

def f26_drtj_057_ncfcommon_to_equity_8q_d2(ncfcommon, equity):
    return _safe_div(ncfcommon.rolling(8, min_periods=3).sum(), equity).diff().diff()

def f26_drtj_058_ncfcommon_growth_yoy_d2(ncfcommon):
    return _yoy_pct(_ttm(ncfcommon)).diff().diff()

def f26_drtj_059_ncfcommon_minus_ncfdiv_ttm_d2(ncfcommon, ncfdiv):
    return (_ttm(ncfcommon) - _ttm(ncfdiv)).diff().diff()

def f26_drtj_060_ncfcommon_to_assets_ttm_d2(ncfcommon, assets):
    return _safe_div(_ttm(ncfcommon), assets).diff().diff()

def f26_drtj_061_sharesbas_zscore_4q_d2(sharesbas):
    return _rolling_zscore(sharesbas, 4).diff().diff()

def f26_drtj_062_sharesbas_qoq_zscore_8q_d2(sharesbas):
    return _rolling_zscore(_qoq_pct(sharesbas), 8).diff().diff()

def f26_drtj_063_sharesbas_qoq_zscore_12q_d2(sharesbas):
    return _rolling_zscore(_qoq_pct(sharesbas), 12).diff().diff()

def f26_drtj_064_sharesbas_growth_z_minus_mean_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q - q.rolling(8, min_periods=3).mean()).diff().diff()

def f26_drtj_065_sharesbas_acceleration_signal_8q_d2(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.rolling(8, min_periods=3).mean().shift(1)).diff().diff()

def f26_drtj_066_sharesbas_above_trend_8q_d2(sharesbas):
    trend = sharesbas.rolling(8, min_periods=3).mean()
    return (sharesbas - trend).diff().diff()

def f26_drtj_067_sharesbas_above_trend_zscore_8q_d2(sharesbas):
    return _rolling_zscore(sharesbas, 8).diff().diff()

def f26_drtj_068_sharesbas_residual_to_trend_8q_d2(sharesbas):
    trend = sharesbas.rolling(8, min_periods=3).mean()
    return _safe_div(sharesbas - trend, trend.abs()).diff().diff()

def f26_drtj_069_sharesbas_growth_persistence_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return q.rolling(8, min_periods=3).apply(lambda y: pd.Series(y).autocorr(lag=1) if np.isfinite(y).sum() >= 3 else np.nan, raw=False).diff().diff()

def f26_drtj_070_sharesbas_dilution_intensity_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas).clip(lower=0)
    return (q.rolling(8, min_periods=3).sum() / 8.0).diff().diff()

def f26_drtj_071_sharesbas_growth_dispersion_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).std().diff().diff()

def f26_drtj_072_sharesbas_growth_dispersion_12q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(12, min_periods=4).std().diff().diff()

def f26_drtj_073_sharesbas_growth_range_8q_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q.rolling(8, min_periods=3).max() - q.rolling(8, min_periods=3).min()).diff().diff()

def f26_drtj_074_sharesbas_dilution_streak_length_d2(sharesbas):
    return _runlen_pos(_qoq_pct(sharesbas)).rolling(8, min_periods=1).max().diff().diff()

def f26_drtj_075_sharesbas_clean_quarter_ratio_8q_d2(sharesbas):
    pos = (_qoq_pct(sharesbas) <= 0).astype(float)
    return pos.rolling(8, min_periods=3).mean().diff().diff()
DILUTION_RATE_TRAJECTORY_D2_REGISTRY_001_075 = {'f26_drtj_001_sharesbas_qoq_pct_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_001_sharesbas_qoq_pct_d2}, 'f26_drtj_002_sharesbas_yoy_pct_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_002_sharesbas_yoy_pct_d2}, 'f26_drtj_003_sharesbas_8q_pct_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_003_sharesbas_8q_pct_d2}, 'f26_drtj_004_sharesbas_12q_pct_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_004_sharesbas_12q_pct_d2}, 'f26_drtj_005_sharesbas_log_diff_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_005_sharesbas_log_diff_4q_d2}, 'f26_drtj_006_sharesbas_compound_growth_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_006_sharesbas_compound_growth_4q_d2}, 'f26_drtj_007_sharesbas_avg_qoq_pct_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_007_sharesbas_avg_qoq_pct_4q_d2}, 'f26_drtj_008_sharesbas_avg_qoq_pct_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_008_sharesbas_avg_qoq_pct_8q_d2}, 'f26_drtj_009_sharesbas_max_qoq_pct_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_009_sharesbas_max_qoq_pct_8q_d2}, 'f26_drtj_010_sharesbas_consecutive_dil_quarters_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_010_sharesbas_consecutive_dil_quarters_d2}, 'f26_drtj_011_sharesbas_dilution_frequency_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_011_sharesbas_dilution_frequency_8q_d2}, 'f26_drtj_012_sharesbas_persistent_dilution_streak_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_012_sharesbas_persistent_dilution_streak_d2}, 'f26_drtj_013_sharesbas_qoq_skewness_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_013_sharesbas_qoq_skewness_8q_d2}, 'f26_drtj_014_sharesbas_qoq_kurt_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_014_sharesbas_qoq_kurt_8q_d2}, 'f26_drtj_015_sharesbas_qoq_max_minus_mean_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_015_sharesbas_qoq_max_minus_mean_8q_d2}, 'f26_drtj_016_shareswadil_qoq_pct_d2': {'inputs': ['shareswadil'], 'func': f26_drtj_016_shareswadil_qoq_pct_d2}, 'f26_drtj_017_shareswadil_yoy_pct_d2': {'inputs': ['shareswadil'], 'func': f26_drtj_017_shareswadil_yoy_pct_d2}, 'f26_drtj_018_shareswadil_8q_pct_d2': {'inputs': ['shareswadil'], 'func': f26_drtj_018_shareswadil_8q_pct_d2}, 'f26_drtj_019_shareswadil_log_diff_4q_d2': {'inputs': ['shareswadil'], 'func': f26_drtj_019_shareswadil_log_diff_4q_d2}, 'f26_drtj_020_shareswadil_minus_shareswa_share_d2': {'inputs': ['shareswadil', 'shareswa'], 'func': f26_drtj_020_shareswadil_minus_shareswa_share_d2}, 'f26_drtj_021_shareswadil_minus_shareswa_yoy_d2': {'inputs': ['shareswadil', 'shareswa'], 'func': f26_drtj_021_shareswadil_minus_shareswa_yoy_d2}, 'f26_drtj_022_shareswadil_minus_shareswa_8q_pct_d2': {'inputs': ['shareswadil', 'shareswa'], 'func': f26_drtj_022_shareswadil_minus_shareswa_8q_pct_d2}, 'f26_drtj_023_dilution_gap_zscore_8q_d2': {'inputs': ['shareswadil', 'shareswa'], 'func': f26_drtj_023_dilution_gap_zscore_8q_d2}, 'f26_drtj_024_shareswadil_to_sharesbas_d2': {'inputs': ['shareswadil', 'sharesbas'], 'func': f26_drtj_024_shareswadil_to_sharesbas_d2}, 'f26_drtj_025_shareswadil_to_sharesbas_yoy_change_d2': {'inputs': ['shareswadil', 'sharesbas'], 'func': f26_drtj_025_shareswadil_to_sharesbas_yoy_change_d2}, 'f26_drtj_026_shareswa_to_sharesbas_d2': {'inputs': ['shareswa', 'sharesbas'], 'func': f26_drtj_026_shareswa_to_sharesbas_d2}, 'f26_drtj_027_shareswa_qoq_pct_d2': {'inputs': ['shareswa'], 'func': f26_drtj_027_shareswa_qoq_pct_d2}, 'f26_drtj_028_shareswa_yoy_pct_d2': {'inputs': ['shareswa'], 'func': f26_drtj_028_shareswa_yoy_pct_d2}, 'f26_drtj_029_shareswa_minus_sharesbas_share_d2': {'inputs': ['shareswa', 'sharesbas'], 'func': f26_drtj_029_shareswa_minus_sharesbas_share_d2}, 'f26_drtj_030_sharesbas_minus_lag1_to_avg_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_030_sharesbas_minus_lag1_to_avg_4q_d2}, 'f26_drtj_031_sharesbas_trailing_growth_252d_proxy_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_031_sharesbas_trailing_growth_252d_proxy_d2}, 'f26_drtj_032_sharesbas_3y_cagr_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_032_sharesbas_3y_cagr_d2}, 'f26_drtj_033_sharesbas_5y_cagr_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_033_sharesbas_5y_cagr_d2}, 'f26_drtj_034_sharesbas_secondary_offering_flag_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_034_sharesbas_secondary_offering_flag_4q_d2}, 'f26_drtj_035_sharesbas_secondary_offering_count_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_035_sharesbas_secondary_offering_count_8q_d2}, 'f26_drtj_036_sharesbas_secondary_offering_count_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_036_sharesbas_secondary_offering_count_12q_d2}, 'f26_drtj_037_sharesbas_largest_single_qoq_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_037_sharesbas_largest_single_qoq_8q_d2}, 'f26_drtj_038_sharesbas_largest_single_qoq_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_038_sharesbas_largest_single_qoq_12q_d2}, 'f26_drtj_039_sharesbas_largest_single_qoq_20q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_039_sharesbas_largest_single_qoq_20q_d2}, 'f26_drtj_040_sharesbas_avg_top2_qoq_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_040_sharesbas_avg_top2_qoq_8q_d2}, 'f26_drtj_041_sharesbas_avg_top3_qoq_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_041_sharesbas_avg_top3_qoq_12q_d2}, 'f26_drtj_042_sharesbas_share_of_growth_from_top1_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_042_sharesbas_share_of_growth_from_top1_d2}, 'f26_drtj_043_sharesbas_share_of_growth_from_top3_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_043_sharesbas_share_of_growth_from_top3_d2}, 'f26_drtj_044_sharesbas_diffusion_index_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_044_sharesbas_diffusion_index_8q_d2}, 'f26_drtj_045_sharesbas_diffusion_index_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_045_sharesbas_diffusion_index_12q_d2}, 'f26_drtj_046_dilution_vs_revenue_growth_yoy_d2': {'inputs': ['sharesbas', 'revenue'], 'func': f26_drtj_046_dilution_vs_revenue_growth_yoy_d2}, 'f26_drtj_047_dilution_vs_revenue_growth_8q_d2': {'inputs': ['sharesbas', 'revenue'], 'func': f26_drtj_047_dilution_vs_revenue_growth_8q_d2}, 'f26_drtj_048_dilution_per_dollar_revenue_growth_d2': {'inputs': ['sharesbas', 'revenue'], 'func': f26_drtj_048_dilution_per_dollar_revenue_growth_d2}, 'f26_drtj_049_sharesbas_growth_vs_equity_growth_yoy_d2': {'inputs': ['sharesbas', 'equity'], 'func': f26_drtj_049_sharesbas_growth_vs_equity_growth_yoy_d2}, 'f26_drtj_050_sharesbas_growth_vs_assets_growth_yoy_d2': {'inputs': ['sharesbas', 'assets'], 'func': f26_drtj_050_sharesbas_growth_vs_assets_growth_yoy_d2}, 'f26_drtj_051_sharesbas_growth_vs_fcf_yoy_d2': {'inputs': ['sharesbas', 'fcf'], 'func': f26_drtj_051_sharesbas_growth_vs_fcf_yoy_d2}, 'f26_drtj_052_ncfcommon_to_marketcap_ttm_d2': {'inputs': ['ncfcommon', 'marketcap'], 'func': f26_drtj_052_ncfcommon_to_marketcap_ttm_d2}, 'f26_drtj_053_ncfcommon_to_marketcap_yoy_d2': {'inputs': ['ncfcommon', 'marketcap'], 'func': f26_drtj_053_ncfcommon_to_marketcap_yoy_d2}, 'f26_drtj_054_ncfcommon_positive_quarters_count_8q_d2': {'inputs': ['ncfcommon'], 'func': f26_drtj_054_ncfcommon_positive_quarters_count_8q_d2}, 'f26_drtj_055_ncfcommon_positive_streak_d2': {'inputs': ['ncfcommon'], 'func': f26_drtj_055_ncfcommon_positive_streak_d2}, 'f26_drtj_056_ncfcommon_avg_8q_d2': {'inputs': ['ncfcommon'], 'func': f26_drtj_056_ncfcommon_avg_8q_d2}, 'f26_drtj_057_ncfcommon_to_equity_8q_d2': {'inputs': ['ncfcommon', 'equity'], 'func': f26_drtj_057_ncfcommon_to_equity_8q_d2}, 'f26_drtj_058_ncfcommon_growth_yoy_d2': {'inputs': ['ncfcommon'], 'func': f26_drtj_058_ncfcommon_growth_yoy_d2}, 'f26_drtj_059_ncfcommon_minus_ncfdiv_ttm_d2': {'inputs': ['ncfcommon', 'ncfdiv'], 'func': f26_drtj_059_ncfcommon_minus_ncfdiv_ttm_d2}, 'f26_drtj_060_ncfcommon_to_assets_ttm_d2': {'inputs': ['ncfcommon', 'assets'], 'func': f26_drtj_060_ncfcommon_to_assets_ttm_d2}, 'f26_drtj_061_sharesbas_zscore_4q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_061_sharesbas_zscore_4q_d2}, 'f26_drtj_062_sharesbas_qoq_zscore_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_062_sharesbas_qoq_zscore_8q_d2}, 'f26_drtj_063_sharesbas_qoq_zscore_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_063_sharesbas_qoq_zscore_12q_d2}, 'f26_drtj_064_sharesbas_growth_z_minus_mean_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_064_sharesbas_growth_z_minus_mean_8q_d2}, 'f26_drtj_065_sharesbas_acceleration_signal_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_065_sharesbas_acceleration_signal_8q_d2}, 'f26_drtj_066_sharesbas_above_trend_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_066_sharesbas_above_trend_8q_d2}, 'f26_drtj_067_sharesbas_above_trend_zscore_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_067_sharesbas_above_trend_zscore_8q_d2}, 'f26_drtj_068_sharesbas_residual_to_trend_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_068_sharesbas_residual_to_trend_8q_d2}, 'f26_drtj_069_sharesbas_growth_persistence_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_069_sharesbas_growth_persistence_8q_d2}, 'f26_drtj_070_sharesbas_dilution_intensity_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_070_sharesbas_dilution_intensity_8q_d2}, 'f26_drtj_071_sharesbas_growth_dispersion_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_071_sharesbas_growth_dispersion_8q_d2}, 'f26_drtj_072_sharesbas_growth_dispersion_12q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_072_sharesbas_growth_dispersion_12q_d2}, 'f26_drtj_073_sharesbas_growth_range_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_073_sharesbas_growth_range_8q_d2}, 'f26_drtj_074_sharesbas_dilution_streak_length_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_074_sharesbas_dilution_streak_length_d2}, 'f26_drtj_075_sharesbas_clean_quarter_ratio_8q_d2': {'inputs': ['sharesbas'], 'func': f26_drtj_075_sharesbas_clean_quarter_ratio_8q_d2}}