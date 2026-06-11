
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(cashneq, investmentsc, debt):
    return cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)

# 5d slope of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_slope_v001_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_slope_v002_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_slope_v003_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_slope_v004_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_slope_v005_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_slope_v006_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_slope_v007_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_slope_v008_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_slope_v009_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_slope_v010_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_slope_v011_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_slope_v012_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_slope_v013_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_slope_v014_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_slope_v015_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_slope_v016_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_slope_v017_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_slope_v018_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_slope_v019_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_slope_v020_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_slope_v021_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_slope_v022_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_slope_v023_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_slope_v024_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_slope_v025_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_slope_v026_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_slope_v027_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_slope_v028_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_slope_v029_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_slope_v030_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_slope_v031_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_slope_v032_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_slope_v033_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_slope_v034_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_slope_v035_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_slope_v036_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_slope_v037_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_slope_v038_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_slope_v039_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_slope_v040_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_slope_v041_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_slope_v042_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_slope_v043_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_slope_v044_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_slope_v045_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_slope_v046_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_slope_v047_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_slope_v048_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_slope_v049_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_slope_v050_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_slope_v051_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_slope_v052_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_slope_v053_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_slope_v054_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_slope_v055_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_slope_v056_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_slope_v057_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_slope_v058_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_slope_v059_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_slope_v060_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_slope_v061_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_slope_v062_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_slope_v063_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_slope_v064_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_slope_v065_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_slope_v066_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_slope_v067_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_slope_v068_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_slope_v069_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_slope_v070_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_slope_v071_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_slope_v072_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_slope_v073_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_slope_v074_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_slope_v075_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_slope_v076_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_slope_v077_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_slope_v078_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_slope_v079_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_slope_v080_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_slope_v081_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_slope_v082_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_slope_v083_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_slope_v084_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_slope_v085_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_slope_v086_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_slope_v087_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_slope_v088_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_slope_v089_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_slope_v090_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_slope_v091_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_slope_v092_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_slope_v093_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_slope_v094_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_slope_v095_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_slope_v096_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_slope_v097_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_slope_v098_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_slope_v099_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_slope_v100_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_slope_v101_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_slope_v102_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_slope_v103_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_slope_v104_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_slope_v105_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_slope_v106_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_slope_v107_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_slope_v108_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_slope_v109_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_slope_v110_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_slope_v111_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_slope_v112_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_slope_v113_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_slope_v114_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_slope_v115_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_slope_v116_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_slope_v117_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_slope_v118_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_slope_v119_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_slope_v120_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_slope_v121_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_slope_v122_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_slope_v123_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_slope_v124_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_slope_v125_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_slope_v126_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_slope_v127_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_slope_v128_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_slope_v129_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_slope_v130_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_slope_v131_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_slope_v132_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_slope_v133_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_slope_v134_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_slope_v135_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_slope_v136_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_slope_v137_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_slope_v138_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_slope_v139_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_slope_v140_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_slope_v141_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_slope_v142_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_slope_v143_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_slope_v144_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_slope_v145_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_slope_v146_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_slope_v147_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_slope_v148_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_slope_v149_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_slope_v150_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

