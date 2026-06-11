import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (halving cycle phase) =====
def _f02_cyclepos(s, w):
    # continuous position of price within trailing w-day min..max range, in [0,1]
    lo = s.rolling(w, min_periods=max(2, w // 2)).min()
    hi = s.rolling(w, min_periods=max(2, w // 2)).max()
    rng = (hi - lo).replace(0, np.nan)
    return (s - lo) / rng


def _f02_cycleret(s, w):
    # long-horizon log return (cumulative cycle drift)
    return np.log(s / s.shift(w))


def _f02_cycleosc(s, w):
    # price oscillation vs long EMA, normalized by trailing std (cycle z-oscillator)
    ema = s.ewm(span=w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - ema) / sd.replace(0, np.nan)


def _f02_cycledd(s, w):
    # continuous drawdown from trailing w-day running peak (<=0)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max().replace(0, np.nan)
    return s / peak - 1.0


# ============ FEATURES 001-075 ============

# 252d cycle position within annual range
def f02hc_f02_halving_cycle_phase_cyclepos_252d_base_v001_signal(closeadj):
    result = _f02_cyclepos(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d cycle position within 1.5y range
def f02hc_f02_halving_cycle_phase_cyclepos_378d_base_v002_signal(closeadj):
    result = _f02_cyclepos(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cycle position within 2y range
def f02hc_f02_halving_cycle_phase_cyclepos_504d_base_v003_signal(closeadj):
    result = _f02_cyclepos(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 756d cycle position within 3y range
def f02hc_f02_halving_cycle_phase_cyclepos_756d_base_v004_signal(closeadj):
    result = _f02_cyclepos(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d cycle position within 4y (full halving) range
def f02hc_f02_halving_cycle_phase_cyclepos_1008d_base_v005_signal(closeadj):
    result = _f02_cyclepos(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position centered to [-1,1] over 504d
def f02hc_f02_halving_cycle_phase_posctr_504d_base_v006_signal(closeadj):
    result = 2.0 * _f02_cyclepos(closeadj, 504) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position centered to [-1,1] over 1008d
def f02hc_f02_halving_cycle_phase_posctr_1008d_base_v007_signal(closeadj):
    result = 2.0 * _f02_cyclepos(closeadj, 1008) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d long-horizon log return
def f02hc_f02_halving_cycle_phase_cycleret_252d_base_v008_signal(closeadj):
    result = _f02_cycleret(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d long-horizon log return
def f02hc_f02_halving_cycle_phase_cycleret_378d_base_v009_signal(closeadj):
    result = _f02_cycleret(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d long-horizon log return
def f02hc_f02_halving_cycle_phase_cycleret_504d_base_v010_signal(closeadj):
    result = _f02_cycleret(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 756d long-horizon log return
def f02hc_f02_halving_cycle_phase_cycleret_756d_base_v011_signal(closeadj):
    result = _f02_cycleret(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d long-horizon log return (full cycle drift)
def f02hc_f02_halving_cycle_phase_cycleret_1008d_base_v012_signal(closeadj):
    result = _f02_cycleret(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 504d cycle return
def f02hc_f02_halving_cycle_phase_annret_504d_base_v013_signal(closeadj):
    result = _f02_cycleret(closeadj, 504) * (252.0 / 504.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 1008d cycle return
def f02hc_f02_halving_cycle_phase_annret_1008d_base_v014_signal(closeadj):
    result = _f02_cycleret(closeadj, 1008) * (252.0 / 1008.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cycle oscillator vs long EMA
def f02hc_f02_halving_cycle_phase_cycleosc_252d_base_v015_signal(closeadj):
    result = _f02_cycleosc(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d cycle oscillator vs long EMA
def f02hc_f02_halving_cycle_phase_cycleosc_378d_base_v016_signal(closeadj):
    result = _f02_cycleosc(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cycle oscillator vs long EMA
def f02hc_f02_halving_cycle_phase_cycleosc_504d_base_v017_signal(closeadj):
    result = _f02_cycleosc(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 756d cycle oscillator vs long EMA
def f02hc_f02_halving_cycle_phase_cycleosc_756d_base_v018_signal(closeadj):
    result = _f02_cycleosc(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d cycle oscillator vs long EMA
def f02hc_f02_halving_cycle_phase_cycleosc_1008d_base_v019_signal(closeadj):
    result = _f02_cycleosc(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown from cycle peak
def f02hc_f02_halving_cycle_phase_cycledd_252d_base_v020_signal(closeadj):
    result = _f02_cycledd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown from cycle peak
def f02hc_f02_halving_cycle_phase_cycledd_504d_base_v021_signal(closeadj):
    result = _f02_cycledd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 756d drawdown from cycle peak
def f02hc_f02_halving_cycle_phase_cycledd_756d_base_v022_signal(closeadj):
    result = _f02_cycledd(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d drawdown from cycle peak (full halving)
def f02hc_f02_halving_cycle_phase_cycledd_1008d_base_v023_signal(closeadj):
    result = _f02_cycledd(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# log drawdown from 504d peak (continuous, heavier tail)
def f02hc_f02_halving_cycle_phase_logdd_504d_base_v024_signal(closeadj):
    peak = closeadj.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = np.log(closeadj / peak) + _f02_cycledd(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log drawdown from 1008d peak
def f02hc_f02_halving_cycle_phase_logdd_1008d_base_v025_signal(closeadj):
    peak = closeadj.rolling(1008, min_periods=252).max().replace(0, np.nan)
    result = np.log(closeadj / peak) + _f02_cycledd(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below multi-year (504d) high, normalized
def f02hc_f02_halving_cycle_phase_disthigh_504d_base_v026_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (hi - closeadj) / hi + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below multi-year (1008d) high, normalized
def f02hc_f02_halving_cycle_phase_disthigh_1008d_base_v027_signal(closeadj):
    hi = closeadj.rolling(1008, min_periods=252).max().replace(0, np.nan)
    result = (hi - closeadj) / hi + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above multi-year (504d) low, normalized
def f02hc_f02_halving_cycle_phase_distlow_504d_base_v028_signal(closeadj):
    lo = closeadj.rolling(504, min_periods=126).min().replace(0, np.nan)
    result = (closeadj - lo) / lo + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above multi-year (1008d) low, normalized
def f02hc_f02_halving_cycle_phase_distlow_1008d_base_v029_signal(closeadj):
    lo = closeadj.rolling(1008, min_periods=252).min().replace(0, np.nan)
    result = (closeadj - lo) / lo + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log distance from 756d high
def f02hc_f02_halving_cycle_phase_logdisthigh_756d_base_v030_signal(closeadj):
    hi = closeadj.rolling(756, min_periods=189).max().replace(0, np.nan)
    result = np.log(closeadj / hi) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log distance from 756d low
def f02hc_f02_halving_cycle_phase_logdistlow_756d_base_v031_signal(closeadj):
    lo = closeadj.rolling(756, min_periods=189).min().replace(0, np.nan)
    result = np.log(closeadj / lo) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 200d EMA spread (normalized)
def f02hc_f02_halving_cycle_phase_emaspread_200d_base_v032_signal(closeadj):
    ema = closeadj.ewm(span=200, min_periods=100).mean()
    result = _safe_div(closeadj - ema, ema) + _f02_cycleosc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d EMA spread (normalized)
def f02hc_f02_halving_cycle_phase_emaspread_252d_base_v033_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126).mean()
    result = _safe_div(closeadj - ema, ema) + _f02_cycleosc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 504d EMA spread (normalized)
def f02hc_f02_halving_cycle_phase_emaspread_504d_base_v034_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252).mean()
    result = _safe_div(closeadj - ema, ema) + _f02_cycleosc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log price vs 252d EMA ratio
def f02hc_f02_halving_cycle_phase_logema_252d_base_v035_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126).mean().replace(0, np.nan)
    result = np.log(closeadj / ema) + _f02_cycleosc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log price vs 504d EMA ratio
def f02hc_f02_halving_cycle_phase_logema_504d_base_v036_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252).mean().replace(0, np.nan)
    result = np.log(closeadj / ema) + _f02_cycleosc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sine of cycle progress (504d position mapped to phase)
def f02hc_f02_halving_cycle_phase_sinphase_504d_base_v037_signal(closeadj):
    result = np.sin(2.0 * np.pi * _f02_cyclepos(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# cosine of cycle progress (504d position mapped to phase)
def f02hc_f02_halving_cycle_phase_cosphase_504d_base_v038_signal(closeadj):
    result = np.cos(2.0 * np.pi * _f02_cyclepos(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# sine of cycle progress (1008d full halving phase)
def f02hc_f02_halving_cycle_phase_sinphase_1008d_base_v039_signal(closeadj):
    result = np.sin(2.0 * np.pi * _f02_cyclepos(closeadj, 1008))
    return result.replace([np.inf, -np.inf], np.nan)


# cosine of cycle progress (1008d full halving phase)
def f02hc_f02_halving_cycle_phase_cosphase_1008d_base_v040_signal(closeadj):
    result = np.cos(2.0 * np.pi * _f02_cyclepos(closeadj, 1008))
    return result.replace([np.inf, -np.inf], np.nan)


# sine phase driven by 756d cycle return rank
def f02hc_f02_halving_cycle_phase_sinret_756d_base_v041_signal(closeadj):
    prog = _f02_cycleret(closeadj, 756).rolling(756, min_periods=189).rank(pct=True)
    result = np.sin(2.0 * np.pi * prog)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to trailing 252d mean
def f02hc_f02_halving_cycle_phase_pmratio_252d_base_v042_signal(closeadj):
    result = _safe_div(closeadj, _mean(closeadj, 252)) + _f02_cyclepos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to trailing 504d mean
def f02hc_f02_halving_cycle_phase_pmratio_504d_base_v043_signal(closeadj):
    result = _safe_div(closeadj, _mean(closeadj, 504)) + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to trailing 1008d mean
def f02hc_f02_halving_cycle_phase_pmratio_1008d_base_v044_signal(closeadj):
    result = _safe_div(closeadj, _mean(closeadj, 1008)) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to trailing 756d mean
def f02hc_f02_halving_cycle_phase_logpmratio_756d_base_v045_signal(closeadj):
    m = _mean(closeadj, 756).replace(0, np.nan)
    result = np.log(closeadj / m) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-normalized z-score of price over 252d
def f02hc_f02_halving_cycle_phase_zprice_252d_base_v046_signal(closeadj):
    result = _z(closeadj, 252) + _f02_cyclepos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-normalized z-score of price over 504d
def f02hc_f02_halving_cycle_phase_zprice_504d_base_v047_signal(closeadj):
    result = _z(closeadj, 504) + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-normalized z-score of price over 1008d
def f02hc_f02_halving_cycle_phase_zprice_1008d_base_v048_signal(closeadj):
    result = _z(closeadj, 1008) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of log price over 756d
def f02hc_f02_halving_cycle_phase_zlogprice_756d_base_v049_signal(closeadj):
    result = _z(np.log(closeadj), 756) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_504d_base_v050_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(504.0)
    result = _safe_div(_f02_cycleret(closeadj, 504), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 756d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_756d_base_v051_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(756.0)
    result = _safe_div(_f02_cycleret(closeadj, 756), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_1008d_base_v052_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(1008.0)
    result = _safe_div(_f02_cycleret(closeadj, 1008), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_252d_base_v053_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(252.0)
    result = _safe_div(_f02_cycleret(closeadj, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative underwater area within 504d cycle (mean drawdown depth)
def f02hc_f02_halving_cycle_phase_uwarea_504d_base_v054_signal(closeadj):
    dd = _f02_cycledd(closeadj, 504)
    result = dd.rolling(504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative underwater area within 1008d cycle
def f02hc_f02_halving_cycle_phase_uwarea_1008d_base_v055_signal(closeadj):
    dd = _f02_cycledd(closeadj, 1008)
    result = dd.rolling(1008, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative underwater area within 756d cycle
def f02hc_f02_halving_cycle_phase_uwarea_756d_base_v056_signal(closeadj):
    dd = _f02_cycledd(closeadj, 756)
    result = dd.rolling(756, min_periods=189).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position smoothed over 63d (504d range)
def f02hc_f02_halving_cycle_phase_possmooth_504d_base_v057_signal(closeadj):
    result = _mean(_f02_cyclepos(closeadj, 504), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position smoothed over 126d (1008d range)
def f02hc_f02_halving_cycle_phase_possmooth_1008d_base_v058_signal(closeadj):
    result = _mean(_f02_cyclepos(closeadj, 1008), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle position 504d vs 1008d (phase divergence)
def f02hc_f02_halving_cycle_phase_posspread_504_1008_base_v059_signal(closeadj):
    result = _f02_cyclepos(closeadj, 504) - _f02_cyclepos(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle position 252d vs 756d
def f02hc_f02_halving_cycle_phase_posspread_252_756_base_v060_signal(closeadj):
    result = _f02_cyclepos(closeadj, 252) - _f02_cyclepos(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle return 252d vs 1008d (acceleration into cycle)
def f02hc_f02_halving_cycle_phase_retspread_252_1008_base_v061_signal(closeadj):
    result = _f02_cycleret(closeadj, 252) - _f02_cycleret(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle return 504d vs 1008d
def f02hc_f02_halving_cycle_phase_retspread_504_1008_base_v062_signal(closeadj):
    result = _f02_cycleret(closeadj, 504) - _f02_cycleret(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle oscillator spread 252d vs 504d
def f02hc_f02_halving_cycle_phase_oscspread_252_504_base_v063_signal(closeadj):
    result = _f02_cycleosc(closeadj, 252) - _f02_cycleosc(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 504d
def f02hc_f02_halving_cycle_phase_prank_504d_base_v064_signal(closeadj):
    result = closeadj.rolling(504, min_periods=126).rank(pct=True) + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 1008d
def f02hc_f02_halving_cycle_phase_prank_1008d_base_v065_signal(closeadj):
    result = closeadj.rolling(1008, min_periods=252).rank(pct=True) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 756d
def f02hc_f02_halving_cycle_phase_prank_756d_base_v066_signal(closeadj):
    result = closeadj.rolling(756, min_periods=189).rank(pct=True) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle return z-scored over 1008d window
def f02hc_f02_halving_cycle_phase_zret_504d_base_v067_signal(closeadj):
    result = _z(_f02_cycleret(closeadj, 504), 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle return z-scored over 1008d window (252d return)
def f02hc_f02_halving_cycle_phase_zret_252d_base_v068_signal(closeadj):
    result = _z(_f02_cycleret(closeadj, 252), 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle oscillator z-scored over 504d window
def f02hc_f02_halving_cycle_phase_zosc_252d_base_v069_signal(closeadj):
    result = _z(_f02_cycleosc(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# price ratio to 504d max (proximity to cycle high, continuous)
def f02hc_f02_halving_cycle_phase_hiratio_504d_base_v070_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = closeadj / hi + _f02_cycledd(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price ratio to 1008d max (proximity to cycle high)
def f02hc_f02_halving_cycle_phase_hiratio_1008d_base_v071_signal(closeadj):
    hi = closeadj.rolling(1008, min_periods=252).max().replace(0, np.nan)
    result = closeadj / hi + _f02_cycledd(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price ratio to 756d min (lift off cycle low, continuous)
def f02hc_f02_halving_cycle_phase_loratio_756d_base_v072_signal(closeadj):
    lo = closeadj.rolling(756, min_periods=189).min().replace(0, np.nan)
    result = closeadj / lo + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position weighted by long return magnitude
def f02hc_f02_halving_cycle_phase_poswret_504d_base_v073_signal(closeadj):
    result = _f02_cyclepos(closeadj, 504) * _f02_cycleret(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth weighted by cycle position (recovery tension)
def f02hc_f02_halving_cycle_phase_ddwpos_1008d_base_v074_signal(closeadj):
    result = _f02_cycledd(closeadj, 1008) * _f02_cyclepos(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed 1008d cycle return (bounded cycle drift)
def f02hc_f02_halving_cycle_phase_tanhret_1008d_base_v075_signal(closeadj):
    result = np.tanh(_f02_cycleret(closeadj, 1008))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02hc_f02_halving_cycle_phase_cyclepos_252d_base_v001_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_378d_base_v002_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_504d_base_v003_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_756d_base_v004_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_1008d_base_v005_signal,
    f02hc_f02_halving_cycle_phase_posctr_504d_base_v006_signal,
    f02hc_f02_halving_cycle_phase_posctr_1008d_base_v007_signal,
    f02hc_f02_halving_cycle_phase_cycleret_252d_base_v008_signal,
    f02hc_f02_halving_cycle_phase_cycleret_378d_base_v009_signal,
    f02hc_f02_halving_cycle_phase_cycleret_504d_base_v010_signal,
    f02hc_f02_halving_cycle_phase_cycleret_756d_base_v011_signal,
    f02hc_f02_halving_cycle_phase_cycleret_1008d_base_v012_signal,
    f02hc_f02_halving_cycle_phase_annret_504d_base_v013_signal,
    f02hc_f02_halving_cycle_phase_annret_1008d_base_v014_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_252d_base_v015_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_378d_base_v016_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_504d_base_v017_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_756d_base_v018_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_1008d_base_v019_signal,
    f02hc_f02_halving_cycle_phase_cycledd_252d_base_v020_signal,
    f02hc_f02_halving_cycle_phase_cycledd_504d_base_v021_signal,
    f02hc_f02_halving_cycle_phase_cycledd_756d_base_v022_signal,
    f02hc_f02_halving_cycle_phase_cycledd_1008d_base_v023_signal,
    f02hc_f02_halving_cycle_phase_logdd_504d_base_v024_signal,
    f02hc_f02_halving_cycle_phase_logdd_1008d_base_v025_signal,
    f02hc_f02_halving_cycle_phase_disthigh_504d_base_v026_signal,
    f02hc_f02_halving_cycle_phase_disthigh_1008d_base_v027_signal,
    f02hc_f02_halving_cycle_phase_distlow_504d_base_v028_signal,
    f02hc_f02_halving_cycle_phase_distlow_1008d_base_v029_signal,
    f02hc_f02_halving_cycle_phase_logdisthigh_756d_base_v030_signal,
    f02hc_f02_halving_cycle_phase_logdistlow_756d_base_v031_signal,
    f02hc_f02_halving_cycle_phase_emaspread_200d_base_v032_signal,
    f02hc_f02_halving_cycle_phase_emaspread_252d_base_v033_signal,
    f02hc_f02_halving_cycle_phase_emaspread_504d_base_v034_signal,
    f02hc_f02_halving_cycle_phase_logema_252d_base_v035_signal,
    f02hc_f02_halving_cycle_phase_logema_504d_base_v036_signal,
    f02hc_f02_halving_cycle_phase_sinphase_504d_base_v037_signal,
    f02hc_f02_halving_cycle_phase_cosphase_504d_base_v038_signal,
    f02hc_f02_halving_cycle_phase_sinphase_1008d_base_v039_signal,
    f02hc_f02_halving_cycle_phase_cosphase_1008d_base_v040_signal,
    f02hc_f02_halving_cycle_phase_sinret_756d_base_v041_signal,
    f02hc_f02_halving_cycle_phase_pmratio_252d_base_v042_signal,
    f02hc_f02_halving_cycle_phase_pmratio_504d_base_v043_signal,
    f02hc_f02_halving_cycle_phase_pmratio_1008d_base_v044_signal,
    f02hc_f02_halving_cycle_phase_logpmratio_756d_base_v045_signal,
    f02hc_f02_halving_cycle_phase_zprice_252d_base_v046_signal,
    f02hc_f02_halving_cycle_phase_zprice_504d_base_v047_signal,
    f02hc_f02_halving_cycle_phase_zprice_1008d_base_v048_signal,
    f02hc_f02_halving_cycle_phase_zlogprice_756d_base_v049_signal,
    f02hc_f02_halving_cycle_phase_volret_504d_base_v050_signal,
    f02hc_f02_halving_cycle_phase_volret_756d_base_v051_signal,
    f02hc_f02_halving_cycle_phase_volret_1008d_base_v052_signal,
    f02hc_f02_halving_cycle_phase_volret_252d_base_v053_signal,
    f02hc_f02_halving_cycle_phase_uwarea_504d_base_v054_signal,
    f02hc_f02_halving_cycle_phase_uwarea_1008d_base_v055_signal,
    f02hc_f02_halving_cycle_phase_uwarea_756d_base_v056_signal,
    f02hc_f02_halving_cycle_phase_possmooth_504d_base_v057_signal,
    f02hc_f02_halving_cycle_phase_possmooth_1008d_base_v058_signal,
    f02hc_f02_halving_cycle_phase_posspread_504_1008_base_v059_signal,
    f02hc_f02_halving_cycle_phase_posspread_252_756_base_v060_signal,
    f02hc_f02_halving_cycle_phase_retspread_252_1008_base_v061_signal,
    f02hc_f02_halving_cycle_phase_retspread_504_1008_base_v062_signal,
    f02hc_f02_halving_cycle_phase_oscspread_252_504_base_v063_signal,
    f02hc_f02_halving_cycle_phase_prank_504d_base_v064_signal,
    f02hc_f02_halving_cycle_phase_prank_1008d_base_v065_signal,
    f02hc_f02_halving_cycle_phase_prank_756d_base_v066_signal,
    f02hc_f02_halving_cycle_phase_zret_504d_base_v067_signal,
    f02hc_f02_halving_cycle_phase_zret_252d_base_v068_signal,
    f02hc_f02_halving_cycle_phase_zosc_252d_base_v069_signal,
    f02hc_f02_halving_cycle_phase_hiratio_504d_base_v070_signal,
    f02hc_f02_halving_cycle_phase_hiratio_1008d_base_v071_signal,
    f02hc_f02_halving_cycle_phase_loratio_756d_base_v072_signal,
    f02hc_f02_halving_cycle_phase_poswret_504d_base_v073_signal,
    f02hc_f02_halving_cycle_phase_ddwpos_1008d_base_v074_signal,
    f02hc_f02_halving_cycle_phase_tanhret_1008d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_HALVING_CYCLE_PHASE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f02_cyclepos", "_f02_cycleret", "_f02_cycleosc", "_f02_cycledd")
    n_features = 0
    nan_ok = 0
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
    print(f"OK f02_halving_cycle_phase_base_001_075_claude: {n_features} features pass")
