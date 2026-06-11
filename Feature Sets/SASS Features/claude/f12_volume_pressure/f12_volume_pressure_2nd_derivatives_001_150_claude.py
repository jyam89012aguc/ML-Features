import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _dollar_vol(closeadj, volume):
    return closeadj * volume


def _rel_vol(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _surge(volume, a, b):
    return _mean(volume, a) / _mean(volume, b).replace(0, np.nan)


def _net_press(closeadj, volume, w):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    return (_rsum(up, w) - _rsum(dn, w)) / _rsum(volume, w).replace(0, np.nan)


def _conc(volume, w):
    return _rsum(volume ** 2, w) / (_rsum(volume, w) ** 2).replace(0, np.nan)



# slope (plain ROC, 5d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvola_63d_slope_v001_signal(volume):
    base = _rel_vol(volume, 63)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvolc_63d_slope_v002_signal(volume):
    base = _rel_vol(volume, 63)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvola_63d_slope_v003_signal(volume):
    base = _rel_vol(volume, 63)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvolc_63d_slope_v004_signal(volume):
    base = _rel_vol(volume, 63)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvola_63d_slope_v005_signal(volume):
    base = _rel_vol(volume, 63)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of relvol/63d base
def f12vp_f12_volume_pressure_relvolc_63d_slope_v006_signal(volume):
    base = _rel_vol(volume, 63)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of relvol/21d base
def f12vp_f12_volume_pressure_relvolc_21d_slope_v007_signal(volume):
    base = _rel_vol(volume, 21)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of relvol/126d base
def f12vp_f12_volume_pressure_relvolc_126d_slope_v008_signal(volume):
    base = _rel_vol(volume, 126)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563a_63d_slope_v009_signal(volume):
    base = _surge(volume, 5, 63)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563c_63d_slope_v010_signal(volume):
    base = _surge(volume, 5, 63)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563a_63d_slope_v011_signal(volume):
    base = _surge(volume, 5, 63)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563c_63d_slope_v012_signal(volume):
    base = _surge(volume, 5, 63)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563a_63d_slope_v013_signal(volume):
    base = _surge(volume, 5, 63)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of surge563/63d base
def f12vp_f12_volume_pressure_surge563c_63d_slope_v014_signal(volume):
    base = _surge(volume, 5, 63)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of surge21126/126d base
def f12vp_f12_volume_pressure_surge21126a_126d_slope_v015_signal(volume):
    base = _surge(volume, 21, 126)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of surge21126/126d base
def f12vp_f12_volume_pressure_surge21126b_126d_slope_v016_signal(volume):
    base = _surge(volume, 21, 126)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of surge21126/126d base
def f12vp_f12_volume_pressure_surge21126c_126d_slope_v017_signal(volume):
    base = _surge(volume, 21, 126)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of surge21126/126d base
def f12vp_f12_volume_pressure_surge21126a_126d_slope_v018_signal(volume):
    base = _surge(volume, 21, 126)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of surge21126/126d base
def f12vp_f12_volume_pressure_surge21126c_126d_slope_v019_signal(volume):
    base = _surge(volume, 21, 126)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252a_252d_slope_v020_signal(volume):
    base = _surge(volume, 42, 252)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252b_252d_slope_v021_signal(volume):
    base = _surge(volume, 42, 252)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252c_252d_slope_v022_signal(volume):
    base = _surge(volume, 42, 252)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252a_252d_slope_v023_signal(volume):
    base = _surge(volume, 42, 252)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252b_252d_slope_v024_signal(volume):
    base = _surge(volume, 42, 252)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of surge42252/252d base
def f12vp_f12_volume_pressure_surge42252c_252d_slope_v025_signal(volume):
    base = _surge(volume, 42, 252)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of netpress/21d base
def f12vp_f12_volume_pressure_netpressa_21d_slope_v026_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 21)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of netpress/21d base
def f12vp_f12_volume_pressure_netpressc_21d_slope_v027_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 21)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of netpress/21d base
def f12vp_f12_volume_pressure_netpressa_21d_slope_v028_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 21)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of netpress/21d base
def f12vp_f12_volume_pressure_netpressb_21d_slope_v029_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 21)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of netpress/21d base
def f12vp_f12_volume_pressure_netpressc_21d_slope_v030_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 21)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressa_63d_slope_v031_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressb_63d_slope_v032_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressc_63d_slope_v033_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressa_63d_slope_v034_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressb_63d_slope_v035_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressc_63d_slope_v036_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressa_63d_slope_v037_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressb_63d_slope_v038_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of netpress/63d base
def f12vp_f12_volume_pressure_netpressc_63d_slope_v039_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 63)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressa_126d_slope_v040_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressb_126d_slope_v041_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressc_126d_slope_v042_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressa_126d_slope_v043_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressb_126d_slope_v044_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of netpress/126d base
def f12vp_f12_volume_pressure_netpressc_126d_slope_v045_signal(closeadj, volume):
    base = _net_press(closeadj, volume, 126)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of conc/63d base
