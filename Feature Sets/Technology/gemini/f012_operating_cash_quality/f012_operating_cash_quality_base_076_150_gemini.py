import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f012_ocf_ni_gap(ncfo, netinc):
    return ncfo - netinc.fillna(0)


def _f012_ocf_to_ni(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan).abs()


def _f012_noncash_share(depamor, sbcomp, opex):
    nc = depamor.fillna(0) + sbcomp.fillna(0)
    return nc / opex.abs().replace(0, np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_z_63d_base_v076_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_z_126d_base_v077_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_z_252d_base_v078_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_z_504d_base_v079_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_z_63d_base_v080_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_z_126d_base_v081_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_z_252d_base_v082_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_z_504d_base_v083_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_z_63d_base_v084_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_z_126d_base_v085_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_z_252d_base_v086_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_z_504d_base_v087_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_z_63d_base_v088_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_z_126d_base_v089_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_z_252d_base_v090_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_z_504d_base_v091_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_z_63d_base_v092_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_z_126d_base_v093_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_z_252d_base_v094_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_z_504d_base_v095_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_z_63d_base_v096_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_z_126d_base_v097_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_z_252d_base_v098_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_z_504d_base_v099_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_z_63d_base_v100_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_z_126d_base_v101_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_z_252d_base_v102_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_z_504d_base_v103_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_distmax_252d_base_v104_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_distmax_504d_base_v105_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_distmax_252d_base_v106_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_distmax_504d_base_v107_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_distmax_252d_base_v108_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_distmax_504d_base_v109_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_distmax_252d_base_v110_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_distmax_504d_base_v111_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_distmax_252d_base_v112_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_distmax_504d_base_v113_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_distmax_252d_base_v114_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_distmax_504d_base_v115_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_distmax_252d_base_v116_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_distmax_504d_base_v117_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_distmed_126d_base_v118_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_distmed_252d_base_v119_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_distmed_504d_base_v120_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_distmed_126d_base_v121_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_distmed_252d_base_v122_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_distmed_504d_base_v123_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_distmed_126d_base_v124_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_distmed_252d_base_v125_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_distmed_504d_base_v126_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_distmed_126d_base_v127_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_distmed_252d_base_v128_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_distmed_504d_base_v129_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_distmed_126d_base_v130_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_distmed_252d_base_v131_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_distmed_504d_base_v132_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_distmed_126d_base_v133_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_distmed_252d_base_v134_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_distmed_504d_base_v135_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_distmed_126d_base_v136_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_distmed_252d_base_v137_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_distmed_504d_base_v138_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_chg_63d_base_v139_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_chg_252d_base_v140_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_chg_63d_base_v141_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_chg_252d_base_v142_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_chg_63d_base_v143_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_chg_252d_base_v144_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_chg_63d_base_v145_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_chg_252d_base_v146_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_chg_63d_base_v147_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_chg_252d_base_v148_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_chg_63d_base_v149_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_chg_252d_base_v150_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

