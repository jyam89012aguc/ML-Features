
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_raw_21d_base_v001_signal(pb, closeadj):
    result = _mean(pb, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_raw_63d_base_v002_signal(pb, closeadj):
    result = _mean(pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_raw_126d_base_v003_signal(pb, closeadj):
    result = _mean(pb, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_raw_252d_base_v004_signal(pb, closeadj):
    result = _mean(pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_raw_504d_base_v005_signal(pb, closeadj):
    result = _mean(pb, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_log_21d_base_v006_signal(pb, closeadj):
    result = _mean(_log(pb), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_log_63d_base_v007_signal(pb, closeadj):
    result = _mean(_log(pb), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_log_126d_base_v008_signal(pb, closeadj):
    result = _mean(_log(pb), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_log_252d_base_v009_signal(pb, closeadj):
    result = _mean(_log(pb), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed pb
def gm_f80_biotech_f80_price_to_book_ratio_log_504d_base_v010_signal(pb, closeadj):
    result = _mean(_log(pb), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of pb
def gm_f80_biotech_f80_price_to_book_ratio_z_21d_base_v011_signal(pb):
    result = _z(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb
def gm_f80_biotech_f80_price_to_book_ratio_z_63d_base_v012_signal(pb):
    result = _z(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb
def gm_f80_biotech_f80_price_to_book_ratio_z_126d_base_v013_signal(pb):
    result = _z(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb
def gm_f80_biotech_f80_price_to_book_ratio_z_252d_base_v014_signal(pb):
    result = _z(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb
def gm_f80_biotech_f80_price_to_book_ratio_z_504d_base_v015_signal(pb):
    result = _z(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of pb
def gm_f80_biotech_f80_price_to_book_ratio_pct_21d_base_v016_signal(pb):
    result = _pct_change(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of pb
def gm_f80_biotech_f80_price_to_book_ratio_pct_63d_base_v017_signal(pb):
    result = _pct_change(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of pb
def gm_f80_biotech_f80_price_to_book_ratio_pct_126d_base_v018_signal(pb):
    result = _pct_change(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of pb
def gm_f80_biotech_f80_price_to_book_ratio_pct_252d_base_v019_signal(pb):
    result = _pct_change(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of pb
def gm_f80_biotech_f80_price_to_book_ratio_pct_504d_base_v020_signal(pb):
    result = _pct_change(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share pb
def gm_f80_biotech_f80_price_to_book_ratio_ps_21d_base_v021_signal(pb, sharesbas, closeadj):
    ps = _safe_div(pb, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share pb
def gm_f80_biotech_f80_price_to_book_ratio_ps_63d_base_v022_signal(pb, sharesbas, closeadj):
    ps = _safe_div(pb, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share pb
def gm_f80_biotech_f80_price_to_book_ratio_ps_126d_base_v023_signal(pb, sharesbas, closeadj):
    ps = _safe_div(pb, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share pb
def gm_f80_biotech_f80_price_to_book_ratio_ps_252d_base_v024_signal(pb, sharesbas, closeadj):
    ps = _safe_div(pb, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share pb
def gm_f80_biotech_f80_price_to_book_ratio_ps_504d_base_v025_signal(pb, sharesbas, closeadj):
    ps = _safe_div(pb, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of pb to equity
def gm_f80_biotech_f80_price_to_book_ratio_ratio_equity_21d_base_v026_signal(pb, equity):
    ratio = _safe_div(pb, equity)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of pb to equity
def gm_f80_biotech_f80_price_to_book_ratio_ratio_equity_63d_base_v027_signal(pb, equity):
    ratio = _safe_div(pb, equity)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of pb to equity
def gm_f80_biotech_f80_price_to_book_ratio_ratio_equity_126d_base_v028_signal(pb, equity):
    ratio = _safe_div(pb, equity)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of pb to equity
def gm_f80_biotech_f80_price_to_book_ratio_ratio_equity_252d_base_v029_signal(pb, equity):
    ratio = _safe_div(pb, equity)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of pb to equity
def gm_f80_biotech_f80_price_to_book_ratio_ratio_equity_504d_base_v030_signal(pb, equity):
    ratio = _safe_div(pb, equity)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pb scaled by assets
def gm_f80_biotech_f80_price_to_book_ratio_asset_scaled_21d_base_v031_signal(pb, assets):
    scaled = _safe_div(pb, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pb scaled by assets
def gm_f80_biotech_f80_price_to_book_ratio_asset_scaled_63d_base_v032_signal(pb, assets):
    scaled = _safe_div(pb, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pb scaled by assets
def gm_f80_biotech_f80_price_to_book_ratio_asset_scaled_126d_base_v033_signal(pb, assets):
    scaled = _safe_div(pb, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pb scaled by assets
def gm_f80_biotech_f80_price_to_book_ratio_asset_scaled_252d_base_v034_signal(pb, assets):
    scaled = _safe_div(pb, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pb scaled by assets
def gm_f80_biotech_f80_price_to_book_ratio_asset_scaled_504d_base_v035_signal(pb, assets):
    scaled = _safe_div(pb, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pb scaled by pb
def gm_f80_biotech_f80_price_to_book_ratio_mcap_scaled_21d_base_v036_signal(pb):
    scaled = _safe_div(pb, pb)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pb scaled by pb
def gm_f80_biotech_f80_price_to_book_ratio_mcap_scaled_63d_base_v037_signal(pb):
    scaled = _safe_div(pb, pb)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pb scaled by pb
def gm_f80_biotech_f80_price_to_book_ratio_mcap_scaled_126d_base_v038_signal(pb):
    scaled = _safe_div(pb, pb)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pb scaled by pb
def gm_f80_biotech_f80_price_to_book_ratio_mcap_scaled_252d_base_v039_signal(pb):
    scaled = _safe_div(pb, pb)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pb scaled by pb
def gm_f80_biotech_f80_price_to_book_ratio_mcap_scaled_504d_base_v040_signal(pb):
    scaled = _safe_div(pb, pb)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_low_21d_base_v041_signal(pb):
    low = pb.rolling(21).min()
    result = _safe_div(pb - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_low_63d_base_v042_signal(pb):
    low = pb.rolling(63).min()
    result = _safe_div(pb - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_low_126d_base_v043_signal(pb):
    low = pb.rolling(126).min()
    result = _safe_div(pb - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_low_252d_base_v044_signal(pb):
    low = pb.rolling(252).min()
    result = _safe_div(pb - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_low_504d_base_v045_signal(pb):
    low = pb.rolling(504).min()
    result = _safe_div(pb - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_high_21d_base_v046_signal(pb):
    high = pb.rolling(21).max()
    result = _safe_div(high - pb, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_high_63d_base_v047_signal(pb):
    high = pb.rolling(63).max()
    result = _safe_div(high - pb, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_high_126d_base_v048_signal(pb):
    high = pb.rolling(126).max()
    result = _safe_div(high - pb, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_high_252d_base_v049_signal(pb):
    high = pb.rolling(252).max()
    result = _safe_div(high - pb, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high pb
def gm_f80_biotech_f80_price_to_book_ratio_dist_high_504d_base_v050_signal(pb):
    high = pb.rolling(504).max()
    result = _safe_div(high - pb, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of pb
def gm_f80_biotech_f80_price_to_book_ratio_mom_21d_base_v051_signal(pb):
    m1 = _mean(pb, 21)
    m2 = _mean(pb, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of pb
def gm_f80_biotech_f80_price_to_book_ratio_mom_63d_base_v052_signal(pb):
    m1 = _mean(pb, 63)
    m2 = _mean(pb, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of pb
def gm_f80_biotech_f80_price_to_book_ratio_mom_126d_base_v053_signal(pb):
    m1 = _mean(pb, 126)
    m2 = _mean(pb, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of pb
def gm_f80_biotech_f80_price_to_book_ratio_mom_252d_base_v054_signal(pb):
    m1 = _mean(pb, 252)
    m2 = _mean(pb, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of pb
def gm_f80_biotech_f80_price_to_book_ratio_mom_504d_base_v055_signal(pb):
    m1 = _mean(pb, 504)
    m2 = _mean(pb, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of pb
def gm_f80_biotech_f80_price_to_book_ratio_skew_21d_base_v056_signal(pb):
    result = _skew(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of pb
def gm_f80_biotech_f80_price_to_book_ratio_skew_63d_base_v057_signal(pb):
    result = _skew(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of pb
def gm_f80_biotech_f80_price_to_book_ratio_skew_126d_base_v058_signal(pb):
    result = _skew(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of pb
def gm_f80_biotech_f80_price_to_book_ratio_skew_252d_base_v059_signal(pb):
    result = _skew(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of pb
def gm_f80_biotech_f80_price_to_book_ratio_skew_504d_base_v060_signal(pb):
    result = _skew(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of pb
def gm_f80_biotech_f80_price_to_book_ratio_kurt_21d_base_v061_signal(pb):
    result = _kurt(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of pb
def gm_f80_biotech_f80_price_to_book_ratio_kurt_63d_base_v062_signal(pb):
    result = _kurt(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of pb
def gm_f80_biotech_f80_price_to_book_ratio_kurt_126d_base_v063_signal(pb):
    result = _kurt(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of pb
def gm_f80_biotech_f80_price_to_book_ratio_kurt_252d_base_v064_signal(pb):
    result = _kurt(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of pb
def gm_f80_biotech_f80_price_to_book_ratio_kurt_504d_base_v065_signal(pb):
    result = _kurt(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of pb
def gm_f80_biotech_f80_price_to_book_ratio_rank_21d_base_v066_signal(pb, closeadj):
    result = _rank(pb, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of pb
def gm_f80_biotech_f80_price_to_book_ratio_rank_63d_base_v067_signal(pb, closeadj):
    result = _rank(pb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of pb
def gm_f80_biotech_f80_price_to_book_ratio_rank_126d_base_v068_signal(pb, closeadj):
    result = _rank(pb, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of pb
def gm_f80_biotech_f80_price_to_book_ratio_rank_252d_base_v069_signal(pb, closeadj):
    result = _rank(pb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of pb
def gm_f80_biotech_f80_price_to_book_ratio_rank_504d_base_v070_signal(pb, closeadj):
    result = _rank(pb, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of pb
def gm_f80_biotech_f80_price_to_book_ratio_autocorr_21d_base_v071_signal(pb):
    result = _autocorr(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of pb
def gm_f80_biotech_f80_price_to_book_ratio_autocorr_63d_base_v072_signal(pb):
    result = _autocorr(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of pb
def gm_f80_biotech_f80_price_to_book_ratio_autocorr_126d_base_v073_signal(pb):
    result = _autocorr(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of pb
def gm_f80_biotech_f80_price_to_book_ratio_autocorr_252d_base_v074_signal(pb):
    result = _autocorr(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of pb
def gm_f80_biotech_f80_price_to_book_ratio_autocorr_504d_base_v075_signal(pb):
    result = _autocorr(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)