def f12vp_f12_volume_pressure_conca_63d_slope_v046_signal(volume):
    base = _conc(volume, 63)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concb_63d_slope_v047_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concc_63d_slope_v048_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of conc/63d base
def f12vp_f12_volume_pressure_conca_63d_slope_v049_signal(volume):
    base = _conc(volume, 63)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concb_63d_slope_v050_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concc_63d_slope_v051_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of conc/63d base
def f12vp_f12_volume_pressure_conca_63d_slope_v052_signal(volume):
    base = _conc(volume, 63)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concb_63d_slope_v053_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of conc/63d base
def f12vp_f12_volume_pressure_concc_63d_slope_v054_signal(volume):
    base = _conc(volume, 63)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of conc/21d base
def f12vp_f12_volume_pressure_conca_21d_slope_v055_signal(volume):
    base = _conc(volume, 21)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of conc/21d base
def f12vp_f12_volume_pressure_concc_21d_slope_v056_signal(volume):
    base = _conc(volume, 21)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of conc/21d base
def f12vp_f12_volume_pressure_conca_21d_slope_v057_signal(volume):
    base = _conc(volume, 21)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of conc/21d base
def f12vp_f12_volume_pressure_concb_21d_slope_v058_signal(volume):
    base = _conc(volume, 21)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of conc/21d base
def f12vp_f12_volume_pressure_concc_21d_slope_v059_signal(volume):
    base = _conc(volume, 21)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdaya_63d_slope_v060_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdayb_63d_slope_v061_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdayc_63d_slope_v062_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdaya_63d_slope_v063_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdayb_63d_slope_v064_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdayc_63d_slope_v065_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdaya_63d_slope_v066_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of topday/63d base
def f12vp_f12_volume_pressure_topdayc_63d_slope_v067_signal(volume):
    base = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolzb_63d_slope_v068_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolzc_63d_slope_v069_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolza_63d_slope_v070_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolzc_63d_slope_v071_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolza_63d_slope_v072_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of dvolz/63d base
