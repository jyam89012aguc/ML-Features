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
def _f31_revenue_cycle_phase(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (revenue - m) / sd.replace(0, np.nan)


def _f31_margin_cycle_pos(ebitdamargin, w):
    lo = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    hi = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).max()
    return (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)


def _f31_oem_cycle_score(revenue, ebitdamargin, w):
    rphase = _f31_revenue_cycle_phase(revenue, w)
    mpos = _f31_margin_cycle_pos(ebitdamargin, w)
    return rphase * mpos


# v076-v080: EMA-smoothed cycle phase
def f31aoc_f31_auto_oem_cycle_position_phase_ema_63d_base_v076_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_126d_base_v077_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126)
    result = base.ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_252d_base_v078_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_504d_base_v079_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_378d_base_v080_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378)
    result = base.ewm(span=89, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081-v085: EMA-smoothed margin pos
def f31aoc_f31_auto_oem_cycle_position_mpos_ema_63d_base_v081_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_126d_base_v082_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126)
    result = base.ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_252d_base_v083_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_504d_base_v084_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_378d_base_v085_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378)
    result = base.ewm(span=89, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086-v090: score × capex/revenue
def f31aoc_f31_auto_oem_cycle_position_score_x_capint_63d_base_v086_signal(revenue, ebitdamargin, capex, closeadj):
    capint = _safe_div(_mean(capex, 21), _mean(revenue, 21))
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_capint_126d_base_v087_signal(revenue, ebitdamargin, capex, closeadj):
    capint = _safe_div(_mean(capex, 63), _mean(revenue, 63))
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_capint_252d_base_v088_signal(revenue, ebitdamargin, capex, closeadj):
    capint = _safe_div(_mean(capex, 126), _mean(revenue, 126))
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_capint_504d_base_v089_signal(revenue, ebitdamargin, capex, closeadj):
    capint = _safe_div(_mean(capex, 252), _mean(revenue, 252))
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_capint_378d_base_v090_signal(revenue, ebitdamargin, capex, closeadj):
    capint = _safe_div(_mean(capex, 189), _mean(revenue, 189))
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v095: phase squared
def f31aoc_f31_auto_oem_cycle_position_phase_sq_63d_base_v091_signal(revenue, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 63)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_sq_126d_base_v092_signal(revenue, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 126)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_sq_252d_base_v093_signal(revenue, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 252)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_sq_504d_base_v094_signal(revenue, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 504)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_sq_378d_base_v095_signal(revenue, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 378)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096-v100: cycle score × ebitdamargin
def f31aoc_f31_auto_oem_cycle_position_score_x_margin_63d_base_v096_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_126d_base_v097_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_252d_base_v098_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_504d_base_v099_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_378d_base_v100_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101-v105: rev phase × log close
def f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_63d_base_v101_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_126d_base_v102_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_252d_base_v103_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_504d_base_v104_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_378d_base_v105_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v110: mpos × log close
def f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_63d_base_v106_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_126d_base_v107_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_252d_base_v108_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_504d_base_v109_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_378d_base_v110_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 378) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v111-v115: phase × revenue growth
def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_63d_base_v111_signal(revenue, closeadj):
    grow = revenue.pct_change(63)
    result = _f31_revenue_cycle_phase(revenue, 63) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_126d_base_v112_signal(revenue, closeadj):
    grow = revenue.pct_change(126)
    result = _f31_revenue_cycle_phase(revenue, 126) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_252d_base_v113_signal(revenue, closeadj):
    grow = revenue.pct_change(252)
    result = _f31_revenue_cycle_phase(revenue, 252) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_504d_base_v114_signal(revenue, closeadj):
    grow = revenue.pct_change(252)
    result = _f31_revenue_cycle_phase(revenue, 504) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_378d_base_v115_signal(revenue, closeadj):
    grow = revenue.pct_change(189)
    result = _f31_revenue_cycle_phase(revenue, 378) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116-v120: phase - mpos divergence
def f31aoc_f31_auto_oem_cycle_position_div_63d_base_v116_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 63)
    m = _f31_margin_cycle_pos(ebitdamargin, 63)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_126d_base_v117_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 126)
    m = _f31_margin_cycle_pos(ebitdamargin, 126)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_252d_base_v118_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 252)
    m = _f31_margin_cycle_pos(ebitdamargin, 252)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_504d_base_v119_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 504)
    m = _f31_margin_cycle_pos(ebitdamargin, 504)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_378d_base_v120_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 378)
    m = _f31_margin_cycle_pos(ebitdamargin, 378)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v125: mpos product across windows
