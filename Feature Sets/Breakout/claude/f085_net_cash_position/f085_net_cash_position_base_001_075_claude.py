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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f085_net_cash(cashneq, debt):
    return cashneq - debt


def _f085_net_cash_ratio(cashneq, debt, marketcap):
    nc = cashneq - debt
    return nc / marketcap.abs().replace(0, np.nan)


def _f085_bs_strength(cashneq, debt, equity, w):
    raw = (cashneq - debt) / equity.abs().replace(0, np.nan)
    return raw.rolling(w, min_periods=max(1, w // 2)).mean()


def f085ncp_f085_net_cash_position_nc_21d_xclose_base_v001_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_21d_xemac_base_v002_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_21d_xmean_base_v003_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_21d_xclose2_base_v004_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_21d_xmlong_base_v005_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_63d_xclose_base_v006_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_63d_xemac_base_v007_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_63d_xmean_base_v008_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_63d_xclose2_base_v009_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_63d_xmlong_base_v010_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_252d_xclose_base_v011_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_252d_xemac_base_v012_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_252d_xmean_base_v013_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_252d_xclose2_base_v014_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nc_252d_xmlong_base_v015_signal(cashneq, debt, closeadj):
    base = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_21d_xclose_base_v016_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 21) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_21d_xemac_base_v017_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 21) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_21d_xmean_base_v018_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 21) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_21d_xclose2_base_v019_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 21) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_21d_xmlong_base_v020_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 21) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_63d_xclose_base_v021_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 63) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_63d_xemac_base_v022_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 63) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_63d_xmean_base_v023_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 63) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_63d_xclose2_base_v024_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 63) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_63d_xmlong_base_v025_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 63) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_252d_xclose_base_v026_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 252) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_252d_xemac_base_v027_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 252) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_252d_xmean_base_v028_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 252) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_252d_xclose2_base_v029_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 252) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncm_252d_xmlong_base_v030_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt)
    base = _mean(nc, 252) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_21d_xclose_base_v031_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _z(nc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_21d_xemac_base_v032_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _z(nc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_21d_xmean_base_v033_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _z(nc, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_21d_xclose2_base_v034_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _z(nc, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_21d_xmlong_base_v035_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _z(nc, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_63d_xclose_base_v036_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _z(nc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_63d_xemac_base_v037_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _z(nc, 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_63d_xmean_base_v038_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _z(nc, 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_63d_xclose2_base_v039_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _z(nc, 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_63d_xmlong_base_v040_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _z(nc, 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_252d_xclose_base_v041_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _z(nc, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_252d_xemac_base_v042_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _z(nc, 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_252d_xmean_base_v043_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _z(nc, 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_252d_xclose2_base_v044_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _z(nc, 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncz_252d_xmlong_base_v045_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _z(nc, 504)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_21d_xclose_base_v046_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _ema(nc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_21d_xemac_base_v047_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _ema(nc, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_21d_xmean_base_v048_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _ema(nc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_21d_xclose2_base_v049_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _ema(nc, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_21d_xmlong_base_v050_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(21, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = _ema(nc, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_63d_xclose_base_v051_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _ema(nc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_63d_xemac_base_v052_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _ema(nc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_63d_xmean_base_v053_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _ema(nc, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_63d_xclose2_base_v054_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _ema(nc, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_63d_xmlong_base_v055_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(63, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = _ema(nc, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_252d_xclose_base_v056_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _ema(nc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_252d_xemac_base_v057_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _ema(nc, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_252d_xmean_base_v058_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _ema(nc, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_252d_xclose2_base_v059_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _ema(nc, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_nce_252d_xmlong_base_v060_signal(cashneq, debt, closeadj):
    nc = _f085_net_cash(cashneq, debt) / cashneq.rolling(252, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = _ema(nc, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_21d_xclose_base_v061_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_21d_xemac_base_v062_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_21d_xmean_base_v063_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_21d_xclose2_base_v064_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_21d_xmlong_base_v065_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_63d_xclose_base_v066_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_63d_xemac_base_v067_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_63d_xmean_base_v068_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_63d_xclose2_base_v069_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_63d_xmlong_base_v070_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_252d_xclose_base_v071_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_252d_xemac_base_v072_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_252d_xmean_base_v073_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_252d_xclose2_base_v074_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f085ncp_f085_net_cash_position_ncr_252d_xmlong_base_v075_signal(cashneq, debt, marketcap, closeadj):
    base = _f085_net_cash_ratio(cashneq, debt, marketcap)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f085ncp_f085_net_cash_position_nc_21d_xclose_base_v001_signal,
    f085ncp_f085_net_cash_position_nc_21d_xemac_base_v002_signal,
    f085ncp_f085_net_cash_position_nc_21d_xmean_base_v003_signal,
    f085ncp_f085_net_cash_position_nc_21d_xclose2_base_v004_signal,
    f085ncp_f085_net_cash_position_nc_21d_xmlong_base_v005_signal,
    f085ncp_f085_net_cash_position_nc_63d_xclose_base_v006_signal,
    f085ncp_f085_net_cash_position_nc_63d_xemac_base_v007_signal,
    f085ncp_f085_net_cash_position_nc_63d_xmean_base_v008_signal,
    f085ncp_f085_net_cash_position_nc_63d_xclose2_base_v009_signal,
    f085ncp_f085_net_cash_position_nc_63d_xmlong_base_v010_signal,
    f085ncp_f085_net_cash_position_nc_252d_xclose_base_v011_signal,
    f085ncp_f085_net_cash_position_nc_252d_xemac_base_v012_signal,
    f085ncp_f085_net_cash_position_nc_252d_xmean_base_v013_signal,
    f085ncp_f085_net_cash_position_nc_252d_xclose2_base_v014_signal,
    f085ncp_f085_net_cash_position_nc_252d_xmlong_base_v015_signal,
    f085ncp_f085_net_cash_position_ncm_21d_xclose_base_v016_signal,
    f085ncp_f085_net_cash_position_ncm_21d_xemac_base_v017_signal,
    f085ncp_f085_net_cash_position_ncm_21d_xmean_base_v018_signal,
    f085ncp_f085_net_cash_position_ncm_21d_xclose2_base_v019_signal,
    f085ncp_f085_net_cash_position_ncm_21d_xmlong_base_v020_signal,
    f085ncp_f085_net_cash_position_ncm_63d_xclose_base_v021_signal,
    f085ncp_f085_net_cash_position_ncm_63d_xemac_base_v022_signal,
    f085ncp_f085_net_cash_position_ncm_63d_xmean_base_v023_signal,
    f085ncp_f085_net_cash_position_ncm_63d_xclose2_base_v024_signal,
    f085ncp_f085_net_cash_position_ncm_63d_xmlong_base_v025_signal,
    f085ncp_f085_net_cash_position_ncm_252d_xclose_base_v026_signal,
    f085ncp_f085_net_cash_position_ncm_252d_xemac_base_v027_signal,
    f085ncp_f085_net_cash_position_ncm_252d_xmean_base_v028_signal,
    f085ncp_f085_net_cash_position_ncm_252d_xclose2_base_v029_signal,
    f085ncp_f085_net_cash_position_ncm_252d_xmlong_base_v030_signal,
    f085ncp_f085_net_cash_position_ncz_21d_xclose_base_v031_signal,
    f085ncp_f085_net_cash_position_ncz_21d_xemac_base_v032_signal,
    f085ncp_f085_net_cash_position_ncz_21d_xmean_base_v033_signal,
    f085ncp_f085_net_cash_position_ncz_21d_xclose2_base_v034_signal,
    f085ncp_f085_net_cash_position_ncz_21d_xmlong_base_v035_signal,
    f085ncp_f085_net_cash_position_ncz_63d_xclose_base_v036_signal,
    f085ncp_f085_net_cash_position_ncz_63d_xemac_base_v037_signal,
    f085ncp_f085_net_cash_position_ncz_63d_xmean_base_v038_signal,
    f085ncp_f085_net_cash_position_ncz_63d_xclose2_base_v039_signal,
    f085ncp_f085_net_cash_position_ncz_63d_xmlong_base_v040_signal,
    f085ncp_f085_net_cash_position_ncz_252d_xclose_base_v041_signal,
    f085ncp_f085_net_cash_position_ncz_252d_xemac_base_v042_signal,
    f085ncp_f085_net_cash_position_ncz_252d_xmean_base_v043_signal,
    f085ncp_f085_net_cash_position_ncz_252d_xclose2_base_v044_signal,
    f085ncp_f085_net_cash_position_ncz_252d_xmlong_base_v045_signal,
    f085ncp_f085_net_cash_position_nce_21d_xclose_base_v046_signal,
    f085ncp_f085_net_cash_position_nce_21d_xemac_base_v047_signal,
    f085ncp_f085_net_cash_position_nce_21d_xmean_base_v048_signal,
    f085ncp_f085_net_cash_position_nce_21d_xclose2_base_v049_signal,
    f085ncp_f085_net_cash_position_nce_21d_xmlong_base_v050_signal,
    f085ncp_f085_net_cash_position_nce_63d_xclose_base_v051_signal,
    f085ncp_f085_net_cash_position_nce_63d_xemac_base_v052_signal,
    f085ncp_f085_net_cash_position_nce_63d_xmean_base_v053_signal,
    f085ncp_f085_net_cash_position_nce_63d_xclose2_base_v054_signal,
    f085ncp_f085_net_cash_position_nce_63d_xmlong_base_v055_signal,
    f085ncp_f085_net_cash_position_nce_252d_xclose_base_v056_signal,
    f085ncp_f085_net_cash_position_nce_252d_xemac_base_v057_signal,
    f085ncp_f085_net_cash_position_nce_252d_xmean_base_v058_signal,
    f085ncp_f085_net_cash_position_nce_252d_xclose2_base_v059_signal,
    f085ncp_f085_net_cash_position_nce_252d_xmlong_base_v060_signal,
    f085ncp_f085_net_cash_position_ncr_21d_xclose_base_v061_signal,
    f085ncp_f085_net_cash_position_ncr_21d_xemac_base_v062_signal,
    f085ncp_f085_net_cash_position_ncr_21d_xmean_base_v063_signal,
    f085ncp_f085_net_cash_position_ncr_21d_xclose2_base_v064_signal,
    f085ncp_f085_net_cash_position_ncr_21d_xmlong_base_v065_signal,
    f085ncp_f085_net_cash_position_ncr_63d_xclose_base_v066_signal,
    f085ncp_f085_net_cash_position_ncr_63d_xemac_base_v067_signal,
    f085ncp_f085_net_cash_position_ncr_63d_xmean_base_v068_signal,
    f085ncp_f085_net_cash_position_ncr_63d_xclose2_base_v069_signal,
    f085ncp_f085_net_cash_position_ncr_63d_xmlong_base_v070_signal,
    f085ncp_f085_net_cash_position_ncr_252d_xclose_base_v071_signal,
    f085ncp_f085_net_cash_position_ncr_252d_xemac_base_v072_signal,
    f085ncp_f085_net_cash_position_ncr_252d_xmean_base_v073_signal,
    f085ncp_f085_net_cash_position_ncr_252d_xclose2_base_v074_signal,
    f085ncp_f085_net_cash_position_ncr_252d_xmlong_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F085_NET_CASH_POSITION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
        "fcf": fcf, "ncfo": ncfo, "cashneq": cashneq, "debt": debt, "equity": equity,
        "sharesbas": sharesbas, "shareswa": shareswa, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f085_net_cash", "_f085_net_cash_ratio", "_f085_bs_strength")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f085_net_cash_position_base_001_075_claude: {n_features} features pass")
