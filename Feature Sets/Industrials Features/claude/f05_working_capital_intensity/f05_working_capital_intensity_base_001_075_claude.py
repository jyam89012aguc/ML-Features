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

# ===== folder domain primitives =====
def _f05_working_capital_ratio(inventory, receivables, payables, revenue):
    wc = inventory + receivables - payables
    return wc / revenue.replace(0, np.nan).abs()


def _f05_net_op_cycle(inventory, receivables, payables, cor):
    inv_days = 365.0 * inventory / cor.replace(0, np.nan).abs()
    rec_days = 365.0 * receivables / cor.replace(0, np.nan).abs()
    pay_days = 365.0 * payables / cor.replace(0, np.nan).abs()
    return inv_days + rec_days - pay_days


def _f05_wc_burn(workingcapital, revenue, w):
    burn = workingcapital.pct_change(periods=w)
    rev_scale = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return burn * rev_scale / revenue.replace(0, np.nan).abs()

def f05wci_f05_working_capital_intensity_wcr_5d_base_v001_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_10d_base_v002_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_21d_base_v003_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_42d_base_v004_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_63d_base_v005_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_126d_base_v006_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_189d_base_v007_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcr_252d_base_v008_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_5d_base_v009_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 5) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_10d_base_v010_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 10) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_21d_base_v011_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 21) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_42d_base_v012_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 42) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_63d_base_v013_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 63) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_126d_base_v014_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 126) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_189d_base_v015_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 189) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noc_252d_base_v016_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 252) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_5d_base_v017_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_10d_base_v018_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_21d_base_v019_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_42d_base_v020_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_63d_base_v021_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_126d_base_v022_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_189d_base_v023_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcb_252d_base_v024_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_5d_base_v025_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_10d_base_v026_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_21d_base_v027_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_42d_base_v028_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_63d_base_v029_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_126d_base_v030_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_189d_base_v031_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrstd_252d_base_v032_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_5d_base_v033_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 5) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_10d_base_v034_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 10) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_21d_base_v035_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 21) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_42d_base_v036_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 42) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_63d_base_v037_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 63) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_126d_base_v038_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 126) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_189d_base_v039_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 189) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocstd_252d_base_v040_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _std(base, 252) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_5d_base_v041_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_10d_base_v042_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_21d_base_v043_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_42d_base_v044_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_63d_base_v045_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_126d_base_v046_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_189d_base_v047_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbstd_252d_base_v048_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrz_21d_base_v049_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrz_63d_base_v050_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrz_126d_base_v051_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrz_252d_base_v052_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocz_21d_base_v053_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocz_63d_base_v054_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocz_126d_base_v055_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocz_252d_base_v056_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbz_21d_base_v057_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbz_63d_base_v058_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbz_126d_base_v059_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbz_252d_base_v060_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrchg_21d_base_v061_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrchg_63d_base_v062_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrchg_126d_base_v063_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrchg_252d_base_v064_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocchg_21d_base_v065_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.diff(21) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocchg_63d_base_v066_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.diff(63) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocchg_126d_base_v067_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.diff(126) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocchg_252d_base_v068_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.diff(252) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbchg_21d_base_v069_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbchg_63d_base_v070_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbchg_126d_base_v071_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbchg_252d_base_v072_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxnoc_21d_base_v073_signal(inventory, receivables, payables, revenue, cor, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 21) * _mean(b, 21) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxnoc_63d_base_v074_signal(inventory, receivables, payables, revenue, cor, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 63) * _mean(b, 63) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxnoc_126d_base_v075_signal(inventory, receivables, payables, revenue, cor, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 126) * _mean(b, 126) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05wci_f05_working_capital_intensity_wcr_5d_base_v001_signal,
    f05wci_f05_working_capital_intensity_wcr_10d_base_v002_signal,
    f05wci_f05_working_capital_intensity_wcr_21d_base_v003_signal,
    f05wci_f05_working_capital_intensity_wcr_42d_base_v004_signal,
    f05wci_f05_working_capital_intensity_wcr_63d_base_v005_signal,
    f05wci_f05_working_capital_intensity_wcr_126d_base_v006_signal,
    f05wci_f05_working_capital_intensity_wcr_189d_base_v007_signal,
    f05wci_f05_working_capital_intensity_wcr_252d_base_v008_signal,
    f05wci_f05_working_capital_intensity_noc_5d_base_v009_signal,
    f05wci_f05_working_capital_intensity_noc_10d_base_v010_signal,
    f05wci_f05_working_capital_intensity_noc_21d_base_v011_signal,
    f05wci_f05_working_capital_intensity_noc_42d_base_v012_signal,
    f05wci_f05_working_capital_intensity_noc_63d_base_v013_signal,
    f05wci_f05_working_capital_intensity_noc_126d_base_v014_signal,
    f05wci_f05_working_capital_intensity_noc_189d_base_v015_signal,
    f05wci_f05_working_capital_intensity_noc_252d_base_v016_signal,
    f05wci_f05_working_capital_intensity_wcb_5d_base_v017_signal,
    f05wci_f05_working_capital_intensity_wcb_10d_base_v018_signal,
    f05wci_f05_working_capital_intensity_wcb_21d_base_v019_signal,
    f05wci_f05_working_capital_intensity_wcb_42d_base_v020_signal,
    f05wci_f05_working_capital_intensity_wcb_63d_base_v021_signal,
    f05wci_f05_working_capital_intensity_wcb_126d_base_v022_signal,
    f05wci_f05_working_capital_intensity_wcb_189d_base_v023_signal,
    f05wci_f05_working_capital_intensity_wcb_252d_base_v024_signal,
    f05wci_f05_working_capital_intensity_wcrstd_5d_base_v025_signal,
    f05wci_f05_working_capital_intensity_wcrstd_10d_base_v026_signal,
    f05wci_f05_working_capital_intensity_wcrstd_21d_base_v027_signal,
    f05wci_f05_working_capital_intensity_wcrstd_42d_base_v028_signal,
    f05wci_f05_working_capital_intensity_wcrstd_63d_base_v029_signal,
    f05wci_f05_working_capital_intensity_wcrstd_126d_base_v030_signal,
    f05wci_f05_working_capital_intensity_wcrstd_189d_base_v031_signal,
    f05wci_f05_working_capital_intensity_wcrstd_252d_base_v032_signal,
    f05wci_f05_working_capital_intensity_nocstd_5d_base_v033_signal,
    f05wci_f05_working_capital_intensity_nocstd_10d_base_v034_signal,
    f05wci_f05_working_capital_intensity_nocstd_21d_base_v035_signal,
    f05wci_f05_working_capital_intensity_nocstd_42d_base_v036_signal,
    f05wci_f05_working_capital_intensity_nocstd_63d_base_v037_signal,
    f05wci_f05_working_capital_intensity_nocstd_126d_base_v038_signal,
    f05wci_f05_working_capital_intensity_nocstd_189d_base_v039_signal,
    f05wci_f05_working_capital_intensity_nocstd_252d_base_v040_signal,
    f05wci_f05_working_capital_intensity_wcbstd_5d_base_v041_signal,
    f05wci_f05_working_capital_intensity_wcbstd_10d_base_v042_signal,
    f05wci_f05_working_capital_intensity_wcbstd_21d_base_v043_signal,
    f05wci_f05_working_capital_intensity_wcbstd_42d_base_v044_signal,
    f05wci_f05_working_capital_intensity_wcbstd_63d_base_v045_signal,
    f05wci_f05_working_capital_intensity_wcbstd_126d_base_v046_signal,
    f05wci_f05_working_capital_intensity_wcbstd_189d_base_v047_signal,
    f05wci_f05_working_capital_intensity_wcbstd_252d_base_v048_signal,
    f05wci_f05_working_capital_intensity_wcrz_21d_base_v049_signal,
    f05wci_f05_working_capital_intensity_wcrz_63d_base_v050_signal,
    f05wci_f05_working_capital_intensity_wcrz_126d_base_v051_signal,
    f05wci_f05_working_capital_intensity_wcrz_252d_base_v052_signal,
    f05wci_f05_working_capital_intensity_nocz_21d_base_v053_signal,
    f05wci_f05_working_capital_intensity_nocz_63d_base_v054_signal,
    f05wci_f05_working_capital_intensity_nocz_126d_base_v055_signal,
    f05wci_f05_working_capital_intensity_nocz_252d_base_v056_signal,
    f05wci_f05_working_capital_intensity_wcbz_21d_base_v057_signal,
    f05wci_f05_working_capital_intensity_wcbz_63d_base_v058_signal,
    f05wci_f05_working_capital_intensity_wcbz_126d_base_v059_signal,
    f05wci_f05_working_capital_intensity_wcbz_252d_base_v060_signal,
    f05wci_f05_working_capital_intensity_wcrchg_21d_base_v061_signal,
    f05wci_f05_working_capital_intensity_wcrchg_63d_base_v062_signal,
    f05wci_f05_working_capital_intensity_wcrchg_126d_base_v063_signal,
    f05wci_f05_working_capital_intensity_wcrchg_252d_base_v064_signal,
    f05wci_f05_working_capital_intensity_nocchg_21d_base_v065_signal,
    f05wci_f05_working_capital_intensity_nocchg_63d_base_v066_signal,
    f05wci_f05_working_capital_intensity_nocchg_126d_base_v067_signal,
    f05wci_f05_working_capital_intensity_nocchg_252d_base_v068_signal,
    f05wci_f05_working_capital_intensity_wcbchg_21d_base_v069_signal,
    f05wci_f05_working_capital_intensity_wcbchg_63d_base_v070_signal,
    f05wci_f05_working_capital_intensity_wcbchg_126d_base_v071_signal,
    f05wci_f05_working_capital_intensity_wcbchg_252d_base_v072_signal,
    f05wci_f05_working_capital_intensity_wcrxnoc_21d_base_v073_signal,
    f05wci_f05_working_capital_intensity_wcrxnoc_63d_base_v074_signal,
    f05wci_f05_working_capital_intensity_wcrxnoc_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_WORKING_CAPITAL_INTENSITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f05_working_capital_ratio', '_f05_net_op_cycle', '_f05_wc_burn')
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
    print(f"OK f05_working_capital_intensity_base_001_075_claude: {n_features} features pass")