def f12vp_f12_volume_pressure_dvolzc_63d_slope_v073_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _z(np.log(dv.replace(0, np.nan)), 63)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgea_126d_slope_v074_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgeb_126d_slope_v075_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgec_126d_slope_v076_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgea_126d_slope_v077_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgeb_126d_slope_v078_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of dvolsurge/126d base
def f12vp_f12_volume_pressure_dvolsurgec_126d_slope_v079_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volrank/252d base
def f12vp_f12_volume_pressure_volrankc_252d_slope_v080_signal(volume):
    base = volume.rolling(252, min_periods=126).rank(pct=True) - 0.5
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of volrank/252d base
def f12vp_f12_volume_pressure_volrankc_252d_slope_v081_signal(volume):
    base = volume.rolling(252, min_periods=126).rank(pct=True) - 0.5
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volband/63d base
def f12vp_f12_volume_pressure_volbandc_63d_slope_v082_signal(volume):
    hi = _rmax(volume, 63)
    lo = _rmin(volume, 63)
    base = (volume - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of volband/63d base
def f12vp_f12_volume_pressure_volbanda_63d_slope_v083_signal(volume):
    hi = _rmax(volume, 63)
    lo = _rmin(volume, 63)
    base = (volume - lo) / (hi - lo).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of volband/63d base
def f12vp_f12_volume_pressure_volbandc_63d_slope_v084_signal(volume):
    hi = _rmax(volume, 63)
    lo = _rmin(volume, 63)
    base = (volume - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimea_126d_slope_v085_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimeb_126d_slope_v086_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimec_126d_slope_v087_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimea_126d_slope_v088_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimeb_126d_slope_v089_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of volregime/126d base
def f12vp_f12_volume_pressure_volregimec_126d_slope_v090_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    base = (av - lo) / (hi - lo).replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of intensity/21d base
def f12vp_f12_volume_pressure_intensitya_21d_slope_v091_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = ret.abs() * volume
    base = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of intensity/21d base
def f12vp_f12_volume_pressure_intensityc_21d_slope_v092_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = ret.abs() * volume
    base = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of intensity/21d base
def f12vp_f12_volume_pressure_intensitya_21d_slope_v093_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = ret.abs() * volume
    base = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of intensity/21d base
def f12vp_f12_volume_pressure_intensityb_21d_slope_v094_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = ret.abs() * volume
    base = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of intensity/21d base
def f12vp_f12_volume_pressure_intensityc_21d_slope_v095_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = ret.abs() * volume
    base = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of ewmratio/63d base
def f12vp_f12_volume_pressure_ewmratiob_63d_slope_v096_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    slow = volume.ewm(span=63, min_periods=21).mean()
    base = fast / slow.replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of ewmratio/63d base
def f12vp_f12_volume_pressure_ewmratioc_63d_slope_v097_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    slow = volume.ewm(span=63, min_periods=21).mean()
    base = fast / slow.replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of ewmratio/63d base
def f12vp_f12_volume_pressure_ewmratiob_63d_slope_v098_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    slow = volume.ewm(span=63, min_periods=21).mean()
    base = fast / slow.replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of ewmratio/63d base
def f12vp_f12_volume_pressure_ewmratioa_63d_slope_v099_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    slow = volume.ewm(span=63, min_periods=21).mean()
    base = fast / slow.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyb_63d_slope_v100_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyc_63d_slope_v101_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropya_63d_slope_v102_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyb_63d_slope_v103_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyc_63d_slope_v104_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropya_63d_slope_v105_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyb_63d_slope_v106_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of volentropy/63d base
def f12vp_f12_volume_pressure_volentropyc_63d_slope_v107_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    base = contrib.rolling(63, min_periods=42).sum() / np.log(63.0)
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowa_126d_slope_v108_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowb_126d_slope_v109_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowc_126d_slope_v110_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowa_126d_slope_v111_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowb_126d_slope_v112_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of dvolgrow/126d base
def f12vp_f12_volume_pressure_dvolgrowc_126d_slope_v113_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    base = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of volweightret/21d base
def f12vp_f12_volume_pressure_volweightreta_21d_slope_v114_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of volweightret/21d base
def f12vp_f12_volume_pressure_volweightretc_21d_slope_v115_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of volweightret/21d base
def f12vp_f12_volume_pressure_volweightreta_21d_slope_v116_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of volweightret/21d base
def f12vp_f12_volume_pressure_volweightretb_21d_slope_v117_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volweightret/21d base
def f12vp_f12_volume_pressure_volweightretc_21d_slope_v118_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2meda_63d_slope_v119_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2medb_63d_slope_v120_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2medc_63d_slope_v121_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2meda_63d_slope_v122_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2medb_63d_slope_v123_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of spike2med/63d base
def f12vp_f12_volume_pressure_spike2medb_63d_slope_v124_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    base = hi / med.replace(0, np.nan)
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_volefforta_21d_slope_v125_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_voleffortb_21d_slope_v126_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_voleffortc_21d_slope_v127_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_volefforta_21d_slope_v128_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_voleffortb_21d_slope_v129_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of voleffort/21d base
def f12vp_f12_volume_pressure_voleffortc_21d_slope_v130_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / ret.replace(0, np.nan)
    base = np.log(eff.rolling(21, min_periods=10).median())
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixa_63d_slope_v131_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixc_63d_slope_v132_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixa_63d_slope_v133_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixb_63d_slope_v134_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixc_63d_slope_v135_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixa_63d_slope_v136_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixb_63d_slope_v137_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of dvmix/63d base
def f12vp_f12_volume_pressure_dvmixc_63d_slope_v138_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 63).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 63).replace(0, np.nan))
    base = rdv - rv
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1a_63d_slope_v139_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1b_63d_slope_v140_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1c_63d_slope_v141_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 21d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1a_63d_slope_v142_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    d = (base - base.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 21d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1b_63d_slope_v143_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(21)) / 21.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 21d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1c_63d_slope_v144_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(21)) / 21.0
    d = sl.ewm(span=21, min_periods=10).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 63d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1a_63d_slope_v145_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    d = (base - base.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 63d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1b_63d_slope_v146_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(63)) / 63.0
    d = _z(sl, 189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 63d ROC) of volacf1/63d base
