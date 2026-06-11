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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (Altman-Z / distress / runway) =====
def _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    a = assets.replace(0, np.nan)
    return (1.2 * (workingcapital / a) + 1.4 * (retearn / a) + 3.3 * (ebit / a)
            + 0.6 * (equity / liabilities.replace(0, np.nan)) + 1.0 * (revenue / a))


def _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets):
    a = assets.replace(0, np.nan)
    return (6.56 * (workingcapital / a) + 3.26 * (retearn / a) + 6.72 * (ebit / a)
            + 1.05 * (equity / liabilities.replace(0, np.nan)))


def _f37_runway(cashneq, opex):
    return cashneq / opex.replace(0, np.nan)


# ============================================================
def f37da_f37_distress_risk_altman_wcassetsa_63d_jerk_v001_signal(workingcapital, assets):
    x = _safe_div(workingcapital, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcassetsb_63d_jerk_v002_signal(workingcapital, assets):
    x = _safe_div(workingcapital, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcassetsc_63d_jerk_v003_signal(workingcapital, assets):
    x = _safe_div(workingcapital, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reassetsa_63d_jerk_v004_signal(retearn, assets):
    x = _safe_div(retearn, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reassetsb_63d_jerk_v005_signal(retearn, assets):
    x = _safe_div(retearn, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reassetsc_63d_jerk_v006_signal(retearn, assets):
    x = _safe_div(retearn, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitassetsa_63d_jerk_v007_signal(ebit, assets):
    x = _safe_div(ebit, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitassetsb_63d_jerk_v008_signal(ebit, assets):
    x = _safe_div(ebit, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitassetsc_63d_jerk_v009_signal(ebit, assets):
    x = _safe_div(ebit, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqliaba_63d_jerk_v010_signal(equity, liabilities):
    x = _safe_div(equity, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqliabb_63d_jerk_v011_signal(equity, liabilities):
    x = _safe_div(equity, liabilities)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqliabc_63d_jerk_v012_signal(equity, liabilities):
    x = _safe_div(equity, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_revassetsa_63d_jerk_v013_signal(revenue, assets):
    x = _safe_div(revenue, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_revassetsb_63d_jerk_v014_signal(revenue, assets):
    x = _safe_div(revenue, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_revassetsc_63d_jerk_v015_signal(revenue, assets):
    x = _safe_div(revenue, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zscorea_63d_jerk_v016_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zscoreb_63d_jerk_v017_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zscorec_63d_jerk_v018_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zprimea_63d_jerk_v019_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    x = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zprimeb_63d_jerk_v020_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    x = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zprimec_63d_jerk_v021_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    x = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwaya_63d_jerk_v022_signal(cashneq, opex):
    x = _f37_runway(cashneq, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayb_63d_jerk_v023_signal(cashneq, opex):
    x = _f37_runway(cashneq, opex)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayc_63d_jerk_v024_signal(cashneq, opex):
    x = _f37_runway(cashneq, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayreva_63d_jerk_v025_signal(cashneq, opex, revenue):
    x = _safe_div(cashneq, opex) * _safe_div(revenue, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayrevb_63d_jerk_v026_signal(cashneq, opex, revenue):
    x = _safe_div(cashneq, opex) * _safe_div(revenue, opex)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayrevc_63d_jerk_v027_signal(cashneq, opex, revenue):
    x = _safe_div(cashneq, opex) * _safe_div(revenue, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_burnstressa_21d_jerk_v028_signal(opex, cashneq):
    x = _safe_div(opex, cashneq)
    base = _mean(x, 7)
    d1 = base - base.shift(5)
    b = d1 - d1.shift(5)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_burnstressb_21d_jerk_v029_signal(opex, cashneq):
    x = _safe_div(opex, cashneq)
    base = _z(x, 63)
    d1 = base - base.shift(10)
    b = d1 - d1.shift(10)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_burnstressc_21d_jerk_v030_signal(opex, cashneq):
    x = _safe_div(opex, cashneq)
    base = _mean(x, 7)
    d1 = base - base.shift(5)
    acc = d1 - d1.shift(5)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitcovera_126d_jerk_v031_signal(ebit, opex):
    x = _z(_safe_div(ebit, opex), 126)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitcoverb_126d_jerk_v032_signal(ebit, opex):
    x = _z(_safe_div(ebit, opex), 126)
    base = _z(x, 126)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitcoverc_126d_jerk_v033_signal(ebit, opex):
    x = _z(_safe_div(ebit, opex), 126)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_oprunwaya_63d_jerk_v034_signal(cashneq, ebit, opex):
    x = _safe_div(cashneq + ebit, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_oprunwayb_63d_jerk_v035_signal(cashneq, ebit, opex):
    x = _safe_div(cashneq + ebit, opex)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_oprunwayc_63d_jerk_v036_signal(cashneq, ebit, opex):
    x = _safe_div(cashneq + ebit, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabassetsa_63d_jerk_v037_signal(liabilities, assets):
    x = _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabassetsb_63d_jerk_v038_signal(liabilities, assets):
    x = _safe_div(liabilities, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabassetsc_63d_jerk_v039_signal(liabilities, assets):
    x = _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabebita_63d_jerk_v040_signal(liabilities, ebit):
    x = _safe_div(liabilities, ebit)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabebitb_63d_jerk_v041_signal(liabilities, ebit):
    x = _safe_div(liabilities, ebit)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabebitc_63d_jerk_v042_signal(liabilities, ebit):
    x = _safe_div(liabilities, ebit)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabreva_63d_jerk_v043_signal(liabilities, revenue):
    x = _safe_div(liabilities, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabrevb_63d_jerk_v044_signal(liabilities, revenue):
    x = _safe_div(liabilities, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liabrevc_63d_jerk_v045_signal(liabilities, revenue):
    x = _safe_div(liabilities, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqassetsa_63d_jerk_v046_signal(equity, assets):
    x = _safe_div(equity, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqassetsb_63d_jerk_v047_signal(equity, assets):
    x = _safe_div(equity, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_eqassetsc_63d_jerk_v048_signal(equity, assets):
    x = _safe_div(equity, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netdebta_63d_jerk_v049_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netdebtb_63d_jerk_v050_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netdebtc_63d_jerk_v051_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_debttoeqa_63d_jerk_v052_signal(liabilities, equity):
    x = _safe_div(liabilities, equity)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_debttoeqb_63d_jerk_v053_signal(liabilities, equity):
    x = _safe_div(liabilities, equity)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_debttoeqc_63d_jerk_v054_signal(liabilities, equity):
    x = _safe_div(liabilities, equity)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashassetsa_63d_jerk_v055_signal(cashneq, assets):
    x = _safe_div(cashneq, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashassetsb_63d_jerk_v056_signal(cashneq, assets):
    x = _safe_div(cashneq, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashassetsc_63d_jerk_v057_signal(cashneq, assets):
    x = _safe_div(cashneq, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashliaba_63d_jerk_v058_signal(cashneq, liabilities):
    x = _safe_div(cashneq, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashliabb_63d_jerk_v059_signal(cashneq, liabilities):
    x = _safe_div(cashneq, liabilities)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashliabc_63d_jerk_v060_signal(cashneq, liabilities):
    x = _safe_div(cashneq, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashreva_63d_jerk_v061_signal(cashneq, revenue):
    x = _safe_div(cashneq, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashrevb_63d_jerk_v062_signal(cashneq, revenue):
    x = _safe_div(cashneq, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashrevc_63d_jerk_v063_signal(cashneq, revenue):
    x = _safe_div(cashneq, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcliaba_63d_jerk_v064_signal(workingcapital, liabilities):
    x = _safe_div(workingcapital, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcliabb_63d_jerk_v065_signal(workingcapital, liabilities):
    x = _safe_div(workingcapital, liabilities)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcliabc_63d_jerk_v066_signal(workingcapital, liabilities):
    x = _safe_div(workingcapital, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcreva_63d_jerk_v067_signal(workingcapital, revenue):
    x = _safe_div(workingcapital, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcrevb_63d_jerk_v068_signal(workingcapital, revenue):
    x = _safe_div(workingcapital, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_wcrevc_63d_jerk_v069_signal(workingcapital, revenue):
    x = _safe_div(workingcapital, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_recasha_63d_jerk_v070_signal(retearn, cashneq):
    x = np.tanh(_safe_div(retearn, cashneq))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_recashb_63d_jerk_v071_signal(retearn, cashneq):
    x = np.tanh(_safe_div(retearn, cashneq))
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_recashc_63d_jerk_v072_signal(retearn, cashneq):
    x = np.tanh(_safe_div(retearn, cashneq))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reliaba_63d_jerk_v073_signal(retearn, liabilities):
    x = _safe_div(retearn, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reliabb_63d_jerk_v074_signal(retearn, liabilities):
    x = _safe_div(retearn, liabilities)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_reliabc_63d_jerk_v075_signal(retearn, liabilities):
    x = _safe_div(retearn, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitliaba_63d_jerk_v076_signal(ebit, liabilities):
    x = _safe_div(ebit, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitliabb_63d_jerk_v077_signal(ebit, liabilities):
    x = _safe_div(ebit, liabilities)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitliabc_63d_jerk_v078_signal(ebit, liabilities):
    x = _safe_div(ebit, liabilities)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitopexa_63d_jerk_v079_signal(ebit, opex, revenue):
    x = _safe_div(ebit, opex) - _safe_div(ebit, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitopexb_63d_jerk_v080_signal(ebit, opex, revenue):
    x = _safe_div(ebit, opex) - _safe_div(ebit, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitopexc_63d_jerk_v081_signal(ebit, opex, revenue):
    x = _safe_div(ebit, opex) - _safe_div(ebit, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexreva_63d_jerk_v082_signal(opex, revenue):
    x = _safe_div(opex, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexrevb_63d_jerk_v083_signal(opex, revenue):
    x = _safe_div(opex, revenue)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexrevc_63d_jerk_v084_signal(opex, revenue):
    x = _safe_div(opex, revenue)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexassetsa_63d_jerk_v085_signal(opex, assets):
    x = _safe_div(opex, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexassetsb_63d_jerk_v086_signal(opex, assets):
    x = _safe_div(opex, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opexassetsc_63d_jerk_v087_signal(opex, assets):
    x = _safe_div(opex, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opsurplusa_63d_jerk_v088_signal(revenue, opex, assets):
    x = _safe_div(revenue - opex, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opsurplusb_63d_jerk_v089_signal(revenue, opex, assets):
    x = _safe_div(revenue - opex, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_opsurplusc_63d_jerk_v090_signal(revenue, opex, assets):
    x = _safe_div(revenue - opex, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_capadeqa_63d_jerk_v091_signal(retearn, assets, cashneq):
    x = _safe_div(retearn, assets) * np.tanh(_safe_div(cashneq, assets))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_capadeqb_63d_jerk_v092_signal(retearn, assets, cashneq):
    x = _safe_div(retearn, assets) * np.tanh(_safe_div(cashneq, assets))
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_capadeqc_63d_jerk_v093_signal(retearn, assets, cashneq):
    x = _safe_div(retearn, assets) * np.tanh(_safe_div(cashneq, assets))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zscza_252d_jerk_v094_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = _z(z, 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zsczb_252d_jerk_v095_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = _z(z, 252)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zsczc_252d_jerk_v096_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = _z(z, 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayza_252d_jerk_v097_signal(cashneq, opex):
    x = _z(_f37_runway(cashneq, opex), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayzb_252d_jerk_v098_signal(cashneq, opex):
    x = _z(_f37_runway(cashneq, opex), 252)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_runwayzc_252d_jerk_v099_signal(cashneq, opex):
    x = _z(_f37_runway(cashneq, opex), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_levza_252d_jerk_v100_signal(liabilities, assets):
    x = _z(_safe_div(liabilities, assets), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_levzb_252d_jerk_v101_signal(liabilities, assets):
    x = _z(_safe_div(liabilities, assets), 252)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_levzc_252d_jerk_v102_signal(liabilities, assets):
    x = _z(_safe_div(liabilities, assets), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitza_252d_jerk_v103_signal(ebit, assets):
    x = _z(_safe_div(ebit, assets), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitzb_252d_jerk_v104_signal(ebit, assets):
    x = _z(_safe_div(ebit, assets), 252)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitzc_252d_jerk_v105_signal(ebit, assets):
    x = _z(_safe_div(ebit, assets), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvza_252d_jerk_v106_signal(equity, liabilities):
    x = _z(_safe_div(equity, liabilities), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvzb_252d_jerk_v107_signal(equity, liabilities):
    x = _z(_safe_div(equity, liabilities), 252)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvzc_252d_jerk_v108_signal(equity, liabilities):
    x = _z(_safe_div(equity, liabilities), 252)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashza_126d_jerk_v109_signal(cashneq, assets):
    x = _z(_safe_div(cashneq, assets), 126)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashzb_126d_jerk_v110_signal(cashneq, assets):
    x = _z(_safe_div(cashneq, assets), 126)
    base = _z(x, 126)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_cashzc_126d_jerk_v111_signal(cashneq, assets):
    x = _z(_safe_div(cashneq, assets), 126)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zgapfloora_63d_jerk_v112_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    d_low = (z - 1.81).abs()
    d_high = (z - 2.99).abs()
    x = pd.concat([d_low, d_high], axis=1).min(axis=1)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zgapfloorb_63d_jerk_v113_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    d_low = (z - 1.81).abs()
    d_high = (z - 2.99).abs()
    x = pd.concat([d_low, d_high], axis=1).min(axis=1)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zgapfloorc_63d_jerk_v114_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    d_low = (z - 1.81).abs()
    d_high = (z - 2.99).abs()
    x = pd.concat([d_low, d_high], axis=1).min(axis=1)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zinstaba_63d_jerk_v115_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = z.rolling(63, min_periods=21).std()
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zinstabb_63d_jerk_v116_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = z.rolling(63, min_periods=21).std()
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zinstabc_63d_jerk_v117_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x = z.rolling(63, min_periods=21).std()
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitwca_63d_jerk_v118_signal(ebit, workingcapital):
    x = np.tanh(_safe_div(ebit, workingcapital))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitwcb_63d_jerk_v119_signal(ebit, workingcapital):
    x = np.tanh(_safe_div(ebit, workingcapital))
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_ebitwcc_63d_jerk_v120_signal(ebit, workingcapital):
    x = np.tanh(_safe_div(ebit, workingcapital))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_x2x5a_63d_jerk_v121_signal(retearn, revenue, assets):
    x = _safe_div(retearn, assets) - _safe_div(revenue, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_x2x5b_63d_jerk_v122_signal(retearn, revenue, assets):
    x = _safe_div(retearn, assets) - _safe_div(revenue, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_x2x5c_63d_jerk_v123_signal(retearn, revenue, assets):
    x = _safe_div(retearn, assets) - _safe_div(revenue, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqcompa_63d_jerk_v124_signal(cashneq, workingcapital, assets):
    x = _safe_div(cashneq, assets) + 0.5 * np.tanh(_safe_div(workingcapital, assets))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqcompb_63d_jerk_v125_signal(cashneq, workingcapital, assets):
    x = _safe_div(cashneq, assets) + 0.5 * np.tanh(_safe_div(workingcapital, assets))
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqcompc_63d_jerk_v126_signal(cashneq, workingcapital, assets):
    x = _safe_div(cashneq, assets) + 0.5 * np.tanh(_safe_div(workingcapital, assets))
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvbala_63d_jerk_v127_signal(equity, liabilities, cashneq, opex):
    x = np.tanh(_safe_div(equity, liabilities)) * _safe_div(cashneq, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvbalb_63d_jerk_v128_signal(equity, liabilities, cashneq, opex):
    x = np.tanh(_safe_div(equity, liabilities)) * _safe_div(cashneq, opex)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_solvbalc_63d_jerk_v129_signal(equity, liabilities, cashneq, opex):
    x = np.tanh(_safe_div(equity, liabilities)) * _safe_div(cashneq, opex)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_fragilitya_63d_jerk_v130_signal(liabilities, assets, ebit):
    lev = _safe_div(liabilities, assets)
    cov = _safe_div(ebit, liabilities)
    x = lev / (cov.abs() + 0.01)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_fragilityb_63d_jerk_v131_signal(liabilities, assets, ebit):
    lev = _safe_div(liabilities, assets)
    cov = _safe_div(ebit, liabilities)
    x = lev / (cov.abs() + 0.01)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_fragilityc_63d_jerk_v132_signal(liabilities, assets, ebit):
    lev = _safe_div(liabilities, assets)
    cov = _safe_div(ebit, liabilities)
    x = lev / (cov.abs() + 0.01)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqstressa_63d_jerk_v133_signal(opex, cashneq, liabilities, assets):
    x = _safe_div(opex, cashneq) * _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqstressb_63d_jerk_v134_signal(opex, cashneq, liabilities, assets):
    x = _safe_div(opex, cashneq) * _safe_div(liabilities, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_liqstressc_63d_jerk_v135_signal(opex, cashneq, liabilities, assets):
    x = _safe_div(opex, cashneq) * _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_severitya_63d_jerk_v136_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    x = p * _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_severityb_63d_jerk_v137_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    x = p * _safe_div(liabilities, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_severityc_63d_jerk_v138_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    x = p * _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_selffunda_63d_jerk_v139_signal(revenue, opex, cashneq):
    x = _safe_div(revenue - opex, cashneq)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_selffundb_63d_jerk_v140_signal(revenue, opex, cashneq):
    x = _safe_div(revenue - opex, cashneq)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_selffundc_63d_jerk_v141_signal(revenue, opex, cashneq):
    x = _safe_div(revenue - opex, cashneq)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netliaba_126d_jerk_v142_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netliabb_126d_jerk_v143_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _z(x, 126)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_netliabc_126d_jerk_v144_signal(liabilities, cashneq, assets):
    x = _safe_div(liabilities - cashneq, assets)
    base = _mean(x, 42)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zrobusta_252d_jerk_v145_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    med = z.rolling(252, min_periods=63).median()
    mad = (z - med).abs().rolling(252, min_periods=63).median()
    x = (z - med) / (1.4826 * mad).replace(0, np.nan)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    b = d1 - d1.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zrobustb_252d_jerk_v146_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    med = z.rolling(252, min_periods=63).median()
    mad = (z - med).abs().rolling(252, min_periods=63).median()
    x = (z - med) / (1.4826 * mad).replace(0, np.nan)
    base = _z(x, 252)
    d1 = base - base.shift(126)
    b = d1 - d1.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_zrobustc_252d_jerk_v147_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    med = z.rolling(252, min_periods=63).median()
    mad = (z - med).abs().rolling(252, min_periods=63).median()
    x = (z - med) / (1.4826 * mad).replace(0, np.nan)
    base = _mean(x, 84)
    d1 = base - base.shift(63)
    acc = d1 - d1.shift(63)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_survcompa_63d_jerk_v148_signal(cashneq, opex, equity, assets, liabilities):
    cov = np.log1p(_safe_div(cashneq, opex).clip(lower=0))
    x = cov + _safe_div(equity, assets) - _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    b = d1 - d1.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_survcompb_63d_jerk_v149_signal(cashneq, opex, equity, assets, liabilities):
    cov = np.log1p(_safe_div(cashneq, opex).clip(lower=0))
    x = cov + _safe_div(equity, assets) - _safe_div(liabilities, assets)
    base = _z(x, 63)
    d1 = base - base.shift(42)
    b = d1 - d1.shift(42)
    return b.replace([np.inf, -np.inf], np.nan)

def f37da_f37_distress_risk_altman_survcompc_63d_jerk_v150_signal(cashneq, opex, equity, assets, liabilities):
    cov = np.log1p(_safe_div(cashneq, opex).clip(lower=0))
    x = cov + _safe_div(equity, assets) - _safe_div(liabilities, assets)
    base = _mean(x, 21)
    d1 = base - base.shift(21)
    acc = d1 - d1.shift(21)
    b = acc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return b.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f37da_f37_distress_risk_altman_wcassetsa_63d_jerk_v001_signal,
    f37da_f37_distress_risk_altman_wcassetsb_63d_jerk_v002_signal,
    f37da_f37_distress_risk_altman_wcassetsc_63d_jerk_v003_signal,
    f37da_f37_distress_risk_altman_reassetsa_63d_jerk_v004_signal,
    f37da_f37_distress_risk_altman_reassetsb_63d_jerk_v005_signal,
    f37da_f37_distress_risk_altman_reassetsc_63d_jerk_v006_signal,
    f37da_f37_distress_risk_altman_ebitassetsa_63d_jerk_v007_signal,
    f37da_f37_distress_risk_altman_ebitassetsb_63d_jerk_v008_signal,
    f37da_f37_distress_risk_altman_ebitassetsc_63d_jerk_v009_signal,
    f37da_f37_distress_risk_altman_eqliaba_63d_jerk_v010_signal,
    f37da_f37_distress_risk_altman_eqliabb_63d_jerk_v011_signal,
    f37da_f37_distress_risk_altman_eqliabc_63d_jerk_v012_signal,
    f37da_f37_distress_risk_altman_revassetsa_63d_jerk_v013_signal,
    f37da_f37_distress_risk_altman_revassetsb_63d_jerk_v014_signal,
    f37da_f37_distress_risk_altman_revassetsc_63d_jerk_v015_signal,
    f37da_f37_distress_risk_altman_zscorea_63d_jerk_v016_signal,
    f37da_f37_distress_risk_altman_zscoreb_63d_jerk_v017_signal,
    f37da_f37_distress_risk_altman_zscorec_63d_jerk_v018_signal,
    f37da_f37_distress_risk_altman_zprimea_63d_jerk_v019_signal,
    f37da_f37_distress_risk_altman_zprimeb_63d_jerk_v020_signal,
    f37da_f37_distress_risk_altman_zprimec_63d_jerk_v021_signal,
    f37da_f37_distress_risk_altman_runwaya_63d_jerk_v022_signal,
    f37da_f37_distress_risk_altman_runwayb_63d_jerk_v023_signal,
    f37da_f37_distress_risk_altman_runwayc_63d_jerk_v024_signal,
    f37da_f37_distress_risk_altman_runwayreva_63d_jerk_v025_signal,
    f37da_f37_distress_risk_altman_runwayrevb_63d_jerk_v026_signal,
    f37da_f37_distress_risk_altman_runwayrevc_63d_jerk_v027_signal,
    f37da_f37_distress_risk_altman_burnstressa_21d_jerk_v028_signal,
    f37da_f37_distress_risk_altman_burnstressb_21d_jerk_v029_signal,
    f37da_f37_distress_risk_altman_burnstressc_21d_jerk_v030_signal,
    f37da_f37_distress_risk_altman_ebitcovera_126d_jerk_v031_signal,
    f37da_f37_distress_risk_altman_ebitcoverb_126d_jerk_v032_signal,
    f37da_f37_distress_risk_altman_ebitcoverc_126d_jerk_v033_signal,
    f37da_f37_distress_risk_altman_oprunwaya_63d_jerk_v034_signal,
    f37da_f37_distress_risk_altman_oprunwayb_63d_jerk_v035_signal,
    f37da_f37_distress_risk_altman_oprunwayc_63d_jerk_v036_signal,
    f37da_f37_distress_risk_altman_liabassetsa_63d_jerk_v037_signal,
    f37da_f37_distress_risk_altman_liabassetsb_63d_jerk_v038_signal,
    f37da_f37_distress_risk_altman_liabassetsc_63d_jerk_v039_signal,
    f37da_f37_distress_risk_altman_liabebita_63d_jerk_v040_signal,
    f37da_f37_distress_risk_altman_liabebitb_63d_jerk_v041_signal,
    f37da_f37_distress_risk_altman_liabebitc_63d_jerk_v042_signal,
    f37da_f37_distress_risk_altman_liabreva_63d_jerk_v043_signal,
    f37da_f37_distress_risk_altman_liabrevb_63d_jerk_v044_signal,
    f37da_f37_distress_risk_altman_liabrevc_63d_jerk_v045_signal,
    f37da_f37_distress_risk_altman_eqassetsa_63d_jerk_v046_signal,
    f37da_f37_distress_risk_altman_eqassetsb_63d_jerk_v047_signal,
    f37da_f37_distress_risk_altman_eqassetsc_63d_jerk_v048_signal,
    f37da_f37_distress_risk_altman_netdebta_63d_jerk_v049_signal,
    f37da_f37_distress_risk_altman_netdebtb_63d_jerk_v050_signal,
    f37da_f37_distress_risk_altman_netdebtc_63d_jerk_v051_signal,
    f37da_f37_distress_risk_altman_debttoeqa_63d_jerk_v052_signal,
    f37da_f37_distress_risk_altman_debttoeqb_63d_jerk_v053_signal,
    f37da_f37_distress_risk_altman_debttoeqc_63d_jerk_v054_signal,
    f37da_f37_distress_risk_altman_cashassetsa_63d_jerk_v055_signal,
    f37da_f37_distress_risk_altman_cashassetsb_63d_jerk_v056_signal,
    f37da_f37_distress_risk_altman_cashassetsc_63d_jerk_v057_signal,
    f37da_f37_distress_risk_altman_cashliaba_63d_jerk_v058_signal,
    f37da_f37_distress_risk_altman_cashliabb_63d_jerk_v059_signal,
    f37da_f37_distress_risk_altman_cashliabc_63d_jerk_v060_signal,
    f37da_f37_distress_risk_altman_cashreva_63d_jerk_v061_signal,
    f37da_f37_distress_risk_altman_cashrevb_63d_jerk_v062_signal,
    f37da_f37_distress_risk_altman_cashrevc_63d_jerk_v063_signal,
    f37da_f37_distress_risk_altman_wcliaba_63d_jerk_v064_signal,
    f37da_f37_distress_risk_altman_wcliabb_63d_jerk_v065_signal,
    f37da_f37_distress_risk_altman_wcliabc_63d_jerk_v066_signal,
    f37da_f37_distress_risk_altman_wcreva_63d_jerk_v067_signal,
    f37da_f37_distress_risk_altman_wcrevb_63d_jerk_v068_signal,
    f37da_f37_distress_risk_altman_wcrevc_63d_jerk_v069_signal,
    f37da_f37_distress_risk_altman_recasha_63d_jerk_v070_signal,
    f37da_f37_distress_risk_altman_recashb_63d_jerk_v071_signal,
    f37da_f37_distress_risk_altman_recashc_63d_jerk_v072_signal,
    f37da_f37_distress_risk_altman_reliaba_63d_jerk_v073_signal,
    f37da_f37_distress_risk_altman_reliabb_63d_jerk_v074_signal,
    f37da_f37_distress_risk_altman_reliabc_63d_jerk_v075_signal,
    f37da_f37_distress_risk_altman_ebitliaba_63d_jerk_v076_signal,
    f37da_f37_distress_risk_altman_ebitliabb_63d_jerk_v077_signal,
    f37da_f37_distress_risk_altman_ebitliabc_63d_jerk_v078_signal,
    f37da_f37_distress_risk_altman_ebitopexa_63d_jerk_v079_signal,
    f37da_f37_distress_risk_altman_ebitopexb_63d_jerk_v080_signal,
    f37da_f37_distress_risk_altman_ebitopexc_63d_jerk_v081_signal,
    f37da_f37_distress_risk_altman_opexreva_63d_jerk_v082_signal,
    f37da_f37_distress_risk_altman_opexrevb_63d_jerk_v083_signal,
    f37da_f37_distress_risk_altman_opexrevc_63d_jerk_v084_signal,
    f37da_f37_distress_risk_altman_opexassetsa_63d_jerk_v085_signal,
    f37da_f37_distress_risk_altman_opexassetsb_63d_jerk_v086_signal,
    f37da_f37_distress_risk_altman_opexassetsc_63d_jerk_v087_signal,
    f37da_f37_distress_risk_altman_opsurplusa_63d_jerk_v088_signal,
    f37da_f37_distress_risk_altman_opsurplusb_63d_jerk_v089_signal,
    f37da_f37_distress_risk_altman_opsurplusc_63d_jerk_v090_signal,
    f37da_f37_distress_risk_altman_capadeqa_63d_jerk_v091_signal,
    f37da_f37_distress_risk_altman_capadeqb_63d_jerk_v092_signal,
    f37da_f37_distress_risk_altman_capadeqc_63d_jerk_v093_signal,
    f37da_f37_distress_risk_altman_zscza_252d_jerk_v094_signal,
    f37da_f37_distress_risk_altman_zsczb_252d_jerk_v095_signal,
    f37da_f37_distress_risk_altman_zsczc_252d_jerk_v096_signal,
    f37da_f37_distress_risk_altman_runwayza_252d_jerk_v097_signal,
    f37da_f37_distress_risk_altman_runwayzb_252d_jerk_v098_signal,
    f37da_f37_distress_risk_altman_runwayzc_252d_jerk_v099_signal,
    f37da_f37_distress_risk_altman_levza_252d_jerk_v100_signal,
    f37da_f37_distress_risk_altman_levzb_252d_jerk_v101_signal,
    f37da_f37_distress_risk_altman_levzc_252d_jerk_v102_signal,
    f37da_f37_distress_risk_altman_ebitza_252d_jerk_v103_signal,
    f37da_f37_distress_risk_altman_ebitzb_252d_jerk_v104_signal,
    f37da_f37_distress_risk_altman_ebitzc_252d_jerk_v105_signal,
    f37da_f37_distress_risk_altman_solvza_252d_jerk_v106_signal,
    f37da_f37_distress_risk_altman_solvzb_252d_jerk_v107_signal,
    f37da_f37_distress_risk_altman_solvzc_252d_jerk_v108_signal,
    f37da_f37_distress_risk_altman_cashza_126d_jerk_v109_signal,
    f37da_f37_distress_risk_altman_cashzb_126d_jerk_v110_signal,
    f37da_f37_distress_risk_altman_cashzc_126d_jerk_v111_signal,
    f37da_f37_distress_risk_altman_zgapfloora_63d_jerk_v112_signal,
    f37da_f37_distress_risk_altman_zgapfloorb_63d_jerk_v113_signal,
    f37da_f37_distress_risk_altman_zgapfloorc_63d_jerk_v114_signal,
    f37da_f37_distress_risk_altman_zinstaba_63d_jerk_v115_signal,
    f37da_f37_distress_risk_altman_zinstabb_63d_jerk_v116_signal,
    f37da_f37_distress_risk_altman_zinstabc_63d_jerk_v117_signal,
    f37da_f37_distress_risk_altman_ebitwca_63d_jerk_v118_signal,
    f37da_f37_distress_risk_altman_ebitwcb_63d_jerk_v119_signal,
    f37da_f37_distress_risk_altman_ebitwcc_63d_jerk_v120_signal,
    f37da_f37_distress_risk_altman_x2x5a_63d_jerk_v121_signal,
    f37da_f37_distress_risk_altman_x2x5b_63d_jerk_v122_signal,
    f37da_f37_distress_risk_altman_x2x5c_63d_jerk_v123_signal,
    f37da_f37_distress_risk_altman_liqcompa_63d_jerk_v124_signal,
    f37da_f37_distress_risk_altman_liqcompb_63d_jerk_v125_signal,
    f37da_f37_distress_risk_altman_liqcompc_63d_jerk_v126_signal,
    f37da_f37_distress_risk_altman_solvbala_63d_jerk_v127_signal,
    f37da_f37_distress_risk_altman_solvbalb_63d_jerk_v128_signal,
    f37da_f37_distress_risk_altman_solvbalc_63d_jerk_v129_signal,
    f37da_f37_distress_risk_altman_fragilitya_63d_jerk_v130_signal,
    f37da_f37_distress_risk_altman_fragilityb_63d_jerk_v131_signal,
    f37da_f37_distress_risk_altman_fragilityc_63d_jerk_v132_signal,
    f37da_f37_distress_risk_altman_liqstressa_63d_jerk_v133_signal,
    f37da_f37_distress_risk_altman_liqstressb_63d_jerk_v134_signal,
    f37da_f37_distress_risk_altman_liqstressc_63d_jerk_v135_signal,
    f37da_f37_distress_risk_altman_severitya_63d_jerk_v136_signal,
    f37da_f37_distress_risk_altman_severityb_63d_jerk_v137_signal,
    f37da_f37_distress_risk_altman_severityc_63d_jerk_v138_signal,
    f37da_f37_distress_risk_altman_selffunda_63d_jerk_v139_signal,
    f37da_f37_distress_risk_altman_selffundb_63d_jerk_v140_signal,
    f37da_f37_distress_risk_altman_selffundc_63d_jerk_v141_signal,
    f37da_f37_distress_risk_altman_netliaba_126d_jerk_v142_signal,
    f37da_f37_distress_risk_altman_netliabb_126d_jerk_v143_signal,
    f37da_f37_distress_risk_altman_netliabc_126d_jerk_v144_signal,
    f37da_f37_distress_risk_altman_zrobusta_252d_jerk_v145_signal,
    f37da_f37_distress_risk_altman_zrobustb_252d_jerk_v146_signal,
    f37da_f37_distress_risk_altman_zrobustc_252d_jerk_v147_signal,
    f37da_f37_distress_risk_altman_survcompa_63d_jerk_v148_signal,
    f37da_f37_distress_risk_altman_survcompb_63d_jerk_v149_signal,
    f37da_f37_distress_risk_altman_survcompc_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_DISTRESS_RISK_ALTMAN_REGISTRY_3RD_001_150 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    cols = {}
    cols["assets"] = _fund(1, base=1e9, drift=0.0, vol=0.12).rename("assets")
    cols["revenue"] = _fund(2, base=6e8, drift=0.0, vol=0.18).rename("revenue")
    cols["liabilities"] = _fund(3, base=5e8, drift=0.0, vol=0.15).rename("liabilities")
    cols["cashneq"] = _fund(4, base=1.5e8, drift=0.0, vol=0.2).rename("cashneq")
    cols["opex"] = _fund(5, base=5e8, drift=0.0, vol=0.15).rename("opex")
    cols["workingcapital"] = _fund(6, base=2e8, drift=0.0, vol=0.22, allow_neg=True).rename("workingcapital")
    cols["retearn"] = _fund(7, base=3e8, drift=0.0, vol=0.25, allow_neg=True).rename("retearn")
    cols["ebit"] = _fund(8, base=1.2e8, drift=-0.02, vol=0.35, allow_neg=True).rename("ebit")
    cols["equity"] = _fund(9, base=4e8, drift=-0.03, vol=0.35, allow_neg=True).rename("equity")
    return cols


if __name__ == "__main__":
    cols = _build_synth()

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

    print("OK f37_distress_risk_altman_3rd_derivatives_001_150_claude: %d features pass" % n_features)
