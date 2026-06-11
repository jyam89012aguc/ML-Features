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
def f22mt_f22_margin_trajectory_raw_21d_21d_base_v076_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_21d_21d_base_v077_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_21d_21d_base_v078_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_21d_21d_base_v079_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_21d_21d_base_v080_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_21d_21d_base_v081_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_21d_21d_base_v082_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_21d_21d_base_v083_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_21d_21d_base_v084_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 21d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_21d_21d_base_v085_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 21)) * (_f22_margin_traj_gp(gp, revenue, 21)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_63d_63d_base_v086_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_63d_63d_base_v087_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 63), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_63d_63d_base_v088_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_63d_63d_base_v089_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_63d_63d_base_v090_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_63d_63d_base_v091_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_63d_63d_base_v092_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_63d_63d_base_v093_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_63d_63d_base_v094_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 63d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_63d_63d_base_v095_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 63)) * (_f22_margin_traj_gp(gp, revenue, 63)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_126d_126d_base_v096_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_126d_126d_base_v097_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_126d_126d_base_v098_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_126d_126d_base_v099_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_126d_126d_base_v100_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_126d_126d_base_v101_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_126d_126d_base_v102_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_126d_126d_base_v103_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_126d_126d_base_v104_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 126)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 126d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_126d_126d_base_v105_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 126)) * (_f22_margin_traj_gp(gp, revenue, 126)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_252d_252d_base_v106_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_252d_252d_base_v107_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_252d_252d_base_v108_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_252d_252d_base_v109_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_252d_252d_base_v110_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_252d_252d_base_v111_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_252d_252d_base_v112_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_252d_252d_base_v113_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_252d_252d_base_v114_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 252d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_252d_252d_base_v115_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 252)) * (_f22_margin_traj_gp(gp, revenue, 252)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_raw_504d_504d_base_v116_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean21_504d_504d_base_v117_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 504), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_mean63_504d_504d_base_v118_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_std63_504d_504d_base_v119_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z63_504d_504d_base_v120_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_z252_504d_504d_base_v121_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 504), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema21_504d_504d_base_v122_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_ema63_504d_504d_base_v123_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_absmean63_504d_504d_base_v124_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 504d primitive for f22_margin_trajectory
def f22mt_f22_margin_trajectory_sqrmean63_504d_504d_base_v125_signal(gp, opinc, netinc, revenue, closeadj):
    base = ((_f22_margin_traj_gp(gp, revenue, 504)) * (_f22_margin_traj_gp(gp, revenue, 504)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v126_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v127_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v128_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v129_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v130_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f22mt_f22_margin_trajectory_std21_21d_21d_base_v131_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f22mt_f22_margin_trajectory_z126_63d_63d_base_v132_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f22mt_f22_margin_trajectory_z504_126d_126d_base_v133_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f22mt_f22_margin_trajectory_absmean21_252d_252d_base_v134_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f22mt_f22_margin_trajectory_absmean252_504d_504d_base_v135_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v136_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v137_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v138_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v139_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v140_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f22mt_f22_margin_trajectory_std21_21d_21d_base_v141_signal(gp, opinc, netinc, revenue, closeadj):
    base = _std(_f22_margin_traj_gp(gp, revenue, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f22mt_f22_margin_trajectory_z126_63d_63d_base_v142_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f22mt_f22_margin_trajectory_z504_126d_126d_base_v143_signal(gp, opinc, netinc, revenue, closeadj):
    base = _z(_f22_margin_traj_gp(gp, revenue, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f22mt_f22_margin_trajectory_absmean21_252d_252d_base_v144_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f22mt_f22_margin_trajectory_absmean252_504d_504d_base_v145_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f22mt_f22_margin_trajectory_ema126_21d_21d_base_v146_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f22mt_f22_margin_trajectory_ema252_63d_63d_base_v147_signal(gp, opinc, netinc, revenue, closeadj):
    base = (_f22_margin_traj_gp(gp, revenue, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f22mt_f22_margin_trajectory_mean126_126d_126d_base_v148_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f22mt_f22_margin_trajectory_mean252_252d_252d_base_v149_signal(gp, opinc, netinc, revenue, closeadj):
    base = _mean(_f22_margin_traj_gp(gp, revenue, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f22mt_f22_margin_trajectory_std126_504d_504d_base_v150_signal(gp, opinc, netinc, revenue, closeadj):
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
    print(f"OK f22_margin_trajectory_base_076_150_claude: {n_features} features pass")
