import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f017_qchg(rnd):
    return rnd.diff(periods=63)


def _f017_ychg(rnd):
    return rnd.diff(periods=252)


def cg_f017_rnd_growth_rnd_qchg_z_63d_base_v076_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_z_126d_base_v077_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_z_252d_base_v078_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_z_504d_base_v079_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_z_63d_base_v080_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_z_126d_base_v081_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_z_252d_base_v082_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_z_504d_base_v083_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_z_63d_base_v084_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_z_126d_base_v085_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_z_252d_base_v086_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_z_504d_base_v087_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_z_63d_base_v088_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_z_126d_base_v089_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_z_252d_base_v090_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_z_504d_base_v091_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_z_63d_base_v092_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_z_126d_base_v093_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_z_252d_base_v094_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_z_504d_base_v095_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_z_63d_base_v096_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_z_126d_base_v097_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_z_252d_base_v098_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_z_504d_base_v099_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_z_63d_base_v100_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_z_126d_base_v101_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_z_252d_base_v102_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_z_504d_base_v103_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_distmax_252d_base_v104_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_distmax_504d_base_v105_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_distmax_252d_base_v106_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_distmax_504d_base_v107_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_distmax_252d_base_v108_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_distmax_504d_base_v109_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_distmax_252d_base_v110_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_distmax_504d_base_v111_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_distmax_252d_base_v112_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_distmax_504d_base_v113_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_distmax_252d_base_v114_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_distmax_504d_base_v115_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_distmax_252d_base_v116_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_distmax_504d_base_v117_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_distmed_126d_base_v118_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_distmed_252d_base_v119_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_distmed_504d_base_v120_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_distmed_126d_base_v121_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_distmed_252d_base_v122_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_distmed_504d_base_v123_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_distmed_126d_base_v124_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_distmed_252d_base_v125_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_distmed_504d_base_v126_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_distmed_126d_base_v127_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_distmed_252d_base_v128_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_distmed_504d_base_v129_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_distmed_126d_base_v130_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_distmed_252d_base_v131_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_distmed_504d_base_v132_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_distmed_126d_base_v133_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_distmed_252d_base_v134_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_distmed_504d_base_v135_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_distmed_126d_base_v136_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_distmed_252d_base_v137_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_log_growth_distmed_504d_base_v138_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_chg_63d_base_v139_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_qchg_chg_252d_base_v140_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_chg_63d_base_v141_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_ychg_chg_252d_base_v142_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_chg_63d_base_v143_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_q_chg_252d_base_v144_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_chg_63d_base_v145_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_pct_y_chg_252d_base_v146_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_chg_63d_base_v147_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_growth_to_rev_growth_chg_252d_base_v148_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_chg_63d_base_v149_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f017_rnd_growth_rnd_to_prior_chg_252d_base_v150_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

