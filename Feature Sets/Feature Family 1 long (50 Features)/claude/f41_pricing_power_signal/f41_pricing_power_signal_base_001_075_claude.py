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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f41_pricing_power_gpgrow(gp, w):
    return gp.pct_change(w)


def _f41_pricing_power_gprev(gp, revenue, w):
    gm = gp / revenue.replace(0, np.nan)
    return gm.diff(w)


def _f41_pricing_power_passthrough(gp, revenue, w):
    g_gp = gp.pct_change(w)
    g_rev = revenue.pct_change(w)
    return g_gp - g_rev


# 21d gross margin change × closeadj (gp/revenue trajectory)
def f41pps_f41_pricing_power_signal_gprev_21d_base_v001_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 21) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_63d_base_v002_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_126d_base_v003_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 126) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_252d_base_v004_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_504d_base_v005_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# 21d gross profit growth rate × closeadj
def f41pps_f41_pricing_power_signal_gpgrow_21d_base_v006_signal(gp, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 21)
    return (aux * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_63d_base_v007_signal(gp, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_126d_base_v008_signal(gp, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 126) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_252d_base_v009_signal(gp, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_504d_base_v010_signal(gp, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# 21d passthrough power: gp growth - revenue growth
def f41pps_f41_pricing_power_signal_passthrough_21d_base_v011_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 21) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_63d_base_v012_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_126d_base_v013_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 126) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_252d_base_v014_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_504d_base_v015_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of 63d gross margin change
def f41pps_f41_pricing_power_signal_gprevmean_252d_base_v016_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63)
    return (_mean(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmean_63d_base_v017_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (_mean(base, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d std of gp growth
def f41pps_f41_pricing_power_signal_gpgrowstd_252d_base_v018_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    return (_std(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowstd_63d_base_v019_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 5)
    return (_std(base, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d zscore of gp growth
def f41pps_f41_pricing_power_signal_gpgrowz_252d_base_v020_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    return (_z(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowz_504d_base_v021_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252)
    return (_z(base, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# zscores of gprev
def f41pps_f41_pricing_power_signal_gprevz_252d_base_v022_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (_z(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevz_504d_base_v023_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252)
    return (_z(base, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gross margin level × closeadj
def f41pps_f41_pricing_power_signal_gmlevel_252d_base_v024_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmlevel_63d_base_v025_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 21d gp growth × revenue level (notional)
def f41pps_f41_pricing_power_signal_gpgrowxrev_21d_base_v026_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 21) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrev_252d_base_v027_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gprev × revenue
def f41pps_f41_pricing_power_signal_gprevxrev_252d_base_v028_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxrev_63d_base_v029_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# passthrough × revenue
def f41pps_f41_pricing_power_signal_passthroughxrev_252d_base_v030_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthroughxrev_63d_base_v031_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 63) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × eps
def f41pps_f41_pricing_power_signal_gpgrowxeps_252d_base_v032_signal(gp, eps, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * eps * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxeps_63d_base_v033_signal(gp, eps, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * eps * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp/assets ratio change (asset-light pricing)
def f41pps_f41_pricing_power_signal_gpassets_252d_base_v034_signal(gp, assets, closeadj):
    ratio = gp / assets.replace(0, np.nan)
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    return ((_mean(ratio, 252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpassets_63d_base_v035_signal(gp, assets, closeadj):
    ratio = gp / assets.replace(0, np.nan)
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    return ((_mean(ratio, 63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d EMA of gprev
def f41pps_f41_pricing_power_signal_gprevema_252d_base_v036_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.ewm(span=252, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevema_63d_base_v037_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.ewm(span=63, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d EMA of gp growth
def f41pps_f41_pricing_power_signal_gpgrowema_252d_base_v038_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    return (base.ewm(span=252, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowema_63d_base_v039_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 5)
    return (base.ewm(span=63, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d expanding mean of gprev (long-run pricing power)
def f41pps_f41_pricing_power_signal_gprevexp_base_v040_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.expanding(min_periods=63).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d expanding zscore of gprev
def f41pps_f41_pricing_power_signal_gprevexpz_base_v041_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    m = base.expanding(min_periods=63).mean()
    sd = base.expanding(min_periods=63).std().replace(0, np.nan)
    return ((base - m) / sd * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d positive gprev frequency
def f41pps_f41_pricing_power_signal_gprevposfreq_252d_base_v042_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0).astype(float)
    return (pos.rolling(252, min_periods=63).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevposfreq_504d_base_v043_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0).astype(float)
    return (pos.rolling(504, min_periods=126).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d sum of gprev (cumulative margin expansion)
def f41pps_f41_pricing_power_signal_gprevsum_252d_base_v044_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsum_504d_base_v045_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsum_63d_base_v046_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 5)
    return (base.rolling(63, min_periods=21).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × debt growth (price power vs leverage)
def f41pps_f41_pricing_power_signal_gpgrowxdebt_252d_base_v047_signal(gp, debt, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * debt.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxdebt_63d_base_v048_signal(gp, debt, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * debt.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × ebitda growth
def f41pps_f41_pricing_power_signal_gprevxebgrow_252d_base_v049_signal(gp, revenue, ebitda, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * ebitda.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxebgrow_63d_base_v050_signal(gp, revenue, ebitda, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * ebitda.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × marketcap proxy (priceable scale)
def f41pps_f41_pricing_power_signal_gpgrowxmc_252d_base_v051_signal(gp, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    return (_f41_pricing_power_gpgrow(gp, 252) * closeadj / mc * gp).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxmc_63d_base_v052_signal(gp, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    return (_f41_pricing_power_gpgrow(gp, 63) * closeadj / mc * gp).replace([np.inf, -np.inf], np.nan)


# 252d gross margin × ebitda
def f41pps_f41_pricing_power_signal_gmxebitda_252d_base_v053_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * ebitda * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxebitda_63d_base_v054_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * ebitda * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp growth - opex growth (cost passthrough)
def f41pps_f41_pricing_power_signal_costpass_252d_base_v055_signal(gp, opinc, revenue, closeadj):
    opex = (revenue - opinc).abs()
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    return ((gp.pct_change(252) - opex.pct_change(252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_costpass_63d_base_v056_signal(gp, opinc, revenue, closeadj):
    opex = (revenue - opinc).abs()
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    return ((gp.pct_change(63) - opex.pct_change(63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × current ratio
def f41pps_f41_pricing_power_signal_gpgrowxcr_252d_base_v057_signal(gp, currentratio, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * currentratio * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxcr_63d_base_v058_signal(gp, currentratio, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * currentratio * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × eps growth
def f41pps_f41_pricing_power_signal_gprevxepsg_252d_base_v059_signal(gp, revenue, eps, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * eps.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxepsg_63d_base_v060_signal(gp, revenue, eps, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * eps.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × ncfo level
def f41pps_f41_pricing_power_signal_gpgrowxncfo_252d_base_v061_signal(gp, ncfo, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * ncfo * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxncfo_63d_base_v062_signal(gp, ncfo, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * ncfo * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × fcf level
def f41pps_f41_pricing_power_signal_gpgrowxfcf_252d_base_v063_signal(gp, fcf, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * fcf * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxfcf_63d_base_v064_signal(gp, fcf, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * fcf * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gross margin × revenue × closeadj (pricing scale)
def f41pps_f41_pricing_power_signal_gmxrevscale_252d_base_v065_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxrevscale_63d_base_v066_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d composite: gp growth × revenue growth (compounding pricing)
def f41pps_f41_pricing_power_signal_compoundprice_252d_base_v067_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * revenue.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_compoundprice_63d_base_v068_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * revenue.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev signed magnitude
def f41pps_f41_pricing_power_signal_gprevsignmag_252d_base_v069_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252)
    return (np.sign(base) * base.abs() * closeadj * revenue / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsignmag_63d_base_v070_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63)
    return (np.sign(base) * base.abs() * closeadj * revenue / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gprev SNR
def f41pps_f41_pricing_power_signal_gprevsnr_252d_base_v071_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    sd = _std(base, 252).replace(0, np.nan)
    return (_mean(base, 63) / sd * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsnr_504d_base_v072_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    sd = _std(base, 504).replace(0, np.nan)
    return (_mean(base, 252) / sd * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d composite: gp/revenue × revenue growth × ebitda
def f41pps_f41_pricing_power_signal_megacomposite_252d_base_v073_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * revenue.pct_change(252).fillna(0.0) * ebitda * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d composite: passthrough × eps × revenue
def f41pps_f41_pricing_power_signal_passcomposite_252d_base_v074_signal(gp, revenue, eps, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * eps * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d ultimate: gprev mean × revenue level × eps growth
def f41pps_f41_pricing_power_signal_ultimate_252d_base_v075_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (_mean(base, 252) * revenue * eps.pct_change(252).fillna(0.0) * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41pps_f41_pricing_power_signal_gprev_21d_base_v001_signal,
    f41pps_f41_pricing_power_signal_gprev_63d_base_v002_signal,
    f41pps_f41_pricing_power_signal_gprev_126d_base_v003_signal,
    f41pps_f41_pricing_power_signal_gprev_252d_base_v004_signal,
    f41pps_f41_pricing_power_signal_gprev_504d_base_v005_signal,
    f41pps_f41_pricing_power_signal_gpgrow_21d_base_v006_signal,
    f41pps_f41_pricing_power_signal_gpgrow_63d_base_v007_signal,
    f41pps_f41_pricing_power_signal_gpgrow_126d_base_v008_signal,
    f41pps_f41_pricing_power_signal_gpgrow_252d_base_v009_signal,
    f41pps_f41_pricing_power_signal_gpgrow_504d_base_v010_signal,
    f41pps_f41_pricing_power_signal_passthrough_21d_base_v011_signal,
    f41pps_f41_pricing_power_signal_passthrough_63d_base_v012_signal,
    f41pps_f41_pricing_power_signal_passthrough_126d_base_v013_signal,
    f41pps_f41_pricing_power_signal_passthrough_252d_base_v014_signal,
    f41pps_f41_pricing_power_signal_passthrough_504d_base_v015_signal,
    f41pps_f41_pricing_power_signal_gprevmean_252d_base_v016_signal,
    f41pps_f41_pricing_power_signal_gprevmean_63d_base_v017_signal,
    f41pps_f41_pricing_power_signal_gpgrowstd_252d_base_v018_signal,
    f41pps_f41_pricing_power_signal_gpgrowstd_63d_base_v019_signal,
    f41pps_f41_pricing_power_signal_gpgrowz_252d_base_v020_signal,
    f41pps_f41_pricing_power_signal_gpgrowz_504d_base_v021_signal,
    f41pps_f41_pricing_power_signal_gprevz_252d_base_v022_signal,
    f41pps_f41_pricing_power_signal_gprevz_504d_base_v023_signal,
    f41pps_f41_pricing_power_signal_gmlevel_252d_base_v024_signal,
    f41pps_f41_pricing_power_signal_gmlevel_63d_base_v025_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrev_21d_base_v026_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrev_252d_base_v027_signal,
    f41pps_f41_pricing_power_signal_gprevxrev_252d_base_v028_signal,
    f41pps_f41_pricing_power_signal_gprevxrev_63d_base_v029_signal,
    f41pps_f41_pricing_power_signal_passthroughxrev_252d_base_v030_signal,
    f41pps_f41_pricing_power_signal_passthroughxrev_63d_base_v031_signal,
    f41pps_f41_pricing_power_signal_gpgrowxeps_252d_base_v032_signal,
    f41pps_f41_pricing_power_signal_gpgrowxeps_63d_base_v033_signal,
    f41pps_f41_pricing_power_signal_gpassets_252d_base_v034_signal,
    f41pps_f41_pricing_power_signal_gpassets_63d_base_v035_signal,
    f41pps_f41_pricing_power_signal_gprevema_252d_base_v036_signal,
    f41pps_f41_pricing_power_signal_gprevema_63d_base_v037_signal,
    f41pps_f41_pricing_power_signal_gpgrowema_252d_base_v038_signal,
    f41pps_f41_pricing_power_signal_gpgrowema_63d_base_v039_signal,
    f41pps_f41_pricing_power_signal_gprevexp_base_v040_signal,
    f41pps_f41_pricing_power_signal_gprevexpz_base_v041_signal,
    f41pps_f41_pricing_power_signal_gprevposfreq_252d_base_v042_signal,
    f41pps_f41_pricing_power_signal_gprevposfreq_504d_base_v043_signal,
    f41pps_f41_pricing_power_signal_gprevsum_252d_base_v044_signal,
    f41pps_f41_pricing_power_signal_gprevsum_504d_base_v045_signal,
    f41pps_f41_pricing_power_signal_gprevsum_63d_base_v046_signal,
    f41pps_f41_pricing_power_signal_gpgrowxdebt_252d_base_v047_signal,
    f41pps_f41_pricing_power_signal_gpgrowxdebt_63d_base_v048_signal,
    f41pps_f41_pricing_power_signal_gprevxebgrow_252d_base_v049_signal,
    f41pps_f41_pricing_power_signal_gprevxebgrow_63d_base_v050_signal,
    f41pps_f41_pricing_power_signal_gpgrowxmc_252d_base_v051_signal,
    f41pps_f41_pricing_power_signal_gpgrowxmc_63d_base_v052_signal,
    f41pps_f41_pricing_power_signal_gmxebitda_252d_base_v053_signal,
    f41pps_f41_pricing_power_signal_gmxebitda_63d_base_v054_signal,
    f41pps_f41_pricing_power_signal_costpass_252d_base_v055_signal,
    f41pps_f41_pricing_power_signal_costpass_63d_base_v056_signal,
    f41pps_f41_pricing_power_signal_gpgrowxcr_252d_base_v057_signal,
    f41pps_f41_pricing_power_signal_gpgrowxcr_63d_base_v058_signal,
    f41pps_f41_pricing_power_signal_gprevxepsg_252d_base_v059_signal,
    f41pps_f41_pricing_power_signal_gprevxepsg_63d_base_v060_signal,
    f41pps_f41_pricing_power_signal_gpgrowxncfo_252d_base_v061_signal,
    f41pps_f41_pricing_power_signal_gpgrowxncfo_63d_base_v062_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcf_252d_base_v063_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcf_63d_base_v064_signal,
    f41pps_f41_pricing_power_signal_gmxrevscale_252d_base_v065_signal,
    f41pps_f41_pricing_power_signal_gmxrevscale_63d_base_v066_signal,
    f41pps_f41_pricing_power_signal_compoundprice_252d_base_v067_signal,
    f41pps_f41_pricing_power_signal_compoundprice_63d_base_v068_signal,
    f41pps_f41_pricing_power_signal_gprevsignmag_252d_base_v069_signal,
    f41pps_f41_pricing_power_signal_gprevsignmag_63d_base_v070_signal,
    f41pps_f41_pricing_power_signal_gprevsnr_252d_base_v071_signal,
    f41pps_f41_pricing_power_signal_gprevsnr_504d_base_v072_signal,
    f41pps_f41_pricing_power_signal_megacomposite_252d_base_v073_signal,
    f41pps_f41_pricing_power_signal_passcomposite_252d_base_v074_signal,
    f41pps_f41_pricing_power_signal_ultimate_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_PRICING_POWER_SIGNAL_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp = pd.Series(4.0e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))), name="gp")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "gp": gp, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "currentratio": currentratio, "fcf": fcf, "ncfo": ncfo, "sharesbas": sharesbas,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_pricing_power",)
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
    print(f"OK f41_pricing_power_signal_base_001_075_claude: {n_features} features pass")
