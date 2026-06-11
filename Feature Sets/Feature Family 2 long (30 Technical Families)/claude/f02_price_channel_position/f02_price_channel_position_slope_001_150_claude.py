"""f02_price_channel_position slope (1st deriv): base.diff(k)."""
import numpy as np
import pandas as pd

def f02pc_f02_price_channel_position_chpos_20d_slope_v001_signal(close,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    base = (close - lo) / (hi - lo).replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chposlg_55d_slope_v002_signal(closeadj,high,low):
    hi = high.rolling(55,min_periods=55).max()
    lo = low.rolling(55,min_periods=55).min()
    eps = (hi - lo) * 0.001 + 1e-9
    base = np.log((closeadj - lo) + eps) - np.log((hi - closeadj) + eps)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chmid_200d_slope_v003_signal(closeadj,high,low):
    hi = high.rolling(200,min_periods=200).max()
    lo = low.rolling(200,min_periods=200).min()
    mid = (hi + lo) / 2.0
    side = np.sign(closeadj - mid).where(~mid.isna())
    base = side.ewm(alpha=0.02,adjust=False,min_periods=50).mean()
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dtop_10d_slope_v004_signal(close,high):
    hi = high.rolling(10,min_periods=10).max()
    base = (hi - close) / close.replace(0,np.nan)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dbot_50d_slope_v005_signal(closeadj,low):
    lo = low.rolling(50,min_periods=50).min()
    base = (closeadj - lo) / closeadj.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dtoplg_200d_slope_v006_signal(closeadj,high):
    hi = high.rolling(200,min_periods=200).max()
    base = np.log(hi / closeadj.replace(0,np.nan))
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chwid_20d_slope_v007_signal(close,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    base = (hi - lo) / close.replace(0,np.nan)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chwidlg_63d_slope_v008_signal(closeadj,high,low):
    hi = high.rolling(63,min_periods=63).max()
    lo = low.rolling(63,min_periods=63).min()
    base = np.log(hi.replace(0,np.nan) / lo.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chwidrk_120d_slope_v009_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    base = w.rolling(120,min_periods=60).rank(pct=True) - 0.5
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chwidslp_50d_slope_v010_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    base = w.diff(21) / w.abs().rolling(21,min_periods=21).mean().replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chwidrat_50d_slope_v011_signal(closeadj,high,low):
    hi10 = high.rolling(10,min_periods=10).max()
    lo10 = low.rolling(10,min_periods=10).min()
    hi50 = high.rolling(50,min_periods=50).max()
    lo50 = low.rolling(50,min_periods=50).min()
    w10 = (hi10 - lo10).replace(0,np.nan)
    w50 = (hi50 - lo50).replace(0,np.nan)
    base = np.log(w10) - np.log(w50)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chpinch_60d_slope_v012_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    rk = w.rolling(60,min_periods=30).rank(pct=True)
    base = (rk < 0.20).astype(float)
    base[rk.isna()] = np.nan
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chhislp_30d_slope_v013_signal(closeadj,high):
    hi = high.rolling(30,min_periods=30).max()
    base = hi.diff(10) / hi.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chloslp_30d_slope_v014_signal(closeadj,low):
    lo = low.rolling(30,min_periods=30).min()
    base = np.sign(lo.diff(10)).where(~lo.isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chmidslp_100d_slope_v015_signal(closeadj,high,low):
    hi = high.rolling(100,min_periods=100).max()
    lo = low.rolling(100,min_periods=100).min()
    mid = (hi + lo) / 2.0
    base = mid.diff(21) / mid.replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chexpdv_30d_slope_v016_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    base = (hi.diff(10) / hi.replace(0,np.nan)) - (lo.diff(10) / lo.replace(0,np.nan))
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkup_20d_slope_v017_signal(close,high):
    prior = high.shift(1).rolling(20,min_periods=20).max()
    base = np.sign(close - prior).astype(float)
    base[prior.isna()] = np.nan
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkdn_55d_slope_v018_signal(closeadj,low):
    prior = low.shift(1).rolling(55,min_periods=55).min()
    base = np.sign(closeadj - prior).astype(float)
    base[prior.isna()] = np.nan
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkcnt_60d_slope_v019_signal(closeadj,high):
    prior20 = high.shift(1).rolling(20,min_periods=20).max()
    brk = (closeadj > prior20).astype(float)
    brk[prior20.isna()] = np.nan
    base = brk.rolling(60,min_periods=30).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkbal_50d_slope_v020_signal(closeadj,high,low):
    ph = high.shift(1).rolling(20,min_periods=20).max()
    pl = low.shift(1).rolling(20,min_periods=20).min()
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    up[ph.isna()] = np.nan
    dn[pl.isna()] = np.nan
    base = up.rolling(50,min_periods=25).sum() - dn.rolling(50,min_periods=25).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_streakup_20d_slope_v021_signal(close,high):
    hi = high.rolling(20,min_periods=20).max()
    lo = close.rolling(20,min_periods=20).min()
    thr = lo + 0.8 * (hi - lo)
    hit = (close >= thr).astype(float)
    grp = (hit != hit.shift()).cumsum()
    base = hit.groupby(grp).cumsum().where(~hi.isna())
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dayslast_50d_slope_v022_signal(closeadj,high):
    hi = high.rolling(50,min_periods=50).max()
    at_top = (closeadj >= hi)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    last_hit = idx.where(at_top).ffill()
    base = (idx - last_hit).clip(upper=50.0).where(~hi.isna())
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dayslo_100d_slope_v023_signal(closeadj,low):
    lo = low.rolling(100,min_periods=100).min()
    at_bot = (low <= lo)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    last_hit = idx.where(at_bot).ffill()
    base = (idx - last_hit).clip(upper=100.0).where(~lo.isna())
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dayswide_60d_slope_v024_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    rk = w.rolling(60,min_periods=30).rank(pct=True)
    wide = (rk >= 0.90)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    last_hit = idx.where(wide).ffill()
    base = (idx - last_hit).clip(upper=60.0).where(~rk.isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_donst_30d_slope_v025_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pd.Series(0.0,index=closeadj.index,dtype=float)
    base[pos >= 0.75] = 1.0
    base[pos <= 0.25] = -1.0
    base[pos.isna()] = np.nan
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_donqt_75d_slope_v026_signal(closeadj,high,low):
    hi = high.rolling(75,min_periods=75).max()
    lo = low.rolling(75,min_periods=75).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pd.Series(np.nan,index=closeadj.index,dtype=float)
    base[pos < 0.25] = 0.0
    base[(pos >= 0.25) & (pos < 0.5)] = 1.0
    base[(pos >= 0.5) & (pos < 0.75)] = 2.0
    base[pos >= 0.75] = 3.0
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_stoK_14d_slope_v027_signal(close,high,low):
    hi = high.rolling(14,min_periods=14).max()
    lo = low.rolling(14,min_periods=14).min()
    base = 100.0 * (close - lo) / (hi - lo).replace(0,np.nan)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_stoXdrt_14d_slope_v028_signal(close,high,low):
    hi = high.rolling(14,min_periods=14).max()
    lo = low.rolling(14,min_periods=14).min()
    k = 100.0 * (close - lo) / (hi - lo).replace(0,np.nan)
    base = k.diff(5) - 5.0 * k.diff(1)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_stoSK_42d_slope_v029_signal(closeadj,high,low):
    hi = high.rolling(42,min_periods=42).max()
    lo = low.rolling(42,min_periods=42).min()
    k = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = k.rolling(5,min_periods=5).mean() - 0.5
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_stochmi_25d_slope_v030_signal(closeadj,high,low):
    hi = high.rolling(25,min_periods=25).max()
    lo = low.rolling(25,min_periods=25).min()
    mid = (hi + lo) / 2.0
    num = (closeadj - mid).ewm(span=5,adjust=False,min_periods=5).mean()
    den = ((hi - lo) / 2.0).ewm(span=5,adjust=False,min_periods=5).mean()
    base = num / den.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_wpr_10d_slope_v031_signal(close,high,low):
    hi = high.rolling(10,min_periods=10).max()
    lo = low.rolling(10,min_periods=10).min()
    base = -100.0 * (hi - close) / (hi - lo).replace(0,np.nan)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_halfbin_63d_slope_v032_signal(closeadj,high,low):
    hi = high.rolling(63,min_periods=63).max()
    lo = low.rolling(63,min_periods=63).min()
    mid = (hi + lo) / 2.0
    base = np.sign(closeadj - mid).astype(float)
    base[mid.isna()] = np.nan
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_asymabs_30d_slope_v033_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    a = (hi - closeadj).abs() + 1e-9
    b = (closeadj - lo).abs() + 1e-9
    base = np.log(a) - np.log(b)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_lastside_40d_slope_v034_signal(closeadj,high,low):
    hi = high.rolling(40,min_periods=40).max()
    lo = low.rolling(40,min_periods=40).min()
    at_top = (high >= hi)
    at_bot = (low <= lo)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    top_idx = idx.where(at_top).ffill()
    bot_idx = idx.where(at_bot).ffill()
    state = np.sign(top_idx - bot_idx).where(~(hi.isna() | lo.isna()))
    return state.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_topvsbot_60d_slope_v035_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    top_hit = (pos >= 0.95).astype(float)
    bot_hit = (pos <= 0.05).astype(float)
    top_hit[pos.isna()] = np.nan
    bot_hit[pos.isna()] = np.nan
    base = top_hit.rolling(60,min_periods=30).sum() - bot_hit.rolling(60,min_periods=30).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_timetop_60d_slope_v036_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    in_top = (pos >= 0.90).astype(float)
    in_top[pos.isna()] = np.nan
    base = in_top.rolling(60,min_periods=30).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_timebot_120d_slope_v037_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    in_bot = (pos <= 0.10).astype(float)
    in_bot[pos.isna()] = np.nan
    base = in_bot.rolling(120,min_periods=60).mean()
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_anchhi_30d_slope_v038_signal(closeadj,high):
    hi = high.rolling(30,min_periods=30).max()
    base = np.log(closeadj.replace(0,np.nan) / hi.replace(0,np.nan))
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_anchlo_100d_slope_v039_signal(closeadj,low):
    lo = low.rolling(100,min_periods=100).min()
    base = np.log(closeadj.replace(0,np.nan) / lo.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_decay_50d_slope_v040_signal(closeadj,high):
    hi = high.rolling(50,min_periods=50).max()
    sig = closeadj.diff().rolling(50,min_periods=50).std()
    base = (hi - closeadj) / sig.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_vwapchpos_30d_slope_v041_signal(closeadj,high,low,volume):
    typ = (high + low + closeadj) / 3.0
    pv = typ * volume
    vwap = pv.rolling(30,min_periods=30).sum() / volume.rolling(30,min_periods=30).sum().replace(0,np.nan)
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    base = (closeadj - vwap) / (hi - lo).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_volbrk_40d_slope_v042_signal(closeadj,high,volume):
    ph = high.shift(1).rolling(20,min_periods=20).max()
    brk = (closeadj > ph).astype(float)
    brk[ph.isna()] = np.nan
    brk_vol = (brk * volume).rolling(40,min_periods=20).sum()
    all_vol = volume.rolling(40,min_periods=20).sum().replace(0,np.nan)
    avg_brk = brk_vol / (brk.rolling(40,min_periods=20).sum().replace(0,np.nan))
    avg_all = all_vol / 40.0
    base = np.log(avg_brk.replace(0,np.nan) / avg_all.replace(0,np.nan))
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posrk_120d_slope_v043_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.rolling(120,min_periods=60).rank(pct=True) - 0.5
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posstd_60d_slope_v044_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.rolling(60,min_periods=30).std()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posskew_90d_slope_v045_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.rolling(90,min_periods=45).skew()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_zscpos_50d_slope_v046_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    mu = pos.rolling(50,min_periods=25).mean()
    sd = pos.rolling(50,min_periods=25).std()
    base = (pos - mu) / sd.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_nearedge_30d_slope_v047_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    width = (hi - lo).replace(0,np.nan)
    to_top = (hi - closeadj) / width
    to_bot = (closeadj - lo) / width
    nearest = pd.concat([to_top,to_bot],axis=1).min(axis=1)
    s = np.sign(to_bot - to_top)
    base = s * nearest
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posagree_60d_slope_v048_signal(closeadj,high,low):
    h10 = high.rolling(10,min_periods=10).max()
    l10 = low.rolling(10,min_periods=10).min()
    h60 = high.rolling(60,min_periods=60).max()
    l60 = low.rolling(60,min_periods=60).min()
    p10 = (closeadj - l10) / (h10 - l10).replace(0,np.nan) - 0.5
    p60 = (closeadj - l60) / (h60 - l60).replace(0,np.nan) - 0.5
    base = np.sign(p10) * np.sign(p60)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_tanhdt_25d_slope_v049_signal(close,high,low):
    hi = high.rolling(25,min_periods=25).max()
    lo = low.rolling(25,min_periods=25).min()
    pos = (close - lo) / (hi - lo).replace(0,np.nan)
    near_top = (pos >= 0.9).astype(float)
    near_bot = (pos <= 0.1).astype(float)
    state = near_top - near_bot
    grp = (state != state.shift()).cumsum()
    streak = state.groupby(grp).cumcount() + 1
    base = (state * streak).where(~hi.isna())
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_diffpos_50d_slope_v050_signal(closeadj,high,low):
    h10 = high.rolling(10,min_periods=10).max()
    l10 = low.rolling(10,min_periods=10).min()
    h50 = high.rolling(50,min_periods=50).max()
    l50 = low.rolling(50,min_periods=50).min()
    p10 = (closeadj - l10) / (h10 - l10).replace(0,np.nan)
    p50 = (closeadj - l50) / (h50 - l50).replace(0,np.nan)
    base = p10 - p50
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_diffdt_100d_slope_v051_signal(closeadj,high,low):
    h20 = high.rolling(20,min_periods=20).max()
    h100 = high.rolling(100,min_periods=100).max()
    a = (h20 - closeadj) + 1e-9
    b = (h100 - closeadj) + 1e-9
    base = np.log(a) - np.log(b)
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_midcross_60d_slope_v052_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    mid = (hi + lo) / 2.0
    sgn = np.sign(closeadj - mid)
    cross = (sgn != sgn.shift(1)).astype(float)
    cross[sgn.isna() | sgn.shift(1).isna()] = np.nan
    base = cross.rolling(60,min_periods=30).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_topcnt_40d_slope_v053_signal(closeadj,high):
    h5p = high.shift(1).rolling(5,min_periods=5).max()
    h20p = high.shift(1).rolling(20,min_periods=20).max()
    comp = ((closeadj > h5p) & (closeadj > h20p)).astype(float)
    comp[h5p.isna() | h20p.isna()] = np.nan
    base = comp.rolling(40,min_periods=20).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hirk_100d_slope_v054_signal(closeadj,high,low):
    h100 = high.rolling(100,min_periods=100).max()
    l100 = low.rolling(100,min_periods=100).min()
    top_hit = (high >= h100).astype(float).where(~h100.isna())
    bot_hit = (low <= l100).astype(float).where(~l100.isna())
    base = top_hit.rolling(100,min_periods=50).sum() - bot_hit.rolling(100,min_periods=50).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_lork_60d_slope_v055_signal(closeadj,high,low):
    h60 = high.rolling(60,min_periods=60).max()
    l60 = low.rolling(60,min_periods=60).min()
    at_bot = (low <= l60).astype(float)
    at_top = (low >= h60).astype(float)
    state = at_top - at_bot
    grp = (state != state.shift()).cumsum()
    streak = state.groupby(grp).cumcount() + 1
    base = (state * streak).where(~l60.isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chacc_50d_slope_v056_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    mid = (hi + lo) / 2.0
    base = (mid - 2.0 * mid.shift(10) + mid.shift(20)) / mid.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_widacc_30d_slope_v057_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    w = (hi - lo)
    base = (w - 2.0 * w.shift(10) + w.shift(20)) / w.abs().rolling(20,min_periods=20).mean().replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_ulpos_20d_slope_v058_signal(close,high,low):
    hi = high.rolling(20,min_periods=20).max()
    dd = (hi - close) / hi.replace(0,np.nan)
    base = (dd ** 2).rolling(20,min_periods=20).mean().pow(0.5)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_uppos_30d_slope_v059_signal(closeadj,high,low):
    lo = low.rolling(30,min_periods=30).min()
    ru = (closeadj - lo) / lo.replace(0,np.nan)
    base = (ru ** 2).rolling(30,min_periods=30).mean().pow(0.5)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_atrwid_20d_slope_v060_signal(close,high,low):
    tr = pd.concat([(high - low),(high - close.shift(1)).abs(),(low - close.shift(1)).abs()],axis=1).max(axis=1)
    atr = tr.rolling(20,min_periods=20).mean()
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    base = (hi - lo) / atr.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_atrposd_30d_slope_v061_signal(closeadj,high,low):
    tr = pd.concat([(high - low),(high - closeadj.shift(1)).abs(),(low - closeadj.shift(1)).abs()],axis=1).max(axis=1)
    atr = tr.rolling(30,min_periods=30).mean()
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    mid = (hi + lo) / 2.0
    raw = (closeadj - mid) / atr.replace(0,np.nan)
    base = np.floor(raw)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_newhicnt_50d_slope_v062_signal(closeadj,high):
    prior = high.shift(1).rolling(50,min_periods=50).max()
    new_hi = (high > prior).astype(float)
    new_hi[prior.isna()] = np.nan
    base = new_hi.rolling(50,min_periods=25).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_newlocnt_30d_slope_v063_signal(closeadj,low):
    prior = low.shift(1).rolling(30,min_periods=30).min()
    new_lo = (low < prior).astype(float)
    new_lo[prior.isna()] = np.nan
    base = new_lo.rolling(30,min_periods=15).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pierce_30d_slope_v064_signal(close,high,low):
    ph = high.shift(1).rolling(30,min_periods=30).max()
    pl = low.shift(1).rolling(30,min_periods=30).min()
    width = (ph - pl).replace(0,np.nan)
    up = (close - ph).clip(lower=0.0) / width
    dn = (pl - close).clip(lower=0.0) / width
    base = up - dn
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pierce_100d_slope_v065_signal(closeadj,high,low):
    ph = high.shift(1).rolling(100,min_periods=100).max()
    pl = low.shift(1).rolling(100,min_periods=100).min()
    width = (ph - pl).replace(0,np.nan)
    up = (closeadj - ph).clip(lower=0.0) / width
    dn = (pl - closeadj).clip(lower=0.0) / width
    base = up - dn
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_decayrt_70d_slope_v066_signal(closeadj,high):
    hi = high.rolling(70,min_periods=70).max()
    drop = (hi - closeadj) / closeadj.replace(0,np.nan)
    base = drop.diff(21) / 21.0
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hivol_60d_slope_v067_signal(closeadj,high):
    hi = high.rolling(20,min_periods=20).max()
    sd = hi.rolling(60,min_periods=30).std()
    mu = hi.rolling(60,min_periods=30).mean().replace(0,np.nan)
    base = sd / mu
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_lovol_90d_slope_v068_signal(closeadj,low):
    lo = low.rolling(40,min_periods=40).min()
    sd = lo.rolling(90,min_periods=45).std()
    mu = lo.rolling(90,min_periods=45).mean().replace(0,np.nan)
    base = sd / mu
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posac1_60d_slope_v069_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.rolling(60,min_periods=40).corr(pos.shift(1))
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hiprgr_30d_slope_v070_signal(closeadj,high):
    hi = high.rolling(30,min_periods=30).max()
    base = (hi - hi.shift(21)) / hi.shift(21).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_loprgr_30d_slope_v071_signal(closeadj,low):
    lo = low.rolling(30,min_periods=30).min()
    base = (lo - lo.shift(21)) / lo.shift(21).replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pkfill_30d_slope_v072_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    touch = (high >= hi).astype(float)
    touch[hi.isna()] = np.nan
    base = touch.rolling(30,min_periods=15).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pivpos_50d_slope_v073_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    c50 = closeadj.rolling(50,min_periods=50).mean()
    piv = (hi + lo + c50) / 3.0
    r1 = 2.0 * piv - lo
    s1 = 2.0 * piv - hi
    above = (closeadj > r1).astype(float).where(~piv.isna())
    below = (closeadj < s1).astype(float).where(~piv.isna())
    base = above.rolling(50,min_periods=25).sum() - below.rolling(50,min_periods=25).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hlrk_80d_slope_v074_signal(closeadj,high,low):
    hl = (high - low) / closeadj.replace(0,np.nan)
    base = hl.rolling(80,min_periods=40).rank(pct=True) - 0.5
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_regpos_150d_slope_v075_signal(closeadj,high,low):
    pri_hi = high.shift(1).rolling(150,min_periods=150).max()
    pri_lo = low.shift(1).rolling(150,min_periods=150).min()
    nh = (high > pri_hi).astype(float).where(~pri_hi.isna())
    nl = (low < pri_lo).astype(float).where(~pri_lo.isna())
    base = (nh.rolling(150,min_periods=75).sum() - nl.rolling(150,min_periods=75).sum()) / 150.0
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hl2pos_20d_slope_v076_signal(close,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    hl2 = ((high + low) / 2.0).rolling(20,min_periods=20).mean()
    bar_rng = (high - low).rolling(20,min_periods=20).mean()
    width = (hi - lo).replace(0,np.nan)
    base = np.sign(close - hl2) * (bar_rng / width)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_hccpos_42d_slope_v077_signal(closeadj,high,low):
    hi = high.rolling(42,min_periods=42).max()
    lo = low.rolling(42,min_periods=42).min()
    hlc3 = ((high + low + closeadj) / 3.0).rolling(42,min_periods=42).mean()
    base = np.sign(closeadj - hlc3).where(~hi.isna()) * ((hi - lo) / closeadj.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_ohlcrng_30d_slope_v078_signal(closeadj,open_,high,low):
    bar_rng = (high - low).rolling(30,min_periods=30).mean()
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    chrng = (hi - lo).replace(0,np.nan)
    base = bar_rng / chrng
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_obpos_10d_slope_v079_signal(close,open_,high,low):
    hi = high.rolling(10,min_periods=10).max()
    lo = low.rolling(10,min_periods=10).min()
    base = np.sign((open_ - lo) - (hi - open_)).where(~hi.isna())
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_truebw_25d_slope_v080_signal(closeadj,high,low):
    tr = pd.concat([(high - low),(high - closeadj.shift(1)).abs(),(low - closeadj.shift(1)).abs()],axis=1).max(axis=1)
    base = tr.rolling(25,min_periods=25).max() / closeadj.replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_kelt_20d_slope_v081_signal(close,high,low):
    ema = close.ewm(span=20,adjust=False,min_periods=20).mean()
    tr = pd.concat([(high - low),(high - close.shift(1)).abs(),(low - close.shift(1)).abs()],axis=1).max(axis=1)
    atr = tr.rolling(20,min_periods=20).mean()
    base = (close - ema) / (2.0 * atr).replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_keltatr_50d_slope_v082_signal(closeadj,high,low):
    tr = pd.concat([(high - low),(high - closeadj.shift(1)).abs(),(low - closeadj.shift(1)).abs()],axis=1).max(axis=1)
    atr = tr.rolling(50,min_periods=50).mean()
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    base = atr * np.sqrt(50.0) / (hi - lo).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_keltdiv_30d_slope_v083_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    don = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    ema = closeadj.ewm(span=30,adjust=False,min_periods=30).mean()
    tr = pd.concat([(high - low),(high - closeadj.shift(1)).abs(),(low - closeadj.shift(1)).abs()],axis=1).max(axis=1)
    atr = tr.rolling(30,min_periods=30).mean()
    kelt_b = (closeadj - (ema - 2.0 * atr)) / (4.0 * atr).replace(0,np.nan)
    base = don - kelt_b
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_bollhi_20d_slope_v084_signal(close,high):
    sma = high.rolling(20,min_periods=20).mean()
    sd = high.rolling(20,min_periods=20).std()
    base = (high - sma) / (2.0 * sd).replace(0,np.nan)
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_bolllo_30d_slope_v085_signal(closeadj,low):
    sma = low.rolling(30,min_periods=30).mean()
    sd = low.rolling(30,min_periods=30).std()
    base = (low - sma) / (2.0 * sd).replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_bollratlo_60d_slope_v086_signal(closeadj,high,low):
    sh = high.rolling(60,min_periods=60).std()
    sl = low.rolling(60,min_periods=60).std()
    base = np.log(sh.replace(0,np.nan)) - np.log(sl.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_qchpos_30d_slope_v087_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).quantile(0.95)
    lo = low.rolling(30,min_periods=30).quantile(0.05)
    halfw = (hi - lo).replace(0,np.nan) / 2.0
    above = (closeadj - hi).clip(lower=0.0) / halfw
    below = (lo - closeadj).clip(lower=0.0) / halfw
    base = above - below
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_qchwid_60d_slope_v088_signal(closeadj,high,low):
    hi = high.rolling(60,min_periods=60).quantile(0.95)
    lo = low.rolling(60,min_periods=60).quantile(0.05)
    w = (hi - lo) / closeadj.replace(0,np.nan)
    base = np.log(w.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_qchdiff_50d_slope_v089_signal(closeadj,high,low):
    hi_max = high.rolling(50,min_periods=50).max()
    hi_q = high.rolling(50,min_periods=50).quantile(0.95)
    base = (hi_max - hi_q) / closeadj.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_iqrch_45d_slope_v090_signal(closeadj,high,low):
    hi = high.rolling(45,min_periods=45).quantile(0.75)
    lo = low.rolling(45,min_periods=45).quantile(0.25)
    iqr = (hi - lo).replace(0,np.nan)
    above = (closeadj - hi).clip(lower=0.0) / iqr
    below = (lo - closeadj).clip(lower=0.0) / iqr
    base = above - below
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_medch_30d_slope_v091_signal(closeadj,high,low):
    med = closeadj.rolling(30,min_periods=30).median()
    side = np.sign(closeadj - med)
    flip = (side != side.shift(1)).astype(float).where(~med.isna())
    base = flip.rolling(30,min_periods=15).sum() - 5.0
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_qchhi_100d_slope_v092_signal(closeadj,high):
    hi = high.rolling(100,min_periods=100).quantile(0.95)
    base = np.log(hi / closeadj.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brk52w_252d_slope_v093_signal(closeadj,high):
    prior = high.shift(1).rolling(252,min_periods=200).max()
    flag = (closeadj > prior).astype(float)
    flag[prior.isna()] = np.nan
    return flag.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pos252_252d_slope_v094_signal(closeadj,high,low):
    hi = high.rolling(252,min_periods=200).max()
    lo = low.rolling(252,min_periods=200).min()
    mid = (hi + lo) / 2.0
    up = (closeadj >= mid).astype(float).where(~mid.isna())
    dn = (closeadj <= mid).astype(float).where(~mid.isna())
    base = up.ewm(alpha=0.05,adjust=False,min_periods=50).mean() - dn.ewm(alpha=0.05,adjust=False,min_periods=50).mean()
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dist52h_252d_slope_v095_signal(closeadj,high):
    hi = high.rolling(252,min_periods=200).max()
    base = np.log(hi / closeadj.replace(0,np.nan))
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_dist52l_252d_slope_v096_signal(closeadj,low):
    lo = low.rolling(252,min_periods=200).min()
    base = np.log(closeadj / lo.replace(0,np.nan))
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_zh252_252d_slope_v097_signal(closeadj,high,low):
    hi = high.rolling(252,min_periods=200).max()
    lo = low.rolling(252,min_periods=200).min()
    new_h = (high >= hi).astype(float).where(~hi.isna())
    new_l = (low <= lo).astype(float).where(~lo.isna())
    base = new_h.rolling(252,min_periods=100).mean() - new_l.rolling(252,min_periods=100).mean()
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_swhipos_30d_slope_v098_signal(closeadj,high):
    swing = high.rolling(5,min_periods=5).max().shift(-2)
    is_swing = (high == swing)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    last_hit = idx.where(is_swing).ffill()
    base = (idx - last_hit).clip(upper=30.0).where(~swing.isna())
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_swlopos_30d_slope_v099_signal(closeadj,low):
    swing = low.rolling(5,min_periods=5).min().shift(-2)
    is_swing = (low == swing)
    idx = pd.Series(np.arange(len(closeadj),dtype=float),index=closeadj.index)
    last_hit = idx.where(is_swing).ffill()
    base = (idx - last_hit).clip(upper=30.0).where(~swing.isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_swdir_30d_slope_v100_signal(closeadj,high,low):
    swh = high.rolling(5,min_periods=5).max().shift(-2)
    swl = low.rolling(5,min_periods=5).min().shift(-2)
    h_flag = (high == swh).astype(float)
    l_flag = (low == swl).astype(float)
    h_flag[swh.isna()] = np.nan
    l_flag[swl.isna()] = np.nan
    base = np.sign(h_flag.rolling(30,min_periods=15).sum() - l_flag.rolling(30,min_periods=15).sum())
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_topcond_60d_slope_v101_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    w = hi - lo
    wmed = w.rolling(60,min_periods=30).median()
    flag = ((pos >= 0.8) & (w > wmed)).astype(float)
    flag[pos.isna() | wmed.isna()] = np.nan
    base = flag.rolling(60,min_periods=30).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_bothcnt_50d_slope_v102_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    flag = ((pos >= 0.9) & (closeadj > closeadj.shift(1))).astype(float)
    flag[pos.isna()] = np.nan
    base = flag.rolling(50,min_periods=25).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pinchbrk_70d_slope_v103_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    rk = w.rolling(70,min_periods=35).rank(pct=True)
    ph = high.shift(1).rolling(10,min_periods=10).max()
    brk = (closeadj > ph)
    flag = ((rk < 0.25) & brk).astype(float)
    flag[rk.isna() | ph.isna()] = np.nan
    base = flag.rolling(70,min_periods=35).sum()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_strongbot_30d_slope_v104_signal(close,high,low):
    hi = high.rolling(14,min_periods=14).max()
    lo = low.rolling(14,min_periods=14).min()
    pos = (close - lo) / (hi - lo).replace(0,np.nan)
    flag = (pos <= 0.2).astype(float)
    flag[pos.isna()] = np.nan
    base = flag.rolling(30,min_periods=15).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_acccnt_40d_slope_v105_signal(closeadj,high,low):
    hi = high.rolling(5,min_periods=5).max()
    lo = low.rolling(5,min_periods=5).min()
    w = hi - lo
    growth = w / w.shift(10).replace(0,np.nan)
    flag = (growth > 1.25).astype(float)
    flag[growth.isna()] = np.nan
    base = flag.rolling(40,min_periods=20).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkmag_50d_slope_v106_signal(closeadj,high):
    prior = high.shift(1).rolling(20,min_periods=20).max()
    mag = (closeadj - prior).clip(lower=0.0)
    norm = mag / closeadj.replace(0,np.nan)
    base = norm.rolling(50,min_periods=25).mean().where(~prior.isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkmaxmag_60d_slope_v107_signal(closeadj,high,low):
    ph = high.shift(1).rolling(30,min_periods=30).max()
    pl = low.shift(1).rolling(30,min_periods=30).min()
    up = (closeadj - ph).clip(lower=0.0)
    dn = (pl - closeadj).clip(lower=0.0)
    m = pd.concat([up,dn],axis=1).max(axis=1) / closeadj.replace(0,np.nan)
    base = m.rolling(60,min_periods=30).max()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brksig_40d_slope_v108_signal(closeadj,high):
    prior = high.shift(1).rolling(20,min_periods=20).max()
    flag = (closeadj > prior).astype(float)
    flag[prior.isna()] = np.nan
    cnt = flag.rolling(50,min_periods=25).mean()
    mu = cnt.rolling(40,min_periods=20).mean()
    sd = cnt.rolling(40,min_periods=20).std()
    base = (cnt - mu) / sd.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pinchrat_50d_slope_v109_signal(closeadj,high,low):
    h5 = high.rolling(5,min_periods=5).max()
    l5 = low.rolling(5,min_periods=5).min()
    h50 = high.rolling(50,min_periods=50).max()
    l50 = low.rolling(50,min_periods=50).min()
    base = (h5 - l5) / (h50 - l50).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chstack_100d_slope_v110_signal(closeadj,high,low):
    def _q(n):
        hi = high.rolling(n,min_periods=n).max()
        lo = low.rolling(n,min_periods=n).min()
        return ((closeadj - lo) / (hi - lo).replace(0,np.nan) >= 0.75).astype(float)
    base = _q(10) + _q(30) + _q(60) + _q(100)
    base = base.where(~high.rolling(100,min_periods=100).max().isna())
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chstackdn_100d_slope_v111_signal(closeadj,high,low):
    def _q(n):
        hi = high.rolling(n,min_periods=n).max()
        lo = low.rolling(n,min_periods=n).min()
        return ((closeadj - lo) / (hi - lo).replace(0,np.nan) <= 0.25).astype(float)
    base = _q(10) + _q(30) + _q(60) + _q(100)
    base = base.where(~high.rolling(100,min_periods=100).max().isna())
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_rangedom_30d_slope_v112_signal(closeadj,high,low):
    rng = high - low
    rolling_max5 = rng.rolling(5,min_periods=5).max()
    flag = (rng >= rolling_max5).astype(float)
    flag[rolling_max5.isna()] = np.nan
    base = flag.rolling(30,min_periods=15).mean()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_sigpos_30d_slope_v113_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    mu = pos.rolling(60,min_periods=30).mean()
    sd = pos.rolling(60,min_periods=30).std()
    z = (pos - mu) / sd.replace(0,np.nan)
    base = 1.0 / (1.0 + np.exp(-z.clip(-20.0,20.0)))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_arctanw_40d_slope_v114_signal(closeadj,high,low):
    hi = high.rolling(40,min_periods=40).max()
    lo = low.rolling(40,min_periods=40).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    mu = w.rolling(60,min_periods=30).mean()
    sd = w.rolling(60,min_periods=30).std()
    z = (w - mu) / sd.replace(0,np.nan)
    base = (2.0 / np.pi) * np.arctan(z)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_tanhdcn_30d_slope_v115_signal(closeadj,high):
    hi = high.rolling(30,min_periods=30).max()
    z = np.log(hi.replace(0,np.nan) / closeadj.replace(0,np.nan))
    base = np.tanh(z * 10.0)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_logrng_20d_slope_v116_signal(close,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    base = (np.log(hi.replace(0,np.nan)) - np.log(lo.replace(0,np.nan))).rank(pct=True) - 0.5
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_lrretchcd_50d_slope_v117_signal(closeadj,high,low):
    lr = np.log(closeadj.replace(0,np.nan)).diff()
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    dp = pos.diff()
    base = lr.rolling(50,min_periods=30).corr(dp)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_pxret_40d_slope_v118_signal(closeadj,high,low):
    hi = high.rolling(40,min_periods=40).max()
    lo = low.rolling(40,min_periods=40).min()
    cret = np.log(closeadj / closeadj.shift(40).replace(0,np.nan))
    wlog = np.log(hi.replace(0,np.nan)) - np.log(lo.replace(0,np.nan))
    base = cret / wlog.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chsharpe_30d_slope_v119_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    wlog = np.log(hi.replace(0,np.nan)) - np.log(lo.replace(0,np.nan))
    cret = np.log(closeadj / closeadj.shift(30).replace(0,np.nan))
    base = cret / wlog.replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_vwhipos_30d_slope_v120_signal(closeadj,high,low,volume):
    vh = (high * volume).rolling(30,min_periods=30).sum() / volume.rolling(30,min_periods=30).sum().replace(0,np.nan)
    base = (closeadj - vh) / closeadj.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_vwlopos_30d_slope_v121_signal(closeadj,low,volume):
    vl = (low * volume).rolling(30,min_periods=30).sum() / volume.rolling(30,min_periods=30).sum().replace(0,np.nan)
    below = (closeadj < vl).astype(float).where(~vl.isna())
    base = below.rolling(30,min_periods=15).mean() - 0.5
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_volrng_50d_slope_v122_signal(closeadj,high,low,volume):
    vh = (high * volume).rolling(50,min_periods=50).sum() / volume.rolling(50,min_periods=50).sum().replace(0,np.nan)
    vl = (low * volume).rolling(50,min_periods=50).sum() / volume.rolling(50,min_periods=50).sum().replace(0,np.nan)
    base = (vh - vl) / closeadj.replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_volnewhi_40d_slope_v123_signal(closeadj,high,volume):
    prior = high.shift(1).rolling(20,min_periods=20).max()
    new_hi = (high > prior).astype(float)
    new_hi[prior.isna()] = np.nan
    nh_vol = (new_hi * volume).rolling(40,min_periods=20).sum() / new_hi.rolling(40,min_periods=20).sum().replace(0,np.nan)
    all_vol = volume.rolling(40,min_periods=20).mean()
    base = np.log(nh_vol.replace(0,np.nan) / all_vol.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_volpos_30d_slope_v124_signal(closeadj,high,low,volume):
    vh = (high * volume).rolling(30,min_periods=30).sum() / volume.rolling(30,min_periods=30).sum().replace(0,np.nan)
    vmed = volume.rolling(30,min_periods=30).median()
    pierce = ((closeadj > vh) & (volume > vmed)).astype(float).where(~vh.isna())
    base = pierce.rolling(30,min_periods=15).mean() - 0.1
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_widkurt_90d_slope_v125_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    base = w.rolling(90,min_periods=45).kurt()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_widskew_70d_slope_v126_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    base = w.rolling(70,min_periods=35).skew()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkkurt_80d_slope_v127_signal(closeadj,high):
    hi = high.rolling(40,min_periods=40).max()
    mag = (hi - closeadj) / closeadj.replace(0,np.nan)
    base = mag.rolling(80,min_periods=40).kurt()
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_widrkdif_80d_slope_v128_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0,np.nan)
    rk = w.rolling(80,min_periods=40).rank(pct=True)
    base = rk - rk.shift(21)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posrkfast_30d_slope_v129_signal(closeadj,high,low):
    h5 = high.rolling(5,min_periods=5).max()
    l5 = low.rolling(5,min_periods=5).min()
    pos = (closeadj - l5) / (h5 - l5).replace(0,np.nan)
    base = pos.rolling(30,min_periods=15).rank(pct=True) - 0.5
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chconsec_60d_slope_v130_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    mid = (hi + lo) / 2.0
    above = (closeadj > mid).astype(float)
    above[mid.isna()] = np.nan
    def _mr(a):
        if np.isnan(a).any(): return float('nan')
        m=c=0
        for v in a:
            c = c+1 if v>0 else 0
            if c>m: m=c
        return float(m)
    base = above.rolling(60,min_periods=60).apply(_mr,raw=True)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_postransr_60d_slope_v131_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    was_low = (pos.shift(5) <= 0.25)
    is_high = (pos >= 0.75)
    trans = (was_low & is_high).astype(float)
    trans[pos.isna() | pos.shift(5).isna()] = np.nan
    base = trans.rolling(60,min_periods=30).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_bodyrng_30d_slope_v132_signal(close,open_,high,low):
    hi5 = high.rolling(5,min_periods=5).max()
    lo5 = low.rolling(5,min_periods=5).min()
    body = (close - open_).abs()
    base = body.rolling(30,min_periods=15).mean() / (hi5 - lo5).rolling(30,min_periods=15).mean().replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_wickrat_25d_slope_v133_signal(close,open_,high,low):
    upper_wick = high - pd.concat([close,open_],axis=1).max(axis=1)
    hi5 = high.rolling(5,min_periods=5).max()
    lo5 = low.rolling(5,min_periods=5).min()
    rng5 = (hi5 - lo5).replace(0,np.nan)
    base = (upper_wick / rng5).rolling(25,min_periods=15).mean()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_wicklo_25d_slope_v134_signal(close,open_,high,low):
    lower_wick = pd.concat([close,open_],axis=1).min(axis=1) - low
    hi5 = high.rolling(5,min_periods=5).max()
    lo5 = low.rolling(5,min_periods=5).min()
    rng5 = (hi5 - lo5).replace(0,np.nan)
    base = (lower_wick / rng5).rolling(25,min_periods=15).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chreg_60d_slope_v135_signal(closeadj,high,low):
    hi = high.rolling(60,min_periods=60).max()
    lo = low.rolling(60,min_periods=60).min()
    mid = (hi + lo) / 2.0
    t = np.arange(60,dtype=float); tm = t.mean(); dn = ((t - tm) ** 2).sum()
    def _slp(a):
        if np.any(np.isnan(a)): return float('nan')
        return float(((t - tm) * (a - a.mean())).sum() / dn)
    s = mid.rolling(60,min_periods=60).apply(_slp,raw=True)
    base = (s / mid.replace(0,np.nan)).replace([np.inf,-np.inf],np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chregfit_50d_slope_v136_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    mid = (hi + lo) / 2.0
    cov = closeadj.rolling(50,min_periods=50).cov(mid)
    vc = closeadj.rolling(50,min_periods=50).var()
    vm = mid.rolling(50,min_periods=50).var()
    base = (cov * cov) / (vc * vm).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_topbotdv_60d_slope_v137_signal(closeadj,high,low):
    hi = high.rolling(60,min_periods=60).max()
    lo = low.rolling(60,min_periods=60).min()
    dh = hi - hi.shift(30)
    dl = lo.shift(30) - lo
    base = np.arctan(dh) - np.arctan(dl)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chshape_50d_slope_v138_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    base = (hi - hi.shift(25)) / (hi.shift(25) - lo.shift(25)).replace(0,np.nan)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chsym_30d_slope_v139_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    mid = (hi + lo) / 2.0
    mu = closeadj.rolling(30,min_periods=30).mean()
    base = (closeadj - mid) / (closeadj - mu).replace(0,np.nan)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chemap_30d_slope_v140_signal(closeadj,high,low):
    hi = high.rolling(30,min_periods=30).max()
    lo = low.rolling(30,min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.ewm(span=10,adjust=False,min_periods=10).mean() - 0.5
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chminmid_20d_slope_v141_signal(close,high,low):
    h10 = high.rolling(10,min_periods=10).max()
    l10 = low.rolling(10,min_periods=10).min()
    pos = (close - l10) / (h10 - l10).replace(0,np.nan)
    base = pos.rolling(20,min_periods=20).min()
    return base.diff(5).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chmaxmid_20d_slope_v142_signal(close,high,low):
    h10 = high.rolling(10,min_periods=10).max()
    l10 = low.rolling(10,min_periods=10).min()
    pos = (close - l10) / (h10 - l10).replace(0,np.nan)
    base = pos.rolling(20,min_periods=20).max() - 0.5
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_agrstack_60d_slope_v143_signal(closeadj,high,low):
    def _b(n):
        hi = high.rolling(n,min_periods=n).max()
        lo = low.rolling(n,min_periods=n).min()
        return np.sign((closeadj - lo) / (hi - lo).replace(0,np.nan) - 0.5)
    base = _b(10) + _b(30) + _b(60)
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_brkagg_45d_slope_v144_signal(closeadj,high,low):
    ph = high.shift(1).rolling(20,min_periods=20).max()
    pl = low.shift(1).rolling(20,min_periods=20).min()
    s = pd.Series(0.0,index=closeadj.index,dtype=float)
    s[closeadj > ph] = 1.0
    s[closeadj < pl] = -1.0
    s[ph.isna() | pl.isna()] = np.nan
    base = s.rolling(45,min_periods=22).sum()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chexh_50d_slope_v145_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    extreme = ((pos >= 0.95) | (pos <= 0.05)).astype(float)
    extreme[pos.isna()] = np.nan
    base = extreme.rolling(50,min_periods=25).mean()
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_anchprior_45d_slope_v146_signal(closeadj,high):
    win = high.shift(22).rolling(23,min_periods=23).max()
    base = np.log(closeadj.replace(0,np.nan) / win.replace(0,np.nan))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_anchpriorlo_70d_slope_v147_signal(closeadj,low):
    win = low.shift(30).rolling(41,min_periods=41).min()
    base = np.log(closeadj.replace(0,np.nan) / win.replace(0,np.nan))
    return base.diff(63).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chrew_50d_slope_v148_signal(closeadj,high,low):
    hi = high.rolling(50,min_periods=50).max()
    lo = low.rolling(50,min_periods=50).min()
    above = (hi - closeadj).clip(lower=1e-9)
    below = (closeadj - lo).clip(lower=1e-9)
    base = np.log(above / below)
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_posac5_75d_slope_v149_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    base = pos.rolling(75,min_periods=50).corr(pos.shift(5))
    return base.diff(21).replace([np.inf,-np.inf],np.nan)

def f02pc_f02_price_channel_position_chrev_55d_slope_v150_signal(closeadj,high,low):
    hi = high.rolling(20,min_periods=20).max()
    lo = low.rolling(20,min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0,np.nan)
    s = np.sign(pos - 0.5)
    cross = (s != s.shift(1)).astype(float)
    cross[s.isna() | s.shift(1).isna()] = np.nan
    base = cross.rolling(55,min_periods=28).mean()
    return base.diff(10).replace([np.inf,-np.inf],np.nan)

def _e(fn,*inputs):
    return fn.__name__,{"inputs": list(inputs),"func": fn}

f02_price_channel_position_slope_001_150_REGISTRY = dict([
_e(f02pc_f02_price_channel_position_chpos_20d_slope_v001_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_chposlg_55d_slope_v002_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chmid_200d_slope_v003_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_dtop_10d_slope_v004_signal,"close","high"),
_e(f02pc_f02_price_channel_position_dbot_50d_slope_v005_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_dtoplg_200d_slope_v006_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_chwid_20d_slope_v007_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_chwidlg_63d_slope_v008_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chwidrk_120d_slope_v009_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chwidslp_50d_slope_v010_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chwidrat_50d_slope_v011_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chpinch_60d_slope_v012_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chhislp_30d_slope_v013_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_chloslp_30d_slope_v014_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_chmidslp_100d_slope_v015_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chexpdv_30d_slope_v016_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_brkup_20d_slope_v017_signal,"close","high"),
_e(f02pc_f02_price_channel_position_brkdn_55d_slope_v018_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_brkcnt_60d_slope_v019_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_brkbal_50d_slope_v020_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_streakup_20d_slope_v021_signal,"close","high"),
_e(f02pc_f02_price_channel_position_dayslast_50d_slope_v022_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_dayslo_100d_slope_v023_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_dayswide_60d_slope_v024_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_donst_30d_slope_v025_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_donqt_75d_slope_v026_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_stoK_14d_slope_v027_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_stoXdrt_14d_slope_v028_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_stoSK_42d_slope_v029_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_stochmi_25d_slope_v030_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_wpr_10d_slope_v031_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_halfbin_63d_slope_v032_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_asymabs_30d_slope_v033_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_lastside_40d_slope_v034_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_topvsbot_60d_slope_v035_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_timetop_60d_slope_v036_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_timebot_120d_slope_v037_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_anchhi_30d_slope_v038_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_anchlo_100d_slope_v039_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_decay_50d_slope_v040_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_vwapchpos_30d_slope_v041_signal,"closeadj","high","low","volume"),
_e(f02pc_f02_price_channel_position_volbrk_40d_slope_v042_signal,"closeadj","high","volume"),
_e(f02pc_f02_price_channel_position_posrk_120d_slope_v043_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_posstd_60d_slope_v044_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_posskew_90d_slope_v045_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_zscpos_50d_slope_v046_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_nearedge_30d_slope_v047_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_posagree_60d_slope_v048_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_tanhdt_25d_slope_v049_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_diffpos_50d_slope_v050_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_diffdt_100d_slope_v051_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_midcross_60d_slope_v052_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_topcnt_40d_slope_v053_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_hirk_100d_slope_v054_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_lork_60d_slope_v055_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chacc_50d_slope_v056_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_widacc_30d_slope_v057_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_ulpos_20d_slope_v058_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_uppos_30d_slope_v059_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_atrwid_20d_slope_v060_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_atrposd_30d_slope_v061_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_newhicnt_50d_slope_v062_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_newlocnt_30d_slope_v063_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_pierce_30d_slope_v064_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_pierce_100d_slope_v065_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_decayrt_70d_slope_v066_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_hivol_60d_slope_v067_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_lovol_90d_slope_v068_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_posac1_60d_slope_v069_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_hiprgr_30d_slope_v070_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_loprgr_30d_slope_v071_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_pkfill_30d_slope_v072_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_pivpos_50d_slope_v073_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_hlrk_80d_slope_v074_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_regpos_150d_slope_v075_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_hl2pos_20d_slope_v076_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_hccpos_42d_slope_v077_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_ohlcrng_30d_slope_v078_signal,"closeadj","open","high","low"),
_e(f02pc_f02_price_channel_position_obpos_10d_slope_v079_signal,"close","open","high","low"),
_e(f02pc_f02_price_channel_position_truebw_25d_slope_v080_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_kelt_20d_slope_v081_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_keltatr_50d_slope_v082_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_keltdiv_30d_slope_v083_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_bollhi_20d_slope_v084_signal,"close","high"),
_e(f02pc_f02_price_channel_position_bolllo_30d_slope_v085_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_bollratlo_60d_slope_v086_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_qchpos_30d_slope_v087_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_qchwid_60d_slope_v088_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_qchdiff_50d_slope_v089_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_iqrch_45d_slope_v090_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_medch_30d_slope_v091_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_qchhi_100d_slope_v092_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_brk52w_252d_slope_v093_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_pos252_252d_slope_v094_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_dist52h_252d_slope_v095_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_dist52l_252d_slope_v096_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_zh252_252d_slope_v097_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_swhipos_30d_slope_v098_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_swlopos_30d_slope_v099_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_swdir_30d_slope_v100_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_topcond_60d_slope_v101_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_bothcnt_50d_slope_v102_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_pinchbrk_70d_slope_v103_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_strongbot_30d_slope_v104_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_acccnt_40d_slope_v105_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_brkmag_50d_slope_v106_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_brkmaxmag_60d_slope_v107_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_brksig_40d_slope_v108_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_pinchrat_50d_slope_v109_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chstack_100d_slope_v110_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chstackdn_100d_slope_v111_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_rangedom_30d_slope_v112_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_sigpos_30d_slope_v113_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_arctanw_40d_slope_v114_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_tanhdcn_30d_slope_v115_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_logrng_20d_slope_v116_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_lrretchcd_50d_slope_v117_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_pxret_40d_slope_v118_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chsharpe_30d_slope_v119_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_vwhipos_30d_slope_v120_signal,"closeadj","high","low","volume"),
_e(f02pc_f02_price_channel_position_vwlopos_30d_slope_v121_signal,"closeadj","low","volume"),
_e(f02pc_f02_price_channel_position_volrng_50d_slope_v122_signal,"closeadj","high","low","volume"),
_e(f02pc_f02_price_channel_position_volnewhi_40d_slope_v123_signal,"closeadj","high","volume"),
_e(f02pc_f02_price_channel_position_volpos_30d_slope_v124_signal,"closeadj","high","low","volume"),
_e(f02pc_f02_price_channel_position_widkurt_90d_slope_v125_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_widskew_70d_slope_v126_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_brkkurt_80d_slope_v127_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_widrkdif_80d_slope_v128_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_posrkfast_30d_slope_v129_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chconsec_60d_slope_v130_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_postransr_60d_slope_v131_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_bodyrng_30d_slope_v132_signal,"close","open","high","low"),
_e(f02pc_f02_price_channel_position_wickrat_25d_slope_v133_signal,"close","open","high","low"),
_e(f02pc_f02_price_channel_position_wicklo_25d_slope_v134_signal,"close","open","high","low"),
_e(f02pc_f02_price_channel_position_chreg_60d_slope_v135_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chregfit_50d_slope_v136_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_topbotdv_60d_slope_v137_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chshape_50d_slope_v138_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chsym_30d_slope_v139_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chemap_30d_slope_v140_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chminmid_20d_slope_v141_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_chmaxmid_20d_slope_v142_signal,"close","high","low"),
_e(f02pc_f02_price_channel_position_agrstack_60d_slope_v143_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_brkagg_45d_slope_v144_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chexh_50d_slope_v145_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_anchprior_45d_slope_v146_signal,"closeadj","high"),
_e(f02pc_f02_price_channel_position_anchpriorlo_70d_slope_v147_signal,"closeadj","low"),
_e(f02pc_f02_price_channel_position_chrew_50d_slope_v148_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_posac5_75d_slope_v149_signal,"closeadj","high","low"),
_e(f02pc_f02_price_channel_position_chrev_55d_slope_v150_signal,"closeadj","high","low"),
])

def _synthetic_inputs(n=800,seed=42):
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012,0.011,seg),
        rng.normal(-0.0005,0.018,seg),
        rng.normal(-0.0010,0.014,seg),
        rng.normal(0.0008,0.012,rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0,0.0003,size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0,0.008,size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close,open_) * np.exp(np.abs(rng.normal(0.0,0.006,size=n)))
    low = np.minimum(close,open_) * np.exp(-np.abs(rng.normal(0.0,0.006,size=n)))
    volume = rng.lognormal(mean=13.0,sigma=0.6,size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_,index=idx,dtype=float),
        "high": pd.Series(high,index=idx,dtype=float),
        "low": pd.Series(low,index=idx,dtype=float),
        "close": pd.Series(close,index=idx,dtype=float),
        "closeadj": pd.Series(closeadj,index=idx,dtype=float),
        "volume": pd.Series(volume,index=idx,dtype=float),
    })

def _self_test():
    df = _synthetic_inputs(n=800,seed=42)
    results = {}
    for name,entry in f02_price_channel_position_slope_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out,pd.Series),f"{name}: not a Series"
        assert len(out) == len(df),f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0,f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1,f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80,f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results},axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf,-np.inf],np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values,0.0)
    max_corr = float(corr.max().max())
    assert max_corr <= 0.95 + 1e-9,f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
