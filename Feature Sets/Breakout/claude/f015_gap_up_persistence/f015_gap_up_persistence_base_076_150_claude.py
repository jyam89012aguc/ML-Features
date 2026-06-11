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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f015_gap_proxy(close, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    return ret / sd.replace(0, np.nan)


def _f015_gap_persistence(close, volume, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    gap_z = ret / sd.replace(0, np.nan)
    pos_gap = gap_z.clip(lower=0)
    vlz = volume / volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (pos_gap * vlz).rolling(w, min_periods=max(1, w // 2)).sum()


def _f015_conviction_gap(close, volume, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    gap_z = ret / sd.replace(0, np.nan)
    pos_gap = gap_z.clip(lower=0)
    vlz = volume / volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    smoothed = (pos_gap * vlz).rolling(w, min_periods=max(1, w // 2)).mean()
    return smoothed * close


def f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v076_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v077_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v078_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v079_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v080_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v081_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v082_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v083_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v084_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v085_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v086_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v087_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v088_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v089_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v090_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_base_v091_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_base_v092_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_base_v093_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_378d_base_v094_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_504d_base_v095_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_5d_base_v096_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_10d_base_v097_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_base_v098_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_base_v099_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_base_v100_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_base_v101_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_base_v102_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_base_v103_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_378d_base_v104_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_504d_base_v105_signal(closeadj, volume):
    result = _z(_f015_conviction_gap(closeadj, volume, 504), 252) * _safe_div(_mean(closeadj, 63), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v106_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v107_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v108_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v109_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v110_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v111_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v112_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v113_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v114_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v115_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v116_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v117_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v118_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v119_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v120_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_base_v121_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_base_v122_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_base_v123_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_378d_base_v124_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_504d_base_v125_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_5d_base_v126_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_10d_base_v127_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_base_v128_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_base_v129_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_base_v130_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_base_v131_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_base_v132_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_base_v133_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_378d_base_v134_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_504d_base_v135_signal(closeadj, volume):
    result = (_f015_conviction_gap(closeadj, volume, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v136_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 5)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v137_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 10)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v138_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 21)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v139_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 42)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v140_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 63)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v141_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 126)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v142_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 189)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v143_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 252)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v144_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 378)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v145_signal(closeadj):
    result = (_f015_gap_proxy(closeadj, 504)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v146_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 5)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v147_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 10)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v148_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v149_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v150_signal(closeadj, volume):
    result = (_f015_gap_persistence(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v076_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v077_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v078_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v079_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v080_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v081_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v082_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v083_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v084_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v085_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v086_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v087_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v088_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v089_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v090_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_base_v091_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_base_v092_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_base_v093_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_378d_base_v094_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_504d_base_v095_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_5d_base_v096_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_10d_base_v097_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_base_v098_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_base_v099_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_base_v100_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_base_v101_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_base_v102_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_base_v103_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_378d_base_v104_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_504d_base_v105_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v106_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v107_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v108_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v109_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v110_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v111_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v112_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v113_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v114_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v115_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v116_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v117_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v118_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v119_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v120_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_base_v121_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_base_v122_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_base_v123_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_378d_base_v124_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_504d_base_v125_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_5d_base_v126_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_10d_base_v127_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_base_v128_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_base_v129_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_base_v130_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_base_v131_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_base_v132_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_base_v133_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_378d_base_v134_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_504d_base_v135_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_5d_base_v136_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_10d_base_v137_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_base_v138_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_base_v139_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_base_v140_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_base_v141_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_base_v142_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_base_v143_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_378d_base_v144_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_504d_base_v145_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_5d_base_v146_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_10d_base_v147_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_base_v148_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_base_v149_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F015_GAP_UP_PERSISTENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {
        "closeadj": closeadj,
        "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f015_gap_proxy", "_f015_gap_persistence", "_f015_conviction_gap")
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f015_gap_up_persistence_076_150_claude: {n_features} features pass")
