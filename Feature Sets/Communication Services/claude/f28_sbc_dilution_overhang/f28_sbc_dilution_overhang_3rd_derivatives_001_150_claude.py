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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


# ===== folder domain primitives: SBC dilution / overhang =====
def _sb_dilrate(sbcomp, marketcap):
    return _safe_div(sbcomp, marketcap)


def _sb_promote_opex(sbcomp, opex):
    return _safe_div(sbcomp, opex)


def _sb_promote_rev(sbcomp, revenue):
    return _safe_div(sbcomp, revenue)


def _sb_burn_subsidy(sbcomp, ncfo):
    return _safe_div(sbcomp, ncfo.abs())


def _sb_overhang(shareswadil, shareswa):
    return _safe_div(shareswadil, shareswa) - 1.0


def _sb_paper_vs_cash(sbcomp, ncfcommon):
    return _safe_div(sbcomp, ncfcommon.abs())

# jerk: 2nd deriv of dilrate sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_dilrate_smsw21_21d_jerk_v001_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_dilrate_smsw42_42d_jerk_v002_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_dilrate_smsw63_63d_jerk_v003_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_dilrate_smsw95_95d_jerk_v004_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_dilrate_smsw126_126d_jerk_v005_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate z-base, 21d
def f28sb_f28_sbc_dilution_overhang_dilrate_zsw21_21d_jerk_v006_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate z-base, 42d
def f28sb_f28_sbc_dilution_overhang_dilrate_zsw42_42d_jerk_v007_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate z-base, 63d
def f28sb_f28_sbc_dilution_overhang_dilrate_zsw63_63d_jerk_v008_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate z-base, 95d
def f28sb_f28_sbc_dilution_overhang_dilrate_zsw95_95d_jerk_v009_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate z-base, 126d
def f28sb_f28_sbc_dilution_overhang_dilrate_zsw126_126d_jerk_v010_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_dilrate_rcsw21_21d_jerk_v011_signal(sbcomp, marketcap):
    lvl = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_dilrate_rcsw42_42d_jerk_v012_signal(sbcomp, marketcap):
    lvl = _mean(_sb_dilrate(sbcomp, marketcap), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_dilrate_rcsw63_63d_jerk_v013_signal(sbcomp, marketcap):
    lvl = _mean(_sb_dilrate(sbcomp, marketcap), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_dilrate_rcsw95_95d_jerk_v014_signal(sbcomp, marketcap):
    lvl = _mean(_sb_dilrate(sbcomp, marketcap), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_dilrate_rcsw126_126d_jerk_v015_signal(sbcomp, marketcap):
    lvl = _mean(_sb_dilrate(sbcomp, marketcap), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_dilrate_dpsw21_21d_jerk_v016_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_dilrate_dpsw42_42d_jerk_v017_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_dilrate_dpsw63_63d_jerk_v018_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_dilrate_dpsw95_95d_jerk_v019_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_dilrate_dpsw126_126d_jerk_v020_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_dilrate_rksw21_21d_jerk_v021_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_dilrate_rksw42_42d_jerk_v022_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_dilrate_rksw63_63d_jerk_v023_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_dilrate_rksw95_95d_jerk_v024_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of dilrate rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_dilrate_rksw126_126d_jerk_v025_signal(sbcomp, marketcap):
    lvl = _sb_dilrate(sbcomp, marketcap)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_promopex_smsw21_21d_jerk_v026_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_promopex_smsw42_42d_jerk_v027_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_promopex_smsw63_63d_jerk_v028_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_promopex_smsw95_95d_jerk_v029_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_promopex_smsw126_126d_jerk_v030_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex z-base, 21d
def f28sb_f28_sbc_dilution_overhang_promopex_zsw21_21d_jerk_v031_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex z-base, 42d
def f28sb_f28_sbc_dilution_overhang_promopex_zsw42_42d_jerk_v032_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex z-base, 63d
def f28sb_f28_sbc_dilution_overhang_promopex_zsw63_63d_jerk_v033_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex z-base, 95d
def f28sb_f28_sbc_dilution_overhang_promopex_zsw95_95d_jerk_v034_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex z-base, 126d
def f28sb_f28_sbc_dilution_overhang_promopex_zsw126_126d_jerk_v035_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_promopex_rcsw21_21d_jerk_v036_signal(sbcomp, opex):
    lvl = _mean(_sb_promote_opex(sbcomp, opex), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_promopex_rcsw42_42d_jerk_v037_signal(sbcomp, opex):
    lvl = _mean(_sb_promote_opex(sbcomp, opex), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_promopex_rcsw63_63d_jerk_v038_signal(sbcomp, opex):
    lvl = _mean(_sb_promote_opex(sbcomp, opex), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_promopex_rcsw95_95d_jerk_v039_signal(sbcomp, opex):
    lvl = _mean(_sb_promote_opex(sbcomp, opex), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_promopex_rcsw126_126d_jerk_v040_signal(sbcomp, opex):
    lvl = _mean(_sb_promote_opex(sbcomp, opex), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_promopex_dpsw21_21d_jerk_v041_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_promopex_dpsw42_42d_jerk_v042_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_promopex_dpsw63_63d_jerk_v043_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_promopex_dpsw95_95d_jerk_v044_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_promopex_dpsw126_126d_jerk_v045_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_promopex_rksw21_21d_jerk_v046_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_promopex_rksw42_42d_jerk_v047_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_promopex_rksw63_63d_jerk_v048_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_promopex_rksw95_95d_jerk_v049_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promopex rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_promopex_rksw126_126d_jerk_v050_signal(sbcomp, opex):
    lvl = _sb_promote_opex(sbcomp, opex)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_promrev_smsw21_21d_jerk_v051_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_promrev_smsw42_42d_jerk_v052_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_promrev_smsw63_63d_jerk_v053_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_promrev_smsw95_95d_jerk_v054_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_promrev_smsw126_126d_jerk_v055_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev z-base, 21d
def f28sb_f28_sbc_dilution_overhang_promrev_zsw21_21d_jerk_v056_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev z-base, 42d
def f28sb_f28_sbc_dilution_overhang_promrev_zsw42_42d_jerk_v057_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev z-base, 63d
def f28sb_f28_sbc_dilution_overhang_promrev_zsw63_63d_jerk_v058_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev z-base, 95d
def f28sb_f28_sbc_dilution_overhang_promrev_zsw95_95d_jerk_v059_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev z-base, 126d
def f28sb_f28_sbc_dilution_overhang_promrev_zsw126_126d_jerk_v060_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_promrev_rcsw21_21d_jerk_v061_signal(sbcomp, revenue):
    lvl = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_promrev_rcsw42_42d_jerk_v062_signal(sbcomp, revenue):
    lvl = _mean(_sb_promote_rev(sbcomp, revenue), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_promrev_rcsw63_63d_jerk_v063_signal(sbcomp, revenue):
    lvl = _mean(_sb_promote_rev(sbcomp, revenue), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_promrev_rcsw95_95d_jerk_v064_signal(sbcomp, revenue):
    lvl = _mean(_sb_promote_rev(sbcomp, revenue), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_promrev_rcsw126_126d_jerk_v065_signal(sbcomp, revenue):
    lvl = _mean(_sb_promote_rev(sbcomp, revenue), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_promrev_dpsw21_21d_jerk_v066_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_promrev_dpsw42_42d_jerk_v067_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_promrev_dpsw63_63d_jerk_v068_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_promrev_dpsw95_95d_jerk_v069_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_promrev_dpsw126_126d_jerk_v070_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_promrev_rksw21_21d_jerk_v071_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_promrev_rksw42_42d_jerk_v072_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_promrev_rksw63_63d_jerk_v073_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_promrev_rksw95_95d_jerk_v074_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of promrev rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_promrev_rksw126_126d_jerk_v075_signal(sbcomp, revenue):
    lvl = _sb_promote_rev(sbcomp, revenue)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_burnsub_smsw21_21d_jerk_v076_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_burnsub_smsw42_42d_jerk_v077_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_burnsub_smsw63_63d_jerk_v078_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_burnsub_smsw95_95d_jerk_v079_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_burnsub_smsw126_126d_jerk_v080_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub z-base, 21d
def f28sb_f28_sbc_dilution_overhang_burnsub_zsw21_21d_jerk_v081_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub z-base, 42d
def f28sb_f28_sbc_dilution_overhang_burnsub_zsw42_42d_jerk_v082_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub z-base, 63d
def f28sb_f28_sbc_dilution_overhang_burnsub_zsw63_63d_jerk_v083_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub z-base, 95d
def f28sb_f28_sbc_dilution_overhang_burnsub_zsw95_95d_jerk_v084_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub z-base, 126d
def f28sb_f28_sbc_dilution_overhang_burnsub_zsw126_126d_jerk_v085_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_burnsub_rcsw21_21d_jerk_v086_signal(sbcomp, ncfo):
    lvl = _mean(_sb_burn_subsidy(sbcomp, ncfo), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_burnsub_rcsw42_42d_jerk_v087_signal(sbcomp, ncfo):
    lvl = _mean(_sb_burn_subsidy(sbcomp, ncfo), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_burnsub_rcsw63_63d_jerk_v088_signal(sbcomp, ncfo):
    lvl = _mean(_sb_burn_subsidy(sbcomp, ncfo), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_burnsub_rcsw95_95d_jerk_v089_signal(sbcomp, ncfo):
    lvl = _mean(_sb_burn_subsidy(sbcomp, ncfo), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_burnsub_rcsw126_126d_jerk_v090_signal(sbcomp, ncfo):
    lvl = _mean(_sb_burn_subsidy(sbcomp, ncfo), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_burnsub_dpsw21_21d_jerk_v091_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_burnsub_dpsw42_42d_jerk_v092_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_burnsub_dpsw63_63d_jerk_v093_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_burnsub_dpsw95_95d_jerk_v094_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_burnsub_dpsw126_126d_jerk_v095_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_burnsub_rksw21_21d_jerk_v096_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_burnsub_rksw42_42d_jerk_v097_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_burnsub_rksw63_63d_jerk_v098_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_burnsub_rksw95_95d_jerk_v099_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of burnsub rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_burnsub_rksw126_126d_jerk_v100_signal(sbcomp, ncfo):
    lvl = _sb_burn_subsidy(sbcomp, ncfo)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_overhang_smsw21_21d_jerk_v101_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_overhang_smsw42_42d_jerk_v102_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_overhang_smsw63_63d_jerk_v103_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_overhang_smsw95_95d_jerk_v104_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_overhang_smsw126_126d_jerk_v105_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang z-base, 21d
def f28sb_f28_sbc_dilution_overhang_overhang_zsw21_21d_jerk_v106_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang z-base, 42d
def f28sb_f28_sbc_dilution_overhang_overhang_zsw42_42d_jerk_v107_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang z-base, 63d
def f28sb_f28_sbc_dilution_overhang_overhang_zsw63_63d_jerk_v108_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang z-base, 95d
def f28sb_f28_sbc_dilution_overhang_overhang_zsw95_95d_jerk_v109_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang z-base, 126d
def f28sb_f28_sbc_dilution_overhang_overhang_zsw126_126d_jerk_v110_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_overhang_rcsw21_21d_jerk_v111_signal(shareswadil, shareswa):
    lvl = _mean(_sb_overhang(shareswadil, shareswa), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_overhang_rcsw42_42d_jerk_v112_signal(shareswadil, shareswa):
    lvl = _mean(_sb_overhang(shareswadil, shareswa), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_overhang_rcsw63_63d_jerk_v113_signal(shareswadil, shareswa):
    lvl = _mean(_sb_overhang(shareswadil, shareswa), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_overhang_rcsw95_95d_jerk_v114_signal(shareswadil, shareswa):
    lvl = _mean(_sb_overhang(shareswadil, shareswa), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_overhang_rcsw126_126d_jerk_v115_signal(shareswadil, shareswa):
    lvl = _mean(_sb_overhang(shareswadil, shareswa), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_overhang_dpsw21_21d_jerk_v116_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_overhang_dpsw42_42d_jerk_v117_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_overhang_dpsw63_63d_jerk_v118_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_overhang_dpsw95_95d_jerk_v119_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_overhang_dpsw126_126d_jerk_v120_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_overhang_rksw21_21d_jerk_v121_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_overhang_rksw42_42d_jerk_v122_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_overhang_rksw63_63d_jerk_v123_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_overhang_rksw95_95d_jerk_v124_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of overhang rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_overhang_rksw126_126d_jerk_v125_signal(shareswadil, shareswa):
    lvl = _sb_overhang(shareswadil, shareswa)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash sm-base, 21d
def f28sb_f28_sbc_dilution_overhang_papercash_smsw21_21d_jerk_v126_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _mean(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash sm-base, 42d
def f28sb_f28_sbc_dilution_overhang_papercash_smsw42_42d_jerk_v127_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _mean(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash sm-base, 63d
def f28sb_f28_sbc_dilution_overhang_papercash_smsw63_63d_jerk_v128_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _mean(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash sm-base, 95d
def f28sb_f28_sbc_dilution_overhang_papercash_smsw95_95d_jerk_v129_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _mean(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash sm-base, 126d
def f28sb_f28_sbc_dilution_overhang_papercash_smsw126_126d_jerk_v130_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _mean(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash z-base, 21d
def f28sb_f28_sbc_dilution_overhang_papercash_zsw21_21d_jerk_v131_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _z(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash z-base, 42d
def f28sb_f28_sbc_dilution_overhang_papercash_zsw42_42d_jerk_v132_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _z(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash z-base, 63d
def f28sb_f28_sbc_dilution_overhang_papercash_zsw63_63d_jerk_v133_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _z(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash z-base, 95d
def f28sb_f28_sbc_dilution_overhang_papercash_zsw95_95d_jerk_v134_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _z(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash z-base, 126d
def f28sb_f28_sbc_dilution_overhang_papercash_zsw126_126d_jerk_v135_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _z(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rc-base, 21d
def f28sb_f28_sbc_dilution_overhang_papercash_rcsw21_21d_jerk_v136_signal(sbcomp, ncfcommon):
    lvl = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 21)
    base = _roc(lvl, 21)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rc-base, 42d
def f28sb_f28_sbc_dilution_overhang_papercash_rcsw42_42d_jerk_v137_signal(sbcomp, ncfcommon):
    lvl = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 42)
    base = _roc(lvl, 42)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rc-base, 63d
def f28sb_f28_sbc_dilution_overhang_papercash_rcsw63_63d_jerk_v138_signal(sbcomp, ncfcommon):
    lvl = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 63)
    base = _roc(lvl, 63)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rc-base, 95d
def f28sb_f28_sbc_dilution_overhang_papercash_rcsw95_95d_jerk_v139_signal(sbcomp, ncfcommon):
    lvl = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 95)
    base = _roc(lvl, 95)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rc-base, 126d
def f28sb_f28_sbc_dilution_overhang_papercash_rcsw126_126d_jerk_v140_signal(sbcomp, ncfcommon):
    lvl = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 126)
    base = _roc(lvl, 126)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash dp-base, 21d
def f28sb_f28_sbc_dilution_overhang_papercash_dpsw21_21d_jerk_v141_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _std(lvl, 42)
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash dp-base, 42d
def f28sb_f28_sbc_dilution_overhang_papercash_dpsw42_42d_jerk_v142_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _std(lvl, 84)
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash dp-base, 63d
def f28sb_f28_sbc_dilution_overhang_papercash_dpsw63_63d_jerk_v143_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _std(lvl, 126)
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash dp-base, 95d
def f28sb_f28_sbc_dilution_overhang_papercash_dpsw95_95d_jerk_v144_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _std(lvl, 190)
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash dp-base, 126d
def f28sb_f28_sbc_dilution_overhang_papercash_dpsw126_126d_jerk_v145_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    base = _std(lvl, 252)
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rk-base, 21d
def f28sb_f28_sbc_dilution_overhang_papercash_rksw21_21d_jerk_v146_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = lvl - lvl.shift(21)
    base = chg.rolling(84, min_periods=max(1, 21*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    result = (d1 - d1.shift(21)) / float(21 * 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rk-base, 42d
def f28sb_f28_sbc_dilution_overhang_papercash_rksw42_42d_jerk_v147_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = lvl - lvl.shift(42)
    base = chg.rolling(168, min_periods=max(1, 42*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    result = (d1 - d1.shift(42)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rk-base, 63d
def f28sb_f28_sbc_dilution_overhang_papercash_rksw63_63d_jerk_v148_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = lvl - lvl.shift(63)
    base = chg.rolling(252, min_periods=max(1, 63*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    result = (d1 - d1.shift(63)) / float(63 * 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rk-base, 95d
def f28sb_f28_sbc_dilution_overhang_papercash_rksw95_95d_jerk_v149_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = lvl - lvl.shift(95)
    base = chg.rolling(380, min_periods=max(1, 95*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(95)
    result = (d1 - d1.shift(95)) / float(95 * 95)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk: 2nd deriv of papercash rk-base, 126d
def f28sb_f28_sbc_dilution_overhang_papercash_rksw126_126d_jerk_v150_signal(sbcomp, ncfcommon):
    lvl = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = lvl - lvl.shift(126)
    base = chg.rolling(504, min_periods=max(1, 126*4 // 3)).rank(pct=True) - 0.5
    d1 = base - base.shift(126)
    result = (d1 - d1.shift(126)) / float(126 * 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sb_f28_sbc_dilution_overhang_dilrate_smsw21_21d_jerk_v001_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_smsw42_42d_jerk_v002_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_smsw63_63d_jerk_v003_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_smsw95_95d_jerk_v004_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_smsw126_126d_jerk_v005_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_zsw21_21d_jerk_v006_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_zsw42_42d_jerk_v007_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_zsw63_63d_jerk_v008_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_zsw95_95d_jerk_v009_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_zsw126_126d_jerk_v010_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rcsw21_21d_jerk_v011_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rcsw42_42d_jerk_v012_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rcsw63_63d_jerk_v013_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rcsw95_95d_jerk_v014_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rcsw126_126d_jerk_v015_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dpsw21_21d_jerk_v016_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dpsw42_42d_jerk_v017_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dpsw63_63d_jerk_v018_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dpsw95_95d_jerk_v019_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dpsw126_126d_jerk_v020_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rksw21_21d_jerk_v021_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rksw42_42d_jerk_v022_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rksw63_63d_jerk_v023_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rksw95_95d_jerk_v024_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rksw126_126d_jerk_v025_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_smsw21_21d_jerk_v026_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_smsw42_42d_jerk_v027_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_smsw63_63d_jerk_v028_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_smsw95_95d_jerk_v029_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_smsw126_126d_jerk_v030_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_zsw21_21d_jerk_v031_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_zsw42_42d_jerk_v032_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_zsw63_63d_jerk_v033_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_zsw95_95d_jerk_v034_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_zsw126_126d_jerk_v035_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rcsw21_21d_jerk_v036_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rcsw42_42d_jerk_v037_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rcsw63_63d_jerk_v038_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rcsw95_95d_jerk_v039_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rcsw126_126d_jerk_v040_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_dpsw21_21d_jerk_v041_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_dpsw42_42d_jerk_v042_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_dpsw63_63d_jerk_v043_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_dpsw95_95d_jerk_v044_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_dpsw126_126d_jerk_v045_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rksw21_21d_jerk_v046_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rksw42_42d_jerk_v047_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rksw63_63d_jerk_v048_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rksw95_95d_jerk_v049_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_rksw126_126d_jerk_v050_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_smsw21_21d_jerk_v051_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_smsw42_42d_jerk_v052_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_smsw63_63d_jerk_v053_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_smsw95_95d_jerk_v054_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_smsw126_126d_jerk_v055_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_zsw21_21d_jerk_v056_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_zsw42_42d_jerk_v057_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_zsw63_63d_jerk_v058_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_zsw95_95d_jerk_v059_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_zsw126_126d_jerk_v060_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rcsw21_21d_jerk_v061_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rcsw42_42d_jerk_v062_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rcsw63_63d_jerk_v063_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rcsw95_95d_jerk_v064_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rcsw126_126d_jerk_v065_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_dpsw21_21d_jerk_v066_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_dpsw42_42d_jerk_v067_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_dpsw63_63d_jerk_v068_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_dpsw95_95d_jerk_v069_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_dpsw126_126d_jerk_v070_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rksw21_21d_jerk_v071_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rksw42_42d_jerk_v072_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rksw63_63d_jerk_v073_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rksw95_95d_jerk_v074_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_rksw126_126d_jerk_v075_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_smsw21_21d_jerk_v076_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_smsw42_42d_jerk_v077_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_smsw63_63d_jerk_v078_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_smsw95_95d_jerk_v079_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_smsw126_126d_jerk_v080_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_zsw21_21d_jerk_v081_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_zsw42_42d_jerk_v082_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_zsw63_63d_jerk_v083_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_zsw95_95d_jerk_v084_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_zsw126_126d_jerk_v085_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rcsw21_21d_jerk_v086_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rcsw42_42d_jerk_v087_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rcsw63_63d_jerk_v088_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rcsw95_95d_jerk_v089_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rcsw126_126d_jerk_v090_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_dpsw21_21d_jerk_v091_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_dpsw42_42d_jerk_v092_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_dpsw63_63d_jerk_v093_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_dpsw95_95d_jerk_v094_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_dpsw126_126d_jerk_v095_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rksw21_21d_jerk_v096_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rksw42_42d_jerk_v097_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rksw63_63d_jerk_v098_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rksw95_95d_jerk_v099_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_rksw126_126d_jerk_v100_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_smsw21_21d_jerk_v101_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_smsw42_42d_jerk_v102_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_smsw63_63d_jerk_v103_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_smsw95_95d_jerk_v104_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_smsw126_126d_jerk_v105_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_zsw21_21d_jerk_v106_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_zsw42_42d_jerk_v107_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_zsw63_63d_jerk_v108_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_zsw95_95d_jerk_v109_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_zsw126_126d_jerk_v110_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rcsw21_21d_jerk_v111_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rcsw42_42d_jerk_v112_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rcsw63_63d_jerk_v113_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rcsw95_95d_jerk_v114_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rcsw126_126d_jerk_v115_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dpsw21_21d_jerk_v116_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dpsw42_42d_jerk_v117_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dpsw63_63d_jerk_v118_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dpsw95_95d_jerk_v119_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dpsw126_126d_jerk_v120_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rksw21_21d_jerk_v121_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rksw42_42d_jerk_v122_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rksw63_63d_jerk_v123_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rksw95_95d_jerk_v124_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rksw126_126d_jerk_v125_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_smsw21_21d_jerk_v126_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_smsw42_42d_jerk_v127_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_smsw63_63d_jerk_v128_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_smsw95_95d_jerk_v129_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_smsw126_126d_jerk_v130_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_zsw21_21d_jerk_v131_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_zsw42_42d_jerk_v132_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_zsw63_63d_jerk_v133_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_zsw95_95d_jerk_v134_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_zsw126_126d_jerk_v135_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rcsw21_21d_jerk_v136_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rcsw42_42d_jerk_v137_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rcsw63_63d_jerk_v138_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rcsw95_95d_jerk_v139_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rcsw126_126d_jerk_v140_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dpsw21_21d_jerk_v141_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dpsw42_42d_jerk_v142_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dpsw63_63d_jerk_v143_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dpsw95_95d_jerk_v144_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dpsw126_126d_jerk_v145_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rksw21_21d_jerk_v146_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rksw42_42d_jerk_v147_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rksw63_63d_jerk_v148_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rksw95_95d_jerk_v149_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rksw126_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SBC_DILUTION_OVERHANG_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    sbcomp = _fund(101, base=4e7, drift=0.03, vol=0.08).rename("sbcomp")
    opex = _fund(102, base=3e8, drift=0.025, vol=0.05).rename("opex")
    revenue = _fund(103, base=5e8, drift=0.03, vol=0.05).rename("revenue")
    marketcap = _fund(104, base=2e9, drift=0.02, vol=0.09).rename("marketcap")
    ncfcommon = _fund(105, base=3e7, drift=0.0, vol=0.10, allow_neg=True).rename("ncfcommon")
    shareswa = _fund(106, base=2e8, drift=0.01, vol=0.02).rename("shareswa")
    _dilfac = pd.Series(np.abs(np.random.default_rng(107).normal(0.05, 0.03, n)), name=None)
    shareswadil = (shareswa * (1.0 + _dilfac)).rename("shareswadil")
    ncfo = _fund(108, base=6e7, drift=0.02, vol=0.10, allow_neg=True).rename("ncfo")

    cols = {
        "sbcomp": sbcomp, "opex": opex, "revenue": revenue, "marketcap": marketcap,
        "ncfcommon": ncfcommon, "shareswa": shareswa, "shareswadil": shareswadil,
        "ncfo": ncfo, "closeadj": closeadj,
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
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset of allowlist" % (name, meta["inputs"])
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

    print("OK f28_sbc_dilution_overhang_3rd_derivatives_001_150_claude: %d features pass" % n_features)
