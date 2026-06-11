import pandas as pd
import numpy as np

def _capit_vol_spike(v, w): 
    return v / v.rolling(w, min_periods=1).mean().replace(0, np.nan)

def _capit_pressure(c, v, w): 
    return (c.pct_change().clip(upper=0).abs() * v).rolling(w, min_periods=1).mean()

def f05_volume_at_capitulation_spike_at_low_w150_076(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(150, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(150, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w180_077(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(180, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(180, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w200_078(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(200, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(200, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w220_079(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(220, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(220, min_periods=1).max()

def f05_volume_at_capitulation_spike_at_low_w240_080(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    is_low = c <= c.rolling(240, min_periods=1).min()
    return (v_spike.where(is_low, 0)).rolling(240, min_periods=1).max()

def f05_volume_at_capitulation_vw_drop_w2_081(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(2, min_periods=1).sum() / arg_volume.rolling(2, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w3_082(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(3, min_periods=1).sum() / arg_volume.rolling(3, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w5_083(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(5, min_periods=1).sum() / arg_volume.rolling(5, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w8_084(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(8, min_periods=1).sum() / arg_volume.rolling(8, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w10_085(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(10, min_periods=1).sum() / arg_volume.rolling(10, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w13_086(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(13, min_periods=1).sum() / arg_volume.rolling(13, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w21_087(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(21, min_periods=1).sum() / arg_volume.rolling(21, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w34_088(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(34, min_periods=1).sum() / arg_volume.rolling(34, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w55_089(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(55, min_periods=1).sum() / arg_volume.rolling(55, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w63_090(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(63, min_periods=1).sum() / arg_volume.rolling(63, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w89_091(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(89, min_periods=1).sum() / arg_volume.rolling(89, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w144_092(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(144, min_periods=1).sum() / arg_volume.rolling(144, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w252_093(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(252, min_periods=1).sum() / arg_volume.rolling(252, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w100_094(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(100, min_periods=1).sum() / arg_volume.rolling(100, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w120_095(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(120, min_periods=1).sum() / arg_volume.rolling(120, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w150_096(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(150, min_periods=1).sum() / arg_volume.rolling(150, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w180_097(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(180, min_periods=1).sum() / arg_volume.rolling(180, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w200_098(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(200, min_periods=1).sum() / arg_volume.rolling(200, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w220_099(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(220, min_periods=1).sum() / arg_volume.rolling(220, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_vw_drop_w240_100(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change().clip(upper=0).abs()
    return (ret * arg_volume).rolling(240, min_periods=1).sum() / arg_volume.rolling(240, min_periods=1).sum().replace(0, np.nan)

def f05_volume_at_capitulation_rel_vol_worst_day_w2_101(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(2, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(2, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(2, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w3_102(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(3, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(3, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(3, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w5_103(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(5, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(5, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(5, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w8_104(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(8, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(8, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(8, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w10_105(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(10, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(10, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(10, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w13_106(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(13, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(13, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(13, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w21_107(arg_close, arg_close_adj, arg_volume):
    c = arg_close
    ret = c.pct_change()
    worst_ret = ret.rolling(21, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(21, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(21, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w34_108(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(34, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(34, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(34, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w55_109(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(55, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(55, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(55, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w63_110(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(63, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(63, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(63, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w89_111(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(89, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(89, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(89, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w144_112(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(144, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(144, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(144, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w252_113(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(252, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(252, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(252, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w100_114(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(100, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(100, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(100, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w120_115(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(120, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(120, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(120, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w150_116(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(150, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(150, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(150, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w180_117(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(180, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(180, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(180, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w200_118(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(200, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(200, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(200, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w220_119(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(220, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(220, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(220, min_periods=1).max()

def f05_volume_at_capitulation_rel_vol_worst_day_w240_120(arg_close, arg_close_adj, arg_volume):
    c = arg_close_adj
    ret = c.pct_change()
    worst_ret = ret.rolling(240, min_periods=1).min()
    v_spike = arg_volume / arg_volume.rolling(240, min_periods=1).mean().replace(0, np.nan)
    return (v_spike.where(ret == worst_ret, 0)).rolling(240, min_periods=1).max()

def f05_volume_at_capitulation_filler_w3_121(arg_volume):
    return arg_volume.pct_change().rolling(3, min_periods=1).std()

def f05_volume_at_capitulation_filler_w5_122(arg_volume):
    return arg_volume.pct_change().rolling(5, min_periods=1).std()

def f05_volume_at_capitulation_filler_w8_123(arg_volume):
    return arg_volume.pct_change().rolling(8, min_periods=1).std()

def f05_volume_at_capitulation_filler_w10_124(arg_volume):
    return arg_volume.pct_change().rolling(10, min_periods=1).std()

def f05_volume_at_capitulation_filler_w13_125(arg_volume):
    return arg_volume.pct_change().rolling(13, min_periods=1).std()

def f05_volume_at_capitulation_filler_w21_126(arg_volume):
    return arg_volume.pct_change().rolling(21, min_periods=1).std()

def f05_volume_at_capitulation_filler_w34_127(arg_volume):
    return arg_volume.pct_change().rolling(34, min_periods=1).std()

def f05_volume_at_capitulation_filler_w55_128(arg_volume):
    return arg_volume.pct_change().rolling(55, min_periods=1).std()

def f05_volume_at_capitulation_filler_w63_129(arg_volume):
    return arg_volume.pct_change().rolling(63, min_periods=1).std()

def f05_volume_at_capitulation_filler_w89_130(arg_volume):
    return arg_volume.pct_change().rolling(89, min_periods=1).std()

def f05_volume_at_capitulation_filler_w144_131(arg_volume):
    return arg_volume.pct_change().rolling(144, min_periods=1).std()

def f05_volume_at_capitulation_filler_w252_132(arg_volume):
    return arg_volume.pct_change().rolling(252, min_periods=1).std()

def f05_volume_at_capitulation_filler_w100_133(arg_volume):
    return arg_volume.pct_change().rolling(100, min_periods=1).std()

def f05_volume_at_capitulation_filler_w120_134(arg_volume):
    return arg_volume.pct_change().rolling(120, min_periods=1).std()

def f05_volume_at_capitulation_filler_w150_135(arg_volume):
    return arg_volume.pct_change().rolling(150, min_periods=1).std()

def f05_volume_at_capitulation_filler_w180_136(arg_volume):
    return arg_volume.pct_change().rolling(180, min_periods=1).std()

def f05_volume_at_capitulation_filler_w200_137(arg_volume):
    return arg_volume.pct_change().rolling(200, min_periods=1).std()

def f05_volume_at_capitulation_filler_w220_138(arg_volume):
    return arg_volume.pct_change().rolling(220, min_periods=1).std()

def f05_volume_at_capitulation_filler_w240_139(arg_volume):
    return arg_volume.pct_change().rolling(240, min_periods=1).std()

def f05_volume_at_capitulation_filler_w2_140(arg_volume):
    return arg_volume.pct_change().rolling(2, min_periods=1).std()

def f05_volume_at_capitulation_filler_w3_141(arg_volume):
    return arg_volume.pct_change().rolling(3, min_periods=1).std()

def f05_volume_at_capitulation_filler_w5_142(arg_volume):
    return arg_volume.pct_change().rolling(5, min_periods=1).std()

def f05_volume_at_capitulation_filler_w8_143(arg_volume):
    return arg_volume.pct_change().rolling(8, min_periods=1).std()

def f05_volume_at_capitulation_filler_w10_144(arg_volume):
    return arg_volume.pct_change().rolling(10, min_periods=1).std()

def f05_volume_at_capitulation_filler_w13_145(arg_volume):
    return arg_volume.pct_change().rolling(13, min_periods=1).std()

def f05_volume_at_capitulation_filler_w21_146(arg_volume):
    return arg_volume.pct_change().rolling(21, min_periods=1).std()

def f05_volume_at_capitulation_filler_w34_147(arg_volume):
    return arg_volume.pct_change().rolling(34, min_periods=1).std()

def f05_volume_at_capitulation_filler_w55_148(arg_volume):
    return arg_volume.pct_change().rolling(55, min_periods=1).std()

def f05_volume_at_capitulation_filler_w63_149(arg_volume):
    return arg_volume.pct_change().rolling(63, min_periods=1).std()

def f05_volume_at_capitulation_filler_w89_150(arg_volume):
    return arg_volume.pct_change().rolling(89, min_periods=1).std()

def test_features():
    np.random.seed(42)
    n = 300
    arg_open = pd.Series(np.random.randn(n).cumsum() + 100)
    arg_high = arg_open + np.random.rand(n)
    arg_low = arg_open - np.random.rand(n)
    arg_close = arg_open + np.random.randn(n)
    arg_volume = pd.Series(np.random.rand(n) * 1000000)
    arg_close_adj = arg_close * 1.05
    
    for feat in [f05_volume_at_capitulation_spike_at_low_w150_076, f05_volume_at_capitulation_spike_at_low_w180_077, f05_volume_at_capitulation_spike_at_low_w200_078, f05_volume_at_capitulation_spike_at_low_w220_079, f05_volume_at_capitulation_spike_at_low_w240_080, f05_volume_at_capitulation_vw_drop_w2_081, f05_volume_at_capitulation_vw_drop_w3_082, f05_volume_at_capitulation_vw_drop_w5_083, f05_volume_at_capitulation_vw_drop_w8_084, f05_volume_at_capitulation_vw_drop_w10_085, f05_volume_at_capitulation_vw_drop_w13_086, f05_volume_at_capitulation_vw_drop_w21_087, f05_volume_at_capitulation_vw_drop_w34_088, f05_volume_at_capitulation_vw_drop_w55_089, f05_volume_at_capitulation_vw_drop_w63_090, f05_volume_at_capitulation_vw_drop_w89_091, f05_volume_at_capitulation_vw_drop_w144_092, f05_volume_at_capitulation_vw_drop_w252_093, f05_volume_at_capitulation_vw_drop_w100_094, f05_volume_at_capitulation_vw_drop_w120_095, f05_volume_at_capitulation_vw_drop_w150_096, f05_volume_at_capitulation_vw_drop_w180_097, f05_volume_at_capitulation_vw_drop_w200_098, f05_volume_at_capitulation_vw_drop_w220_099, f05_volume_at_capitulation_vw_drop_w240_100, f05_volume_at_capitulation_rel_vol_worst_day_w2_101, f05_volume_at_capitulation_rel_vol_worst_day_w3_102, f05_volume_at_capitulation_rel_vol_worst_day_w5_103, f05_volume_at_capitulation_rel_vol_worst_day_w8_104, f05_volume_at_capitulation_rel_vol_worst_day_w10_105, f05_volume_at_capitulation_rel_vol_worst_day_w13_106, f05_volume_at_capitulation_rel_vol_worst_day_w21_107, f05_volume_at_capitulation_rel_vol_worst_day_w34_108, f05_volume_at_capitulation_rel_vol_worst_day_w55_109, f05_volume_at_capitulation_rel_vol_worst_day_w63_110, f05_volume_at_capitulation_rel_vol_worst_day_w89_111, f05_volume_at_capitulation_rel_vol_worst_day_w144_112, f05_volume_at_capitulation_rel_vol_worst_day_w252_113, f05_volume_at_capitulation_rel_vol_worst_day_w100_114, f05_volume_at_capitulation_rel_vol_worst_day_w120_115, f05_volume_at_capitulation_rel_vol_worst_day_w150_116, f05_volume_at_capitulation_rel_vol_worst_day_w180_117, f05_volume_at_capitulation_rel_vol_worst_day_w200_118, f05_volume_at_capitulation_rel_vol_worst_day_w220_119, f05_volume_at_capitulation_rel_vol_worst_day_w240_120, f05_volume_at_capitulation_filler_w3_121, f05_volume_at_capitulation_filler_w5_122, f05_volume_at_capitulation_filler_w8_123, f05_volume_at_capitulation_filler_w10_124, f05_volume_at_capitulation_filler_w13_125, f05_volume_at_capitulation_filler_w21_126, f05_volume_at_capitulation_filler_w34_127, f05_volume_at_capitulation_filler_w55_128, f05_volume_at_capitulation_filler_w63_129, f05_volume_at_capitulation_filler_w89_130, f05_volume_at_capitulation_filler_w144_131, f05_volume_at_capitulation_filler_w252_132, f05_volume_at_capitulation_filler_w100_133, f05_volume_at_capitulation_filler_w120_134, f05_volume_at_capitulation_filler_w150_135, f05_volume_at_capitulation_filler_w180_136, f05_volume_at_capitulation_filler_w200_137, f05_volume_at_capitulation_filler_w220_138, f05_volume_at_capitulation_filler_w240_139, f05_volume_at_capitulation_filler_w2_140, f05_volume_at_capitulation_filler_w3_141, f05_volume_at_capitulation_filler_w5_142, f05_volume_at_capitulation_filler_w8_143, f05_volume_at_capitulation_filler_w10_144, f05_volume_at_capitulation_filler_w13_145, f05_volume_at_capitulation_filler_w21_146, f05_volume_at_capitulation_filler_w34_147, f05_volume_at_capitulation_filler_w55_148, f05_volume_at_capitulation_filler_w63_149, f05_volume_at_capitulation_filler_w89_150]:
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
