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


def cg_f020_sga_rnd_mix_sga_to_rnd_z_63d_base_v076_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_z_126d_base_v077_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_z_252d_base_v078_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_z_504d_base_v079_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_z_63d_base_v080_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_z_126d_base_v081_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_z_252d_base_v082_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_z_504d_base_v083_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_z_63d_base_v084_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_z_126d_base_v085_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_z_252d_base_v086_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_z_504d_base_v087_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_z_63d_base_v088_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_z_126d_base_v089_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_z_252d_base_v090_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_z_504d_base_v091_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_z_63d_base_v092_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_z_126d_base_v093_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_z_252d_base_v094_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_z_504d_base_v095_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_z_63d_base_v096_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_z_126d_base_v097_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_z_252d_base_v098_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_z_504d_base_v099_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_z_63d_base_v100_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_z_126d_base_v101_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_z_252d_base_v102_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_z_504d_base_v103_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_z_63d_base_v104_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_z_126d_base_v105_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_z_252d_base_v106_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_z_504d_base_v107_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_z_63d_base_v108_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_z_126d_base_v109_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_z_252d_base_v110_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_z_504d_base_v111_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_z_63d_base_v112_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_z_126d_base_v113_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_z_252d_base_v114_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_z_504d_base_v115_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_z_63d_base_v116_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_z_126d_base_v117_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_z_252d_base_v118_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_z_504d_base_v119_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_z_63d_base_v120_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_z_126d_base_v121_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_z_252d_base_v122_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_z_504d_base_v123_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_z_63d_base_v124_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_z_126d_base_v125_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_z_252d_base_v126_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_z_504d_base_v127_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_z_63d_base_v128_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_z_126d_base_v129_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_z_252d_base_v130_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_z_504d_base_v131_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_distmax_252d_base_v132_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_distmax_504d_base_v133_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_distmax_252d_base_v134_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_distmax_504d_base_v135_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_distmax_252d_base_v136_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_distmax_504d_base_v137_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_distmax_252d_base_v138_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_distmax_504d_base_v139_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_distmax_252d_base_v140_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_distmax_504d_base_v141_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_distmax_252d_base_v142_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_distmax_504d_base_v143_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_distmax_252d_base_v144_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_opex_split_index_distmax_504d_base_v145_signal(rnd, sgna, closeadj):
    base = (rnd - sgna) / (rnd + sgna).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_distmax_252d_base_v146_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_distmax_504d_base_v147_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_distmax_252d_base_v148_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_above_1_distmax_504d_base_v149_signal(revenue, sgna, closeadj):
    base = (_f020_magic_number(revenue, sgna) > 1.0).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_distmax_252d_base_v150_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_magic_number_smoothed_252_distmax_504d_base_v151_signal(revenue, sgna, closeadj):
    base = _f020_magic_number(revenue, sgna).rolling(252, min_periods=63).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_distmax_252d_base_v152_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_months_distmax_504d_base_v153_signal(sgna, revenue, gp, closeadj):
    base = 12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_distmax_252d_base_v154_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_cac_payback_under_24m_distmax_504d_base_v155_signal(sgna, revenue, gp, closeadj):
    base = ((12 * sgna.shift(63) / (revenue.diff(periods=63) * (gp / revenue.replace(0, np.nan).abs())).replace(0, np.nan)) < 24).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_distmax_252d_base_v156_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_growth_lead_rev_distmax_504d_base_v157_signal(sgna, revenue, closeadj):
    base = sgna.pct_change(periods=63).shift(63) - revenue.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_distmax_252d_base_v158_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_growth_lead_rev_distmax_504d_base_v159_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252).shift(252) - revenue.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_distmed_126d_base_v160_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_distmed_252d_base_v161_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rnd_distmed_504d_base_v162_signal(sgna, rnd, closeadj):
    base = _f020_sga_to_rnd(sgna, rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_distmed_126d_base_v163_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_distmed_252d_base_v164_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_share_opex_distmed_504d_base_v165_signal(sgna, opex, closeadj):
    base = _f020_sga_share(sgna, opex)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_distmed_126d_base_v166_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_distmed_252d_base_v167_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_share_opex_distmed_504d_base_v168_signal(rnd, opex, closeadj):
    base = rnd / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_distmed_126d_base_v169_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_distmed_252d_base_v170_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_to_rev_distmed_504d_base_v171_signal(sgna, revenue, closeadj):
    base = sgna / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_distmed_126d_base_v172_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_distmed_252d_base_v173_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_sga_yoy_chg_distmed_504d_base_v174_signal(sgna, closeadj):
    base = sgna.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f020_sga_rnd_mix_rnd_minus_sga_share_distmed_126d_base_v175_signal(rnd, sgna, opex, closeadj):
    base = (rnd - sgna) / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

