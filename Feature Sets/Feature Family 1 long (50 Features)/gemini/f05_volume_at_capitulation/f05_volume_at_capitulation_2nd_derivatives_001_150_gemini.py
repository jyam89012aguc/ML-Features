import pandas as pd
import numpy as np

def f05_volume_at_capitulation_pressure_w2_001_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(2, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w3_002_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(3, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w5_003_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(5, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w8_004_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(8, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w10_005_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(10, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w13_006_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(13, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w21_007_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(21, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w34_008_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(34, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w55_009_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(55, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w63_010_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(63, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w89_011_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(89, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w144_012_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(144, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w252_013_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(252, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w100_014_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(100, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w120_015_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(120, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w150_016_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(150, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w180_017_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(180, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w200_018_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(200, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w220_019_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(220, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_pressure_w240_020_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(240, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_spike_w2_021_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(2, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w3_022_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(3, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w5_023_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(5, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w8_024_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(8, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w10_025_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(10, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w13_026_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(13, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w21_027_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(21, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w34_028_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(34, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w55_029_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(55, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w63_030_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(63, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w89_031_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(89, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w144_032_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(144, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w252_033_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(252, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w100_034_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(100, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w120_035_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(120, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w150_036_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(150, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w180_037_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(180, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w200_038_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(200, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w220_039_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(220, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_spike_w240_040_slope(arg_volume):
    v = arg_volume
    return (v / v.rolling(240, min_periods=1).mean().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vol_range_down_w2_041_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(2, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w3_042_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(3, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w5_043_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(5, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w8_044_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(8, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w10_045_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(10, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w13_046_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(13, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w21_047_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(21, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w34_048_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(34, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w55_049_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(55, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w63_050_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(63, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w89_051_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(89, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w144_052_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(144, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w252_053_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(252, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w100_054_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(100, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w120_055_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(120, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w150_056_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(150, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w180_057_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(180, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w200_058_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(200, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w220_059_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(220, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_vol_range_down_w240_060_slope(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(240, min_periods=1).mean()).diff()

def f05_volume_at_capitulation_spike_at_low_w2_061_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(2, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(2, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w3_062_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(3, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(3, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w5_063_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(5, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(5, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w8_064_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(8, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(8, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w10_065_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(10, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(10, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w13_066_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(13, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(13, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w21_067_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(21, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(21, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w34_068_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(34, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(34, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w55_069_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(55, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(55, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w63_070_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(63, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(63, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w89_071_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(89, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(89, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w144_072_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(144, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(144, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w252_073_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(252, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(252, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w100_074_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(100, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(100, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w120_075_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(120, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(120, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w150_076_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(150, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(150, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w180_077_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(180, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(180, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w200_078_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(200, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(200, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w220_079_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(220, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(220, min_periods=1).max()).diff()

def f05_volume_at_capitulation_spike_at_low_w240_080_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(240, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(240, min_periods=1).max()).diff()

def f05_volume_at_capitulation_vw_drop_w2_081_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(2, min_periods=1).sum() / arg_volume.rolling(2, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w3_082_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(3, min_periods=1).sum() / arg_volume.rolling(3, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w5_083_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(5, min_periods=1).sum() / arg_volume.rolling(5, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w8_084_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(8, min_periods=1).sum() / arg_volume.rolling(8, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w10_085_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(10, min_periods=1).sum() / arg_volume.rolling(10, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w13_086_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(13, min_periods=1).sum() / arg_volume.rolling(13, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w21_087_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(21, min_periods=1).sum() / arg_volume.rolling(21, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w34_088_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(34, min_periods=1).sum() / arg_volume.rolling(34, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w55_089_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(55, min_periods=1).sum() / arg_volume.rolling(55, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w63_090_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(63, min_periods=1).sum() / arg_volume.rolling(63, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w89_091_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(89, min_periods=1).sum() / arg_volume.rolling(89, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w144_092_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(144, min_periods=1).sum() / arg_volume.rolling(144, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w252_093_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(252, min_periods=1).sum() / arg_volume.rolling(252, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w100_094_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(100, min_periods=1).sum() / arg_volume.rolling(100, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w120_095_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(120, min_periods=1).sum() / arg_volume.rolling(120, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w150_096_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(150, min_periods=1).sum() / arg_volume.rolling(150, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w180_097_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(180, min_periods=1).sum() / arg_volume.rolling(180, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w200_098_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(200, min_periods=1).sum() / arg_volume.rolling(200, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w220_099_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(220, min_periods=1).sum() / arg_volume.rolling(220, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_vw_drop_w240_100_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(240, min_periods=1).sum() / arg_volume.rolling(240, min_periods=1).sum().replace(0, np.nan)).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w2_101_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(2, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(2, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w3_102_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(3, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(3, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w5_103_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(5, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(5, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w8_104_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(8, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(8, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w10_105_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(10, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(10, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w13_106_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(13, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(13, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w21_107_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(21, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(21, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w34_108_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(34, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(34, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w55_109_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(55, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(55, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w63_110_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(63, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(63, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w89_111_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(89, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(89, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w144_112_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(144, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(144, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w252_113_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(252, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(252, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w100_114_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(100, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(100, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w120_115_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(120, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(120, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w150_116_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(150, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(150, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w180_117_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(180, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(180, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w200_118_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(200, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(200, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w220_119_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(220, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(220, min_periods=1).max()).diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w240_120_slope(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(240, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(240, min_periods=1).max()).diff()

def f05_volume_at_capitulation_filler_w3_121_slope(arg_volume):

    return (arg_volume.pct_change().rolling(3, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w5_122_slope(arg_volume):

    return (arg_volume.pct_change().rolling(5, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w8_123_slope(arg_volume):

    return (arg_volume.pct_change().rolling(8, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w10_124_slope(arg_volume):

    return (arg_volume.pct_change().rolling(10, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w13_125_slope(arg_volume):

    return (arg_volume.pct_change().rolling(13, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w21_126_slope(arg_volume):

    return (arg_volume.pct_change().rolling(21, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w34_127_slope(arg_volume):

    return (arg_volume.pct_change().rolling(34, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w55_128_slope(arg_volume):

    return (arg_volume.pct_change().rolling(55, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w63_129_slope(arg_volume):

    return (arg_volume.pct_change().rolling(63, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w89_130_slope(arg_volume):

    return (arg_volume.pct_change().rolling(89, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w144_131_slope(arg_volume):

    return (arg_volume.pct_change().rolling(144, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w252_132_slope(arg_volume):

    return (arg_volume.pct_change().rolling(252, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w100_133_slope(arg_volume):

    return (arg_volume.pct_change().rolling(100, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w120_134_slope(arg_volume):

    return (arg_volume.pct_change().rolling(120, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w150_135_slope(arg_volume):

    return (arg_volume.pct_change().rolling(150, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w180_136_slope(arg_volume):

    return (arg_volume.pct_change().rolling(180, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w200_137_slope(arg_volume):

    return (arg_volume.pct_change().rolling(200, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w220_138_slope(arg_volume):

    return (arg_volume.pct_change().rolling(220, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w240_139_slope(arg_volume):

    return (arg_volume.pct_change().rolling(240, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w2_140_slope(arg_volume):

    return (arg_volume.pct_change().rolling(2, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w3_141_slope(arg_volume):

    return (arg_volume.pct_change().rolling(3, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w5_142_slope(arg_volume):

    return (arg_volume.pct_change().rolling(5, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w8_143_slope(arg_volume):

    return (arg_volume.pct_change().rolling(8, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w10_144_slope(arg_volume):

    return (arg_volume.pct_change().rolling(10, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w13_145_slope(arg_volume):

    return (arg_volume.pct_change().rolling(13, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w21_146_slope(arg_volume):

    return (arg_volume.pct_change().rolling(21, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w34_147_slope(arg_volume):

    return (arg_volume.pct_change().rolling(34, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w55_148_slope(arg_volume):

    return (arg_volume.pct_change().rolling(55, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w63_149_slope(arg_volume):

    return (arg_volume.pct_change().rolling(63, min_periods=1).std()).diff()

def f05_volume_at_capitulation_filler_w89_150_slope(arg_volume):

    return (arg_volume.pct_change().rolling(89, min_periods=1).std()).diff()

def test_features():
    np.random.seed(42)
    n = 300
    arg_open = pd.Series(np.random.randn(n).cumsum() + 100)
    arg_high = arg_open + np.random.rand(n)
    arg_low = arg_open - np.random.rand(n)
    arg_close = arg_open + np.random.randn(n)
    arg_volume = pd.Series(np.random.rand(n) * 1000000)
    arg_close_adj = arg_close * 1.05
    
    for feat in [f05_volume_at_capitulation_pressure_w2_001_slope, f05_volume_at_capitulation_pressure_w3_002_slope, f05_volume_at_capitulation_pressure_w5_003_slope, f05_volume_at_capitulation_pressure_w8_004_slope, f05_volume_at_capitulation_pressure_w10_005_slope, f05_volume_at_capitulation_pressure_w13_006_slope, f05_volume_at_capitulation_pressure_w21_007_slope, f05_volume_at_capitulation_pressure_w34_008_slope, f05_volume_at_capitulation_pressure_w55_009_slope, f05_volume_at_capitulation_pressure_w63_010_slope, f05_volume_at_capitulation_pressure_w89_011_slope, f05_volume_at_capitulation_pressure_w144_012_slope, f05_volume_at_capitulation_pressure_w252_013_slope, f05_volume_at_capitulation_pressure_w100_014_slope, f05_volume_at_capitulation_pressure_w120_015_slope, f05_volume_at_capitulation_pressure_w150_016_slope, f05_volume_at_capitulation_pressure_w180_017_slope, f05_volume_at_capitulation_pressure_w200_018_slope, f05_volume_at_capitulation_pressure_w220_019_slope, f05_volume_at_capitulation_pressure_w240_020_slope, f05_volume_at_capitulation_vol_spike_w2_021_slope, f05_volume_at_capitulation_vol_spike_w3_022_slope, f05_volume_at_capitulation_vol_spike_w5_023_slope, f05_volume_at_capitulation_vol_spike_w8_024_slope, f05_volume_at_capitulation_vol_spike_w10_025_slope, f05_volume_at_capitulation_vol_spike_w13_026_slope, f05_volume_at_capitulation_vol_spike_w21_027_slope, f05_volume_at_capitulation_vol_spike_w34_028_slope, f05_volume_at_capitulation_vol_spike_w55_029_slope, f05_volume_at_capitulation_vol_spike_w63_030_slope, f05_volume_at_capitulation_vol_spike_w89_031_slope, f05_volume_at_capitulation_vol_spike_w144_032_slope, f05_volume_at_capitulation_vol_spike_w252_033_slope, f05_volume_at_capitulation_vol_spike_w100_034_slope, f05_volume_at_capitulation_vol_spike_w120_035_slope, f05_volume_at_capitulation_vol_spike_w150_036_slope, f05_volume_at_capitulation_vol_spike_w180_037_slope, f05_volume_at_capitulation_vol_spike_w200_038_slope, f05_volume_at_capitulation_vol_spike_w220_039_slope, f05_volume_at_capitulation_vol_spike_w240_040_slope, f05_volume_at_capitulation_vol_range_down_w2_041_slope, f05_volume_at_capitulation_vol_range_down_w3_042_slope, f05_volume_at_capitulation_vol_range_down_w5_043_slope, f05_volume_at_capitulation_vol_range_down_w8_044_slope, f05_volume_at_capitulation_vol_range_down_w10_045_slope, f05_volume_at_capitulation_vol_range_down_w13_046_slope, f05_volume_at_capitulation_vol_range_down_w21_047_slope, f05_volume_at_capitulation_vol_range_down_w34_048_slope, f05_volume_at_capitulation_vol_range_down_w55_049_slope, f05_volume_at_capitulation_vol_range_down_w63_050_slope, f05_volume_at_capitulation_vol_range_down_w89_051_slope, f05_volume_at_capitulation_vol_range_down_w144_052_slope, f05_volume_at_capitulation_vol_range_down_w252_053_slope, f05_volume_at_capitulation_vol_range_down_w100_054_slope, f05_volume_at_capitulation_vol_range_down_w120_055_slope, f05_volume_at_capitulation_vol_range_down_w150_056_slope, f05_volume_at_capitulation_vol_range_down_w180_057_slope, f05_volume_at_capitulation_vol_range_down_w200_058_slope, f05_volume_at_capitulation_vol_range_down_w220_059_slope, f05_volume_at_capitulation_vol_range_down_w240_060_slope, f05_volume_at_capitulation_spike_at_low_w2_061_slope, f05_volume_at_capitulation_spike_at_low_w3_062_slope, f05_volume_at_capitulation_spike_at_low_w5_063_slope, f05_volume_at_capitulation_spike_at_low_w8_064_slope, f05_volume_at_capitulation_spike_at_low_w10_065_slope, f05_volume_at_capitulation_spike_at_low_w13_066_slope, f05_volume_at_capitulation_spike_at_low_w21_067_slope, f05_volume_at_capitulation_spike_at_low_w34_068_slope, f05_volume_at_capitulation_spike_at_low_w55_069_slope, f05_volume_at_capitulation_spike_at_low_w63_070_slope, f05_volume_at_capitulation_spike_at_low_w89_071_slope, f05_volume_at_capitulation_spike_at_low_w144_072_slope, f05_volume_at_capitulation_spike_at_low_w252_073_slope, f05_volume_at_capitulation_spike_at_low_w100_074_slope, f05_volume_at_capitulation_spike_at_low_w120_075_slope, f05_volume_at_capitulation_spike_at_low_w150_076_slope, f05_volume_at_capitulation_spike_at_low_w180_077_slope, f05_volume_at_capitulation_spike_at_low_w200_078_slope, f05_volume_at_capitulation_spike_at_low_w220_079_slope, f05_volume_at_capitulation_spike_at_low_w240_080_slope, f05_volume_at_capitulation_vw_drop_w2_081_slope, f05_volume_at_capitulation_vw_drop_w3_082_slope, f05_volume_at_capitulation_vw_drop_w5_083_slope, f05_volume_at_capitulation_vw_drop_w8_084_slope, f05_volume_at_capitulation_vw_drop_w10_085_slope, f05_volume_at_capitulation_vw_drop_w13_086_slope, f05_volume_at_capitulation_vw_drop_w21_087_slope, f05_volume_at_capitulation_vw_drop_w34_088_slope, f05_volume_at_capitulation_vw_drop_w55_089_slope, f05_volume_at_capitulation_vw_drop_w63_090_slope, f05_volume_at_capitulation_vw_drop_w89_091_slope, f05_volume_at_capitulation_vw_drop_w144_092_slope, f05_volume_at_capitulation_vw_drop_w252_093_slope, f05_volume_at_capitulation_vw_drop_w100_094_slope, f05_volume_at_capitulation_vw_drop_w120_095_slope, f05_volume_at_capitulation_vw_drop_w150_096_slope, f05_volume_at_capitulation_vw_drop_w180_097_slope, f05_volume_at_capitulation_vw_drop_w200_098_slope, f05_volume_at_capitulation_vw_drop_w220_099_slope, f05_volume_at_capitulation_vw_drop_w240_100_slope, f05_volume_at_capitulation_rel_vol_worst_day_w2_101_slope, f05_volume_at_capitulation_rel_vol_worst_day_w3_102_slope, f05_volume_at_capitulation_rel_vol_worst_day_w5_103_slope, f05_volume_at_capitulation_rel_vol_worst_day_w8_104_slope, f05_volume_at_capitulation_rel_vol_worst_day_w10_105_slope, f05_volume_at_capitulation_rel_vol_worst_day_w13_106_slope, f05_volume_at_capitulation_rel_vol_worst_day_w21_107_slope, f05_volume_at_capitulation_rel_vol_worst_day_w34_108_slope, f05_volume_at_capitulation_rel_vol_worst_day_w55_109_slope, f05_volume_at_capitulation_rel_vol_worst_day_w63_110_slope, f05_volume_at_capitulation_rel_vol_worst_day_w89_111_slope, f05_volume_at_capitulation_rel_vol_worst_day_w144_112_slope, f05_volume_at_capitulation_rel_vol_worst_day_w252_113_slope, f05_volume_at_capitulation_rel_vol_worst_day_w100_114_slope, f05_volume_at_capitulation_rel_vol_worst_day_w120_115_slope, f05_volume_at_capitulation_rel_vol_worst_day_w150_116_slope, f05_volume_at_capitulation_rel_vol_worst_day_w180_117_slope, f05_volume_at_capitulation_rel_vol_worst_day_w200_118_slope, f05_volume_at_capitulation_rel_vol_worst_day_w220_119_slope, f05_volume_at_capitulation_rel_vol_worst_day_w240_120_slope, f05_volume_at_capitulation_filler_w3_121_slope, f05_volume_at_capitulation_filler_w5_122_slope, f05_volume_at_capitulation_filler_w8_123_slope, f05_volume_at_capitulation_filler_w10_124_slope, f05_volume_at_capitulation_filler_w13_125_slope, f05_volume_at_capitulation_filler_w21_126_slope, f05_volume_at_capitulation_filler_w34_127_slope, f05_volume_at_capitulation_filler_w55_128_slope, f05_volume_at_capitulation_filler_w63_129_slope, f05_volume_at_capitulation_filler_w89_130_slope, f05_volume_at_capitulation_filler_w144_131_slope, f05_volume_at_capitulation_filler_w252_132_slope, f05_volume_at_capitulation_filler_w100_133_slope, f05_volume_at_capitulation_filler_w120_134_slope, f05_volume_at_capitulation_filler_w150_135_slope, f05_volume_at_capitulation_filler_w180_136_slope, f05_volume_at_capitulation_filler_w200_137_slope, f05_volume_at_capitulation_filler_w220_138_slope, f05_volume_at_capitulation_filler_w240_139_slope, f05_volume_at_capitulation_filler_w2_140_slope, f05_volume_at_capitulation_filler_w3_141_slope, f05_volume_at_capitulation_filler_w5_142_slope, f05_volume_at_capitulation_filler_w8_143_slope, f05_volume_at_capitulation_filler_w10_144_slope, f05_volume_at_capitulation_filler_w13_145_slope, f05_volume_at_capitulation_filler_w21_146_slope, f05_volume_at_capitulation_filler_w34_147_slope, f05_volume_at_capitulation_filler_w55_148_slope, f05_volume_at_capitulation_filler_w63_149_slope, f05_volume_at_capitulation_filler_w89_150_slope]:
        # Inspect function signature to pass correct arguments
        import inspect
        sig = inspect.signature(feat)
        kwargs = {}
        if 'arg_open' in sig.parameters: kwargs['arg_open'] = arg_open
        if 'arg_high' in sig.parameters: kwargs['arg_high'] = arg_high
        if 'arg_low' in sig.parameters: kwargs['arg_low'] = arg_low
        if 'arg_close' in sig.parameters: kwargs['arg_close'] = arg_close
        if 'arg_volume' in sig.parameters: kwargs['arg_volume'] = arg_volume
        if 'arg_close_adj' in sig.parameters: kwargs['arg_close_adj'] = arg_close_adj
        
        q = feat(**kwargs)
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0

if __name__ == "__main__":
    test_features()
    print("All tests passed!")
