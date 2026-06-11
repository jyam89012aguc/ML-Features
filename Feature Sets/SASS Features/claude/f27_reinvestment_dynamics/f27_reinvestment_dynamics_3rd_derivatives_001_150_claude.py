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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _capex_rev(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _rnd_rev(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _sbc_rev(sbcomp, revenue):
    return sbcomp / revenue.replace(0, np.nan)


def _reinv_rate(capex, rnd, revenue):
    return (capex + rnd) / revenue.replace(0, np.nan)


def _growth_capex(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _glog(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# jerk of capexrev (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_capexrevddn_21d_jerk_v001_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexrev (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_capexrevaccr_42d_jerk_v002_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexrev (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_capexrevemadd_63d_jerk_v003_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexrev (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexrevsgsq_126d_jerk_v004_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndrev (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_rndrevddn_42d_jerk_v005_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndrev (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_rndrevaccr_63d_jerk_v006_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndrev (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_rndrevemadd_126d_jerk_v007_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndrev (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndrevsgsq_21d_jerk_v008_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcrev (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcrevddn_63d_jerk_v009_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcrev (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_sbcrevaccr_126d_jerk_v010_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcrev (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcrevemadd_21d_jerk_v011_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcrev (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcrevsgsq_42d_jerk_v012_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvrate (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_reinvrateddn_126d_jerk_v013_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvrate (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_reinvrateaccr_21d_jerk_v014_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvrate (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_reinvrateemadd_42d_jerk_v015_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvrate (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvratesgsq_63d_jerk_v016_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of growthcapex (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_growthcapexddn_21d_jerk_v017_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of growthcapex (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_growthcapexaccr_42d_jerk_v018_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of growthcapex (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_growthcapexemadd_63d_jerk_v019_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of growthcapex (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_growthcapexsgsq_126d_jerk_v020_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndassets (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_rndassetsddn_42d_jerk_v021_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndassets (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_rndassetsaccr_63d_jerk_v022_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndassets (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_rndassetsemadd_126d_jerk_v023_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndassetssgsq_21d_jerk_v024_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexassets (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_capexassetsddn_63d_jerk_v025_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexassets (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_capexassetsaccr_126d_jerk_v026_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexassets (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_capexassetsemadd_21d_jerk_v027_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexassets (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexassetssgsq_42d_jerk_v028_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndmix (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_rndmixddn_126d_jerk_v029_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndmix (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_rndmixaccr_21d_jerk_v030_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndmix (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_rndmixemadd_42d_jerk_v031_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndmix (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndmixsgsq_63d_jerk_v032_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinv (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_totinvddn_21d_jerk_v033_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinv (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_totinvaccr_42d_jerk_v034_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinv (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_totinvemadd_63d_jerk_v035_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinv (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvsgsq_126d_jerk_v036_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvassets (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_reinvassetsddn_42d_jerk_v037_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvassets (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_reinvassetsaccr_63d_jerk_v038_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvassets (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_reinvassetsemadd_126d_jerk_v039_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvassetssgsq_21d_jerk_v040_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvppne (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_reinvppneddn_63d_jerk_v041_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvppne (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_reinvppneaccr_126d_jerk_v042_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvppne (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_reinvppneemadd_21d_jerk_v043_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of reinvppne (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvppnesgsq_42d_jerk_v044_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of invtilt (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_invtiltddn_126d_jerk_v045_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of invtilt (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_invtiltaccr_21d_jerk_v046_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of invtilt (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_invtiltemadd_42d_jerk_v047_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of invtilt (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_invtiltsgsq_63d_jerk_v048_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbctilt (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltddn_21d_jerk_v049_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbctilt (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltaccr_42d_jerk_v050_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbctilt (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltemadd_63d_jerk_v051_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbctilt (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltsgsq_126d_jerk_v052_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndsbctilt (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltddn_42d_jerk_v053_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndsbctilt (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltaccr_63d_jerk_v054_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndsbctilt (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltemadd_126d_jerk_v055_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndsbctilt (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltsgsq_21d_jerk_v056_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexppnespr (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_capexppnesprddn_63d_jerk_v057_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexppnespr (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_capexppnespraccr_126d_jerk_v058_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexppnespr (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_capexppnespremadd_21d_jerk_v059_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexppnespr (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexppnesprsgsq_42d_jerk_v060_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndppne (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_rndppneddn_126d_jerk_v061_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndppne (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_rndppneaccr_21d_jerk_v062_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndppne (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_rndppneemadd_42d_jerk_v063_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndppne (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndppnesgsq_63d_jerk_v064_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcassets (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcassetsddn_21d_jerk_v065_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcassets (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_sbcassetsaccr_42d_jerk_v066_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcassets (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcassetsemadd_63d_jerk_v067_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcassets (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcassetssgsq_126d_jerk_v068_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcppne (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcppneddn_42d_jerk_v069_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcppne (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_sbcppneaccr_63d_jerk_v070_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcppne (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcppneemadd_126d_jerk_v071_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcppne (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcppnesgsq_21d_jerk_v072_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revppne (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_revppneddn_63d_jerk_v073_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revppne (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_revppneaccr_126d_jerk_v074_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revppne (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_revppneemadd_21d_jerk_v075_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revppne (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_revppnesgsq_42d_jerk_v076_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvassets (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_totinvassetsddn_126d_jerk_v077_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvassets (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_totinvassetsaccr_21d_jerk_v078_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvassets (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_totinvassetsemadd_42d_jerk_v079_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvassets (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvassetssgsq_63d_jerk_v080_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvppne (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_totinvppneddn_21d_jerk_v081_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvppne (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_totinvppneaccr_42d_jerk_v082_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvppne (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_totinvppneemadd_63d_jerk_v083_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of totinvppne (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvppnesgsq_126d_jerk_v084_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexshare (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_capexshareddn_42d_jerk_v085_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexshare (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_capexshareaccr_63d_jerk_v086_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexshare (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_capexshareemadd_126d_jerk_v087_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexshare (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsharesgsq_21d_jerk_v088_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcshare (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcshareddn_63d_jerk_v089_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcshare (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_sbcshareaccr_126d_jerk_v090_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcshare (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcshareemadd_21d_jerk_v091_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcshare (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcsharesgsq_42d_jerk_v092_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbccapexr (base ~252d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_sbccapexrddn_126d_jerk_v093_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbccapexr (base ~252d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_sbccapexraccr_21d_jerk_v094_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbccapexr (base ~252d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_sbccapexremadd_42d_jerk_v095_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbccapexr (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbccapexrsgsq_63d_jerk_v096_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbcmix (base ~252d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixddn_21d_jerk_v097_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbcmix (base ~252d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixaccr_42d_jerk_v098_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbcmix (base ~252d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixemadd_63d_jerk_v099_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexsbcmix (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixsgsq_126d_jerk_v100_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revassets (base ~252d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_revassetsddn_42d_jerk_v101_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revassets (base ~252d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_revassetsaccr_63d_jerk_v102_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revassets (base ~252d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_revassetsemadd_126d_jerk_v103_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_revassetssgsq_21d_jerk_v104_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppneassets (base ~252d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_ppneassetsddn_63d_jerk_v105_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppneassets (base ~252d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_ppneassetsaccr_126d_jerk_v106_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppneassets (base ~252d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_ppneassetsemadd_21d_jerk_v107_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppneassets (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_ppneassetssgsq_42d_jerk_v108_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrowlv (base ~126d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvddn_126d_jerk_v109_signal(capex):
    lv = _glog(capex, 63)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrowlv (base ~126d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvaccr_21d_jerk_v110_signal(capex):
    lv = _glog(capex, 63)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrowlv (base ~126d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvemadd_42d_jerk_v111_signal(capex):
    lv = _glog(capex, 63)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrowlv (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvsgsq_63d_jerk_v112_signal(capex):
    lv = _glog(capex, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrowlv (base ~126d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvddn_21d_jerk_v113_signal(rnd):
    lv = _glog(rnd, 63)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrowlv (base ~126d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvaccr_42d_jerk_v114_signal(rnd):
    lv = _glog(rnd, 63)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrowlv (base ~126d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvemadd_63d_jerk_v115_signal(rnd):
    lv = _glog(rnd, 63)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrowlv (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvsgsq_126d_jerk_v116_signal(rnd):
    lv = _glog(rnd, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrowlv (base ~126d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvddn_42d_jerk_v117_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrowlv (base ~126d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvaccr_63d_jerk_v118_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrowlv (base ~126d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvemadd_126d_jerk_v119_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrowlv (base ~126d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvsgsq_21d_jerk_v120_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppnegrowlv (base ~126d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvddn_63d_jerk_v121_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppnegrowlv (base ~126d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvaccr_126d_jerk_v122_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppnegrowlv (base ~126d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvemadd_21d_jerk_v123_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ppnegrowlv (base ~126d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvsgsq_42d_jerk_v124_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revgrowlv (base ~126d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_revgrowlvddn_126d_jerk_v125_signal(revenue):
    lv = _glog(revenue, 63)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revgrowlv (base ~126d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_revgrowlvaccr_21d_jerk_v126_signal(revenue):
    lv = _glog(revenue, 63)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revgrowlv (base ~126d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_revgrowlvemadd_42d_jerk_v127_signal(revenue):
    lv = _glog(revenue, 63)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of revgrowlv (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_revgrowlvsgsq_63d_jerk_v128_signal(revenue):
    lv = _glog(revenue, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of assetsgrowlv (base ~126d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvddn_21d_jerk_v129_signal(assets):
    lv = _glog(assets, 63)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of assetsgrowlv (base ~126d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvaccr_42d_jerk_v130_signal(assets):
    lv = _glog(assets, 63)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of assetsgrowlv (base ~126d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvemadd_63d_jerk_v131_signal(assets):
    lv = _glog(assets, 63)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of assetsgrowlv (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvsgsq_126d_jerk_v132_signal(assets):
    lv = _glog(assets, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrow126 (base ~126d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_capexgrow126ddn_42d_jerk_v133_signal(capex):
    lv = _glog(capex, 126)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrow126 (base ~126d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_capexgrow126accr_63d_jerk_v134_signal(capex):
    lv = _glog(capex, 126)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrow126 (base ~126d) via 126d emadd operator
def f27ri_f27_reinvestment_dynamics_capexgrow126emadd_126d_jerk_v135_signal(capex):
    lv = _glog(capex, 126)
    b = (lambda e: e - 2*e.shift(126) + e.shift(2*126))(lv.ewm(span=4*126, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexgrow126 (base ~126d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexgrow126sgsq_21d_jerk_v136_signal(capex):
    lv = _glog(capex, 126)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrow126 (base ~126d) via 63d ddn operator
def f27ri_f27_reinvestment_dynamics_rndgrow126ddn_63d_jerk_v137_signal(rnd):
    lv = _glog(rnd, 126)
    b = ((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrow126 (base ~126d) via 126d accr operator
def f27ri_f27_reinvestment_dynamics_rndgrow126accr_126d_jerk_v138_signal(rnd):
    lv = _glog(rnd, 126)
    b = _rank(lv.pct_change(126) - lv.pct_change(126).shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrow126 (base ~126d) via 21d emadd operator
def f27ri_f27_reinvestment_dynamics_rndgrow126emadd_21d_jerk_v139_signal(rnd):
    lv = _glog(rnd, 126)
    b = (lambda e: e - 2*e.shift(21) + e.shift(2*21))(lv.ewm(span=4*21, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rndgrow126 (base ~126d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndgrow126sgsq_42d_jerk_v140_signal(rnd):
    lv = _glog(rnd, 126)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrow126 (base ~126d) via 126d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126ddn_126d_jerk_v141_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = ((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrow126 (base ~126d) via 21d accr operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126accr_21d_jerk_v142_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = _rank(lv.pct_change(21) - lv.pct_change(21).shift(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrow126 (base ~126d) via 42d emadd operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126emadd_42d_jerk_v143_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = (lambda e: e - 2*e.shift(42) + e.shift(2*42))(lv.ewm(span=4*42, min_periods=42).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcgrow126 (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126sgsq_63d_jerk_v144_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(63)) - (lv.shift(63) - lv.shift(2*63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexvsrndg (base ~126d) via 21d ddn operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgddn_21d_jerk_v145_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = ((lv - lv.shift(21)) - (lv.shift(21) - lv.shift(2*21))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexvsrndg (base ~126d) via 42d accr operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgaccr_42d_jerk_v146_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = _rank(lv.pct_change(42) - lv.pct_change(42).shift(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexvsrndg (base ~126d) via 63d emadd operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgemadd_63d_jerk_v147_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = (lambda e: e - 2*e.shift(63) + e.shift(2*63))(lv.ewm(span=4*63, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of capexvsrndg (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgsgsq_126d_jerk_v148_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = (lambda a: np.sign(a) * a.abs() ** 0.5)((lv - lv.shift(126)) - (lv.shift(126) - lv.shift(2*126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcvscapexg (base ~126d) via 42d ddn operator
def f27ri_f27_reinvestment_dynamics_sbcvscapexgddn_42d_jerk_v149_signal(sbcomp, capex):
    lv = _glog(sbcomp, 63) - _glog(capex, 63)
    b = ((lv - lv.shift(42)) - (lv.shift(42) - lv.shift(2*42))) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sbcvscapexg (base ~126d) via 63d accr operator
def f27ri_f27_reinvestment_dynamics_sbcvscapexgaccr_63d_jerk_v150_signal(sbcomp, capex):
    lv = _glog(sbcomp, 63) - _glog(capex, 63)
    b = _rank(lv.pct_change(63) - lv.pct_change(63).shift(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ri_f27_reinvestment_dynamics_capexrevddn_21d_jerk_v001_signal,
    f27ri_f27_reinvestment_dynamics_capexrevaccr_42d_jerk_v002_signal,
    f27ri_f27_reinvestment_dynamics_capexrevemadd_63d_jerk_v003_signal,
    f27ri_f27_reinvestment_dynamics_capexrevsgsq_126d_jerk_v004_signal,
    f27ri_f27_reinvestment_dynamics_rndrevddn_42d_jerk_v005_signal,
    f27ri_f27_reinvestment_dynamics_rndrevaccr_63d_jerk_v006_signal,
    f27ri_f27_reinvestment_dynamics_rndrevemadd_126d_jerk_v007_signal,
    f27ri_f27_reinvestment_dynamics_rndrevsgsq_21d_jerk_v008_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevddn_63d_jerk_v009_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevaccr_126d_jerk_v010_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevemadd_21d_jerk_v011_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevsgsq_42d_jerk_v012_signal,
    f27ri_f27_reinvestment_dynamics_reinvrateddn_126d_jerk_v013_signal,
    f27ri_f27_reinvestment_dynamics_reinvrateaccr_21d_jerk_v014_signal,
    f27ri_f27_reinvestment_dynamics_reinvrateemadd_42d_jerk_v015_signal,
    f27ri_f27_reinvestment_dynamics_reinvratesgsq_63d_jerk_v016_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexddn_21d_jerk_v017_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexaccr_42d_jerk_v018_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexemadd_63d_jerk_v019_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexsgsq_126d_jerk_v020_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsddn_42d_jerk_v021_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsaccr_63d_jerk_v022_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsemadd_126d_jerk_v023_signal,
    f27ri_f27_reinvestment_dynamics_rndassetssgsq_21d_jerk_v024_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsddn_63d_jerk_v025_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsaccr_126d_jerk_v026_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsemadd_21d_jerk_v027_signal,
    f27ri_f27_reinvestment_dynamics_capexassetssgsq_42d_jerk_v028_signal,
    f27ri_f27_reinvestment_dynamics_rndmixddn_126d_jerk_v029_signal,
    f27ri_f27_reinvestment_dynamics_rndmixaccr_21d_jerk_v030_signal,
    f27ri_f27_reinvestment_dynamics_rndmixemadd_42d_jerk_v031_signal,
    f27ri_f27_reinvestment_dynamics_rndmixsgsq_63d_jerk_v032_signal,
    f27ri_f27_reinvestment_dynamics_totinvddn_21d_jerk_v033_signal,
    f27ri_f27_reinvestment_dynamics_totinvaccr_42d_jerk_v034_signal,
    f27ri_f27_reinvestment_dynamics_totinvemadd_63d_jerk_v035_signal,
    f27ri_f27_reinvestment_dynamics_totinvsgsq_126d_jerk_v036_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsddn_42d_jerk_v037_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsaccr_63d_jerk_v038_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsemadd_126d_jerk_v039_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetssgsq_21d_jerk_v040_signal,
    f27ri_f27_reinvestment_dynamics_reinvppneddn_63d_jerk_v041_signal,
    f27ri_f27_reinvestment_dynamics_reinvppneaccr_126d_jerk_v042_signal,
    f27ri_f27_reinvestment_dynamics_reinvppneemadd_21d_jerk_v043_signal,
    f27ri_f27_reinvestment_dynamics_reinvppnesgsq_42d_jerk_v044_signal,
    f27ri_f27_reinvestment_dynamics_invtiltddn_126d_jerk_v045_signal,
    f27ri_f27_reinvestment_dynamics_invtiltaccr_21d_jerk_v046_signal,
    f27ri_f27_reinvestment_dynamics_invtiltemadd_42d_jerk_v047_signal,
    f27ri_f27_reinvestment_dynamics_invtiltsgsq_63d_jerk_v048_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltddn_21d_jerk_v049_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltaccr_42d_jerk_v050_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltemadd_63d_jerk_v051_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltsgsq_126d_jerk_v052_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltddn_42d_jerk_v053_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltaccr_63d_jerk_v054_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltemadd_126d_jerk_v055_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltsgsq_21d_jerk_v056_signal,
    f27ri_f27_reinvestment_dynamics_capexppnesprddn_63d_jerk_v057_signal,
    f27ri_f27_reinvestment_dynamics_capexppnespraccr_126d_jerk_v058_signal,
    f27ri_f27_reinvestment_dynamics_capexppnespremadd_21d_jerk_v059_signal,
    f27ri_f27_reinvestment_dynamics_capexppnesprsgsq_42d_jerk_v060_signal,
    f27ri_f27_reinvestment_dynamics_rndppneddn_126d_jerk_v061_signal,
    f27ri_f27_reinvestment_dynamics_rndppneaccr_21d_jerk_v062_signal,
    f27ri_f27_reinvestment_dynamics_rndppneemadd_42d_jerk_v063_signal,
    f27ri_f27_reinvestment_dynamics_rndppnesgsq_63d_jerk_v064_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetsddn_21d_jerk_v065_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetsaccr_42d_jerk_v066_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetsemadd_63d_jerk_v067_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetssgsq_126d_jerk_v068_signal,
    f27ri_f27_reinvestment_dynamics_sbcppneddn_42d_jerk_v069_signal,
    f27ri_f27_reinvestment_dynamics_sbcppneaccr_63d_jerk_v070_signal,
    f27ri_f27_reinvestment_dynamics_sbcppneemadd_126d_jerk_v071_signal,
    f27ri_f27_reinvestment_dynamics_sbcppnesgsq_21d_jerk_v072_signal,
    f27ri_f27_reinvestment_dynamics_revppneddn_63d_jerk_v073_signal,
    f27ri_f27_reinvestment_dynamics_revppneaccr_126d_jerk_v074_signal,
    f27ri_f27_reinvestment_dynamics_revppneemadd_21d_jerk_v075_signal,
    f27ri_f27_reinvestment_dynamics_revppnesgsq_42d_jerk_v076_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetsddn_126d_jerk_v077_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetsaccr_21d_jerk_v078_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetsemadd_42d_jerk_v079_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetssgsq_63d_jerk_v080_signal,
    f27ri_f27_reinvestment_dynamics_totinvppneddn_21d_jerk_v081_signal,
    f27ri_f27_reinvestment_dynamics_totinvppneaccr_42d_jerk_v082_signal,
    f27ri_f27_reinvestment_dynamics_totinvppneemadd_63d_jerk_v083_signal,
    f27ri_f27_reinvestment_dynamics_totinvppnesgsq_126d_jerk_v084_signal,
    f27ri_f27_reinvestment_dynamics_capexshareddn_42d_jerk_v085_signal,
    f27ri_f27_reinvestment_dynamics_capexshareaccr_63d_jerk_v086_signal,
    f27ri_f27_reinvestment_dynamics_capexshareemadd_126d_jerk_v087_signal,
    f27ri_f27_reinvestment_dynamics_capexsharesgsq_21d_jerk_v088_signal,
    f27ri_f27_reinvestment_dynamics_sbcshareddn_63d_jerk_v089_signal,
    f27ri_f27_reinvestment_dynamics_sbcshareaccr_126d_jerk_v090_signal,
    f27ri_f27_reinvestment_dynamics_sbcshareemadd_21d_jerk_v091_signal,
    f27ri_f27_reinvestment_dynamics_sbcsharesgsq_42d_jerk_v092_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexrddn_126d_jerk_v093_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexraccr_21d_jerk_v094_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexremadd_42d_jerk_v095_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexrsgsq_63d_jerk_v096_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixddn_21d_jerk_v097_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixaccr_42d_jerk_v098_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixemadd_63d_jerk_v099_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixsgsq_126d_jerk_v100_signal,
    f27ri_f27_reinvestment_dynamics_revassetsddn_42d_jerk_v101_signal,
    f27ri_f27_reinvestment_dynamics_revassetsaccr_63d_jerk_v102_signal,
    f27ri_f27_reinvestment_dynamics_revassetsemadd_126d_jerk_v103_signal,
    f27ri_f27_reinvestment_dynamics_revassetssgsq_21d_jerk_v104_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetsddn_63d_jerk_v105_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetsaccr_126d_jerk_v106_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetsemadd_21d_jerk_v107_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetssgsq_42d_jerk_v108_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvddn_126d_jerk_v109_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvaccr_21d_jerk_v110_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvemadd_42d_jerk_v111_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvsgsq_63d_jerk_v112_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvddn_21d_jerk_v113_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvaccr_42d_jerk_v114_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvemadd_63d_jerk_v115_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvsgsq_126d_jerk_v116_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvddn_42d_jerk_v117_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvaccr_63d_jerk_v118_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvemadd_126d_jerk_v119_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvsgsq_21d_jerk_v120_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvddn_63d_jerk_v121_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvaccr_126d_jerk_v122_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvemadd_21d_jerk_v123_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvsgsq_42d_jerk_v124_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvddn_126d_jerk_v125_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvaccr_21d_jerk_v126_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvemadd_42d_jerk_v127_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvsgsq_63d_jerk_v128_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvddn_21d_jerk_v129_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvaccr_42d_jerk_v130_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvemadd_63d_jerk_v131_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvsgsq_126d_jerk_v132_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126ddn_42d_jerk_v133_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126accr_63d_jerk_v134_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126emadd_126d_jerk_v135_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126sgsq_21d_jerk_v136_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126ddn_63d_jerk_v137_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126accr_126d_jerk_v138_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126emadd_21d_jerk_v139_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126sgsq_42d_jerk_v140_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126ddn_126d_jerk_v141_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126accr_21d_jerk_v142_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126emadd_42d_jerk_v143_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126sgsq_63d_jerk_v144_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgddn_21d_jerk_v145_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgaccr_42d_jerk_v146_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgemadd_63d_jerk_v147_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgsgsq_126d_jerk_v148_signal,
    f27ri_f27_reinvestment_dynamics_sbcvscapexgddn_42d_jerk_v149_signal,
    f27ri_f27_reinvestment_dynamics_sbcvscapexgaccr_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REINVESTMENT_DYNAMICS_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    capex = _fund(102, base=8e7, drift=0.025, vol=0.06).rename("capex")
    rnd = _fund(103, base=6e7, drift=0.035, vol=0.07).rename("rnd")
    sbcomp = _fund(104, base=3e7, drift=0.04, vol=0.08).rename("sbcomp")
    assets = _fund(105, base=2e9, drift=0.02, vol=0.03).rename("assets")
    ppnenet = _fund(106, base=5e8, drift=0.02, vol=0.05).rename("ppnenet")

    cols = {"revenue": revenue, "capex": capex, "rnd": rnd,
            "sbcomp": sbcomp, "assets": assets, "ppnenet": ppnenet}

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

    print("OK f27_reinvestment_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
