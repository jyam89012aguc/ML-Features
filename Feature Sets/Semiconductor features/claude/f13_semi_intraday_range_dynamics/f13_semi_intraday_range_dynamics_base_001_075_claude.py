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


# 21d average true range
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_base_v001_signal(high, low, closeadj):
    result = _f13_atr(high, low, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d average true range
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_base_v002_signal(high, low, closeadj):
    result = _f13_atr(high, low, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d average true range
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_base_v003_signal(high, low, closeadj):
    result = _f13_atr(high, low, closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d average true range
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_base_v004_signal(high, low, closeadj):
    result = _f13_atr(high, low, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d average true range
def f13ir_f13_semi_intraday_range_dynamics_atr_504d_base_v005_signal(high, low, closeadj):
    result = _f13_atr(high, low, closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR normalized by close
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_base_v006_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    result = atr / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR normalized by close
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_base_v007_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    result = atr / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ATR normalized by close
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_base_v008_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    result = atr / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR normalized by close
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_base_v009_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    result = atr / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ATR normalized by close
def f13ir_f13_semi_intraday_range_dynamics_atrpct_504d_base_v010_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 504)
    result = atr / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of high-low range
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_base_v011_signal(high, low, closeadj):
    hl = high - low
    result = _mean(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of high-low range
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_base_v012_signal(high, low, closeadj):
    hl = high - low
    result = _mean(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of high-low range
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_base_v013_signal(high, low, closeadj):
    hl = high - low
    result = _mean(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of high-low range
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_base_v014_signal(high, low, closeadj):
    hl = high - low
    result = _mean(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of high-low range
def f13ir_f13_semi_intraday_range_dynamics_meanhl_504d_base_v015_signal(high, low, closeadj):
    hl = high - low
    result = _mean(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of HL range as pct of prev close
def f13ir_f13_semi_intraday_range_dynamics_meanhlpct_21d_base_v016_signal(high, low, closeadj):
    hl = (high - low) / closeadj.shift(1).replace(0, np.nan)
    result = _mean(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of HL range as pct of prev close
def f13ir_f13_semi_intraday_range_dynamics_meanhlpct_63d_base_v017_signal(high, low, closeadj):
    hl = (high - low) / closeadj.shift(1).replace(0, np.nan)
    result = _mean(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of HL range as pct of prev close
def f13ir_f13_semi_intraday_range_dynamics_meanhlpct_126d_base_v018_signal(high, low, closeadj):
    hl = (high - low) / closeadj.shift(1).replace(0, np.nan)
    result = _mean(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of HL range as pct of prev close
def f13ir_f13_semi_intraday_range_dynamics_meanhlpct_252d_base_v019_signal(high, low, closeadj):
    hl = (high - low) / closeadj.shift(1).replace(0, np.nan)
    result = _mean(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of HL range as pct of prev close
def f13ir_f13_semi_intraday_range_dynamics_meanhlpct_504d_base_v020_signal(high, low, closeadj):
    hl = (high - low) / closeadj.shift(1).replace(0, np.nan)
    result = _mean(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of high-low range
def f13ir_f13_semi_intraday_range_dynamics_stdhl_21d_base_v021_signal(high, low, closeadj):
    hl = high - low
    result = _std(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of high-low range
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_base_v022_signal(high, low, closeadj):
    hl = high - low
    result = _std(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of high-low range
def f13ir_f13_semi_intraday_range_dynamics_stdhl_126d_base_v023_signal(high, low, closeadj):
    hl = high - low
    result = _std(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of high-low range
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_base_v024_signal(high, low, closeadj):
    hl = high - low
    result = _std(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of high-low range
def f13ir_f13_semi_intraday_range_dynamics_stdhl_504d_base_v025_signal(high, low, closeadj):
    hl = high - low
    result = _std(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of high-low range
def f13ir_f13_semi_intraday_range_dynamics_zhl_21d_base_v026_signal(high, low, closeadj):
    hl = high - low
    result = _z(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of high-low range
def f13ir_f13_semi_intraday_range_dynamics_zhl_63d_base_v027_signal(high, low, closeadj):
    hl = high - low
    result = _z(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of high-low range
def f13ir_f13_semi_intraday_range_dynamics_zhl_126d_base_v028_signal(high, low, closeadj):
    hl = high - low
    result = _z(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of high-low range
def f13ir_f13_semi_intraday_range_dynamics_zhl_252d_base_v029_signal(high, low, closeadj):
    hl = high - low
    result = _z(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of high-low range
def f13ir_f13_semi_intraday_range_dynamics_zhl_504d_base_v030_signal(high, low, closeadj):
    hl = high - low
    result = _z(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Parkinson volatility
def f13ir_f13_semi_intraday_range_dynamics_parkinson_21d_base_v031_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    result = (r * r).rolling(21, min_periods=11).mean() / (4 * np.log(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Parkinson volatility
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_base_v032_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    result = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Parkinson volatility
def f13ir_f13_semi_intraday_range_dynamics_parkinson_126d_base_v033_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    result = (r * r).rolling(126, min_periods=63).mean() / (4 * np.log(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Parkinson volatility
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_base_v034_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    result = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Parkinson volatility
def f13ir_f13_semi_intraday_range_dynamics_parkinson_504d_base_v035_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    result = (r * r).rolling(504, min_periods=252).mean() / (4 * np.log(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Garman-Klass volatility
def f13ir_f13_semi_intraday_range_dynamics_gkvol_21d_base_v036_signal(high, low, closeadj):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk.rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Garman-Klass volatility
def f13ir_f13_semi_intraday_range_dynamics_gkvol_63d_base_v037_signal(high, low, closeadj):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk.rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Garman-Klass volatility
def f13ir_f13_semi_intraday_range_dynamics_gkvol_126d_base_v038_signal(high, low, closeadj):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Garman-Klass volatility
def f13ir_f13_semi_intraday_range_dynamics_gkvol_252d_base_v039_signal(high, low, closeadj):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Garman-Klass volatility
def f13ir_f13_semi_intraday_range_dynamics_gkvol_504d_base_v040_signal(high, low, closeadj):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk.rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of close position in daily HL range
def f13ir_f13_semi_intraday_range_dynamics_closepos_21d_base_v041_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = _mean(pos, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of close position in daily HL range
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_base_v042_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = _mean(pos, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of close position in daily HL range
def f13ir_f13_semi_intraday_range_dynamics_closepos_126d_base_v043_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = _mean(pos, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of close position in daily HL range
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_base_v044_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = _mean(pos, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of close position in daily HL range
def f13ir_f13_semi_intraday_range_dynamics_closepos_504d_base_v045_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    result = _mean(pos, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of TR as pct of close
def f13ir_f13_semi_intraday_range_dynamics_meantrpct_21d_base_v046_signal(high, low, closeadj):
    tr = _f13_true_range(high, low, closeadj)
    result = _mean(tr / closeadj.replace(0, np.nan), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of TR as pct of close
def f13ir_f13_semi_intraday_range_dynamics_meantrpct_63d_base_v047_signal(high, low, closeadj):
    tr = _f13_true_range(high, low, closeadj)
    result = _mean(tr / closeadj.replace(0, np.nan), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of TR as pct of close
def f13ir_f13_semi_intraday_range_dynamics_meantrpct_126d_base_v048_signal(high, low, closeadj):
    tr = _f13_true_range(high, low, closeadj)
    result = _mean(tr / closeadj.replace(0, np.nan), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of TR as pct of close
def f13ir_f13_semi_intraday_range_dynamics_meantrpct_252d_base_v049_signal(high, low, closeadj):
    tr = _f13_true_range(high, low, closeadj)
    result = _mean(tr / closeadj.replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of TR as pct of close
def f13ir_f13_semi_intraday_range_dynamics_meantrpct_504d_base_v050_signal(high, low, closeadj):
    tr = _f13_true_range(high, low, closeadj)
    result = _mean(tr / closeadj.replace(0, np.nan), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max high-low range
def f13ir_f13_semi_intraday_range_dynamics_maxhl_21d_base_v051_signal(high, low, closeadj):
    hl = high - low
    result = _max(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max high-low range
def f13ir_f13_semi_intraday_range_dynamics_maxhl_63d_base_v052_signal(high, low, closeadj):
    hl = high - low
    result = _max(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max high-low range
def f13ir_f13_semi_intraday_range_dynamics_maxhl_126d_base_v053_signal(high, low, closeadj):
    hl = high - low
    result = _max(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max high-low range
def f13ir_f13_semi_intraday_range_dynamics_maxhl_252d_base_v054_signal(high, low, closeadj):
    hl = high - low
    result = _max(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max high-low range
def f13ir_f13_semi_intraday_range_dynamics_maxhl_504d_base_v055_signal(high, low, closeadj):
    hl = high - low
    result = _max(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min high-low range
def f13ir_f13_semi_intraday_range_dynamics_minhl_21d_base_v056_signal(high, low, closeadj):
    hl = high - low
    result = _min(hl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min high-low range
def f13ir_f13_semi_intraday_range_dynamics_minhl_63d_base_v057_signal(high, low, closeadj):
    hl = high - low
    result = _min(hl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min high-low range
def f13ir_f13_semi_intraday_range_dynamics_minhl_126d_base_v058_signal(high, low, closeadj):
    hl = high - low
    result = _min(hl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min high-low range
def f13ir_f13_semi_intraday_range_dynamics_minhl_252d_base_v059_signal(high, low, closeadj):
    hl = high - low
    result = _min(hl, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min high-low range
def f13ir_f13_semi_intraday_range_dynamics_minhl_504d_base_v060_signal(high, low, closeadj):
    hl = high - low
    result = _min(hl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range expansion (HL today / 21d ATR)
def f13ir_f13_semi_intraday_range_dynamics_rngexp_21d_base_v061_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 21)
    result = hl / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range expansion (HL today / 63d ATR)
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_base_v062_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    result = hl / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range expansion (HL today / 126d ATR)
def f13ir_f13_semi_intraday_range_dynamics_rngexp_126d_base_v063_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 126)
    result = hl / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range expansion (HL today / 252d ATR)
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_base_v064_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    result = hl / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range expansion (HL today / 504d ATR)
def f13ir_f13_semi_intraday_range_dynamics_rngexp_504d_base_v065_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 504)
    result = hl / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of high above prev close
def f13ir_f13_semi_intraday_range_dynamics_highabovepc_21d_base_v066_signal(high, low, closeadj):
    hp = high / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(hp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of high above prev close
def f13ir_f13_semi_intraday_range_dynamics_highabovepc_63d_base_v067_signal(high, low, closeadj):
    hp = high / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(hp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of high above prev close
def f13ir_f13_semi_intraday_range_dynamics_highabovepc_126d_base_v068_signal(high, low, closeadj):
    hp = high / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(hp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of high above prev close
def f13ir_f13_semi_intraday_range_dynamics_highabovepc_252d_base_v069_signal(high, low, closeadj):
    hp = high / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(hp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of high above prev close
def f13ir_f13_semi_intraday_range_dynamics_highabovepc_504d_base_v070_signal(high, low, closeadj):
    hp = high / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(hp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of low below prev close
def f13ir_f13_semi_intraday_range_dynamics_lowbelowpc_21d_base_v071_signal(high, low, closeadj):
    lp = low / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(lp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of low below prev close
def f13ir_f13_semi_intraday_range_dynamics_lowbelowpc_63d_base_v072_signal(high, low, closeadj):
    lp = low / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(lp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of low below prev close
def f13ir_f13_semi_intraday_range_dynamics_lowbelowpc_126d_base_v073_signal(high, low, closeadj):
    lp = low / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(lp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of low below prev close
def f13ir_f13_semi_intraday_range_dynamics_lowbelowpc_252d_base_v074_signal(high, low, closeadj):
    lp = low / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(lp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of low below prev close
def f13ir_f13_semi_intraday_range_dynamics_lowbelowpc_504d_base_v075_signal(high, low, closeadj):
    lp = low / closeadj.shift(1).replace(0, np.nan) - 1.0
    result = _mean(lp, 504)
    return result.replace([np.inf, -np.inf], np.nan)
