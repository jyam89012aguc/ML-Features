import pandas as pd
import numpy as np

def _capit_vol_spike(v, w): 
    return v / v.rolling(w, min_periods=1).mean().replace(0, np.nan)

def _capit_pressure(c, v, w): 
    return (c.pct_change().clip(upper=0).abs() * v).rolling(w, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w2_001(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(2, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w3_002(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(3, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w5_003(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(5, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w8_004(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(8, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w10_005(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(10, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w13_006(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(13, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w21_007(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(21, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w34_008(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(34, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w55_009(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(55, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w63_010(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(63, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w89_011(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(89, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w144_012(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(144, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w252_013(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(252, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w100_014(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(100, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w120_015(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(120, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w150_016(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(150, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w180_017(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(180, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w200_018(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(200, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w220_019(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(220, min_periods=1).mean()

def f05_volume_at_capitulation_pressure_w240_020(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    return (c.pct_change().clip(upper=0).abs() * arg_volume).rolling(240, min_periods=1).mean()

def f05_volume_at_capitulation_vol_spike_w2_021(arg_volume):
    v = arg_volume
    return v / v.rolling(2, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w3_022(arg_volume):
    v = arg_volume
    return v / v.rolling(3, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w5_023(arg_volume):
    v = arg_volume
    return v / v.rolling(5, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w8_024(arg_volume):
    v = arg_volume
    return v / v.rolling(8, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w10_025(arg_volume):
    v = arg_volume
    return v / v.rolling(10, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w13_026(arg_volume):
    v = arg_volume
    return v / v.rolling(13, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w21_027(arg_volume):
    v = arg_volume
    return v / v.rolling(21, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w34_028(arg_volume):
    v = arg_volume
    return v / v.rolling(34, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w55_029(arg_volume):
    v = arg_volume
    return v / v.rolling(55, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w63_030(arg_volume):
    v = arg_volume
    return v / v.rolling(63, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w89_031(arg_volume):
    v = arg_volume
    return v / v.rolling(89, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w144_032(arg_volume):
    v = arg_volume
    return v / v.rolling(144, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w252_033(arg_volume):
    v = arg_volume
    return v / v.rolling(252, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w100_034(arg_volume):
    v = arg_volume
    return v / v.rolling(100, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w120_035(arg_volume):
    v = arg_volume
    return v / v.rolling(120, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w150_036(arg_volume):
    v = arg_volume
    return v / v.rolling(150, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w180_037(arg_volume):
    v = arg_volume
    return v / v.rolling(180, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w200_038(arg_volume):
    v = arg_volume
    return v / v.rolling(200, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w220_039(arg_volume):
    v = arg_volume
    return v / v.rolling(220, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_spike_w240_040(arg_volume):
    v = arg_volume
    return v / v.rolling(240, min_periods=1).mean().replace(0, np.nan)

def f05_volume_at_capitulation_vol_range_down_w2_041(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(2, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w3_042(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(3, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w5_043(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(5, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w8_044(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(8, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w10_045(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(10, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w13_046(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(13, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w21_047(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(21, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w34_048(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(34, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w55_049(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(55, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w63_050(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(63, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w89_051(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(89, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w144_052(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(144, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w252_053(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(252, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w100_054(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(100, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w120_055(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(120, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w150_056(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(150, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w180_057(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(180, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w200_058(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(200, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w220_059(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(220, min_periods=1).mean()

def f05_volume_at_capitulation_vol_range_down_w240_060(arg_open, arg_high, arg_low, arg_close, arg_volume):
    range_hl = (arg_high - arg_low).replace(0, 1e-9)
    ratio = arg_volume / range_hl
    return (ratio.where(arg_close < arg_open, 0)).rolling(240, min_periods=1).mean()

def f05_volume_at_capitulation_spike_at_low_w2_061(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(2, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(2, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w3_062(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(3, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(3, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w5_063(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(5, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(5, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w8_064(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(8, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(8, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w10_065(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(10, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(10, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w13_066(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(13, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(13, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w21_067(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(21, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(21, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w34_068(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(34, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(34, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w55_069(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(55, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(55, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w63_070(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(63, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(63, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w89_071(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(89, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(89, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w144_072(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(144, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(144, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w252_073(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(252, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(252, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w100_074(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(100, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(100, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w120_075(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(120, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(120, min_periods=1).max()

def test_features():
    np.random.seed(42)
    n = 300
    arg_open = pd.Series(np.random.randn(n).cumsum() + 100)
    arg_high = arg_open + np.random.rand(n)
    arg_low = arg_open - np.random.rand(n)
    arg_close = arg_open + np.random.randn(n)
    arg_volume = pd.Series(np.random.rand(n) * 1000000)
    arg_close_adj = arg_close * 1.05
    
    for feat in [f05_volume_at_capitulation_pressure_w2_001, f05_volume_at_capitulation_pressure_w3_002, f05_volume_at_capitulation_pressure_w5_003, f05_volume_at_capitulation_pressure_w8_004, f05_volume_at_capitulation_pressure_w10_005, f05_volume_at_capitulation_pressure_w13_006, f05_volume_at_capitulation_pressure_w21_007, f05_volume_at_capitulation_pressure_w34_008, f05_volume_at_capitulation_pressure_w55_009, f05_volume_at_capitulation_pressure_w63_010, f05_volume_at_capitulation_pressure_w89_011, f05_volume_at_capitulation_pressure_w144_012, f05_volume_at_capitulation_pressure_w252_013, f05_volume_at_capitulation_pressure_w100_014, f05_volume_at_capitulation_pressure_w120_015, f05_volume_at_capitulation_pressure_w150_016, f05_volume_at_capitulation_pressure_w180_017, f05_volume_at_capitulation_pressure_w200_018, f05_volume_at_capitulation_pressure_w220_019, f05_volume_at_capitulation_pressure_w240_020, f05_volume_at_capitulation_vol_spike_w2_021, f05_volume_at_capitulation_vol_spike_w3_022, f05_volume_at_capitulation_vol_spike_w5_023, f05_volume_at_capitulation_vol_spike_w8_024, f05_volume_at_capitulation_vol_spike_w10_025, f05_volume_at_capitulation_vol_spike_w13_026, f05_volume_at_capitulation_vol_spike_w21_027, f05_volume_at_capitulation_vol_spike_w34_028, f05_volume_at_capitulation_vol_spike_w55_029, f05_volume_at_capitulation_vol_spike_w63_030, f05_volume_at_capitulation_vol_spike_w89_031, f05_volume_at_capitulation_vol_spike_w144_032, f05_volume_at_capitulation_vol_spike_w252_033, f05_volume_at_capitulation_vol_spike_w100_034, f05_volume_at_capitulation_vol_spike_w120_035, f05_volume_at_capitulation_vol_spike_w150_036, f05_volume_at_capitulation_vol_spike_w180_037, f05_volume_at_capitulation_vol_spike_w200_038, f05_volume_at_capitulation_vol_spike_w220_039, f05_volume_at_capitulation_vol_spike_w240_040, f05_volume_at_capitulation_vol_range_down_w2_041, f05_volume_at_capitulation_vol_range_down_w3_042, f05_volume_at_capitulation_vol_range_down_w5_043, f05_volume_at_capitulation_vol_range_down_w8_044, f05_volume_at_capitulation_vol_range_down_w10_045, f05_volume_at_capitulation_vol_range_down_w13_046, f05_volume_at_capitulation_vol_range_down_w21_047, f05_volume_at_capitulation_vol_range_down_w34_048, f05_volume_at_capitulation_vol_range_down_w55_049, f05_volume_at_capitulation_vol_range_down_w63_050, f05_volume_at_capitulation_vol_range_down_w89_051, f05_volume_at_capitulation_vol_range_down_w144_052, f05_volume_at_capitulation_vol_range_down_w252_053, f05_volume_at_capitulation_vol_range_down_w100_054, f05_volume_at_capitulation_vol_range_down_w120_055, f05_volume_at_capitulation_vol_range_down_w150_056, f05_volume_at_capitulation_vol_range_down_w180_057, f05_volume_at_capitulation_vol_range_down_w200_058, f05_volume_at_capitulation_vol_range_down_w220_059, f05_volume_at_capitulation_vol_range_down_w240_060, f05_volume_at_capitulation_spike_at_low_w2_061, f05_volume_at_capitulation_spike_at_low_w3_062, f05_volume_at_capitulation_spike_at_low_w5_063, f05_volume_at_capitulation_spike_at_low_w8_064, f05_volume_at_capitulation_spike_at_low_w10_065, f05_volume_at_capitulation_spike_at_low_w13_066, f05_volume_at_capitulation_spike_at_low_w21_067, f05_volume_at_capitulation_spike_at_low_w34_068, f05_volume_at_capitulation_spike_at_low_w55_069, f05_volume_at_capitulation_spike_at_low_w63_070, f05_volume_at_capitulation_spike_at_low_w89_071, f05_volume_at_capitulation_spike_at_low_w144_072, f05_volume_at_capitulation_spike_at_low_w252_073, f05_volume_at_capitulation_spike_at_low_w100_074, f05_volume_at_capitulation_spike_at_low_w120_075]:
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
