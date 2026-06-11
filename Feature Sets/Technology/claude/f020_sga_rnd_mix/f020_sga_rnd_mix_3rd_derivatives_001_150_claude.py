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


# 21d acceleration of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accel_21d_3d_v001_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accel_63d_3d_v002_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accel_126d_3d_v003_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accel_252d_3d_v004_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accel_21d_3d_v005_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accel_63d_3d_v006_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accel_126d_3d_v007_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accel_252d_3d_v008_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accel_21d_3d_v009_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accel_63d_3d_v010_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accel_126d_3d_v011_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accel_252d_3d_v012_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accel_21d_3d_v013_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accel_63d_3d_v014_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accel_126d_3d_v015_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accel_252d_3d_v016_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accel_21d_3d_v017_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accel_63d_3d_v018_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accel_126d_3d_v019_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accel_252d_3d_v020_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accel_21d_3d_v021_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accel_63d_3d_v022_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accel_126d_3d_v023_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accel_252d_3d_v024_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accel_21d_3d_v025_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accel_63d_3d_v026_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accel_126d_3d_v027_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accel_252d_3d_v028_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accel_21d_3d_v029_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accel_63d_3d_v030_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accel_126d_3d_v031_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accel_252d_3d_v032_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accel_21d_3d_v033_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accel_63d_3d_v034_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accel_126d_3d_v035_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accel_252d_3d_v036_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_accel_21d_3d_v037_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_accel_63d_3d_v038_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_accel_126d_3d_v039_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_accel_252d_3d_v040_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_accel_21d_3d_v041_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_accel_63d_3d_v042_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_accel_126d_3d_v043_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_accel_252d_3d_v044_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_accel_21d_3d_v045_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_accel_63d_3d_v046_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_accel_126d_3d_v047_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_accel_252d_3d_v048_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_accel_21d_3d_v049_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_accel_63d_3d_v050_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_accel_126d_3d_v051_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_accel_252d_3d_v052_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_accel_21d_3d_v053_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_accel_63d_3d_v054_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_accel_126d_3d_v055_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_accel_252d_3d_v056_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slopez_21d_z126_3d_v057_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slopez_63d_z252_3d_v058_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slopez_126d_z252_3d_v059_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_slopez_252d_z504_3d_v060_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slopez_21d_z126_3d_v061_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slopez_63d_z252_3d_v062_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slopez_126d_z252_3d_v063_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_slopez_252d_z504_3d_v064_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slopez_21d_z126_3d_v065_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slopez_63d_z252_3d_v066_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slopez_126d_z252_3d_v067_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_slopez_252d_z504_3d_v068_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slopez_21d_z126_3d_v069_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slopez_63d_z252_3d_v070_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slopez_126d_z252_3d_v071_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_slopez_252d_z504_3d_v072_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slopez_21d_z126_3d_v073_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slopez_63d_z252_3d_v074_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slopez_126d_z252_3d_v075_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_slopez_252d_z504_3d_v076_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slopez_21d_z126_3d_v077_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slopez_63d_z252_3d_v078_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slopez_126d_z252_3d_v079_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_slopez_252d_z504_3d_v080_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slopez_21d_z126_3d_v081_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slopez_63d_z252_3d_v082_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slopez_126d_z252_3d_v083_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_slopez_252d_z504_3d_v084_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slopez_21d_z126_3d_v085_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slopez_63d_z252_3d_v086_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slopez_126d_z252_3d_v087_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_slopez_252d_z504_3d_v088_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slopez_21d_z126_3d_v089_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slopez_63d_z252_3d_v090_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slopez_126d_z252_3d_v091_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_slopez_252d_z504_3d_v092_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slopez_21d_z126_3d_v093_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slopez_63d_z252_3d_v094_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slopez_126d_z252_3d_v095_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_slopez_252d_z504_3d_v096_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slopez_21d_z126_3d_v097_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slopez_63d_z252_3d_v098_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slopez_126d_z252_3d_v099_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_slopez_252d_z504_3d_v100_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slopez_21d_z126_3d_v101_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slopez_63d_z252_3d_v102_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slopez_126d_z252_3d_v103_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_slopez_252d_z504_3d_v104_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slopez_21d_z126_3d_v105_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slopez_63d_z252_3d_v106_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slopez_126d_z252_3d_v107_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_slopez_252d_z504_3d_v108_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slopez_21d_z126_3d_v109_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slopez_63d_z252_3d_v110_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slopez_126d_z252_3d_v111_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_slopez_252d_z504_3d_v112_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_jerk_21d_3d_v113_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_jerk_63d_3d_v114_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_jerk_126d_3d_v115_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_jerk_21d_3d_v116_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_jerk_63d_3d_v117_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_jerk_126d_3d_v118_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_jerk_21d_3d_v119_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_jerk_63d_3d_v120_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_jerk_126d_3d_v121_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_jerk_21d_3d_v122_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_jerk_63d_3d_v123_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_jerk_126d_3d_v124_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_jerk_21d_3d_v125_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_jerk_63d_3d_v126_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_jerk_126d_3d_v127_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_jerk_21d_3d_v128_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_jerk_63d_3d_v129_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_jerk_126d_3d_v130_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_jerk_21d_3d_v131_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_jerk_63d_3d_v132_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_jerk_126d_3d_v133_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_jerk_21d_3d_v134_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_jerk_63d_3d_v135_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_jerk_126d_3d_v136_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_jerk_21d_3d_v137_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_jerk_63d_3d_v138_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_jerk_126d_3d_v139_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_jerk_21d_3d_v140_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_jerk_63d_3d_v141_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of magic_number_smoothed_252
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_jerk_126d_3d_v142_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_jerk_21d_3d_v143_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_jerk_63d_3d_v144_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cac_payback_months
def f020srm_f020_sga_rnd_mix_cac_payback_months_jerk_126d_3d_v145_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_jerk_21d_3d_v146_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_jerk_63d_3d_v147_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cac_payback_under_24m
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_jerk_126d_3d_v148_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_jerk_21d_3d_v149_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_jerk_63d_3d_v150_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sga_growth_lead_rev
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_jerk_126d_3d_v151_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_jerk_21d_3d_v152_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_jerk_63d_3d_v153_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_growth_lead_rev
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_jerk_126d_3d_v154_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sga_to_rnd smoothed over 252d
def f020srm_f020_sga_rnd_mix_sga_to_rnd_smoothaccel_63d_sm252_3d_v155_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sga_to_rnd smoothed over 504d
def f020srm_f020_sga_rnd_mix_sga_to_rnd_smoothaccel_252d_sm504_3d_v156_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sga_share_opex smoothed over 252d
def f020srm_f020_sga_rnd_mix_sga_share_opex_smoothaccel_63d_sm252_3d_v157_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sga_share_opex smoothed over 504d
def f020srm_f020_sga_rnd_mix_sga_share_opex_smoothaccel_252d_sm504_3d_v158_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_share_opex smoothed over 252d
def f020srm_f020_sga_rnd_mix_rnd_share_opex_smoothaccel_63d_sm252_3d_v159_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_share_opex smoothed over 504d
def f020srm_f020_sga_rnd_mix_rnd_share_opex_smoothaccel_252d_sm504_3d_v160_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sga_to_rev smoothed over 252d
def f020srm_f020_sga_rnd_mix_sga_to_rev_smoothaccel_63d_sm252_3d_v161_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sga_to_rev smoothed over 504d
def f020srm_f020_sga_rnd_mix_sga_to_rev_smoothaccel_252d_sm504_3d_v162_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sga_yoy_chg smoothed over 252d
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_smoothaccel_63d_sm252_3d_v163_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sga_yoy_chg smoothed over 504d
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_smoothaccel_252d_sm504_3d_v164_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_minus_sga_share smoothed over 252d
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_smoothaccel_63d_sm252_3d_v165_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_minus_sga_share smoothed over 504d
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_smoothaccel_252d_sm504_3d_v166_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opex_split_index smoothed over 252d
def f020srm_f020_sga_rnd_mix_opex_split_index_smoothaccel_63d_sm252_3d_v167_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opex_split_index smoothed over 504d
def f020srm_f020_sga_rnd_mix_opex_split_index_smoothaccel_252d_sm504_3d_v168_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of magic_number smoothed over 252d
def f020srm_f020_sga_rnd_mix_magic_number_smoothaccel_63d_sm252_3d_v169_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of magic_number smoothed over 504d
def f020srm_f020_sga_rnd_mix_magic_number_smoothaccel_252d_sm504_3d_v170_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of magic_number_above_1 smoothed over 252d
def f020srm_f020_sga_rnd_mix_magic_number_above_1_smoothaccel_63d_sm252_3d_v171_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of magic_number_above_1 smoothed over 504d
def f020srm_f020_sga_rnd_mix_magic_number_above_1_smoothaccel_252d_sm504_3d_v172_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of magic_number_smoothed_252 smoothed over 252d
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_smoothaccel_63d_sm252_3d_v173_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of magic_number_smoothed_252 smoothed over 504d
def f020srm_f020_sga_rnd_mix_magic_number_smoothed_252_smoothaccel_252d_sm504_3d_v174_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cac_payback_months smoothed over 252d
def f020srm_f020_sga_rnd_mix_cac_payback_months_smoothaccel_63d_sm252_3d_v175_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cac_payback_months smoothed over 504d
def f020srm_f020_sga_rnd_mix_cac_payback_months_smoothaccel_252d_sm504_3d_v176_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cac_payback_under_24m smoothed over 252d
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_smoothaccel_63d_sm252_3d_v177_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cac_payback_under_24m smoothed over 504d
def f020srm_f020_sga_rnd_mix_cac_payback_under_24m_smoothaccel_252d_sm504_3d_v178_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sga_growth_lead_rev smoothed over 252d
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_smoothaccel_63d_sm252_3d_v179_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sga_growth_lead_rev smoothed over 504d
def f020srm_f020_sga_rnd_mix_sga_growth_lead_rev_smoothaccel_252d_sm504_3d_v180_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_growth_lead_rev smoothed over 252d
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_smoothaccel_63d_sm252_3d_v181_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_growth_lead_rev smoothed over 504d
def f020srm_f020_sga_rnd_mix_rnd_growth_lead_rev_smoothaccel_252d_sm504_3d_v182_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accelz_21d_z252_3d_v183_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sga_to_rnd
def f020srm_f020_sga_rnd_mix_sga_to_rnd_accelz_63d_z504_3d_v184_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accelz_21d_z252_3d_v185_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sga_share_opex
def f020srm_f020_sga_rnd_mix_sga_share_opex_accelz_63d_z504_3d_v186_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accelz_21d_z252_3d_v187_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_share_opex
def f020srm_f020_sga_rnd_mix_rnd_share_opex_accelz_63d_z504_3d_v188_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accelz_21d_z252_3d_v189_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sga_to_rev
def f020srm_f020_sga_rnd_mix_sga_to_rev_accelz_63d_z504_3d_v190_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accelz_21d_z252_3d_v191_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sga_yoy_chg
def f020srm_f020_sga_rnd_mix_sga_yoy_chg_accelz_63d_z504_3d_v192_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accelz_21d_z252_3d_v193_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_minus_sga_share
def f020srm_f020_sga_rnd_mix_rnd_minus_sga_share_accelz_63d_z504_3d_v194_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accelz_21d_z252_3d_v195_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opex_split_index
def f020srm_f020_sga_rnd_mix_opex_split_index_accelz_63d_z504_3d_v196_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accelz_21d_z252_3d_v197_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of magic_number
def f020srm_f020_sga_rnd_mix_magic_number_accelz_63d_z504_3d_v198_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accelz_21d_z252_3d_v199_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of magic_number_above_1
def f020srm_f020_sga_rnd_mix_magic_number_above_1_accelz_63d_z504_3d_v200_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

