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


def cg_f004_net_cash_position_netcash_lvl_mean_21d_base_v001_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_mean_63d_base_v002_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_mean_126d_base_v003_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_mean_252d_base_v004_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_mean_504d_base_v005_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_mean_21d_base_v006_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_mean_63d_base_v007_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_mean_126d_base_v008_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_mean_252d_base_v009_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_mean_504d_base_v010_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_mean_21d_base_v011_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_mean_63d_base_v012_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_mean_126d_base_v013_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_mean_252d_base_v014_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_mean_504d_base_v015_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_mean_21d_base_v016_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_mean_63d_base_v017_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_mean_126d_base_v018_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_mean_252d_base_v019_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_mean_504d_base_v020_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_mean_21d_base_v021_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_mean_63d_base_v022_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_mean_126d_base_v023_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_mean_252d_base_v024_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_mean_504d_base_v025_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_mean_21d_base_v026_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_mean_63d_base_v027_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_mean_126d_base_v028_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_mean_252d_base_v029_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_mean_504d_base_v030_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_mean_21d_base_v031_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_mean_63d_base_v032_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_mean_126d_base_v033_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_mean_252d_base_v034_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_mean_504d_base_v035_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_median_63d_base_v036_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_median_252d_base_v037_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_median_504d_base_v038_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_median_63d_base_v039_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_median_252d_base_v040_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_median_504d_base_v041_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_median_63d_base_v042_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_median_252d_base_v043_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_median_504d_base_v044_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_median_63d_base_v045_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_median_252d_base_v046_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_median_504d_base_v047_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_median_63d_base_v048_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_median_252d_base_v049_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_median_504d_base_v050_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_median_63d_base_v051_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_median_252d_base_v052_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_median_504d_base_v053_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_median_63d_base_v054_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_median_252d_base_v055_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_median_504d_base_v056_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_rmax_252d_base_v057_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_rmax_504d_base_v058_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_rmax_252d_base_v059_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_rmax_504d_base_v060_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_rmax_252d_base_v061_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_rmax_504d_base_v062_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_rmax_252d_base_v063_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_asset_rmax_504d_base_v064_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_rmax_252d_base_v065_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_equity_rmax_504d_base_v066_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_rmax_252d_base_v067_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_ev_rmax_504d_base_v068_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_rmax_252d_base_v069_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_to_rnd_rmax_504d_base_v070_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_rmin_252d_base_v071_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_lvl_rmin_504d_base_v072_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_rmin_252d_base_v073_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_mcap_rmin_504d_base_v074_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f004_net_cash_position_netcash_per_share_rmin_252d_base_v075_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

