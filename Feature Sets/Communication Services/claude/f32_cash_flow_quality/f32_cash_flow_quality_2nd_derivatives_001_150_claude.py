import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (cash flow quality) =====
def _f32_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f32_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f32_cash_conv(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan)


def _f32_capex_cover(ncfo, capex):
    return ncfo / capex.replace(0, np.nan)


def _f32_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f32_selffund_balance(ncfo, capex):
    return (ncfo - capex) / (ncfo.abs() + capex).replace(0, np.nan)

# slope of fcfmgn base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgn_21d_slope_v001_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgn base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgn_63d_slope_v002_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgn base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgn_126d_slope_v003_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgn base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgn_21d_slope_v004_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgn base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgn_63d_slope_v005_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgn base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgn_126d_slope_v006_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconv base over 21d horizon
def f32cf_f32_cash_flow_quality_cashconv_21d_slope_v007_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconv base over 63d horizon
def f32cf_f32_cash_flow_quality_cashconv_63d_slope_v008_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconv base over 126d horizon
def f32cf_f32_cash_flow_quality_cashconv_126d_slope_v009_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgr base over 21d horizon
def f32cf_f32_cash_flow_quality_capexgr_21d_slope_v010_signal(capex):
    base = np.log(_mean(capex, 21).replace(0, np.nan)) - np.log(_mean(capex, 21).shift(63).replace(0, np.nan))
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgr base over 63d horizon
def f32cf_f32_cash_flow_quality_capexgr_63d_slope_v011_signal(capex):
    base = np.log(_mean(capex, 21).replace(0, np.nan)) - np.log(_mean(capex, 21).shift(63).replace(0, np.nan))
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgr base over 126d horizon
def f32cf_f32_cash_flow_quality_capexgr_126d_slope_v012_signal(capex):
    base = np.log(_mean(capex, 21).replace(0, np.nan)) - np.log(_mean(capex, 21).shift(63).replace(0, np.nan))
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexint base over 21d horizon
def f32cf_f32_cash_flow_quality_capexint_21d_slope_v013_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexint base over 63d horizon
def f32cf_f32_cash_flow_quality_capexint_63d_slope_v014_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexint base over 126d horizon
def f32cf_f32_cash_flow_quality_capexint_126d_slope_v015_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffund base over 21d horizon
def f32cf_f32_cash_flow_quality_selffund_21d_slope_v016_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffund base over 63d horizon
def f32cf_f32_cash_flow_quality_selffund_63d_slope_v017_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffund base over 126d horizon
def f32cf_f32_cash_flow_quality_selffund_126d_slope_v018_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfps base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfps_21d_slope_v019_signal(fcfps):
    base = fcfps
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfps base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfps_63d_slope_v020_signal(fcfps):
    base = fcfps
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfps base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfps_126d_slope_v021_signal(fcfps):
    base = fcfps
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgn base over 21d horizon
def f32cf_f32_cash_flow_quality_netmgn_21d_slope_v022_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgn base over 63d horizon
def f32cf_f32_cash_flow_quality_netmgn_63d_slope_v023_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgn base over 126d horizon
def f32cf_f32_cash_flow_quality_netmgn_126d_slope_v024_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfofocf base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfofocf_21d_slope_v025_signal(fcf, ncfo):
    base = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfofocf base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfofocf_63d_slope_v026_signal(fcf, ncfo):
    base = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfofocf base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfofocf_126d_slope_v027_signal(fcf, ncfo):
    base = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of accrshare base over 21d horizon
def f32cf_f32_cash_flow_quality_accrshare_21d_slope_v028_signal(netinc, ncfo):
    base = (netinc - ncfo) / (netinc.abs() + ncfo.abs()).replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of accrshare base over 63d horizon
def f32cf_f32_cash_flow_quality_accrshare_63d_slope_v029_signal(netinc, ncfo):
    base = (netinc - ncfo) / (netinc.abs() + ncfo.abs()).replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of accrshare base over 126d horizon
def f32cf_f32_cash_flow_quality_accrshare_126d_slope_v030_signal(netinc, ncfo):
    base = (netinc - ncfo) / (netinc.abs() + ncfo.abs()).replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of paperscash base over 21d horizon
