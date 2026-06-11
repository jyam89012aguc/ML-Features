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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== derivative engine: 2nd math derivative (jerk / acceleration) of a base series =====
def _slope(s, w):
    # rolling OLS slope vs time index (1st discrete derivative, per-day)
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx * idx).sum()

    def _f(a):
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _accel(s, w):
    # rolling 2nd derivative: slope-of-slope (acceleration / jerk of the level series)
    return _slope(_slope(s, w), w)


# ----- normalized 2nd-derivative variants (decouple ratios sharing a common trend) -----
def _accel_z(s, w):
    # acceleration of the z-scored series (unit-variance-normalized 2nd derivative)
    return _accel(_z(s, w), w)


def _accel_pct(s, w):
    # acceleration normalized by the local level magnitude (percentage 2nd derivative)
    ac = _accel(s, w)
    lvl = _mean(s, w).abs()
    return ac / lvl.replace(0, np.nan)


def _accel_log(s, w):
    # acceleration of the sign-preserving log-magnitude (multiplicative 2nd derivative)
    t = np.sign(s) * np.log1p(s.abs())
    return _accel(t, w)


def _accel_sn(s, w):
    # signal-to-noise acceleration: 2nd derivative divided by local dispersion
    ac = _accel(s, w)
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return ac / sd.replace(0, np.nan)


