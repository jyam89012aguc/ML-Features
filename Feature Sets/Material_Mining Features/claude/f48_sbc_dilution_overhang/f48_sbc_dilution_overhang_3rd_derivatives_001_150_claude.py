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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _macd(s, a, b):
    # fast-minus-slow EWM band-pass of a series
    return s.ewm(span=a, min_periods=max(2, a // 2)).mean() - s.ewm(span=b, min_periods=max(3, b // 2)).mean()


# ===== folder domain primitives (stock-based-comp dilution overhang) =====
def _f48_dilrate(sbcomp, marketcap):
    # annualized SBC dilution rate = stock comp as a fraction of market cap
    return sbcomp / marketcap.replace(0, np.nan)


def _f48_promote(sbcomp, opex):
    # promote intensity = SBC as a fraction of total operating expense
    return sbcomp / opex.replace(0, np.nan)


def _f48_sgna_load(sbcomp, sgna):
    # SBC as a fraction of SG&A (where stock comp usually books)
    return sbcomp / sgna.replace(0, np.nan)


def _f48_rev_load(sbcomp, revenue):
    # SBC per dollar of revenue (meaningful for producers)
    return sbcomp / revenue.replace(0, np.nan)


def _f48_burn_subsidy(sbcomp, ncfo):
    # non-cash comp subsidy relative to the magnitude of operating cash burn
    return sbcomp / ncfo.abs().replace(0, np.nan)


def _f48_overhang(shareswadil, shareswa):
    # diluted-vs-basic share overhang from options / RSUs / warrants
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f48_papermix(sbcomp, ncfcommon):
    # paper-vs-cash mix: SBC vs net cash raised from common (ncfcommon swings sign)
    return sbcomp / (sbcomp + ncfcommon.abs()).replace(0, np.nan)


def _f48_growth(s, w):
    # log growth of a (possibly negative) fundamental series over w days, on magnitude
    return np.log(s.abs().replace(0, np.nan) / s.shift(w).abs().replace(0, np.nan))


def _f48_truedil(sbcomp, marketcap, shareswa, w):
    # combined true dilution = SBC/mktcap + realized weighted-share growth
    rate = sbcomp / marketcap.replace(0, np.nan)
    grow = shareswa / shareswa.shift(w).replace(0, np.nan) - 1.0
    return rate + grow


# jerk 21d of dilrate [raw]
def f48sb_f48_sbc_dilution_overhang_dilratejk_21d_jerk_v001_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of dilrate [rank]
def f48sb_f48_sbc_dilution_overhang_dilratejkr_63d_jerk_v002_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of dilrate [accel]
def f48sb_f48_sbc_dilution_overhang_dilratejka2_126d_jerk_v003_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promote [abs]
def f48sb_f48_sbc_dilution_overhang_promotejkab_21d_jerk_v004_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promote [regime]
def f48sb_f48_sbc_dilution_overhang_promotejkrg_63d_jerk_v005_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of promote [volnorm]
def f48sb_f48_sbc_dilution_overhang_promotejkvn_126d_jerk_v006_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sgnaload [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkeg_21d_jerk_v007_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sgnaload [raw]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjk_63d_jerk_v008_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sgnaload [rank]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkr_126d_jerk_v009_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revload [accel]
def f48sb_f48_sbc_dilution_overhang_revloadjka2_21d_jerk_v010_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revload [abs]
def f48sb_f48_sbc_dilution_overhang_revloadjkab_63d_jerk_v011_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revload [regime]
def f48sb_f48_sbc_dilution_overhang_revloadjkrg_126d_jerk_v012_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = (jerk > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of burnsub [volnorm]
def f48sb_f48_sbc_dilution_overhang_burnsubjkvn_21d_jerk_v013_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of burnsub [ewmgap]
def f48sb_f48_sbc_dilution_overhang_burnsubjkeg_63d_jerk_v014_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of burnsub [raw]
def f48sb_f48_sbc_dilution_overhang_burnsubjk_126d_jerk_v015_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhang [rank]
def f48sb_f48_sbc_dilution_overhang_overhangjkr_21d_jerk_v016_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhang [accel]
def f48sb_f48_sbc_dilution_overhang_overhangjka2_63d_jerk_v017_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhang [abs]
def f48sb_f48_sbc_dilution_overhang_overhangjkab_126d_jerk_v018_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of papermix [regime]
def f48sb_f48_sbc_dilution_overhang_papermixjkrg_21d_jerk_v019_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of papermix [volnorm]
def f48sb_f48_sbc_dilution_overhang_papermixjkvn_63d_jerk_v020_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of papermix [ewmgap]
def f48sb_f48_sbc_dilution_overhang_papermixjkeg_126d_jerk_v021_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of truedil [raw]
def f48sb_f48_sbc_dilution_overhang_truediljk_21d_jerk_v022_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of truedil [rank]
def f48sb_f48_sbc_dilution_overhang_truediljkr_63d_jerk_v023_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of truedil [accel]
def f48sb_f48_sbc_dilution_overhang_truediljka2_126d_jerk_v024_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrow [abs]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkab_21d_jerk_v025_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrow [regime]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkrg_63d_jerk_v026_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcgrow [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkvn_126d_jerk_v027_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revminrev [ewmgap]
def f48sb_f48_sbc_dilution_overhang_revminrevjkeg_21d_jerk_v028_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revminrev [raw]
def f48sb_f48_sbc_dilution_overhang_revminrevjk_63d_jerk_v029_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revminrev [rank]
def f48sb_f48_sbc_dilution_overhang_revminrevjkr_126d_jerk_v030_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrowq [accel]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjka2_21d_jerk_v031_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 42d of sbcgrowq [abs]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkab_42d_jerk_v032_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(42) / 42.0
    jerk = slope.diff(42) / 42.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrowq [regime]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkrg_63d_jerk_v033_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promXover [volnorm]
def f48sb_f48_sbc_dilution_overhang_promXoverjkvn_21d_jerk_v034_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promXover [ewmgap]
def f48sb_f48_sbc_dilution_overhang_promXoverjkeg_63d_jerk_v035_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 84d of promXover [raw]
def f48sb_f48_sbc_dilution_overhang_promXoverjk_84d_jerk_v036_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(84) / 84.0
    jerk = slope.diff(84) / 84.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsrev [rank]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkr_21d_jerk_v037_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsrev [accel]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjka2_63d_jerk_v038_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsrev [abs]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkab_126d_jerk_v039_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsmcap [regime]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkrg_21d_jerk_v040_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsmcap [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkvn_63d_jerk_v041_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsmcap [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkeg_126d_jerk_v042_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsshare [raw]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejk_21d_jerk_v043_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsshare [rank]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkr_63d_jerk_v044_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsshare [accel]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejka2_126d_jerk_v045_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhangidx [abs]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkab_21d_jerk_v046_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhangidx [regime]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkrg_63d_jerk_v047_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhangidx [volnorm]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkvn_126d_jerk_v048_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of dilXover [ewmgap]
def f48sb_f48_sbc_dilution_overhang_dilXoverjkeg_21d_jerk_v049_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of dilXover [raw]
def f48sb_f48_sbc_dilution_overhang_dilXoverjk_63d_jerk_v050_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of dilXover [rank]
def f48sb_f48_sbc_dilution_overhang_dilXoverjkr_126d_jerk_v051_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of dilrate [accel]
def f48sb_f48_sbc_dilution_overhang_dilratejka2_21d_jerk_v052_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of dilrate [abs]
def f48sb_f48_sbc_dilution_overhang_dilratejkab_63d_jerk_v053_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of dilrate [regime]
def f48sb_f48_sbc_dilution_overhang_dilratejkrg_126d_jerk_v054_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = (jerk > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promote [volnorm]
def f48sb_f48_sbc_dilution_overhang_promotejkvn_21d_jerk_v055_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promote [ewmgap]
def f48sb_f48_sbc_dilution_overhang_promotejkeg_63d_jerk_v056_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of promote [raw]
def f48sb_f48_sbc_dilution_overhang_promotejk_126d_jerk_v057_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sgnaload [rank]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkr_21d_jerk_v058_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sgnaload [accel]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjka2_63d_jerk_v059_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sgnaload [abs]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkab_126d_jerk_v060_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revload [regime]
def f48sb_f48_sbc_dilution_overhang_revloadjkrg_21d_jerk_v061_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revload [volnorm]
def f48sb_f48_sbc_dilution_overhang_revloadjkvn_63d_jerk_v062_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revload [ewmgap]
def f48sb_f48_sbc_dilution_overhang_revloadjkeg_126d_jerk_v063_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of burnsub [raw]
def f48sb_f48_sbc_dilution_overhang_burnsubjk_21d_jerk_v064_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of burnsub [rank]
def f48sb_f48_sbc_dilution_overhang_burnsubjkr_63d_jerk_v065_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of burnsub [accel]
def f48sb_f48_sbc_dilution_overhang_burnsubjka2_126d_jerk_v066_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhang [abs]
def f48sb_f48_sbc_dilution_overhang_overhangjkab_21d_jerk_v067_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhang [regime]
def f48sb_f48_sbc_dilution_overhang_overhangjkrg_63d_jerk_v068_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhang [volnorm]
def f48sb_f48_sbc_dilution_overhang_overhangjkvn_126d_jerk_v069_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of papermix [ewmgap]
def f48sb_f48_sbc_dilution_overhang_papermixjkeg_21d_jerk_v070_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of papermix [raw]
def f48sb_f48_sbc_dilution_overhang_papermixjk_63d_jerk_v071_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of papermix [rank]
def f48sb_f48_sbc_dilution_overhang_papermixjkr_126d_jerk_v072_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of truedil [accel]
def f48sb_f48_sbc_dilution_overhang_truediljka2_21d_jerk_v073_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of truedil [abs]
def f48sb_f48_sbc_dilution_overhang_truediljkab_63d_jerk_v074_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of truedil [regime]
def f48sb_f48_sbc_dilution_overhang_truediljkrg_126d_jerk_v075_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = (jerk > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrow [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkvn_21d_jerk_v076_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrow [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkeg_63d_jerk_v077_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcgrow [raw]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjk_126d_jerk_v078_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revminrev [rank]
def f48sb_f48_sbc_dilution_overhang_revminrevjkr_21d_jerk_v079_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revminrev [accel]
def f48sb_f48_sbc_dilution_overhang_revminrevjka2_63d_jerk_v080_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revminrev [abs]
def f48sb_f48_sbc_dilution_overhang_revminrevjkab_126d_jerk_v081_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrowq [regime]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkrg_21d_jerk_v082_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 42d of sbcgrowq [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkvn_42d_jerk_v083_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(42) / 42.0
    jerk = slope.diff(42) / 42.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrowq [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkeg_63d_jerk_v084_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promXover [raw]
def f48sb_f48_sbc_dilution_overhang_promXoverjk_21d_jerk_v085_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promXover [rank]
def f48sb_f48_sbc_dilution_overhang_promXoverjkr_63d_jerk_v086_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 84d of promXover [accel]
def f48sb_f48_sbc_dilution_overhang_promXoverjka2_84d_jerk_v087_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(84) / 84.0
    jerk = slope.diff(84) / 84.0
    result = jerk - jerk.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsrev [abs]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkab_21d_jerk_v088_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsrev [regime]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkrg_63d_jerk_v089_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsrev [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkvn_126d_jerk_v090_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsmcap [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkeg_21d_jerk_v091_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsmcap [raw]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjk_63d_jerk_v092_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsmcap [rank]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkr_126d_jerk_v093_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsshare [accel]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejka2_21d_jerk_v094_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsshare [abs]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkab_63d_jerk_v095_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsshare [regime]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkrg_126d_jerk_v096_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = (jerk > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhangidx [volnorm]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkvn_21d_jerk_v097_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhangidx [ewmgap]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkeg_63d_jerk_v098_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhangidx [raw]
def f48sb_f48_sbc_dilution_overhang_overhangidxjk_126d_jerk_v099_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of dilXover [rank]
def f48sb_f48_sbc_dilution_overhang_dilXoverjkr_21d_jerk_v100_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of dilXover [accel]
def f48sb_f48_sbc_dilution_overhang_dilXoverjka2_63d_jerk_v101_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of dilXover [abs]
def f48sb_f48_sbc_dilution_overhang_dilXoverjkab_126d_jerk_v102_signal(sbcomp, marketcap, shareswadil, shareswa):
    base = (_f48_dilrate(sbcomp, marketcap) * _f48_overhang(shareswadil, shareswa))
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of dilrate [regime]
def f48sb_f48_sbc_dilution_overhang_dilratejkrg_21d_jerk_v103_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of dilrate [volnorm]
def f48sb_f48_sbc_dilution_overhang_dilratejkvn_63d_jerk_v104_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of dilrate [ewmgap]
def f48sb_f48_sbc_dilution_overhang_dilratejkeg_126d_jerk_v105_signal(sbcomp, marketcap):
    base = _f48_dilrate(sbcomp, marketcap)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promote [raw]
def f48sb_f48_sbc_dilution_overhang_promotejk_21d_jerk_v106_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promote [rank]
def f48sb_f48_sbc_dilution_overhang_promotejkr_63d_jerk_v107_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of promote [accel]
def f48sb_f48_sbc_dilution_overhang_promotejka2_126d_jerk_v108_signal(sbcomp, opex):
    base = _f48_promote(sbcomp, opex)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sgnaload [abs]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkab_21d_jerk_v109_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sgnaload [regime]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkrg_63d_jerk_v110_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sgnaload [volnorm]
def f48sb_f48_sbc_dilution_overhang_sgnaloadjkvn_126d_jerk_v111_signal(sbcomp, sgna):
    base = _f48_sgna_load(sbcomp, sgna)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revload [ewmgap]
def f48sb_f48_sbc_dilution_overhang_revloadjkeg_21d_jerk_v112_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revload [raw]
def f48sb_f48_sbc_dilution_overhang_revloadjk_63d_jerk_v113_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revload [rank]
def f48sb_f48_sbc_dilution_overhang_revloadjkr_126d_jerk_v114_signal(sbcomp, revenue):
    base = _f48_rev_load(sbcomp, revenue)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of burnsub [accel]
def f48sb_f48_sbc_dilution_overhang_burnsubjka2_21d_jerk_v115_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of burnsub [abs]
def f48sb_f48_sbc_dilution_overhang_burnsubjkab_63d_jerk_v116_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of burnsub [regime]
def f48sb_f48_sbc_dilution_overhang_burnsubjkrg_126d_jerk_v117_signal(sbcomp, ncfo):
    base = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = (jerk > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhang [volnorm]
def f48sb_f48_sbc_dilution_overhang_overhangjkvn_21d_jerk_v118_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhang [ewmgap]
def f48sb_f48_sbc_dilution_overhang_overhangjkeg_63d_jerk_v119_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhang [raw]
def f48sb_f48_sbc_dilution_overhang_overhangjk_126d_jerk_v120_signal(shareswadil, shareswa):
    base = _f48_overhang(shareswadil, shareswa)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of papermix [rank]
def f48sb_f48_sbc_dilution_overhang_papermixjkr_21d_jerk_v121_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of papermix [accel]
def f48sb_f48_sbc_dilution_overhang_papermixjka2_63d_jerk_v122_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of papermix [abs]
def f48sb_f48_sbc_dilution_overhang_papermixjkab_126d_jerk_v123_signal(sbcomp, ncfcommon):
    base = _f48_papermix(sbcomp, ncfcommon)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of truedil [regime]
def f48sb_f48_sbc_dilution_overhang_truediljkrg_21d_jerk_v124_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of truedil [volnorm]
def f48sb_f48_sbc_dilution_overhang_truediljkvn_63d_jerk_v125_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of truedil [ewmgap]
def f48sb_f48_sbc_dilution_overhang_truediljkeg_126d_jerk_v126_signal(sbcomp, marketcap, shareswa):
    base = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrow [raw]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjk_21d_jerk_v127_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrow [rank]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjkr_63d_jerk_v128_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcgrow [accel]
def f48sb_f48_sbc_dilution_overhang_sbcgrowjka2_126d_jerk_v129_signal(sbcomp):
    base = _f48_growth(sbcomp, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of revminrev [abs]
def f48sb_f48_sbc_dilution_overhang_revminrevjkab_21d_jerk_v130_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk.abs().rolling(10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of revminrev [regime]
def f48sb_f48_sbc_dilution_overhang_revminrevjkrg_63d_jerk_v131_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = (jerk > 0).astype(float).rolling(42, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of revminrev [volnorm]
def f48sb_f48_sbc_dilution_overhang_revminrevjkvn_126d_jerk_v132_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    base = rl / rl.rolling(252, min_periods=84).median().replace(0, np.nan)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = _macd(jerk, 63, 315)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcgrowq [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkeg_21d_jerk_v133_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.rolling(30, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 42d of sbcgrowq [raw]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjk_42d_jerk_v134_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(42) / 42.0
    jerk = slope.diff(42) / 42.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcgrowq [rank]
def f48sb_f48_sbc_dilution_overhang_sbcgrowqjkr_63d_jerk_v135_signal(sbcomp):
    base = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of promXover [accel]
def f48sb_f48_sbc_dilution_overhang_promXoverjka2_21d_jerk_v136_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk - jerk.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of promXover [abs]
def f48sb_f48_sbc_dilution_overhang_promXoverjkab_63d_jerk_v137_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk.abs().rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 84d of promXover [regime]
def f48sb_f48_sbc_dilution_overhang_promXoverjkrg_84d_jerk_v138_signal(sbcomp, opex, shareswadil, shareswa):
    base = _f48_promote(sbcomp, opex) * _f48_overhang(shareswadil, shareswa)
    slope = base.diff(84) / 84.0
    jerk = slope.diff(84) / 84.0
    result = (jerk > 0).astype(float).rolling(84, min_periods=42).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsrev [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkvn_21d_jerk_v139_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _macd(jerk, 10, 50)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsrev [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjkeg_63d_jerk_v140_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.rolling(63, min_periods=21).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsrev [raw]
def f48sb_f48_sbc_dilution_overhang_sbcvsrevjk_126d_jerk_v141_signal(sbcomp, revenue):
    base = _f48_growth(sbcomp, 126) - _f48_growth(revenue, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsmcap [rank]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkr_21d_jerk_v142_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsmcap [accel]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjka2_63d_jerk_v143_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = jerk - jerk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsmcap [abs]
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkab_126d_jerk_v144_signal(sbcomp, marketcap):
    base = _f48_growth(sbcomp, 504) - _f48_growth(marketcap, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk.abs().rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of sbcvsshare [regime]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkrg_21d_jerk_v145_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = (jerk > 0).astype(float).rolling(21, min_periods=10).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of sbcvsshare [volnorm]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkvn_63d_jerk_v146_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _macd(jerk, 21, 105)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of sbcvsshare [ewmgap]
def f48sb_f48_sbc_dilution_overhang_sbcvssharejkeg_126d_jerk_v147_signal(sbcomp, shareswa):
    base = _f48_growth(sbcomp, 63) - _f48_growth(shareswa, 252)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.rolling(189, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 21d of overhangidx [raw]
def f48sb_f48_sbc_dilution_overhang_overhangidxjk_21d_jerk_v148_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(21) / 21.0
    jerk = slope.diff(21) / 21.0
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 63d of overhangidx [rank]
def f48sb_f48_sbc_dilution_overhang_overhangidxjkr_63d_jerk_v149_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(63) / 63.0
    jerk = slope.diff(63) / 63.0
    result = _rank(jerk, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 126d of overhangidx [accel]
def f48sb_f48_sbc_dilution_overhang_overhangidxjka2_126d_jerk_v150_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    base = pd.concat([r, o, bs], axis=1).mean(axis=1)
    slope = base.diff(126) / 126.0
    jerk = slope.diff(126) / 126.0
    result = jerk - jerk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f48sb_f48_sbc_dilution_overhang_dilratejk_21d_jerk_v001_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkr_63d_jerk_v002_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejka2_126d_jerk_v003_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkab_21d_jerk_v004_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkrg_63d_jerk_v005_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkvn_126d_jerk_v006_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkeg_21d_jerk_v007_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjk_63d_jerk_v008_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkr_126d_jerk_v009_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjka2_21d_jerk_v010_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkab_63d_jerk_v011_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkrg_126d_jerk_v012_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjkvn_21d_jerk_v013_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjkeg_63d_jerk_v014_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjk_126d_jerk_v015_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkr_21d_jerk_v016_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjka2_63d_jerk_v017_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkab_126d_jerk_v018_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkrg_21d_jerk_v019_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkvn_63d_jerk_v020_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkeg_126d_jerk_v021_signal,
    f48sb_f48_sbc_dilution_overhang_truediljk_21d_jerk_v022_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkr_63d_jerk_v023_signal,
    f48sb_f48_sbc_dilution_overhang_truediljka2_126d_jerk_v024_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkab_21d_jerk_v025_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkrg_63d_jerk_v026_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkvn_126d_jerk_v027_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkeg_21d_jerk_v028_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjk_63d_jerk_v029_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkr_126d_jerk_v030_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjka2_21d_jerk_v031_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkab_42d_jerk_v032_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkrg_63d_jerk_v033_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjkvn_21d_jerk_v034_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjkeg_63d_jerk_v035_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjk_84d_jerk_v036_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkr_21d_jerk_v037_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjka2_63d_jerk_v038_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkab_126d_jerk_v039_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkrg_21d_jerk_v040_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkvn_63d_jerk_v041_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkeg_126d_jerk_v042_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejk_21d_jerk_v043_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkr_63d_jerk_v044_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejka2_126d_jerk_v045_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkab_21d_jerk_v046_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkrg_63d_jerk_v047_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkvn_126d_jerk_v048_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjkeg_21d_jerk_v049_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjk_63d_jerk_v050_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjkr_126d_jerk_v051_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejka2_21d_jerk_v052_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkab_63d_jerk_v053_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkrg_126d_jerk_v054_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkvn_21d_jerk_v055_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkeg_63d_jerk_v056_signal,
    f48sb_f48_sbc_dilution_overhang_promotejk_126d_jerk_v057_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkr_21d_jerk_v058_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjka2_63d_jerk_v059_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkab_126d_jerk_v060_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkrg_21d_jerk_v061_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkvn_63d_jerk_v062_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkeg_126d_jerk_v063_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjk_21d_jerk_v064_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjkr_63d_jerk_v065_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjka2_126d_jerk_v066_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkab_21d_jerk_v067_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkrg_63d_jerk_v068_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkvn_126d_jerk_v069_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkeg_21d_jerk_v070_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjk_63d_jerk_v071_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkr_126d_jerk_v072_signal,
    f48sb_f48_sbc_dilution_overhang_truediljka2_21d_jerk_v073_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkab_63d_jerk_v074_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkrg_126d_jerk_v075_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkvn_21d_jerk_v076_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkeg_63d_jerk_v077_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjk_126d_jerk_v078_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkr_21d_jerk_v079_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjka2_63d_jerk_v080_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkab_126d_jerk_v081_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkrg_21d_jerk_v082_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkvn_42d_jerk_v083_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkeg_63d_jerk_v084_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjk_21d_jerk_v085_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjkr_63d_jerk_v086_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjka2_84d_jerk_v087_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkab_21d_jerk_v088_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkrg_63d_jerk_v089_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkvn_126d_jerk_v090_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkeg_21d_jerk_v091_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjk_63d_jerk_v092_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkr_126d_jerk_v093_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejka2_21d_jerk_v094_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkab_63d_jerk_v095_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkrg_126d_jerk_v096_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkvn_21d_jerk_v097_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkeg_63d_jerk_v098_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjk_126d_jerk_v099_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjkr_21d_jerk_v100_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjka2_63d_jerk_v101_signal,
    f48sb_f48_sbc_dilution_overhang_dilXoverjkab_126d_jerk_v102_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkrg_21d_jerk_v103_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkvn_63d_jerk_v104_signal,
    f48sb_f48_sbc_dilution_overhang_dilratejkeg_126d_jerk_v105_signal,
    f48sb_f48_sbc_dilution_overhang_promotejk_21d_jerk_v106_signal,
    f48sb_f48_sbc_dilution_overhang_promotejkr_63d_jerk_v107_signal,
    f48sb_f48_sbc_dilution_overhang_promotejka2_126d_jerk_v108_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkab_21d_jerk_v109_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkrg_63d_jerk_v110_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadjkvn_126d_jerk_v111_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkeg_21d_jerk_v112_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjk_63d_jerk_v113_signal,
    f48sb_f48_sbc_dilution_overhang_revloadjkr_126d_jerk_v114_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjka2_21d_jerk_v115_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjkab_63d_jerk_v116_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubjkrg_126d_jerk_v117_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkvn_21d_jerk_v118_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjkeg_63d_jerk_v119_signal,
    f48sb_f48_sbc_dilution_overhang_overhangjk_126d_jerk_v120_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkr_21d_jerk_v121_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjka2_63d_jerk_v122_signal,
    f48sb_f48_sbc_dilution_overhang_papermixjkab_126d_jerk_v123_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkrg_21d_jerk_v124_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkvn_63d_jerk_v125_signal,
    f48sb_f48_sbc_dilution_overhang_truediljkeg_126d_jerk_v126_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjk_21d_jerk_v127_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjkr_63d_jerk_v128_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowjka2_126d_jerk_v129_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkab_21d_jerk_v130_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkrg_63d_jerk_v131_signal,
    f48sb_f48_sbc_dilution_overhang_revminrevjkvn_126d_jerk_v132_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkeg_21d_jerk_v133_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjk_42d_jerk_v134_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowqjkr_63d_jerk_v135_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjka2_21d_jerk_v136_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjkab_63d_jerk_v137_signal,
    f48sb_f48_sbc_dilution_overhang_promXoverjkrg_84d_jerk_v138_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkvn_21d_jerk_v139_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjkeg_63d_jerk_v140_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevjk_126d_jerk_v141_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkr_21d_jerk_v142_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjka2_63d_jerk_v143_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapjkab_126d_jerk_v144_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkrg_21d_jerk_v145_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkvn_63d_jerk_v146_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssharejkeg_126d_jerk_v147_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjk_21d_jerk_v148_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjkr_63d_jerk_v149_signal,
    f48sb_f48_sbc_dilution_overhang_overhangidxjka2_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SBC_DILUTION_OVERHANG_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    sbcomp = _fund(201, base=1.2e7, drift=0.03, vol=0.10).rename("sbcomp")
    opex = _fund(202, base=6.0e7, drift=0.02, vol=0.07).rename("opex")
    sgna = _fund(203, base=2.4e7, drift=0.02, vol=0.08).rename("sgna")
    revenue = _fund(204, base=5.0e7, drift=0.025, vol=0.12).rename("revenue")
    marketcap = _fund(205, base=4.0e8, drift=0.01, vol=0.18).rename("marketcap")
    shareswa = _fund(206, base=7.6e7, drift=0.038, vol=0.05).rename("shareswa")
    _gap = _fund(207, base=6.0e6, drift=0.04, vol=0.09).abs()
    shareswadil = (shareswa + _gap).rename("shareswadil")
    _raise = _fund(208, base=2.0e7, drift=0.02, vol=0.5)
    _return = _fund(209, base=1.6e7, drift=0.02, vol=0.45)
    ncfcommon = (_return - _raise).rename("ncfcommon")
    _burn = _fund(210, base=3.0e7, drift=0.015, vol=0.20)
    ncfo = (_burn - 3.0e7 * 0.9).rename("ncfo")

    cols = {"sbcomp": sbcomp, "opex": opex, "sgna": sgna, "revenue": revenue,
            "marketcap": marketcap, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon, "ncfo": ncfo}

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

    print("OK f48_sbc_dilution_overhang_3rd_derivatives_001_150_claude: %d features pass" % n_features)
