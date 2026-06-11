import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _f03_depth(c, w): return (c / c.rolling(w, min_periods=1).max().replace(0, np.nan) - 1)
def _f03_dur(c, w): return (w - 1 - c.rolling(w, min_periods=1).apply(np.argmax, raw=True))

def f03_crash_depth_duration_depth_open_63d_base_v091_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_63d_base_v092_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_63d_base_v093_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 63) * _f03_dur(arg_open, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_63d_base_v094_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_63d_base_v095_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 63) / 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_63d_base_v096_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 63) / (_f03_dur(arg_open, 63) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_63d_base_v097_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_63d_base_v098_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_63d_base_v099_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 63) * _f03_dur(arg_high, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_63d_base_v100_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_63d_base_v101_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 63) / 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_63d_base_v102_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 63) / (_f03_dur(arg_high, 63) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_63d_base_v103_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_63d_base_v104_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_63d_base_v105_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 63) * _f03_dur(arg_low, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_63d_base_v106_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_63d_base_v107_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 63) / 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_63d_base_v108_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 63) / (_f03_dur(arg_low, 63) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_63d_base_v109_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_63d_base_v110_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_63d_base_v111_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 63) * _f03_dur(arg_close, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_63d_base_v112_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_63d_base_v113_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 63) / 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_63d_base_v114_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 63) / (_f03_dur(arg_close, 63) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_63d_base_v115_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_63d_base_v116_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_63d_base_v117_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 63) * _f03_dur(arg_closeadj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_63d_base_v118_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_63d_base_v119_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 63) / 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_63d_base_v120_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 63) / (_f03_dur(arg_closeadj, 63) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_126d_base_v121_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_126d_base_v122_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_126d_base_v123_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 126) * _f03_dur(arg_open, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_126d_base_v124_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_126d_base_v125_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 126) / 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_126d_base_v126_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 126) / (_f03_dur(arg_open, 126) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_126d_base_v127_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_126d_base_v128_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_126d_base_v129_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 126) * _f03_dur(arg_high, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_126d_base_v130_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_126d_base_v131_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 126) / 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_126d_base_v132_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 126) / (_f03_dur(arg_high, 126) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_126d_base_v133_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_126d_base_v134_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_126d_base_v135_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 126) * _f03_dur(arg_low, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_126d_base_v136_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_126d_base_v137_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 126) / 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_126d_base_v138_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 126) / (_f03_dur(arg_low, 126) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_126d_base_v139_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_126d_base_v140_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_126d_base_v141_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 126) * _f03_dur(arg_close, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_126d_base_v142_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_126d_base_v143_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 126) / 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_126d_base_v144_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 126) / (_f03_dur(arg_close, 126) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_126d_base_v145_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_126d_base_v146_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_126d_base_v147_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 126) * _f03_dur(arg_closeadj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_126d_base_v148_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_126d_base_v149_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 126) / 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_126d_base_v150_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 126) / (_f03_dur(arg_closeadj, 126) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_252d_base_v151_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_252d_base_v152_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_252d_base_v153_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 252) * _f03_dur(arg_open, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_252d_base_v154_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_252d_base_v155_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 252) / 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_252d_base_v156_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 252) / (_f03_dur(arg_open, 252) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_252d_base_v157_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_252d_base_v158_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_252d_base_v159_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 252) * _f03_dur(arg_high, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_252d_base_v160_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_252d_base_v161_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 252) / 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_252d_base_v162_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 252) / (_f03_dur(arg_high, 252) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_252d_base_v163_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_252d_base_v164_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_252d_base_v165_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 252) * _f03_dur(arg_low, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_252d_base_v166_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_252d_base_v167_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 252) / 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_252d_base_v168_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 252) / (_f03_dur(arg_low, 252) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_252d_base_v169_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_252d_base_v170_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_252d_base_v171_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 252) * _f03_dur(arg_close, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_252d_base_v172_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_252d_base_v173_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 252) / 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_252d_base_v174_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 252) / (_f03_dur(arg_close, 252) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_252d_base_v175_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_252d_base_v176_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_252d_base_v177_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 252) * _f03_dur(arg_closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_252d_base_v178_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_252d_base_v179_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 252) / 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_252d_base_v180_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 252) / (_f03_dur(arg_closeadj, 252) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f03_crash_depth_duration_depth_open_63d_base_v091_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_63d_base_v091_signal},
    "f03_crash_depth_duration_dur_open_63d_base_v092_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_63d_base_v092_signal},
    "f03_crash_depth_duration_severity_open_63d_base_v093_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_63d_base_v093_signal},
    "f03_crash_depth_duration_depth_zscore_open_63d_base_v094_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_63d_base_v094_signal},
    "f03_crash_depth_duration_dur_norm_open_63d_base_v095_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_63d_base_v095_signal},
    "f03_crash_depth_duration_depth_norm_open_63d_base_v096_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_63d_base_v096_signal},
    "f03_crash_depth_duration_depth_high_63d_base_v097_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_63d_base_v097_signal},
    "f03_crash_depth_duration_dur_high_63d_base_v098_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_63d_base_v098_signal},
    "f03_crash_depth_duration_severity_high_63d_base_v099_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_63d_base_v099_signal},
    "f03_crash_depth_duration_depth_zscore_high_63d_base_v100_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_63d_base_v100_signal},
    "f03_crash_depth_duration_dur_norm_high_63d_base_v101_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_63d_base_v101_signal},
    "f03_crash_depth_duration_depth_norm_high_63d_base_v102_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_63d_base_v102_signal},
    "f03_crash_depth_duration_depth_low_63d_base_v103_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_63d_base_v103_signal},
    "f03_crash_depth_duration_dur_low_63d_base_v104_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_63d_base_v104_signal},
    "f03_crash_depth_duration_severity_low_63d_base_v105_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_63d_base_v105_signal},
    "f03_crash_depth_duration_depth_zscore_low_63d_base_v106_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_63d_base_v106_signal},
    "f03_crash_depth_duration_dur_norm_low_63d_base_v107_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_63d_base_v107_signal},
    "f03_crash_depth_duration_depth_norm_low_63d_base_v108_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_63d_base_v108_signal},
    "f03_crash_depth_duration_depth_close_63d_base_v109_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_63d_base_v109_signal},
    "f03_crash_depth_duration_dur_close_63d_base_v110_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_63d_base_v110_signal},
    "f03_crash_depth_duration_severity_close_63d_base_v111_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_63d_base_v111_signal},
    "f03_crash_depth_duration_depth_zscore_close_63d_base_v112_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_63d_base_v112_signal},
    "f03_crash_depth_duration_dur_norm_close_63d_base_v113_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_63d_base_v113_signal},
    "f03_crash_depth_duration_depth_norm_close_63d_base_v114_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_63d_base_v114_signal},
    "f03_crash_depth_duration_depth_closeadj_63d_base_v115_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_63d_base_v115_signal},
    "f03_crash_depth_duration_dur_closeadj_63d_base_v116_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_63d_base_v116_signal},
    "f03_crash_depth_duration_severity_closeadj_63d_base_v117_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_63d_base_v117_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_63d_base_v118_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_63d_base_v118_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_63d_base_v119_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_63d_base_v119_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_63d_base_v120_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_63d_base_v120_signal},
    "f03_crash_depth_duration_depth_open_126d_base_v121_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_126d_base_v121_signal},
    "f03_crash_depth_duration_dur_open_126d_base_v122_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_126d_base_v122_signal},
    "f03_crash_depth_duration_severity_open_126d_base_v123_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_126d_base_v123_signal},
    "f03_crash_depth_duration_depth_zscore_open_126d_base_v124_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_126d_base_v124_signal},
    "f03_crash_depth_duration_dur_norm_open_126d_base_v125_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_126d_base_v125_signal},
    "f03_crash_depth_duration_depth_norm_open_126d_base_v126_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_126d_base_v126_signal},
    "f03_crash_depth_duration_depth_high_126d_base_v127_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_126d_base_v127_signal},
    "f03_crash_depth_duration_dur_high_126d_base_v128_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_126d_base_v128_signal},
    "f03_crash_depth_duration_severity_high_126d_base_v129_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_126d_base_v129_signal},
    "f03_crash_depth_duration_depth_zscore_high_126d_base_v130_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_126d_base_v130_signal},
    "f03_crash_depth_duration_dur_norm_high_126d_base_v131_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_126d_base_v131_signal},
    "f03_crash_depth_duration_depth_norm_high_126d_base_v132_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_126d_base_v132_signal},
    "f03_crash_depth_duration_depth_low_126d_base_v133_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_126d_base_v133_signal},
    "f03_crash_depth_duration_dur_low_126d_base_v134_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_126d_base_v134_signal},
    "f03_crash_depth_duration_severity_low_126d_base_v135_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_126d_base_v135_signal},
    "f03_crash_depth_duration_depth_zscore_low_126d_base_v136_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_126d_base_v136_signal},
    "f03_crash_depth_duration_dur_norm_low_126d_base_v137_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_126d_base_v137_signal},
    "f03_crash_depth_duration_depth_norm_low_126d_base_v138_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_126d_base_v138_signal},
    "f03_crash_depth_duration_depth_close_126d_base_v139_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_126d_base_v139_signal},
    "f03_crash_depth_duration_dur_close_126d_base_v140_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_126d_base_v140_signal},
    "f03_crash_depth_duration_severity_close_126d_base_v141_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_126d_base_v141_signal},
    "f03_crash_depth_duration_depth_zscore_close_126d_base_v142_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_126d_base_v142_signal},
    "f03_crash_depth_duration_dur_norm_close_126d_base_v143_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_126d_base_v143_signal},
    "f03_crash_depth_duration_depth_norm_close_126d_base_v144_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_126d_base_v144_signal},
    "f03_crash_depth_duration_depth_closeadj_126d_base_v145_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_126d_base_v145_signal},
    "f03_crash_depth_duration_dur_closeadj_126d_base_v146_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_126d_base_v146_signal},
    "f03_crash_depth_duration_severity_closeadj_126d_base_v147_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_126d_base_v147_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_126d_base_v148_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_126d_base_v148_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_126d_base_v149_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_126d_base_v149_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_126d_base_v150_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_126d_base_v150_signal},
    "f03_crash_depth_duration_depth_open_252d_base_v151_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_252d_base_v151_signal},
    "f03_crash_depth_duration_dur_open_252d_base_v152_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_252d_base_v152_signal},
    "f03_crash_depth_duration_severity_open_252d_base_v153_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_252d_base_v153_signal},
    "f03_crash_depth_duration_depth_zscore_open_252d_base_v154_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_252d_base_v154_signal},
    "f03_crash_depth_duration_dur_norm_open_252d_base_v155_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_252d_base_v155_signal},
    "f03_crash_depth_duration_depth_norm_open_252d_base_v156_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_252d_base_v156_signal},
    "f03_crash_depth_duration_depth_high_252d_base_v157_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_252d_base_v157_signal},
    "f03_crash_depth_duration_dur_high_252d_base_v158_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_252d_base_v158_signal},
    "f03_crash_depth_duration_severity_high_252d_base_v159_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_252d_base_v159_signal},
    "f03_crash_depth_duration_depth_zscore_high_252d_base_v160_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_252d_base_v160_signal},
    "f03_crash_depth_duration_dur_norm_high_252d_base_v161_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_252d_base_v161_signal},
    "f03_crash_depth_duration_depth_norm_high_252d_base_v162_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_252d_base_v162_signal},
    "f03_crash_depth_duration_depth_low_252d_base_v163_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_252d_base_v163_signal},
    "f03_crash_depth_duration_dur_low_252d_base_v164_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_252d_base_v164_signal},
    "f03_crash_depth_duration_severity_low_252d_base_v165_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_252d_base_v165_signal},
    "f03_crash_depth_duration_depth_zscore_low_252d_base_v166_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_252d_base_v166_signal},
    "f03_crash_depth_duration_dur_norm_low_252d_base_v167_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_252d_base_v167_signal},
    "f03_crash_depth_duration_depth_norm_low_252d_base_v168_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_252d_base_v168_signal},
    "f03_crash_depth_duration_depth_close_252d_base_v169_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_252d_base_v169_signal},
    "f03_crash_depth_duration_dur_close_252d_base_v170_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_252d_base_v170_signal},
    "f03_crash_depth_duration_severity_close_252d_base_v171_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_252d_base_v171_signal},
    "f03_crash_depth_duration_depth_zscore_close_252d_base_v172_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_252d_base_v172_signal},
    "f03_crash_depth_duration_dur_norm_close_252d_base_v173_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_252d_base_v173_signal},
    "f03_crash_depth_duration_depth_norm_close_252d_base_v174_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_252d_base_v174_signal},
    "f03_crash_depth_duration_depth_closeadj_252d_base_v175_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_252d_base_v175_signal},
    "f03_crash_depth_duration_dur_closeadj_252d_base_v176_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_252d_base_v176_signal},
    "f03_crash_depth_duration_severity_closeadj_252d_base_v177_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_252d_base_v177_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_252d_base_v178_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_252d_base_v178_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_252d_base_v179_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_252d_base_v179_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_252d_base_v180_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_252d_base_v180_signal}
}

if __name__ == "__main__":
    np.random.seed(42)
    n = 2500
    close = pd.Series(np.exp(np.random.normal(-0.02, 0.1, n).cumsum()) * 100)
    df = pd.DataFrame({
        'close': close, 'closeadj': close,
        'open': close.shift(1) * np.exp(np.random.normal(0, 0.02, n)),
        'high': close * np.exp(np.random.uniform(0, 0.05, n)),
        'low': close * np.exp(np.random.uniform(-0.05, 0, n)),
        'volume': np.random.randint(1000, 1000000, n).astype(float)
    }).ffill().bfill()
    
    for name, info in REGISTRY.items():
        res = info["func"](*[df[col] for col in info["inputs"]])
        assert len(res) > 0
        assert not res.isna().all()
    print("OK")
