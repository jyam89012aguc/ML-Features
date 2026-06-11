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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f13_hl_range(h, l):
    return h - l


def _f13_hl_pct(h, l, c):
    return (h - l) / c.shift(1).replace(0, np.nan)


def _f13_true_range(h, l, c):
    pc = c.shift(1)
    tr1 = h - l
    tr2 = (h - pc).abs()
    tr3 = (l - pc).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def _f13_atr(h, l, c, w):
    tr = _f13_true_range(h, l, c)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


# 21d position-in-range of HL range
def f13ir_f13_semi_intraday_range_dynamics_rngposition_21d_base_v076_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 21)
    hi = _max(hl, 21)
    result = (hl - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of HL range
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_base_v077_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    result = (hl - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of HL range
def f13ir_f13_semi_intraday_range_dynamics_rngposition_126d_base_v078_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 126)
    hi = _max(hl, 126)
    result = (hl - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of HL range
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_base_v079_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    result = (hl - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of HL range
def f13ir_f13_semi_intraday_range_dynamics_rngposition_504d_base_v080_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 504)
    hi = _max(hl, 504)
    result = (hl - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance from rolling-high
def f13ir_f13_semi_intraday_range_dynamics_highdistfromhigh_21d_base_v081_signal(high, low, closeadj):
    rh = _max(high, 21)
    result = (high - rh) / rh.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance from rolling-high
def f13ir_f13_semi_intraday_range_dynamics_highdistfromhigh_63d_base_v082_signal(high, low, closeadj):
    rh = _max(high, 63)
    result = (high - rh) / rh.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d distance from rolling-high
def f13ir_f13_semi_intraday_range_dynamics_highdistfromhigh_126d_base_v083_signal(high, low, closeadj):
    rh = _max(high, 126)
    result = (high - rh) / rh.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance from rolling-high
def f13ir_f13_semi_intraday_range_dynamics_highdistfromhigh_252d_base_v084_signal(high, low, closeadj):
    rh = _max(high, 252)
    result = (high - rh) / rh.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distance from rolling-high
def f13ir_f13_semi_intraday_range_dynamics_highdistfromhigh_504d_base_v085_signal(high, low, closeadj):
    rh = _max(high, 504)
    result = (high - rh) / rh.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance from rolling-low
def f13ir_f13_semi_intraday_range_dynamics_lowdistfromlow_21d_base_v086_signal(high, low, closeadj):
    rl = _min(low, 21)
    result = (low - rl) / rl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance from rolling-low
def f13ir_f13_semi_intraday_range_dynamics_lowdistfromlow_63d_base_v087_signal(high, low, closeadj):
    rl = _min(low, 63)
    result = (low - rl) / rl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d distance from rolling-low
def f13ir_f13_semi_intraday_range_dynamics_lowdistfromlow_126d_base_v088_signal(high, low, closeadj):
    rl = _min(low, 126)
    result = (low - rl) / rl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance from rolling-low
def f13ir_f13_semi_intraday_range_dynamics_lowdistfromlow_252d_base_v089_signal(high, low, closeadj):
    rl = _min(low, 252)
    result = (low - rl) / rl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distance from rolling-low
def f13ir_f13_semi_intraday_range_dynamics_lowdistfromlow_504d_base_v090_signal(high, low, closeadj):
    rl = _min(low, 504)
    result = (low - rl) / rl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 21d ATR to 63d ATR
def f13ir_f13_semi_intraday_range_dynamics_atrratio_21v63_base_v091_signal(high, low, closeadj):
    atr_s = _f13_atr(high, low, closeadj, 21)
    atr_l = _f13_atr(high, low, closeadj, 63)
    result = atr_s / atr_l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 21d ATR to 126d ATR
def f13ir_f13_semi_intraday_range_dynamics_atrratio_21v126_base_v092_signal(high, low, closeadj):
    atr_s = _f13_atr(high, low, closeadj, 21)
    atr_l = _f13_atr(high, low, closeadj, 126)
    result = atr_s / atr_l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 63d ATR to 126d ATR
def f13ir_f13_semi_intraday_range_dynamics_atrratio_63v126_base_v093_signal(high, low, closeadj):
    atr_s = _f13_atr(high, low, closeadj, 63)
    atr_l = _f13_atr(high, low, closeadj, 126)
    result = atr_s / atr_l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 63d ATR to 252d ATR
def f13ir_f13_semi_intraday_range_dynamics_atrratio_63v252_base_v094_signal(high, low, closeadj):
    atr_s = _f13_atr(high, low, closeadj, 63)
    atr_l = _f13_atr(high, low, closeadj, 252)
    result = atr_s / atr_l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 126d ATR to 252d ATR
def f13ir_f13_semi_intraday_range_dynamics_atrratio_126v252_base_v095_signal(high, low, closeadj):
    atr_s = _f13_atr(high, low, closeadj, 126)
    atr_l = _f13_atr(high, low, closeadj, 252)
    result = atr_s / atr_l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of HL range
def f13ir_f13_semi_intraday_range_dynamics_skewhl_21d_base_v096_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of HL range
def f13ir_f13_semi_intraday_range_dynamics_skewhl_63d_base_v097_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of HL range
def f13ir_f13_semi_intraday_range_dynamics_skewhl_126d_base_v098_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of HL range
def f13ir_f13_semi_intraday_range_dynamics_skewhl_252d_base_v099_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of HL range
def f13ir_f13_semi_intraday_range_dynamics_skewhl_504d_base_v100_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of HL range
def f13ir_f13_semi_intraday_range_dynamics_kurthl_21d_base_v101_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of HL range
def f13ir_f13_semi_intraday_range_dynamics_kurthl_63d_base_v102_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of HL range
def f13ir_f13_semi_intraday_range_dynamics_kurthl_126d_base_v103_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of HL range
def f13ir_f13_semi_intraday_range_dynamics_kurthl_252d_base_v104_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of HL range
def f13ir_f13_semi_intraday_range_dynamics_kurthl_504d_base_v105_signal(high, low, closeadj):
    hl = high - low
    result = hl.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of inside-bar days
def f13ir_f13_semi_intraday_range_dynamics_insidebarct_21d_base_v106_signal(high, low, closeadj):
    ib = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    result = ib.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of inside-bar days
def f13ir_f13_semi_intraday_range_dynamics_insidebarct_63d_base_v107_signal(high, low, closeadj):
    ib = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    result = ib.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of inside-bar days
def f13ir_f13_semi_intraday_range_dynamics_insidebarct_126d_base_v108_signal(high, low, closeadj):
    ib = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    result = ib.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of inside-bar days
def f13ir_f13_semi_intraday_range_dynamics_insidebarct_252d_base_v109_signal(high, low, closeadj):
    ib = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    result = ib.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of inside-bar days
def f13ir_f13_semi_intraday_range_dynamics_insidebarct_504d_base_v110_signal(high, low, closeadj):
    ib = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    result = ib.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of outside-bar days
def f13ir_f13_semi_intraday_range_dynamics_outsidebarct_21d_base_v111_signal(high, low, closeadj):
    ob = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    result = ob.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of outside-bar days
def f13ir_f13_semi_intraday_range_dynamics_outsidebarct_63d_base_v112_signal(high, low, closeadj):
    ob = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    result = ob.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of outside-bar days
def f13ir_f13_semi_intraday_range_dynamics_outsidebarct_126d_base_v113_signal(high, low, closeadj):
    ob = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    result = ob.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of outside-bar days
def f13ir_f13_semi_intraday_range_dynamics_outsidebarct_252d_base_v114_signal(high, low, closeadj):
    ob = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    result = ob.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of outside-bar days
def f13ir_f13_semi_intraday_range_dynamics_outsidebarct_504d_base_v115_signal(high, low, closeadj):
    ob = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    result = ob.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of strong close (close in upper 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_strongclose_21d_base_v116_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos > 0.8).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of strong close (close in upper 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_base_v117_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of strong close (close in upper 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_strongclose_126d_base_v118_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos > 0.8).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of strong close (close in upper 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_base_v119_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of strong close (close in upper 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_strongclose_504d_base_v120_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos > 0.8).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of weak close (close in lower 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_weakclose_21d_base_v121_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos < 0.2).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of weak close (close in lower 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_base_v122_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of weak close (close in lower 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_weakclose_126d_base_v123_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos < 0.2).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of weak close (close in lower 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_base_v124_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of weak close (close in lower 20% of daily range)
def f13ir_f13_semi_intraday_range_dynamics_weakclose_504d_base_v125_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = (pos < 0.2).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of ATR
def f13ir_f13_semi_intraday_range_dynamics_atrz_21d_base_v126_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    result = _z(atr, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of ATR
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_base_v127_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    result = _z(atr, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of ATR
def f13ir_f13_semi_intraday_range_dynamics_atrz_126d_base_v128_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    result = _z(atr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of ATR
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_base_v129_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    result = _z(atr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of ATR
def f13ir_f13_semi_intraday_range_dynamics_atrz_504d_base_v130_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 504)
    result = _z(atr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of HL-to-ATR ratio (range expansion z)
def f13ir_f13_semi_intraday_range_dynamics_rngexpz_21d_base_v131_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 21)
    result = _z(hl / atr.replace(0, np.nan), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of HL-to-ATR ratio (range expansion z)
def f13ir_f13_semi_intraday_range_dynamics_rngexpz_63d_base_v132_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    result = _z(hl / atr.replace(0, np.nan), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of HL-to-ATR ratio (range expansion z)
def f13ir_f13_semi_intraday_range_dynamics_rngexpz_126d_base_v133_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 126)
    result = _z(hl / atr.replace(0, np.nan), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of HL-to-ATR ratio (range expansion z)
def f13ir_f13_semi_intraday_range_dynamics_rngexpz_252d_base_v134_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    result = _z(hl / atr.replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of HL-to-ATR ratio (range expansion z)
def f13ir_f13_semi_intraday_range_dynamics_rngexpz_504d_base_v135_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 504)
    result = _z(hl / atr.replace(0, np.nan), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR-to-vol ratio (path roughness)
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_21d_base_v136_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    vol = _std(closeadj.pct_change(), 21) * closeadj
    result = atr / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR-to-vol ratio (path roughness)
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_base_v137_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    result = atr / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ATR-to-vol ratio (path roughness)
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_126d_base_v138_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    vol = _std(closeadj.pct_change(), 126) * closeadj
    result = atr / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR-to-vol ratio (path roughness)
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_252d_base_v139_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    vol = _std(closeadj.pct_change(), 252) * closeadj
    result = atr / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ATR-to-vol ratio (path roughness)
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_504d_base_v140_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 504)
    vol = _std(closeadj.pct_change(), 504) * closeadj
    result = atr / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of ATR from rolling peak
def f13ir_f13_semi_intraday_range_dynamics_atrdd_21d_base_v141_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    result = atr - _max(atr, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of ATR from rolling peak
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_base_v142_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    result = atr - _max(atr, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of ATR from rolling peak
def f13ir_f13_semi_intraday_range_dynamics_atrdd_126d_base_v143_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    result = atr - _max(atr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of ATR from rolling peak
def f13ir_f13_semi_intraday_range_dynamics_atrdd_252d_base_v144_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    result = atr - _max(atr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of ATR from rolling peak
def f13ir_f13_semi_intraday_range_dynamics_atrdd_504d_base_v145_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 504)
    result = atr - _max(atr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range EMA crossover 5v21
def f13ir_f13_semi_intraday_range_dynamics_hlema_5v21_base_v146_signal(high, low, closeadj):
    hl = high - low
    result = hl.ewm(span=5, adjust=False).mean() - hl.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range EMA crossover 21v63
def f13ir_f13_semi_intraday_range_dynamics_hlema_21v63_base_v147_signal(high, low, closeadj):
    hl = high - low
    result = hl.ewm(span=21, adjust=False).mean() - hl.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range EMA crossover 63v126
def f13ir_f13_semi_intraday_range_dynamics_hlema_63v126_base_v148_signal(high, low, closeadj):
    hl = high - low
    result = hl.ewm(span=63, adjust=False).mean() - hl.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range EMA crossover 126v252
def f13ir_f13_semi_intraday_range_dynamics_hlema_126v252_base_v149_signal(high, low, closeadj):
    hl = high - low
    result = hl.ewm(span=126, adjust=False).mean() - hl.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range EMA crossover 252v504
def f13ir_f13_semi_intraday_range_dynamics_hlema_252v504_base_v150_signal(high, low, closeadj):
    hl = high - low
    result = hl.ewm(span=252, adjust=False).mean() - hl.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
