"""insider_activity_snapshot d3 features 001_075 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_log_signed(s):
    """Log of |s|+1 with sign — for net-flow series that cross zero."""
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

def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _days_since_min(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmin(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _streak_above_zero(flag_series, window, min_periods=None):
    """Current consecutive-bar streak of flag>0 within rolling window."""
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

def _recency_since_event(flag_series, window, min_periods=None):
    """Bars since the last event (flag>0) within window; returns window length if none."""
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

def f18_iasp_001_insider_net_value_zscore_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_net_value, YDAYS).diff().diff().diff()

def f18_iasp_002_insider_net_value_zscore_63d_d3(insider_net_value: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_net_value, QDAYS).diff().diff().diff()

def f18_iasp_003_insider_net_value_rank_pct_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    return _rolling_rank_pct(insider_net_value, YDAYS).diff().diff().diff()

def f18_iasp_004_insider_net_value_sum_21d_d3(insider_net_value: pd.Series) -> pd.Series:
    return insider_net_value.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f18_iasp_005_insider_net_value_sum_63d_d3(insider_net_value: pd.Series) -> pd.Series:
    return insider_net_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_006_insider_net_value_sum_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    return insider_net_value.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_007_insider_net_value_sum_21d_zscore_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    s21 = insider_net_value.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(s21, YDAYS).diff().diff().diff()

def f18_iasp_008_insider_net_value_sum_63d_zscore_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    s63 = insider_net_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(s63, YDAYS).diff().diff().diff()

def f18_iasp_009_insider_net_value_sum_63d_minus_252d_baseline_d3(insider_net_value: pd.Series) -> pd.Series:
    s63 = insider_net_value.rolling(QDAYS, min_periods=MDAYS).sum()
    s252 = insider_net_value.rolling(YDAYS, min_periods=QDAYS).sum()
    return (s63 - s252 * (QDAYS / YDAYS)).diff().diff().diff()

def f18_iasp_010_insider_net_value_log_sign_intensity_63d_d3(insider_net_value: pd.Series) -> pd.Series:
    sg = _safe_log_signed(insider_net_value)
    return sg.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_011_insider_net_shares_sum_21d_d3(insider_net_shares: pd.Series) -> pd.Series:
    return insider_net_shares.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f18_iasp_012_insider_net_shares_sum_63d_d3(insider_net_shares: pd.Series) -> pd.Series:
    return insider_net_shares.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_013_insider_net_shares_sum_252d_d3(insider_net_shares: pd.Series) -> pd.Series:
    return insider_net_shares.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_014_insider_net_shares_sum_21d_zscore_252d_d3(insider_net_shares: pd.Series) -> pd.Series:
    s21 = insider_net_shares.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(s21, YDAYS).diff().diff().diff()

def f18_iasp_015_insider_net_shares_rank_pct_252d_d3(insider_net_shares: pd.Series) -> pd.Series:
    return _rolling_rank_pct(insider_net_shares, YDAYS).diff().diff().diff()

def f18_iasp_016_net_flow_negative_days_count_63d_d3(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value < 0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_017_net_flow_negative_days_count_252d_d3(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value < 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_018_net_flow_negative_days_streak_d3(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value < 0).astype(int)
    return _streak_above_zero(flag, QDAYS).diff().diff().diff()

def f18_iasp_019_net_flow_pct_of_days_with_activity_63d_d3(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value != 0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f18_iasp_020_insider_net_value_log_diff_21d_d3(insider_net_value: pd.Series) -> pd.Series:
    return _safe_log_signed(insider_net_value).diff(MDAYS).diff().diff().diff()

def f18_iasp_021_insider_sell_value_zscore_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_022_insider_sell_value_sum_21d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return insider_sell_value.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f18_iasp_023_insider_sell_value_sum_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_024_insider_sell_value_sum_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return insider_sell_value.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_025_insider_sell_value_top_decile_count_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (insider_sell_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_026_insider_sell_value_p99_count_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (insider_sell_value >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_027_insider_sell_value_days_above_p90_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    thr = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    flag = (insider_sell_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_028_insider_sell_value_log_diff_21d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return _safe_log(insider_sell_value).diff(MDAYS).diff().diff().diff()

def f18_iasp_029_insider_sell_value_log_diff_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return _safe_log(insider_sell_value).diff(QDAYS).diff().diff().diff()

def f18_iasp_030_insider_sell_value_max_single_day_252d_log_ratio_d3(insider_sell_value: pd.Series) -> pd.Series:
    mx = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).max()
    med = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_log(_safe_div(mx, med)).diff().diff().diff()

def f18_iasp_031_insider_sell_shares_sum_63d_d3(insider_sell_shares: pd.Series) -> pd.Series:
    return insider_sell_shares.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_032_insider_sell_shares_zscore_252d_d3(insider_sell_shares: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_sell_shares, YDAYS).diff().diff().diff()

def f18_iasp_033_insider_sell_count_sum_63d_d3(insider_sell_count: pd.Series) -> pd.Series:
    return insider_sell_count.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_034_insider_sell_count_zscore_252d_d3(insider_sell_count: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_sell_count, YDAYS).diff().diff().diff()

def f18_iasp_035_insider_sell_count_top_decile_count_63d_d3(insider_sell_count: pd.Series) -> pd.Series:
    thr = insider_sell_count.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (insider_sell_count >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_036_insider_sell_count_streak_above_p75_252d_d3(insider_sell_count: pd.Series) -> pd.Series:
    thr = insider_sell_count.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    flag = (insider_sell_count > thr).astype(int)
    return _streak_above_zero(flag, QDAYS).diff().diff().diff()

def f18_iasp_037_days_since_largest_sell_value_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return _days_since_max(insider_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_038_sell_value_to_sma_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    sma = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(insider_sell_value, sma).diff().diff().diff()

def f18_iasp_039_sell_value_to_sma_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    sma = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(insider_sell_value, sma).diff().diff().diff()

def f18_iasp_040_sell_value_share_of_top5_days_in_63d_d3(insider_sell_value: pd.Series) -> pd.Series:

    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-5:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return insider_sell_value.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True).diff().diff().diff()

def f18_iasp_041_sell_value_pareto_top1_in_252d_d3(insider_sell_value: pd.Series) -> pd.Series:
    mx = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).max()
    tot = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(mx, tot).diff().diff().diff()

def f18_iasp_042_sell_value_acceleration_21d_d3(insider_sell_value: pd.Series) -> pd.Series:
    return _safe_log(insider_sell_value).diff(MDAYS).diff(MDAYS).diff().diff().diff()

def f18_iasp_043_sell_value_z_max_in_63d_d3(insider_sell_value: pd.Series) -> pd.Series:
    z = _rolling_zscore(insider_sell_value, YDAYS)
    return z.rolling(QDAYS, min_periods=MDAYS).max().diff().diff().diff()

def f18_iasp_044_sell_value_skewness_63d_d3(insider_sell_value: pd.Series) -> pd.Series:

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return insider_sell_value.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True).diff().diff().diff()

def f18_iasp_045_sell_value_kurtosis_63d_d3(insider_sell_value: pd.Series) -> pd.Series:

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return insider_sell_value.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True).diff().diff().diff()

def f18_iasp_046_insider_buy_value_zscore_252d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_buy_value, YDAYS).diff().diff().diff()

def f18_iasp_047_insider_buy_value_sum_21d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return insider_buy_value.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f18_iasp_048_insider_buy_value_sum_63d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return insider_buy_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_049_insider_buy_value_sum_252d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return insider_buy_value.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_050_insider_buy_value_log_diff_21d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return _safe_log(insider_buy_value).diff(MDAYS).diff().diff().diff()

def f18_iasp_051_insider_buy_value_log_diff_63d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return _safe_log(insider_buy_value).diff(QDAYS).diff().diff().diff()

def f18_iasp_052_insider_buy_count_sum_63d_d3(insider_buy_count: pd.Series) -> pd.Series:
    return insider_buy_count.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_053_insider_buy_count_zscore_252d_d3(insider_buy_count: pd.Series) -> pd.Series:
    return _rolling_zscore(insider_buy_count, YDAYS).diff().diff().diff()

def f18_iasp_054_days_since_largest_buy_value_252d_d3(insider_buy_value: pd.Series) -> pd.Series:
    return _days_since_max(insider_buy_value, YDAYS).diff().diff().diff()

def f18_iasp_055_buy_value_top_decile_count_63d_d3(insider_buy_value: pd.Series) -> pd.Series:
    thr = insider_buy_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (insider_buy_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_056_buy_to_sell_value_log_ratio_63d_d3(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    b = insider_buy_value.rolling(QDAYS, min_periods=MDAYS).sum()
    s = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_log(_safe_div(b, s)).diff().diff().diff()

def f18_iasp_057_buy_minus_sell_value_zscore_63d_over_252d_d3(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    bms = (insider_buy_value - insider_sell_value).rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(bms, YDAYS).diff().diff().diff()

def f18_iasp_058_days_with_zero_buys_63d_d3(insider_buy_value: pd.Series) -> pd.Series:
    flag = (insider_buy_value.fillna(0) == 0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_059_days_with_zero_buys_252d_d3(insider_buy_value: pd.Series) -> pd.Series:
    flag = (insider_buy_value.fillna(0) == 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f18_iasp_060_buy_dry_up_streak_max_252d_d3(insider_buy_value: pd.Series) -> pd.Series:
    flag = (insider_buy_value.fillna(0) == 0).astype(int)

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
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True).diff().diff().diff()

def f18_iasp_061_ceo_sell_value_zscore_252d_d3(ceo_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(ceo_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_062_ceo_sell_value_sum_63d_d3(ceo_sell_value: pd.Series) -> pd.Series:
    return ceo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_063_ceo_sell_value_above_p90_count_63d_d3(ceo_sell_value: pd.Series) -> pd.Series:
    thr = ceo_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (ceo_sell_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_064_days_since_ceo_sell_event_252d_d3(ceo_sell_value: pd.Series) -> pd.Series:
    flag = (ceo_sell_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff().diff().diff()

def f18_iasp_065_ceo_sell_log_diff_63d_d3(ceo_sell_value: pd.Series) -> pd.Series:
    return _safe_log(ceo_sell_value).diff(QDAYS).diff().diff().diff()

def f18_iasp_066_cfo_sell_value_zscore_252d_d3(cfo_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(cfo_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_067_cfo_sell_value_sum_63d_d3(cfo_sell_value: pd.Series) -> pd.Series:
    return cfo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_068_days_since_cfo_sell_event_252d_d3(cfo_sell_value: pd.Series) -> pd.Series:
    flag = (cfo_sell_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff().diff().diff()

def f18_iasp_069_cfo_sell_log_diff_63d_d3(cfo_sell_value: pd.Series) -> pd.Series:
    return _safe_log(cfo_sell_value).diff(QDAYS).diff().diff().diff()

def f18_iasp_070_officer_sell_value_zscore_252d_d3(officer_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(officer_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_071_officer_sell_value_sum_63d_d3(officer_sell_value: pd.Series) -> pd.Series:
    return officer_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_072_officer_sell_log_diff_63d_d3(officer_sell_value: pd.Series) -> pd.Series:
    return _safe_log(officer_sell_value).diff(QDAYS).diff().diff().diff()

def f18_iasp_073_director_sell_value_zscore_252d_d3(director_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(director_sell_value, YDAYS).diff().diff().diff()

def f18_iasp_074_director_sell_value_sum_63d_d3(director_sell_value: pd.Series) -> pd.Series:
    return director_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f18_iasp_075_director_sell_log_diff_63d_d3(director_sell_value: pd.Series) -> pd.Series:
    return _safe_log(director_sell_value).diff(QDAYS).diff().diff().diff()
INSIDER_ACTIVITY_SNAPSHOT_D3_REGISTRY_001_075 = {'f18_iasp_001_insider_net_value_zscore_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_001_insider_net_value_zscore_252d_d3}, 'f18_iasp_002_insider_net_value_zscore_63d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_002_insider_net_value_zscore_63d_d3}, 'f18_iasp_003_insider_net_value_rank_pct_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_003_insider_net_value_rank_pct_252d_d3}, 'f18_iasp_004_insider_net_value_sum_21d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_004_insider_net_value_sum_21d_d3}, 'f18_iasp_005_insider_net_value_sum_63d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_005_insider_net_value_sum_63d_d3}, 'f18_iasp_006_insider_net_value_sum_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_006_insider_net_value_sum_252d_d3}, 'f18_iasp_007_insider_net_value_sum_21d_zscore_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_007_insider_net_value_sum_21d_zscore_252d_d3}, 'f18_iasp_008_insider_net_value_sum_63d_zscore_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_008_insider_net_value_sum_63d_zscore_252d_d3}, 'f18_iasp_009_insider_net_value_sum_63d_minus_252d_baseline_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_009_insider_net_value_sum_63d_minus_252d_baseline_d3}, 'f18_iasp_010_insider_net_value_log_sign_intensity_63d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_010_insider_net_value_log_sign_intensity_63d_d3}, 'f18_iasp_011_insider_net_shares_sum_21d_d3': {'inputs': ['insider_net_shares'], 'func': f18_iasp_011_insider_net_shares_sum_21d_d3}, 'f18_iasp_012_insider_net_shares_sum_63d_d3': {'inputs': ['insider_net_shares'], 'func': f18_iasp_012_insider_net_shares_sum_63d_d3}, 'f18_iasp_013_insider_net_shares_sum_252d_d3': {'inputs': ['insider_net_shares'], 'func': f18_iasp_013_insider_net_shares_sum_252d_d3}, 'f18_iasp_014_insider_net_shares_sum_21d_zscore_252d_d3': {'inputs': ['insider_net_shares'], 'func': f18_iasp_014_insider_net_shares_sum_21d_zscore_252d_d3}, 'f18_iasp_015_insider_net_shares_rank_pct_252d_d3': {'inputs': ['insider_net_shares'], 'func': f18_iasp_015_insider_net_shares_rank_pct_252d_d3}, 'f18_iasp_016_net_flow_negative_days_count_63d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_016_net_flow_negative_days_count_63d_d3}, 'f18_iasp_017_net_flow_negative_days_count_252d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_017_net_flow_negative_days_count_252d_d3}, 'f18_iasp_018_net_flow_negative_days_streak_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_018_net_flow_negative_days_streak_d3}, 'f18_iasp_019_net_flow_pct_of_days_with_activity_63d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_019_net_flow_pct_of_days_with_activity_63d_d3}, 'f18_iasp_020_insider_net_value_log_diff_21d_d3': {'inputs': ['insider_net_value'], 'func': f18_iasp_020_insider_net_value_log_diff_21d_d3}, 'f18_iasp_021_insider_sell_value_zscore_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_021_insider_sell_value_zscore_252d_d3}, 'f18_iasp_022_insider_sell_value_sum_21d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_022_insider_sell_value_sum_21d_d3}, 'f18_iasp_023_insider_sell_value_sum_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_023_insider_sell_value_sum_63d_d3}, 'f18_iasp_024_insider_sell_value_sum_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_024_insider_sell_value_sum_252d_d3}, 'f18_iasp_025_insider_sell_value_top_decile_count_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_025_insider_sell_value_top_decile_count_63d_d3}, 'f18_iasp_026_insider_sell_value_p99_count_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_026_insider_sell_value_p99_count_252d_d3}, 'f18_iasp_027_insider_sell_value_days_above_p90_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_027_insider_sell_value_days_above_p90_63d_d3}, 'f18_iasp_028_insider_sell_value_log_diff_21d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_028_insider_sell_value_log_diff_21d_d3}, 'f18_iasp_029_insider_sell_value_log_diff_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_029_insider_sell_value_log_diff_63d_d3}, 'f18_iasp_030_insider_sell_value_max_single_day_252d_log_ratio_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_030_insider_sell_value_max_single_day_252d_log_ratio_d3}, 'f18_iasp_031_insider_sell_shares_sum_63d_d3': {'inputs': ['insider_sell_shares'], 'func': f18_iasp_031_insider_sell_shares_sum_63d_d3}, 'f18_iasp_032_insider_sell_shares_zscore_252d_d3': {'inputs': ['insider_sell_shares'], 'func': f18_iasp_032_insider_sell_shares_zscore_252d_d3}, 'f18_iasp_033_insider_sell_count_sum_63d_d3': {'inputs': ['insider_sell_count'], 'func': f18_iasp_033_insider_sell_count_sum_63d_d3}, 'f18_iasp_034_insider_sell_count_zscore_252d_d3': {'inputs': ['insider_sell_count'], 'func': f18_iasp_034_insider_sell_count_zscore_252d_d3}, 'f18_iasp_035_insider_sell_count_top_decile_count_63d_d3': {'inputs': ['insider_sell_count'], 'func': f18_iasp_035_insider_sell_count_top_decile_count_63d_d3}, 'f18_iasp_036_insider_sell_count_streak_above_p75_252d_d3': {'inputs': ['insider_sell_count'], 'func': f18_iasp_036_insider_sell_count_streak_above_p75_252d_d3}, 'f18_iasp_037_days_since_largest_sell_value_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_037_days_since_largest_sell_value_252d_d3}, 'f18_iasp_038_sell_value_to_sma_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_038_sell_value_to_sma_252d_d3}, 'f18_iasp_039_sell_value_to_sma_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_039_sell_value_to_sma_63d_d3}, 'f18_iasp_040_sell_value_share_of_top5_days_in_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_040_sell_value_share_of_top5_days_in_63d_d3}, 'f18_iasp_041_sell_value_pareto_top1_in_252d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_041_sell_value_pareto_top1_in_252d_d3}, 'f18_iasp_042_sell_value_acceleration_21d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_042_sell_value_acceleration_21d_d3}, 'f18_iasp_043_sell_value_z_max_in_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_043_sell_value_z_max_in_63d_d3}, 'f18_iasp_044_sell_value_skewness_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_044_sell_value_skewness_63d_d3}, 'f18_iasp_045_sell_value_kurtosis_63d_d3': {'inputs': ['insider_sell_value'], 'func': f18_iasp_045_sell_value_kurtosis_63d_d3}, 'f18_iasp_046_insider_buy_value_zscore_252d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_046_insider_buy_value_zscore_252d_d3}, 'f18_iasp_047_insider_buy_value_sum_21d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_047_insider_buy_value_sum_21d_d3}, 'f18_iasp_048_insider_buy_value_sum_63d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_048_insider_buy_value_sum_63d_d3}, 'f18_iasp_049_insider_buy_value_sum_252d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_049_insider_buy_value_sum_252d_d3}, 'f18_iasp_050_insider_buy_value_log_diff_21d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_050_insider_buy_value_log_diff_21d_d3}, 'f18_iasp_051_insider_buy_value_log_diff_63d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_051_insider_buy_value_log_diff_63d_d3}, 'f18_iasp_052_insider_buy_count_sum_63d_d3': {'inputs': ['insider_buy_count'], 'func': f18_iasp_052_insider_buy_count_sum_63d_d3}, 'f18_iasp_053_insider_buy_count_zscore_252d_d3': {'inputs': ['insider_buy_count'], 'func': f18_iasp_053_insider_buy_count_zscore_252d_d3}, 'f18_iasp_054_days_since_largest_buy_value_252d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_054_days_since_largest_buy_value_252d_d3}, 'f18_iasp_055_buy_value_top_decile_count_63d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_055_buy_value_top_decile_count_63d_d3}, 'f18_iasp_056_buy_to_sell_value_log_ratio_63d_d3': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f18_iasp_056_buy_to_sell_value_log_ratio_63d_d3}, 'f18_iasp_057_buy_minus_sell_value_zscore_63d_over_252d_d3': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f18_iasp_057_buy_minus_sell_value_zscore_63d_over_252d_d3}, 'f18_iasp_058_days_with_zero_buys_63d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_058_days_with_zero_buys_63d_d3}, 'f18_iasp_059_days_with_zero_buys_252d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_059_days_with_zero_buys_252d_d3}, 'f18_iasp_060_buy_dry_up_streak_max_252d_d3': {'inputs': ['insider_buy_value'], 'func': f18_iasp_060_buy_dry_up_streak_max_252d_d3}, 'f18_iasp_061_ceo_sell_value_zscore_252d_d3': {'inputs': ['ceo_sell_value'], 'func': f18_iasp_061_ceo_sell_value_zscore_252d_d3}, 'f18_iasp_062_ceo_sell_value_sum_63d_d3': {'inputs': ['ceo_sell_value'], 'func': f18_iasp_062_ceo_sell_value_sum_63d_d3}, 'f18_iasp_063_ceo_sell_value_above_p90_count_63d_d3': {'inputs': ['ceo_sell_value'], 'func': f18_iasp_063_ceo_sell_value_above_p90_count_63d_d3}, 'f18_iasp_064_days_since_ceo_sell_event_252d_d3': {'inputs': ['ceo_sell_value'], 'func': f18_iasp_064_days_since_ceo_sell_event_252d_d3}, 'f18_iasp_065_ceo_sell_log_diff_63d_d3': {'inputs': ['ceo_sell_value'], 'func': f18_iasp_065_ceo_sell_log_diff_63d_d3}, 'f18_iasp_066_cfo_sell_value_zscore_252d_d3': {'inputs': ['cfo_sell_value'], 'func': f18_iasp_066_cfo_sell_value_zscore_252d_d3}, 'f18_iasp_067_cfo_sell_value_sum_63d_d3': {'inputs': ['cfo_sell_value'], 'func': f18_iasp_067_cfo_sell_value_sum_63d_d3}, 'f18_iasp_068_days_since_cfo_sell_event_252d_d3': {'inputs': ['cfo_sell_value'], 'func': f18_iasp_068_days_since_cfo_sell_event_252d_d3}, 'f18_iasp_069_cfo_sell_log_diff_63d_d3': {'inputs': ['cfo_sell_value'], 'func': f18_iasp_069_cfo_sell_log_diff_63d_d3}, 'f18_iasp_070_officer_sell_value_zscore_252d_d3': {'inputs': ['officer_sell_value'], 'func': f18_iasp_070_officer_sell_value_zscore_252d_d3}, 'f18_iasp_071_officer_sell_value_sum_63d_d3': {'inputs': ['officer_sell_value'], 'func': f18_iasp_071_officer_sell_value_sum_63d_d3}, 'f18_iasp_072_officer_sell_log_diff_63d_d3': {'inputs': ['officer_sell_value'], 'func': f18_iasp_072_officer_sell_log_diff_63d_d3}, 'f18_iasp_073_director_sell_value_zscore_252d_d3': {'inputs': ['director_sell_value'], 'func': f18_iasp_073_director_sell_value_zscore_252d_d3}, 'f18_iasp_074_director_sell_value_sum_63d_d3': {'inputs': ['director_sell_value'], 'func': f18_iasp_074_director_sell_value_sum_63d_d3}, 'f18_iasp_075_director_sell_log_diff_63d_d3': {'inputs': ['director_sell_value'], 'func': f18_iasp_075_director_sell_log_diff_63d_d3}}
