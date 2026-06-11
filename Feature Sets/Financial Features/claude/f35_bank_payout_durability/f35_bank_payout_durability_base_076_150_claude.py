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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f35_payout_floor(payoutratio, w):
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()


def _f35_payout_durability(payoutratio, eps, w):
    mu = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = eps.rolling(w, min_periods=max(1, w // 2)).std()
    return mu / sd.replace(0, np.nan)


def _f35_payout_sustainability(payoutratio, fcfps, w):
    margin = (1.0 - payoutratio)
    fcf_g = fcfps.pct_change(periods=w)
    return margin * fcf_g


# ===== features =====
def f35bpd_f35_bank_payout_durability_payoutfloorema_10d_base_v076_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_21d_base_v077_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_42d_base_v078_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 42)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_63d_base_v079_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_126d_base_v080_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_189d_base_v081_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 189)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_252d_base_v082_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_378d_base_v083_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 378)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_504d_base_v084_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorema_5d_base_v085_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_21d_base_v086_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = _std(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_42d_base_v087_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 42)
    result = _std(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_63d_base_v088_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_126d_base_v089_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_189d_base_v090_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 189)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_252d_base_v091_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_378d_base_v092_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 378)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurstd_504d_base_v093_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_21d_base_v094_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 21)
    result = _qrank(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_63d_base_v095_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = _qrank(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_126d_base_v096_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 126)
    result = _qrank(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_252d_base_v097_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = _qrank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_504d_base_v098_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = _qrank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustqrank_42d_base_v099_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 42)
    result = _qrank(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_21d_base_v100_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_63d_base_v101_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_126d_base_v102_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_252d_base_v103_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_504d_base_v104_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxeps_42d_base_v105_signal(payoutratio, eps, closeadj):
    base = _f35_payout_floor(payoutratio, 42)
    result = base * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxc_21d_base_v106_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = base * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxc_63d_base_v107_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxc_126d_base_v108_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxc_252d_base_v109_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = base * _mean(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxc_504d_base_v110_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = base * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxfcfps_21d_base_v111_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 21)
    result = base * fcfps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxfcfps_63d_base_v112_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = base * fcfps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxfcfps_126d_base_v113_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 126)
    result = base * fcfps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxfcfps_252d_base_v114_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = base * fcfps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxfcfps_504d_base_v115_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = base * fcfps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutheadroom_21d_base_v116_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = (payoutratio - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutheadroom_63d_base_v117_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = (payoutratio - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutheadroom_126d_base_v118_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = (payoutratio - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutheadroom_252d_base_v119_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = (payoutratio - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutheadroom_504d_base_v120_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = (payoutratio - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurdiff_21d_base_v121_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = (base - base.shift(7)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurdiff_63d_base_v122_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurdiff_126d_base_v123_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = (base - base.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurdiff_252d_base_v124_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = (base - base.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurdiff_504d_base_v125_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = (base - base.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustdiff_21d_base_v126_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 21)
    result = (base - base.shift(7)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustdiff_63d_base_v127_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustdiff_126d_base_v128_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 126)
    result = (base - base.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustdiff_252d_base_v129_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = (base - base.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustdiff_504d_base_v130_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = (base - base.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_21d_base_v131_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = _qrank(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_63d_base_v132_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = _qrank(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_126d_base_v133_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = _qrank(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_252d_base_v134_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = _qrank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_504d_base_v135_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = _qrank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorqrank_42d_base_v136_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 42)
    result = _qrank(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_21d_base_v137_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    dg = dps.pct_change(periods=21)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_63d_base_v138_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    dg = dps.pct_change(periods=63)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_126d_base_v139_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    dg = dps.pct_change(periods=126)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_252d_base_v140_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    dg = dps.pct_change(periods=252)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_504d_base_v141_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    dg = dps.pct_change(periods=504)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdpsg_42d_base_v142_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 42)
    dg = dps.pct_change(periods=42)
    result = base * dg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_21d_base_v143_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 21)
    d = _f35_payout_durability(payoutratio, eps, 21)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_42d_base_v144_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 42)
    d = _f35_payout_durability(payoutratio, eps, 42)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_63d_base_v145_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 63)
    d = _f35_payout_durability(payoutratio, eps, 63)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_126d_base_v146_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 126)
    d = _f35_payout_durability(payoutratio, eps, 126)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_189d_base_v147_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 189)
    d = _f35_payout_durability(payoutratio, eps, 189)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_252d_base_v148_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 252)
    d = _f35_payout_durability(payoutratio, eps, 252)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_378d_base_v149_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 378)
    d = _f35_payout_durability(payoutratio, eps, 378)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutcomposite_504d_base_v150_signal(payoutratio, eps, closeadj):
    f = _f35_payout_floor(payoutratio, 504)
    d = _f35_payout_durability(payoutratio, eps, 504)
    result = (f + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35bpd_f35_bank_payout_durability_payoutfloorema_10d_base_v076_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_21d_base_v077_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_42d_base_v078_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_63d_base_v079_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_126d_base_v080_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_189d_base_v081_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_252d_base_v082_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_378d_base_v083_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_504d_base_v084_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorema_5d_base_v085_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_21d_base_v086_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_42d_base_v087_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_63d_base_v088_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_126d_base_v089_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_189d_base_v090_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_252d_base_v091_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_378d_base_v092_signal,
    f35bpd_f35_bank_payout_durability_payoutdurstd_504d_base_v093_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_21d_base_v094_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_63d_base_v095_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_126d_base_v096_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_252d_base_v097_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_504d_base_v098_signal,
    f35bpd_f35_bank_payout_durability_payoutsustqrank_42d_base_v099_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_21d_base_v100_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_63d_base_v101_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_126d_base_v102_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_252d_base_v103_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_504d_base_v104_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxeps_42d_base_v105_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxc_21d_base_v106_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxc_63d_base_v107_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxc_126d_base_v108_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxc_252d_base_v109_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxc_504d_base_v110_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxfcfps_21d_base_v111_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxfcfps_63d_base_v112_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxfcfps_126d_base_v113_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxfcfps_252d_base_v114_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxfcfps_504d_base_v115_signal,
    f35bpd_f35_bank_payout_durability_payoutheadroom_21d_base_v116_signal,
    f35bpd_f35_bank_payout_durability_payoutheadroom_63d_base_v117_signal,
    f35bpd_f35_bank_payout_durability_payoutheadroom_126d_base_v118_signal,
    f35bpd_f35_bank_payout_durability_payoutheadroom_252d_base_v119_signal,
    f35bpd_f35_bank_payout_durability_payoutheadroom_504d_base_v120_signal,
    f35bpd_f35_bank_payout_durability_payoutdurdiff_21d_base_v121_signal,
    f35bpd_f35_bank_payout_durability_payoutdurdiff_63d_base_v122_signal,
    f35bpd_f35_bank_payout_durability_payoutdurdiff_126d_base_v123_signal,
    f35bpd_f35_bank_payout_durability_payoutdurdiff_252d_base_v124_signal,
    f35bpd_f35_bank_payout_durability_payoutdurdiff_504d_base_v125_signal,
    f35bpd_f35_bank_payout_durability_payoutsustdiff_21d_base_v126_signal,
    f35bpd_f35_bank_payout_durability_payoutsustdiff_63d_base_v127_signal,
    f35bpd_f35_bank_payout_durability_payoutsustdiff_126d_base_v128_signal,
    f35bpd_f35_bank_payout_durability_payoutsustdiff_252d_base_v129_signal,
    f35bpd_f35_bank_payout_durability_payoutsustdiff_504d_base_v130_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_21d_base_v131_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_63d_base_v132_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_126d_base_v133_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_252d_base_v134_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_504d_base_v135_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorqrank_42d_base_v136_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_21d_base_v137_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_63d_base_v138_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_126d_base_v139_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_252d_base_v140_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_504d_base_v141_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdpsg_42d_base_v142_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_21d_base_v143_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_42d_base_v144_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_63d_base_v145_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_126d_base_v146_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_189d_base_v147_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_252d_base_v148_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_378d_base_v149_signal,
    f35bpd_f35_bank_payout_durability_payoutcomposite_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_BANK_PAYOUT_DURABILITY_REGISTRY_076_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_payout_floor", "_f35_payout_durability", "_f35_payout_sustainability",)
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
    print(f"OK f35_bank_payout_durability_base_076_150_claude: {n_features} features pass")
