
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_raw_21d_base_v001_signal(wcturn, closeadj):
    result = _mean(wcturn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_raw_63d_base_v002_signal(wcturn, closeadj):
    result = _mean(wcturn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_raw_126d_base_v003_signal(wcturn, closeadj):
    result = _mean(wcturn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_raw_252d_base_v004_signal(wcturn, closeadj):
    result = _mean(wcturn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_raw_504d_base_v005_signal(wcturn, closeadj):
    result = _mean(wcturn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_log_21d_base_v006_signal(wcturn, closeadj):
    result = _mean(_log(wcturn), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_log_63d_base_v007_signal(wcturn, closeadj):
    result = _mean(_log(wcturn), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_log_126d_base_v008_signal(wcturn, closeadj):
    result = _mean(_log(wcturn), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_log_252d_base_v009_signal(wcturn, closeadj):
    result = _mean(_log(wcturn), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed wcturn
def gm_f56_biotech_f56_working_capital_turnover_log_504d_base_v010_signal(wcturn, closeadj):
    result = _mean(_log(wcturn), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of wcturn
def gm_f56_biotech_f56_working_capital_turnover_z_21d_base_v011_signal(wcturn):
    result = _z(wcturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wcturn
def gm_f56_biotech_f56_working_capital_turnover_z_63d_base_v012_signal(wcturn):
    result = _z(wcturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wcturn
def gm_f56_biotech_f56_working_capital_turnover_z_126d_base_v013_signal(wcturn):
    result = _z(wcturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wcturn
def gm_f56_biotech_f56_working_capital_turnover_z_252d_base_v014_signal(wcturn):
    result = _z(wcturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wcturn
def gm_f56_biotech_f56_working_capital_turnover_z_504d_base_v015_signal(wcturn):
    result = _z(wcturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of wcturn
def gm_f56_biotech_f56_working_capital_turnover_pct_21d_base_v016_signal(wcturn):
    result = _pct_change(wcturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of wcturn
def gm_f56_biotech_f56_working_capital_turnover_pct_63d_base_v017_signal(wcturn):
    result = _pct_change(wcturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of wcturn
def gm_f56_biotech_f56_working_capital_turnover_pct_126d_base_v018_signal(wcturn):
    result = _pct_change(wcturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of wcturn
def gm_f56_biotech_f56_working_capital_turnover_pct_252d_base_v019_signal(wcturn):
    result = _pct_change(wcturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of wcturn
def gm_f56_biotech_f56_working_capital_turnover_pct_504d_base_v020_signal(wcturn):
    result = _pct_change(wcturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share wcturn
def gm_f56_biotech_f56_working_capital_turnover_ps_21d_base_v021_signal(wcturn, sharesbas, closeadj):
    ps = _safe_div(wcturn, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share wcturn
def gm_f56_biotech_f56_working_capital_turnover_ps_63d_base_v022_signal(wcturn, sharesbas, closeadj):
    ps = _safe_div(wcturn, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share wcturn
def gm_f56_biotech_f56_working_capital_turnover_ps_126d_base_v023_signal(wcturn, sharesbas, closeadj):
    ps = _safe_div(wcturn, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share wcturn
def gm_f56_biotech_f56_working_capital_turnover_ps_252d_base_v024_signal(wcturn, sharesbas, closeadj):
    ps = _safe_div(wcturn, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share wcturn
def gm_f56_biotech_f56_working_capital_turnover_ps_504d_base_v025_signal(wcturn, sharesbas, closeadj):
    ps = _safe_div(wcturn, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of wcturn to workingcapital
def gm_f56_biotech_f56_working_capital_turnover_ratio_workingcapital_21d_base_v026_signal(wcturn, workingcapital):
    ratio = _safe_div(wcturn, workingcapital)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of wcturn to workingcapital
def gm_f56_biotech_f56_working_capital_turnover_ratio_workingcapital_63d_base_v027_signal(wcturn, workingcapital):
    ratio = _safe_div(wcturn, workingcapital)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of wcturn to workingcapital
def gm_f56_biotech_f56_working_capital_turnover_ratio_workingcapital_126d_base_v028_signal(wcturn, workingcapital):
    ratio = _safe_div(wcturn, workingcapital)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of wcturn to workingcapital
def gm_f56_biotech_f56_working_capital_turnover_ratio_workingcapital_252d_base_v029_signal(wcturn, workingcapital):
    ratio = _safe_div(wcturn, workingcapital)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of wcturn to workingcapital
def gm_f56_biotech_f56_working_capital_turnover_ratio_workingcapital_504d_base_v030_signal(wcturn, workingcapital):
    ratio = _safe_div(wcturn, workingcapital)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d wcturn scaled by assets
def gm_f56_biotech_f56_working_capital_turnover_asset_scaled_21d_base_v031_signal(wcturn, assets):
    scaled = _safe_div(wcturn, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d wcturn scaled by assets
def gm_f56_biotech_f56_working_capital_turnover_asset_scaled_63d_base_v032_signal(wcturn, assets):
    scaled = _safe_div(wcturn, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d wcturn scaled by assets
def gm_f56_biotech_f56_working_capital_turnover_asset_scaled_126d_base_v033_signal(wcturn, assets):
    scaled = _safe_div(wcturn, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d wcturn scaled by assets
def gm_f56_biotech_f56_working_capital_turnover_asset_scaled_252d_base_v034_signal(wcturn, assets):
    scaled = _safe_div(wcturn, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d wcturn scaled by assets
def gm_f56_biotech_f56_working_capital_turnover_asset_scaled_504d_base_v035_signal(wcturn, assets):
    scaled = _safe_div(wcturn, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d wcturn scaled by marketcap
def gm_f56_biotech_f56_working_capital_turnover_mcap_scaled_21d_base_v036_signal(wcturn, marketcap):
    scaled = _safe_div(wcturn, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d wcturn scaled by marketcap
def gm_f56_biotech_f56_working_capital_turnover_mcap_scaled_63d_base_v037_signal(wcturn, marketcap):
    scaled = _safe_div(wcturn, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d wcturn scaled by marketcap
def gm_f56_biotech_f56_working_capital_turnover_mcap_scaled_126d_base_v038_signal(wcturn, marketcap):
    scaled = _safe_div(wcturn, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d wcturn scaled by marketcap
def gm_f56_biotech_f56_working_capital_turnover_mcap_scaled_252d_base_v039_signal(wcturn, marketcap):
    scaled = _safe_div(wcturn, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d wcturn scaled by marketcap
def gm_f56_biotech_f56_working_capital_turnover_mcap_scaled_504d_base_v040_signal(wcturn, marketcap):
    scaled = _safe_div(wcturn, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_low_21d_base_v041_signal(wcturn):
    low = wcturn.rolling(21).min()
    result = _safe_div(wcturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_low_63d_base_v042_signal(wcturn):
    low = wcturn.rolling(63).min()
    result = _safe_div(wcturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_low_126d_base_v043_signal(wcturn):
    low = wcturn.rolling(126).min()
    result = _safe_div(wcturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_low_252d_base_v044_signal(wcturn):
    low = wcturn.rolling(252).min()
    result = _safe_div(wcturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_low_504d_base_v045_signal(wcturn):
    low = wcturn.rolling(504).min()
    result = _safe_div(wcturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_high_21d_base_v046_signal(wcturn):
    high = wcturn.rolling(21).max()
    result = _safe_div(high - wcturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_high_63d_base_v047_signal(wcturn):
    high = wcturn.rolling(63).max()
    result = _safe_div(high - wcturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_high_126d_base_v048_signal(wcturn):
    high = wcturn.rolling(126).max()
    result = _safe_div(high - wcturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_high_252d_base_v049_signal(wcturn):
    high = wcturn.rolling(252).max()
    result = _safe_div(high - wcturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high wcturn
def gm_f56_biotech_f56_working_capital_turnover_dist_high_504d_base_v050_signal(wcturn):
    high = wcturn.rolling(504).max()
    result = _safe_div(high - wcturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of wcturn
def gm_f56_biotech_f56_working_capital_turnover_mom_21d_base_v051_signal(wcturn):
    m1 = _mean(wcturn, 21)
    m2 = _mean(wcturn, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of wcturn
def gm_f56_biotech_f56_working_capital_turnover_mom_63d_base_v052_signal(wcturn):
    m1 = _mean(wcturn, 63)
    m2 = _mean(wcturn, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of wcturn
def gm_f56_biotech_f56_working_capital_turnover_mom_126d_base_v053_signal(wcturn):
    m1 = _mean(wcturn, 126)
    m2 = _mean(wcturn, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of wcturn
def gm_f56_biotech_f56_working_capital_turnover_mom_252d_base_v054_signal(wcturn):
    m1 = _mean(wcturn, 252)
    m2 = _mean(wcturn, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of wcturn
def gm_f56_biotech_f56_working_capital_turnover_mom_504d_base_v055_signal(wcturn):
    m1 = _mean(wcturn, 504)
    m2 = _mean(wcturn, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of wcturn
def gm_f56_biotech_f56_working_capital_turnover_skew_21d_base_v056_signal(wcturn):
    result = _skew(wcturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of wcturn
def gm_f56_biotech_f56_working_capital_turnover_skew_63d_base_v057_signal(wcturn):
    result = _skew(wcturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of wcturn
def gm_f56_biotech_f56_working_capital_turnover_skew_126d_base_v058_signal(wcturn):
    result = _skew(wcturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of wcturn
def gm_f56_biotech_f56_working_capital_turnover_skew_252d_base_v059_signal(wcturn):
    result = _skew(wcturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of wcturn
def gm_f56_biotech_f56_working_capital_turnover_skew_504d_base_v060_signal(wcturn):
    result = _skew(wcturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of wcturn
def gm_f56_biotech_f56_working_capital_turnover_kurt_21d_base_v061_signal(wcturn):
    result = _kurt(wcturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of wcturn
def gm_f56_biotech_f56_working_capital_turnover_kurt_63d_base_v062_signal(wcturn):
    result = _kurt(wcturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of wcturn
def gm_f56_biotech_f56_working_capital_turnover_kurt_126d_base_v063_signal(wcturn):
    result = _kurt(wcturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of wcturn
def gm_f56_biotech_f56_working_capital_turnover_kurt_252d_base_v064_signal(wcturn):
    result = _kurt(wcturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of wcturn
def gm_f56_biotech_f56_working_capital_turnover_kurt_504d_base_v065_signal(wcturn):
    result = _kurt(wcturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of wcturn
def gm_f56_biotech_f56_working_capital_turnover_rank_21d_base_v066_signal(wcturn, closeadj):
    result = _rank(wcturn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of wcturn
def gm_f56_biotech_f56_working_capital_turnover_rank_63d_base_v067_signal(wcturn, closeadj):
    result = _rank(wcturn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of wcturn
def gm_f56_biotech_f56_working_capital_turnover_rank_126d_base_v068_signal(wcturn, closeadj):
    result = _rank(wcturn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of wcturn
def gm_f56_biotech_f56_working_capital_turnover_rank_252d_base_v069_signal(wcturn, closeadj):
    result = _rank(wcturn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of wcturn
def gm_f56_biotech_f56_working_capital_turnover_rank_504d_base_v070_signal(wcturn, closeadj):
    result = _rank(wcturn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of wcturn
def gm_f56_biotech_f56_working_capital_turnover_autocorr_21d_base_v071_signal(wcturn):
    result = _autocorr(wcturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of wcturn
def gm_f56_biotech_f56_working_capital_turnover_autocorr_63d_base_v072_signal(wcturn):
    result = _autocorr(wcturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of wcturn
def gm_f56_biotech_f56_working_capital_turnover_autocorr_126d_base_v073_signal(wcturn):
    result = _autocorr(wcturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of wcturn
def gm_f56_biotech_f56_working_capital_turnover_autocorr_252d_base_v074_signal(wcturn):
    result = _autocorr(wcturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of wcturn
def gm_f56_biotech_f56_working_capital_turnover_autocorr_504d_base_v075_signal(wcturn):
    result = _autocorr(wcturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

