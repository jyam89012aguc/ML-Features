import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    # discrete first derivative over horizon w (rate of change per day)
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (working-capital dynamics) =====
def _f20_dso(receivables, revenue, w):
    rev_day = revenue.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return receivables / rev_day.replace(0, np.nan)


def _f20_dio(inventory, cor, w):
    cor_day = cor.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return inventory / cor_day.replace(0, np.nan)


def _f20_dpo(payables, cor, w):
    cor_day = cor.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return payables / cor_day.replace(0, np.nan)


def _f20_ccc(receivables, inventory, payables, revenue, cor, w):
    return (_f20_dso(receivables, revenue, w)
            + _f20_dio(inventory, cor, w)
            - _f20_dpo(payables, cor, w))


def _f20_wc(assetsc, liabilitiesc):
    return assetsc - liabilitiesc


def _f20_recratio(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


def _f20_invratio(inventory, cor):
    return inventory / cor.replace(0, np.nan)


def _f20_payratio(payables, cor):
    return payables / cor.replace(0, np.nan)


# ============================================================
# slope (1st math derivative) features
# ============================================================

# slope of DSO over 21d horizon (collection-period velocity)
def f20wc_f20_working_capital_dynamics_dso_21d_slope_v001_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _roc(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO over 63d horizon
def f20wc_f20_working_capital_dynamics_dso_63d_slope_v002_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO over 21d horizon (inventory-days velocity)
def f20wc_f20_working_capital_dynamics_dio_21d_slope_v003_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _roc(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO over 63d horizon
def f20wc_f20_working_capital_dynamics_dio_63d_slope_v004_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO over 21d horizon (payment-stretch velocity)
def f20wc_f20_working_capital_dynamics_dpo_21d_slope_v005_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _roc(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO over 63d horizon
def f20wc_f20_working_capital_dynamics_dpo_63d_slope_v006_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCC over 21d horizon (cash-cycle velocity)
def f20wc_f20_working_capital_dynamics_ccc_21d_slope_v007_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _roc(c, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCC over 63d horizon
def f20wc_f20_working_capital_dynamics_ccc_63d_slope_v008_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _roc(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating cycle (DSO+DIO) over 63d
def f20wc_f20_working_capital_dynamics_opcyc_63d_slope_v009_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _roc(op, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables/revenue intensity over 21d
def f20wc_f20_working_capital_dynamics_recrev_21d_slope_v010_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables/revenue intensity over 63d
def f20wc_f20_working_capital_dynamics_recrev_63d_slope_v011_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory/cor intensity over 21d
def f20wc_f20_working_capital_dynamics_invcor_21d_slope_v012_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory/cor intensity over 63d
def f20wc_f20_working_capital_dynamics_invcor_63d_slope_v013_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of payables/cor intensity over 63d
def f20wc_f20_working_capital_dynamics_paycor_63d_slope_v014_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of working-capital intensity (WC/revenue) over 63d
def f20wc_f20_working_capital_dynamics_wcint_63d_slope_v015_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _roc(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over 21d
def f20wc_f20_working_capital_dynamics_curratio_21d_slope_v016_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _roc(cr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over 63d
def f20wc_f20_working_capital_dynamics_curratio_63d_slope_v017_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _roc(cr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-ratio velocity convergence: short vs long-horizon velocity (inventory-stripped liquidity)
def f20wc_f20_working_capital_dynamics_quick_63d_slope_v018_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _roc(q, 21) - _roc(q, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-trade-WC intensity over 63d
def f20wc_f20_working_capital_dynamics_nowc_63d_slope_v019_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    b = _roc(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables share of current assets over 63d
def f20wc_f20_working_capital_dynamics_recshare_63d_slope_v020_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _roc(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory share of current assets over 63d
def f20wc_f20_working_capital_dynamics_invshare_63d_slope_v021_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _roc(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of payables share of current liabilities over 63d
def f20wc_f20_working_capital_dynamics_payshare_63d_slope_v022_signal(payables, liabilitiesc):
    share = payables / liabilitiesc.replace(0, np.nan)
    b = _roc(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables-to-payables trade balance over 63d
def f20wc_f20_working_capital_dynamics_recpay_63d_slope_v023_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-payables coverage over 63d
def f20wc_f20_working_capital_dynamics_invpay_63d_slope_v024_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO-minus-DPO net financing days over 63d
def f20wc_f20_working_capital_dynamics_dsodpo_63d_slope_v025_signal(receivables, payables, revenue, cor):
    net = _f20_dso(receivables, revenue, 252) - _f20_dpo(payables, cor, 252)
    b = _roc(net, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of DSO over 21d (standardized collection velocity)
def f20wc_f20_working_capital_dynamics_dsoz_21d_slope_v026_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    sl = _roc(d, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of DIO over 21d
def f20wc_f20_working_capital_dynamics_dioz_21d_slope_v027_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    sl = _roc(d, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of DPO over 21d
def f20wc_f20_working_capital_dynamics_dpoz_21d_slope_v028_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    sl = _roc(d, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of CCC over 63d
def f20wc_f20_working_capital_dynamics_cccz_63d_slope_v029_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    sl = _roc(c, 63)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DSO slope vs 504d history
def f20wc_f20_working_capital_dynamics_dsorank_63d_slope_v030_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    sl = _roc(d, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DIO slope vs 504d history
def f20wc_f20_working_capital_dynamics_diorank_63d_slope_v031_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    sl = _roc(d, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of CCC slope vs 504d history
def f20wc_f20_working_capital_dynamics_cccrank_63d_slope_v032_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    sl = _roc(c, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO slope risk-adjusted by DSO dispersion (velocity per unit volatility)
def f20wc_f20_working_capital_dynamics_dsora_63d_slope_v033_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    sl = _roc(d, 63)
    b = sl / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO slope risk-adjusted by DIO dispersion
def f20wc_f20_working_capital_dynamics_diora_63d_slope_v034_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    sl = _roc(d, 63)
    b = sl / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO slope risk-adjusted by DPO dispersion
def f20wc_f20_working_capital_dynamics_dpora_63d_slope_v035_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    sl = _roc(d, 63)
    b = sl / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded slope of CCC over 63d (squashed cycle velocity)
def f20wc_f20_working_capital_dynamics_ccctanh_63d_slope_v036_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    sl = _roc(c, 63)
    b = np.tanh(sl * 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-intensity velocity dispersion (collection-trajectory volatility)
def f20wc_f20_working_capital_dynamics_recrevtanh_21d_slope_v037_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    sl = _roc(r, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of DSO slope (signed collection velocity)
def f20wc_f20_working_capital_dynamics_dsosm_63d_slope_v038_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    sl = _roc(d, 63)
    b = np.sign(sl) * (sl.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of DIO slope
def f20wc_f20_working_capital_dynamics_diosm_63d_slope_v039_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    sl = _roc(d, 63)
    b = np.sign(sl) * (sl.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO smoothed by EMA before differencing (denoised velocity)
def f20wc_f20_working_capital_dynamics_dsoema_63d_slope_v040_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63).ewm(span=42, min_periods=21).mean()
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO smoothed by EMA before differencing
def f20wc_f20_working_capital_dynamics_dioema_63d_slope_v041_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO smoothed by EMA before differencing
def f20wc_f20_working_capital_dynamics_dpoema_63d_slope_v042_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _roc(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-receivables composition over 63d
def f20wc_f20_working_capital_dynamics_invrec_63d_slope_v043_signal(inventory, receivables):
    r = inventory / receivables.replace(0, np.nan)
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-to-receivables composition acceleration (supplier-vs-customer 2nd order)
def f20wc_f20_working_capital_dynamics_payrec_63d_slope_v044_signal(payables, receivables):
    r = payables / receivables.replace(0, np.nan)
    sl = _roc(r, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-cushion (WC/current assets) velocity dispersion (liquidity-buffer-velocity volatility)
def f20wc_f20_working_capital_dynamics_wccush_63d_slope_v045_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    cush = wc / assetsc.replace(0, np.nan)
    sl = _roc(cush, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO-to-DIO balance over 63d
def f20wc_f20_working_capital_dynamics_dsodiobal_63d_slope_v046_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    dio = _f20_dio(inventory, cor, 252)
    bal = (dso - dio) / (dso + dio).replace(0, np.nan)
    b = _roc(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO coverage of operating cycle over 63d
def f20wc_f20_working_capital_dynamics_dpocover_63d_slope_v047_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    cover = dpo / op.replace(0, np.nan)
    b = _roc(cover, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables/revenue intensity over 126d (long-horizon collection drift)
def f20wc_f20_working_capital_dynamics_recrev_126d_slope_v048_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _roc(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory/cor intensity over 126d
def f20wc_f20_working_capital_dynamics_invcor_126d_slope_v049_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _roc(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCC over 126d (long-horizon cycle drift)
def f20wc_f20_working_capital_dynamics_ccc_126d_slope_v050_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _roc(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of current-asset level over 63d (liquidity-base velocity)
def f20wc_f20_working_capital_dynamics_ca_63d_slope_v051_signal(assetsc):
    lg = np.log(assetsc.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of current-liability level over 63d
def f20wc_f20_working_capital_dynamics_cl_63d_slope_v052_signal(liabilitiesc):
    lg = np.log(liabilitiesc.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-receivables over 63d (receivables growth velocity)
def f20wc_f20_working_capital_dynamics_rec_63d_slope_v053_signal(receivables):
    lg = np.log(receivables.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-inventory over 63d (inventory growth velocity)
def f20wc_f20_working_capital_dynamics_inv_63d_slope_v054_signal(inventory):
    lg = np.log(inventory.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-payables over 63d (payables growth velocity)
def f20wc_f20_working_capital_dynamics_pay_63d_slope_v055_signal(payables):
    lg = np.log(payables.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-velocity vs revenue-velocity, z-blended ACCELERATION spread (collection-vs-sales 2nd order)
def f20wc_f20_working_capital_dynamics_dsorev_63d_slope_v056_signal(receivables, revenue):
    rg = _roc(np.log(receivables.replace(0, np.nan)), 63)
    sg = _roc(np.log(revenue.replace(0, np.nan)), 63)
    spread = rg - sg
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-velocity vs cor-velocity acceleration spread (build-vs-demand 2nd order)
def f20wc_f20_working_capital_dynamics_invcorvel_63d_slope_v057_signal(inventory, cor):
    ig = _roc(np.log(inventory.replace(0, np.nan)), 63)
    cg = _roc(np.log(cor.replace(0, np.nan)), 63)
    spread = ig - cg
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-velocity vs cor-velocity acceleration spread (supplier-financing 2nd order)
def f20wc_f20_working_capital_dynamics_paycorvel_63d_slope_v058_signal(payables, cor):
    pg = _roc(np.log(payables.replace(0, np.nan)), 63)
    cg = _roc(np.log(cor.replace(0, np.nan)), 63)
    spread = pg - cg
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-trade-WC over current assets over 63d
def f20wc_f20_working_capital_dynamics_nowcca_63d_slope_v059_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    ratio = nowc / assetsc.replace(0, np.nan)
    b = _roc(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating cycle over 21d (short-horizon cycle velocity)
def f20wc_f20_working_capital_dynamics_opcyc_21d_slope_v060_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _roc(op, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of working-capital intensity over 63d
def f20wc_f20_working_capital_dynamics_wcintz_63d_slope_v061_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    sl = _roc(ratio, 63)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC velocity acceleration over 126d horizon (multi-year cycle 2nd order)
def f20wc_f20_working_capital_dynamics_cccrank_126d_slope_v062_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    sl = _roc(c, 126)
    b = sl - sl.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity dispersion (volatility of collection velocity over 252d)
def f20wc_f20_working_capital_dynamics_dsoveldisp_63d_slope_v063_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    sl = _roc(d, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO velocity dispersion
def f20wc_f20_working_capital_dynamics_dioveldisp_63d_slope_v064_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    sl = _roc(d, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC velocity dispersion
def f20wc_f20_working_capital_dynamics_cccveldisp_63d_slope_v065_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    sl = _roc(c, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables/revenue minus slope of inventory/cor (intensity-velocity spread)
def f20wc_f20_working_capital_dynamics_recinvvel_63d_slope_v066_signal(receivables, inventory, revenue, cor):
    rv = _roc(_f20_recratio(receivables, revenue), 63)
    iv = _roc(_f20_invratio(inventory, cor), 63)
    b = _z(rv, 252) - _z(iv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO intensity minus slope of DIO intensity (supplier-vs-stock velocity)
def f20wc_f20_working_capital_dynamics_paydiovel_63d_slope_v067_signal(payables, inventory, cor):
    pv = _roc(_f20_payratio(payables, cor), 63)
    iv = _roc(_f20_invratio(inventory, cor), 63)
    b = _z(pv, 252) - _z(iv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trade-balance (receivables/payables) over 21d
def f20wc_f20_working_capital_dynamics_recpay_21d_slope_v068_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-trade-WC over current liabilities over 63d
def f20wc_f20_working_capital_dynamics_nowcliab_63d_slope_v069_signal(receivables, inventory, payables, liabilitiesc):
    nowc = receivables + inventory - payables
    ratio = nowc / liabilitiesc.replace(0, np.nan)
    b = _roc(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-over-liabilities velocity ranked vs 504d history (current-surplus-velocity positioning)
def f20wc_f20_working_capital_dynamics_wcliab_63d_slope_v070_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / liabilitiesc.replace(0, np.nan)
    sl = _roc(ratio, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO over 5d horizon (high-frequency collection velocity)
def f20wc_f20_working_capital_dynamics_dso_5d_slope_v071_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = _roc(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO over 5d horizon (high-frequency build velocity)
def f20wc_f20_working_capital_dynamics_dio_5d_slope_v072_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = _roc(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO over 5d horizon
def f20wc_f20_working_capital_dynamics_dpo_5d_slope_v073_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    b = _roc(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCC over 5d horizon (high-frequency cycle velocity)
def f20wc_f20_working_capital_dynamics_ccc_5d_slope_v074_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = _roc(c, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over 5d
def f20wc_f20_working_capital_dynamics_curratio_5d_slope_v075_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _roc(cr, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables intensity over 5d
def f20wc_f20_working_capital_dynamics_recrev_5d_slope_v076_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _roc(r, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory intensity over 5d
def f20wc_f20_working_capital_dynamics_invcor_5d_slope_v077_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _roc(r, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of payables intensity over 21d
def f20wc_f20_working_capital_dynamics_paycor_21d_slope_v078_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables share over 21d
def f20wc_f20_working_capital_dynamics_recshare_21d_slope_v079_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _roc(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory share over 21d
def f20wc_f20_working_capital_dynamics_invshare_21d_slope_v080_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _roc(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of current ratio over 63d
def f20wc_f20_working_capital_dynamics_curratioz_63d_slope_v081_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    sl = _roc(cr, 63)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of quick ratio over 63d
def f20wc_f20_working_capital_dynamics_quickz_63d_slope_v082_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    sl = _roc(q, 63)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of net-trade-WC intensity over 63d
def f20wc_f20_working_capital_dynamics_nowcz_63d_slope_v083_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    sl = _roc(ratio, 63)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of receivables-intensity slope over 504d
def f20wc_f20_working_capital_dynamics_recrevrank_63d_slope_v084_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    sl = _roc(r, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of inventory-intensity slope over 504d
def f20wc_f20_working_capital_dynamics_invrank_63d_slope_v085_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    sl = _roc(r, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of payables-intensity slope over 504d
def f20wc_f20_working_capital_dynamics_payrank_63d_slope_v086_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    sl = _roc(r, 63)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing-days velocity, risk-adjusted by CCC dispersion (standardized net velocity)
def f20wc_f20_working_capital_dynamics_dsodpovel_63d_slope_v087_signal(receivables, inventory, payables, revenue, cor):
    net = _f20_dso(receivables, revenue, 252) - _f20_dpo(payables, cor, 252)
    sl = _roc(net, 63)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = sl / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO slope minus DPO slope (inventory financing-gap velocity)
def f20wc_f20_working_capital_dynamics_diodpovel_63d_slope_v088_signal(inventory, payables, cor):
    isl = _roc(_f20_dio(inventory, cor, 252), 63)
    psl = _roc(_f20_dpo(payables, cor, 252), 63)
    b = isl - psl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-payables coverage over 21d
def f20wc_f20_working_capital_dynamics_invpay_21d_slope_v089_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-cushion velocity convergence: short vs long-horizon (liquidity-buffer 2nd order)
def f20wc_f20_working_capital_dynamics_wccush_21d_slope_v090_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    cush = wc / assetsc.replace(0, np.nan)
    b = _roc(cush, 21) - _roc(cush, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity oscillation: 21d velocity minus its own slow EMA (collection-velocity noise)
def f20wc_f20_working_capital_dynamics_dsotanh_21d_slope_v091_signal(receivables, revenue):
    sl = _roc(_f20_dso(receivables, revenue, 63), 21)
    b = sl - sl.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO velocity oscillation: 21d velocity minus its own slow EMA (build-velocity noise)
def f20wc_f20_working_capital_dynamics_diotanh_21d_slope_v092_signal(inventory, cor):
    sl = _roc(_f20_dio(inventory, cor, 63), 21)
    b = sl - sl.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC velocity dispersion ratio: short-window velocity vol vs long-window velocity vol
def f20wc_f20_working_capital_dynamics_cccsm_63d_slope_v093_signal(receivables, inventory, payables, revenue, cor):
    sl = _roc(_f20_ccc(receivables, inventory, payables, revenue, cor, 63), 21)
    b = _std(sl, 63) / _std(sl, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO velocity dispersion ratio: short-window velocity vol vs long-window velocity vol
def f20wc_f20_working_capital_dynamics_dposm_63d_slope_v094_signal(payables, cor):
    sl = _roc(_f20_dpo(payables, cor, 63), 21)
    b = _std(sl, 63) / _std(sl, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed CCC over 63d (denoised cycle velocity)
def f20wc_f20_working_capital_dynamics_cccema_63d_slope_v095_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _roc(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed receivables intensity over 63d
def f20wc_f20_working_capital_dynamics_recrevema_63d_slope_v096_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue).ewm(span=42, min_periods=21).mean()
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-receivables composition over 21d
def f20wc_f20_working_capital_dynamics_invrec_21d_slope_v097_signal(inventory, receivables):
    r = inventory / receivables.replace(0, np.nan)
    b = _roc(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-to-receivables composition velocity dispersion (trade-mix-velocity volatility)
def f20wc_f20_working_capital_dynamics_payrec_21d_slope_v098_signal(payables, receivables):
    r = payables / receivables.replace(0, np.nan)
    sl = _roc(r, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity vs DPO velocity interaction (collection-vs-payment velocity product sign)
def f20wc_f20_working_capital_dynamics_dsocush_63d_slope_v099_signal(receivables, payables, revenue, cor):
    dsl = _z(_roc(_f20_dso(receivables, revenue, 252), 63), 252)
    psl = _z(_roc(_f20_dpo(payables, cor, 252), 63), 252)
    b = dsl * psl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC velocity scaled by WC intensity (cash-tie-up-weighted cycle velocity)
def f20wc_f20_working_capital_dynamics_cccwc_63d_slope_v100_signal(receivables, inventory, payables, revenue, cor, assetsc, liabilitiesc):
    sl = _roc(_f20_ccc(receivables, inventory, payables, revenue, cor, 252), 63)
    wc = _f20_wc(assetsc, liabilitiesc)
    wint = wc / revenue.replace(0, np.nan)
    b = _z(sl, 252) * _z(wint, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-net-trade-WC velocity dispersion (productivity-velocity volatility)
def f20wc_f20_working_capital_dynamics_revnowc_63d_slope_v101_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    prod = revenue / nowc.replace(0, np.nan)
    sl = _roc(prod, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover (cor/inventory) velocity convergence: short vs long horizon
def f20wc_f20_working_capital_dynamics_invturn_63d_slope_v102_signal(cor, inventory):
    t = cor / inventory.replace(0, np.nan)
    b = _roc(t, 21) - _roc(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-turnover (revenue/receivables) velocity convergence: short vs long horizon
def f20wc_f20_working_capital_dynamics_recturn_63d_slope_v103_signal(revenue, receivables):
    t = revenue / receivables.replace(0, np.nan)
    b = _roc(t, 21) - _roc(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-turnover (cor/payables) velocity convergence: short vs long horizon
def f20wc_f20_working_capital_dynamics_payturn_63d_slope_v104_signal(cor, payables):
    t = cor / payables.replace(0, np.nan)
    b = _roc(t, 21) - _roc(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-turnover (revenue/WC) velocity dispersion (capital-productivity-velocity volatility)
def f20wc_f20_working_capital_dynamics_wcturn_126d_slope_v105_signal(revenue, assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    t = revenue / wc.replace(0, np.nan)
    sl = _roc(t, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO over 126d, risk-adjusted by DSO dispersion
def f20wc_f20_working_capital_dynamics_dsora_126d_slope_v106_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    sl = _roc(d, 126)
    b = sl / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO over 126d, risk-adjusted
def f20wc_f20_working_capital_dynamics_diora_126d_slope_v107_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    sl = _roc(d, 126)
    b = sl / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity acceleration (collection-velocity 2nd order, 21d roc differenced)
def f20wc_f20_working_capital_dynamics_dsorank_21d_slope_v108_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    sl = _roc(d, 21)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DIO velocity over 252d
def f20wc_f20_working_capital_dynamics_diorank_21d_slope_v109_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    sl = _roc(d, 21)
    b = _rank(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DPO velocity over 252d
def f20wc_f20_working_capital_dynamics_dporank_21d_slope_v110_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    sl = _roc(d, 21)
    b = _rank(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating cycle over 126d
def f20wc_f20_working_capital_dynamics_opcyc_126d_slope_v111_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _roc(op, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO-share-of-CCC over 63d
def f20wc_f20_working_capital_dynamics_dsoshare_63d_slope_v112_signal(receivables, inventory, payables, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    share = dso / c.replace(0, np.nan)
    b = _roc(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO-vs-DPO financing-balance acceleration (self-financing-of-stock 2nd order)
def f20wc_f20_working_capital_dynamics_diodpobal_63d_slope_v113_signal(inventory, payables, cor):
    dio = _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    bal = (dio - dpo) / (dio + dpo).replace(0, np.nan)
    sl = _roc(bal, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset rotation acceleration: receivables-share-minus-inventory-share velocity, differenced
def f20wc_f20_working_capital_dynamics_recinvshare_63d_slope_v114_signal(receivables, inventory, assetsc):
    rs = receivables / assetsc.replace(0, np.nan)
    isr = inventory / assetsc.replace(0, np.nan)
    spread = _roc(rs, 63) - _roc(isr, 63)
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of defensive interval (liquid current assets / per-day cor) over 63d
def f20wc_f20_working_capital_dynamics_definterval_63d_slope_v115_signal(receivables, assetsc, inventory, cor):
    liquid = receivables + (assetsc - inventory)
    cor_day = _mean(cor, 252) / 91.0
    di = liquid / cor_day.replace(0, np.nan)
    b = _roc(di, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-cor over 63d (demand velocity, working-capital denominator)
def f20wc_f20_working_capital_dynamics_cor_63d_slope_v116_signal(cor):
    lg = np.log(cor.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-revenue over 63d (sales velocity, collection denominator)
def f20wc_f20_working_capital_dynamics_rev_63d_slope_v117_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    b = _roc(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity convergence: short-horizon velocity minus long-horizon velocity
def f20wc_f20_working_capital_dynamics_dsorel_21d_slope_v118_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _roc(d, 21) - _roc(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO velocity convergence: short-horizon velocity minus long-horizon velocity
def f20wc_f20_working_capital_dynamics_diorel_21d_slope_v119_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _roc(d, 21) - _roc(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC velocity convergence: short-horizon velocity minus long-horizon velocity
def f20wc_f20_working_capital_dynamics_cccrel_21d_slope_v120_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _roc(c, 21) - _roc(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-trade-WC over current liabilities over 21d
def f20wc_f20_working_capital_dynamics_nowcliab_21d_slope_v121_signal(receivables, inventory, payables, liabilitiesc):
    nowc = receivables + inventory - payables
    ratio = nowc / liabilitiesc.replace(0, np.nan)
    b = _roc(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trade-balance (receivables/payables) over 126d
def f20wc_f20_working_capital_dynamics_recpay_126d_slope_v122_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _roc(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-payables coverage over 126d
def f20wc_f20_working_capital_dynamics_invpay_126d_slope_v123_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _roc(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of receivables intensity over 21d
def f20wc_f20_working_capital_dynamics_recrevz_21d_slope_v124_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    sl = _roc(r, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of inventory intensity over 21d
def f20wc_f20_working_capital_dynamics_invcorz_21d_slope_v125_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    sl = _roc(r, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored slope of payables intensity over 21d
def f20wc_f20_working_capital_dynamics_paycorz_21d_slope_v126_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    sl = _roc(r, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables-share over 126d (structural collection-asset rotation)
def f20wc_f20_working_capital_dynamics_recshare_126d_slope_v127_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _roc(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-share over 126d
def f20wc_f20_working_capital_dynamics_invshare_126d_slope_v128_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _roc(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of payables-share over 126d
def f20wc_f20_working_capital_dynamics_payshare_126d_slope_v129_signal(payables, liabilitiesc):
    share = payables / liabilitiesc.replace(0, np.nan)
    b = _roc(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# collection-vs-stock velocity divergence, z-blended (standardized velocity spread)
def f20wc_f20_working_capital_dynamics_dsodiovel_63d_slope_v130_signal(receivables, inventory, revenue, cor):
    dsl = _roc(_f20_dso(receivables, revenue, 252), 63)
    isl = _roc(_f20_dio(inventory, cor, 252), 63)
    b = _z(dsl, 252) - _z(isl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of quick ratio over 21d
def f20wc_f20_working_capital_dynamics_quick_21d_slope_v131_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _roc(q, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of WC intensity over 126d (long-horizon intensity drift)
def f20wc_f20_working_capital_dynamics_wcint_126d_slope_v132_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _roc(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO coverage over 21d
def f20wc_f20_working_capital_dynamics_dpocover_21d_slope_v133_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    cover = dpo / op.replace(0, np.nan)
    b = _roc(cover, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO-to-DIO balance over 21d
def f20wc_f20_working_capital_dynamics_dsodiobal_21d_slope_v134_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    dio = _f20_dio(inventory, cor, 252)
    bal = (dso - dio) / (dso + dio).replace(0, np.nan)
    b = _roc(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of CCC relative-velocity over 504d
def f20wc_f20_working_capital_dynamics_cccrelrank_63d_slope_v135_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    rel = _roc(c, 63) / c.replace(0, np.nan)
    b = _rank(rel, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO velocity asymmetry: positive vs negative velocity magnitude over 252d
def f20wc_f20_working_capital_dynamics_dsovelasym_63d_slope_v136_signal(receivables, revenue):
    sl = _roc(_f20_dso(receivables, revenue, 63), 21)
    up = sl.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-sl.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO velocity asymmetry
def f20wc_f20_working_capital_dynamics_diovelasym_63d_slope_v137_signal(inventory, cor):
    sl = _roc(_f20_dio(inventory, cor, 63), 21)
    up = sl.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-sl.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue-velocity minus cor-velocity gap (operating-leverage on WC denominators)
def f20wc_f20_working_capital_dynamics_revcorvel_63d_slope_v138_signal(revenue, cor):
    rv = _roc(np.log(revenue.replace(0, np.nan)), 63)
    cv = _roc(np.log(cor.replace(0, np.nan)), 63)
    b = rv - cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory-to-payables coverage smoothed by EMA over 63d
def f20wc_f20_working_capital_dynamics_invpayema_63d_slope_v139_signal(inventory, payables):
    r = (inventory / payables.replace(0, np.nan)).ewm(span=42, min_periods=21).mean()
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables-to-payables trade balance smoothed by EMA over 63d
def f20wc_f20_working_capital_dynamics_recpayema_63d_slope_v140_signal(receivables, payables):
    r = (receivables / payables.replace(0, np.nan)).ewm(span=42, min_periods=21).mean()
    b = _roc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-over-liabilities velocity acceleration (current-surplus 2nd order over 126d)
def f20wc_f20_working_capital_dynamics_wcliab_126d_slope_v141_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / liabilitiesc.replace(0, np.nan)
    sl = _roc(ratio, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-trade-WC over current assets over 126d
def f20wc_f20_working_capital_dynamics_nowcca_126d_slope_v142_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    ratio = nowc / assetsc.replace(0, np.nan)
    b = _roc(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DSO over 252d horizon (annual collection drift velocity)
def f20wc_f20_working_capital_dynamics_dso_252d_slope_v143_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _roc(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DIO over 252d horizon
def f20wc_f20_working_capital_dynamics_dio_252d_slope_v144_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _roc(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of DPO over 252d horizon
def f20wc_f20_working_capital_dynamics_dpo_252d_slope_v145_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _roc(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCC over 252d horizon
def f20wc_f20_working_capital_dynamics_ccc_252d_slope_v146_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _roc(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio velocity dispersion over 252d (liquidity-velocity volatility)
def f20wc_f20_working_capital_dynamics_curratio_126d_slope_v147_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    sl = _roc(cr, 21)
    b = _std(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of receivables intensity over 252d (annual collection-burden drift)
def f20wc_f20_working_capital_dynamics_recrev_252d_slope_v148_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _roc(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inventory intensity over 252d
def f20wc_f20_working_capital_dynamics_invcor_252d_slope_v149_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _roc(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite WC velocity: z-blended slope of DSO+DIO-DPO intensities over 63d
def f20wc_f20_working_capital_dynamics_wcvel_63d_slope_v150_signal(receivables, inventory, payables, revenue, cor):
    dv = _roc(_f20_dso(receivables, revenue, 63), 63)
    iv = _roc(_f20_dio(inventory, cor, 63), 63)
    pv = _roc(_f20_dpo(payables, cor, 63), 63)
    b = _z(dv, 252) + _z(iv, 252) - _z(pv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20wc_f20_working_capital_dynamics_dso_21d_slope_v001_signal,
    f20wc_f20_working_capital_dynamics_dso_63d_slope_v002_signal,
    f20wc_f20_working_capital_dynamics_dio_21d_slope_v003_signal,
    f20wc_f20_working_capital_dynamics_dio_63d_slope_v004_signal,
    f20wc_f20_working_capital_dynamics_dpo_21d_slope_v005_signal,
    f20wc_f20_working_capital_dynamics_dpo_63d_slope_v006_signal,
    f20wc_f20_working_capital_dynamics_ccc_21d_slope_v007_signal,
    f20wc_f20_working_capital_dynamics_ccc_63d_slope_v008_signal,
    f20wc_f20_working_capital_dynamics_opcyc_63d_slope_v009_signal,
    f20wc_f20_working_capital_dynamics_recrev_21d_slope_v010_signal,
    f20wc_f20_working_capital_dynamics_recrev_63d_slope_v011_signal,
    f20wc_f20_working_capital_dynamics_invcor_21d_slope_v012_signal,
    f20wc_f20_working_capital_dynamics_invcor_63d_slope_v013_signal,
    f20wc_f20_working_capital_dynamics_paycor_63d_slope_v014_signal,
    f20wc_f20_working_capital_dynamics_wcint_63d_slope_v015_signal,
    f20wc_f20_working_capital_dynamics_curratio_21d_slope_v016_signal,
    f20wc_f20_working_capital_dynamics_curratio_63d_slope_v017_signal,
    f20wc_f20_working_capital_dynamics_quick_63d_slope_v018_signal,
    f20wc_f20_working_capital_dynamics_nowc_63d_slope_v019_signal,
    f20wc_f20_working_capital_dynamics_recshare_63d_slope_v020_signal,
    f20wc_f20_working_capital_dynamics_invshare_63d_slope_v021_signal,
    f20wc_f20_working_capital_dynamics_payshare_63d_slope_v022_signal,
    f20wc_f20_working_capital_dynamics_recpay_63d_slope_v023_signal,
    f20wc_f20_working_capital_dynamics_invpay_63d_slope_v024_signal,
    f20wc_f20_working_capital_dynamics_dsodpo_63d_slope_v025_signal,
    f20wc_f20_working_capital_dynamics_dsoz_21d_slope_v026_signal,
    f20wc_f20_working_capital_dynamics_dioz_21d_slope_v027_signal,
    f20wc_f20_working_capital_dynamics_dpoz_21d_slope_v028_signal,
    f20wc_f20_working_capital_dynamics_cccz_63d_slope_v029_signal,
    f20wc_f20_working_capital_dynamics_dsorank_63d_slope_v030_signal,
    f20wc_f20_working_capital_dynamics_diorank_63d_slope_v031_signal,
    f20wc_f20_working_capital_dynamics_cccrank_63d_slope_v032_signal,
    f20wc_f20_working_capital_dynamics_dsora_63d_slope_v033_signal,
    f20wc_f20_working_capital_dynamics_diora_63d_slope_v034_signal,
    f20wc_f20_working_capital_dynamics_dpora_63d_slope_v035_signal,
    f20wc_f20_working_capital_dynamics_ccctanh_63d_slope_v036_signal,
    f20wc_f20_working_capital_dynamics_recrevtanh_21d_slope_v037_signal,
    f20wc_f20_working_capital_dynamics_dsosm_63d_slope_v038_signal,
    f20wc_f20_working_capital_dynamics_diosm_63d_slope_v039_signal,
    f20wc_f20_working_capital_dynamics_dsoema_63d_slope_v040_signal,
    f20wc_f20_working_capital_dynamics_dioema_63d_slope_v041_signal,
    f20wc_f20_working_capital_dynamics_dpoema_63d_slope_v042_signal,
    f20wc_f20_working_capital_dynamics_invrec_63d_slope_v043_signal,
    f20wc_f20_working_capital_dynamics_payrec_63d_slope_v044_signal,
    f20wc_f20_working_capital_dynamics_wccush_63d_slope_v045_signal,
    f20wc_f20_working_capital_dynamics_dsodiobal_63d_slope_v046_signal,
    f20wc_f20_working_capital_dynamics_dpocover_63d_slope_v047_signal,
    f20wc_f20_working_capital_dynamics_recrev_126d_slope_v048_signal,
    f20wc_f20_working_capital_dynamics_invcor_126d_slope_v049_signal,
    f20wc_f20_working_capital_dynamics_ccc_126d_slope_v050_signal,
    f20wc_f20_working_capital_dynamics_ca_63d_slope_v051_signal,
    f20wc_f20_working_capital_dynamics_cl_63d_slope_v052_signal,
    f20wc_f20_working_capital_dynamics_rec_63d_slope_v053_signal,
    f20wc_f20_working_capital_dynamics_inv_63d_slope_v054_signal,
    f20wc_f20_working_capital_dynamics_pay_63d_slope_v055_signal,
    f20wc_f20_working_capital_dynamics_dsorev_63d_slope_v056_signal,
    f20wc_f20_working_capital_dynamics_invcorvel_63d_slope_v057_signal,
    f20wc_f20_working_capital_dynamics_paycorvel_63d_slope_v058_signal,
    f20wc_f20_working_capital_dynamics_nowcca_63d_slope_v059_signal,
    f20wc_f20_working_capital_dynamics_opcyc_21d_slope_v060_signal,
    f20wc_f20_working_capital_dynamics_wcintz_63d_slope_v061_signal,
    f20wc_f20_working_capital_dynamics_cccrank_126d_slope_v062_signal,
    f20wc_f20_working_capital_dynamics_dsoveldisp_63d_slope_v063_signal,
    f20wc_f20_working_capital_dynamics_dioveldisp_63d_slope_v064_signal,
    f20wc_f20_working_capital_dynamics_cccveldisp_63d_slope_v065_signal,
    f20wc_f20_working_capital_dynamics_recinvvel_63d_slope_v066_signal,
    f20wc_f20_working_capital_dynamics_paydiovel_63d_slope_v067_signal,
    f20wc_f20_working_capital_dynamics_recpay_21d_slope_v068_signal,
    f20wc_f20_working_capital_dynamics_nowcliab_63d_slope_v069_signal,
    f20wc_f20_working_capital_dynamics_wcliab_63d_slope_v070_signal,
    f20wc_f20_working_capital_dynamics_dso_5d_slope_v071_signal,
    f20wc_f20_working_capital_dynamics_dio_5d_slope_v072_signal,
    f20wc_f20_working_capital_dynamics_dpo_5d_slope_v073_signal,
    f20wc_f20_working_capital_dynamics_ccc_5d_slope_v074_signal,
    f20wc_f20_working_capital_dynamics_curratio_5d_slope_v075_signal,
    f20wc_f20_working_capital_dynamics_recrev_5d_slope_v076_signal,
    f20wc_f20_working_capital_dynamics_invcor_5d_slope_v077_signal,
    f20wc_f20_working_capital_dynamics_paycor_21d_slope_v078_signal,
    f20wc_f20_working_capital_dynamics_recshare_21d_slope_v079_signal,
    f20wc_f20_working_capital_dynamics_invshare_21d_slope_v080_signal,
    f20wc_f20_working_capital_dynamics_curratioz_63d_slope_v081_signal,
    f20wc_f20_working_capital_dynamics_quickz_63d_slope_v082_signal,
    f20wc_f20_working_capital_dynamics_nowcz_63d_slope_v083_signal,
    f20wc_f20_working_capital_dynamics_recrevrank_63d_slope_v084_signal,
    f20wc_f20_working_capital_dynamics_invrank_63d_slope_v085_signal,
    f20wc_f20_working_capital_dynamics_payrank_63d_slope_v086_signal,
    f20wc_f20_working_capital_dynamics_dsodpovel_63d_slope_v087_signal,
    f20wc_f20_working_capital_dynamics_diodpovel_63d_slope_v088_signal,
    f20wc_f20_working_capital_dynamics_invpay_21d_slope_v089_signal,
    f20wc_f20_working_capital_dynamics_wccush_21d_slope_v090_signal,
    f20wc_f20_working_capital_dynamics_dsotanh_21d_slope_v091_signal,
    f20wc_f20_working_capital_dynamics_diotanh_21d_slope_v092_signal,
    f20wc_f20_working_capital_dynamics_cccsm_63d_slope_v093_signal,
    f20wc_f20_working_capital_dynamics_dposm_63d_slope_v094_signal,
    f20wc_f20_working_capital_dynamics_cccema_63d_slope_v095_signal,
    f20wc_f20_working_capital_dynamics_recrevema_63d_slope_v096_signal,
    f20wc_f20_working_capital_dynamics_invrec_21d_slope_v097_signal,
    f20wc_f20_working_capital_dynamics_payrec_21d_slope_v098_signal,
    f20wc_f20_working_capital_dynamics_dsocush_63d_slope_v099_signal,
    f20wc_f20_working_capital_dynamics_cccwc_63d_slope_v100_signal,
    f20wc_f20_working_capital_dynamics_revnowc_63d_slope_v101_signal,
    f20wc_f20_working_capital_dynamics_invturn_63d_slope_v102_signal,
    f20wc_f20_working_capital_dynamics_recturn_63d_slope_v103_signal,
    f20wc_f20_working_capital_dynamics_payturn_63d_slope_v104_signal,
    f20wc_f20_working_capital_dynamics_wcturn_126d_slope_v105_signal,
    f20wc_f20_working_capital_dynamics_dsora_126d_slope_v106_signal,
    f20wc_f20_working_capital_dynamics_diora_126d_slope_v107_signal,
    f20wc_f20_working_capital_dynamics_dsorank_21d_slope_v108_signal,
    f20wc_f20_working_capital_dynamics_diorank_21d_slope_v109_signal,
    f20wc_f20_working_capital_dynamics_dporank_21d_slope_v110_signal,
    f20wc_f20_working_capital_dynamics_opcyc_126d_slope_v111_signal,
    f20wc_f20_working_capital_dynamics_dsoshare_63d_slope_v112_signal,
    f20wc_f20_working_capital_dynamics_diodpobal_63d_slope_v113_signal,
    f20wc_f20_working_capital_dynamics_recinvshare_63d_slope_v114_signal,
    f20wc_f20_working_capital_dynamics_definterval_63d_slope_v115_signal,
    f20wc_f20_working_capital_dynamics_cor_63d_slope_v116_signal,
    f20wc_f20_working_capital_dynamics_rev_63d_slope_v117_signal,
    f20wc_f20_working_capital_dynamics_dsorel_21d_slope_v118_signal,
    f20wc_f20_working_capital_dynamics_diorel_21d_slope_v119_signal,
    f20wc_f20_working_capital_dynamics_cccrel_21d_slope_v120_signal,
    f20wc_f20_working_capital_dynamics_nowcliab_21d_slope_v121_signal,
    f20wc_f20_working_capital_dynamics_recpay_126d_slope_v122_signal,
    f20wc_f20_working_capital_dynamics_invpay_126d_slope_v123_signal,
    f20wc_f20_working_capital_dynamics_recrevz_21d_slope_v124_signal,
    f20wc_f20_working_capital_dynamics_invcorz_21d_slope_v125_signal,
    f20wc_f20_working_capital_dynamics_paycorz_21d_slope_v126_signal,
    f20wc_f20_working_capital_dynamics_recshare_126d_slope_v127_signal,
    f20wc_f20_working_capital_dynamics_invshare_126d_slope_v128_signal,
    f20wc_f20_working_capital_dynamics_payshare_126d_slope_v129_signal,
    f20wc_f20_working_capital_dynamics_dsodiovel_63d_slope_v130_signal,
    f20wc_f20_working_capital_dynamics_quick_21d_slope_v131_signal,
    f20wc_f20_working_capital_dynamics_wcint_126d_slope_v132_signal,
    f20wc_f20_working_capital_dynamics_dpocover_21d_slope_v133_signal,
    f20wc_f20_working_capital_dynamics_dsodiobal_21d_slope_v134_signal,
    f20wc_f20_working_capital_dynamics_cccrelrank_63d_slope_v135_signal,
    f20wc_f20_working_capital_dynamics_dsovelasym_63d_slope_v136_signal,
    f20wc_f20_working_capital_dynamics_diovelasym_63d_slope_v137_signal,
    f20wc_f20_working_capital_dynamics_revcorvel_63d_slope_v138_signal,
    f20wc_f20_working_capital_dynamics_invpayema_63d_slope_v139_signal,
    f20wc_f20_working_capital_dynamics_recpayema_63d_slope_v140_signal,
    f20wc_f20_working_capital_dynamics_wcliab_126d_slope_v141_signal,
    f20wc_f20_working_capital_dynamics_nowcca_126d_slope_v142_signal,
    f20wc_f20_working_capital_dynamics_dso_252d_slope_v143_signal,
    f20wc_f20_working_capital_dynamics_dio_252d_slope_v144_signal,
    f20wc_f20_working_capital_dynamics_dpo_252d_slope_v145_signal,
    f20wc_f20_working_capital_dynamics_ccc_252d_slope_v146_signal,
    f20wc_f20_working_capital_dynamics_curratio_126d_slope_v147_signal,
    f20wc_f20_working_capital_dynamics_recrev_252d_slope_v148_signal,
    f20wc_f20_working_capital_dynamics_invcor_252d_slope_v149_signal,
    f20wc_f20_working_capital_dynamics_wcvel_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_WORKING_CAPITAL_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    receivables = _fund(101, base=2.0e8).rename("receivables")
    inventory = _fund(102, base=1.5e8).rename("inventory")
    payables = _fund(103, base=1.2e8).rename("payables")
    revenue = _fund(104, base=8.0e8).rename("revenue")
    cor = _fund(105, base=5.0e8).rename("cor")
    assetsc = _fund(106, base=6.0e8).rename("assetsc")
    liabilitiesc = _fund(107, base=3.5e8).rename("liabilitiesc")

    cols = {
        "receivables": receivables, "inventory": inventory, "payables": payables,
        "revenue": revenue, "cor": cor, "assetsc": assetsc, "liabilitiesc": liabilitiesc,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f20_working_capital_dynamics_2nd_derivatives_001_150_claude: %d features pass" % n_features)
