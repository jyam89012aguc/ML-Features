import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f020_sga_to_rnd(sgna, rnd):
    return sgna / rnd.abs().replace(0, np.nan)


def _f020_sga_share(sgna, opex):
    return sgna / opex.abs().replace(0, np.nan)


def _f020_magic_number(revenue, sgna):
    # SaaS Magic Number proxy: 4 * (Q-over-Q revenue change) / prior-quarter S&M.
    # SG&A used as S&M proxy since Sharadar SF1 does not split.
    return 4 * revenue.diff(periods=63) / sgna.shift(63).abs().replace(0, np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_mean_21d_base_v001_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_mean_63d_base_v002_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_mean_126d_base_v003_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_mean_252d_base_v004_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_mean_504d_base_v005_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_mean_21d_base_v006_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_mean_63d_base_v007_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_mean_126d_base_v008_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_mean_252d_base_v009_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_mean_504d_base_v010_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_mean_21d_base_v011_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_mean_63d_base_v012_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_mean_126d_base_v013_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_mean_252d_base_v014_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_mean_504d_base_v015_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_mean_21d_base_v016_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_mean_63d_base_v017_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_mean_126d_base_v018_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_mean_252d_base_v019_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_mean_504d_base_v020_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_mean_21d_base_v021_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_mean_63d_base_v022_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_mean_126d_base_v023_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_mean_252d_base_v024_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_mean_504d_base_v025_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_mean_21d_base_v026_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_mean_63d_base_v027_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_mean_126d_base_v028_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_mean_252d_base_v029_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_mean_504d_base_v030_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_mean_21d_base_v031_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_mean_63d_base_v032_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_mean_126d_base_v033_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_mean_252d_base_v034_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_mean_504d_base_v035_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_mean_21d_base_v036_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_mean_63d_base_v037_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_mean_126d_base_v038_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_mean_252d_base_v039_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_mean_504d_base_v040_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_mean_21d_base_v041_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_mean_63d_base_v042_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_mean_126d_base_v043_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_mean_252d_base_v044_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_mean_504d_base_v045_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_mean_21d_base_v046_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_mean_63d_base_v047_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_mean_126d_base_v048_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_mean_252d_base_v049_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_mean_504d_base_v050_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_mean_21d_base_v051_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_mean_63d_base_v052_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_mean_126d_base_v053_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_mean_252d_base_v054_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_mean_504d_base_v055_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_mean_21d_base_v056_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_mean_63d_base_v057_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_mean_126d_base_v058_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_mean_252d_base_v059_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_mean_504d_base_v060_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_mean_21d_base_v061_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_mean_63d_base_v062_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_mean_126d_base_v063_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_mean_252d_base_v064_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_mean_504d_base_v065_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_mean_21d_base_v066_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_mean_63d_base_v067_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_mean_126d_base_v068_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_mean_252d_base_v069_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_mean_504d_base_v070_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_median_63d_base_v071_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_median_252d_base_v072_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_median_504d_base_v073_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_median_63d_base_v074_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_median_252d_base_v075_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_median_504d_base_v076_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_median_63d_base_v077_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_median_252d_base_v078_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_median_504d_base_v079_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_median_63d_base_v080_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_median_252d_base_v081_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_median_504d_base_v082_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_median_63d_base_v083_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_median_252d_base_v084_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_median_504d_base_v085_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_median_63d_base_v086_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_median_252d_base_v087_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_median_504d_base_v088_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_median_63d_base_v089_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_median_252d_base_v090_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_median_504d_base_v091_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_median_63d_base_v092_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_median_252d_base_v093_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_median_504d_base_v094_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_median_63d_base_v095_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_median_252d_base_v096_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_median_504d_base_v097_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_median_63d_base_v098_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_median_252d_base_v099_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_median_504d_base_v100_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

