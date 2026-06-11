"""institutional_holding_collapse_trajectory d1 features 001-075 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

def _runlen_neg(s):
    neg = (s < 0).astype(float)
    grp = (neg != neg.shift()).cumsum()
    return neg.groupby(grp).cumsum() * neg

def f28_ihct_001_inst_holders_qoq_change_d1(inst_holders):
    return inst_holders.diff().diff()

def f28_ihct_002_inst_holders_yoy_change_d1(inst_holders):
    return (inst_holders - inst_holders.shift(4)).diff()

def f28_ihct_003_inst_holders_8q_change_d1(inst_holders):
    return (inst_holders - inst_holders.shift(8)).diff()

def f28_ihct_004_inst_holders_12q_change_d1(inst_holders):
    return (inst_holders - inst_holders.shift(12)).diff()

def f28_ihct_005_inst_holders_qoq_pct_d1(inst_holders):
    return _qoq_pct(inst_holders).diff()

def f28_ihct_006_inst_holders_yoy_pct_d1(inst_holders):
    return _yoy_pct(inst_holders).diff()

def f28_ihct_007_inst_holders_log_diff_4q_d1(inst_holders):
    return (_safe_log(inst_holders) - _safe_log(inst_holders.shift(4))).diff()

def f28_ihct_008_inst_holders_8q_cagr_d1(inst_holders):
    r = _safe_div(inst_holders, inst_holders.shift(8))
    return (r ** 0.5 - 1.0).diff()

def f28_ihct_009_inst_holders_drawdown_8q_d1(inst_holders):
    hi = inst_holders.rolling(8, min_periods=3).max()
    return _safe_div(inst_holders - hi, hi.abs()).diff()

def f28_ihct_010_inst_holders_drawdown_16q_d1(inst_holders):
    hi = inst_holders.rolling(16, min_periods=4).max()
    return _safe_div(inst_holders - hi, hi.abs()).diff()

def f28_ihct_011_inst_holders_below_8q_avg_flag_d1(inst_holders):
    avg = inst_holders.rolling(8, min_periods=3).mean()
    return (inst_holders < avg).astype(float).diff()

def f28_ihct_012_inst_holders_zscore_8q_d1(inst_holders):
    return _rolling_zscore(inst_holders, 8).diff()

def f28_ihct_013_inst_holders_zscore_16q_d1(inst_holders):
    return _rolling_zscore(inst_holders, 16).diff()

def f28_ihct_014_inst_holders_max_minus_now_8q_d1(inst_holders):
    return (inst_holders.rolling(8, min_periods=3).max() - inst_holders).diff()

def f28_ihct_015_inst_holders_consecutive_decline_streak_d1(inst_holders):
    return _runlen_neg(inst_holders.diff()).diff()

def f28_ihct_016_inst_units_qoq_pct_d1(inst_units):
    return _qoq_pct(inst_units).diff()

def f28_ihct_017_inst_units_yoy_pct_d1(inst_units):
    return _yoy_pct(inst_units).diff()

def f28_ihct_018_inst_units_8q_pct_d1(inst_units):
    return _safe_div(inst_units - inst_units.shift(8), inst_units.shift(8).abs()).diff()

def f28_ihct_019_inst_units_drawdown_8q_d1(inst_units):
    hi = inst_units.rolling(8, min_periods=3).max()
    return _safe_div(inst_units - hi, hi.abs()).diff()

def f28_ihct_020_inst_units_drawdown_16q_d1(inst_units):
    hi = inst_units.rolling(16, min_periods=4).max()
    return _safe_div(inst_units - hi, hi.abs()).diff()

def f28_ihct_021_inst_value_qoq_pct_d1(inst_value):
    return _qoq_pct(inst_value).diff()

def f28_ihct_022_inst_value_yoy_pct_d1(inst_value):
    return _yoy_pct(inst_value).diff()

def f28_ihct_023_inst_value_8q_pct_d1(inst_value):
    return _safe_div(inst_value - inst_value.shift(8), inst_value.shift(8).abs()).diff()

def f28_ihct_024_inst_units_log_diff_yoy_d1(inst_units):
    return (_safe_log(inst_units) - _safe_log(inst_units.shift(4))).diff()

def f28_ihct_025_inst_units_acceleration_4q_d1(inst_units):
    return _yoy_pct(inst_units).diff().diff()

def f28_ihct_026_inst_units_consecutive_decline_streak_d1(inst_units):
    return _runlen_neg(inst_units.diff()).diff()

def f28_ihct_027_inst_units_zscore_8q_d1(inst_units):
    return _rolling_zscore(inst_units, 8).diff()

def f28_ihct_028_inst_units_avg_4q_minus_avg_8q_d1(inst_units):
    return (inst_units.rolling(4, min_periods=2).mean() - inst_units.rolling(8, min_periods=3).mean()).diff()

def f28_ihct_029_inst_units_diffusion_8q_d1(inst_units):
    return (inst_units.diff() < 0).astype(float).rolling(8, min_periods=3).mean().diff()

def f28_ihct_030_inst_units_max_drop_4q_d1(inst_units):
    return _qoq_pct(inst_units).rolling(4, min_periods=2).min().diff()

def f28_ihct_031_inst_ownership_pct_qoq_change_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return own.diff().diff()

def f28_ihct_032_inst_ownership_pct_yoy_change_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return (own - own.shift(4)).diff()

def f28_ihct_033_inst_ownership_pct_8q_change_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return (own - own.shift(8)).diff()

def f28_ihct_034_inst_ownership_pct_drawdown_8q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    hi = own.rolling(8, min_periods=3).max()
    return (own - hi).diff()

def f28_ihct_035_inst_ownership_pct_drawdown_16q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    hi = own.rolling(16, min_periods=4).max()
    return (own - hi).diff()

def f28_ihct_036_inst_ownership_pct_zscore_8q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return _rolling_zscore(own, 8).diff()

def f28_ihct_037_inst_ownership_pct_consecutive_decline_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return _runlen_neg(own.diff()).diff()

def f28_ihct_038_inst_ownership_pct_change_minus_buyback_pct_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    share_chg = _qoq_pct(sharesbas)
    return (own.diff() - -share_chg.clip(upper=0)).diff()

def f28_ihct_039_inst_ownership_pct_change_vs_dilution_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    dil = _qoq_pct(sharesbas).clip(lower=0)
    return (own.diff() + dil).diff()

def f28_ihct_040_inst_ownership_pct_below_lt_avg_16q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    avg = own.rolling(16, min_periods=4).mean()
    return (own - avg).diff()

def f28_ihct_041_inst_ownership_pct_chunk_loss_8q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return own.diff().rolling(8, min_periods=3).min().diff()

def f28_ihct_042_inst_ownership_pct_step_decline_8q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    a = own.rolling(4, min_periods=2).mean()
    b = own.shift(4).rolling(4, min_periods=2).mean()
    return (a - b).diff()

def f28_ihct_043_inst_ownership_pct_2yr_decline_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return (own - own.shift(8)).diff()

def f28_ihct_044_inst_ownership_pct_max_drawdown_16q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    hi = own.rolling(16, min_periods=4).max()
    dd = own - hi
    return dd.rolling(16, min_periods=4).min().diff()

def f28_ihct_045_inst_ownership_pct_total_drop_8q_d1(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return own.diff().clip(upper=0).rolling(8, min_periods=3).sum().diff()

def f28_ihct_046_inst_top10_share_qoq_change_d1(inst_top10_share):
    return inst_top10_share.diff().diff()

def f28_ihct_047_inst_top10_share_yoy_change_d1(inst_top10_share):
    return (inst_top10_share - inst_top10_share.shift(4)).diff()

def f28_ihct_048_inst_top5_share_qoq_change_d1(inst_top5_share):
    return inst_top5_share.diff().diff()

def f28_ihct_049_inst_top5_share_yoy_change_d1(inst_top5_share):
    return (inst_top5_share - inst_top5_share.shift(4)).diff()

def f28_ihct_050_inst_top10_share_increasing_flag_d1(inst_top10_share):
    return (inst_top10_share.diff() > 0).astype(float).diff()

def f28_ihct_051_inst_top10_share_growth_8q_d1(inst_top10_share):
    return (inst_top10_share - inst_top10_share.shift(8)).diff()

def f28_ihct_052_inst_top10_share_minus_top5_share_change_d1(inst_top10_share, inst_top5_share):
    diff_share = inst_top10_share - inst_top5_share
    return diff_share.diff(4).diff()

def f28_ihct_053_inst_hhi_qoq_change_d1(inst_concentration_hhi):
    return inst_concentration_hhi.diff().diff()

def f28_ihct_054_inst_hhi_yoy_change_d1(inst_concentration_hhi):
    return (inst_concentration_hhi - inst_concentration_hhi.shift(4)).diff()

def f28_ihct_055_inst_hhi_growth_8q_d1(inst_concentration_hhi):
    return (inst_concentration_hhi - inst_concentration_hhi.shift(8)).diff()

def f28_ihct_056_inst_holders_minus_top10_share_divergence_d1(inst_holders, inst_top10_share):
    return (_yoy_pct(inst_holders) + inst_top10_share.diff(4)).diff()

def f28_ihct_057_inst_concentration_rising_streak_d1(inst_concentration_hhi):
    pos = (inst_concentration_hhi.diff() > 0).astype(float)
    grp = (pos != pos.shift()).cumsum()
    return (pos.groupby(grp).cumsum() * pos).diff()

def f28_ihct_058_inst_avg_position_size_qoq_d1(inst_avg_position_size):
    return _qoq_pct(inst_avg_position_size).diff()

def f28_ihct_059_inst_avg_position_size_yoy_d1(inst_avg_position_size):
    return _yoy_pct(inst_avg_position_size).diff()

def f28_ihct_060_inst_avg_position_size_drawdown_8q_d1(inst_avg_position_size):
    hi = inst_avg_position_size.rolling(8, min_periods=3).max()
    return _safe_div(inst_avg_position_size - hi, hi.abs()).diff()

def f28_ihct_061_inst_inc_count_qoq_change_d1(inst_inc_count):
    return inst_inc_count.diff().diff()

def f28_ihct_062_inst_inc_count_yoy_pct_d1(inst_inc_count):
    return _yoy_pct(inst_inc_count).diff()

def f28_ihct_063_inst_dec_count_qoq_change_d1(inst_dec_count):
    return inst_dec_count.diff().diff()

def f28_ihct_064_inst_dec_count_yoy_pct_d1(inst_dec_count):
    return _yoy_pct(inst_dec_count).diff()

def f28_ihct_065_inst_dec_to_inc_ratio_d1(inst_dec_count, inst_inc_count):
    return _safe_div(inst_dec_count, inst_inc_count).diff()

def f28_ihct_066_inst_dec_to_inc_ratio_qoq_change_d1(inst_dec_count, inst_inc_count):
    return _safe_div(inst_dec_count, inst_inc_count).diff().diff()

def f28_ihct_067_inst_dec_to_inc_ratio_yoy_change_d1(inst_dec_count, inst_inc_count):
    r = _safe_div(inst_dec_count, inst_inc_count)
    return (r - r.shift(4)).diff()

def f28_ihct_068_inst_dec_minus_inc_count_d1(inst_dec_count, inst_inc_count):
    return (inst_dec_count - inst_inc_count).diff()

def f28_ihct_069_inst_dec_minus_inc_count_yoy_d1(inst_dec_count, inst_inc_count):
    d = inst_dec_count - inst_inc_count
    return (d - d.shift(4)).diff()

def f28_ihct_070_inst_churn_index_qoq_d1(inst_inc_count, inst_dec_count, inst_holders):
    return _safe_div(inst_inc_count + inst_dec_count, inst_holders).diff()

def f28_ihct_071_inst_churn_index_yoy_d1(inst_inc_count, inst_dec_count, inst_holders):
    r = _safe_div(inst_inc_count + inst_dec_count, inst_holders)
    return (r - r.shift(4)).diff()

def f28_ihct_072_inst_churn_persistence_8q_d1(inst_inc_count, inst_dec_count, inst_holders):
    r = _safe_div(inst_inc_count + inst_dec_count, inst_holders)
    return r.rolling(8, min_periods=3).mean().diff()

def f28_ihct_073_inst_dec_share_of_total_d1(inst_dec_count, inst_inc_count):
    return _safe_div(inst_dec_count, inst_dec_count + inst_inc_count).diff()

def f28_ihct_074_inst_inc_share_of_total_d1(inst_inc_count, inst_dec_count):
    return _safe_div(inst_inc_count, inst_dec_count + inst_inc_count).diff()

def f28_ihct_075_inst_dec_share_acceleration_d1(inst_dec_count, inst_inc_count):
    r = _safe_div(inst_dec_count, inst_dec_count + inst_inc_count)
    return (r - r.shift(4)).diff()
INSTITUTIONAL_HOLDING_COLLAPSE_TRAJECTORY_D1_REGISTRY_001_075 = {'f28_ihct_001_inst_holders_qoq_change_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_001_inst_holders_qoq_change_d1}, 'f28_ihct_002_inst_holders_yoy_change_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_002_inst_holders_yoy_change_d1}, 'f28_ihct_003_inst_holders_8q_change_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_003_inst_holders_8q_change_d1}, 'f28_ihct_004_inst_holders_12q_change_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_004_inst_holders_12q_change_d1}, 'f28_ihct_005_inst_holders_qoq_pct_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_005_inst_holders_qoq_pct_d1}, 'f28_ihct_006_inst_holders_yoy_pct_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_006_inst_holders_yoy_pct_d1}, 'f28_ihct_007_inst_holders_log_diff_4q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_007_inst_holders_log_diff_4q_d1}, 'f28_ihct_008_inst_holders_8q_cagr_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_008_inst_holders_8q_cagr_d1}, 'f28_ihct_009_inst_holders_drawdown_8q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_009_inst_holders_drawdown_8q_d1}, 'f28_ihct_010_inst_holders_drawdown_16q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_010_inst_holders_drawdown_16q_d1}, 'f28_ihct_011_inst_holders_below_8q_avg_flag_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_011_inst_holders_below_8q_avg_flag_d1}, 'f28_ihct_012_inst_holders_zscore_8q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_012_inst_holders_zscore_8q_d1}, 'f28_ihct_013_inst_holders_zscore_16q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_013_inst_holders_zscore_16q_d1}, 'f28_ihct_014_inst_holders_max_minus_now_8q_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_014_inst_holders_max_minus_now_8q_d1}, 'f28_ihct_015_inst_holders_consecutive_decline_streak_d1': {'inputs': ['inst_holders'], 'func': f28_ihct_015_inst_holders_consecutive_decline_streak_d1}, 'f28_ihct_016_inst_units_qoq_pct_d1': {'inputs': ['inst_units'], 'func': f28_ihct_016_inst_units_qoq_pct_d1}, 'f28_ihct_017_inst_units_yoy_pct_d1': {'inputs': ['inst_units'], 'func': f28_ihct_017_inst_units_yoy_pct_d1}, 'f28_ihct_018_inst_units_8q_pct_d1': {'inputs': ['inst_units'], 'func': f28_ihct_018_inst_units_8q_pct_d1}, 'f28_ihct_019_inst_units_drawdown_8q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_019_inst_units_drawdown_8q_d1}, 'f28_ihct_020_inst_units_drawdown_16q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_020_inst_units_drawdown_16q_d1}, 'f28_ihct_021_inst_value_qoq_pct_d1': {'inputs': ['inst_value'], 'func': f28_ihct_021_inst_value_qoq_pct_d1}, 'f28_ihct_022_inst_value_yoy_pct_d1': {'inputs': ['inst_value'], 'func': f28_ihct_022_inst_value_yoy_pct_d1}, 'f28_ihct_023_inst_value_8q_pct_d1': {'inputs': ['inst_value'], 'func': f28_ihct_023_inst_value_8q_pct_d1}, 'f28_ihct_024_inst_units_log_diff_yoy_d1': {'inputs': ['inst_units'], 'func': f28_ihct_024_inst_units_log_diff_yoy_d1}, 'f28_ihct_025_inst_units_acceleration_4q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_025_inst_units_acceleration_4q_d1}, 'f28_ihct_026_inst_units_consecutive_decline_streak_d1': {'inputs': ['inst_units'], 'func': f28_ihct_026_inst_units_consecutive_decline_streak_d1}, 'f28_ihct_027_inst_units_zscore_8q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_027_inst_units_zscore_8q_d1}, 'f28_ihct_028_inst_units_avg_4q_minus_avg_8q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_028_inst_units_avg_4q_minus_avg_8q_d1}, 'f28_ihct_029_inst_units_diffusion_8q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_029_inst_units_diffusion_8q_d1}, 'f28_ihct_030_inst_units_max_drop_4q_d1': {'inputs': ['inst_units'], 'func': f28_ihct_030_inst_units_max_drop_4q_d1}, 'f28_ihct_031_inst_ownership_pct_qoq_change_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_031_inst_ownership_pct_qoq_change_d1}, 'f28_ihct_032_inst_ownership_pct_yoy_change_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_032_inst_ownership_pct_yoy_change_d1}, 'f28_ihct_033_inst_ownership_pct_8q_change_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_033_inst_ownership_pct_8q_change_d1}, 'f28_ihct_034_inst_ownership_pct_drawdown_8q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_034_inst_ownership_pct_drawdown_8q_d1}, 'f28_ihct_035_inst_ownership_pct_drawdown_16q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_035_inst_ownership_pct_drawdown_16q_d1}, 'f28_ihct_036_inst_ownership_pct_zscore_8q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_036_inst_ownership_pct_zscore_8q_d1}, 'f28_ihct_037_inst_ownership_pct_consecutive_decline_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_037_inst_ownership_pct_consecutive_decline_d1}, 'f28_ihct_038_inst_ownership_pct_change_minus_buyback_pct_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_038_inst_ownership_pct_change_minus_buyback_pct_d1}, 'f28_ihct_039_inst_ownership_pct_change_vs_dilution_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_039_inst_ownership_pct_change_vs_dilution_d1}, 'f28_ihct_040_inst_ownership_pct_below_lt_avg_16q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_040_inst_ownership_pct_below_lt_avg_16q_d1}, 'f28_ihct_041_inst_ownership_pct_chunk_loss_8q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_041_inst_ownership_pct_chunk_loss_8q_d1}, 'f28_ihct_042_inst_ownership_pct_step_decline_8q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_042_inst_ownership_pct_step_decline_8q_d1}, 'f28_ihct_043_inst_ownership_pct_2yr_decline_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_043_inst_ownership_pct_2yr_decline_d1}, 'f28_ihct_044_inst_ownership_pct_max_drawdown_16q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_044_inst_ownership_pct_max_drawdown_16q_d1}, 'f28_ihct_045_inst_ownership_pct_total_drop_8q_d1': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_045_inst_ownership_pct_total_drop_8q_d1}, 'f28_ihct_046_inst_top10_share_qoq_change_d1': {'inputs': ['inst_top10_share'], 'func': f28_ihct_046_inst_top10_share_qoq_change_d1}, 'f28_ihct_047_inst_top10_share_yoy_change_d1': {'inputs': ['inst_top10_share'], 'func': f28_ihct_047_inst_top10_share_yoy_change_d1}, 'f28_ihct_048_inst_top5_share_qoq_change_d1': {'inputs': ['inst_top5_share'], 'func': f28_ihct_048_inst_top5_share_qoq_change_d1}, 'f28_ihct_049_inst_top5_share_yoy_change_d1': {'inputs': ['inst_top5_share'], 'func': f28_ihct_049_inst_top5_share_yoy_change_d1}, 'f28_ihct_050_inst_top10_share_increasing_flag_d1': {'inputs': ['inst_top10_share'], 'func': f28_ihct_050_inst_top10_share_increasing_flag_d1}, 'f28_ihct_051_inst_top10_share_growth_8q_d1': {'inputs': ['inst_top10_share'], 'func': f28_ihct_051_inst_top10_share_growth_8q_d1}, 'f28_ihct_052_inst_top10_share_minus_top5_share_change_d1': {'inputs': ['inst_top10_share', 'inst_top5_share'], 'func': f28_ihct_052_inst_top10_share_minus_top5_share_change_d1}, 'f28_ihct_053_inst_hhi_qoq_change_d1': {'inputs': ['inst_concentration_hhi'], 'func': f28_ihct_053_inst_hhi_qoq_change_d1}, 'f28_ihct_054_inst_hhi_yoy_change_d1': {'inputs': ['inst_concentration_hhi'], 'func': f28_ihct_054_inst_hhi_yoy_change_d1}, 'f28_ihct_055_inst_hhi_growth_8q_d1': {'inputs': ['inst_concentration_hhi'], 'func': f28_ihct_055_inst_hhi_growth_8q_d1}, 'f28_ihct_056_inst_holders_minus_top10_share_divergence_d1': {'inputs': ['inst_holders', 'inst_top10_share'], 'func': f28_ihct_056_inst_holders_minus_top10_share_divergence_d1}, 'f28_ihct_057_inst_concentration_rising_streak_d1': {'inputs': ['inst_concentration_hhi'], 'func': f28_ihct_057_inst_concentration_rising_streak_d1}, 'f28_ihct_058_inst_avg_position_size_qoq_d1': {'inputs': ['inst_avg_position_size'], 'func': f28_ihct_058_inst_avg_position_size_qoq_d1}, 'f28_ihct_059_inst_avg_position_size_yoy_d1': {'inputs': ['inst_avg_position_size'], 'func': f28_ihct_059_inst_avg_position_size_yoy_d1}, 'f28_ihct_060_inst_avg_position_size_drawdown_8q_d1': {'inputs': ['inst_avg_position_size'], 'func': f28_ihct_060_inst_avg_position_size_drawdown_8q_d1}, 'f28_ihct_061_inst_inc_count_qoq_change_d1': {'inputs': ['inst_inc_count'], 'func': f28_ihct_061_inst_inc_count_qoq_change_d1}, 'f28_ihct_062_inst_inc_count_yoy_pct_d1': {'inputs': ['inst_inc_count'], 'func': f28_ihct_062_inst_inc_count_yoy_pct_d1}, 'f28_ihct_063_inst_dec_count_qoq_change_d1': {'inputs': ['inst_dec_count'], 'func': f28_ihct_063_inst_dec_count_qoq_change_d1}, 'f28_ihct_064_inst_dec_count_yoy_pct_d1': {'inputs': ['inst_dec_count'], 'func': f28_ihct_064_inst_dec_count_yoy_pct_d1}, 'f28_ihct_065_inst_dec_to_inc_ratio_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_065_inst_dec_to_inc_ratio_d1}, 'f28_ihct_066_inst_dec_to_inc_ratio_qoq_change_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_066_inst_dec_to_inc_ratio_qoq_change_d1}, 'f28_ihct_067_inst_dec_to_inc_ratio_yoy_change_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_067_inst_dec_to_inc_ratio_yoy_change_d1}, 'f28_ihct_068_inst_dec_minus_inc_count_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_068_inst_dec_minus_inc_count_d1}, 'f28_ihct_069_inst_dec_minus_inc_count_yoy_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_069_inst_dec_minus_inc_count_yoy_d1}, 'f28_ihct_070_inst_churn_index_qoq_d1': {'inputs': ['inst_inc_count', 'inst_dec_count', 'inst_holders'], 'func': f28_ihct_070_inst_churn_index_qoq_d1}, 'f28_ihct_071_inst_churn_index_yoy_d1': {'inputs': ['inst_inc_count', 'inst_dec_count', 'inst_holders'], 'func': f28_ihct_071_inst_churn_index_yoy_d1}, 'f28_ihct_072_inst_churn_persistence_8q_d1': {'inputs': ['inst_inc_count', 'inst_dec_count', 'inst_holders'], 'func': f28_ihct_072_inst_churn_persistence_8q_d1}, 'f28_ihct_073_inst_dec_share_of_total_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_073_inst_dec_share_of_total_d1}, 'f28_ihct_074_inst_inc_share_of_total_d1': {'inputs': ['inst_inc_count', 'inst_dec_count'], 'func': f28_ihct_074_inst_inc_share_of_total_d1}, 'f28_ihct_075_inst_dec_share_acceleration_d1': {'inputs': ['inst_dec_count', 'inst_inc_count'], 'func': f28_ihct_075_inst_dec_share_acceleration_d1}}