def _accel_rng(s, w):
    # acceleration normalized by the local peak-to-trough range (bounded 2nd derivative)
    ac = _accel(s, w)
    rng = (s.rolling(w, min_periods=max(2, w // 2)).max()
           - s.rolling(w, min_periods=max(2, w // 2)).min())
    return ac / rng.replace(0, np.nan)


# ===== working-capital ratio primitives (15 distinct base quantities) =====
def _wc01_dso(receivables, revenue):  # days-sales-outstanding proxy
    return receivables / revenue.replace(0, np.nan)


def _wc02_dpo(payables, cor):  # days-payable-outstanding proxy
    return payables / cor.replace(0, np.nan)


def _wc03_ccc(receivables, revenue, payables, cor):  # cash-conversion cycle
    return receivables / revenue.replace(0, np.nan) - payables / cor.replace(0, np.nan)


def _wc04_nwcint(workingcapital, revenue):  # net-working-capital intensity
    return workingcapital / revenue.replace(0, np.nan)


def _wc05_clcover(assetsc, liabilitiesc):  # current-liability coverage
    return assetsc / liabilitiesc.replace(0, np.nan)


def _wc06_defcush(deferredrev, revenue):  # deferred-revenue cushion
    return deferredrev / revenue.replace(0, np.nan)


def _wc07_recinassetsc(receivables, assetsc):  # receivables share of current assets
    return receivables / assetsc.replace(0, np.nan)


def _wc08_payinliabc(payables, liabilitiesc):  # payables share of current liabilities
    return payables / liabilitiesc.replace(0, np.nan)


def _wc09_rectopay(receivables, payables):  # net trade-credit balance
    return receivables / payables.replace(0, np.nan)


def _wc10_nettradeint(receivables, payables, revenue):  # net trade credit / revenue
    return (receivables - payables) / revenue.replace(0, np.nan)


def _wc11_recliabc(receivables, liabilitiesc):  # receivables vs current liabilities
    return receivables / liabilitiesc.replace(0, np.nan)


def _wc12_recrevg(receivables, revenue):  # receivables-growth-minus-revenue-growth divergence
    rg = np.log(receivables.replace(0, np.nan) / receivables.shift(63).replace(0, np.nan))
    sg = np.log(revenue.replace(0, np.nan) / revenue.shift(63).replace(0, np.nan))
    return rg - sg


def _wc13_correv(cor, revenue):  # cost-of-revenue intensity (inverse gross margin)
    return cor / revenue.replace(0, np.nan)


def _wc14_liabcint(liabilitiesc, revenue):  # current-liability intensity
    return liabilitiesc / revenue.replace(0, np.nan)


def _wc15_quickcover(assetsc, receivables, liabilitiesc):  # quick-coverage proxy
    return (assetsc - receivables) / liabilitiesc.replace(0, np.nan)


# ============================================================
# The 15 base ratios are paired with 10 windows. To keep features decorrelated,
# each window-group uses a different acceleration normalization (z / pct / sn / log / rng),
# so a base ratio's jerk is never merely a re-windowing of another's.

# ---------- window 10d : accel_z ----------
def f52wc_f52_working_capital_receivables_dso_10d_jerk_v001_signal(receivables, revenue):
    b = _accel_z(_wc01_dso(receivables, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_10d_jerk_v002_signal(payables, cor):
    b = _accel_z(_wc02_dpo(payables, cor), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_10d_jerk_v003_signal(receivables, revenue, payables, cor):
    b = _accel_z(_wc03_ccc(receivables, revenue, payables, cor), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_10d_jerk_v004_signal(workingcapital, revenue):
    b = _accel_z(_wc04_nwcint(workingcapital, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_10d_jerk_v005_signal(assetsc, liabilitiesc):
    b = _accel_z(_wc05_clcover(assetsc, liabilitiesc), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_10d_jerk_v006_signal(deferredrev, revenue):
    b = _accel_z(_wc06_defcush(deferredrev, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_10d_jerk_v007_signal(receivables, assetsc):
    b = _accel_z(_wc07_recinassetsc(receivables, assetsc), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_10d_jerk_v008_signal(payables, liabilitiesc):
    b = _accel_z(_wc08_payinliabc(payables, liabilitiesc), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_10d_jerk_v009_signal(receivables, payables):
    b = _accel_z(_wc09_rectopay(receivables, payables), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_10d_jerk_v010_signal(receivables, payables, revenue):
    b = _accel_z(_wc10_nettradeint(receivables, payables, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_10d_jerk_v011_signal(receivables, liabilitiesc):
    b = _accel_z(_wc11_recliabc(receivables, liabilitiesc), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_10d_jerk_v012_signal(receivables, revenue):
    b = _accel_z(_wc12_recrevg(receivables, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_10d_jerk_v013_signal(cor, revenue):
    b = _accel_z(_wc13_correv(cor, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_10d_jerk_v014_signal(liabilitiesc, revenue):
    b = _accel_z(_wc14_liabcint(liabilitiesc, revenue), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_10d_jerk_v015_signal(assetsc, receivables, liabilitiesc):
    b = _accel_z(_wc15_quickcover(assetsc, receivables, liabilitiesc), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 21d : accel_pct ----------
def f52wc_f52_working_capital_receivables_dso_21d_jerk_v016_signal(receivables, revenue):
    b = _accel_pct(_wc01_dso(receivables, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_21d_jerk_v017_signal(payables, cor):
    b = _accel_pct(_wc02_dpo(payables, cor), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_21d_jerk_v018_signal(receivables, revenue, payables, cor):
    b = _accel_pct(_wc03_ccc(receivables, revenue, payables, cor), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_21d_jerk_v019_signal(workingcapital, revenue):
    b = _accel_pct(_wc04_nwcint(workingcapital, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_21d_jerk_v020_signal(assetsc, liabilitiesc):
    b = _accel_pct(_wc05_clcover(assetsc, liabilitiesc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_21d_jerk_v021_signal(deferredrev, revenue):
    b = _accel_pct(_wc06_defcush(deferredrev, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_21d_jerk_v022_signal(receivables, assetsc):
    b = _accel_pct(_wc07_recinassetsc(receivables, assetsc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_21d_jerk_v023_signal(payables, liabilitiesc):
    b = _accel_pct(_wc08_payinliabc(payables, liabilitiesc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_21d_jerk_v024_signal(receivables, payables):
    b = _accel_pct(_wc09_rectopay(receivables, payables), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_21d_jerk_v025_signal(receivables, payables, revenue):
    b = _accel_pct(_wc10_nettradeint(receivables, payables, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_21d_jerk_v026_signal(receivables, liabilitiesc):
    b = _accel_pct(_wc11_recliabc(receivables, liabilitiesc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_21d_jerk_v027_signal(receivables, revenue):
    b = _accel_pct(_wc12_recrevg(receivables, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_21d_jerk_v028_signal(cor, revenue):
    b = _accel_pct(_wc13_correv(cor, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_21d_jerk_v029_signal(liabilitiesc, revenue):
    b = _accel_pct(_wc14_liabcint(liabilitiesc, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_21d_jerk_v030_signal(assetsc, receivables, liabilitiesc):
    b = _accel_pct(_wc15_quickcover(assetsc, receivables, liabilitiesc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 42d : accel_sn ----------
def f52wc_f52_working_capital_receivables_dso_42d_jerk_v031_signal(receivables, revenue):
    b = _accel_sn(_wc01_dso(receivables, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_42d_jerk_v032_signal(payables, cor):
    b = _accel_sn(_wc02_dpo(payables, cor), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_42d_jerk_v033_signal(receivables, revenue, payables, cor):
    b = _accel_sn(_wc03_ccc(receivables, revenue, payables, cor), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_42d_jerk_v034_signal(workingcapital, revenue):
    b = _accel_sn(_wc04_nwcint(workingcapital, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_42d_jerk_v035_signal(assetsc, liabilitiesc):
    b = _accel_sn(_wc05_clcover(assetsc, liabilitiesc), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_42d_jerk_v036_signal(deferredrev, revenue):
    b = _accel_sn(_wc06_defcush(deferredrev, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_42d_jerk_v037_signal(receivables, assetsc):
    b = _accel_sn(_wc07_recinassetsc(receivables, assetsc), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_42d_jerk_v038_signal(payables, liabilitiesc):
    b = _accel_sn(_wc08_payinliabc(payables, liabilitiesc), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_42d_jerk_v039_signal(receivables, payables):
    b = _accel_sn(_wc09_rectopay(receivables, payables), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_42d_jerk_v040_signal(receivables, payables, revenue):
    b = _accel_sn(_wc10_nettradeint(receivables, payables, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_42d_jerk_v041_signal(receivables, liabilitiesc):
    b = _accel_sn(_wc11_recliabc(receivables, liabilitiesc), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_42d_jerk_v042_signal(receivables, revenue):
    b = _accel_sn(_wc12_recrevg(receivables, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_42d_jerk_v043_signal(cor, revenue):
    b = _accel_sn(_wc13_correv(cor, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_42d_jerk_v044_signal(liabilitiesc, revenue):
    b = _accel_sn(_wc14_liabcint(liabilitiesc, revenue), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_42d_jerk_v045_signal(assetsc, receivables, liabilitiesc):
    b = _accel_sn(_wc15_quickcover(assetsc, receivables, liabilitiesc), 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 63d : accel_log ----------
def f52wc_f52_working_capital_receivables_dso_63d_jerk_v046_signal(receivables, revenue):
    b = _accel_log(_wc01_dso(receivables, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_63d_jerk_v047_signal(payables, cor):
    b = _accel_log(_wc02_dpo(payables, cor), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_63d_jerk_v048_signal(receivables, revenue, payables, cor):
    b = _accel_log(_wc03_ccc(receivables, revenue, payables, cor), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_63d_jerk_v049_signal(workingcapital, revenue):
    b = _accel_log(_wc04_nwcint(workingcapital, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_63d_jerk_v050_signal(assetsc, liabilitiesc):
    b = _accel_log(_wc05_clcover(assetsc, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_63d_jerk_v051_signal(deferredrev, revenue):
    b = _accel_log(_wc06_defcush(deferredrev, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_63d_jerk_v052_signal(receivables, assetsc):
    b = _accel_log(_wc07_recinassetsc(receivables, assetsc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_63d_jerk_v053_signal(payables, liabilitiesc):
    b = _accel_log(_wc08_payinliabc(payables, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_63d_jerk_v054_signal(receivables, payables):
    b = _accel_log(_wc09_rectopay(receivables, payables), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_63d_jerk_v055_signal(receivables, payables, revenue):
    b = _accel_log(_wc10_nettradeint(receivables, payables, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_63d_jerk_v056_signal(receivables, liabilitiesc):
    b = _accel_log(_wc11_recliabc(receivables, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_63d_jerk_v057_signal(receivables, revenue):
    b = _accel_log(_wc12_recrevg(receivables, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_63d_jerk_v058_signal(cor, revenue):
    b = _accel_log(_wc13_correv(cor, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_63d_jerk_v059_signal(liabilitiesc, revenue):
    b = _accel_log(_wc14_liabcint(liabilitiesc, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_63d_jerk_v060_signal(assetsc, receivables, liabilitiesc):
    b = _accel_log(_wc15_quickcover(assetsc, receivables, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 84d : accel_rng ----------
def f52wc_f52_working_capital_receivables_dso_84d_jerk_v061_signal(receivables, revenue):
    b = _accel_rng(_wc01_dso(receivables, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_84d_jerk_v062_signal(payables, cor):
    b = _accel_rng(_wc02_dpo(payables, cor), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_84d_jerk_v063_signal(receivables, revenue, payables, cor):
    b = _accel_rng(_wc03_ccc(receivables, revenue, payables, cor), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_84d_jerk_v064_signal(workingcapital, revenue):
    b = _accel_rng(_wc04_nwcint(workingcapital, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_84d_jerk_v065_signal(assetsc, liabilitiesc):
    b = _accel_rng(_wc05_clcover(assetsc, liabilitiesc), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_84d_jerk_v066_signal(deferredrev, revenue):
    b = _accel_rng(_wc06_defcush(deferredrev, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_84d_jerk_v067_signal(receivables, assetsc):
    b = _accel_rng(_wc07_recinassetsc(receivables, assetsc), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_84d_jerk_v068_signal(payables, liabilitiesc):
    b = _accel_rng(_wc08_payinliabc(payables, liabilitiesc), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_84d_jerk_v069_signal(receivables, payables):
    b = _accel_rng(_wc09_rectopay(receivables, payables), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_84d_jerk_v070_signal(receivables, payables, revenue):
    b = _accel_rng(_wc10_nettradeint(receivables, payables, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_84d_jerk_v071_signal(receivables, liabilitiesc):
    b = _accel_rng(_wc11_recliabc(receivables, liabilitiesc), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_84d_jerk_v072_signal(receivables, revenue):
    b = _accel_rng(_wc12_recrevg(receivables, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_84d_jerk_v073_signal(cor, revenue):
    b = _accel_rng(_wc13_correv(cor, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_84d_jerk_v074_signal(liabilitiesc, revenue):
    b = _accel_rng(_wc14_liabcint(liabilitiesc, revenue), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_84d_jerk_v075_signal(assetsc, receivables, liabilitiesc):
    b = _accel_rng(_wc15_quickcover(assetsc, receivables, liabilitiesc), 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 110d : accel_z ----------
def f52wc_f52_working_capital_receivables_dso_110d_jerk_v076_signal(receivables, revenue):
    b = _accel_z(_wc01_dso(receivables, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_110d_jerk_v077_signal(payables, cor):
    b = _accel_z(_wc02_dpo(payables, cor), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_110d_jerk_v078_signal(receivables, revenue, payables, cor):
    b = _accel_z(_wc03_ccc(receivables, revenue, payables, cor), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_110d_jerk_v079_signal(workingcapital, revenue):
    b = _accel_z(_wc04_nwcint(workingcapital, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_110d_jerk_v080_signal(assetsc, liabilitiesc):
    b = _accel_z(_wc05_clcover(assetsc, liabilitiesc), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_110d_jerk_v081_signal(deferredrev, revenue):
    b = _accel_z(_wc06_defcush(deferredrev, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_110d_jerk_v082_signal(receivables, assetsc):
    b = _accel_z(_wc07_recinassetsc(receivables, assetsc), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_110d_jerk_v083_signal(payables, liabilitiesc):
    b = _accel_z(_wc08_payinliabc(payables, liabilitiesc), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_110d_jerk_v084_signal(receivables, payables):
    b = _accel_z(_wc09_rectopay(receivables, payables), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_110d_jerk_v085_signal(receivables, payables, revenue):
    b = _accel_z(_wc10_nettradeint(receivables, payables, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_110d_jerk_v086_signal(receivables, liabilitiesc):
    b = _accel_z(_wc11_recliabc(receivables, liabilitiesc), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_110d_jerk_v087_signal(receivables, revenue):
    b = _accel_z(_wc12_recrevg(receivables, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_110d_jerk_v088_signal(cor, revenue):
    b = _accel_z(_wc13_correv(cor, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_110d_jerk_v089_signal(liabilitiesc, revenue):
    b = _accel_z(_wc14_liabcint(liabilitiesc, revenue), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_110d_jerk_v090_signal(assetsc, receivables, liabilitiesc):
    b = _accel_z(_wc15_quickcover(assetsc, receivables, liabilitiesc), 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 130d : accel_pct ----------
def f52wc_f52_working_capital_receivables_dso_130d_jerk_v091_signal(receivables, revenue):
    b = _accel_pct(_wc01_dso(receivables, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_130d_jerk_v092_signal(payables, cor):
    b = _accel_pct(_wc02_dpo(payables, cor), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_130d_jerk_v093_signal(receivables, revenue, payables, cor):
    b = _accel_pct(_wc03_ccc(receivables, revenue, payables, cor), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_130d_jerk_v094_signal(workingcapital, revenue):
    b = _accel_pct(_wc04_nwcint(workingcapital, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_130d_jerk_v095_signal(assetsc, liabilitiesc):
    b = _accel_pct(_wc05_clcover(assetsc, liabilitiesc), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_130d_jerk_v096_signal(deferredrev, revenue):
    b = _accel_pct(_wc06_defcush(deferredrev, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_130d_jerk_v097_signal(receivables, assetsc):
    b = _accel_pct(_wc07_recinassetsc(receivables, assetsc), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_130d_jerk_v098_signal(payables, liabilitiesc):
    b = _accel_pct(_wc08_payinliabc(payables, liabilitiesc), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_130d_jerk_v099_signal(receivables, payables):
    b = _accel_pct(_wc09_rectopay(receivables, payables), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_130d_jerk_v100_signal(receivables, payables, revenue):
    b = _accel_pct(_wc10_nettradeint(receivables, payables, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_130d_jerk_v101_signal(receivables, liabilitiesc):
    b = _accel_pct(_wc11_recliabc(receivables, liabilitiesc), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_130d_jerk_v102_signal(receivables, revenue):
    b = _accel_pct(_wc12_recrevg(receivables, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_130d_jerk_v103_signal(cor, revenue):
    b = _accel_pct(_wc13_correv(cor, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_130d_jerk_v104_signal(liabilitiesc, revenue):
    b = _accel_pct(_wc14_liabcint(liabilitiesc, revenue), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_130d_jerk_v105_signal(assetsc, receivables, liabilitiesc):
    b = _accel_pct(_wc15_quickcover(assetsc, receivables, liabilitiesc), 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 168d : accel_sn ----------
def f52wc_f52_working_capital_receivables_dso_168d_jerk_v106_signal(receivables, revenue):
    b = _accel_sn(_wc01_dso(receivables, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_168d_jerk_v107_signal(payables, cor):
    b = _accel_sn(_wc02_dpo(payables, cor), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_168d_jerk_v108_signal(receivables, revenue, payables, cor):
    b = _accel_sn(_wc03_ccc(receivables, revenue, payables, cor), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_168d_jerk_v109_signal(workingcapital, revenue):
    b = _accel_sn(_wc04_nwcint(workingcapital, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_168d_jerk_v110_signal(assetsc, liabilitiesc):
    b = _accel_sn(_wc05_clcover(assetsc, liabilitiesc), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_168d_jerk_v111_signal(deferredrev, revenue):
    b = _accel_sn(_wc06_defcush(deferredrev, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_168d_jerk_v112_signal(receivables, assetsc):
    b = _accel_sn(_wc07_recinassetsc(receivables, assetsc), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_168d_jerk_v113_signal(payables, liabilitiesc):
    b = _accel_sn(_wc08_payinliabc(payables, liabilitiesc), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_168d_jerk_v114_signal(receivables, payables):
    b = _accel_sn(_wc09_rectopay(receivables, payables), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_168d_jerk_v115_signal(receivables, payables, revenue):
    b = _accel_sn(_wc10_nettradeint(receivables, payables, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_168d_jerk_v116_signal(receivables, liabilitiesc):
    b = _accel_sn(_wc11_recliabc(receivables, liabilitiesc), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_168d_jerk_v117_signal(receivables, revenue):
    b = _accel_sn(_wc12_recrevg(receivables, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_168d_jerk_v118_signal(cor, revenue):
    b = _accel_sn(_wc13_correv(cor, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_168d_jerk_v119_signal(liabilitiesc, revenue):
    b = _accel_sn(_wc14_liabcint(liabilitiesc, revenue), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_168d_jerk_v120_signal(assetsc, receivables, liabilitiesc):
    b = _accel_sn(_wc15_quickcover(assetsc, receivables, liabilitiesc), 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 210d : accel_log ----------
def f52wc_f52_working_capital_receivables_dso_210d_jerk_v121_signal(receivables, revenue):
    b = _accel_log(_wc01_dso(receivables, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_210d_jerk_v122_signal(payables, cor):
    b = _accel_log(_wc02_dpo(payables, cor), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_210d_jerk_v123_signal(receivables, revenue, payables, cor):
    b = _accel_log(_wc03_ccc(receivables, revenue, payables, cor), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_210d_jerk_v124_signal(workingcapital, revenue):
    b = _accel_log(_wc04_nwcint(workingcapital, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_210d_jerk_v125_signal(assetsc, liabilitiesc):
    b = _accel_log(_wc05_clcover(assetsc, liabilitiesc), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_210d_jerk_v126_signal(deferredrev, revenue):
    b = _accel_log(_wc06_defcush(deferredrev, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_210d_jerk_v127_signal(receivables, assetsc):
    b = _accel_log(_wc07_recinassetsc(receivables, assetsc), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_210d_jerk_v128_signal(payables, liabilitiesc):
    b = _accel_log(_wc08_payinliabc(payables, liabilitiesc), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_210d_jerk_v129_signal(receivables, payables):
    b = _accel_log(_wc09_rectopay(receivables, payables), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_210d_jerk_v130_signal(receivables, payables, revenue):
    b = _accel_log(_wc10_nettradeint(receivables, payables, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_210d_jerk_v131_signal(receivables, liabilitiesc):
    b = _accel_log(_wc11_recliabc(receivables, liabilitiesc), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_210d_jerk_v132_signal(receivables, revenue):
    b = _accel_log(_wc12_recrevg(receivables, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_210d_jerk_v133_signal(cor, revenue):
    b = _accel_log(_wc13_correv(cor, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_210d_jerk_v134_signal(liabilitiesc, revenue):
    b = _accel_log(_wc14_liabcint(liabilitiesc, revenue), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_210d_jerk_v135_signal(assetsc, receivables, liabilitiesc):
    b = _accel_log(_wc15_quickcover(assetsc, receivables, liabilitiesc), 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---------- window 252d : accel_rng ----------
def f52wc_f52_working_capital_receivables_dso_252d_jerk_v136_signal(receivables, revenue):
    b = _accel_rng(_wc01_dso(receivables, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_dpo_252d_jerk_v137_signal(payables, cor):
    b = _accel_rng(_wc02_dpo(payables, cor), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_ccc_252d_jerk_v138_signal(receivables, revenue, payables, cor):
    b = _accel_rng(_wc03_ccc(receivables, revenue, payables, cor), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nwcint_252d_jerk_v139_signal(workingcapital, revenue):
    b = _accel_rng(_wc04_nwcint(workingcapital, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_clcover_252d_jerk_v140_signal(assetsc, liabilitiesc):
    b = _accel_rng(_wc05_clcover(assetsc, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_defcush_252d_jerk_v141_signal(deferredrev, revenue):
    b = _accel_rng(_wc06_defcush(deferredrev, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recinassetsc_252d_jerk_v142_signal(receivables, assetsc):
    b = _accel_rng(_wc07_recinassetsc(receivables, assetsc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_payinliabc_252d_jerk_v143_signal(payables, liabilitiesc):
    b = _accel_rng(_wc08_payinliabc(payables, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_rectopay_252d_jerk_v144_signal(receivables, payables):
    b = _accel_rng(_wc09_rectopay(receivables, payables), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_nettradeint_252d_jerk_v145_signal(receivables, payables, revenue):
    b = _accel_rng(_wc10_nettradeint(receivables, payables, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recliabc_252d_jerk_v146_signal(receivables, liabilitiesc):
    b = _accel_rng(_wc11_recliabc(receivables, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_recrevg_252d_jerk_v147_signal(receivables, revenue):
    b = _accel_rng(_wc12_recrevg(receivables, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_correv_252d_jerk_v148_signal(cor, revenue):
    b = _accel_rng(_wc13_correv(cor, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_liabcint_252d_jerk_v149_signal(liabilitiesc, revenue):
    b = _accel_rng(_wc14_liabcint(liabilitiesc, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f52wc_f52_working_capital_receivables_quickcover_252d_jerk_v150_signal(assetsc, receivables, liabilitiesc):
    b = _accel_rng(_wc15_quickcover(assetsc, receivables, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f52wc_f52_working_capital_receivables_dso_10d_jerk_v001_signal,
    f52wc_f52_working_capital_receivables_dpo_10d_jerk_v002_signal,
    f52wc_f52_working_capital_receivables_ccc_10d_jerk_v003_signal,
    f52wc_f52_working_capital_receivables_nwcint_10d_jerk_v004_signal,
    f52wc_f52_working_capital_receivables_clcover_10d_jerk_v005_signal,
    f52wc_f52_working_capital_receivables_defcush_10d_jerk_v006_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_10d_jerk_v007_signal,
    f52wc_f52_working_capital_receivables_payinliabc_10d_jerk_v008_signal,
    f52wc_f52_working_capital_receivables_rectopay_10d_jerk_v009_signal,
    f52wc_f52_working_capital_receivables_nettradeint_10d_jerk_v010_signal,
    f52wc_f52_working_capital_receivables_recliabc_10d_jerk_v011_signal,
    f52wc_f52_working_capital_receivables_recrevg_10d_jerk_v012_signal,
    f52wc_f52_working_capital_receivables_correv_10d_jerk_v013_signal,
    f52wc_f52_working_capital_receivables_liabcint_10d_jerk_v014_signal,
    f52wc_f52_working_capital_receivables_quickcover_10d_jerk_v015_signal,
    f52wc_f52_working_capital_receivables_dso_21d_jerk_v016_signal,
    f52wc_f52_working_capital_receivables_dpo_21d_jerk_v017_signal,
    f52wc_f52_working_capital_receivables_ccc_21d_jerk_v018_signal,
    f52wc_f52_working_capital_receivables_nwcint_21d_jerk_v019_signal,
    f52wc_f52_working_capital_receivables_clcover_21d_jerk_v020_signal,
    f52wc_f52_working_capital_receivables_defcush_21d_jerk_v021_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_21d_jerk_v022_signal,
    f52wc_f52_working_capital_receivables_payinliabc_21d_jerk_v023_signal,
    f52wc_f52_working_capital_receivables_rectopay_21d_jerk_v024_signal,
    f52wc_f52_working_capital_receivables_nettradeint_21d_jerk_v025_signal,
    f52wc_f52_working_capital_receivables_recliabc_21d_jerk_v026_signal,
    f52wc_f52_working_capital_receivables_recrevg_21d_jerk_v027_signal,
    f52wc_f52_working_capital_receivables_correv_21d_jerk_v028_signal,
    f52wc_f52_working_capital_receivables_liabcint_21d_jerk_v029_signal,
    f52wc_f52_working_capital_receivables_quickcover_21d_jerk_v030_signal,
    f52wc_f52_working_capital_receivables_dso_42d_jerk_v031_signal,
    f52wc_f52_working_capital_receivables_dpo_42d_jerk_v032_signal,
    f52wc_f52_working_capital_receivables_ccc_42d_jerk_v033_signal,
    f52wc_f52_working_capital_receivables_nwcint_42d_jerk_v034_signal,
    f52wc_f52_working_capital_receivables_clcover_42d_jerk_v035_signal,
    f52wc_f52_working_capital_receivables_defcush_42d_jerk_v036_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_42d_jerk_v037_signal,
    f52wc_f52_working_capital_receivables_payinliabc_42d_jerk_v038_signal,
    f52wc_f52_working_capital_receivables_rectopay_42d_jerk_v039_signal,
    f52wc_f52_working_capital_receivables_nettradeint_42d_jerk_v040_signal,
    f52wc_f52_working_capital_receivables_recliabc_42d_jerk_v041_signal,
    f52wc_f52_working_capital_receivables_recrevg_42d_jerk_v042_signal,
    f52wc_f52_working_capital_receivables_correv_42d_jerk_v043_signal,
    f52wc_f52_working_capital_receivables_liabcint_42d_jerk_v044_signal,
    f52wc_f52_working_capital_receivables_quickcover_42d_jerk_v045_signal,
    f52wc_f52_working_capital_receivables_dso_63d_jerk_v046_signal,
    f52wc_f52_working_capital_receivables_dpo_63d_jerk_v047_signal,
    f52wc_f52_working_capital_receivables_ccc_63d_jerk_v048_signal,
    f52wc_f52_working_capital_receivables_nwcint_63d_jerk_v049_signal,
    f52wc_f52_working_capital_receivables_clcover_63d_jerk_v050_signal,
    f52wc_f52_working_capital_receivables_defcush_63d_jerk_v051_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_63d_jerk_v052_signal,
    f52wc_f52_working_capital_receivables_payinliabc_63d_jerk_v053_signal,
    f52wc_f52_working_capital_receivables_rectopay_63d_jerk_v054_signal,
    f52wc_f52_working_capital_receivables_nettradeint_63d_jerk_v055_signal,
    f52wc_f52_working_capital_receivables_recliabc_63d_jerk_v056_signal,
    f52wc_f52_working_capital_receivables_recrevg_63d_jerk_v057_signal,
    f52wc_f52_working_capital_receivables_correv_63d_jerk_v058_signal,
    f52wc_f52_working_capital_receivables_liabcint_63d_jerk_v059_signal,
    f52wc_f52_working_capital_receivables_quickcover_63d_jerk_v060_signal,
    f52wc_f52_working_capital_receivables_dso_84d_jerk_v061_signal,
    f52wc_f52_working_capital_receivables_dpo_84d_jerk_v062_signal,
    f52wc_f52_working_capital_receivables_ccc_84d_jerk_v063_signal,
    f52wc_f52_working_capital_receivables_nwcint_84d_jerk_v064_signal,
    f52wc_f52_working_capital_receivables_clcover_84d_jerk_v065_signal,
    f52wc_f52_working_capital_receivables_defcush_84d_jerk_v066_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_84d_jerk_v067_signal,
    f52wc_f52_working_capital_receivables_payinliabc_84d_jerk_v068_signal,
    f52wc_f52_working_capital_receivables_rectopay_84d_jerk_v069_signal,
    f52wc_f52_working_capital_receivables_nettradeint_84d_jerk_v070_signal,
    f52wc_f52_working_capital_receivables_recliabc_84d_jerk_v071_signal,
    f52wc_f52_working_capital_receivables_recrevg_84d_jerk_v072_signal,
    f52wc_f52_working_capital_receivables_correv_84d_jerk_v073_signal,
    f52wc_f52_working_capital_receivables_liabcint_84d_jerk_v074_signal,
    f52wc_f52_working_capital_receivables_quickcover_84d_jerk_v075_signal,
    f52wc_f52_working_capital_receivables_dso_110d_jerk_v076_signal,
    f52wc_f52_working_capital_receivables_dpo_110d_jerk_v077_signal,
    f52wc_f52_working_capital_receivables_ccc_110d_jerk_v078_signal,
    f52wc_f52_working_capital_receivables_nwcint_110d_jerk_v079_signal,
    f52wc_f52_working_capital_receivables_clcover_110d_jerk_v080_signal,
    f52wc_f52_working_capital_receivables_defcush_110d_jerk_v081_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_110d_jerk_v082_signal,
    f52wc_f52_working_capital_receivables_payinliabc_110d_jerk_v083_signal,
    f52wc_f52_working_capital_receivables_rectopay_110d_jerk_v084_signal,
    f52wc_f52_working_capital_receivables_nettradeint_110d_jerk_v085_signal,
    f52wc_f52_working_capital_receivables_recliabc_110d_jerk_v086_signal,
    f52wc_f52_working_capital_receivables_recrevg_110d_jerk_v087_signal,
    f52wc_f52_working_capital_receivables_correv_110d_jerk_v088_signal,
    f52wc_f52_working_capital_receivables_liabcint_110d_jerk_v089_signal,
    f52wc_f52_working_capital_receivables_quickcover_110d_jerk_v090_signal,
    f52wc_f52_working_capital_receivables_dso_130d_jerk_v091_signal,
    f52wc_f52_working_capital_receivables_dpo_130d_jerk_v092_signal,
    f52wc_f52_working_capital_receivables_ccc_130d_jerk_v093_signal,
    f52wc_f52_working_capital_receivables_nwcint_130d_jerk_v094_signal,
    f52wc_f52_working_capital_receivables_clcover_130d_jerk_v095_signal,
    f52wc_f52_working_capital_receivables_defcush_130d_jerk_v096_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_130d_jerk_v097_signal,
    f52wc_f52_working_capital_receivables_payinliabc_130d_jerk_v098_signal,
    f52wc_f52_working_capital_receivables_rectopay_130d_jerk_v099_signal,
    f52wc_f52_working_capital_receivables_nettradeint_130d_jerk_v100_signal,
    f52wc_f52_working_capital_receivables_recliabc_130d_jerk_v101_signal,
    f52wc_f52_working_capital_receivables_recrevg_130d_jerk_v102_signal,
    f52wc_f52_working_capital_receivables_correv_130d_jerk_v103_signal,
    f52wc_f52_working_capital_receivables_liabcint_130d_jerk_v104_signal,
    f52wc_f52_working_capital_receivables_quickcover_130d_jerk_v105_signal,
    f52wc_f52_working_capital_receivables_dso_168d_jerk_v106_signal,
    f52wc_f52_working_capital_receivables_dpo_168d_jerk_v107_signal,
    f52wc_f52_working_capital_receivables_ccc_168d_jerk_v108_signal,
    f52wc_f52_working_capital_receivables_nwcint_168d_jerk_v109_signal,
    f52wc_f52_working_capital_receivables_clcover_168d_jerk_v110_signal,
    f52wc_f52_working_capital_receivables_defcush_168d_jerk_v111_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_168d_jerk_v112_signal,
    f52wc_f52_working_capital_receivables_payinliabc_168d_jerk_v113_signal,
    f52wc_f52_working_capital_receivables_rectopay_168d_jerk_v114_signal,
    f52wc_f52_working_capital_receivables_nettradeint_168d_jerk_v115_signal,
    f52wc_f52_working_capital_receivables_recliabc_168d_jerk_v116_signal,
    f52wc_f52_working_capital_receivables_recrevg_168d_jerk_v117_signal,
    f52wc_f52_working_capital_receivables_correv_168d_jerk_v118_signal,
    f52wc_f52_working_capital_receivables_liabcint_168d_jerk_v119_signal,
    f52wc_f52_working_capital_receivables_quickcover_168d_jerk_v120_signal,
    f52wc_f52_working_capital_receivables_dso_210d_jerk_v121_signal,
    f52wc_f52_working_capital_receivables_dpo_210d_jerk_v122_signal,
    f52wc_f52_working_capital_receivables_ccc_210d_jerk_v123_signal,
    f52wc_f52_working_capital_receivables_nwcint_210d_jerk_v124_signal,
    f52wc_f52_working_capital_receivables_clcover_210d_jerk_v125_signal,
    f52wc_f52_working_capital_receivables_defcush_210d_jerk_v126_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_210d_jerk_v127_signal,
    f52wc_f52_working_capital_receivables_payinliabc_210d_jerk_v128_signal,
    f52wc_f52_working_capital_receivables_rectopay_210d_jerk_v129_signal,
    f52wc_f52_working_capital_receivables_nettradeint_210d_jerk_v130_signal,
    f52wc_f52_working_capital_receivables_recliabc_210d_jerk_v131_signal,
    f52wc_f52_working_capital_receivables_recrevg_210d_jerk_v132_signal,
    f52wc_f52_working_capital_receivables_correv_210d_jerk_v133_signal,
    f52wc_f52_working_capital_receivables_liabcint_210d_jerk_v134_signal,
    f52wc_f52_working_capital_receivables_quickcover_210d_jerk_v135_signal,
    f52wc_f52_working_capital_receivables_dso_252d_jerk_v136_signal,
    f52wc_f52_working_capital_receivables_dpo_252d_jerk_v137_signal,
    f52wc_f52_working_capital_receivables_ccc_252d_jerk_v138_signal,
    f52wc_f52_working_capital_receivables_nwcint_252d_jerk_v139_signal,
    f52wc_f52_working_capital_receivables_clcover_252d_jerk_v140_signal,
    f52wc_f52_working_capital_receivables_defcush_252d_jerk_v141_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_252d_jerk_v142_signal,
    f52wc_f52_working_capital_receivables_payinliabc_252d_jerk_v143_signal,
    f52wc_f52_working_capital_receivables_rectopay_252d_jerk_v144_signal,
    f52wc_f52_working_capital_receivables_nettradeint_252d_jerk_v145_signal,
    f52wc_f52_working_capital_receivables_recliabc_252d_jerk_v146_signal,
    f52wc_f52_working_capital_receivables_recrevg_252d_jerk_v147_signal,
    f52wc_f52_working_capital_receivables_correv_252d_jerk_v148_signal,
    f52wc_f52_working_capital_receivables_liabcint_252d_jerk_v149_signal,
    f52wc_f52_working_capital_receivables_quickcover_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F52_WORKING_CAPITAL_RECEIVABLES_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    receivables = _fund(201, base=8e7, drift=0.030, vol=0.07).rename("receivables")
    payables = _fund(202, base=5e7, drift=0.025, vol=0.08).rename("payables")
    deferredrev = _fund(203, base=4e7, drift=0.035, vol=0.09).rename("deferredrev")
    workingcapital = _fund(204, base=6e7, drift=0.015, vol=0.10, allow_neg=True).rename("workingcapital")
    liabilitiesc = _fund(205, base=1.1e8, drift=0.022, vol=0.06).rename("liabilitiesc")
    assetsc = _fund(206, base=1.7e8, drift=0.024, vol=0.05).rename("assetsc")
    revenue = _fund(207, base=3e8, drift=0.028, vol=0.06).rename("revenue")
    cor = _fund(208, base=1.8e8, drift=0.026, vol=0.07).rename("cor")

    cols = {
        "receivables": receivables, "payables": payables, "deferredrev": deferredrev,
        "workingcapital": workingcapital, "liabilitiesc": liabilitiesc, "assetsc": assetsc,
        "revenue": revenue, "cor": cor,
    }

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps", "de", "ncfdiv", "ncfinv", "dps",
        "divyield", "payoutratio", "prefdivis", "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue", "fndvalue", "undvalue", "prfvalue",
        "fndunits", "undunits",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    print("OK f52_working_capital_receivables_3rd_derivatives_001_150_claude: %d features pass" % n_features)
