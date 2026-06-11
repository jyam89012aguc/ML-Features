import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f005_current_ratio(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan).abs()


def _f005_qac(assetsc, inventory):
    return (assetsc - inventory.fillna(0))


def _f005_cash_quick(cashneq, investmentsc, liabilitiesc):
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / liabilitiesc.replace(0, np.nan).abs()


def cg_f005_current_liquidity_curratio_z_63d_base_v076_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_z_126d_base_v077_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_z_252d_base_v078_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_z_504d_base_v079_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_z_63d_base_v080_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_z_126d_base_v081_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_z_252d_base_v082_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_z_504d_base_v083_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_z_63d_base_v084_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_z_126d_base_v085_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_z_252d_base_v086_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_z_504d_base_v087_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_z_63d_base_v088_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_z_126d_base_v089_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_z_252d_base_v090_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_z_504d_base_v091_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_z_63d_base_v092_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_z_126d_base_v093_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_z_252d_base_v094_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_z_504d_base_v095_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_z_63d_base_v096_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_z_126d_base_v097_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_z_252d_base_v098_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_z_504d_base_v099_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_z_63d_base_v100_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_z_126d_base_v101_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_z_252d_base_v102_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_z_504d_base_v103_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_distmax_252d_base_v104_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_distmax_504d_base_v105_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_distmax_252d_base_v106_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_distmax_504d_base_v107_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_distmax_252d_base_v108_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_distmax_504d_base_v109_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_distmax_252d_base_v110_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_distmax_504d_base_v111_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_distmax_252d_base_v112_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_distmax_504d_base_v113_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_distmax_252d_base_v114_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_distmax_504d_base_v115_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_distmax_252d_base_v116_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_distmax_504d_base_v117_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_distmed_126d_base_v118_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_distmed_252d_base_v119_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_distmed_504d_base_v120_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_distmed_126d_base_v121_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_distmed_252d_base_v122_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_distmed_504d_base_v123_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_distmed_126d_base_v124_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_distmed_252d_base_v125_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_distmed_504d_base_v126_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_distmed_126d_base_v127_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_distmed_252d_base_v128_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_distmed_504d_base_v129_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_distmed_126d_base_v130_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_distmed_252d_base_v131_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_distmed_504d_base_v132_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_distmed_126d_base_v133_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_distmed_252d_base_v134_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_distmed_504d_base_v135_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_distmed_126d_base_v136_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_distmed_252d_base_v137_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_distmed_504d_base_v138_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_chg_63d_base_v139_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_chg_252d_base_v140_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_chg_63d_base_v141_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_chg_252d_base_v142_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_chg_63d_base_v143_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_chg_252d_base_v144_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_chg_63d_base_v145_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_chg_252d_base_v146_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_chg_63d_base_v147_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_chg_252d_base_v148_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_chg_63d_base_v149_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_chg_252d_base_v150_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

