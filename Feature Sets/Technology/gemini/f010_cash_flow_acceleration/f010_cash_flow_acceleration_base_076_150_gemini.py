import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f010_ocf_change(ncfo, n):
    return ncfo.diff(periods=n)


def _f010_fcf_change(fcf, n):
    return fcf.diff(periods=n)


def _f010_cf_signflip(s):
    return (np.sign(s) != np.sign(s.shift(1))).astype(float)


def cg_f010_cash_flow_acceleration_ocf_qchg_z_63d_base_v076_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_z_126d_base_v077_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_z_252d_base_v078_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_z_504d_base_v079_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_z_63d_base_v080_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_z_126d_base_v081_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_z_252d_base_v082_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_z_504d_base_v083_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_z_63d_base_v084_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_z_126d_base_v085_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_z_252d_base_v086_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_z_504d_base_v087_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_z_63d_base_v088_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_z_126d_base_v089_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_z_252d_base_v090_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_z_504d_base_v091_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_z_63d_base_v092_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_z_126d_base_v093_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_z_252d_base_v094_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_z_504d_base_v095_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_z_63d_base_v096_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_z_126d_base_v097_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_z_252d_base_v098_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_z_504d_base_v099_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_z_63d_base_v100_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_z_126d_base_v101_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_z_252d_base_v102_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_z_504d_base_v103_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_z_63d_base_v104_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_z_126d_base_v105_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_z_252d_base_v106_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_z_504d_base_v107_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_distmax_252d_base_v108_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_distmax_504d_base_v109_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_distmax_252d_base_v110_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_distmax_504d_base_v111_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_distmax_252d_base_v112_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_distmax_504d_base_v113_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_distmax_252d_base_v114_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_distmax_504d_base_v115_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_distmax_252d_base_v116_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_distmax_504d_base_v117_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_distmax_252d_base_v118_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_distmax_504d_base_v119_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_distmax_252d_base_v120_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_distmax_504d_base_v121_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_distmax_252d_base_v122_signal(fcf, closeadj):
    base = np.sign(fcf)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_distmax_504d_base_v123_signal(fcf, closeadj):
    base = np.sign(fcf)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_distmed_126d_base_v124_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_distmed_252d_base_v125_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_distmed_504d_base_v126_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_distmed_126d_base_v127_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_distmed_252d_base_v128_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_distmed_504d_base_v129_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_distmed_126d_base_v130_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_distmed_252d_base_v131_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_qchg_distmed_504d_base_v132_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_distmed_126d_base_v133_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_distmed_252d_base_v134_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_ychg_distmed_504d_base_v135_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_distmed_126d_base_v136_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_distmed_252d_base_v137_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_to_pastlevel_distmed_504d_base_v138_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_distmed_126d_base_v139_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_distmed_252d_base_v140_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_to_pastlevel_distmed_504d_base_v141_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_distmed_126d_base_v142_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_distmed_252d_base_v143_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_sign_distmed_504d_base_v144_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_distmed_126d_base_v145_signal(fcf, closeadj):
    base = np.sign(fcf)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_distmed_252d_base_v146_signal(fcf, closeadj):
    base = np.sign(fcf)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_fcf_sign_distmed_504d_base_v147_signal(fcf, closeadj):
    base = np.sign(fcf)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_chg_63d_base_v148_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_qchg_chg_252d_base_v149_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f010_cash_flow_acceleration_ocf_ychg_chg_63d_base_v150_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

