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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f020_sga_to_rnd(sgna, rnd):
    return sgna / rnd.abs().replace(0, np.nan)


def _f020_sga_share(sgna, opex):
    return sgna / opex.abs().replace(0, np.nan)


def _f020_magic_number(revenue, sgna):
    # SaaS Magic Number proxy: 4 * (Q-over-Q revenue change) / prior-quarter S&M.
    # SG&A used as S&M proxy since Sharadar SF1 does not split.
    return 4 * revenue.diff(periods=63) / sgna.shift(63).abs().replace(0, np.nan)


# 21d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slope_21d_2d_v001_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slope_63d_2d_v002_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slope_126d_2d_v003_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slope_252d_2d_v004_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slope_504d_2d_v005_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slope_21d_2d_v006_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slope_63d_2d_v007_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slope_126d_2d_v008_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slope_252d_2d_v009_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slope_504d_2d_v010_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slope_21d_2d_v011_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slope_63d_2d_v012_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slope_126d_2d_v013_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slope_252d_2d_v014_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slope_504d_2d_v015_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slope_21d_2d_v016_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slope_63d_2d_v017_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slope_126d_2d_v018_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slope_252d_2d_v019_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slope_504d_2d_v020_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slope_21d_2d_v021_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slope_63d_2d_v022_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slope_126d_2d_v023_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slope_252d_2d_v024_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slope_504d_2d_v025_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slope_21d_2d_v026_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slope_63d_2d_v027_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slope_126d_2d_v028_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slope_252d_2d_v029_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slope_504d_2d_v030_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slope_21d_2d_v031_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slope_63d_2d_v032_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slope_126d_2d_v033_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slope_252d_2d_v034_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slope_504d_2d_v035_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slope_21d_2d_v036_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slope_63d_2d_v037_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slope_126d_2d_v038_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slope_252d_2d_v039_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slope_504d_2d_v040_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slope_21d_2d_v041_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slope_63d_2d_v042_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slope_126d_2d_v043_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slope_252d_2d_v044_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slope_504d_2d_v045_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slope_21d_2d_v046_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slope_63d_2d_v047_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slope_126d_2d_v048_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slope_252d_2d_v049_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slope_504d_2d_v050_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slope_21d_2d_v051_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slope_63d_2d_v052_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slope_126d_2d_v053_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slope_252d_2d_v054_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slope_504d_2d_v055_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slope_21d_2d_v056_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slope_63d_2d_v057_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slope_126d_2d_v058_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slope_252d_2d_v059_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slope_504d_2d_v060_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slope_21d_2d_v061_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slope_63d_2d_v062_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slope_126d_2d_v063_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slope_252d_2d_v064_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slope_504d_2d_v065_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slope_21d_2d_v066_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slope_63d_2d_v067_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slope_126d_2d_v068_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slope_252d_2d_v069_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slope_504d_2d_v070_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sm21_sl21_2d_v071_signal(sgna, rnd, closeadj):
    base = _mean(_f020_sga_to_rnd(sgna, rnd), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sm63_sl21_2d_v072_signal(sgna, rnd, closeadj):
    base = _mean(_f020_sga_to_rnd(sgna, rnd), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sm63_sl63_2d_v073_signal(sgna, rnd, closeadj):
    base = _mean(_f020_sga_to_rnd(sgna, rnd), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sm252_sl63_2d_v074_signal(sgna, rnd, closeadj):
    base = _mean(_f020_sga_to_rnd(sgna, rnd), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sm252_sl126_2d_v075_signal(sgna, rnd, closeadj):
    base = _mean(_f020_sga_to_rnd(sgna, rnd), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sm21_sl21_2d_v076_signal(sgna, opex, closeadj):
    base = _mean(_f020_sga_share(sgna, opex), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sm63_sl21_2d_v077_signal(sgna, opex, closeadj):
    base = _mean(_f020_sga_share(sgna, opex), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sm63_sl63_2d_v078_signal(sgna, opex, closeadj):
    base = _mean(_f020_sga_share(sgna, opex), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sm252_sl63_2d_v079_signal(sgna, opex, closeadj):
    base = _mean(_f020_sga_share(sgna, opex), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sm252_sl126_2d_v080_signal(sgna, opex, closeadj):
    base = _mean(_f020_sga_share(sgna, opex), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sm21_sl21_2d_v081_signal(rnd, opex, closeadj):
    base = _mean(rnd / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sm63_sl21_2d_v082_signal(rnd, opex, closeadj):
    base = _mean(rnd / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sm63_sl63_2d_v083_signal(rnd, opex, closeadj):
    base = _mean(rnd / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sm252_sl63_2d_v084_signal(rnd, opex, closeadj):
    base = _mean(rnd / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sm252_sl126_2d_v085_signal(rnd, opex, closeadj):
    base = _mean(rnd / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sm21_sl21_2d_v086_signal(sgna, revenue, closeadj):
    base = _mean(sgna / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sm63_sl21_2d_v087_signal(sgna, revenue, closeadj):
    base = _mean(sgna / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sm63_sl63_2d_v088_signal(sgna, revenue, closeadj):
    base = _mean(sgna / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sm252_sl63_2d_v089_signal(sgna, revenue, closeadj):
    base = _mean(sgna / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sm252_sl126_2d_v090_signal(sgna, revenue, closeadj):
    base = _mean(sgna / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sm21_sl21_2d_v091_signal(sgna, closeadj):
    base = _mean(sgna.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sm63_sl21_2d_v092_signal(sgna, closeadj):
    base = _mean(sgna.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sm63_sl63_2d_v093_signal(sgna, closeadj):
    base = _mean(sgna.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sm252_sl63_2d_v094_signal(sgna, closeadj):
    base = _mean(sgna.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sm252_sl126_2d_v095_signal(sgna, closeadj):
    base = _mean(sgna.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sm21_sl21_2d_v096_signal(rnd, sgna, opex, closeadj):
    base = _mean((rnd - sgna) / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sm63_sl21_2d_v097_signal(rnd, sgna, opex, closeadj):
    base = _mean((rnd - sgna) / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sm63_sl63_2d_v098_signal(rnd, sgna, opex, closeadj):
    base = _mean((rnd - sgna) / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sm252_sl63_2d_v099_signal(rnd, sgna, opex, closeadj):
    base = _mean((rnd - sgna) / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sm252_sl126_2d_v100_signal(rnd, sgna, opex, closeadj):
    base = _mean((rnd - sgna) / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_sm21_sl21_2d_v101_signal(rnd, sgna, closeadj):
    base = _mean((rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_sm63_sl21_2d_v102_signal(rnd, sgna, closeadj):
    base = _mean((rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_sm63_sl63_2d_v103_signal(rnd, sgna, closeadj):
    base = _mean((rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_sm252_sl63_2d_v104_signal(rnd, sgna, closeadj):
    base = _mean((rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_sm252_sl126_2d_v105_signal(rnd, sgna, closeadj):
    base = _mean((rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_sm21_sl21_2d_v106_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_sm63_sl21_2d_v107_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_sm63_sl63_2d_v108_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_sm252_sl63_2d_v109_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_sm252_sl126_2d_v110_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_sm21_sl21_2d_v111_signal(revenue, sgna, closeadj):
    base = _mean((_f020_magic_number(revenue, sgna) > 1.0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_sm63_sl21_2d_v112_signal(revenue, sgna, closeadj):
    base = _mean((_f020_magic_number(revenue, sgna) > 1.0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_sm63_sl63_2d_v113_signal(revenue, sgna, closeadj):
    base = _mean((_f020_magic_number(revenue, sgna) > 1.0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_sm252_sl63_2d_v114_signal(revenue, sgna, closeadj):
    base = _mean((_f020_magic_number(revenue, sgna) > 1.0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_sm252_sl126_2d_v115_signal(revenue, sgna, closeadj):
    base = _mean((_f020_magic_number(revenue, sgna) > 1.0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_sm21_sl21_2d_v116_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_sm63_sl21_2d_v117_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_sm63_sl63_2d_v118_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_sm252_sl63_2d_v119_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_sm252_sl126_2d_v120_signal(revenue, sgna, closeadj):
    base = _mean(_f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_sm21_sl21_2d_v121_signal(sgna, revenue, gp, closeadj):
    base = _mean(12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_sm63_sl21_2d_v122_signal(sgna, revenue, gp, closeadj):
    base = _mean(12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_sm63_sl63_2d_v123_signal(sgna, revenue, gp, closeadj):
    base = _mean(12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_sm252_sl63_2d_v124_signal(sgna, revenue, gp, closeadj):
    base = _mean(12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_sm252_sl126_2d_v125_signal(sgna, revenue, gp, closeadj):
    base = _mean(12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_sm21_sl21_2d_v126_signal(sgna, revenue, gp, closeadj):
    base = _mean(((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_sm63_sl21_2d_v127_signal(sgna, revenue, gp, closeadj):
    base = _mean(((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_sm63_sl63_2d_v128_signal(sgna, revenue, gp, closeadj):
    base = _mean(((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_sm252_sl63_2d_v129_signal(sgna, revenue, gp, closeadj):
    base = _mean(((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_sm252_sl126_2d_v130_signal(sgna, revenue, gp, closeadj):
    base = _mean(((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_sm21_sl21_2d_v131_signal(sgna, revenue, closeadj):
    base = _mean(sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_sm63_sl21_2d_v132_signal(sgna, revenue, closeadj):
    base = _mean(sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_sm63_sl63_2d_v133_signal(sgna, revenue, closeadj):
    base = _mean(sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_sm252_sl63_2d_v134_signal(sgna, revenue, closeadj):
    base = _mean(sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_sm252_sl126_2d_v135_signal(sgna, revenue, closeadj):
    base = _mean(sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_sm21_sl21_2d_v136_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_sm63_sl21_2d_v137_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_sm63_sl63_2d_v138_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_sm252_sl63_2d_v139_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_sm252_sl126_2d_v140_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_pctslope_21d_2d_v141_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_pctslope_63d_2d_v142_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_pctslope_252d_2d_v143_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_pctslope_21d_2d_v144_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_pctslope_63d_2d_v145_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_pctslope_252d_2d_v146_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_pctslope_21d_2d_v147_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_pctslope_63d_2d_v148_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_pctslope_252d_2d_v149_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_pctslope_21d_2d_v150_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_pctslope_63d_2d_v151_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_pctslope_252d_2d_v152_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_pctslope_21d_2d_v153_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_pctslope_63d_2d_v154_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_pctslope_252d_2d_v155_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_pctslope_21d_2d_v156_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_pctslope_63d_2d_v157_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_pctslope_252d_2d_v158_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_pctslope_21d_2d_v159_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_pctslope_63d_2d_v160_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_pctslope_252d_2d_v161_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_pctslope_21d_2d_v162_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_pctslope_63d_2d_v163_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_pctslope_252d_2d_v164_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_pctslope_21d_2d_v165_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_pctslope_63d_2d_v166_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_pctslope_252d_2d_v167_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_pctslope_21d_2d_v168_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_pctslope_63d_2d_v169_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_pctslope_252d_2d_v170_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_pctslope_21d_2d_v171_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_pctslope_63d_2d_v172_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_pctslope_252d_2d_v173_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_pctslope_21d_2d_v174_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_pctslope_63d_2d_v175_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_pctslope_252d_2d_v176_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_pctslope_21d_2d_v177_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_pctslope_63d_2d_v178_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_pctslope_252d_2d_v179_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_pctslope_21d_2d_v180_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_pctslope_63d_2d_v181_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_pctslope_252d_2d_v182_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sgnslope_21d_2d_v183_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sgnslope_63d_2d_v184_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_sgnslope_252d_2d_v185_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sgnslope_21d_2d_v186_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sgnslope_63d_2d_v187_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_sgnslope_252d_2d_v188_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sgnslope_21d_2d_v189_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sgnslope_63d_2d_v190_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_sgnslope_252d_2d_v191_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sgnslope_21d_2d_v192_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sgnslope_63d_2d_v193_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_sgnslope_252d_2d_v194_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sgnslope_21d_2d_v195_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sgnslope_63d_2d_v196_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_sgnslope_252d_2d_v197_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sgnslope_21d_2d_v198_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sgnslope_63d_2d_v199_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_sgnslope_252d_2d_v200_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

