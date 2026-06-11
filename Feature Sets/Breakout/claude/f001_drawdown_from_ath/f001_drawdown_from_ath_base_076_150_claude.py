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


def _drawdown(s, w):
    path_max = s.rolling(w, min_periods=1).max()
    return (s - path_max) / path_max.replace(0, np.nan)


def _rsi(s, w):
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w, min_periods=max(1, w // 2)).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w, min_periods=max(1, w // 2)).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


# ===== folder domain primitives =====


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v076_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base) * (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v077_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base) * (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v078_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base) * (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v079_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base) * (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v080_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base) * (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v081_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v082_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v083_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v084_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v085_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v086_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v087_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v088_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v089_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v090_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v091_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v092_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v093_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v094_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v095_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v096_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = np.tanh(_z(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v097_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = np.tanh(_z(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v098_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = np.tanh(_z(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v099_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = np.tanh(_z(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v100_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = np.tanh(_z(base, 126))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v101_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v102_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v103_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v104_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v105_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v106_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).ewm(span=63, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v107_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).ewm(span=63, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v108_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).ewm(span=63, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v109_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).ewm(span=63, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v110_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).ewm(span=63, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v111_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v112_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v113_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v114_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v115_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v116_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v117_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v118_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v119_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v120_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v121_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v122_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v123_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v124_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v125_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).rolling(126, min_periods=max(1, 126 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v126_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v127_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v128_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v129_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v130_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v131_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).rolling(252, min_periods=max(4, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v132_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).rolling(252, min_periods=max(4, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v133_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).rolling(252, min_periods=max(4, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v134_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).rolling(252, min_periods=max(4, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v135_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).rolling(252, min_periods=max(4, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v136_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v137_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v138_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v139_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v140_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v141_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v142_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v143_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v144_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v145_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v146_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v147_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v148_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v149_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v150_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v076_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v077_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v078_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v079_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v080_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v081_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v082_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v083_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v084_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v085_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v086_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v087_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v088_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v089_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v090_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v091_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v092_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v093_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v094_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v095_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v096_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v097_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v098_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v099_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v100_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v101_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v102_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v103_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v104_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v105_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v106_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v107_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v108_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v109_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v110_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v111_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v112_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v113_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v114_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v115_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v116_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v117_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v118_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v119_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v120_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v121_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v122_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v123_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v124_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v125_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v126_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v127_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v128_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v129_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v130_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v131_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v132_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v133_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v134_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v135_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v136_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v137_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v138_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v139_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v140_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v141_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v142_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v143_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v144_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v145_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v146_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v147_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v148_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v149_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F001_DRAWDOWN_FROM_ATH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_drawdown",)
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
    print(f"OK f001_drawdown_from_ath_base_076_150_claude: {n_features} features pass")
