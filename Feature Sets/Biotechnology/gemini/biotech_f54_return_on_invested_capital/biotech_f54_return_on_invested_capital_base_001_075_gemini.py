
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_raw_21d_base_v001_signal(roic, closeadj):
    result = _mean(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_raw_63d_base_v002_signal(roic, closeadj):
    result = _mean(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_raw_126d_base_v003_signal(roic, closeadj):
    result = _mean(roic, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_raw_252d_base_v004_signal(roic, closeadj):
    result = _mean(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_raw_504d_base_v005_signal(roic, closeadj):
    result = _mean(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_log_21d_base_v006_signal(roic, closeadj):
    result = _mean(_log(roic), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_log_63d_base_v007_signal(roic, closeadj):
    result = _mean(_log(roic), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_log_126d_base_v008_signal(roic, closeadj):
    result = _mean(_log(roic), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_log_252d_base_v009_signal(roic, closeadj):
    result = _mean(_log(roic), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed roic
def gm_f54_biotech_f54_return_on_invested_capital_log_504d_base_v010_signal(roic, closeadj):
    result = _mean(_log(roic), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of roic
def gm_f54_biotech_f54_return_on_invested_capital_z_21d_base_v011_signal(roic):
    result = _z(roic, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic
def gm_f54_biotech_f54_return_on_invested_capital_z_63d_base_v012_signal(roic):
    result = _z(roic, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic
def gm_f54_biotech_f54_return_on_invested_capital_z_126d_base_v013_signal(roic):
    result = _z(roic, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic
def gm_f54_biotech_f54_return_on_invested_capital_z_252d_base_v014_signal(roic):
    result = _z(roic, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic
def gm_f54_biotech_f54_return_on_invested_capital_z_504d_base_v015_signal(roic):
    result = _z(roic, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of roic
def gm_f54_biotech_f54_return_on_invested_capital_pct_21d_base_v016_signal(roic):
    result = _pct_change(roic, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of roic
def gm_f54_biotech_f54_return_on_invested_capital_pct_63d_base_v017_signal(roic):
    result = _pct_change(roic, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of roic
def gm_f54_biotech_f54_return_on_invested_capital_pct_126d_base_v018_signal(roic):
    result = _pct_change(roic, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of roic
def gm_f54_biotech_f54_return_on_invested_capital_pct_252d_base_v019_signal(roic):
    result = _pct_change(roic, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of roic
def gm_f54_biotech_f54_return_on_invested_capital_pct_504d_base_v020_signal(roic):
    result = _pct_change(roic, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share roic
def gm_f54_biotech_f54_return_on_invested_capital_ps_21d_base_v021_signal(roic, sharesbas, closeadj):
    ps = _safe_div(roic, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share roic
def gm_f54_biotech_f54_return_on_invested_capital_ps_63d_base_v022_signal(roic, sharesbas, closeadj):
    ps = _safe_div(roic, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share roic
def gm_f54_biotech_f54_return_on_invested_capital_ps_126d_base_v023_signal(roic, sharesbas, closeadj):
    ps = _safe_div(roic, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share roic
def gm_f54_biotech_f54_return_on_invested_capital_ps_252d_base_v024_signal(roic, sharesbas, closeadj):
    ps = _safe_div(roic, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share roic
def gm_f54_biotech_f54_return_on_invested_capital_ps_504d_base_v025_signal(roic, sharesbas, closeadj):
    ps = _safe_div(roic, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of roic to taxexp
def gm_f54_biotech_f54_return_on_invested_capital_ratio_taxexp_21d_base_v026_signal(roic, taxexp):
    ratio = _safe_div(roic, taxexp)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of roic to taxexp
def gm_f54_biotech_f54_return_on_invested_capital_ratio_taxexp_63d_base_v027_signal(roic, taxexp):
    ratio = _safe_div(roic, taxexp)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of roic to taxexp
def gm_f54_biotech_f54_return_on_invested_capital_ratio_taxexp_126d_base_v028_signal(roic, taxexp):
    ratio = _safe_div(roic, taxexp)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of roic to taxexp
def gm_f54_biotech_f54_return_on_invested_capital_ratio_taxexp_252d_base_v029_signal(roic, taxexp):
    ratio = _safe_div(roic, taxexp)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of roic to taxexp
def gm_f54_biotech_f54_return_on_invested_capital_ratio_taxexp_504d_base_v030_signal(roic, taxexp):
    ratio = _safe_div(roic, taxexp)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of roic to invcap
def gm_f54_biotech_f54_return_on_invested_capital_ratio_invcap_21d_base_v031_signal(roic, invcap):
    ratio = _safe_div(roic, invcap)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of roic to invcap
def gm_f54_biotech_f54_return_on_invested_capital_ratio_invcap_63d_base_v032_signal(roic, invcap):
    ratio = _safe_div(roic, invcap)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of roic to invcap
def gm_f54_biotech_f54_return_on_invested_capital_ratio_invcap_126d_base_v033_signal(roic, invcap):
    ratio = _safe_div(roic, invcap)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of roic to invcap
def gm_f54_biotech_f54_return_on_invested_capital_ratio_invcap_252d_base_v034_signal(roic, invcap):
    ratio = _safe_div(roic, invcap)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of roic to invcap
def gm_f54_biotech_f54_return_on_invested_capital_ratio_invcap_504d_base_v035_signal(roic, invcap):
    ratio = _safe_div(roic, invcap)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roic scaled by assets
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_21d_base_v036_signal(roic, assets):
    scaled = _safe_div(roic, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roic scaled by assets
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_63d_base_v037_signal(roic, assets):
    scaled = _safe_div(roic, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roic scaled by assets
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_126d_base_v038_signal(roic, assets):
    scaled = _safe_div(roic, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roic scaled by assets
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_252d_base_v039_signal(roic, assets):
    scaled = _safe_div(roic, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roic scaled by assets
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_504d_base_v040_signal(roic, assets):
    scaled = _safe_div(roic, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roic scaled by marketcap
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_21d_base_v041_signal(roic, marketcap):
    scaled = _safe_div(roic, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roic scaled by marketcap
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_63d_base_v042_signal(roic, marketcap):
    scaled = _safe_div(roic, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roic scaled by marketcap
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_126d_base_v043_signal(roic, marketcap):
    scaled = _safe_div(roic, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roic scaled by marketcap
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_252d_base_v044_signal(roic, marketcap):
    scaled = _safe_div(roic, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roic scaled by marketcap
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_504d_base_v045_signal(roic, marketcap):
    scaled = _safe_div(roic, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_21d_base_v046_signal(roic):
    low = roic.rolling(21).min()
    result = _safe_div(roic - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_63d_base_v047_signal(roic):
    low = roic.rolling(63).min()
    result = _safe_div(roic - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_126d_base_v048_signal(roic):
    low = roic.rolling(126).min()
    result = _safe_div(roic - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_252d_base_v049_signal(roic):
    low = roic.rolling(252).min()
    result = _safe_div(roic - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_504d_base_v050_signal(roic):
    low = roic.rolling(504).min()
    result = _safe_div(roic - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_21d_base_v051_signal(roic):
    high = roic.rolling(21).max()
    result = _safe_div(high - roic, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_63d_base_v052_signal(roic):
    high = roic.rolling(63).max()
    result = _safe_div(high - roic, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_126d_base_v053_signal(roic):
    high = roic.rolling(126).max()
    result = _safe_div(high - roic, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_252d_base_v054_signal(roic):
    high = roic.rolling(252).max()
    result = _safe_div(high - roic, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high roic
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_504d_base_v055_signal(roic):
    high = roic.rolling(504).max()
    result = _safe_div(high - roic, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of roic
def gm_f54_biotech_f54_return_on_invested_capital_mom_21d_base_v056_signal(roic):
    m1 = _mean(roic, 21)
    m2 = _mean(roic, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of roic
def gm_f54_biotech_f54_return_on_invested_capital_mom_63d_base_v057_signal(roic):
    m1 = _mean(roic, 63)
    m2 = _mean(roic, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of roic
def gm_f54_biotech_f54_return_on_invested_capital_mom_126d_base_v058_signal(roic):
    m1 = _mean(roic, 126)
    m2 = _mean(roic, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of roic
def gm_f54_biotech_f54_return_on_invested_capital_mom_252d_base_v059_signal(roic):
    m1 = _mean(roic, 252)
    m2 = _mean(roic, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of roic
def gm_f54_biotech_f54_return_on_invested_capital_mom_504d_base_v060_signal(roic):
    m1 = _mean(roic, 504)
    m2 = _mean(roic, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of roic
def gm_f54_biotech_f54_return_on_invested_capital_skew_21d_base_v061_signal(roic):
    result = _skew(roic, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of roic
def gm_f54_biotech_f54_return_on_invested_capital_skew_63d_base_v062_signal(roic):
    result = _skew(roic, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of roic
def gm_f54_biotech_f54_return_on_invested_capital_skew_126d_base_v063_signal(roic):
    result = _skew(roic, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of roic
def gm_f54_biotech_f54_return_on_invested_capital_skew_252d_base_v064_signal(roic):
    result = _skew(roic, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of roic
def gm_f54_biotech_f54_return_on_invested_capital_skew_504d_base_v065_signal(roic):
    result = _skew(roic, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of roic
def gm_f54_biotech_f54_return_on_invested_capital_kurt_21d_base_v066_signal(roic):
    result = _kurt(roic, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of roic
def gm_f54_biotech_f54_return_on_invested_capital_kurt_63d_base_v067_signal(roic):
    result = _kurt(roic, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of roic
def gm_f54_biotech_f54_return_on_invested_capital_kurt_126d_base_v068_signal(roic):
    result = _kurt(roic, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of roic
def gm_f54_biotech_f54_return_on_invested_capital_kurt_252d_base_v069_signal(roic):
    result = _kurt(roic, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of roic
def gm_f54_biotech_f54_return_on_invested_capital_kurt_504d_base_v070_signal(roic):
    result = _kurt(roic, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of roic
def gm_f54_biotech_f54_return_on_invested_capital_rank_21d_base_v071_signal(roic, closeadj):
    result = _rank(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of roic
def gm_f54_biotech_f54_return_on_invested_capital_rank_63d_base_v072_signal(roic, closeadj):
    result = _rank(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of roic
def gm_f54_biotech_f54_return_on_invested_capital_rank_126d_base_v073_signal(roic, closeadj):
    result = _rank(roic, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of roic
def gm_f54_biotech_f54_return_on_invested_capital_rank_252d_base_v074_signal(roic, closeadj):
    result = _rank(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of roic
def gm_f54_biotech_f54_return_on_invested_capital_rank_504d_base_v075_signal(roic, closeadj):
    result = _rank(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

