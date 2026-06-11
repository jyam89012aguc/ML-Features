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


# v001-v005: revenue cycle phase at different windows scaled by closeadj
def f31aoc_f31_auto_oem_cycle_position_revphase_63d_base_v001_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_revphase_126d_base_v002_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_revphase_252d_base_v003_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_revphase_504d_base_v004_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_revphase_378d_base_v005_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006-v010: margin cycle position scaled
def f31aoc_f31_auto_oem_cycle_position_mpos_63d_base_v006_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_base_v007_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_base_v008_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_base_v009_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_base_v010_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011-v015: composite OEM cycle score
def f31aoc_f31_auto_oem_cycle_position_score_63d_base_v011_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_base_v012_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_base_v013_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_base_v014_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_base_v015_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v020: revenue phase × capex (cycle * investment)
def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_base_v016_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * _mean(capex, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_base_v017_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * _mean(capex, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_base_v018_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * _mean(capex, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_base_v019_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * _mean(capex, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_378d_base_v020_signal(revenue, capex, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * _mean(capex, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021-v025: margin position × revenue level (revenue-weighted)
def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_base_v021_signal(revenue, ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * _mean(revenue, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_base_v022_signal(revenue, ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * _mean(revenue, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_base_v023_signal(revenue, ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 252) * _mean(revenue, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_base_v024_signal(revenue, ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 504) * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_378d_base_v025_signal(revenue, ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 378) * _mean(revenue, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026-v030: revenue cycle phase × ebitdamargin level
def f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_63d_base_v026_signal(revenue, ebitdamargin, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 63) * _mean(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_126d_base_v027_signal(revenue, ebitdamargin, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 126) * _mean(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_252d_base_v028_signal(revenue, ebitdamargin, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 252) * _mean(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_504d_base_v029_signal(revenue, ebitdamargin, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 504) * _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_378d_base_v030_signal(revenue, ebitdamargin, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 378) * _mean(ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v035: rev cycle phase z over secondary window
def f31aoc_f31_auto_oem_cycle_position_phase_z_63d_base_v031_signal(revenue, closeadj):
    result = _z(_f31_revenue_cycle_phase(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_z_126d_base_v032_signal(revenue, closeadj):
    result = _z(_f31_revenue_cycle_phase(revenue, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_z_252d_base_v033_signal(revenue, closeadj):
    result = _z(_f31_revenue_cycle_phase(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_z_504d_base_v034_signal(revenue, closeadj):
    result = _z(_f31_revenue_cycle_phase(revenue, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_z_378d_base_v035_signal(revenue, closeadj):
    result = _z(_f31_revenue_cycle_phase(revenue, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v040: margin cycle pos z
def f31aoc_f31_auto_oem_cycle_position_mpos_z_63d_base_v036_signal(ebitdamargin, closeadj):
    result = _z(_f31_margin_cycle_pos(ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_z_126d_base_v037_signal(ebitdamargin, closeadj):
    result = _z(_f31_margin_cycle_pos(ebitdamargin, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_z_252d_base_v038_signal(ebitdamargin, closeadj):
    result = _z(_f31_margin_cycle_pos(ebitdamargin, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_z_504d_base_v039_signal(ebitdamargin, closeadj):
    result = _z(_f31_margin_cycle_pos(ebitdamargin, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_z_378d_base_v040_signal(ebitdamargin, closeadj):
    result = _z(_f31_margin_cycle_pos(ebitdamargin, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v045: rolling std of revenue cycle phase
def f31aoc_f31_auto_oem_cycle_position_phase_std_63d_base_v041_signal(revenue, closeadj):
    result = _std(_f31_revenue_cycle_phase(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_std_126d_base_v042_signal(revenue, closeadj):
    result = _std(_f31_revenue_cycle_phase(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_std_252d_base_v043_signal(revenue, closeadj):
    result = _std(_f31_revenue_cycle_phase(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_std_504d_base_v044_signal(revenue, closeadj):
    result = _std(_f31_revenue_cycle_phase(revenue, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_std_378d_base_v045_signal(revenue, closeadj):
    result = _std(_f31_revenue_cycle_phase(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v050: rolling mean of margin cycle pos
def f31aoc_f31_auto_oem_cycle_position_mpos_mean_63d_base_v046_signal(ebitdamargin, closeadj):
    result = _mean(_f31_margin_cycle_pos(ebitdamargin, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_mean_126d_base_v047_signal(ebitdamargin, closeadj):
    result = _mean(_f31_margin_cycle_pos(ebitdamargin, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_mean_252d_base_v048_signal(ebitdamargin, closeadj):
    result = _mean(_f31_margin_cycle_pos(ebitdamargin, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_mean_504d_base_v049_signal(ebitdamargin, closeadj):
    result = _mean(_f31_margin_cycle_pos(ebitdamargin, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_mean_378d_base_v050_signal(ebitdamargin, closeadj):
    result = _mean(_f31_margin_cycle_pos(ebitdamargin, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v055: composite score × revenue
def f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_base_v051_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * _mean(revenue, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_base_v052_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * _mean(revenue, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_base_v053_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * _mean(revenue, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_base_v054_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_base_v055_signal(revenue, ebitdamargin, closeadj):
    result = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * _mean(revenue, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056-v060: revenue phase normalized by capex intensity
def f31aoc_f31_auto_oem_cycle_position_phase_per_capex_63d_base_v056_signal(revenue, capex, closeadj):
    capint = _safe_div(_mean(capex, 63), _mean(revenue, 63))
    result = _f31_revenue_cycle_phase(revenue, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_per_capex_126d_base_v057_signal(revenue, capex, closeadj):
    capint = _safe_div(_mean(capex, 126), _mean(revenue, 126))
    result = _f31_revenue_cycle_phase(revenue, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_per_capex_252d_base_v058_signal(revenue, capex, closeadj):
    capint = _safe_div(_mean(capex, 252), _mean(revenue, 252))
    result = _f31_revenue_cycle_phase(revenue, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_per_capex_504d_base_v059_signal(revenue, capex, closeadj):
    capint = _safe_div(_mean(capex, 504), _mean(revenue, 504))
    result = _f31_revenue_cycle_phase(revenue, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_per_capex_378d_base_v060_signal(revenue, capex, closeadj):
    capint = _safe_div(_mean(capex, 378), _mean(revenue, 378))
    result = _f31_revenue_cycle_phase(revenue, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v065: margin cycle pos × capex
def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_63d_base_v061_signal(ebitdamargin, capex, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 63) * _mean(capex, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_126d_base_v062_signal(ebitdamargin, capex, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 126) * _mean(capex, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_252d_base_v063_signal(ebitdamargin, capex, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 252) * _mean(capex, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_504d_base_v064_signal(ebitdamargin, capex, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 504) * _mean(capex, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_378d_base_v065_signal(ebitdamargin, capex, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 378) * _mean(capex, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v070: cycle score sign × magnitude expanded
def f31aoc_f31_auto_oem_cycle_position_score_signedmag_63d_base_v066_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 63)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signedmag_126d_base_v067_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 126)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signedmag_252d_base_v068_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 252)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signedmag_504d_base_v069_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 504)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signedmag_378d_base_v070_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 378)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071-v075: phase × close (price scaled cycle)
def f31aoc_f31_auto_oem_cycle_position_phase_x_close_21d_base_v071_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_close_42d_base_v072_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_close_189d_base_v073_signal(revenue, closeadj):
    result = _f31_revenue_cycle_phase(revenue, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_close_42d_base_v074_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_close_189d_base_v075_signal(ebitdamargin, closeadj):
    result = _f31_margin_cycle_pos(ebitdamargin, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31aoc_f31_auto_oem_cycle_position_revphase_63d_base_v001_signal,
    f31aoc_f31_auto_oem_cycle_position_revphase_126d_base_v002_signal,
    f31aoc_f31_auto_oem_cycle_position_revphase_252d_base_v003_signal,
    f31aoc_f31_auto_oem_cycle_position_revphase_504d_base_v004_signal,
    f31aoc_f31_auto_oem_cycle_position_revphase_378d_base_v005_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_base_v006_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_base_v007_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_base_v008_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_base_v009_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_base_v010_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_base_v011_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_base_v012_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_base_v013_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_base_v014_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_base_v015_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_base_v016_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_base_v017_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_base_v018_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_base_v019_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_378d_base_v020_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_base_v021_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_base_v022_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_base_v023_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_base_v024_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_378d_base_v025_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_63d_base_v026_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_126d_base_v027_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_252d_base_v028_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_504d_base_v029_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_marginlvl_378d_base_v030_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_z_63d_base_v031_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_z_126d_base_v032_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_z_252d_base_v033_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_z_504d_base_v034_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_z_378d_base_v035_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_z_63d_base_v036_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_z_126d_base_v037_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_z_252d_base_v038_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_z_504d_base_v039_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_z_378d_base_v040_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_std_63d_base_v041_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_std_126d_base_v042_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_std_252d_base_v043_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_std_504d_base_v044_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_std_378d_base_v045_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_mean_63d_base_v046_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_mean_126d_base_v047_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_mean_252d_base_v048_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_mean_504d_base_v049_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_mean_378d_base_v050_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_base_v051_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_base_v052_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_base_v053_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_base_v054_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_base_v055_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_per_capex_63d_base_v056_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_per_capex_126d_base_v057_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_per_capex_252d_base_v058_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_per_capex_504d_base_v059_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_per_capex_378d_base_v060_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_63d_base_v061_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_126d_base_v062_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_252d_base_v063_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_504d_base_v064_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_378d_base_v065_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signedmag_63d_base_v066_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signedmag_126d_base_v067_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signedmag_252d_base_v068_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signedmag_504d_base_v069_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signedmag_378d_base_v070_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_close_21d_base_v071_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_close_42d_base_v072_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_close_189d_base_v073_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_close_42d_base_v074_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_close_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_AUTO_OEM_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f31_auto_oem_cycle_position_base_001_075_claude: {n_features} features pass")
