import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f004_net_cash(cashneq, investmentsc, debt):
    return cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)


def _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return nc / marketcap.replace(0, np.nan).abs()


def _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return nc / sharesbas.replace(0, np.nan).abs()


def cg_f004_net_cash_position_netcash_lvl_z_63d_base_v076_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_z_126d_base_v077_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_z_252d_base_v078_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_z_504d_base_v079_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_z_63d_base_v080_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_z_126d_base_v081_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_z_252d_base_v082_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_z_504d_base_v083_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_z_63d_base_v084_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_z_126d_base_v085_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_z_252d_base_v086_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_z_504d_base_v087_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_z_63d_base_v088_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_z_126d_base_v089_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_z_252d_base_v090_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_z_504d_base_v091_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_z_63d_base_v092_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_z_126d_base_v093_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_z_252d_base_v094_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_z_504d_base_v095_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_z_63d_base_v096_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_z_126d_base_v097_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_z_252d_base_v098_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_z_504d_base_v099_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_z_63d_base_v100_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_z_126d_base_v101_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_z_252d_base_v102_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_z_504d_base_v103_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_distmax_252d_base_v104_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_distmax_504d_base_v105_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_distmax_252d_base_v106_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_distmax_504d_base_v107_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_distmax_252d_base_v108_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_distmax_504d_base_v109_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_distmax_252d_base_v110_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_distmax_504d_base_v111_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_distmax_252d_base_v112_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_distmax_504d_base_v113_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_distmax_252d_base_v114_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_distmax_504d_base_v115_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_distmax_252d_base_v116_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_distmax_504d_base_v117_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_distmed_126d_base_v118_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_distmed_252d_base_v119_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_distmed_504d_base_v120_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_distmed_126d_base_v121_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_distmed_252d_base_v122_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_distmed_504d_base_v123_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_distmed_126d_base_v124_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_distmed_252d_base_v125_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_distmed_504d_base_v126_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_distmed_126d_base_v127_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_distmed_252d_base_v128_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_distmed_504d_base_v129_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_distmed_126d_base_v130_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_distmed_252d_base_v131_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_distmed_504d_base_v132_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_distmed_126d_base_v133_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_distmed_252d_base_v134_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_distmed_504d_base_v135_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_distmed_126d_base_v136_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_distmed_252d_base_v137_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_distmed_504d_base_v138_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_chg_63d_base_v139_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_chg_252d_base_v140_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_chg_63d_base_v141_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_chg_252d_base_v142_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_chg_63d_base_v143_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_chg_252d_base_v144_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_chg_63d_base_v145_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_chg_252d_base_v146_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_chg_63d_base_v147_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_chg_252d_base_v148_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_chg_63d_base_v149_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_chg_252d_base_v150_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

