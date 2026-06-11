import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w)


def _jerk(s, w):
    sl = s.diff(periods=w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====

def _f22_margin_traj_gp(gp, revenue, w):
    m = gp / revenue.replace(0, np.nan).abs()
    return m.diff(w) / m.shift(w).abs().replace(0, np.nan)


def _f22_margin_traj_op(opinc, revenue, w):
    m = opinc / revenue.replace(0, np.nan).abs()
    return m.diff(w) / m.shift(w).abs().replace(0, np.nan)


def _f22_margin_traj_net(netinc, revenue, w):
    m = netinc / revenue.replace(0, np.nan).abs()
    return m.diff(w) / m.shift(w).abs().replace(0, np.nan)

# raw of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_21d_21d_base_v001_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_21d_21d_base_v002_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_21d_21d_base_v003_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_21d_21d_base_v004_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_21d_21d_base_v005_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_21d_21d_base_v006_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_21d_21d_base_v007_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_21d_21d_base_v008_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_21d_21d_base_v009_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_21d_21d_base_v010_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 21)) * (_f22_margin_traj_gp(gp, revenue, 21)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_63d_63d_base_v011_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_63d_63d_base_v012_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 63), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_63d_63d_base_v013_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_63d_63d_base_v014_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_63d_63d_base_v015_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_63d_63d_base_v016_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_63d_63d_base_v017_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_63d_63d_base_v018_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_63d_63d_base_v019_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_63d_63d_base_v020_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 63)) * (_f22_margin_traj_gp(gp, revenue, 63)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_126d_126d_base_v021_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_126d_126d_base_v022_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_126d_126d_base_v023_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_126d_126d_base_v024_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_126d_126d_base_v025_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_126d_126d_base_v026_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_126d_126d_base_v027_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_126d_126d_base_v028_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_126d_126d_base_v029_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_126d_126d_base_v030_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 126)) * (_f22_margin_traj_gp(gp, revenue, 126)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_252d_252d_base_v031_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_252d_252d_base_v032_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_252d_252d_base_v033_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_252d_252d_base_v034_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_252d_252d_base_v035_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_252d_252d_base_v036_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_252d_252d_base_v037_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_252d_252d_base_v038_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_252d_252d_base_v039_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_252d_252d_base_v040_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 252)) * (_f22_margin_traj_gp(gp, revenue, 252)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_504d_504d_base_v041_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_504d_504d_base_v042_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 504), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_504d_504d_base_v043_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_504d_504d_base_v044_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_504d_504d_base_v045_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_504d_504d_base_v046_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 504), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_504d_504d_base_v047_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_504d_504d_base_v048_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_504d_504d_base_v049_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_504d_504d_base_v050_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 504)) * (_f22_margin_traj_gp(gp, revenue, 504)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v051_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v052_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v053_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v054_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v055_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f22mt_f22_margin_trajectory_std21_21d_21d_base_v056_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f22mt_f22_margin_trajectory_z126_63d_63d_base_v057_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f22mt_f22_margin_trajectory_z504_126d_126d_base_v058_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f22mt_f22_margin_trajectory_absmean21_252d_252d_base_v059_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f22mt_f22_margin_trajectory_absmean252_504d_504d_base_v060_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v061_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v062_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v063_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v064_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v065_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f22mt_f22_margin_trajectory_std21_21d_21d_base_v066_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f22mt_f22_margin_trajectory_z126_63d_63d_base_v067_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f22mt_f22_margin_trajectory_z504_126d_126d_base_v068_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f22mt_f22_margin_trajectory_absmean21_252d_252d_base_v069_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f22mt_f22_margin_trajectory_absmean252_504d_504d_base_v070_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v071_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v072_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v073_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v074_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v075_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f22mt_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    cols = {"gp": gp, "opinc": opinc, "netinc": netinc, "revenue": revenue, "closeadj": closeadj}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_margin_traj_gp", "_f22_margin_traj_op", "_f22_margin_traj_net",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f22_margin_trajectory_base_001_075_claude: {n_features} features pass")
