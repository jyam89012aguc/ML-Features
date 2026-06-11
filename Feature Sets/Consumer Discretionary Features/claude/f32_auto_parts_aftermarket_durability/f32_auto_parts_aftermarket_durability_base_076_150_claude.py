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
def _f32_margin_floor(grossmargin, w):
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f32_margin_persistence(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f32_aftermarket_score(grossmargin, ebitdamargin, w):
    floor = _f32_margin_floor(grossmargin, w)
    persist = _f32_margin_persistence(ebitdamargin, w)
    return floor * persist


def f32apd_f32_auto_parts_aftermarket_durability_phase_ema_63d_base_v076_signal(grossmargin, closeadj):
    base = _f32_margin_floor(grossmargin, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_ema_126d_base_v077_signal(grossmargin, closeadj):
    base = _f32_margin_floor(grossmargin, 126)
    result = base.ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_ema_252d_base_v078_signal(grossmargin, closeadj):
    base = _f32_margin_floor(grossmargin, 252)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_ema_504d_base_v079_signal(grossmargin, closeadj):
    base = _f32_margin_floor(grossmargin, 504)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_ema_378d_base_v080_signal(grossmargin, closeadj):
    base = _f32_margin_floor(grossmargin, 378)
    result = base.ewm(span=89, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081-v085: EMA-smoothed margin pos
def f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_63d_base_v081_signal(ebitdamargin, closeadj):
    base = _f32_margin_persistence(ebitdamargin, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_126d_base_v082_signal(ebitdamargin, closeadj):
    base = _f32_margin_persistence(ebitdamargin, 126)
    result = base.ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_252d_base_v083_signal(ebitdamargin, closeadj):
    base = _f32_margin_persistence(ebitdamargin, 252)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_504d_base_v084_signal(ebitdamargin, closeadj):
    base = _f32_margin_persistence(ebitdamargin, 504)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_378d_base_v085_signal(ebitdamargin, closeadj):
    base = _f32_margin_persistence(ebitdamargin, 378)
    result = base.ewm(span=89, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086-v090: score × revenue/grossmargin
def f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_63d_base_v086_signal(grossmargin, ebitdamargin, revenue, closeadj):
    capint = _safe_div(_mean(revenue, 21), _mean(grossmargin, 21))
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_126d_base_v087_signal(grossmargin, ebitdamargin, revenue, closeadj):
    capint = _safe_div(_mean(revenue, 63), _mean(grossmargin, 63))
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_252d_base_v088_signal(grossmargin, ebitdamargin, revenue, closeadj):
    capint = _safe_div(_mean(revenue, 126), _mean(grossmargin, 126))
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_504d_base_v089_signal(grossmargin, ebitdamargin, revenue, closeadj):
    capint = _safe_div(_mean(revenue, 252), _mean(grossmargin, 252))
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_378d_base_v090_signal(grossmargin, ebitdamargin, revenue, closeadj):
    capint = _safe_div(_mean(revenue, 189), _mean(grossmargin, 189))
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v095: phase squared
def f32apd_f32_auto_parts_aftermarket_durability_phase_sq_63d_base_v091_signal(grossmargin, closeadj):
    p = _f32_margin_floor(grossmargin, 63)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_sq_126d_base_v092_signal(grossmargin, closeadj):
    p = _f32_margin_floor(grossmargin, 126)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_sq_252d_base_v093_signal(grossmargin, closeadj):
    p = _f32_margin_floor(grossmargin, 252)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_sq_504d_base_v094_signal(grossmargin, closeadj):
    p = _f32_margin_floor(grossmargin, 504)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_sq_378d_base_v095_signal(grossmargin, closeadj):
    p = _f32_margin_floor(grossmargin, 378)
    result = np.sign(p) * p * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096-v100: cycle score × ebitdamargin
def f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_63d_base_v096_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 63) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_126d_base_v097_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 126) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_252d_base_v098_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 252) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_504d_base_v099_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 504) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_378d_base_v100_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 378) * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101-v105: rev phase × log close
def f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_63d_base_v101_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_126d_base_v102_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_252d_base_v103_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_504d_base_v104_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_378d_base_v105_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 378) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v110: mpos × log close
def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_63d_base_v106_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_126d_base_v107_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_252d_base_v108_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_504d_base_v109_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_378d_base_v110_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 378) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v111-v115: phase × grossmargin growth
def f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_63d_base_v111_signal(grossmargin, closeadj):
    grow = grossmargin.pct_change(63)
    result = _f32_margin_floor(grossmargin, 63) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_126d_base_v112_signal(grossmargin, closeadj):
    grow = grossmargin.pct_change(126)
    result = _f32_margin_floor(grossmargin, 126) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_252d_base_v113_signal(grossmargin, closeadj):
    grow = grossmargin.pct_change(252)
    result = _f32_margin_floor(grossmargin, 252) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_504d_base_v114_signal(grossmargin, closeadj):
    grow = grossmargin.pct_change(252)
    result = _f32_margin_floor(grossmargin, 504) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_378d_base_v115_signal(grossmargin, closeadj):
    grow = grossmargin.pct_change(189)
    result = _f32_margin_floor(grossmargin, 378) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116-v120: phase - mpos divergence