def f31aoc_f31_auto_oem_cycle_position_mpos_xwin_63_252_base_v121_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_xwin_126_504_base_v122_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_xwin_63_252_base_v123_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * _f31_revenue_cycle_phase(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_xwin_126_504_base_v124_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * _f31_revenue_cycle_phase(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_xwin_63_252_base_v125_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126-v130: phase × capex z
def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_63d_base_v126_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * _z(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_126d_base_v127_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * _z(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_252d_base_v128_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * _z(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_504d_base_v129_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * _z(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_378d_base_v130_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * _z(capex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131-v135: cycle score smoothing combo (mean of base × close)
def f31aoc_f31_auto_oem_cycle_position_score_mean_63d_base_v131_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f31_oem_cycle_score(revenue, ebitdamargin, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_mean_126d_base_v132_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f31_oem_cycle_score(revenue, ebitdamargin, 126), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_mean_252d_base_v133_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f31_oem_cycle_score(revenue, ebitdamargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_mean_504d_base_v134_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f31_oem_cycle_score(revenue, ebitdamargin, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_mean_378d_base_v135_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f31_oem_cycle_score(revenue, ebitdamargin, 378), 89) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v140: cycle score std (volatility of cycle phase)
def f31aoc_f31_auto_oem_cycle_position_score_std_63d_base_v136_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f31_oem_cycle_score(revenue, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_std_126d_base_v137_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f31_oem_cycle_score(revenue, ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_std_252d_base_v138_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f31_oem_cycle_score(revenue, ebitdamargin, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_std_504d_base_v139_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f31_oem_cycle_score(revenue, ebitdamargin, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_std_378d_base_v140_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f31_oem_cycle_score(revenue, ebitdamargin, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141-v145: rev phase × capex/ppe (asset turnover analog)
def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_63d_base_v141_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * _safe_div(_mean(capex, 21), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_126d_base_v142_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * _safe_div(_mean(capex, 63), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_252d_base_v143_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * _safe_div(_mean(capex, 126), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_504d_base_v144_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * _safe_div(_mean(capex, 252), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_378d_base_v145_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * _safe_div(_mean(capex, 189), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


# v146-v150: mpos × revenue growth
def f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_63d_base_v146_signal(revenue, ebitdamargin, closeadj):
    grow = revenue.pct_change(63)
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_126d_base_v147_signal(revenue, ebitdamargin, closeadj):
    grow = revenue.pct_change(126)
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_252d_base_v148_signal(revenue, ebitdamargin, closeadj):
    grow = revenue.pct_change(252)
    result = _f31_margin_cycle_pos(ebitdamargin, 252) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_504d_base_v149_signal(revenue, ebitdamargin, closeadj):
    grow = revenue.pct_change(252)
    result = _f31_margin_cycle_pos(ebitdamargin, 504) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_378d_base_v150_signal(revenue, ebitdamargin, closeadj):
    grow = revenue.pct_change(189)
    result = _f31_margin_cycle_pos(ebitdamargin, 378) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31aoc_f31_auto_oem_cycle_position_phase_ema_63d_base_v076_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_126d_base_v077_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_252d_base_v078_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_504d_base_v079_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_378d_base_v080_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_63d_base_v081_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_126d_base_v082_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_252d_base_v083_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_504d_base_v084_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_378d_base_v085_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_capint_63d_base_v086_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_capint_126d_base_v087_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_capint_252d_base_v088_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_capint_504d_base_v089_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_capint_378d_base_v090_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_sq_63d_base_v091_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_sq_126d_base_v092_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_sq_252d_base_v093_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_sq_504d_base_v094_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_sq_378d_base_v095_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_63d_base_v096_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_126d_base_v097_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_252d_base_v098_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_504d_base_v099_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_378d_base_v100_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_63d_base_v101_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_126d_base_v102_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_252d_base_v103_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_504d_base_v104_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_logclose_378d_base_v105_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_63d_base_v106_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_126d_base_v107_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_252d_base_v108_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_504d_base_v109_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_logclose_378d_base_v110_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_63d_base_v111_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_126d_base_v112_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_252d_base_v113_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_504d_base_v114_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_378d_base_v115_signal,
    f31aoc_f31_auto_oem_cycle_position_div_63d_base_v116_signal,
    f31aoc_f31_auto_oem_cycle_position_div_126d_base_v117_signal,
    f31aoc_f31_auto_oem_cycle_position_div_252d_base_v118_signal,
    f31aoc_f31_auto_oem_cycle_position_div_504d_base_v119_signal,
    f31aoc_f31_auto_oem_cycle_position_div_378d_base_v120_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_xwin_63_252_base_v121_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_xwin_126_504_base_v122_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_xwin_63_252_base_v123_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_xwin_126_504_base_v124_signal,
    f31aoc_f31_auto_oem_cycle_position_score_xwin_63_252_base_v125_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_63d_base_v126_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_126d_base_v127_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_252d_base_v128_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_504d_base_v129_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_378d_base_v130_signal,
    f31aoc_f31_auto_oem_cycle_position_score_mean_63d_base_v131_signal,
    f31aoc_f31_auto_oem_cycle_position_score_mean_126d_base_v132_signal,
    f31aoc_f31_auto_oem_cycle_position_score_mean_252d_base_v133_signal,
    f31aoc_f31_auto_oem_cycle_position_score_mean_504d_base_v134_signal,
    f31aoc_f31_auto_oem_cycle_position_score_mean_378d_base_v135_signal,
    f31aoc_f31_auto_oem_cycle_position_score_std_63d_base_v136_signal,
    f31aoc_f31_auto_oem_cycle_position_score_std_126d_base_v137_signal,
    f31aoc_f31_auto_oem_cycle_position_score_std_252d_base_v138_signal,
    f31aoc_f31_auto_oem_cycle_position_score_std_504d_base_v139_signal,
    f31aoc_f31_auto_oem_cycle_position_score_std_378d_base_v140_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_63d_base_v141_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_126d_base_v142_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_252d_base_v143_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_504d_base_v144_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_per_close_378d_base_v145_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_63d_base_v146_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_126d_base_v147_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_252d_base_v148_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_504d_base_v149_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_revgrow_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_AUTO_OEM_CYCLE_POSITION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_revenue_cycle_phase", "_f31_margin_cycle_pos", "_f31_oem_cycle_score")
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
    print(f"OK f31_auto_oem_cycle_position_base_076_150_claude: {n_features} features pass")