def f12vp_f12_volume_pressure_volacf1c_63d_slope_v147_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    sl = (base - base.shift(63)) / 63.0
    d = sl.ewm(span=63, min_periods=31).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (plain ROC, 5d ROC) of pvcorr/63d base
def f12vp_f12_volume_pressure_pvcorra_63d_slope_v148_signal(closeadj, volume):
    dlv = np.log(volume.replace(0, np.nan)).diff()
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(dlv)
    d = (base - base.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (z-scored slope, 5d ROC) of pvcorr/63d base
def f12vp_f12_volume_pressure_pvcorrb_63d_slope_v149_signal(closeadj, volume):
    dlv = np.log(volume.replace(0, np.nan)).diff()
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(dlv)
    sl = (base - base.shift(5)) / 5.0
    d = _z(sl, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (EWMA-smoothed slope, 5d ROC) of pvcorr/63d base
def f12vp_f12_volume_pressure_pvcorrc_63d_slope_v150_signal(closeadj, volume):
    dlv = np.log(volume.replace(0, np.nan)).diff()
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(dlv)
    sl = (base - base.shift(5)) / 5.0
    d = sl.ewm(span=5, min_periods=3).mean()
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12vp_f12_volume_pressure_relvola_63d_slope_v001_signal,
    f12vp_f12_volume_pressure_relvolc_63d_slope_v002_signal,
    f12vp_f12_volume_pressure_relvola_63d_slope_v003_signal,
    f12vp_f12_volume_pressure_relvolc_63d_slope_v004_signal,
    f12vp_f12_volume_pressure_relvola_63d_slope_v005_signal,
    f12vp_f12_volume_pressure_relvolc_63d_slope_v006_signal,
    f12vp_f12_volume_pressure_relvolc_21d_slope_v007_signal,
    f12vp_f12_volume_pressure_relvolc_126d_slope_v008_signal,
    f12vp_f12_volume_pressure_surge563a_63d_slope_v009_signal,
    f12vp_f12_volume_pressure_surge563c_63d_slope_v010_signal,
    f12vp_f12_volume_pressure_surge563a_63d_slope_v011_signal,
    f12vp_f12_volume_pressure_surge563c_63d_slope_v012_signal,
    f12vp_f12_volume_pressure_surge563a_63d_slope_v013_signal,
    f12vp_f12_volume_pressure_surge563c_63d_slope_v014_signal,
    f12vp_f12_volume_pressure_surge21126a_126d_slope_v015_signal,
    f12vp_f12_volume_pressure_surge21126b_126d_slope_v016_signal,
    f12vp_f12_volume_pressure_surge21126c_126d_slope_v017_signal,
    f12vp_f12_volume_pressure_surge21126a_126d_slope_v018_signal,
    f12vp_f12_volume_pressure_surge21126c_126d_slope_v019_signal,
    f12vp_f12_volume_pressure_surge42252a_252d_slope_v020_signal,
    f12vp_f12_volume_pressure_surge42252b_252d_slope_v021_signal,
    f12vp_f12_volume_pressure_surge42252c_252d_slope_v022_signal,
    f12vp_f12_volume_pressure_surge42252a_252d_slope_v023_signal,
    f12vp_f12_volume_pressure_surge42252b_252d_slope_v024_signal,
    f12vp_f12_volume_pressure_surge42252c_252d_slope_v025_signal,
    f12vp_f12_volume_pressure_netpressa_21d_slope_v026_signal,
    f12vp_f12_volume_pressure_netpressc_21d_slope_v027_signal,
    f12vp_f12_volume_pressure_netpressa_21d_slope_v028_signal,
    f12vp_f12_volume_pressure_netpressb_21d_slope_v029_signal,
    f12vp_f12_volume_pressure_netpressc_21d_slope_v030_signal,
    f12vp_f12_volume_pressure_netpressa_63d_slope_v031_signal,
    f12vp_f12_volume_pressure_netpressb_63d_slope_v032_signal,
    f12vp_f12_volume_pressure_netpressc_63d_slope_v033_signal,
    f12vp_f12_volume_pressure_netpressa_63d_slope_v034_signal,
    f12vp_f12_volume_pressure_netpressb_63d_slope_v035_signal,
    f12vp_f12_volume_pressure_netpressc_63d_slope_v036_signal,
    f12vp_f12_volume_pressure_netpressa_63d_slope_v037_signal,
    f12vp_f12_volume_pressure_netpressb_63d_slope_v038_signal,
    f12vp_f12_volume_pressure_netpressc_63d_slope_v039_signal,
    f12vp_f12_volume_pressure_netpressa_126d_slope_v040_signal,
    f12vp_f12_volume_pressure_netpressb_126d_slope_v041_signal,
    f12vp_f12_volume_pressure_netpressc_126d_slope_v042_signal,
    f12vp_f12_volume_pressure_netpressa_126d_slope_v043_signal,
    f12vp_f12_volume_pressure_netpressb_126d_slope_v044_signal,
    f12vp_f12_volume_pressure_netpressc_126d_slope_v045_signal,
    f12vp_f12_volume_pressure_conca_63d_slope_v046_signal,
    f12vp_f12_volume_pressure_concb_63d_slope_v047_signal,
    f12vp_f12_volume_pressure_concc_63d_slope_v048_signal,
    f12vp_f12_volume_pressure_conca_63d_slope_v049_signal,
    f12vp_f12_volume_pressure_concb_63d_slope_v050_signal,
    f12vp_f12_volume_pressure_concc_63d_slope_v051_signal,
    f12vp_f12_volume_pressure_conca_63d_slope_v052_signal,
    f12vp_f12_volume_pressure_concb_63d_slope_v053_signal,
    f12vp_f12_volume_pressure_concc_63d_slope_v054_signal,
    f12vp_f12_volume_pressure_conca_21d_slope_v055_signal,
    f12vp_f12_volume_pressure_concc_21d_slope_v056_signal,
    f12vp_f12_volume_pressure_conca_21d_slope_v057_signal,
    f12vp_f12_volume_pressure_concb_21d_slope_v058_signal,
    f12vp_f12_volume_pressure_concc_21d_slope_v059_signal,
    f12vp_f12_volume_pressure_topdaya_63d_slope_v060_signal,
    f12vp_f12_volume_pressure_topdayb_63d_slope_v061_signal,
    f12vp_f12_volume_pressure_topdayc_63d_slope_v062_signal,
    f12vp_f12_volume_pressure_topdaya_63d_slope_v063_signal,
    f12vp_f12_volume_pressure_topdayb_63d_slope_v064_signal,
    f12vp_f12_volume_pressure_topdayc_63d_slope_v065_signal,
    f12vp_f12_volume_pressure_topdaya_63d_slope_v066_signal,
    f12vp_f12_volume_pressure_topdayc_63d_slope_v067_signal,
    f12vp_f12_volume_pressure_dvolzb_63d_slope_v068_signal,
    f12vp_f12_volume_pressure_dvolzc_63d_slope_v069_signal,
    f12vp_f12_volume_pressure_dvolza_63d_slope_v070_signal,
    f12vp_f12_volume_pressure_dvolzc_63d_slope_v071_signal,
    f12vp_f12_volume_pressure_dvolza_63d_slope_v072_signal,
    f12vp_f12_volume_pressure_dvolzc_63d_slope_v073_signal,
    f12vp_f12_volume_pressure_dvolsurgea_126d_slope_v074_signal,
    f12vp_f12_volume_pressure_dvolsurgeb_126d_slope_v075_signal,
    f12vp_f12_volume_pressure_dvolsurgec_126d_slope_v076_signal,
    f12vp_f12_volume_pressure_dvolsurgea_126d_slope_v077_signal,
    f12vp_f12_volume_pressure_dvolsurgeb_126d_slope_v078_signal,
    f12vp_f12_volume_pressure_dvolsurgec_126d_slope_v079_signal,
    f12vp_f12_volume_pressure_volrankc_252d_slope_v080_signal,
    f12vp_f12_volume_pressure_volrankc_252d_slope_v081_signal,
    f12vp_f12_volume_pressure_volbandc_63d_slope_v082_signal,
    f12vp_f12_volume_pressure_volbanda_63d_slope_v083_signal,
    f12vp_f12_volume_pressure_volbandc_63d_slope_v084_signal,
    f12vp_f12_volume_pressure_volregimea_126d_slope_v085_signal,
    f12vp_f12_volume_pressure_volregimeb_126d_slope_v086_signal,
    f12vp_f12_volume_pressure_volregimec_126d_slope_v087_signal,
    f12vp_f12_volume_pressure_volregimea_126d_slope_v088_signal,
    f12vp_f12_volume_pressure_volregimeb_126d_slope_v089_signal,
    f12vp_f12_volume_pressure_volregimec_126d_slope_v090_signal,
    f12vp_f12_volume_pressure_intensitya_21d_slope_v091_signal,
    f12vp_f12_volume_pressure_intensityc_21d_slope_v092_signal,
    f12vp_f12_volume_pressure_intensitya_21d_slope_v093_signal,
    f12vp_f12_volume_pressure_intensityb_21d_slope_v094_signal,
    f12vp_f12_volume_pressure_intensityc_21d_slope_v095_signal,
    f12vp_f12_volume_pressure_ewmratiob_63d_slope_v096_signal,
    f12vp_f12_volume_pressure_ewmratioc_63d_slope_v097_signal,
    f12vp_f12_volume_pressure_ewmratiob_63d_slope_v098_signal,
    f12vp_f12_volume_pressure_ewmratioa_63d_slope_v099_signal,
    f12vp_f12_volume_pressure_volentropyb_63d_slope_v100_signal,
    f12vp_f12_volume_pressure_volentropyc_63d_slope_v101_signal,
    f12vp_f12_volume_pressure_volentropya_63d_slope_v102_signal,
    f12vp_f12_volume_pressure_volentropyb_63d_slope_v103_signal,
    f12vp_f12_volume_pressure_volentropyc_63d_slope_v104_signal,
    f12vp_f12_volume_pressure_volentropya_63d_slope_v105_signal,
    f12vp_f12_volume_pressure_volentropyb_63d_slope_v106_signal,
    f12vp_f12_volume_pressure_volentropyc_63d_slope_v107_signal,
    f12vp_f12_volume_pressure_dvolgrowa_126d_slope_v108_signal,
    f12vp_f12_volume_pressure_dvolgrowb_126d_slope_v109_signal,
    f12vp_f12_volume_pressure_dvolgrowc_126d_slope_v110_signal,
    f12vp_f12_volume_pressure_dvolgrowa_126d_slope_v111_signal,
    f12vp_f12_volume_pressure_dvolgrowb_126d_slope_v112_signal,
    f12vp_f12_volume_pressure_dvolgrowc_126d_slope_v113_signal,
    f12vp_f12_volume_pressure_volweightreta_21d_slope_v114_signal,
    f12vp_f12_volume_pressure_volweightretc_21d_slope_v115_signal,
    f12vp_f12_volume_pressure_volweightreta_21d_slope_v116_signal,
    f12vp_f12_volume_pressure_volweightretb_21d_slope_v117_signal,
    f12vp_f12_volume_pressure_volweightretc_21d_slope_v118_signal,
    f12vp_f12_volume_pressure_spike2meda_63d_slope_v119_signal,
    f12vp_f12_volume_pressure_spike2medb_63d_slope_v120_signal,
    f12vp_f12_volume_pressure_spike2medc_63d_slope_v121_signal,
    f12vp_f12_volume_pressure_spike2meda_63d_slope_v122_signal,
    f12vp_f12_volume_pressure_spike2medb_63d_slope_v123_signal,
    f12vp_f12_volume_pressure_spike2medb_63d_slope_v124_signal,
    f12vp_f12_volume_pressure_volefforta_21d_slope_v125_signal,
    f12vp_f12_volume_pressure_voleffortb_21d_slope_v126_signal,
    f12vp_f12_volume_pressure_voleffortc_21d_slope_v127_signal,
    f12vp_f12_volume_pressure_volefforta_21d_slope_v128_signal,
    f12vp_f12_volume_pressure_voleffortb_21d_slope_v129_signal,
    f12vp_f12_volume_pressure_voleffortc_21d_slope_v130_signal,
    f12vp_f12_volume_pressure_dvmixa_63d_slope_v131_signal,
    f12vp_f12_volume_pressure_dvmixc_63d_slope_v132_signal,
    f12vp_f12_volume_pressure_dvmixa_63d_slope_v133_signal,
    f12vp_f12_volume_pressure_dvmixb_63d_slope_v134_signal,
    f12vp_f12_volume_pressure_dvmixc_63d_slope_v135_signal,
    f12vp_f12_volume_pressure_dvmixa_63d_slope_v136_signal,
    f12vp_f12_volume_pressure_dvmixb_63d_slope_v137_signal,
    f12vp_f12_volume_pressure_dvmixc_63d_slope_v138_signal,
    f12vp_f12_volume_pressure_volacf1a_63d_slope_v139_signal,
    f12vp_f12_volume_pressure_volacf1b_63d_slope_v140_signal,
    f12vp_f12_volume_pressure_volacf1c_63d_slope_v141_signal,
    f12vp_f12_volume_pressure_volacf1a_63d_slope_v142_signal,
    f12vp_f12_volume_pressure_volacf1b_63d_slope_v143_signal,
    f12vp_f12_volume_pressure_volacf1c_63d_slope_v144_signal,
    f12vp_f12_volume_pressure_volacf1a_63d_slope_v145_signal,
    f12vp_f12_volume_pressure_volacf1b_63d_slope_v146_signal,
    f12vp_f12_volume_pressure_volacf1c_63d_slope_v147_signal,
    f12vp_f12_volume_pressure_pvcorra_63d_slope_v148_signal,
    f12vp_f12_volume_pressure_pvcorrb_63d_slope_v149_signal,
    f12vp_f12_volume_pressure_pvcorrc_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_VOLUME_PRESSURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f12_volume_pressure_2nd_derivatives_001_150_claude: %d features pass" % n_features)