def f32apd_f32_auto_parts_aftermarket_durability_div_63d_base_v116_signal(grossmargin, ebitdamargin, closeadj):
    p = _f32_margin_floor(grossmargin, 63)
    m = _f32_margin_persistence(ebitdamargin, 63)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_div_126d_base_v117_signal(grossmargin, ebitdamargin, closeadj):
    p = _f32_margin_floor(grossmargin, 126)
    m = _f32_margin_persistence(ebitdamargin, 126)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_div_252d_base_v118_signal(grossmargin, ebitdamargin, closeadj):
    p = _f32_margin_floor(grossmargin, 252)
    m = _f32_margin_persistence(ebitdamargin, 252)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_div_504d_base_v119_signal(grossmargin, ebitdamargin, closeadj):
    p = _f32_margin_floor(grossmargin, 504)
    m = _f32_margin_persistence(ebitdamargin, 504)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_div_378d_base_v120_signal(grossmargin, ebitdamargin, closeadj):
    p = _f32_margin_floor(grossmargin, 378)
    m = _f32_margin_persistence(ebitdamargin, 378)
    result = (p - 2.0 * m + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v125: mpos product across windows
def f32apd_f32_auto_parts_aftermarket_durability_mpos_xwin_63_252_base_v121_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 63) * _f32_margin_persistence(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_xwin_126_504_base_v122_signal(ebitdamargin, closeadj):
    result = _f32_margin_persistence(ebitdamargin, 126) * _f32_margin_persistence(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_xwin_63_252_base_v123_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 63) * _f32_margin_floor(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_xwin_126_504_base_v124_signal(grossmargin, closeadj):
    result = _f32_margin_floor(grossmargin, 126) * _f32_margin_floor(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_xwin_63_252_base_v125_signal(grossmargin, ebitdamargin, closeadj):
    result = _f32_aftermarket_score(grossmargin, ebitdamargin, 63) * _f32_aftermarket_score(grossmargin, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126-v130: phase × revenue z
def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_63d_base_v126_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 63) * _z(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_126d_base_v127_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 126) * _z(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_252d_base_v128_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 252) * _z(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_504d_base_v129_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 504) * _z(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_378d_base_v130_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 378) * _z(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131-v135: cycle score smoothing combo (mean of base × close)
def f32apd_f32_auto_parts_aftermarket_durability_score_mean_63d_base_v131_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f32_aftermarket_score(grossmargin, ebitdamargin, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_mean_126d_base_v132_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f32_aftermarket_score(grossmargin, ebitdamargin, 126), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_mean_252d_base_v133_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f32_aftermarket_score(grossmargin, ebitdamargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_mean_504d_base_v134_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f32_aftermarket_score(grossmargin, ebitdamargin, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_mean_378d_base_v135_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f32_aftermarket_score(grossmargin, ebitdamargin, 378), 89) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v140: cycle score std (volatility of cycle phase)
def f32apd_f32_auto_parts_aftermarket_durability_score_std_63d_base_v136_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f32_aftermarket_score(grossmargin, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_std_126d_base_v137_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f32_aftermarket_score(grossmargin, ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_std_252d_base_v138_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f32_aftermarket_score(grossmargin, ebitdamargin, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_std_504d_base_v139_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f32_aftermarket_score(grossmargin, ebitdamargin, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_score_std_378d_base_v140_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f32_aftermarket_score(grossmargin, ebitdamargin, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141-v145: rev phase × revenue/ppe (asset turnover analog)
def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_63d_base_v141_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 63) * _safe_div(_mean(revenue, 21), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_126d_base_v142_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 126) * _safe_div(_mean(revenue, 63), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_252d_base_v143_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 252) * _safe_div(_mean(revenue, 126), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_504d_base_v144_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 504) * _safe_div(_mean(revenue, 252), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_378d_base_v145_signal(grossmargin, revenue, closeadj):
    result = _f32_margin_floor(grossmargin, 378) * _safe_div(_mean(revenue, 189), closeadj * 1e6)
    return result.replace([np.inf, -np.inf], np.nan)


# v146-v150: mpos × grossmargin growth
def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_63d_base_v146_signal(grossmargin, ebitdamargin, closeadj):
    grow = grossmargin.pct_change(63)
    result = _f32_margin_persistence(ebitdamargin, 63) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_126d_base_v147_signal(grossmargin, ebitdamargin, closeadj):
    grow = grossmargin.pct_change(126)
    result = _f32_margin_persistence(ebitdamargin, 126) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_252d_base_v148_signal(grossmargin, ebitdamargin, closeadj):
    grow = grossmargin.pct_change(252)
    result = _f32_margin_persistence(ebitdamargin, 252) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_504d_base_v149_signal(grossmargin, ebitdamargin, closeadj):
    grow = grossmargin.pct_change(252)
    result = _f32_margin_persistence(ebitdamargin, 504) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_378d_base_v150_signal(grossmargin, ebitdamargin, closeadj):
    grow = grossmargin.pct_change(189)
    result = _f32_margin_persistence(ebitdamargin, 378) * grow * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32apd_f32_auto_parts_aftermarket_durability_phase_ema_63d_base_v076_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_ema_126d_base_v077_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_ema_252d_base_v078_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_ema_504d_base_v079_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_ema_378d_base_v080_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_63d_base_v081_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_126d_base_v082_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_252d_base_v083_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_504d_base_v084_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_ema_378d_base_v085_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_63d_base_v086_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_126d_base_v087_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_252d_base_v088_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_504d_base_v089_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_capint_378d_base_v090_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_sq_63d_base_v091_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_sq_126d_base_v092_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_sq_252d_base_v093_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_sq_504d_base_v094_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_sq_378d_base_v095_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_63d_base_v096_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_126d_base_v097_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_252d_base_v098_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_504d_base_v099_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_x_margin_378d_base_v100_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_63d_base_v101_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_126d_base_v102_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_252d_base_v103_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_504d_base_v104_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_logclose_378d_base_v105_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_63d_base_v106_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_126d_base_v107_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_252d_base_v108_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_504d_base_v109_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_logclose_378d_base_v110_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_63d_base_v111_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_126d_base_v112_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_252d_base_v113_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_504d_base_v114_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_revgrow_378d_base_v115_signal,
    f32apd_f32_auto_parts_aftermarket_durability_div_63d_base_v116_signal,
    f32apd_f32_auto_parts_aftermarket_durability_div_126d_base_v117_signal,
    f32apd_f32_auto_parts_aftermarket_durability_div_252d_base_v118_signal,
    f32apd_f32_auto_parts_aftermarket_durability_div_504d_base_v119_signal,
    f32apd_f32_auto_parts_aftermarket_durability_div_378d_base_v120_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_xwin_63_252_base_v121_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_xwin_126_504_base_v122_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_xwin_63_252_base_v123_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_xwin_126_504_base_v124_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_xwin_63_252_base_v125_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_63d_base_v126_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_126d_base_v127_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_252d_base_v128_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_504d_base_v129_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capexz_378d_base_v130_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_mean_63d_base_v131_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_mean_126d_base_v132_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_mean_252d_base_v133_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_mean_504d_base_v134_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_mean_378d_base_v135_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_std_63d_base_v136_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_std_126d_base_v137_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_std_252d_base_v138_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_std_504d_base_v139_signal,
    f32apd_f32_auto_parts_aftermarket_durability_score_std_378d_base_v140_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_63d_base_v141_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_126d_base_v142_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_252d_base_v143_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_504d_base_v144_signal,
    f32apd_f32_auto_parts_aftermarket_durability_phase_x_capex_per_close_378d_base_v145_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_63d_base_v146_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_126d_base_v147_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_252d_base_v148_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_504d_base_v149_signal,
    f32apd_f32_auto_parts_aftermarket_durability_mpos_x_revgrow_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_AUTO_PARTS_AFTERMARKET_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "revenue": revenue}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_margin_floor", "_f32_margin_persistence", "_f32_aftermarket_score")
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
    print(f"OK f32_auto_parts_aftermarket_durability_base_076_150_claude: {n_features} features pass")
