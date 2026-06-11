import pandas as pd
import numpy as np

def f05_volume_at_capitulation_pressure_w2_001_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(2, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w3_002_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(3, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w5_003_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(5, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w8_004_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(8, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w10_005_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(10, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w13_006_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(13, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w21_007_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(21, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w34_008_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(34, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w55_009_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(55, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w63_010_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(63, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w89_011_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(89, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w144_012_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(144, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w252_013_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(252, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w100_014_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(100, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w120_015_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(120, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w150_016_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(150, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w180_017_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(180, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w200_018_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(200, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w220_019_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(220, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_pressure_w240_020_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return ((c.pct_change().clip(upper=0).abs() * arg_volume).rolling(240, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_spike_w2_021_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(2, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w3_022_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(3, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w5_023_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(5, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w8_024_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(8, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w10_025_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(10, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w13_026_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(13, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w21_027_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(21, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w34_028_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(34, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w55_029_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(55, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w63_030_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(63, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w89_031_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(89, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w144_032_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(144, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w252_033_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(252, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w100_034_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(100, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w120_035_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(120, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w150_036_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(150, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w180_037_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(180, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w200_038_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(200, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w220_039_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(220, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_spike_w240_040_jerk(arg_volume):
    v = arg_volume
    return (v / v.rolling(240, min_periods=1).mean().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w2_041_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(2, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w3_042_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(3, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w5_043_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(5, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w8_044_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(8, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w10_045_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(10, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w13_046_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(13, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w21_047_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(21, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w34_048_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(34, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w55_049_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(55, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w63_050_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(63, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w89_051_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(89, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w144_052_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(144, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w252_053_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(252, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w100_054_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(100, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w120_055_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(120, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w150_056_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(150, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w180_057_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(180, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w200_058_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(200, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w220_059_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(220, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_vol_range_down_w240_060_jerk(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return ((ratio.where(arg_close < arg_open, 0)).rolling(240, min_periods=1).mean()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w2_061_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(2, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(2, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w3_062_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(3, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(3, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w5_063_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(5, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(5, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w8_064_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(8, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(8, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w10_065_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(10, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(10, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w13_066_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(13, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(13, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w21_067_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(21, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(21, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w34_068_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(34, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(34, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w55_069_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(55, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(55, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w63_070_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(63, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(63, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w89_071_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(89, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(89, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w144_072_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(144, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(144, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w252_073_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(252, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(252, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w100_074_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(100, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(100, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w120_075_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(120, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(120, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w150_076_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(150, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(150, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w180_077_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(180, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(180, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w200_078_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(200, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(200, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w220_079_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(220, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(220, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_spike_at_low_w240_080_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(240, min_periods=1).min()
    return ((v_spike.where(is_low, 0)).rolling(240, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_vw_drop_w2_081_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(2, min_periods=1).sum() / arg_volume.rolling(2, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w3_082_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(3, min_periods=1).sum() / arg_volume.rolling(3, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w5_083_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(5, min_periods=1).sum() / arg_volume.rolling(5, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w8_084_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(8, min_periods=1).sum() / arg_volume.rolling(8, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w10_085_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(10, min_periods=1).sum() / arg_volume.rolling(10, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w13_086_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(13, min_periods=1).sum() / arg_volume.rolling(13, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w21_087_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(21, min_periods=1).sum() / arg_volume.rolling(21, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w34_088_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(34, min_periods=1).sum() / arg_volume.rolling(34, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w55_089_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(55, min_periods=1).sum() / arg_volume.rolling(55, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w63_090_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(63, min_periods=1).sum() / arg_volume.rolling(63, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w89_091_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(89, min_periods=1).sum() / arg_volume.rolling(89, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w144_092_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(144, min_periods=1).sum() / arg_volume.rolling(144, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w252_093_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(252, min_periods=1).sum() / arg_volume.rolling(252, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w100_094_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(100, min_periods=1).sum() / arg_volume.rolling(100, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w120_095_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(120, min_periods=1).sum() / arg_volume.rolling(120, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w150_096_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(150, min_periods=1).sum() / arg_volume.rolling(150, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w180_097_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(180, min_periods=1).sum() / arg_volume.rolling(180, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w200_098_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(200, min_periods=1).sum() / arg_volume.rolling(200, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w220_099_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(220, min_periods=1).sum() / arg_volume.rolling(220, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_vw_drop_w240_100_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return ((ret * arg_volume).rolling(240, min_periods=1).sum() / arg_volume.rolling(240, min_periods=1).sum().replace(0, np.nan)).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w2_101_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(2, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(2, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w3_102_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(3, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(3, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w5_103_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(5, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(5, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w8_104_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(8, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(8, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w10_105_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(10, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(10, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w13_106_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(13, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(13, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w21_107_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(21, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(21, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w34_108_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(34, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(34, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w55_109_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(55, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(55, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w63_110_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(63, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(63, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w89_111_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(89, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(89, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w144_112_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(144, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(144, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w252_113_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(252, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(252, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w100_114_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(100, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(100, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w120_115_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(120, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(120, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w150_116_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(150, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(150, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w180_117_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(180, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(180, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w200_118_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(200, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(200, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w220_119_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(220, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(220, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_rel_vol_worst_day_w240_120_jerk(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(240, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    return ((v_spike.where(ret == worst_ret, 0)).rolling(240, min_periods=1).max()).diff().diff()

def f05_volume_at_capitulation_filler_w3_121_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(3, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w5_122_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(5, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w8_123_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(8, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w10_124_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(10, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w13_125_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(13, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w21_126_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(21, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w34_127_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(34, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w55_128_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(55, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w63_129_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(63, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w89_130_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(89, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w144_131_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(144, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w252_132_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(252, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w100_133_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(100, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w120_134_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(120, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w150_135_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(150, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w180_136_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(180, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w200_137_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(200, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w220_138_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(220, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w240_139_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(240, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w2_140_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(2, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w3_141_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(3, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w5_142_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(5, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w8_143_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(8, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w10_144_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(10, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w13_145_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(13, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w21_146_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(21, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w34_147_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(34, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w55_148_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(55, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w63_149_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(63, min_periods=1).std()).diff().diff()

def f05_volume_at_capitulation_filler_w89_150_jerk(arg_volume):

    return (arg_volume.pct_change().rolling(89, min_periods=1).std()).diff().diff()

def test_features():
    np.random.seed(42)
    n = 300
    arg_open = pd.Series(np.random.randn(n).cumsum() + 100)
    arg_high = arg_open + np.random.rand(n)
    arg_low = arg_open - np.random.rand(n)
    arg_close = arg_open + np.random.randn(n)
    arg_volume = pd.Series(np.random.rand(n) * 1000000)
    arg_close_adj = arg_close * 1.05
    
    for feat in [f05_volume_at_capitulation_pressure_w2_001_jerk, f05_volume_at_capitulation_pressure_w3_002_jerk, f05_volume_at_capitulation_pressure_w5_003_jerk, f05_volume_at_capitulation_pressure_w8_004_jerk, f05_volume_at_capitulation_pressure_w10_005_jerk, f05_volume_at_capitulation_pressure_w13_006_jerk, f05_volume_at_capitulation_pressure_w21_007_jerk, f05_volume_at_capitulation_pressure_w34_008_jerk, f05_volume_at_capitulation_pressure_w55_009_jerk, f05_volume_at_capitulation_pressure_w63_010_jerk, f05_volume_at_capitulation_pressure_w89_011_jerk, f05_volume_at_capitulation_pressure_w144_012_jerk, f05_volume_at_capitulation_pressure_w252_013_jerk, f05_volume_at_capitulation_pressure_w100_014_jerk, f05_volume_at_capitulation_pressure_w120_015_jerk, f05_volume_at_capitulation_pressure_w150_016_jerk, f05_volume_at_capitulation_pressure_w180_017_jerk, f05_volume_at_capitulation_pressure_w200_018_jerk, f05_volume_at_capitulation_pressure_w220_019_jerk, f05_volume_at_capitulation_pressure_w240_020_jerk, f05_volume_at_capitulation_vol_spike_w2_021_jerk, f05_volume_at_capitulation_vol_spike_w3_022_jerk, f05_volume_at_capitulation_vol_spike_w5_023_jerk, f05_volume_at_capitulation_vol_spike_w8_024_jerk, f05_volume_at_capitulation_vol_spike_w10_025_jerk, f05_volume_at_capitulation_vol_spike_w13_026_jerk, f05_volume_at_capitulation_vol_spike_w21_027_jerk, f05_volume_at_capitulation_vol_spike_w34_028_jerk, f05_volume_at_capitulation_vol_spike_w55_029_jerk, f05_volume_at_capitulation_vol_spike_w63_030_jerk, f05_volume_at_capitulation_vol_spike_w89_031_jerk, f05_volume_at_capitulation_vol_spike_w144_032_jerk, f05_volume_at_capitulation_vol_spike_w252_033_jerk, f05_volume_at_capitulation_vol_spike_w100_034_jerk, f05_volume_at_capitulation_vol_spike_w120_035_jerk, f05_volume_at_capitulation_vol_spike_w150_036_jerk, f05_volume_at_capitulation_vol_spike_w180_037_jerk, f05_volume_at_capitulation_vol_spike_w200_038_jerk, f05_volume_at_capitulation_vol_spike_w220_039_jerk, f05_volume_at_capitulation_vol_spike_w240_040_jerk, f05_volume_at_capitulation_vol_range_down_w2_041_jerk, f05_volume_at_capitulation_vol_range_down_w3_042_jerk, f05_volume_at_capitulation_vol_range_down_w5_043_jerk, f05_volume_at_capitulation_vol_range_down_w8_044_jerk, f05_volume_at_capitulation_vol_range_down_w10_045_jerk, f05_volume_at_capitulation_vol_range_down_w13_046_jerk, f05_volume_at_capitulation_vol_range_down_w21_047_jerk, f05_volume_at_capitulation_vol_range_down_w34_048_jerk, f05_volume_at_capitulation_vol_range_down_w55_049_jerk, f05_volume_at_capitulation_vol_range_down_w63_050_jerk, f05_volume_at_capitulation_vol_range_down_w89_051_jerk, f05_volume_at_capitulation_vol_range_down_w144_052_jerk, f05_volume_at_capitulation_vol_range_down_w252_053_jerk, f05_volume_at_capitulation_vol_range_down_w100_054_jerk, f05_volume_at_capitulation_vol_range_down_w120_055_jerk, f05_volume_at_capitulation_vol_range_down_w150_056_jerk, f05_volume_at_capitulation_vol_range_down_w180_057_jerk, f05_volume_at_capitulation_vol_range_down_w200_058_jerk, f05_volume_at_capitulation_vol_range_down_w220_059_jerk, f05_volume_at_capitulation_vol_range_down_w240_060_jerk, f05_volume_at_capitulation_spike_at_low_w2_061_jerk, f05_volume_at_capitulation_spike_at_low_w3_062_jerk, f05_volume_at_capitulation_spike_at_low_w5_063_jerk, f05_volume_at_capitulation_spike_at_low_w8_064_jerk, f05_volume_at_capitulation_spike_at_low_w10_065_jerk, f05_volume_at_capitulation_spike_at_low_w13_066_jerk, f05_volume_at_capitulation_spike_at_low_w21_067_jerk, f05_volume_at_capitulation_spike_at_low_w34_068_jerk, f05_volume_at_capitulation_spike_at_low_w55_069_jerk, f05_volume_at_capitulation_spike_at_low_w63_070_jerk, f05_volume_at_capitulation_spike_at_low_w89_071_jerk, f05_volume_at_capitulation_spike_at_low_w144_072_jerk, f05_volume_at_capitulation_spike_at_low_w252_073_jerk, f05_volume_at_capitulation_spike_at_low_w100_074_jerk, f05_volume_at_capitulation_spike_at_low_w120_075_jerk, f05_volume_at_capitulation_spike_at_low_w150_076_jerk, f05_volume_at_capitulation_spike_at_low_w180_077_jerk, f05_volume_at_capitulation_spike_at_low_w200_078_jerk, f05_volume_at_capitulation_spike_at_low_w220_079_jerk, f05_volume_at_capitulation_spike_at_low_w240_080_jerk, f05_volume_at_capitulation_vw_drop_w2_081_jerk, f05_volume_at_capitulation_vw_drop_w3_082_jerk, f05_volume_at_capitulation_vw_drop_w5_083_jerk, f05_volume_at_capitulation_vw_drop_w8_084_jerk, f05_volume_at_capitulation_vw_drop_w10_085_jerk, f05_volume_at_capitulation_vw_drop_w13_086_jerk, f05_volume_at_capitulation_vw_drop_w21_087_jerk, f05_volume_at_capitulation_vw_drop_w34_088_jerk, f05_volume_at_capitulation_vw_drop_w55_089_jerk, f05_volume_at_capitulation_vw_drop_w63_090_jerk, f05_volume_at_capitulation_vw_drop_w89_091_jerk, f05_volume_at_capitulation_vw_drop_w144_092_jerk, f05_volume_at_capitulation_vw_drop_w252_093_jerk, f05_volume_at_capitulation_vw_drop_w100_094_jerk, f05_volume_at_capitulation_vw_drop_w120_095_jerk, f05_volume_at_capitulation_vw_drop_w150_096_jerk, f05_volume_at_capitulation_vw_drop_w180_097_jerk, f05_volume_at_capitulation_vw_drop_w200_098_jerk, f05_volume_at_capitulation_vw_drop_w220_099_jerk, f05_volume_at_capitulation_vw_drop_w240_100_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w2_101_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w3_102_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w5_103_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w8_104_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w10_105_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w13_106_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w21_107_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w34_108_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w55_109_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w63_110_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w89_111_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w144_112_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w252_113_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w100_114_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w120_115_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w150_116_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w180_117_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w200_118_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w220_119_jerk, f05_volume_at_capitulation_rel_vol_worst_day_w240_120_jerk, f05_volume_at_capitulation_filler_w3_121_jerk, f05_volume_at_capitulation_filler_w5_122_jerk, f05_volume_at_capitulation_filler_w8_123_jerk, f05_volume_at_capitulation_filler_w10_124_jerk, f05_volume_at_capitulation_filler_w13_125_jerk, f05_volume_at_capitulation_filler_w21_126_jerk, f05_volume_at_capitulation_filler_w34_127_jerk, f05_volume_at_capitulation_filler_w55_128_jerk, f05_volume_at_capitulation_filler_w63_129_jerk, f05_volume_at_capitulation_filler_w89_130_jerk, f05_volume_at_capitulation_filler_w144_131_jerk, f05_volume_at_capitulation_filler_w252_132_jerk, f05_volume_at_capitulation_filler_w100_133_jerk, f05_volume_at_capitulation_filler_w120_134_jerk, f05_volume_at_capitulation_filler_w150_135_jerk, f05_volume_at_capitulation_filler_w180_136_jerk, f05_volume_at_capitulation_filler_w200_137_jerk, f05_volume_at_capitulation_filler_w220_138_jerk, f05_volume_at_capitulation_filler_w240_139_jerk, f05_volume_at_capitulation_filler_w2_140_jerk, f05_volume_at_capitulation_filler_w3_141_jerk, f05_volume_at_capitulation_filler_w5_142_jerk, f05_volume_at_capitulation_filler_w8_143_jerk, f05_volume_at_capitulation_filler_w10_144_jerk, f05_volume_at_capitulation_filler_w13_145_jerk, f05_volume_at_capitulation_filler_w21_146_jerk, f05_volume_at_capitulation_filler_w34_147_jerk, f05_volume_at_capitulation_filler_w55_148_jerk, f05_volume_at_capitulation_filler_w63_149_jerk, f05_volume_at_capitulation_filler_w89_150_jerk]:
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