def f32cf_f32_cash_flow_quality_paperscash_21d_slope_v031_signal(netinc, fcf):
    base = (netinc - fcf) / (netinc.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of paperscash base over 63d horizon
def f32cf_f32_cash_flow_quality_paperscash_63d_slope_v032_signal(netinc, fcf):
    base = (netinc - fcf) / (netinc.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of paperscash base over 126d horizon
def f32cf_f32_cash_flow_quality_paperscash_126d_slope_v033_signal(netinc, fcf):
    base = (netinc - fcf) / (netinc.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexwedge base over 21d horizon
def f32cf_f32_cash_flow_quality_capexwedge_21d_slope_v034_signal(ncfo, fcf):
    base = (ncfo - fcf) / (ncfo.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexwedge base over 63d horizon
def f32cf_f32_cash_flow_quality_capexwedge_63d_slope_v035_signal(ncfo, fcf):
    base = (ncfo - fcf) / (ncfo.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexwedge base over 126d horizon
def f32cf_f32_cash_flow_quality_capexwedge_126d_slope_v036_signal(ncfo, fcf):
    base = (ncfo - fcf) / (ncfo.abs() + fcf.abs()).replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnz base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnz_21d_slope_v037_signal(fcf, revenue):
    base = _z(_f32_fcf_margin(fcf, revenue), 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnz base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnz_63d_slope_v038_signal(fcf, revenue):
    base = _z(_f32_fcf_margin(fcf, revenue), 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnz base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnz_126d_slope_v039_signal(fcf, revenue):
    base = _z(_f32_fcf_margin(fcf, revenue), 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnz base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnz_21d_slope_v040_signal(ncfo, revenue):
    base = _z(_f32_ocf_margin(ncfo, revenue), 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnz base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnz_63d_slope_v041_signal(ncfo, revenue):
    base = _z(_f32_ocf_margin(ncfo, revenue), 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnz base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnz_126d_slope_v042_signal(ncfo, revenue):
    base = _z(_f32_ocf_margin(ncfo, revenue), 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconvz base over 21d horizon
def f32cf_f32_cash_flow_quality_cashconvz_21d_slope_v043_signal(ncfo, netinc):
    base = _z(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconvz base over 63d horizon
def f32cf_f32_cash_flow_quality_cashconvz_63d_slope_v044_signal(ncfo, netinc):
    base = _z(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of cashconvz base over 126d horizon
def f32cf_f32_cash_flow_quality_cashconvz_126d_slope_v045_signal(ncfo, netinc):
    base = _z(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintz base over 21d horizon
def f32cf_f32_cash_flow_quality_capexintz_21d_slope_v046_signal(capex, revenue):
    base = _z(_f32_capex_intensity(capex, revenue), 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintz base over 63d horizon
def f32cf_f32_cash_flow_quality_capexintz_63d_slope_v047_signal(capex, revenue):
    base = _z(_f32_capex_intensity(capex, revenue), 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintz base over 126d horizon
def f32cf_f32_cash_flow_quality_capexintz_126d_slope_v048_signal(capex, revenue):
    base = _z(_f32_capex_intensity(capex, revenue), 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsz base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfpsz_21d_slope_v049_signal(fcfps):
    base = _z(fcfps, 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsz base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfpsz_63d_slope_v050_signal(fcfps):
    base = _z(fcfps, 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsz base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfpsz_126d_slope_v051_signal(fcfps):
    base = _z(fcfps, 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrank base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrank_21d_slope_v052_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrank base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrank_63d_slope_v053_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrank base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrank_126d_slope_v054_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnrank base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnrank_21d_slope_v055_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnrank base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnrank_63d_slope_v056_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnrank base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnrank_126d_slope_v057_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrank base over 21d horizon
def f32cf_f32_cash_flow_quality_selffundrank_21d_slope_v058_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrank base over 63d horizon
def f32cf_f32_cash_flow_quality_selffundrank_63d_slope_v059_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrank base over 126d horizon
def f32cf_f32_cash_flow_quality_selffundrank_126d_slope_v060_signal(ncfo, capex):
    base = _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnvol base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnvol_21d_slope_v061_signal(fcf, revenue):
    base = _std(_f32_fcf_margin(fcf, revenue), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnvol base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnvol_63d_slope_v062_signal(fcf, revenue):
    base = _std(_f32_fcf_margin(fcf, revenue), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnvol base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnvol_126d_slope_v063_signal(fcf, revenue):
    base = _std(_f32_fcf_margin(fcf, revenue), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnvol base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnvol_21d_slope_v064_signal(ncfo, revenue):
    base = _std(_f32_ocf_margin(ncfo, revenue), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnvol base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnvol_63d_slope_v065_signal(ncfo, revenue):
    base = _std(_f32_ocf_margin(ncfo, revenue), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnvol base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnvol_126d_slope_v066_signal(ncfo, revenue):
    base = _std(_f32_ocf_margin(ncfo, revenue), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convvol base over 21d horizon
def f32cf_f32_cash_flow_quality_convvol_21d_slope_v067_signal(ncfo, netinc):
    base = _std(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convvol base over 63d horizon
def f32cf_f32_cash_flow_quality_convvol_63d_slope_v068_signal(ncfo, netinc):
    base = _std(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convvol base over 126d horizon
def f32cf_f32_cash_flow_quality_convvol_126d_slope_v069_signal(ncfo, netinc):
    base = _std(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintvol base over 21d horizon
def f32cf_f32_cash_flow_quality_capexintvol_21d_slope_v070_signal(capex, revenue):
    base = _std(_f32_capex_intensity(capex, revenue), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintvol base over 63d horizon
def f32cf_f32_cash_flow_quality_capexintvol_63d_slope_v071_signal(capex, revenue):
    base = _std(_f32_capex_intensity(capex, revenue), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintvol base over 126d horizon
def f32cf_f32_cash_flow_quality_capexintvol_126d_slope_v072_signal(capex, revenue):
    base = _std(_f32_capex_intensity(capex, revenue), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmed base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmed_21d_slope_v073_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmed base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmed_63d_slope_v074_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmed base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmed_126d_slope_v075_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmed base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmed_21d_slope_v076_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmed base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmed_63d_slope_v077_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmed base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmed_126d_slope_v078_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).median()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnvol base over 21d horizon
def f32cf_f32_cash_flow_quality_netmgnvol_21d_slope_v079_signal(netinc, revenue):
    base = _std(netinc / revenue.replace(0, np.nan), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnvol base over 63d horizon
def f32cf_f32_cash_flow_quality_netmgnvol_63d_slope_v080_signal(netinc, revenue):
    base = _std(netinc / revenue.replace(0, np.nan), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnvol base over 126d horizon
def f32cf_f32_cash_flow_quality_netmgnvol_126d_slope_v081_signal(netinc, revenue):
    base = _std(netinc / revenue.replace(0, np.nan), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrng base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrng_21d_slope_v082_signal(fcf, revenue):
    base = (_f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()) / (_f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max() - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrng base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrng_63d_slope_v083_signal(fcf, revenue):
    base = (_f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()) / (_f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max() - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnrng base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnrng_126d_slope_v084_signal(fcf, revenue):
    base = (_f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()) / (_f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max() - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrng base over 21d horizon
def f32cf_f32_cash_flow_quality_selffundrng_21d_slope_v085_signal(ncfo, capex):
    base = (_f32_selffund_balance(ncfo, capex) - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()) / (_f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).max() - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrng base over 63d horizon
def f32cf_f32_cash_flow_quality_selffundrng_63d_slope_v086_signal(ncfo, capex):
    base = (_f32_selffund_balance(ncfo, capex) - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()) / (_f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).max() - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundrng base over 126d horizon
def f32cf_f32_cash_flow_quality_selffundrng_126d_slope_v087_signal(ncfo, capex):
    base = (_f32_selffund_balance(ncfo, capex) - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()) / (_f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).max() - _f32_selffund_balance(ncfo, capex).rolling(252, min_periods=126).min()).replace(0, np.nan)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndd base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgndd_21d_slope_v088_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndd base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgndd_63d_slope_v089_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndd base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgndd_126d_slope_v090_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue) - _f32_fcf_margin(fcf, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgndd base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgndd_21d_slope_v091_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgndd base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgndd_63d_slope_v092_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgndd base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgndd_126d_slope_v093_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue) - _f32_ocf_margin(ncfo, revenue).rolling(252, min_periods=126).max()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsdd base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfpsdd_21d_slope_v094_signal(fcfps):
    base = fcfps - fcfps.rolling(252, min_periods=126).max()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsdd base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfpsdd_63d_slope_v095_signal(fcfps):
    base = fcfps - fcfps.rolling(252, min_periods=126).max()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfpsdd base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfpsdd_126d_slope_v096_signal(fcfps):
    base = fcfps - fcfps.rolling(252, min_periods=126).max()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnac base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnac_21d_slope_v097_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnac base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnac_63d_slope_v098_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnac base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnac_126d_slope_v099_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnac base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnac_21d_slope_v100_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnac base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnac_63d_slope_v101_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnac base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnac_126d_slope_v102_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).rolling(126, min_periods=63).apply(lambda a: pd.Series(a).autocorr(lag=10) if len(a) > 12 else np.nan, raw=True)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfncfocorr base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfncfocorr_21d_slope_v103_signal(fcf, ncfo):
    base = fcf.diff().rolling(126, min_periods=63).corr(ncfo.diff())
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfncfocorr base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfncfocorr_63d_slope_v104_signal(fcf, ncfo):
    base = fcf.diff().rolling(126, min_periods=63).corr(ncfo.diff())
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfncfocorr base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfncfocorr_126d_slope_v105_signal(fcf, ncfo):
    base = fcf.diff().rolling(126, min_periods=63).corr(ncfo.diff())
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfcapexcorr base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfcapexcorr_21d_slope_v106_signal(fcf, capex):
    base = fcf.diff().rolling(126, min_periods=63).corr(capex.diff())
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfcapexcorr base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfcapexcorr_63d_slope_v107_signal(fcf, capex):
    base = fcf.diff().rolling(126, min_periods=63).corr(capex.diff())
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfcapexcorr base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfcapexcorr_126d_slope_v108_signal(fcf, capex):
    base = fcf.diff().rolling(126, min_periods=63).corr(capex.diff())
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfonetcorr base over 21d horizon
def f32cf_f32_cash_flow_quality_ncfonetcorr_21d_slope_v109_signal(ncfo, netinc):
    base = ncfo.diff().rolling(126, min_periods=63).corr(netinc.diff())
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfonetcorr base over 63d horizon
def f32cf_f32_cash_flow_quality_ncfonetcorr_63d_slope_v110_signal(ncfo, netinc):
    base = ncfo.diff().rolling(126, min_periods=63).corr(netinc.diff())
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfonetcorr base over 126d horizon
def f32cf_f32_cash_flow_quality_ncfonetcorr_126d_slope_v111_signal(ncfo, netinc):
    base = ncfo.diff().rolling(126, min_periods=63).corr(netinc.diff())
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmacd base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmacd_21d_slope_v112_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).ewm(span=21, min_periods=10).mean() - _f32_fcf_margin(fcf, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmacd base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmacd_63d_slope_v113_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).ewm(span=21, min_periods=10).mean() - _f32_fcf_margin(fcf, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnmacd base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnmacd_126d_slope_v114_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).ewm(span=21, min_periods=10).mean() - _f32_fcf_margin(fcf, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmacd base over 21d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmacd_21d_slope_v115_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).ewm(span=21, min_periods=10).mean() - _f32_ocf_margin(ncfo, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmacd base over 63d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmacd_63d_slope_v116_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).ewm(span=21, min_periods=10).mean() - _f32_ocf_margin(ncfo, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ocfmgnmacd base over 126d horizon
def f32cf_f32_cash_flow_quality_ocfmgnmacd_126d_slope_v117_signal(ncfo, revenue):
    base = _f32_ocf_margin(ncfo, revenue).ewm(span=21, min_periods=10).mean() - _f32_ocf_margin(ncfo, revenue).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convmacd base over 21d horizon
def f32cf_f32_cash_flow_quality_convmacd_21d_slope_v118_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=21, min_periods=10).mean() - _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convmacd base over 63d horizon
def f32cf_f32_cash_flow_quality_convmacd_63d_slope_v119_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=21, min_periods=10).mean() - _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convmacd base over 126d horizon
def f32cf_f32_cash_flow_quality_convmacd_126d_slope_v120_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=21, min_periods=10).mean() - _f32_cash_conv(ncfo, netinc).clip(-5, 5).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of jointcash base over 21d horizon
def f32cf_f32_cash_flow_quality_jointcash_21d_slope_v121_signal(fcf, ncfo, revenue):
    base = _f32_fcf_margin(fcf, revenue) * _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of jointcash base over 63d horizon
def f32cf_f32_cash_flow_quality_jointcash_63d_slope_v122_signal(fcf, ncfo, revenue):
    base = _f32_fcf_margin(fcf, revenue) * _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of jointcash base over 126d horizon
def f32cf_f32_cash_flow_quality_jointcash_126d_slope_v123_signal(fcf, ncfo, revenue):
    base = _f32_fcf_margin(fcf, revenue) * _f32_ocf_margin(ncfo, revenue)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convxmgn base over 21d horizon
def f32cf_f32_cash_flow_quality_convxmgn_21d_slope_v124_signal(ncfo, netinc, revenue):
    base = _f32_ocf_margin(ncfo, revenue) * (_f32_cash_conv(ncfo, netinc).clip(-5, 5) - 1.0)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convxmgn base over 63d horizon
def f32cf_f32_cash_flow_quality_convxmgn_63d_slope_v125_signal(ncfo, netinc, revenue):
    base = _f32_ocf_margin(ncfo, revenue) * (_f32_cash_conv(ncfo, netinc).clip(-5, 5) - 1.0)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convxmgn base over 126d horizon
def f32cf_f32_cash_flow_quality_convxmgn_126d_slope_v126_signal(ncfo, netinc, revenue):
    base = _f32_ocf_margin(ncfo, revenue) * (_f32_cash_conv(ncfo, netinc).clip(-5, 5) - 1.0)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnskew base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgnskew_21d_slope_v127_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnskew base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgnskew_63d_slope_v128_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgnskew base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgnskew_126d_slope_v129_signal(fcf, revenue):
    base = _f32_fcf_margin(fcf, revenue).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convskew base over 21d horizon
def f32cf_f32_cash_flow_quality_convskew_21d_slope_v130_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convskew base over 63d horizon
def f32cf_f32_cash_flow_quality_convskew_63d_slope_v131_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of convskew base over 126d horizon
def f32cf_f32_cash_flow_quality_convskew_126d_slope_v132_signal(ncfo, netinc):
    base = _f32_cash_conv(ncfo, netinc).clip(-5, 5).rolling(126, min_periods=63).skew()
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfsm base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfsm_21d_slope_v133_signal(fcf):
    base = np.sign(_mean(fcf, 21)) * (_mean(fcf, 21).abs() ** 0.5)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfsm base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfsm_63d_slope_v134_signal(fcf):
    base = np.sign(_mean(fcf, 21)) * (_mean(fcf, 21).abs() ** 0.5)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfsm base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfsm_126d_slope_v135_signal(fcf):
    base = np.sign(_mean(fcf, 21)) * (_mean(fcf, 21).abs() ** 0.5)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfosm base over 21d horizon
def f32cf_f32_cash_flow_quality_ncfosm_21d_slope_v136_signal(ncfo):
    base = np.sign(_mean(ncfo, 21)) * (_mean(ncfo, 21).abs() ** 0.5)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfosm base over 63d horizon
def f32cf_f32_cash_flow_quality_ncfosm_63d_slope_v137_signal(ncfo):
    base = np.sign(_mean(ncfo, 21)) * (_mean(ncfo, 21).abs() ** 0.5)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ncfosm base over 126d horizon
def f32cf_f32_cash_flow_quality_ncfosm_126d_slope_v138_signal(ncfo):
    base = np.sign(_mean(ncfo, 21)) * (_mean(ncfo, 21).abs() ** 0.5)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndsd base over 21d horizon
def f32cf_f32_cash_flow_quality_fcfmgndsd_21d_slope_v139_signal(fcf, revenue):
    base = ((_f32_fcf_margin(fcf, revenue) - _mean(_f32_fcf_margin(fcf, revenue), 252)).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndsd base over 63d horizon
def f32cf_f32_cash_flow_quality_fcfmgndsd_63d_slope_v140_signal(fcf, revenue):
    base = ((_f32_fcf_margin(fcf, revenue) - _mean(_f32_fcf_margin(fcf, revenue), 252)).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fcfmgndsd base over 126d horizon
def f32cf_f32_cash_flow_quality_fcfmgndsd_126d_slope_v141_signal(fcf, revenue):
    base = ((_f32_fcf_margin(fcf, revenue) - _mean(_f32_fcf_margin(fcf, revenue), 252)).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintrank base over 21d horizon
def f32cf_f32_cash_flow_quality_capexintrank_21d_slope_v142_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintrank base over 63d horizon
def f32cf_f32_cash_flow_quality_capexintrank_63d_slope_v143_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexintrank base over 126d horizon
def f32cf_f32_cash_flow_quality_capexintrank_126d_slope_v144_signal(capex, revenue):
    base = _f32_capex_intensity(capex, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundvol base over 21d horizon
def f32cf_f32_cash_flow_quality_selffundvol_21d_slope_v145_signal(ncfo, capex):
    base = _std(_f32_selffund_balance(ncfo, capex), 126)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundvol base over 63d horizon
def f32cf_f32_cash_flow_quality_selffundvol_63d_slope_v146_signal(ncfo, capex):
    base = _std(_f32_selffund_balance(ncfo, capex), 126)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of selffundvol base over 126d horizon
def f32cf_f32_cash_flow_quality_selffundvol_126d_slope_v147_signal(ncfo, capex):
    base = _std(_f32_selffund_balance(ncfo, capex), 126)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnz base over 21d horizon
def f32cf_f32_cash_flow_quality_netmgnz_21d_slope_v148_signal(netinc, revenue):
    base = _z(netinc / revenue.replace(0, np.nan), 252)
    d1 = base - base.shift(21)
    b = d1 / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnz base over 63d horizon
def f32cf_f32_cash_flow_quality_netmgnz_63d_slope_v149_signal(netinc, revenue):
    base = _z(netinc / revenue.replace(0, np.nan), 252)
    d1 = base - base.shift(63)
    b = d1 / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of netmgnz base over 126d horizon
def f32cf_f32_cash_flow_quality_netmgnz_126d_slope_v150_signal(netinc, revenue):
    base = _z(netinc / revenue.replace(0, np.nan), 252)
    d1 = base - base.shift(126)
    b = d1 / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f32cf_f32_cash_flow_quality_fcfmgn_21d_slope_v001_signal,
    f32cf_f32_cash_flow_quality_fcfmgn_63d_slope_v002_signal,
    f32cf_f32_cash_flow_quality_fcfmgn_126d_slope_v003_signal,
    f32cf_f32_cash_flow_quality_ocfmgn_21d_slope_v004_signal,
    f32cf_f32_cash_flow_quality_ocfmgn_63d_slope_v005_signal,
    f32cf_f32_cash_flow_quality_ocfmgn_126d_slope_v006_signal,
    f32cf_f32_cash_flow_quality_cashconv_21d_slope_v007_signal,
    f32cf_f32_cash_flow_quality_cashconv_63d_slope_v008_signal,
    f32cf_f32_cash_flow_quality_cashconv_126d_slope_v009_signal,
    f32cf_f32_cash_flow_quality_capexgr_21d_slope_v010_signal,
    f32cf_f32_cash_flow_quality_capexgr_63d_slope_v011_signal,
    f32cf_f32_cash_flow_quality_capexgr_126d_slope_v012_signal,
    f32cf_f32_cash_flow_quality_capexint_21d_slope_v013_signal,
    f32cf_f32_cash_flow_quality_capexint_63d_slope_v014_signal,
    f32cf_f32_cash_flow_quality_capexint_126d_slope_v015_signal,
    f32cf_f32_cash_flow_quality_selffund_21d_slope_v016_signal,
    f32cf_f32_cash_flow_quality_selffund_63d_slope_v017_signal,
    f32cf_f32_cash_flow_quality_selffund_126d_slope_v018_signal,
    f32cf_f32_cash_flow_quality_fcfps_21d_slope_v019_signal,
    f32cf_f32_cash_flow_quality_fcfps_63d_slope_v020_signal,
    f32cf_f32_cash_flow_quality_fcfps_126d_slope_v021_signal,
    f32cf_f32_cash_flow_quality_netmgn_21d_slope_v022_signal,
    f32cf_f32_cash_flow_quality_netmgn_63d_slope_v023_signal,
    f32cf_f32_cash_flow_quality_netmgn_126d_slope_v024_signal,
    f32cf_f32_cash_flow_quality_fcfofocf_21d_slope_v025_signal,
    f32cf_f32_cash_flow_quality_fcfofocf_63d_slope_v026_signal,
    f32cf_f32_cash_flow_quality_fcfofocf_126d_slope_v027_signal,
    f32cf_f32_cash_flow_quality_accrshare_21d_slope_v028_signal,
    f32cf_f32_cash_flow_quality_accrshare_63d_slope_v029_signal,
    f32cf_f32_cash_flow_quality_accrshare_126d_slope_v030_signal,
    f32cf_f32_cash_flow_quality_paperscash_21d_slope_v031_signal,
    f32cf_f32_cash_flow_quality_paperscash_63d_slope_v032_signal,
    f32cf_f32_cash_flow_quality_paperscash_126d_slope_v033_signal,
    f32cf_f32_cash_flow_quality_capexwedge_21d_slope_v034_signal,
    f32cf_f32_cash_flow_quality_capexwedge_63d_slope_v035_signal,
    f32cf_f32_cash_flow_quality_capexwedge_126d_slope_v036_signal,
    f32cf_f32_cash_flow_quality_fcfmgnz_21d_slope_v037_signal,
    f32cf_f32_cash_flow_quality_fcfmgnz_63d_slope_v038_signal,
    f32cf_f32_cash_flow_quality_fcfmgnz_126d_slope_v039_signal,
    f32cf_f32_cash_flow_quality_ocfmgnz_21d_slope_v040_signal,
    f32cf_f32_cash_flow_quality_ocfmgnz_63d_slope_v041_signal,
    f32cf_f32_cash_flow_quality_ocfmgnz_126d_slope_v042_signal,
    f32cf_f32_cash_flow_quality_cashconvz_21d_slope_v043_signal,
    f32cf_f32_cash_flow_quality_cashconvz_63d_slope_v044_signal,
    f32cf_f32_cash_flow_quality_cashconvz_126d_slope_v045_signal,
    f32cf_f32_cash_flow_quality_capexintz_21d_slope_v046_signal,
    f32cf_f32_cash_flow_quality_capexintz_63d_slope_v047_signal,
    f32cf_f32_cash_flow_quality_capexintz_126d_slope_v048_signal,
    f32cf_f32_cash_flow_quality_fcfpsz_21d_slope_v049_signal,
    f32cf_f32_cash_flow_quality_fcfpsz_63d_slope_v050_signal,
    f32cf_f32_cash_flow_quality_fcfpsz_126d_slope_v051_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrank_21d_slope_v052_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrank_63d_slope_v053_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrank_126d_slope_v054_signal,
    f32cf_f32_cash_flow_quality_ocfmgnrank_21d_slope_v055_signal,
    f32cf_f32_cash_flow_quality_ocfmgnrank_63d_slope_v056_signal,
    f32cf_f32_cash_flow_quality_ocfmgnrank_126d_slope_v057_signal,
    f32cf_f32_cash_flow_quality_selffundrank_21d_slope_v058_signal,
    f32cf_f32_cash_flow_quality_selffundrank_63d_slope_v059_signal,
    f32cf_f32_cash_flow_quality_selffundrank_126d_slope_v060_signal,
    f32cf_f32_cash_flow_quality_fcfmgnvol_21d_slope_v061_signal,
    f32cf_f32_cash_flow_quality_fcfmgnvol_63d_slope_v062_signal,
    f32cf_f32_cash_flow_quality_fcfmgnvol_126d_slope_v063_signal,
    f32cf_f32_cash_flow_quality_ocfmgnvol_21d_slope_v064_signal,
    f32cf_f32_cash_flow_quality_ocfmgnvol_63d_slope_v065_signal,
    f32cf_f32_cash_flow_quality_ocfmgnvol_126d_slope_v066_signal,
    f32cf_f32_cash_flow_quality_convvol_21d_slope_v067_signal,
    f32cf_f32_cash_flow_quality_convvol_63d_slope_v068_signal,
    f32cf_f32_cash_flow_quality_convvol_126d_slope_v069_signal,
    f32cf_f32_cash_flow_quality_capexintvol_21d_slope_v070_signal,
    f32cf_f32_cash_flow_quality_capexintvol_63d_slope_v071_signal,
    f32cf_f32_cash_flow_quality_capexintvol_126d_slope_v072_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmed_21d_slope_v073_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmed_63d_slope_v074_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmed_126d_slope_v075_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmed_21d_slope_v076_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmed_63d_slope_v077_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmed_126d_slope_v078_signal,
    f32cf_f32_cash_flow_quality_netmgnvol_21d_slope_v079_signal,
    f32cf_f32_cash_flow_quality_netmgnvol_63d_slope_v080_signal,
    f32cf_f32_cash_flow_quality_netmgnvol_126d_slope_v081_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrng_21d_slope_v082_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrng_63d_slope_v083_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrng_126d_slope_v084_signal,
    f32cf_f32_cash_flow_quality_selffundrng_21d_slope_v085_signal,
    f32cf_f32_cash_flow_quality_selffundrng_63d_slope_v086_signal,
    f32cf_f32_cash_flow_quality_selffundrng_126d_slope_v087_signal,
    f32cf_f32_cash_flow_quality_fcfmgndd_21d_slope_v088_signal,
    f32cf_f32_cash_flow_quality_fcfmgndd_63d_slope_v089_signal,
    f32cf_f32_cash_flow_quality_fcfmgndd_126d_slope_v090_signal,
    f32cf_f32_cash_flow_quality_ocfmgndd_21d_slope_v091_signal,
    f32cf_f32_cash_flow_quality_ocfmgndd_63d_slope_v092_signal,
    f32cf_f32_cash_flow_quality_ocfmgndd_126d_slope_v093_signal,
    f32cf_f32_cash_flow_quality_fcfpsdd_21d_slope_v094_signal,
    f32cf_f32_cash_flow_quality_fcfpsdd_63d_slope_v095_signal,
    f32cf_f32_cash_flow_quality_fcfpsdd_126d_slope_v096_signal,
    f32cf_f32_cash_flow_quality_fcfmgnac_21d_slope_v097_signal,
    f32cf_f32_cash_flow_quality_fcfmgnac_63d_slope_v098_signal,
    f32cf_f32_cash_flow_quality_fcfmgnac_126d_slope_v099_signal,
    f32cf_f32_cash_flow_quality_ocfmgnac_21d_slope_v100_signal,
    f32cf_f32_cash_flow_quality_ocfmgnac_63d_slope_v101_signal,
    f32cf_f32_cash_flow_quality_ocfmgnac_126d_slope_v102_signal,
    f32cf_f32_cash_flow_quality_fcfncfocorr_21d_slope_v103_signal,
    f32cf_f32_cash_flow_quality_fcfncfocorr_63d_slope_v104_signal,
    f32cf_f32_cash_flow_quality_fcfncfocorr_126d_slope_v105_signal,
    f32cf_f32_cash_flow_quality_fcfcapexcorr_21d_slope_v106_signal,
    f32cf_f32_cash_flow_quality_fcfcapexcorr_63d_slope_v107_signal,
    f32cf_f32_cash_flow_quality_fcfcapexcorr_126d_slope_v108_signal,
    f32cf_f32_cash_flow_quality_ncfonetcorr_21d_slope_v109_signal,
    f32cf_f32_cash_flow_quality_ncfonetcorr_63d_slope_v110_signal,
    f32cf_f32_cash_flow_quality_ncfonetcorr_126d_slope_v111_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmacd_21d_slope_v112_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmacd_63d_slope_v113_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmacd_126d_slope_v114_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmacd_21d_slope_v115_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmacd_63d_slope_v116_signal,
    f32cf_f32_cash_flow_quality_ocfmgnmacd_126d_slope_v117_signal,
    f32cf_f32_cash_flow_quality_convmacd_21d_slope_v118_signal,
    f32cf_f32_cash_flow_quality_convmacd_63d_slope_v119_signal,
    f32cf_f32_cash_flow_quality_convmacd_126d_slope_v120_signal,
    f32cf_f32_cash_flow_quality_jointcash_21d_slope_v121_signal,
    f32cf_f32_cash_flow_quality_jointcash_63d_slope_v122_signal,
    f32cf_f32_cash_flow_quality_jointcash_126d_slope_v123_signal,
    f32cf_f32_cash_flow_quality_convxmgn_21d_slope_v124_signal,
    f32cf_f32_cash_flow_quality_convxmgn_63d_slope_v125_signal,
    f32cf_f32_cash_flow_quality_convxmgn_126d_slope_v126_signal,
    f32cf_f32_cash_flow_quality_fcfmgnskew_21d_slope_v127_signal,
    f32cf_f32_cash_flow_quality_fcfmgnskew_63d_slope_v128_signal,
    f32cf_f32_cash_flow_quality_fcfmgnskew_126d_slope_v129_signal,
    f32cf_f32_cash_flow_quality_convskew_21d_slope_v130_signal,
    f32cf_f32_cash_flow_quality_convskew_63d_slope_v131_signal,
    f32cf_f32_cash_flow_quality_convskew_126d_slope_v132_signal,
    f32cf_f32_cash_flow_quality_fcfsm_21d_slope_v133_signal,
    f32cf_f32_cash_flow_quality_fcfsm_63d_slope_v134_signal,
    f32cf_f32_cash_flow_quality_fcfsm_126d_slope_v135_signal,
    f32cf_f32_cash_flow_quality_ncfosm_21d_slope_v136_signal,
    f32cf_f32_cash_flow_quality_ncfosm_63d_slope_v137_signal,
    f32cf_f32_cash_flow_quality_ncfosm_126d_slope_v138_signal,
    f32cf_f32_cash_flow_quality_fcfmgndsd_21d_slope_v139_signal,
    f32cf_f32_cash_flow_quality_fcfmgndsd_63d_slope_v140_signal,
    f32cf_f32_cash_flow_quality_fcfmgndsd_126d_slope_v141_signal,
    f32cf_f32_cash_flow_quality_capexintrank_21d_slope_v142_signal,
    f32cf_f32_cash_flow_quality_capexintrank_63d_slope_v143_signal,
    f32cf_f32_cash_flow_quality_capexintrank_126d_slope_v144_signal,
    f32cf_f32_cash_flow_quality_selffundvol_21d_slope_v145_signal,
    f32cf_f32_cash_flow_quality_selffundvol_63d_slope_v146_signal,
    f32cf_f32_cash_flow_quality_selffundvol_126d_slope_v147_signal,
    f32cf_f32_cash_flow_quality_netmgnz_21d_slope_v148_signal,
    f32cf_f32_cash_flow_quality_netmgnz_63d_slope_v149_signal,
    f32cf_f32_cash_flow_quality_netmgnz_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F32_CASH_FLOW_QUALITY_REGISTRY_2ND_DERIVATIVES_001_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(1, base=5e8, drift=0.04, vol=0.06).rename("revenue")
    capex = _fund(2, base=4e7, drift=0.03, vol=0.10).rename("capex")
    fcf = _fund(3, base=6e7, drift=0.0, vol=0.34, allow_neg=True).rename("fcf")
    ncfo = _fund(7, base=9e7, drift=0.0, vol=0.34, allow_neg=True).rename("ncfo")
    netinc = _fund(5, base=5e7, drift=0.0, vol=0.34, allow_neg=True).rename("netinc")
    fcfps = _fund(10, base=2.0, drift=0.0, vol=0.34, allow_neg=True).rename("fcfps")

    cols = {
        "revenue": revenue, "capex": capex, "fcf": fcf, "ncfo": ncfo,
        "netinc": netinc, "fcfps": fcfps,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset" % (
            name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f32_cash_flow_quality_2nd_derivatives_001_150_claude: %d features pass" % n_features)
