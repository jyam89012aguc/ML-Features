
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_base_v001_signal(assetsc, closeadj):
    result = _mean(assetsc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_base_v002_signal(assetsc, closeadj):
    result = _mean(assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_base_v003_signal(assetsc, closeadj):
    result = _mean(assetsc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_base_v004_signal(assetsc, closeadj):
    result = _mean(assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_base_v005_signal(assetsc, closeadj):
    result = _mean(assetsc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_base_v006_signal(assetsc, closeadj):
    result = _mean(_log(assetsc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_base_v007_signal(assetsc, closeadj):
    result = _mean(_log(assetsc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_base_v008_signal(assetsc, closeadj):
    result = _mean(_log(assetsc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_base_v009_signal(assetsc, closeadj):
    result = _mean(_log(assetsc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_base_v010_signal(assetsc, closeadj):
    result = _mean(_log(assetsc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_base_v011_signal(assetsc):
    result = _z(assetsc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_base_v012_signal(assetsc):
    result = _z(assetsc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_base_v013_signal(assetsc):
    result = _z(assetsc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_base_v014_signal(assetsc):
    result = _z(assetsc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_base_v015_signal(assetsc):
    result = _z(assetsc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_pct_21d_base_v016_signal(assetsc):
    result = _pct_change(assetsc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_pct_63d_base_v017_signal(assetsc):
    result = _pct_change(assetsc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_pct_126d_base_v018_signal(assetsc):
    result = _pct_change(assetsc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_pct_252d_base_v019_signal(assetsc):
    result = _pct_change(assetsc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_pct_504d_base_v020_signal(assetsc):
    result = _pct_change(assetsc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_base_v021_signal(assetsc, sharesbas, closeadj):
    ps = _safe_div(assetsc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_base_v022_signal(assetsc, sharesbas, closeadj):
    ps = _safe_div(assetsc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_base_v023_signal(assetsc, sharesbas, closeadj):
    ps = _safe_div(assetsc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_base_v024_signal(assetsc, sharesbas, closeadj):
    ps = _safe_div(assetsc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_base_v025_signal(assetsc, sharesbas, closeadj):
    ps = _safe_div(assetsc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetsc to cashneq
def gm_f62_biotech_f62_operating_accruals_quality_ratio_cashneq_21d_base_v026_signal(assetsc, cashneq):
    ratio = _safe_div(assetsc, cashneq)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetsc to cashneq
def gm_f62_biotech_f62_operating_accruals_quality_ratio_cashneq_63d_base_v027_signal(assetsc, cashneq):
    ratio = _safe_div(assetsc, cashneq)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetsc to cashneq
def gm_f62_biotech_f62_operating_accruals_quality_ratio_cashneq_126d_base_v028_signal(assetsc, cashneq):
    ratio = _safe_div(assetsc, cashneq)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetsc to cashneq
def gm_f62_biotech_f62_operating_accruals_quality_ratio_cashneq_252d_base_v029_signal(assetsc, cashneq):
    ratio = _safe_div(assetsc, cashneq)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetsc to cashneq
def gm_f62_biotech_f62_operating_accruals_quality_ratio_cashneq_504d_base_v030_signal(assetsc, cashneq):
    ratio = _safe_div(assetsc, cashneq)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetsc to liabilitiesc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_liabilitiesc_21d_base_v031_signal(assetsc, liabilitiesc):
    ratio = _safe_div(assetsc, liabilitiesc)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetsc to liabilitiesc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_liabilitiesc_63d_base_v032_signal(assetsc, liabilitiesc):
    ratio = _safe_div(assetsc, liabilitiesc)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetsc to liabilitiesc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_liabilitiesc_126d_base_v033_signal(assetsc, liabilitiesc):
    ratio = _safe_div(assetsc, liabilitiesc)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetsc to liabilitiesc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_liabilitiesc_252d_base_v034_signal(assetsc, liabilitiesc):
    ratio = _safe_div(assetsc, liabilitiesc)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetsc to liabilitiesc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_liabilitiesc_504d_base_v035_signal(assetsc, liabilitiesc):
    ratio = _safe_div(assetsc, liabilitiesc)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetsc to debtc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_debtc_21d_base_v036_signal(assetsc, debtc):
    ratio = _safe_div(assetsc, debtc)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetsc to debtc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_debtc_63d_base_v037_signal(assetsc, debtc):
    ratio = _safe_div(assetsc, debtc)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetsc to debtc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_debtc_126d_base_v038_signal(assetsc, debtc):
    ratio = _safe_div(assetsc, debtc)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetsc to debtc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_debtc_252d_base_v039_signal(assetsc, debtc):
    ratio = _safe_div(assetsc, debtc)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetsc to debtc
def gm_f62_biotech_f62_operating_accruals_quality_ratio_debtc_504d_base_v040_signal(assetsc, debtc):
    ratio = _safe_div(assetsc, debtc)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetsc to taxexp
def gm_f62_biotech_f62_operating_accruals_quality_ratio_taxexp_21d_base_v041_signal(assetsc, taxexp):
    ratio = _safe_div(assetsc, taxexp)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetsc to taxexp
def gm_f62_biotech_f62_operating_accruals_quality_ratio_taxexp_63d_base_v042_signal(assetsc, taxexp):
    ratio = _safe_div(assetsc, taxexp)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetsc to taxexp
def gm_f62_biotech_f62_operating_accruals_quality_ratio_taxexp_126d_base_v043_signal(assetsc, taxexp):
    ratio = _safe_div(assetsc, taxexp)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetsc to taxexp
def gm_f62_biotech_f62_operating_accruals_quality_ratio_taxexp_252d_base_v044_signal(assetsc, taxexp):
    ratio = _safe_div(assetsc, taxexp)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetsc to taxexp
def gm_f62_biotech_f62_operating_accruals_quality_ratio_taxexp_504d_base_v045_signal(assetsc, taxexp):
    ratio = _safe_div(assetsc, taxexp)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetsc to depamor
def gm_f62_biotech_f62_operating_accruals_quality_ratio_depamor_21d_base_v046_signal(assetsc, depamor):
    ratio = _safe_div(assetsc, depamor)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetsc to depamor
def gm_f62_biotech_f62_operating_accruals_quality_ratio_depamor_63d_base_v047_signal(assetsc, depamor):
    ratio = _safe_div(assetsc, depamor)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetsc to depamor
def gm_f62_biotech_f62_operating_accruals_quality_ratio_depamor_126d_base_v048_signal(assetsc, depamor):
    ratio = _safe_div(assetsc, depamor)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetsc to depamor
def gm_f62_biotech_f62_operating_accruals_quality_ratio_depamor_252d_base_v049_signal(assetsc, depamor):
    ratio = _safe_div(assetsc, depamor)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetsc to depamor
def gm_f62_biotech_f62_operating_accruals_quality_ratio_depamor_504d_base_v050_signal(assetsc, depamor):
    ratio = _safe_div(assetsc, depamor)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assetsc scaled by assets
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_base_v051_signal(assetsc, assets):
    scaled = _safe_div(assetsc, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assetsc scaled by assets
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_base_v052_signal(assetsc, assets):
    scaled = _safe_div(assetsc, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assetsc scaled by assets
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_base_v053_signal(assetsc, assets):
    scaled = _safe_div(assetsc, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assetsc scaled by assets
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_base_v054_signal(assetsc, assets):
    scaled = _safe_div(assetsc, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assetsc scaled by assets
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_base_v055_signal(assetsc, assets):
    scaled = _safe_div(assetsc, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assetsc scaled by marketcap
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_base_v056_signal(assetsc, marketcap):
    scaled = _safe_div(assetsc, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assetsc scaled by marketcap
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_base_v057_signal(assetsc, marketcap):
    scaled = _safe_div(assetsc, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assetsc scaled by marketcap
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_base_v058_signal(assetsc, marketcap):
    scaled = _safe_div(assetsc, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assetsc scaled by marketcap
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_base_v059_signal(assetsc, marketcap):
    scaled = _safe_div(assetsc, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assetsc scaled by marketcap
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_base_v060_signal(assetsc, marketcap):
    scaled = _safe_div(assetsc, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_base_v061_signal(assetsc):
    low = assetsc.rolling(21).min()
    result = _safe_div(assetsc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_base_v062_signal(assetsc):
    low = assetsc.rolling(63).min()
    result = _safe_div(assetsc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_base_v063_signal(assetsc):
    low = assetsc.rolling(126).min()
    result = _safe_div(assetsc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_base_v064_signal(assetsc):
    low = assetsc.rolling(252).min()
    result = _safe_div(assetsc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_base_v065_signal(assetsc):
    low = assetsc.rolling(504).min()
    result = _safe_div(assetsc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_base_v066_signal(assetsc):
    high = assetsc.rolling(21).max()
    result = _safe_div(high - assetsc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_base_v067_signal(assetsc):
    high = assetsc.rolling(63).max()
    result = _safe_div(high - assetsc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_base_v068_signal(assetsc):
    high = assetsc.rolling(126).max()
    result = _safe_div(high - assetsc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_base_v069_signal(assetsc):
    high = assetsc.rolling(252).max()
    result = _safe_div(high - assetsc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_base_v070_signal(assetsc):
    high = assetsc.rolling(504).max()
    result = _safe_div(high - assetsc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_base_v071_signal(assetsc):
    m1 = _mean(assetsc, 21)
    m2 = _mean(assetsc, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_base_v072_signal(assetsc):
    m1 = _mean(assetsc, 63)
    m2 = _mean(assetsc, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_base_v073_signal(assetsc):
    m1 = _mean(assetsc, 126)
    m2 = _mean(assetsc, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_base_v074_signal(assetsc):
    m1 = _mean(assetsc, 252)
    m2 = _mean(assetsc, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_base_v075_signal(assetsc):
    m1 = _mean(assetsc, 504)
    m2 = _mean(assetsc, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

