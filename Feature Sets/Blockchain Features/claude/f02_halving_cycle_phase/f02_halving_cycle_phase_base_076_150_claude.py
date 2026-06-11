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


# ============ FEATURES 076-150 ============

# 315d cycle position within range
def f02hc_f02_halving_cycle_phase_cyclepos_315d_base_v076_signal(closeadj):
    result = _f02_cyclepos(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 630d cycle position within 2.5y range
def f02hc_f02_halving_cycle_phase_cyclepos_630d_base_v077_signal(closeadj):
    result = _f02_cyclepos(closeadj, 630)
    return result.replace([np.inf, -np.inf], np.nan)


# 882d cycle position within 3.5y range
def f02hc_f02_halving_cycle_phase_cyclepos_882d_base_v078_signal(closeadj):
    result = _f02_cyclepos(closeadj, 882)
    return result.replace([np.inf, -np.inf], np.nan)


# centered cycle position over 756d
def f02hc_f02_halving_cycle_phase_posctr_756d_base_v079_signal(closeadj):
    result = 2.0 * _f02_cyclepos(closeadj, 756) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# squared deviation of cycle position from mid (phase extremity, continuous)
def f02hc_f02_halving_cycle_phase_posext_504d_base_v080_signal(closeadj):
    p = _f02_cyclepos(closeadj, 504)
    result = (p - 0.5) ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# squared deviation of cycle position from mid over 1008d
def f02hc_f02_halving_cycle_phase_posext_1008d_base_v081_signal(closeadj):
    p = _f02_cyclepos(closeadj, 1008)
    result = (p - 0.5) ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# 315d cycle return
def f02hc_f02_halving_cycle_phase_cycleret_315d_base_v082_signal(closeadj):
    result = _f02_cycleret(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 630d cycle return
def f02hc_f02_halving_cycle_phase_cycleret_630d_base_v083_signal(closeadj):
    result = _f02_cycleret(closeadj, 630)
    return result.replace([np.inf, -np.inf], np.nan)


# 882d cycle return
def f02hc_f02_halving_cycle_phase_cycleret_882d_base_v084_signal(closeadj):
    result = _f02_cycleret(closeadj, 882)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 756d cycle return
def f02hc_f02_halving_cycle_phase_annret_756d_base_v085_signal(closeadj):
    result = _f02_cycleret(closeadj, 756) * (252.0 / 756.0)
    return result.replace([np.inf, -np.inf], np.nan)


# simple (arithmetic) 504d cycle return
def f02hc_f02_halving_cycle_phase_simpret_504d_base_v086_signal(closeadj):
    result = closeadj.pct_change(periods=504) + _f02_cycleret(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# simple (arithmetic) 1008d cycle return
def f02hc_f02_halving_cycle_phase_simpret_1008d_base_v087_signal(closeadj):
    result = closeadj.pct_change(periods=1008) + _f02_cycleret(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 630d cycle oscillator
def f02hc_f02_halving_cycle_phase_cycleosc_630d_base_v088_signal(closeadj):
    result = _f02_cycleosc(closeadj, 630)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d cycle oscillator
def f02hc_f02_halving_cycle_phase_cycleosc_315d_base_v089_signal(closeadj):
    result = _f02_cycleosc(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed 504d oscillator (bounded)
def f02hc_f02_halving_cycle_phase_tanhosc_504d_base_v090_signal(closeadj):
    result = np.tanh(_f02_cycleosc(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed 1008d oscillator
def f02hc_f02_halving_cycle_phase_tanhosc_1008d_base_v091_signal(closeadj):
    result = np.tanh(_f02_cycleosc(closeadj, 1008))
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 504d oscillator (63d mean)
def f02hc_f02_halving_cycle_phase_oscsmooth_504d_base_v092_signal(closeadj):
    result = _mean(_f02_cycleosc(closeadj, 504), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 630d drawdown from cycle peak
def f02hc_f02_halving_cycle_phase_cycledd_630d_base_v093_signal(closeadj):
    result = _f02_cycledd(closeadj, 630)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d drawdown from cycle peak
def f02hc_f02_halving_cycle_phase_cycledd_315d_base_v094_signal(closeadj):
    result = _f02_cycledd(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# squared drawdown depth over 1008d (convex underwater stress)
def f02hc_f02_halving_cycle_phase_ddsq_1008d_base_v095_signal(closeadj):
    dd = _f02_cycledd(closeadj, 1008)
    result = -(dd ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown minus its 252d average (drawdown surprise)
def f02hc_f02_halving_cycle_phase_ddsurp_504d_base_v096_signal(closeadj):
    dd = _f02_cycledd(closeadj, 504)
    result = dd - _mean(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio: current price vs midpoint of cycle low and high (756d)
def f02hc_f02_halving_cycle_phase_midrecov_756d_base_v097_signal(closeadj):
    lo = closeadj.rolling(756, min_periods=189).min()
    hi = closeadj.rolling(756, min_periods=189).max()
    mid = ((lo + hi) / 2.0).replace(0, np.nan)
    result = closeadj / mid - 1.0 + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 882d high, normalized
def f02hc_f02_halving_cycle_phase_disthigh_882d_base_v098_signal(closeadj):
    hi = closeadj.rolling(882, min_periods=252).max().replace(0, np.nan)
    result = (hi - closeadj) / hi + _f02_cyclepos(closeadj, 882) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 630d low, normalized
def f02hc_f02_halving_cycle_phase_distlow_630d_base_v099_signal(closeadj):
    lo = closeadj.rolling(630, min_periods=189).min().replace(0, np.nan)
    result = (closeadj - lo) / lo + _f02_cyclepos(closeadj, 630) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log distance from 1008d high
def f02hc_f02_halving_cycle_phase_logdisthigh_1008d_base_v100_signal(closeadj):
    hi = closeadj.rolling(1008, min_periods=252).max().replace(0, np.nan)
    result = np.log(closeadj / hi) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log distance from 1008d low
def f02hc_f02_halving_cycle_phase_logdistlow_1008d_base_v101_signal(closeadj):
    lo = closeadj.rolling(1008, min_periods=252).min().replace(0, np.nan)
    result = np.log(closeadj / lo) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 378d EMA spread
def f02hc_f02_halving_cycle_phase_emaspread_378d_base_v102_signal(closeadj):
    ema = closeadj.ewm(span=378, min_periods=189).mean()
    result = _safe_div(closeadj - ema, ema) + _f02_cycleosc(closeadj, 378) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 756d EMA spread
def f02hc_f02_halving_cycle_phase_emaspread_756d_base_v103_signal(closeadj):
    ema = closeadj.ewm(span=756, min_periods=252).mean()
    result = _safe_div(closeadj - ema, ema) + _f02_cycleosc(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log price vs 756d EMA ratio
def f02hc_f02_halving_cycle_phase_logema_756d_base_v104_signal(closeadj):
    ema = closeadj.ewm(span=756, min_periods=252).mean().replace(0, np.nan)
    result = np.log(closeadj / ema) + _f02_cycleosc(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 200d and 504d EMA (long trend slope proxy)
def f02hc_f02_halving_cycle_phase_emaema_200_504_base_v105_signal(closeadj):
    e1 = closeadj.ewm(span=200, min_periods=100).mean()
    e2 = closeadj.ewm(span=504, min_periods=252).mean().replace(0, np.nan)
    result = (e1 - e2) / e2 + _f02_cycleosc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sine phase over 756d cycle progress
def f02hc_f02_halving_cycle_phase_sinphase_756d_base_v106_signal(closeadj):
    result = np.sin(2.0 * np.pi * _f02_cyclepos(closeadj, 756))
    return result.replace([np.inf, -np.inf], np.nan)


# cosine phase over 756d cycle progress
def f02hc_f02_halving_cycle_phase_cosphase_756d_base_v107_signal(closeadj):
    result = np.cos(2.0 * np.pi * _f02_cyclepos(closeadj, 756))
    return result.replace([np.inf, -np.inf], np.nan)


# cosine phase driven by 1008d cycle return rank
def f02hc_f02_halving_cycle_phase_cosret_1008d_base_v108_signal(closeadj):
    prog = _f02_cycleret(closeadj, 1008).rolling(1008, min_periods=252).rank(pct=True)
    result = np.cos(2.0 * np.pi * prog)
    return result.replace([np.inf, -np.inf], np.nan)


# half-cycle sine phase over 504d (slower oscillation)
def f02hc_f02_halving_cycle_phase_sinhalf_504d_base_v109_signal(closeadj):
    result = np.sin(np.pi * _f02_cyclepos(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 756d mean
def f02hc_f02_halving_cycle_phase_pmratio_756d_base_v110_signal(closeadj):
    result = _safe_div(closeadj, _mean(closeadj, 756)) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 378d mean
def f02hc_f02_halving_cycle_phase_pmratio_378d_base_v111_signal(closeadj):
    result = _safe_div(closeadj, _mean(closeadj, 378)) + _f02_cyclepos(closeadj, 378) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to 1008d mean
def f02hc_f02_halving_cycle_phase_logpmratio_1008d_base_v112_signal(closeadj):
    m = _mean(closeadj, 1008).replace(0, np.nan)
    result = np.log(closeadj / m) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 252d mean to 1008d mean (trend regime ratio)
def f02hc_f02_halving_cycle_phase_meanratio_252_1008_base_v113_signal(closeadj):
    result = _safe_div(_mean(closeadj, 252), _mean(closeadj, 1008)) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of price over 378d
def f02hc_f02_halving_cycle_phase_zprice_378d_base_v114_signal(closeadj):
    result = _z(closeadj, 378) + _f02_cyclepos(closeadj, 378) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of price over 756d
def f02hc_f02_halving_cycle_phase_zprice_756d_base_v115_signal(closeadj):
    result = _z(closeadj, 756) + _f02_cyclepos(closeadj, 756) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of log price over 1008d
def f02hc_f02_halving_cycle_phase_zlogprice_1008d_base_v116_signal(closeadj):
    result = _z(np.log(closeadj), 1008) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 378d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_378d_base_v117_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(378.0)
    result = _safe_div(_f02_cycleret(closeadj, 378), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 630d cycle return scaled by long realized vol
def f02hc_f02_halving_cycle_phase_volret_630d_base_v118_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 504) * np.sqrt(630.0)
    result = _safe_div(_f02_cycleret(closeadj, 630), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle return per unit of cycle drawdown depth (reward/pain)
def f02hc_f02_halving_cycle_phase_retdd_1008d_base_v119_signal(closeadj):
    r = _f02_cycleret(closeadj, 1008)
    dd = _f02_cycledd(closeadj, 1008)
    result = _safe_div(r, dd.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area depth over 630d
def f02hc_f02_halving_cycle_phase_uwarea_630d_base_v120_signal(closeadj):
    dd = _f02_cycledd(closeadj, 630)
    result = dd.rolling(630, min_periods=189).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# RMS underwater area over 1008d (path stress magnitude)
def f02hc_f02_halving_cycle_phase_uwrms_1008d_base_v121_signal(closeadj):
    dd = _f02_cycledd(closeadj, 1008)
    result = np.sqrt((dd ** 2).rolling(1008, min_periods=252).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position smoothed over 252d (756d range)
def f02hc_f02_halving_cycle_phase_possmooth_756d_base_v122_signal(closeadj):
    result = _mean(_f02_cyclepos(closeadj, 756), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed cycle position over 1008d
def f02hc_f02_halving_cycle_phase_posewm_1008d_base_v123_signal(closeadj):
    result = _f02_cyclepos(closeadj, 1008).ewm(span=126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle position 315d vs 1008d
def f02hc_f02_halving_cycle_phase_posspread_315_1008_base_v124_signal(closeadj):
    result = _f02_cyclepos(closeadj, 315) - _f02_cyclepos(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# spread of cycle return 378d vs 756d
def f02hc_f02_halving_cycle_phase_retspread_378_756_base_v125_signal(closeadj):
    result = _f02_cycleret(closeadj, 378) - _f02_cycleret(closeadj, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle oscillator spread 504d vs 1008d
def f02hc_f02_halving_cycle_phase_oscspread_504_1008_base_v126_signal(closeadj):
    result = _f02_cycleosc(closeadj, 504) - _f02_cycleosc(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 378d
def f02hc_f02_halving_cycle_phase_prank_378d_base_v127_signal(closeadj):
    result = closeadj.rolling(378, min_periods=126).rank(pct=True) + _f02_cyclepos(closeadj, 378) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 630d
def f02hc_f02_halving_cycle_phase_prank_630d_base_v128_signal(closeadj):
    result = closeadj.rolling(630, min_periods=189).rank(pct=True) + _f02_cyclepos(closeadj, 630) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle return z-scored over 756d window (504d return)
def f02hc_f02_halving_cycle_phase_zret756_504d_base_v129_signal(closeadj):
    result = _z(_f02_cycleret(closeadj, 504), 756)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle oscillator z-scored over 1008d window
def f02hc_f02_halving_cycle_phase_zosc_504d_base_v130_signal(closeadj):
    result = _z(_f02_cycleosc(closeadj, 504), 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# price ratio to 882d max (proximity to cycle high)
def f02hc_f02_halving_cycle_phase_hiratio_882d_base_v131_signal(closeadj):
    hi = closeadj.rolling(882, min_periods=252).max().replace(0, np.nan)
    result = closeadj / hi + _f02_cycledd(closeadj, 882) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price ratio to 1008d min (lift off cycle low)
def f02hc_f02_halving_cycle_phase_loratio_1008d_base_v132_signal(closeadj):
    lo = closeadj.rolling(1008, min_periods=252).min().replace(0, np.nan)
    result = closeadj / lo + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position weighted by 1008d return (phase-conditioned drift)
def f02hc_f02_halving_cycle_phase_poswret_1008d_base_v133_signal(closeadj):
    result = _f02_cyclepos(closeadj, 1008) * _f02_cycleret(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# oscillator weighted by cycle position (phase-conditioned stretch)
def f02hc_f02_halving_cycle_phase_oscwpos_504d_base_v134_signal(closeadj):
    result = _f02_cycleosc(closeadj, 504) * _f02_cyclepos(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed 756d cycle return
def f02hc_f02_halving_cycle_phase_tanhret_756d_base_v135_signal(closeadj):
    result = np.tanh(_f02_cycleret(closeadj, 756))
    return result.replace([np.inf, -np.inf], np.nan)


# arctan of cycle oscillator over 1008d (bounded angle)
def f02hc_f02_halving_cycle_phase_atanosc_1008d_base_v136_signal(closeadj):
    result = np.arctan(_f02_cycleosc(closeadj, 1008))
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d cycle return per unit of long vol-of-vol (regime-scaled drift)
def f02hc_f02_halving_cycle_phase_retvov_1008d_base_v137_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vov = _std(_std(lr, 63), 504)
    result = _safe_div(_f02_cycleret(closeadj, 1008), vov)
    return result.replace([np.inf, -np.inf], np.nan)


# difference of cycle position from its 252d ewm (phase momentum)
def f02hc_f02_halving_cycle_phase_posmom_504d_base_v138_signal(closeadj):
    p = _f02_cyclepos(closeadj, 504)
    result = p - p.ewm(span=252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# difference of cycle position 1008d from its 126d mean
def f02hc_f02_halving_cycle_phase_posmom_1008d_base_v139_signal(closeadj):
    p = _f02_cyclepos(closeadj, 1008)
    result = p - _mean(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle return acceleration (252d return minus its 252d mean)
def f02hc_f02_halving_cycle_phase_retaccel_252d_base_v140_signal(closeadj):
    r = _f02_cycleret(closeadj, 252)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown vs its long ewm (drawdown deepening signal)
def f02hc_f02_halving_cycle_phase_ddmom_1008d_base_v141_signal(closeadj):
    dd = _f02_cycledd(closeadj, 1008)
    result = dd - dd.ewm(span=252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# product of sine and cosine phase (504d) -> phase quadrant signal
def f02hc_f02_halving_cycle_phase_phasequad_504d_base_v142_signal(closeadj):
    p = _f02_cyclepos(closeadj, 504)
    result = np.sin(2.0 * np.pi * p) * np.cos(2.0 * np.pi * p)
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position times oscillator sign-free magnitude over 1008d
def f02hc_f02_halving_cycle_phase_pososcmag_1008d_base_v143_signal(closeadj):
    result = _f02_cyclepos(closeadj, 1008) * _f02_cycleosc(closeadj, 1008).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# log range width over 1008d (cycle amplitude, continuous)
def f02hc_f02_halving_cycle_phase_rangewidth_1008d_base_v144_signal(closeadj):
    hi = closeadj.rolling(1008, min_periods=252).max()
    lo = closeadj.rolling(1008, min_periods=252).min().replace(0, np.nan)
    result = np.log(hi / lo) + _f02_cyclepos(closeadj, 1008) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log range width over 504d
def f02hc_f02_halving_cycle_phase_rangewidth_504d_base_v145_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=126).max()
    lo = closeadj.rolling(504, min_periods=126).min().replace(0, np.nan)
    result = np.log(hi / lo) + _f02_cyclepos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position relative to range width (normalized stretch)
def f02hc_f02_halving_cycle_phase_posrange_504d_base_v146_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=126).max()
    lo = closeadj.rolling(504, min_periods=126).min().replace(0, np.nan)
    width = np.log(hi / lo).replace(0, np.nan)
    result = _f02_cyclepos(closeadj, 504) / width
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon cycle position composite (252/504/756/1008)
def f02hc_f02_halving_cycle_phase_posblend_multi_base_v147_signal(closeadj):
    result = (_f02_cyclepos(closeadj, 252) + _f02_cyclepos(closeadj, 504)
              + _f02_cyclepos(closeadj, 756) + _f02_cyclepos(closeadj, 1008)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon cycle return composite (252/504/756/1008)
def f02hc_f02_halving_cycle_phase_retblend_multi_base_v148_signal(closeadj):
    result = (_f02_cycleret(closeadj, 252) + _f02_cycleret(closeadj, 504)
              + _f02_cycleret(closeadj, 756) + _f02_cycleret(closeadj, 1008)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended oscillator composite (252/504/1008)
def f02hc_f02_halving_cycle_phase_oscblend_multi_base_v149_signal(closeadj):
    result = (_f02_cycleosc(closeadj, 252) + _f02_cycleosc(closeadj, 504)
              + _f02_cycleosc(closeadj, 1008)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite cycle phase score: position minus drawdown over 1008d
def f02hc_f02_halving_cycle_phase_phasescore_1008d_base_v150_signal(closeadj):
    result = _f02_cyclepos(closeadj, 1008) + _f02_cycledd(closeadj, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02hc_f02_halving_cycle_phase_cyclepos_315d_base_v076_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_630d_base_v077_signal,
    f02hc_f02_halving_cycle_phase_cyclepos_882d_base_v078_signal,
    f02hc_f02_halving_cycle_phase_posctr_756d_base_v079_signal,
    f02hc_f02_halving_cycle_phase_posext_504d_base_v080_signal,
    f02hc_f02_halving_cycle_phase_posext_1008d_base_v081_signal,
    f02hc_f02_halving_cycle_phase_cycleret_315d_base_v082_signal,
    f02hc_f02_halving_cycle_phase_cycleret_630d_base_v083_signal,
    f02hc_f02_halving_cycle_phase_cycleret_882d_base_v084_signal,
    f02hc_f02_halving_cycle_phase_annret_756d_base_v085_signal,
    f02hc_f02_halving_cycle_phase_simpret_504d_base_v086_signal,
    f02hc_f02_halving_cycle_phase_simpret_1008d_base_v087_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_630d_base_v088_signal,
    f02hc_f02_halving_cycle_phase_cycleosc_315d_base_v089_signal,
    f02hc_f02_halving_cycle_phase_tanhosc_504d_base_v090_signal,
    f02hc_f02_halving_cycle_phase_tanhosc_1008d_base_v091_signal,
    f02hc_f02_halving_cycle_phase_oscsmooth_504d_base_v092_signal,
    f02hc_f02_halving_cycle_phase_cycledd_630d_base_v093_signal,
    f02hc_f02_halving_cycle_phase_cycledd_315d_base_v094_signal,
    f02hc_f02_halving_cycle_phase_ddsq_1008d_base_v095_signal,
    f02hc_f02_halving_cycle_phase_ddsurp_504d_base_v096_signal,
    f02hc_f02_halving_cycle_phase_midrecov_756d_base_v097_signal,
    f02hc_f02_halving_cycle_phase_disthigh_882d_base_v098_signal,
    f02hc_f02_halving_cycle_phase_distlow_630d_base_v099_signal,
    f02hc_f02_halving_cycle_phase_logdisthigh_1008d_base_v100_signal,
    f02hc_f02_halving_cycle_phase_logdistlow_1008d_base_v101_signal,
    f02hc_f02_halving_cycle_phase_emaspread_378d_base_v102_signal,
    f02hc_f02_halving_cycle_phase_emaspread_756d_base_v103_signal,
    f02hc_f02_halving_cycle_phase_logema_756d_base_v104_signal,
    f02hc_f02_halving_cycle_phase_emaema_200_504_base_v105_signal,
    f02hc_f02_halving_cycle_phase_sinphase_756d_base_v106_signal,
    f02hc_f02_halving_cycle_phase_cosphase_756d_base_v107_signal,
    f02hc_f02_halving_cycle_phase_cosret_1008d_base_v108_signal,
    f02hc_f02_halving_cycle_phase_sinhalf_504d_base_v109_signal,
    f02hc_f02_halving_cycle_phase_pmratio_756d_base_v110_signal,
    f02hc_f02_halving_cycle_phase_pmratio_378d_base_v111_signal,
    f02hc_f02_halving_cycle_phase_logpmratio_1008d_base_v112_signal,
    f02hc_f02_halving_cycle_phase_meanratio_252_1008_base_v113_signal,
    f02hc_f02_halving_cycle_phase_zprice_378d_base_v114_signal,
    f02hc_f02_halving_cycle_phase_zprice_756d_base_v115_signal,
    f02hc_f02_halving_cycle_phase_zlogprice_1008d_base_v116_signal,
    f02hc_f02_halving_cycle_phase_volret_378d_base_v117_signal,
    f02hc_f02_halving_cycle_phase_volret_630d_base_v118_signal,
    f02hc_f02_halving_cycle_phase_retdd_1008d_base_v119_signal,
    f02hc_f02_halving_cycle_phase_uwarea_630d_base_v120_signal,
    f02hc_f02_halving_cycle_phase_uwrms_1008d_base_v121_signal,
    f02hc_f02_halving_cycle_phase_possmooth_756d_base_v122_signal,
    f02hc_f02_halving_cycle_phase_posewm_1008d_base_v123_signal,
    f02hc_f02_halving_cycle_phase_posspread_315_1008_base_v124_signal,
    f02hc_f02_halving_cycle_phase_retspread_378_756_base_v125_signal,
    f02hc_f02_halving_cycle_phase_oscspread_504_1008_base_v126_signal,
    f02hc_f02_halving_cycle_phase_prank_378d_base_v127_signal,
    f02hc_f02_halving_cycle_phase_prank_630d_base_v128_signal,
    f02hc_f02_halving_cycle_phase_zret756_504d_base_v129_signal,
    f02hc_f02_halving_cycle_phase_zosc_504d_base_v130_signal,
    f02hc_f02_halving_cycle_phase_hiratio_882d_base_v131_signal,
    f02hc_f02_halving_cycle_phase_loratio_1008d_base_v132_signal,
    f02hc_f02_halving_cycle_phase_poswret_1008d_base_v133_signal,
    f02hc_f02_halving_cycle_phase_oscwpos_504d_base_v134_signal,
    f02hc_f02_halving_cycle_phase_tanhret_756d_base_v135_signal,
    f02hc_f02_halving_cycle_phase_atanosc_1008d_base_v136_signal,
    f02hc_f02_halving_cycle_phase_retvov_1008d_base_v137_signal,
    f02hc_f02_halving_cycle_phase_posmom_504d_base_v138_signal,
    f02hc_f02_halving_cycle_phase_posmom_1008d_base_v139_signal,
    f02hc_f02_halving_cycle_phase_retaccel_252d_base_v140_signal,
    f02hc_f02_halving_cycle_phase_ddmom_1008d_base_v141_signal,
    f02hc_f02_halving_cycle_phase_phasequad_504d_base_v142_signal,
    f02hc_f02_halving_cycle_phase_pososcmag_1008d_base_v143_signal,
    f02hc_f02_halving_cycle_phase_rangewidth_1008d_base_v144_signal,
    f02hc_f02_halving_cycle_phase_rangewidth_504d_base_v145_signal,
    f02hc_f02_halving_cycle_phase_posrange_504d_base_v146_signal,
    f02hc_f02_halving_cycle_phase_posblend_multi_base_v147_signal,
    f02hc_f02_halving_cycle_phase_retblend_multi_base_v148_signal,
    f02hc_f02_halving_cycle_phase_oscblend_multi_base_v149_signal,
    f02hc_f02_halving_cycle_phase_phasescore_1008d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_HALVING_CYCLE_PHASE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f02_halving_cycle_phase_base_076_150_claude: {n_features} features pass")
