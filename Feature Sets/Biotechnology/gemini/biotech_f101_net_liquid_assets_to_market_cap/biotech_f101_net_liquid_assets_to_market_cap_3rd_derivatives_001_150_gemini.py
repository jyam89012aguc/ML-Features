
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(cashneq, investmentsc, debt):
    return cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)

# 5d accel of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_accel_v001_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_accel_v002_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_21d_accel_v003_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_accel_v004_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_accel_v005_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_63d_accel_v006_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_accel_v007_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_accel_v008_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_126d_accel_v009_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_accel_v010_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_accel_v011_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_252d_accel_v012_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_accel_v013_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_accel_v014_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_raw_504d_accel_v015_signal(cashneq, investmentsc, debt):
    base = _mean(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_accel_v016_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_accel_v017_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_21d_accel_v018_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_accel_v019_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_accel_v020_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_63d_accel_v021_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_accel_v022_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_accel_v023_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_126d_accel_v024_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_accel_v025_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_accel_v026_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_252d_accel_v027_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_accel_v028_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_accel_v029_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_log_504d_accel_v030_signal(cashneq, investmentsc, debt):
    base = _mean(_log(_get_metric(cashneq, investmentsc, debt).abs()), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_accel_v031_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_accel_v032_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_21d_accel_v033_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_accel_v034_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_accel_v035_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_63d_accel_v036_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_accel_v037_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_accel_v038_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_126d_accel_v039_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_accel_v040_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_accel_v041_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_252d_accel_v042_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_accel_v043_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_accel_v044_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_z_504d_accel_v045_signal(cashneq, investmentsc, debt):
    base = _z(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_accel_v046_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_accel_v047_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_21d_accel_v048_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_accel_v049_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_accel_v050_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_63d_accel_v051_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_accel_v052_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_accel_v053_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_126d_accel_v054_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_accel_v055_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_accel_v056_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_252d_accel_v057_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_accel_v058_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_accel_v059_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d pct net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_pct_504d_accel_v060_signal(cashneq, investmentsc, debt):
    base = _pct_change(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_accel_v061_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_accel_v062_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_21d_accel_v063_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_accel_v064_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_accel_v065_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_63d_accel_v066_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_accel_v067_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_accel_v068_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_126d_accel_v069_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_accel_v070_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_accel_v071_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_252d_accel_v072_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_accel_v073_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_accel_v074_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ps_504d_accel_v075_signal(cashneq, investmentsc, debt, sharesbas):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_accel_v076_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_accel_v077_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_21d_accel_v078_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_accel_v079_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_accel_v080_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_63d_accel_v081_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_accel_v082_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_accel_v083_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_126d_accel_v084_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_accel_v085_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_accel_v086_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_252d_accel_v087_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_accel_v088_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_accel_v089_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_asset_scaled_504d_accel_v090_signal(cashneq, investmentsc, debt, assets):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_accel_v091_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_accel_v092_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_21d_accel_v093_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_accel_v094_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_accel_v095_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_63d_accel_v096_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_accel_v097_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_accel_v098_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_126d_accel_v099_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_accel_v100_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_accel_v101_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_252d_accel_v102_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_accel_v103_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_accel_v104_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_mcap_scaled_504d_accel_v105_signal(cashneq, investmentsc, debt, marketcap):
    base = _safe_div(_mean(_get_metric(cashneq, investmentsc, debt), 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_accel_v106_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_accel_v107_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_21d_accel_v108_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_accel_v109_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_accel_v110_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_63d_accel_v111_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_accel_v112_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_accel_v113_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_126d_accel_v114_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_accel_v115_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_accel_v116_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_252d_accel_v117_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_accel_v118_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_accel_v119_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d rank net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_rank_504d_accel_v120_signal(cashneq, investmentsc, debt):
    base = _rank(_get_metric(cashneq, investmentsc, debt), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_accel_v121_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_accel_v122_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_21d_accel_v123_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=21).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_accel_v124_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_accel_v125_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_63d_accel_v126_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=63).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_accel_v127_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_accel_v128_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_126d_accel_v129_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=126).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_accel_v130_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_accel_v131_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_252d_accel_v132_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=252).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_accel_v133_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_accel_v134_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ewm net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_ewm_504d_accel_v135_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).ewm(span=504).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_accel_v136_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_accel_v137_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_21d_accel_v138_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(21).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_accel_v139_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_accel_v140_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_63d_accel_v141_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(63).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_accel_v142_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_accel_v143_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_126d_accel_v144_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(126).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_accel_v145_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_accel_v146_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_252d_accel_v147_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(252).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_accel_v148_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_accel_v149_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d med net_liquid
def gm_f101_biotech_f101_net_liquid_assets_to_market_cap_med_504d_accel_v150_signal(cashneq, investmentsc, debt):
    base = _get_metric(cashneq, investmentsc, debt).rolling(504).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

