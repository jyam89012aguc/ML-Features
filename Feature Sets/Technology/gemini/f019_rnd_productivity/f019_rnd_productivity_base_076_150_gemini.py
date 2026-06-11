import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f019_rev_per_rnd(revenue, rnd):
    return revenue / rnd.abs().replace(0, np.nan)


def _f019_gp_per_rnd(gp, rnd):
    return gp / rnd.abs().replace(0, np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_z_63d_base_v076_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_z_126d_base_v077_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_z_252d_base_v078_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_z_504d_base_v079_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_z_63d_base_v080_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_z_126d_base_v081_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_z_252d_base_v082_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_z_504d_base_v083_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_z_63d_base_v084_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_z_126d_base_v085_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_z_252d_base_v086_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_z_504d_base_v087_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_z_63d_base_v088_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_z_126d_base_v089_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_z_252d_base_v090_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_z_504d_base_v091_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_z_63d_base_v092_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_z_126d_base_v093_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_z_252d_base_v094_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_z_504d_base_v095_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_z_63d_base_v096_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_z_126d_base_v097_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_z_252d_base_v098_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_z_504d_base_v099_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_z_63d_base_v100_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_z_126d_base_v101_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_z_252d_base_v102_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_z_504d_base_v103_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_distmax_252d_base_v104_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_distmax_504d_base_v105_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_distmax_252d_base_v106_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_distmax_504d_base_v107_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_distmax_252d_base_v108_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_distmax_504d_base_v109_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_distmax_252d_base_v110_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_distmax_504d_base_v111_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_distmax_252d_base_v112_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_distmax_504d_base_v113_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_distmax_252d_base_v114_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_distmax_504d_base_v115_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_distmax_252d_base_v116_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_distmax_504d_base_v117_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_distmed_126d_base_v118_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_distmed_252d_base_v119_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_distmed_504d_base_v120_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_distmed_126d_base_v121_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_distmed_252d_base_v122_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_distmed_504d_base_v123_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_distmed_126d_base_v124_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_distmed_252d_base_v125_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_distmed_504d_base_v126_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_distmed_126d_base_v127_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_distmed_252d_base_v128_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_distmed_504d_base_v129_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_distmed_126d_base_v130_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_distmed_252d_base_v131_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_distmed_504d_base_v132_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_distmed_126d_base_v133_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_distmed_252d_base_v134_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_distmed_504d_base_v135_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_distmed_126d_base_v136_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_distmed_252d_base_v137_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_distmed_504d_base_v138_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_chg_63d_base_v139_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_chg_252d_base_v140_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_chg_63d_base_v141_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_chg_252d_base_v142_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_chg_63d_base_v143_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_chg_252d_base_v144_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_chg_63d_base_v145_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_chg_252d_base_v146_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_chg_63d_base_v147_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_chg_252d_base_v148_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_chg_63d_base_v149_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_chg_252d_base_v150_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

