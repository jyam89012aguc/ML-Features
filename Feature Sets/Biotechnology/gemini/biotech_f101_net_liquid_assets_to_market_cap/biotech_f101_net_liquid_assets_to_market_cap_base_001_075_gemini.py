
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(cashneq, investmentsc, debt):
    return cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)

# 21d smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_base_v001_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_base_v002_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_base_v003_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_base_v004_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_base_v005_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_base_v006_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(_log(val.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_base_v007_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(_log(val.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_base_v008_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(_log(val.abs()), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_base_v009_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(_log(val.abs()), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_base_v010_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _mean(_log(val.abs()), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_base_v011_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _z(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_base_v012_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _z(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_base_v013_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _z(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_base_v014_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _z(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_base_v015_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _z(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_base_v016_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _pct_change(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_base_v017_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _pct_change(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_base_v018_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _pct_change(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_base_v019_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _pct_change(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_base_v020_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _pct_change(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_base_v021_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_base_v022_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_base_v023_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_base_v024_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_base_v025_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d net_liquid scaled by assets
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_base_v026_signal(cashneq, investmentsc, debt, assets):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d net_liquid scaled by assets
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_base_v027_signal(cashneq, investmentsc, debt, assets):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d net_liquid scaled by assets
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_base_v028_signal(cashneq, investmentsc, debt, assets):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d net_liquid scaled by assets
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_base_v029_signal(cashneq, investmentsc, debt, assets):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d net_liquid scaled by assets
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_base_v030_signal(cashneq, investmentsc, debt, assets):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d net_liquid scaled by marketcap
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_base_v031_signal(cashneq, investmentsc, debt, marketcap):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d net_liquid scaled by marketcap
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_base_v032_signal(cashneq, investmentsc, debt, marketcap):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d net_liquid scaled by marketcap
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_base_v033_signal(cashneq, investmentsc, debt, marketcap):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d net_liquid scaled by marketcap
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_base_v034_signal(cashneq, investmentsc, debt, marketcap):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d net_liquid scaled by marketcap
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_base_v035_signal(cashneq, investmentsc, debt, marketcap):
    val = _get_metric(cashneq, investmentsc, debt)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_low_21d_base_v036_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    low = val.rolling(21).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_low_63d_base_v037_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    low = val.rolling(63).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_low_126d_base_v038_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    low = val.rolling(126).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_low_252d_base_v039_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    low = val.rolling(252).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_low_504d_base_v040_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    low = val.rolling(504).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_high_21d_base_v041_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    high = val.rolling(21).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_high_63d_base_v042_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    high = val.rolling(63).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_high_126d_base_v043_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    high = val.rolling(126).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_high_252d_base_v044_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    high = val.rolling(252).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_dist_high_504d_base_v045_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    high = val.rolling(504).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mom_21d_base_v046_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    m1 = _mean(val, 21)
    m2 = _mean(val, 21*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mom_63d_base_v047_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    m1 = _mean(val, 63)
    m2 = _mean(val, 63*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mom_126d_base_v048_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    m1 = _mean(val, 126)
    m2 = _mean(val, 126*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mom_252d_base_v049_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    m1 = _mean(val, 252)
    m2 = _mean(val, 252*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mom_504d_base_v050_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    m1 = _mean(val, 504)
    m2 = _mean(val, 504*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_skew_21d_base_v051_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _skew(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_skew_63d_base_v052_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _skew(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_skew_126d_base_v053_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _skew(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_skew_252d_base_v054_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _skew(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_skew_504d_base_v055_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _skew(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_kurt_21d_base_v056_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _kurt(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_kurt_63d_base_v057_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _kurt(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_kurt_126d_base_v058_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _kurt(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_kurt_252d_base_v059_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _kurt(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_kurt_504d_base_v060_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _kurt(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_base_v061_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _rank(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_base_v062_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _rank(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_base_v063_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _rank(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_base_v064_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _rank(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_base_v065_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _rank(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_autocorr_21d_base_v066_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _autocorr(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_autocorr_63d_base_v067_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _autocorr(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_autocorr_126d_base_v068_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _autocorr(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_autocorr_252d_base_v069_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _autocorr(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_autocorr_504d_base_v070_signal(cashneq, investmentsc, debt):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _autocorr(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_std_21d_base_v071_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _std(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_std_63d_base_v072_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _std(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_std_126d_base_v073_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _std(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_std_252d_base_v074_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _std(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_std_504d_base_v075_signal(cashneq, investmentsc, debt, closeadj):
    val = _get_metric(cashneq, investmentsc, debt)
    result = _std(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

