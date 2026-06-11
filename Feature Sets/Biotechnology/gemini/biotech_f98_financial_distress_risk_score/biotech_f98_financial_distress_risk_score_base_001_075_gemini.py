
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_raw_21d_base_v001_signal(distress, closeadj):
    result = _mean(distress, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_raw_63d_base_v002_signal(distress, closeadj):
    result = _mean(distress, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_raw_126d_base_v003_signal(distress, closeadj):
    result = _mean(distress, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_raw_252d_base_v004_signal(distress, closeadj):
    result = _mean(distress, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_raw_504d_base_v005_signal(distress, closeadj):
    result = _mean(distress, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_log_21d_base_v006_signal(distress, closeadj):
    result = _mean(_log(distress), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_log_63d_base_v007_signal(distress, closeadj):
    result = _mean(_log(distress), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_log_126d_base_v008_signal(distress, closeadj):
    result = _mean(_log(distress), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_log_252d_base_v009_signal(distress, closeadj):
    result = _mean(_log(distress), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed distress
def gm_f98_biotech_f98_financial_distress_risk_score_log_504d_base_v010_signal(distress, closeadj):
    result = _mean(_log(distress), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of distress
def gm_f98_biotech_f98_financial_distress_risk_score_z_21d_base_v011_signal(distress):
    result = _z(distress, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of distress
def gm_f98_biotech_f98_financial_distress_risk_score_z_63d_base_v012_signal(distress):
    result = _z(distress, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of distress
def gm_f98_biotech_f98_financial_distress_risk_score_z_126d_base_v013_signal(distress):
    result = _z(distress, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of distress
def gm_f98_biotech_f98_financial_distress_risk_score_z_252d_base_v014_signal(distress):
    result = _z(distress, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of distress
def gm_f98_biotech_f98_financial_distress_risk_score_z_504d_base_v015_signal(distress):
    result = _z(distress, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of distress
def gm_f98_biotech_f98_financial_distress_risk_score_pct_21d_base_v016_signal(distress):
    result = _pct_change(distress, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of distress
def gm_f98_biotech_f98_financial_distress_risk_score_pct_63d_base_v017_signal(distress):
    result = _pct_change(distress, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of distress
def gm_f98_biotech_f98_financial_distress_risk_score_pct_126d_base_v018_signal(distress):
    result = _pct_change(distress, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of distress
def gm_f98_biotech_f98_financial_distress_risk_score_pct_252d_base_v019_signal(distress):
    result = _pct_change(distress, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of distress
def gm_f98_biotech_f98_financial_distress_risk_score_pct_504d_base_v020_signal(distress):
    result = _pct_change(distress, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share distress
def gm_f98_biotech_f98_financial_distress_risk_score_ps_21d_base_v021_signal(distress, sharesbas, closeadj):
    ps = _safe_div(distress, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share distress
def gm_f98_biotech_f98_financial_distress_risk_score_ps_63d_base_v022_signal(distress, sharesbas, closeadj):
    ps = _safe_div(distress, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share distress
def gm_f98_biotech_f98_financial_distress_risk_score_ps_126d_base_v023_signal(distress, sharesbas, closeadj):
    ps = _safe_div(distress, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share distress
def gm_f98_biotech_f98_financial_distress_risk_score_ps_252d_base_v024_signal(distress, sharesbas, closeadj):
    ps = _safe_div(distress, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share distress
def gm_f98_biotech_f98_financial_distress_risk_score_ps_504d_base_v025_signal(distress, sharesbas, closeadj):
    ps = _safe_div(distress, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of distress to ncfo
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_ncfo_21d_base_v026_signal(distress, ncfo):
    ratio = _safe_div(distress, ncfo)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of distress to ncfo
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_ncfo_63d_base_v027_signal(distress, ncfo):
    ratio = _safe_div(distress, ncfo)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of distress to ncfo
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_ncfo_126d_base_v028_signal(distress, ncfo):
    ratio = _safe_div(distress, ncfo)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of distress to ncfo
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_ncfo_252d_base_v029_signal(distress, ncfo):
    ratio = _safe_div(distress, ncfo)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of distress to ncfo
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_ncfo_504d_base_v030_signal(distress, ncfo):
    ratio = _safe_div(distress, ncfo)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of distress to debt
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_debt_21d_base_v031_signal(distress, debt):
    ratio = _safe_div(distress, debt)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of distress to debt
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_debt_63d_base_v032_signal(distress, debt):
    ratio = _safe_div(distress, debt)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of distress to debt
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_debt_126d_base_v033_signal(distress, debt):
    ratio = _safe_div(distress, debt)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of distress to debt
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_debt_252d_base_v034_signal(distress, debt):
    ratio = _safe_div(distress, debt)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of distress to debt
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_debt_504d_base_v035_signal(distress, debt):
    ratio = _safe_div(distress, debt)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of distress to sharesbas
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_sharesbas_21d_base_v036_signal(distress, sharesbas):
    ratio = _safe_div(distress, sharesbas)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of distress to sharesbas
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_sharesbas_63d_base_v037_signal(distress, sharesbas):
    ratio = _safe_div(distress, sharesbas)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of distress to sharesbas
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_sharesbas_126d_base_v038_signal(distress, sharesbas):
    ratio = _safe_div(distress, sharesbas)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of distress to sharesbas
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_sharesbas_252d_base_v039_signal(distress, sharesbas):
    ratio = _safe_div(distress, sharesbas)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of distress to sharesbas
def gm_f98_biotech_f98_financial_distress_risk_score_ratio_sharesbas_504d_base_v040_signal(distress, sharesbas):
    ratio = _safe_div(distress, sharesbas)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distress scaled by assets
def gm_f98_biotech_f98_financial_distress_risk_score_asset_scaled_21d_base_v041_signal(distress, assets):
    scaled = _safe_div(distress, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distress scaled by assets
def gm_f98_biotech_f98_financial_distress_risk_score_asset_scaled_63d_base_v042_signal(distress, assets):
    scaled = _safe_div(distress, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distress scaled by assets
def gm_f98_biotech_f98_financial_distress_risk_score_asset_scaled_126d_base_v043_signal(distress, assets):
    scaled = _safe_div(distress, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distress scaled by assets
def gm_f98_biotech_f98_financial_distress_risk_score_asset_scaled_252d_base_v044_signal(distress, assets):
    scaled = _safe_div(distress, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distress scaled by assets
def gm_f98_biotech_f98_financial_distress_risk_score_asset_scaled_504d_base_v045_signal(distress, assets):
    scaled = _safe_div(distress, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distress scaled by marketcap
def gm_f98_biotech_f98_financial_distress_risk_score_mcap_scaled_21d_base_v046_signal(distress, marketcap):
    scaled = _safe_div(distress, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distress scaled by marketcap
def gm_f98_biotech_f98_financial_distress_risk_score_mcap_scaled_63d_base_v047_signal(distress, marketcap):
    scaled = _safe_div(distress, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distress scaled by marketcap
def gm_f98_biotech_f98_financial_distress_risk_score_mcap_scaled_126d_base_v048_signal(distress, marketcap):
    scaled = _safe_div(distress, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distress scaled by marketcap
def gm_f98_biotech_f98_financial_distress_risk_score_mcap_scaled_252d_base_v049_signal(distress, marketcap):
    scaled = _safe_div(distress, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distress scaled by marketcap
def gm_f98_biotech_f98_financial_distress_risk_score_mcap_scaled_504d_base_v050_signal(distress, marketcap):
    scaled = _safe_div(distress, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_low_21d_base_v051_signal(distress):
    low = distress.rolling(21).min()
    result = _safe_div(distress - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_low_63d_base_v052_signal(distress):
    low = distress.rolling(63).min()
    result = _safe_div(distress - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_low_126d_base_v053_signal(distress):
    low = distress.rolling(126).min()
    result = _safe_div(distress - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_low_252d_base_v054_signal(distress):
    low = distress.rolling(252).min()
    result = _safe_div(distress - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_low_504d_base_v055_signal(distress):
    low = distress.rolling(504).min()
    result = _safe_div(distress - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_high_21d_base_v056_signal(distress):
    high = distress.rolling(21).max()
    result = _safe_div(high - distress, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_high_63d_base_v057_signal(distress):
    high = distress.rolling(63).max()
    result = _safe_div(high - distress, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_high_126d_base_v058_signal(distress):
    high = distress.rolling(126).max()
    result = _safe_div(high - distress, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_high_252d_base_v059_signal(distress):
    high = distress.rolling(252).max()
    result = _safe_div(high - distress, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high distress
def gm_f98_biotech_f98_financial_distress_risk_score_dist_high_504d_base_v060_signal(distress):
    high = distress.rolling(504).max()
    result = _safe_div(high - distress, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of distress
def gm_f98_biotech_f98_financial_distress_risk_score_mom_21d_base_v061_signal(distress):
    m1 = _mean(distress, 21)
    m2 = _mean(distress, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of distress
def gm_f98_biotech_f98_financial_distress_risk_score_mom_63d_base_v062_signal(distress):
    m1 = _mean(distress, 63)
    m2 = _mean(distress, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of distress
def gm_f98_biotech_f98_financial_distress_risk_score_mom_126d_base_v063_signal(distress):
    m1 = _mean(distress, 126)
    m2 = _mean(distress, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of distress
def gm_f98_biotech_f98_financial_distress_risk_score_mom_252d_base_v064_signal(distress):
    m1 = _mean(distress, 252)
    m2 = _mean(distress, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of distress
def gm_f98_biotech_f98_financial_distress_risk_score_mom_504d_base_v065_signal(distress):
    m1 = _mean(distress, 504)
    m2 = _mean(distress, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of distress
def gm_f98_biotech_f98_financial_distress_risk_score_skew_21d_base_v066_signal(distress):
    result = _skew(distress, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of distress
def gm_f98_biotech_f98_financial_distress_risk_score_skew_63d_base_v067_signal(distress):
    result = _skew(distress, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of distress
def gm_f98_biotech_f98_financial_distress_risk_score_skew_126d_base_v068_signal(distress):
    result = _skew(distress, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of distress
def gm_f98_biotech_f98_financial_distress_risk_score_skew_252d_base_v069_signal(distress):
    result = _skew(distress, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of distress
def gm_f98_biotech_f98_financial_distress_risk_score_skew_504d_base_v070_signal(distress):
    result = _skew(distress, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of distress
def gm_f98_biotech_f98_financial_distress_risk_score_kurt_21d_base_v071_signal(distress):
    result = _kurt(distress, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of distress
def gm_f98_biotech_f98_financial_distress_risk_score_kurt_63d_base_v072_signal(distress):
    result = _kurt(distress, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of distress
def gm_f98_biotech_f98_financial_distress_risk_score_kurt_126d_base_v073_signal(distress):
    result = _kurt(distress, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of distress
def gm_f98_biotech_f98_financial_distress_risk_score_kurt_252d_base_v074_signal(distress):
    result = _kurt(distress, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of distress
def gm_f98_biotech_f98_financial_distress_risk_score_kurt_504d_base_v075_signal(distress):
    result = _kurt(distress, 504)
    return result.replace([np.inf, -np.inf], np.nan)

