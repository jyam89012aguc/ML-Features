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


def _jerk(s, w):
    # discrete second derivative (acceleration/jerk) over horizon w
    return s - 2.0 * s.shift(w) + s.shift(2 * w)


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
# jerk (2nd math derivative) features
# ============================================================

# jerk of DSO over 21d (collection-period acceleration)
def f20wc_f20_working_capital_dynamics_dso_21d_jerk_v001_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _jerk(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO over 63d
def f20wc_f20_working_capital_dynamics_dso_63d_jerk_v002_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DIO over 21d (inventory-days acceleration)
def f20wc_f20_working_capital_dynamics_dio_21d_jerk_v003_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _jerk(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DIO over 63d
def f20wc_f20_working_capital_dynamics_dio_63d_jerk_v004_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO over 21d (payment-stretch acceleration)
def f20wc_f20_working_capital_dynamics_dpo_21d_jerk_v005_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _jerk(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO over 63d
def f20wc_f20_working_capital_dynamics_dpo_63d_jerk_v006_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CCC over 21d (cash-cycle acceleration)
def f20wc_f20_working_capital_dynamics_ccc_21d_jerk_v007_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _jerk(c, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CCC over 63d
def f20wc_f20_working_capital_dynamics_ccc_63d_jerk_v008_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _jerk(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of operating cycle over 63d
def f20wc_f20_working_capital_dynamics_opcyc_63d_jerk_v009_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _jerk(op, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables intensity over 21d (collection-burden acceleration)
def f20wc_f20_working_capital_dynamics_recrev_21d_jerk_v010_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _jerk(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables intensity over 63d
def f20wc_f20_working_capital_dynamics_recrev_63d_jerk_v011_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory intensity over 21d
def f20wc_f20_working_capital_dynamics_invcor_21d_jerk_v012_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _jerk(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory intensity over 63d
def f20wc_f20_working_capital_dynamics_invcor_63d_jerk_v013_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of payables intensity over 63d
def f20wc_f20_working_capital_dynamics_paycor_63d_jerk_v014_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of working-capital intensity over 63d
def f20wc_f20_working_capital_dynamics_wcint_63d_jerk_v015_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _jerk(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of current ratio over 21d
def f20wc_f20_working_capital_dynamics_curratio_21d_jerk_v016_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _jerk(cr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of current ratio over 63d
def f20wc_f20_working_capital_dynamics_curratio_63d_jerk_v017_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _jerk(cr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quick ratio over 63d
def f20wc_f20_working_capital_dynamics_quick_63d_jerk_v018_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _jerk(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-trade-WC intensity over 63d
def f20wc_f20_working_capital_dynamics_nowc_63d_jerk_v019_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    b = _jerk(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables share of current assets over 63d
def f20wc_f20_working_capital_dynamics_recshare_63d_jerk_v020_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _jerk(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory share of current assets over 63d
def f20wc_f20_working_capital_dynamics_invshare_63d_jerk_v021_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _jerk(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of payables share of current liabilities over 63d
def f20wc_f20_working_capital_dynamics_payshare_63d_jerk_v022_signal(payables, liabilitiesc):
    share = payables / liabilitiesc.replace(0, np.nan)
    b = _jerk(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables-to-payables trade balance over 63d
def f20wc_f20_working_capital_dynamics_recpay_63d_jerk_v023_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory-to-payables coverage over 63d
def f20wc_f20_working_capital_dynamics_invpay_63d_jerk_v024_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO-minus-DPO net financing days over 63d
def f20wc_f20_working_capital_dynamics_dsodpo_63d_jerk_v025_signal(receivables, payables, revenue, cor):
    net = _f20_dso(receivables, revenue, 252) - _f20_dpo(payables, cor, 252)
    b = _jerk(net, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of DSO over 21d (standardized collection acceleration)
def f20wc_f20_working_capital_dynamics_dsoz_21d_jerk_v026_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    jk = _jerk(d, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of DIO over 21d
def f20wc_f20_working_capital_dynamics_dioz_21d_jerk_v027_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    jk = _jerk(d, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of DPO over 21d
def f20wc_f20_working_capital_dynamics_dpoz_21d_jerk_v028_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    jk = _jerk(d, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of CCC over 63d
def f20wc_f20_working_capital_dynamics_cccz_63d_jerk_v029_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    jk = _jerk(c, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DSO jerk vs 504d history
def f20wc_f20_working_capital_dynamics_dsorank_63d_jerk_v030_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    jk = _jerk(d, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DIO jerk vs 504d history
def f20wc_f20_working_capital_dynamics_diorank_63d_jerk_v031_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    jk = _jerk(d, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of CCC jerk vs 504d history
def f20wc_f20_working_capital_dynamics_cccrank_63d_jerk_v032_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    jk = _jerk(c, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk risk-adjusted by DSO dispersion
def f20wc_f20_working_capital_dynamics_dsora_63d_jerk_v033_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    jk = _jerk(d, 63)
    b = jk / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk risk-adjusted by DIO dispersion
def f20wc_f20_working_capital_dynamics_diora_63d_jerk_v034_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    jk = _jerk(d, 63)
    b = jk / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO jerk risk-adjusted by DPO dispersion
def f20wc_f20_working_capital_dynamics_dpora_63d_jerk_v035_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    jk = _jerk(d, 63)
    b = jk / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded jerk of CCC over 63d (squashed cycle acceleration)
def f20wc_f20_working_capital_dynamics_ccctanh_63d_jerk_v036_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    jk = _jerk(c, 63)
    b = np.tanh(jk * 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of receivables intensity over 21d (collection-acceleration volatility)
def f20wc_f20_working_capital_dynamics_recrevdisp_21d_jerk_v037_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    jk = _jerk(r, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of DSO jerk (signed collection acceleration)
def f20wc_f20_working_capital_dynamics_dsosm_63d_jerk_v038_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    jk = _jerk(d, 63)
    b = np.sign(jk) * (jk.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of DIO jerk
def f20wc_f20_working_capital_dynamics_diosm_63d_jerk_v039_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    jk = _jerk(d, 63)
    b = np.sign(jk) * (jk.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed DSO over 63d (denoised collection acceleration)
def f20wc_f20_working_capital_dynamics_dsoema_63d_jerk_v040_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63).ewm(span=42, min_periods=21).mean()
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed DIO over 63d
def f20wc_f20_working_capital_dynamics_dioema_63d_jerk_v041_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed DPO over 63d
def f20wc_f20_working_capital_dynamics_dpoema_63d_jerk_v042_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _jerk(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-receivables jerk convergence: short vs long-horizon jerk (stock-vs-claim 3rd order)
def f20wc_f20_working_capital_dynamics_invrec_63d_jerk_v043_signal(inventory, receivables):
    r = inventory / receivables.replace(0, np.nan)
    b = _jerk(r, 21) - _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-inventory composition jerk z-scored vs 252d, EMA-smoothed (claim-vs-stock acceleration)
def f20wc_f20_working_capital_dynamics_payrec_63d_jerk_v044_signal(receivables, inventory):
    r = (receivables / inventory.replace(0, np.nan)).ewm(span=21, min_periods=10).mean()
    jk = _jerk(r, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-cushion jerk dispersion over 252d (liquidity-buffer-acceleration volatility)
def f20wc_f20_working_capital_dynamics_wccush_63d_jerk_v045_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    cush = wc / assetsc.replace(0, np.nan)
    jk = _jerk(cush, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO-to-DIO balance over 63d
def f20wc_f20_working_capital_dynamics_dsodiobal_63d_jerk_v046_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    dio = _f20_dio(inventory, cor, 252)
    bal = (dso - dio) / (dso + dio).replace(0, np.nan)
    b = _jerk(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO coverage of operating cycle over 63d
def f20wc_f20_working_capital_dynamics_dpocover_63d_jerk_v047_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    cover = dpo / op.replace(0, np.nan)
    b = _jerk(cover, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables intensity over 126d (long-horizon collection acceleration)
def f20wc_f20_working_capital_dynamics_recrev_126d_jerk_v048_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _jerk(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory intensity over 126d
def f20wc_f20_working_capital_dynamics_invcor_126d_jerk_v049_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _jerk(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CCC over 126d (long-horizon cycle acceleration)
def f20wc_f20_working_capital_dynamics_ccc_126d_jerk_v050_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _jerk(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-current-assets over 63d (liquidity-base acceleration)
def f20wc_f20_working_capital_dynamics_ca_63d_jerk_v051_signal(assetsc):
    lg = np.log(assetsc.replace(0, np.nan))
    b = _jerk(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-current-liabilities over 63d
def f20wc_f20_working_capital_dynamics_cl_63d_jerk_v052_signal(liabilitiesc):
    lg = np.log(liabilitiesc.replace(0, np.nan))
    b = _jerk(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth-acceleration z-scored vs 252d (standardized receivables jerk)
def f20wc_f20_working_capital_dynamics_rec_63d_jerk_v053_signal(receivables):
    lg = np.log(receivables.replace(0, np.nan))
    jk = _jerk(lg, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-growth-acceleration dispersion over 252d (inventory-jerk volatility)
def f20wc_f20_working_capital_dynamics_inv_63d_jerk_v054_signal(inventory):
    lg = np.log(inventory.replace(0, np.nan))
    jk = _jerk(lg, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-payables over 63d
def f20wc_f20_working_capital_dynamics_pay_63d_jerk_v055_signal(payables):
    lg = np.log(payables.replace(0, np.nan))
    b = _jerk(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-intensity jerk asymmetry: positive vs negative jerk magnitude (collection-shock skew)
def f20wc_f20_working_capital_dynamics_recrevg_63d_jerk_v056_signal(receivables, revenue):
    jk = _jerk(_f20_recratio(receivables, revenue), 21)
    up = jk.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-jk.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-intensity jerk asymmetry: positive vs negative jerk magnitude (build-shock skew)
def f20wc_f20_working_capital_dynamics_invcorg_63d_jerk_v057_signal(inventory, cor):
    jk = _jerk(_f20_invratio(inventory, cor), 21)
    up = jk.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-jk.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-intensity jerk asymmetry: positive vs negative jerk magnitude (payment-shock skew)
def f20wc_f20_working_capital_dynamics_paycorg_63d_jerk_v058_signal(payables, cor):
    jk = _jerk(_f20_payratio(payables, cor), 21)
    up = jk.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-jk.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-trade-WC over current assets over 63d
def f20wc_f20_working_capital_dynamics_nowcca_63d_jerk_v059_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    ratio = nowc / assetsc.replace(0, np.nan)
    b = _jerk(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of operating cycle over 21d (short-horizon cycle acceleration)
def f20wc_f20_working_capital_dynamics_opcyc_21d_jerk_v060_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _jerk(op, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of working-capital intensity over 63d
def f20wc_f20_working_capital_dynamics_wcintz_63d_jerk_v061_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    jk = _jerk(ratio, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of CCC over 21d (cycle-acceleration volatility)
def f20wc_f20_working_capital_dynamics_cccjkdisp_21d_jerk_v062_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    jk = _jerk(c, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of DSO over 21d
def f20wc_f20_working_capital_dynamics_dsojkdisp_21d_jerk_v063_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    jk = _jerk(d, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of DIO over 21d
def f20wc_f20_working_capital_dynamics_diojkdisp_21d_jerk_v064_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    jk = _jerk(d, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of DPO over 21d
def f20wc_f20_working_capital_dynamics_dpojkdisp_21d_jerk_v065_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    jk = _jerk(d, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-blended jerk spread: receivables-intensity jerk minus inventory-intensity jerk
def f20wc_f20_working_capital_dynamics_recinvjk_63d_jerk_v066_signal(receivables, inventory, revenue, cor):
    rj = _jerk(_f20_recratio(receivables, revenue), 63)
    ij = _jerk(_f20_invratio(inventory, cor), 63)
    b = _z(rj, 252) - _z(ij, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-blended jerk spread: payables-intensity jerk minus inventory-intensity jerk
def f20wc_f20_working_capital_dynamics_payinvjk_63d_jerk_v067_signal(payables, inventory, cor):
    pj = _jerk(_f20_payratio(payables, cor), 63)
    ij = _jerk(_f20_invratio(inventory, cor), 63)
    b = _z(pj, 252) - _z(ij, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of trade-balance (receivables/payables) over 21d
def f20wc_f20_working_capital_dynamics_recpay_21d_jerk_v068_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _jerk(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-trade-WC over current liabilities over 63d
def f20wc_f20_working_capital_dynamics_nowcliab_63d_jerk_v069_signal(receivables, inventory, payables, liabilitiesc):
    nowc = receivables + inventory - payables
    ratio = nowc / liabilitiesc.replace(0, np.nan)
    b = _jerk(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of WC-over-liabilities jerk vs 504d history
def f20wc_f20_working_capital_dynamics_wcliabrank_63d_jerk_v070_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / liabilitiesc.replace(0, np.nan)
    jk = _jerk(ratio, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO over 5d horizon (high-frequency collection acceleration)
def f20wc_f20_working_capital_dynamics_dso_5d_jerk_v071_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = _jerk(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DIO over 5d horizon
def f20wc_f20_working_capital_dynamics_dio_5d_jerk_v072_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = _jerk(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO over 5d horizon
def f20wc_f20_working_capital_dynamics_dpo_5d_jerk_v073_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    b = _jerk(d, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CCC over 5d horizon
def f20wc_f20_working_capital_dynamics_ccc_5d_jerk_v074_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = _jerk(c, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of current ratio over 5d
def f20wc_f20_working_capital_dynamics_curratio_5d_jerk_v075_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _jerk(cr, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables intensity over 5d
def f20wc_f20_working_capital_dynamics_recrev_5d_jerk_v076_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _jerk(r, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory intensity over 5d
def f20wc_f20_working_capital_dynamics_invcor_5d_jerk_v077_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _jerk(r, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of payables intensity over 21d
def f20wc_f20_working_capital_dynamics_paycor_21d_jerk_v078_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _jerk(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables share over 21d
def f20wc_f20_working_capital_dynamics_recshare_21d_jerk_v079_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _jerk(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory share over 21d
def f20wc_f20_working_capital_dynamics_invshare_21d_jerk_v080_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _jerk(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of current ratio over 63d
def f20wc_f20_working_capital_dynamics_curratioz_63d_jerk_v081_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    jk = _jerk(cr, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of quick ratio over 63d
def f20wc_f20_working_capital_dynamics_quickz_63d_jerk_v082_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    jk = _jerk(q, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of net-trade-WC intensity over 63d
def f20wc_f20_working_capital_dynamics_nowcz_63d_jerk_v083_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    jk = _jerk(ratio, 63)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of receivables-intensity jerk over 504d
def f20wc_f20_working_capital_dynamics_recrevrank_63d_jerk_v084_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    jk = _jerk(r, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of inventory-intensity jerk over 504d
def f20wc_f20_working_capital_dynamics_invrank_63d_jerk_v085_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    jk = _jerk(r, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of payables-intensity jerk over 504d
def f20wc_f20_working_capital_dynamics_payrank_63d_jerk_v086_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    jk = _jerk(r, 63)
    b = _rank(jk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing-days acceleration risk-adjusted by CCC dispersion (standardized net jerk)
def f20wc_f20_working_capital_dynamics_dsodpojk_63d_jerk_v087_signal(receivables, inventory, payables, revenue, cor):
    net = _f20_dso(receivables, revenue, 252) - _f20_dpo(payables, cor, 252)
    jk = _jerk(net, 63)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = jk / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk minus DPO jerk (inventory financing-gap acceleration)
def f20wc_f20_working_capital_dynamics_diodpojk_63d_jerk_v088_signal(inventory, payables, cor):
    ij = _jerk(_f20_dio(inventory, cor, 252), 63)
    pj = _jerk(_f20_dpo(payables, cor, 252), 63)
    b = ij - pj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory-to-payables coverage over 21d
def f20wc_f20_working_capital_dynamics_invpay_21d_jerk_v089_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _jerk(r, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-cushion jerk convergence: short vs long-horizon jerk (liquidity-buffer 3rd order)
def f20wc_f20_working_capital_dynamics_wccush_21d_jerk_v090_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    cush = wc / assetsc.replace(0, np.nan)
    b = _jerk(cush, 21) - _jerk(cush, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk vs DPO jerk interaction (collection-vs-payment acceleration product)
def f20wc_f20_working_capital_dynamics_dsodpojkint_63d_jerk_v091_signal(receivables, payables, revenue, cor):
    dj = _z(_jerk(_f20_dso(receivables, revenue, 252), 63), 252)
    pj = _z(_jerk(_f20_dpo(payables, cor, 252), 63), 252)
    b = dj * pj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk vs DSO jerk interaction (stock-vs-collection acceleration product)
def f20wc_f20_working_capital_dynamics_diodsojkint_63d_jerk_v092_signal(receivables, inventory, revenue, cor):
    ij = _z(_jerk(_f20_dio(inventory, cor, 252), 63), 252)
    dj = _z(_jerk(_f20_dso(receivables, revenue, 252), 63), 252)
    b = ij * dj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of CCC jerk over 63d
def f20wc_f20_working_capital_dynamics_cccsm_63d_jerk_v093_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    jk = _jerk(c, 63)
    b = np.sign(jk) * (jk.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of DPO jerk over 63d
def f20wc_f20_working_capital_dynamics_dposm_63d_jerk_v094_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    jk = _jerk(d, 63)
    b = np.sign(jk) * (jk.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed CCC over 63d (denoised cycle acceleration)
def f20wc_f20_working_capital_dynamics_cccema_63d_jerk_v095_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63).ewm(span=42, min_periods=21).mean()
    b = _jerk(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed receivables intensity over 63d
def f20wc_f20_working_capital_dynamics_recrevema_63d_jerk_v096_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue).ewm(span=42, min_periods=21).mean()
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-receivables jerk dispersion over 252d (stock-vs-claim-acceleration volatility)
def f20wc_f20_working_capital_dynamics_invrec_21d_jerk_v097_signal(inventory, receivables):
    r = inventory / receivables.replace(0, np.nan)
    jk = _jerk(r, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of payables-to-receivables composition over 21d
def f20wc_f20_working_capital_dynamics_payrecdisp_21d_jerk_v098_signal(payables, receivables):
    r = payables / receivables.replace(0, np.nan)
    jk = _jerk(r, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC jerk scaled by WC intensity (cash-tie-up-weighted cycle acceleration)
def f20wc_f20_working_capital_dynamics_cccwc_63d_jerk_v099_signal(receivables, inventory, payables, revenue, cor, assetsc, liabilitiesc):
    jk = _jerk(_f20_ccc(receivables, inventory, payables, revenue, cor, 252), 63)
    wc = _f20_wc(assetsc, liabilitiesc)
    wint = wc / revenue.replace(0, np.nan)
    b = _z(jk, 252) * _z(wint, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk scaled by current-ratio cushion (stress-weighted collection acceleration)
def f20wc_f20_working_capital_dynamics_dsocush_63d_jerk_v100_signal(receivables, revenue, assetsc, liabilitiesc):
    jk = _jerk(_f20_dso(receivables, revenue, 252), 63)
    cush = assetsc / liabilitiesc.replace(0, np.nan)
    b = _z(jk, 252) * _z(cush, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of revenue-per-net-trade-WC over 63d (productivity acceleration)
def f20wc_f20_working_capital_dynamics_revnowc_63d_jerk_v101_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    prod = revenue / nowc.replace(0, np.nan)
    b = _jerk(prod, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover (cor/inventory) jerk convergence: short vs long-horizon jerk
def f20wc_f20_working_capital_dynamics_invturn_63d_jerk_v102_signal(cor, inventory):
    t = cor / inventory.replace(0, np.nan)
    b = _jerk(t, 21) - _jerk(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-turnover (revenue/receivables) jerk convergence: short vs long-horizon jerk
def f20wc_f20_working_capital_dynamics_recturn_63d_jerk_v103_signal(revenue, receivables):
    t = revenue / receivables.replace(0, np.nan)
    b = _jerk(t, 21) - _jerk(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-turnover (cor/payables) jerk convergence: short vs long-horizon jerk
def f20wc_f20_working_capital_dynamics_payturn_63d_jerk_v104_signal(cor, payables):
    t = cor / payables.replace(0, np.nan)
    b = _jerk(t, 21) - _jerk(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-turnover (revenue/WC) jerk dispersion over 252d (capital-productivity-acceleration volatility)
def f20wc_f20_working_capital_dynamics_wcturn_126d_jerk_v105_signal(revenue, assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    t = revenue / wc.replace(0, np.nan)
    jk = _jerk(t, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk over 126d risk-adjusted by DSO dispersion
def f20wc_f20_working_capital_dynamics_dsora_126d_jerk_v106_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    jk = _jerk(d, 126)
    b = jk / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk over 126d risk-adjusted by DIO dispersion
def f20wc_f20_working_capital_dynamics_diora_126d_jerk_v107_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    jk = _jerk(d, 126)
    b = jk / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk acceleration: 21d-jerk differenced (collection 3rd-order proxy)
def f20wc_f20_working_capital_dynamics_dsojkacc_21d_jerk_v108_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    jk = _jerk(d, 21)
    b = jk - jk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk acceleration: 21d-jerk differenced
def f20wc_f20_working_capital_dynamics_diojkacc_21d_jerk_v109_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    jk = _jerk(d, 21)
    b = jk - jk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO jerk acceleration: 21d-jerk differenced
def f20wc_f20_working_capital_dynamics_dpojkacc_21d_jerk_v110_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    jk = _jerk(d, 21)
    b = jk - jk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of operating cycle over 126d
def f20wc_f20_working_capital_dynamics_opcyc_126d_jerk_v111_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = _jerk(op, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO-share-of-CCC over 63d
def f20wc_f20_working_capital_dynamics_dsoshare_63d_jerk_v112_signal(receivables, inventory, payables, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    share = dso / c.replace(0, np.nan)
    b = _jerk(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO-vs-DPO financing-balance jerk dispersion over 252d (financing-acceleration volatility)
def f20wc_f20_working_capital_dynamics_diodpobal_63d_jerk_v113_signal(inventory, payables, cor):
    dio = _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    bal = (dio - dpo) / (dio + dpo).replace(0, np.nan)
    jk = _jerk(bal, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk spread: receivables-share jerk minus inventory-share jerk (rotation acceleration)
def f20wc_f20_working_capital_dynamics_recinvshare_63d_jerk_v114_signal(receivables, inventory, assetsc):
    rs = receivables / assetsc.replace(0, np.nan)
    isr = inventory / assetsc.replace(0, np.nan)
    b = _z(_jerk(rs, 63), 252) - _z(_jerk(isr, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of defensive interval over 63d
def f20wc_f20_working_capital_dynamics_definterval_63d_jerk_v115_signal(receivables, assetsc, inventory, cor):
    liquid = receivables + (assetsc - inventory)
    cor_day = _mean(cor, 252) / 91.0
    di = liquid / cor_day.replace(0, np.nan)
    b = _jerk(di, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-cor over 63d (demand acceleration)
def f20wc_f20_working_capital_dynamics_cor_63d_jerk_v116_signal(cor):
    lg = np.log(cor.replace(0, np.nan))
    b = _jerk(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-revenue over 63d (sales acceleration)
def f20wc_f20_working_capital_dynamics_rev_63d_jerk_v117_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    b = _jerk(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk dispersion over 252d (collection-acceleration volatility, 21d jerk)
def f20wc_f20_working_capital_dynamics_dsorel_21d_jerk_v118_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    jk = _jerk(d, 21)
    b = _std(jk, 252) / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk dispersion over 252d (build-acceleration volatility, 21d jerk)
def f20wc_f20_working_capital_dynamics_diorel_21d_jerk_v119_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    jk = _jerk(d, 21)
    b = _std(jk, 252) / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC jerk dispersion over 252d (cycle-acceleration volatility, 21d jerk)
def f20wc_f20_working_capital_dynamics_cccrel_21d_jerk_v120_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    jk = _jerk(c, 21)
    b = _std(jk, 252) / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-trade-WC over current liabilities over 21d
def f20wc_f20_working_capital_dynamics_nowcliab_21d_jerk_v121_signal(receivables, inventory, payables, liabilitiesc):
    nowc = receivables + inventory - payables
    ratio = nowc / liabilitiesc.replace(0, np.nan)
    b = _jerk(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of trade-balance (receivables/payables) over 126d
def f20wc_f20_working_capital_dynamics_recpay_126d_jerk_v122_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _jerk(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory-to-payables coverage over 126d
def f20wc_f20_working_capital_dynamics_invpay_126d_jerk_v123_signal(inventory, payables):
    r = inventory / payables.replace(0, np.nan)
    b = _jerk(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of receivables intensity over 21d
def f20wc_f20_working_capital_dynamics_recrevz_21d_jerk_v124_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    jk = _jerk(r, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of inventory intensity over 21d
def f20wc_f20_working_capital_dynamics_invcorz_21d_jerk_v125_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    jk = _jerk(r, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored jerk of payables intensity over 21d
def f20wc_f20_working_capital_dynamics_paycorz_21d_jerk_v126_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    jk = _jerk(r, 21)
    b = _z(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables-share over 126d (structural rotation acceleration)
def f20wc_f20_working_capital_dynamics_recshare_126d_jerk_v127_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _jerk(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory-share over 126d
def f20wc_f20_working_capital_dynamics_invshare_126d_jerk_v128_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _jerk(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of payables-share over 126d
def f20wc_f20_working_capital_dynamics_payshare_126d_jerk_v129_signal(payables, liabilitiesc):
    share = payables / liabilitiesc.replace(0, np.nan)
    b = _jerk(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk minus DIO jerk, z-blended (collection-vs-stock acceleration spread)
def f20wc_f20_working_capital_dynamics_dsodiojk_63d_jerk_v130_signal(receivables, inventory, revenue, cor):
    dj = _jerk(_f20_dso(receivables, revenue, 252), 63)
    ij = _jerk(_f20_dio(inventory, cor, 252), 63)
    b = _z(dj, 252) - _z(ij, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quick ratio over 21d
def f20wc_f20_working_capital_dynamics_quick_21d_jerk_v131_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _jerk(q, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of WC intensity over 126d
def f20wc_f20_working_capital_dynamics_wcint_126d_jerk_v132_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _jerk(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO coverage over 21d
def f20wc_f20_working_capital_dynamics_dpocover_21d_jerk_v133_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    cover = dpo / op.replace(0, np.nan)
    b = _jerk(cover, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO-to-DIO balance over 21d
def f20wc_f20_working_capital_dynamics_dsodiobal_21d_jerk_v134_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    dio = _f20_dio(inventory, cor, 252)
    bal = (dso - dio) / (dso + dio).replace(0, np.nan)
    b = _jerk(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC jerk dispersion over 252d (cycle-acceleration volatility, 63d jerk)
def f20wc_f20_working_capital_dynamics_cccreltanh_63d_jerk_v135_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    jk = _jerk(c, 63)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO jerk asymmetry: positive vs negative jerk magnitude over 252d
def f20wc_f20_working_capital_dynamics_dsojkasym_63d_jerk_v136_signal(receivables, revenue):
    jk = _jerk(_f20_dso(receivables, revenue, 63), 21)
    up = jk.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-jk.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO jerk asymmetry
def f20wc_f20_working_capital_dynamics_diojkasym_63d_jerk_v137_signal(inventory, cor):
    jk = _jerk(_f20_dio(inventory, cor, 63), 21)
    up = jk.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-jk.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-acceleration minus cor-growth-acceleration (operating-leverage jerk)
def f20wc_f20_working_capital_dynamics_revcorg_63d_jerk_v138_signal(revenue, cor):
    rj = _jerk(np.log(revenue.replace(0, np.nan)), 63)
    cj = _jerk(np.log(cor.replace(0, np.nan)), 63)
    b = rj - cj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed inventory-to-payables coverage over 63d
def f20wc_f20_working_capital_dynamics_invpayema_63d_jerk_v139_signal(inventory, payables):
    r = (inventory / payables.replace(0, np.nan)).ewm(span=42, min_periods=21).mean()
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of EMA-smoothed receivables-to-payables trade balance over 63d
def f20wc_f20_working_capital_dynamics_recpayema_63d_jerk_v140_signal(receivables, payables):
    r = (receivables / payables.replace(0, np.nan)).ewm(span=42, min_periods=21).mean()
    b = _jerk(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of WC over current liabilities over 126d
def f20wc_f20_working_capital_dynamics_wcliab_126d_jerk_v141_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / liabilitiesc.replace(0, np.nan)
    b = _jerk(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-trade-WC over current assets over 126d
def f20wc_f20_working_capital_dynamics_nowcca_126d_jerk_v142_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    ratio = nowc / assetsc.replace(0, np.nan)
    b = _jerk(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DSO over 126d horizon (annual collection acceleration)
def f20wc_f20_working_capital_dynamics_dso_126d_jerk_v143_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = _jerk(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DIO over 126d horizon
def f20wc_f20_working_capital_dynamics_dio_126d_jerk_v144_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = _jerk(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of DPO over 126d horizon
def f20wc_f20_working_capital_dynamics_dpo_126d_jerk_v145_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = _jerk(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of CCC jerk over 1260d (multi-year cycle-acceleration positioning)
def f20wc_f20_working_capital_dynamics_cccrank_126d_jerk_v146_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    jk = _jerk(c, 126)
    b = _rank(jk, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk dispersion of current ratio over 21d (liquidity-acceleration volatility)
def f20wc_f20_working_capital_dynamics_curratiodisp_21d_jerk_v147_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    jk = _jerk(cr, 21)
    b = _std(jk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of receivables intensity over 252d (annual collection-burden acceleration)
def f20wc_f20_working_capital_dynamics_recrev_252d_jerk_v148_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _jerk(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of inventory intensity over 252d
def f20wc_f20_working_capital_dynamics_invcor_252d_jerk_v149_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _jerk(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite WC jerk: z-blended jerk of DSO+DIO-DPO intensities over 63d
def f20wc_f20_working_capital_dynamics_wcjk_63d_jerk_v150_signal(receivables, inventory, payables, revenue, cor):
    dj = _jerk(_f20_dso(receivables, revenue, 63), 63)
    ij = _jerk(_f20_dio(inventory, cor, 63), 63)
    pj = _jerk(_f20_dpo(payables, cor, 63), 63)
    b = _z(dj, 252) + _z(ij, 252) - _z(pj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20wc_f20_working_capital_dynamics_dso_21d_jerk_v001_signal,
    f20wc_f20_working_capital_dynamics_dso_63d_jerk_v002_signal,
    f20wc_f20_working_capital_dynamics_dio_21d_jerk_v003_signal,
    f20wc_f20_working_capital_dynamics_dio_63d_jerk_v004_signal,
    f20wc_f20_working_capital_dynamics_dpo_21d_jerk_v005_signal,
    f20wc_f20_working_capital_dynamics_dpo_63d_jerk_v006_signal,
    f20wc_f20_working_capital_dynamics_ccc_21d_jerk_v007_signal,
    f20wc_f20_working_capital_dynamics_ccc_63d_jerk_v008_signal,
    f20wc_f20_working_capital_dynamics_opcyc_63d_jerk_v009_signal,
    f20wc_f20_working_capital_dynamics_recrev_21d_jerk_v010_signal,
    f20wc_f20_working_capital_dynamics_recrev_63d_jerk_v011_signal,
    f20wc_f20_working_capital_dynamics_invcor_21d_jerk_v012_signal,
    f20wc_f20_working_capital_dynamics_invcor_63d_jerk_v013_signal,
    f20wc_f20_working_capital_dynamics_paycor_63d_jerk_v014_signal,
    f20wc_f20_working_capital_dynamics_wcint_63d_jerk_v015_signal,
    f20wc_f20_working_capital_dynamics_curratio_21d_jerk_v016_signal,
    f20wc_f20_working_capital_dynamics_curratio_63d_jerk_v017_signal,
    f20wc_f20_working_capital_dynamics_quick_63d_jerk_v018_signal,
    f20wc_f20_working_capital_dynamics_nowc_63d_jerk_v019_signal,
    f20wc_f20_working_capital_dynamics_recshare_63d_jerk_v020_signal,
    f20wc_f20_working_capital_dynamics_invshare_63d_jerk_v021_signal,
    f20wc_f20_working_capital_dynamics_payshare_63d_jerk_v022_signal,
    f20wc_f20_working_capital_dynamics_recpay_63d_jerk_v023_signal,
    f20wc_f20_working_capital_dynamics_invpay_63d_jerk_v024_signal,
    f20wc_f20_working_capital_dynamics_dsodpo_63d_jerk_v025_signal,
    f20wc_f20_working_capital_dynamics_dsoz_21d_jerk_v026_signal,
    f20wc_f20_working_capital_dynamics_dioz_21d_jerk_v027_signal,
    f20wc_f20_working_capital_dynamics_dpoz_21d_jerk_v028_signal,
    f20wc_f20_working_capital_dynamics_cccz_63d_jerk_v029_signal,
    f20wc_f20_working_capital_dynamics_dsorank_63d_jerk_v030_signal,
    f20wc_f20_working_capital_dynamics_diorank_63d_jerk_v031_signal,
    f20wc_f20_working_capital_dynamics_cccrank_63d_jerk_v032_signal,
    f20wc_f20_working_capital_dynamics_dsora_63d_jerk_v033_signal,
    f20wc_f20_working_capital_dynamics_diora_63d_jerk_v034_signal,
    f20wc_f20_working_capital_dynamics_dpora_63d_jerk_v035_signal,
    f20wc_f20_working_capital_dynamics_ccctanh_63d_jerk_v036_signal,
    f20wc_f20_working_capital_dynamics_recrevdisp_21d_jerk_v037_signal,
    f20wc_f20_working_capital_dynamics_dsosm_63d_jerk_v038_signal,
    f20wc_f20_working_capital_dynamics_diosm_63d_jerk_v039_signal,
    f20wc_f20_working_capital_dynamics_dsoema_63d_jerk_v040_signal,
    f20wc_f20_working_capital_dynamics_dioema_63d_jerk_v041_signal,
    f20wc_f20_working_capital_dynamics_dpoema_63d_jerk_v042_signal,
    f20wc_f20_working_capital_dynamics_invrec_63d_jerk_v043_signal,
    f20wc_f20_working_capital_dynamics_payrec_63d_jerk_v044_signal,
    f20wc_f20_working_capital_dynamics_wccush_63d_jerk_v045_signal,
    f20wc_f20_working_capital_dynamics_dsodiobal_63d_jerk_v046_signal,
    f20wc_f20_working_capital_dynamics_dpocover_63d_jerk_v047_signal,
    f20wc_f20_working_capital_dynamics_recrev_126d_jerk_v048_signal,
    f20wc_f20_working_capital_dynamics_invcor_126d_jerk_v049_signal,
    f20wc_f20_working_capital_dynamics_ccc_126d_jerk_v050_signal,
    f20wc_f20_working_capital_dynamics_ca_63d_jerk_v051_signal,
    f20wc_f20_working_capital_dynamics_cl_63d_jerk_v052_signal,
    f20wc_f20_working_capital_dynamics_rec_63d_jerk_v053_signal,
    f20wc_f20_working_capital_dynamics_inv_63d_jerk_v054_signal,
    f20wc_f20_working_capital_dynamics_pay_63d_jerk_v055_signal,
    f20wc_f20_working_capital_dynamics_recrevg_63d_jerk_v056_signal,
    f20wc_f20_working_capital_dynamics_invcorg_63d_jerk_v057_signal,
    f20wc_f20_working_capital_dynamics_paycorg_63d_jerk_v058_signal,
    f20wc_f20_working_capital_dynamics_nowcca_63d_jerk_v059_signal,
    f20wc_f20_working_capital_dynamics_opcyc_21d_jerk_v060_signal,
    f20wc_f20_working_capital_dynamics_wcintz_63d_jerk_v061_signal,
    f20wc_f20_working_capital_dynamics_cccjkdisp_21d_jerk_v062_signal,
    f20wc_f20_working_capital_dynamics_dsojkdisp_21d_jerk_v063_signal,
    f20wc_f20_working_capital_dynamics_diojkdisp_21d_jerk_v064_signal,
    f20wc_f20_working_capital_dynamics_dpojkdisp_21d_jerk_v065_signal,
    f20wc_f20_working_capital_dynamics_recinvjk_63d_jerk_v066_signal,
    f20wc_f20_working_capital_dynamics_payinvjk_63d_jerk_v067_signal,
    f20wc_f20_working_capital_dynamics_recpay_21d_jerk_v068_signal,
    f20wc_f20_working_capital_dynamics_nowcliab_63d_jerk_v069_signal,
    f20wc_f20_working_capital_dynamics_wcliabrank_63d_jerk_v070_signal,
    f20wc_f20_working_capital_dynamics_dso_5d_jerk_v071_signal,
    f20wc_f20_working_capital_dynamics_dio_5d_jerk_v072_signal,
    f20wc_f20_working_capital_dynamics_dpo_5d_jerk_v073_signal,
    f20wc_f20_working_capital_dynamics_ccc_5d_jerk_v074_signal,
    f20wc_f20_working_capital_dynamics_curratio_5d_jerk_v075_signal,
    f20wc_f20_working_capital_dynamics_recrev_5d_jerk_v076_signal,
    f20wc_f20_working_capital_dynamics_invcor_5d_jerk_v077_signal,
    f20wc_f20_working_capital_dynamics_paycor_21d_jerk_v078_signal,
    f20wc_f20_working_capital_dynamics_recshare_21d_jerk_v079_signal,
    f20wc_f20_working_capital_dynamics_invshare_21d_jerk_v080_signal,
    f20wc_f20_working_capital_dynamics_curratioz_63d_jerk_v081_signal,
    f20wc_f20_working_capital_dynamics_quickz_63d_jerk_v082_signal,
    f20wc_f20_working_capital_dynamics_nowcz_63d_jerk_v083_signal,
    f20wc_f20_working_capital_dynamics_recrevrank_63d_jerk_v084_signal,
    f20wc_f20_working_capital_dynamics_invrank_63d_jerk_v085_signal,
    f20wc_f20_working_capital_dynamics_payrank_63d_jerk_v086_signal,
    f20wc_f20_working_capital_dynamics_dsodpojk_63d_jerk_v087_signal,
    f20wc_f20_working_capital_dynamics_diodpojk_63d_jerk_v088_signal,
    f20wc_f20_working_capital_dynamics_invpay_21d_jerk_v089_signal,
    f20wc_f20_working_capital_dynamics_wccush_21d_jerk_v090_signal,
    f20wc_f20_working_capital_dynamics_dsodpojkint_63d_jerk_v091_signal,
    f20wc_f20_working_capital_dynamics_diodsojkint_63d_jerk_v092_signal,
    f20wc_f20_working_capital_dynamics_cccsm_63d_jerk_v093_signal,
    f20wc_f20_working_capital_dynamics_dposm_63d_jerk_v094_signal,
    f20wc_f20_working_capital_dynamics_cccema_63d_jerk_v095_signal,
    f20wc_f20_working_capital_dynamics_recrevema_63d_jerk_v096_signal,
    f20wc_f20_working_capital_dynamics_invrec_21d_jerk_v097_signal,
    f20wc_f20_working_capital_dynamics_payrecdisp_21d_jerk_v098_signal,
    f20wc_f20_working_capital_dynamics_cccwc_63d_jerk_v099_signal,
    f20wc_f20_working_capital_dynamics_dsocush_63d_jerk_v100_signal,
    f20wc_f20_working_capital_dynamics_revnowc_63d_jerk_v101_signal,
    f20wc_f20_working_capital_dynamics_invturn_63d_jerk_v102_signal,
    f20wc_f20_working_capital_dynamics_recturn_63d_jerk_v103_signal,
    f20wc_f20_working_capital_dynamics_payturn_63d_jerk_v104_signal,
    f20wc_f20_working_capital_dynamics_wcturn_126d_jerk_v105_signal,
    f20wc_f20_working_capital_dynamics_dsora_126d_jerk_v106_signal,
    f20wc_f20_working_capital_dynamics_diora_126d_jerk_v107_signal,
    f20wc_f20_working_capital_dynamics_dsojkacc_21d_jerk_v108_signal,
    f20wc_f20_working_capital_dynamics_diojkacc_21d_jerk_v109_signal,
    f20wc_f20_working_capital_dynamics_dpojkacc_21d_jerk_v110_signal,
    f20wc_f20_working_capital_dynamics_opcyc_126d_jerk_v111_signal,
    f20wc_f20_working_capital_dynamics_dsoshare_63d_jerk_v112_signal,
    f20wc_f20_working_capital_dynamics_diodpobal_63d_jerk_v113_signal,
    f20wc_f20_working_capital_dynamics_recinvshare_63d_jerk_v114_signal,
    f20wc_f20_working_capital_dynamics_definterval_63d_jerk_v115_signal,
    f20wc_f20_working_capital_dynamics_cor_63d_jerk_v116_signal,
    f20wc_f20_working_capital_dynamics_rev_63d_jerk_v117_signal,
    f20wc_f20_working_capital_dynamics_dsorel_21d_jerk_v118_signal,
    f20wc_f20_working_capital_dynamics_diorel_21d_jerk_v119_signal,
    f20wc_f20_working_capital_dynamics_cccrel_21d_jerk_v120_signal,
    f20wc_f20_working_capital_dynamics_nowcliab_21d_jerk_v121_signal,
    f20wc_f20_working_capital_dynamics_recpay_126d_jerk_v122_signal,
    f20wc_f20_working_capital_dynamics_invpay_126d_jerk_v123_signal,
    f20wc_f20_working_capital_dynamics_recrevz_21d_jerk_v124_signal,
    f20wc_f20_working_capital_dynamics_invcorz_21d_jerk_v125_signal,
    f20wc_f20_working_capital_dynamics_paycorz_21d_jerk_v126_signal,
    f20wc_f20_working_capital_dynamics_recshare_126d_jerk_v127_signal,
    f20wc_f20_working_capital_dynamics_invshare_126d_jerk_v128_signal,
    f20wc_f20_working_capital_dynamics_payshare_126d_jerk_v129_signal,
    f20wc_f20_working_capital_dynamics_dsodiojk_63d_jerk_v130_signal,
    f20wc_f20_working_capital_dynamics_quick_21d_jerk_v131_signal,
    f20wc_f20_working_capital_dynamics_wcint_126d_jerk_v132_signal,
    f20wc_f20_working_capital_dynamics_dpocover_21d_jerk_v133_signal,
    f20wc_f20_working_capital_dynamics_dsodiobal_21d_jerk_v134_signal,
    f20wc_f20_working_capital_dynamics_cccreltanh_63d_jerk_v135_signal,
    f20wc_f20_working_capital_dynamics_dsojkasym_63d_jerk_v136_signal,
    f20wc_f20_working_capital_dynamics_diojkasym_63d_jerk_v137_signal,
    f20wc_f20_working_capital_dynamics_revcorg_63d_jerk_v138_signal,
    f20wc_f20_working_capital_dynamics_invpayema_63d_jerk_v139_signal,
    f20wc_f20_working_capital_dynamics_recpayema_63d_jerk_v140_signal,
    f20wc_f20_working_capital_dynamics_wcliab_126d_jerk_v141_signal,
    f20wc_f20_working_capital_dynamics_nowcca_126d_jerk_v142_signal,
    f20wc_f20_working_capital_dynamics_dso_126d_jerk_v143_signal,
    f20wc_f20_working_capital_dynamics_dio_126d_jerk_v144_signal,
    f20wc_f20_working_capital_dynamics_dpo_126d_jerk_v145_signal,
    f20wc_f20_working_capital_dynamics_cccrank_126d_jerk_v146_signal,
    f20wc_f20_working_capital_dynamics_curratiodisp_21d_jerk_v147_signal,
    f20wc_f20_working_capital_dynamics_recrev_252d_jerk_v148_signal,
    f20wc_f20_working_capital_dynamics_invcor_252d_jerk_v149_signal,
    f20wc_f20_working_capital_dynamics_wcjk_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_WORKING_CAPITAL_DYNAMICS_REGISTRY_JERK_001_150 = REGISTRY


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

    print("OK f20_working_capital_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
