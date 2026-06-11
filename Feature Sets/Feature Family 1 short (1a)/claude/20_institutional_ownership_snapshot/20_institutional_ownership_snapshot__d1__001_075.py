"""institutional_ownership_snapshot d1 features 001-075 — first-derivative wrappers.

Each function inlines the corresponding base computation and appends .diff() to
produce the quarter-over-quarter change of that signal. Inputs and PIT discipline
are identical to __base__001_075.py.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _qoq_pct(s):
    prev = s.shift(1)
    return _safe_div(s - prev, prev.abs())


def _yoy_pct(s):
    prev = s.shift(4)
    return _safe_div(s - prev, prev.abs())


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


def _rolling_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            valid = w[~np.isnan(w)]
            if len(valid) < min_periods:
                return np.nan
            last = w[-1]
            if np.isnan(last):
                return np.nan
            return float((valid <= last).sum() - 1) / max(len(valid) - 1, 1)
        last = w[-1]
        return float((w <= last).sum() - 1) / max(len(w) - 1, 1)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


# ============================================================
#                    D1 FEATURES 001-075
# ============================================================

def f20_iosp_001_inst_pct_of_float_d1(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(inst_units, sharesbas).diff()


def f20_iosp_002_inst_value_to_marketcap_d1(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    return _safe_div(inst_value, marketcap).diff()


def f20_iosp_003_log_inst_investors_d1(inst_investors: pd.Series) -> pd.Series:
    return _safe_log(inst_investors).diff()


def f20_iosp_004_avg_position_value_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    return _safe_div(inst_value, inst_investors).diff()


def f20_iosp_005_avg_position_units_d1(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    return _safe_div(inst_units, inst_investors).diff()


def f20_iosp_006_log_avg_position_value_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    return _safe_log(_safe_div(inst_value, inst_investors)).diff()


def f20_iosp_007_inst_units_per_million_shares_outstanding_d1(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(inst_units, sharesbas / 1.0e6).diff()


def f20_iosp_008_holder_density_log_d1(inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    return (_safe_log(inst_investors) - _safe_log(marketcap)).diff()


def f20_iosp_009_inverse_sqrt_investors_d1(inst_investors: pd.Series) -> pd.Series:
    s = inst_investors.where(inst_investors > 0, np.nan)
    return (1.0 / np.sqrt(s)).diff()


def f20_iosp_010_inst_pct_diluted_d1(inst_units: pd.Series, shareswadil: pd.Series) -> pd.Series:
    return _safe_div(inst_units, shareswadil).diff()


def f20_iosp_011_avg_position_value_zscore_8q_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return _rolling_zscore(avg, 8).diff()


def f20_iosp_012_log_inst_total_value_d1(inst_value: pd.Series) -> pd.Series:
    return _safe_log(inst_value).diff()


def f20_iosp_013_log_inst_total_units_d1(inst_units: pd.Series) -> pd.Series:
    return _safe_log(inst_units).diff()


def f20_iosp_014_underownership_gap_50pct_d1(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pct = _safe_div(inst_units, sharesbas)
    return (0.5 - pct).clip(lower=0.0).diff()


def f20_iosp_015_inst_pct_capped_99_d1(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pct = _safe_div(inst_units, sharesbas)
    return pct.clip(upper=0.99).diff()


def f20_iosp_016_inst_pct_of_basic_shares_d1(inst_units: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_div(inst_units, shareswa).diff()


def f20_iosp_017_value_units_implied_price_d1(inst_value: pd.Series, inst_units: pd.Series) -> pd.Series:
    return _safe_div(inst_value, inst_units).diff()


def f20_iosp_018_implied_price_to_close_ratio_d1(inst_value: pd.Series, inst_units: pd.Series, close: pd.Series) -> pd.Series:
    impl = _safe_div(inst_value, inst_units)
    return _safe_div(impl, close).diff()


def f20_iosp_019_inst_value_per_share_outstanding_d1(inst_value: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(inst_value, sharesbas).diff()


def f20_iosp_020_inst_pct_8q_rank_d1(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pct = _safe_div(inst_units, sharesbas)
    return _rolling_rank(pct, 8).diff()


def f20_iosp_021_inst_units_qoq_pct_d1(inst_units: pd.Series) -> pd.Series:
    return _qoq_pct(inst_units).diff()


def f20_iosp_022_inst_units_yoy_pct_d1(inst_units: pd.Series) -> pd.Series:
    return _yoy_pct(inst_units).diff()


def f20_iosp_023_inst_units_2y_pct_d1(inst_units: pd.Series) -> pd.Series:
    prev = inst_units.shift(8)
    return _safe_div(inst_units - prev, prev.abs()).diff()


def f20_iosp_024_inst_units_3y_pct_d1(inst_units: pd.Series) -> pd.Series:
    prev = inst_units.shift(12)
    return _safe_div(inst_units - prev, prev.abs()).diff()


def f20_iosp_025_inst_units_qoq_signed_diff_d1(inst_units: pd.Series) -> pd.Series:
    return inst_units.diff().diff()


def f20_iosp_026_inst_units_yoy_signed_diff_d1(inst_units: pd.Series) -> pd.Series:
    return inst_units.diff(4).diff()


def f20_iosp_027_inst_investors_qoq_pct_d1(inst_investors: pd.Series) -> pd.Series:
    return _qoq_pct(inst_investors).diff()


def f20_iosp_028_inst_investors_yoy_pct_d1(inst_investors: pd.Series) -> pd.Series:
    return _yoy_pct(inst_investors).diff()


def f20_iosp_029_inst_investors_qoq_signed_diff_d1(inst_investors: pd.Series) -> pd.Series:
    return inst_investors.diff().diff()


def f20_iosp_030_inst_investors_yoy_signed_diff_d1(inst_investors: pd.Series) -> pd.Series:
    return inst_investors.diff(4).diff()


def f20_iosp_031_inst_investors_2y_signed_diff_d1(inst_investors: pd.Series) -> pd.Series:
    return inst_investors.diff(8).diff()


def f20_iosp_032_inst_value_qoq_pct_d1(inst_value: pd.Series) -> pd.Series:
    return _qoq_pct(inst_value).diff()


def f20_iosp_033_inst_value_yoy_pct_d1(inst_value: pd.Series) -> pd.Series:
    return _yoy_pct(inst_value).diff()


def f20_iosp_034_inst_value_qoq_signed_diff_d1(inst_value: pd.Series) -> pd.Series:
    return inst_value.diff().diff()


def f20_iosp_035_inst_value_yoy_signed_diff_d1(inst_value: pd.Series) -> pd.Series:
    return inst_value.diff(4).diff()


def f20_iosp_036_avg_position_value_qoq_pct_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return _qoq_pct(avg).diff()


def f20_iosp_037_avg_position_value_yoy_pct_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return _yoy_pct(avg).diff()


def f20_iosp_038_avg_position_units_qoq_pct_d1(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_units, inst_investors)
    return _qoq_pct(avg).diff()


def f20_iosp_039_avg_position_units_yoy_pct_d1(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_units, inst_investors)
    return _yoy_pct(avg).diff()


def f20_iosp_040_cumulative_4q_inst_units_change_pct_d1(inst_units: pd.Series) -> pd.Series:
    prev = inst_units.shift(4)
    return _safe_div(inst_units - prev, prev.abs()).diff()


def f20_iosp_041_cumulative_4q_inst_investors_change_pct_d1(inst_investors: pd.Series) -> pd.Series:
    prev = inst_investors.shift(4)
    return _safe_div(inst_investors - prev, prev.abs()).diff()


def f20_iosp_042_inst_units_8q_slope_zscored_d1(inst_units: pd.Series) -> pd.Series:
    slope = _rolling_slope(inst_units, 8)
    sd = inst_units.rolling(8, min_periods=3).std()
    return (slope / sd.replace(0, np.nan)).diff()


def f20_iosp_043_inst_investors_8q_slope_zscored_d1(inst_investors: pd.Series) -> pd.Series:
    slope = _rolling_slope(inst_investors, 8)
    sd = inst_investors.rolling(8, min_periods=3).std()
    return (slope / sd.replace(0, np.nan)).diff()


def f20_iosp_044_inst_units_flow_acceleration_d1(inst_units: pd.Series) -> pd.Series:
    return inst_units.diff().diff().diff()


def f20_iosp_045_inst_investors_flow_acceleration_d1(inst_investors: pd.Series) -> pd.Series:
    return inst_investors.diff().diff().diff()


def f20_iosp_046_avg_position_value_qoq_change_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return avg.diff().diff()


def f20_iosp_047_avg_position_value_yoy_change_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return avg.diff(4).diff()


def f20_iosp_048_position_size_intensity_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return _safe_div(avg, marketcap).diff()


def f20_iosp_049_position_size_intensity_qoq_pct_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _qoq_pct(ints).diff()


def f20_iosp_050_position_size_intensity_yoy_pct_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _yoy_pct(ints).diff()


def f20_iosp_051_herfindahl_concentration_proxy_4q_mean_d1(inst_investors: pd.Series) -> pd.Series:
    inv = 1.0 / inst_investors.where(inst_investors > 0, np.nan)
    return inv.rolling(4, min_periods=2).mean().diff()


def f20_iosp_052_log_position_size_zscore_8q_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    lp = _safe_log(_safe_div(inst_value, inst_investors))
    return _rolling_zscore(lp, 8).diff()


def f20_iosp_053_position_size_intensity_4q_mean_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return ints.rolling(4, min_periods=2).mean().diff()


def f20_iosp_054_avg_position_value_zscore_12q_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return _rolling_zscore(avg, 12).diff()


def f20_iosp_055_avg_position_units_zscore_8q_d1(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_units, inst_investors)
    return _rolling_zscore(avg, 8).diff()


def f20_iosp_056_position_value_volatility_8q_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    q = _qoq_pct(avg)
    return q.rolling(8, min_periods=3).std().diff()


def f20_iosp_057_position_count_volatility_8q_d1(inst_investors: pd.Series) -> pd.Series:
    q = _qoq_pct(inst_investors)
    return q.rolling(8, min_periods=3).std().diff()


def f20_iosp_058_concentration_acceleration_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return ints.diff().diff().diff()


def f20_iosp_059_concentration_4q_slope_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _rolling_slope(ints, 4).diff()


def f20_iosp_060_dispersion_divergence_sign_d1(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    return (np.sign(avg.diff()) - np.sign(inst_investors.diff())).diff()


def f20_iosp_061_positioncount_to_marketcap_log_d1(inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    return (_safe_log(inst_investors) - _safe_log(marketcap)).diff()


def f20_iosp_062_units_to_value_ratio_zscore_8q_d1(inst_units: pd.Series, inst_value: pd.Series) -> pd.Series:
    ratio = _safe_div(inst_units, inst_value)
    return _rolling_zscore(ratio, 8).diff()


def f20_iosp_063_liquidity_burden_per_holder_d1(inst_units: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    per_holder = _safe_div(inst_units, inst_investors)
    return _safe_div(per_holder, _safe_log(marketcap)).diff()


def f20_iosp_064_ownership_concentration_index_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    return _safe_div(inst_value, inst_investors * marketcap).diff()


def f20_iosp_065_concentration_8q_trend_slope_d1(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _rolling_slope(ints, 8).diff()


def f20_iosp_066_inst_call_to_units_ratio_d1(inst_calls: pd.Series, inst_units: pd.Series) -> pd.Series:
    return _safe_div(inst_calls, inst_units).diff()


def f20_iosp_067_inst_put_to_units_ratio_d1(inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    return _safe_div(inst_puts, inst_units).diff()


def f20_iosp_068_inst_put_call_skew_d1(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    return _safe_div(inst_puts - inst_calls, inst_puts + inst_calls).diff()


def f20_iosp_069_inst_put_call_skew_qoq_change_d1(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return skew.diff().diff()


def f20_iosp_070_inst_put_call_skew_yoy_change_d1(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return skew.diff(4).diff()


def f20_iosp_071_total_options_intensity_d1(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    return _safe_div(inst_calls + inst_puts, inst_units).diff()


def f20_iosp_072_total_options_intensity_qoq_pct_d1(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    ints = _safe_div(inst_calls + inst_puts, inst_units)
    return _qoq_pct(ints).diff()


def f20_iosp_073_total_options_intensity_yoy_pct_d1(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    ints = _safe_div(inst_calls + inst_puts, inst_units)
    return _yoy_pct(ints).diff()


def f20_iosp_074_options_to_value_ratio_d1(inst_calls: pd.Series, inst_puts: pd.Series, inst_value: pd.Series) -> pd.Series:
    return _safe_div(inst_calls + inst_puts, inst_value).diff()


def f20_iosp_075_inst_calls_qoq_pct_d1(inst_calls: pd.Series) -> pd.Series:
    return _qoq_pct(inst_calls).diff()


# ============================================================
#                        REGISTRY
# ============================================================

INSTITUTIONAL_OWNERSHIP_SNAPSHOT_D1_REGISTRY_001_075 = {
    "f20_iosp_001_inst_pct_of_float_d1": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_001_inst_pct_of_float_d1},
    "f20_iosp_002_inst_value_to_marketcap_d1": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_002_inst_value_to_marketcap_d1},
    "f20_iosp_003_log_inst_investors_d1": {"inputs": ["inst_investors"], "func": f20_iosp_003_log_inst_investors_d1},
    "f20_iosp_004_avg_position_value_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_004_avg_position_value_d1},
    "f20_iosp_005_avg_position_units_d1": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_005_avg_position_units_d1},
    "f20_iosp_006_log_avg_position_value_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_006_log_avg_position_value_d1},
    "f20_iosp_007_inst_units_per_million_shares_outstanding_d1": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_007_inst_units_per_million_shares_outstanding_d1},
    "f20_iosp_008_holder_density_log_d1": {"inputs": ["inst_investors", "marketcap"], "func": f20_iosp_008_holder_density_log_d1},
    "f20_iosp_009_inverse_sqrt_investors_d1": {"inputs": ["inst_investors"], "func": f20_iosp_009_inverse_sqrt_investors_d1},
    "f20_iosp_010_inst_pct_diluted_d1": {"inputs": ["inst_units", "shareswadil"], "func": f20_iosp_010_inst_pct_diluted_d1},
    "f20_iosp_011_avg_position_value_zscore_8q_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_011_avg_position_value_zscore_8q_d1},
    "f20_iosp_012_log_inst_total_value_d1": {"inputs": ["inst_value"], "func": f20_iosp_012_log_inst_total_value_d1},
    "f20_iosp_013_log_inst_total_units_d1": {"inputs": ["inst_units"], "func": f20_iosp_013_log_inst_total_units_d1},
    "f20_iosp_014_underownership_gap_50pct_d1": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_014_underownership_gap_50pct_d1},
    "f20_iosp_015_inst_pct_capped_99_d1": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_015_inst_pct_capped_99_d1},
    "f20_iosp_016_inst_pct_of_basic_shares_d1": {"inputs": ["inst_units", "shareswa"], "func": f20_iosp_016_inst_pct_of_basic_shares_d1},
    "f20_iosp_017_value_units_implied_price_d1": {"inputs": ["inst_value", "inst_units"], "func": f20_iosp_017_value_units_implied_price_d1},
    "f20_iosp_018_implied_price_to_close_ratio_d1": {"inputs": ["inst_value", "inst_units", "close"], "func": f20_iosp_018_implied_price_to_close_ratio_d1},
    "f20_iosp_019_inst_value_per_share_outstanding_d1": {"inputs": ["inst_value", "sharesbas"], "func": f20_iosp_019_inst_value_per_share_outstanding_d1},
    "f20_iosp_020_inst_pct_8q_rank_d1": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_020_inst_pct_8q_rank_d1},
    "f20_iosp_021_inst_units_qoq_pct_d1": {"inputs": ["inst_units"], "func": f20_iosp_021_inst_units_qoq_pct_d1},
    "f20_iosp_022_inst_units_yoy_pct_d1": {"inputs": ["inst_units"], "func": f20_iosp_022_inst_units_yoy_pct_d1},
    "f20_iosp_023_inst_units_2y_pct_d1": {"inputs": ["inst_units"], "func": f20_iosp_023_inst_units_2y_pct_d1},
    "f20_iosp_024_inst_units_3y_pct_d1": {"inputs": ["inst_units"], "func": f20_iosp_024_inst_units_3y_pct_d1},
    "f20_iosp_025_inst_units_qoq_signed_diff_d1": {"inputs": ["inst_units"], "func": f20_iosp_025_inst_units_qoq_signed_diff_d1},
    "f20_iosp_026_inst_units_yoy_signed_diff_d1": {"inputs": ["inst_units"], "func": f20_iosp_026_inst_units_yoy_signed_diff_d1},
    "f20_iosp_027_inst_investors_qoq_pct_d1": {"inputs": ["inst_investors"], "func": f20_iosp_027_inst_investors_qoq_pct_d1},
    "f20_iosp_028_inst_investors_yoy_pct_d1": {"inputs": ["inst_investors"], "func": f20_iosp_028_inst_investors_yoy_pct_d1},
    "f20_iosp_029_inst_investors_qoq_signed_diff_d1": {"inputs": ["inst_investors"], "func": f20_iosp_029_inst_investors_qoq_signed_diff_d1},
    "f20_iosp_030_inst_investors_yoy_signed_diff_d1": {"inputs": ["inst_investors"], "func": f20_iosp_030_inst_investors_yoy_signed_diff_d1},
    "f20_iosp_031_inst_investors_2y_signed_diff_d1": {"inputs": ["inst_investors"], "func": f20_iosp_031_inst_investors_2y_signed_diff_d1},
    "f20_iosp_032_inst_value_qoq_pct_d1": {"inputs": ["inst_value"], "func": f20_iosp_032_inst_value_qoq_pct_d1},
    "f20_iosp_033_inst_value_yoy_pct_d1": {"inputs": ["inst_value"], "func": f20_iosp_033_inst_value_yoy_pct_d1},
    "f20_iosp_034_inst_value_qoq_signed_diff_d1": {"inputs": ["inst_value"], "func": f20_iosp_034_inst_value_qoq_signed_diff_d1},
    "f20_iosp_035_inst_value_yoy_signed_diff_d1": {"inputs": ["inst_value"], "func": f20_iosp_035_inst_value_yoy_signed_diff_d1},
    "f20_iosp_036_avg_position_value_qoq_pct_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_036_avg_position_value_qoq_pct_d1},
    "f20_iosp_037_avg_position_value_yoy_pct_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_037_avg_position_value_yoy_pct_d1},
    "f20_iosp_038_avg_position_units_qoq_pct_d1": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_038_avg_position_units_qoq_pct_d1},
    "f20_iosp_039_avg_position_units_yoy_pct_d1": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_039_avg_position_units_yoy_pct_d1},
    "f20_iosp_040_cumulative_4q_inst_units_change_pct_d1": {"inputs": ["inst_units"], "func": f20_iosp_040_cumulative_4q_inst_units_change_pct_d1},
    "f20_iosp_041_cumulative_4q_inst_investors_change_pct_d1": {"inputs": ["inst_investors"], "func": f20_iosp_041_cumulative_4q_inst_investors_change_pct_d1},
    "f20_iosp_042_inst_units_8q_slope_zscored_d1": {"inputs": ["inst_units"], "func": f20_iosp_042_inst_units_8q_slope_zscored_d1},
    "f20_iosp_043_inst_investors_8q_slope_zscored_d1": {"inputs": ["inst_investors"], "func": f20_iosp_043_inst_investors_8q_slope_zscored_d1},
    "f20_iosp_044_inst_units_flow_acceleration_d1": {"inputs": ["inst_units"], "func": f20_iosp_044_inst_units_flow_acceleration_d1},
    "f20_iosp_045_inst_investors_flow_acceleration_d1": {"inputs": ["inst_investors"], "func": f20_iosp_045_inst_investors_flow_acceleration_d1},
    "f20_iosp_046_avg_position_value_qoq_change_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_046_avg_position_value_qoq_change_d1},
    "f20_iosp_047_avg_position_value_yoy_change_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_047_avg_position_value_yoy_change_d1},
    "f20_iosp_048_position_size_intensity_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_048_position_size_intensity_d1},
    "f20_iosp_049_position_size_intensity_qoq_pct_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_049_position_size_intensity_qoq_pct_d1},
    "f20_iosp_050_position_size_intensity_yoy_pct_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_050_position_size_intensity_yoy_pct_d1},
    "f20_iosp_051_herfindahl_concentration_proxy_4q_mean_d1": {"inputs": ["inst_investors"], "func": f20_iosp_051_herfindahl_concentration_proxy_4q_mean_d1},
    "f20_iosp_052_log_position_size_zscore_8q_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_052_log_position_size_zscore_8q_d1},
    "f20_iosp_053_position_size_intensity_4q_mean_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_053_position_size_intensity_4q_mean_d1},
    "f20_iosp_054_avg_position_value_zscore_12q_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_054_avg_position_value_zscore_12q_d1},
    "f20_iosp_055_avg_position_units_zscore_8q_d1": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_055_avg_position_units_zscore_8q_d1},
    "f20_iosp_056_position_value_volatility_8q_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_056_position_value_volatility_8q_d1},
    "f20_iosp_057_position_count_volatility_8q_d1": {"inputs": ["inst_investors"], "func": f20_iosp_057_position_count_volatility_8q_d1},
    "f20_iosp_058_concentration_acceleration_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_058_concentration_acceleration_d1},
    "f20_iosp_059_concentration_4q_slope_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_059_concentration_4q_slope_d1},
    "f20_iosp_060_dispersion_divergence_sign_d1": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_060_dispersion_divergence_sign_d1},
    "f20_iosp_061_positioncount_to_marketcap_log_d1": {"inputs": ["inst_investors", "marketcap"], "func": f20_iosp_061_positioncount_to_marketcap_log_d1},
    "f20_iosp_062_units_to_value_ratio_zscore_8q_d1": {"inputs": ["inst_units", "inst_value"], "func": f20_iosp_062_units_to_value_ratio_zscore_8q_d1},
    "f20_iosp_063_liquidity_burden_per_holder_d1": {"inputs": ["inst_units", "inst_investors", "marketcap"], "func": f20_iosp_063_liquidity_burden_per_holder_d1},
    "f20_iosp_064_ownership_concentration_index_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_064_ownership_concentration_index_d1},
    "f20_iosp_065_concentration_8q_trend_slope_d1": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_065_concentration_8q_trend_slope_d1},
    "f20_iosp_066_inst_call_to_units_ratio_d1": {"inputs": ["inst_calls", "inst_units"], "func": f20_iosp_066_inst_call_to_units_ratio_d1},
    "f20_iosp_067_inst_put_to_units_ratio_d1": {"inputs": ["inst_puts", "inst_units"], "func": f20_iosp_067_inst_put_to_units_ratio_d1},
    "f20_iosp_068_inst_put_call_skew_d1": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_068_inst_put_call_skew_d1},
    "f20_iosp_069_inst_put_call_skew_qoq_change_d1": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_069_inst_put_call_skew_qoq_change_d1},
    "f20_iosp_070_inst_put_call_skew_yoy_change_d1": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_070_inst_put_call_skew_yoy_change_d1},
    "f20_iosp_071_total_options_intensity_d1": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_071_total_options_intensity_d1},
    "f20_iosp_072_total_options_intensity_qoq_pct_d1": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_072_total_options_intensity_qoq_pct_d1},
    "f20_iosp_073_total_options_intensity_yoy_pct_d1": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_073_total_options_intensity_yoy_pct_d1},
    "f20_iosp_074_options_to_value_ratio_d1": {"inputs": ["inst_calls", "inst_puts", "inst_value"], "func": f20_iosp_074_options_to_value_ratio_d1},
    "f20_iosp_075_inst_calls_qoq_pct_d1": {"inputs": ["inst_calls"], "func": f20_iosp_075_inst_calls_qoq_pct_d1},
}
