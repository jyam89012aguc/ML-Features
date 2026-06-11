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


# slope of capexrev (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_capexrevdn_21d_slope_v001_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexrev (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_capexrevpctr_42d_slope_v002_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexrev (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_capexrevemad_63d_slope_v003_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexrev (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexrevsgsq_126d_slope_v004_signal(capex, revenue):
    lv = _capex_rev(capex, revenue)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndrev (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_rndrevdn_42d_slope_v005_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndrev (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_rndrevpctr_63d_slope_v006_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndrev (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_rndrevemad_126d_slope_v007_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndrev (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndrevsgsq_21d_slope_v008_signal(rnd, revenue):
    lv = _rnd_rev(rnd, revenue)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcrev (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_sbcrevdn_63d_slope_v009_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcrev (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcrevpctr_126d_slope_v010_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcrev (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_sbcrevemad_21d_slope_v011_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcrev (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcrevsgsq_42d_slope_v012_signal(sbcomp, revenue):
    lv = _sbc_rev(sbcomp, revenue)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvrate (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_reinvratedn_126d_slope_v013_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvrate (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_reinvratepctr_21d_slope_v014_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvrate (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_reinvrateemad_42d_slope_v015_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvrate (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvratesgsq_63d_slope_v016_signal(capex, rnd, revenue):
    lv = _reinv_rate(capex, rnd, revenue)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growthcapex (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_growthcapexdn_21d_slope_v017_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growthcapex (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_growthcapexpctr_42d_slope_v018_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growthcapex (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_growthcapexemad_63d_slope_v019_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growthcapex (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_growthcapexsgsq_126d_slope_v020_signal(capex, ppnenet):
    lv = _growth_capex(capex, ppnenet)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndassets (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_rndassetsdn_42d_slope_v021_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndassets (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_rndassetspctr_63d_slope_v022_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndassets (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_rndassetsemad_126d_slope_v023_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndassetssgsq_21d_slope_v024_signal(rnd, assets):
    lv = rnd / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexassets (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_capexassetsdn_63d_slope_v025_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexassets (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_capexassetspctr_126d_slope_v026_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexassets (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_capexassetsemad_21d_slope_v027_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexassets (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexassetssgsq_42d_slope_v028_signal(capex, assets):
    lv = capex / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndmix (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_rndmixdn_126d_slope_v029_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndmix (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_rndmixpctr_21d_slope_v030_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndmix (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_rndmixemad_42d_slope_v031_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndmix (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndmixsgsq_63d_slope_v032_signal(capex, rnd):
    lv = rnd / (capex + rnd).replace(0, np.nan)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinv (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_totinvdn_21d_slope_v033_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinv (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_totinvpctr_42d_slope_v034_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinv (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_totinvemad_63d_slope_v035_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinv (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvsgsq_126d_slope_v036_signal(capex, rnd, sbcomp, revenue):
    lv = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvassets (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_reinvassetsdn_42d_slope_v037_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvassets (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_reinvassetspctr_63d_slope_v038_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvassets (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_reinvassetsemad_126d_slope_v039_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvassetssgsq_21d_slope_v040_signal(capex, rnd, assets):
    lv = (capex + rnd) / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvppne (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_reinvppnedn_63d_slope_v041_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvppne (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_reinvppnepctr_126d_slope_v042_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvppne (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_reinvppneemad_21d_slope_v043_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of reinvppne (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_reinvppnesgsq_42d_slope_v044_signal(capex, rnd, ppnenet):
    lv = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of invtilt (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_invtiltdn_126d_slope_v045_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of invtilt (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_invtiltpctr_21d_slope_v046_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of invtilt (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_invtiltemad_42d_slope_v047_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of invtilt (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_invtiltsgsq_63d_slope_v048_signal(capex, rnd, revenue):
    lv = _capex_rev(capex, revenue) - _rnd_rev(rnd, revenue)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbctilt (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltdn_21d_slope_v049_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbctilt (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltpctr_42d_slope_v050_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbctilt (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltemad_63d_slope_v051_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbctilt (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsbctiltsgsq_126d_slope_v052_signal(capex, sbcomp, revenue):
    lv = _capex_rev(capex, revenue) - _sbc_rev(sbcomp, revenue)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndsbctilt (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltdn_42d_slope_v053_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndsbctilt (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltpctr_63d_slope_v054_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndsbctilt (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltemad_126d_slope_v055_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndsbctilt (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndsbctiltsgsq_21d_slope_v056_signal(rnd, sbcomp, revenue):
    lv = _rnd_rev(rnd, revenue) - _sbc_rev(sbcomp, revenue)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexppnespr (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_capexppnesprdn_63d_slope_v057_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexppnespr (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_capexppnesprpctr_126d_slope_v058_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexppnespr (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_capexppnespremad_21d_slope_v059_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexppnespr (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexppnesprsgsq_42d_slope_v060_signal(capex, ppnenet, revenue):
    lv = _growth_capex(capex, ppnenet) - _capex_rev(capex, revenue)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndppne (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_rndppnedn_126d_slope_v061_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndppne (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_rndppnepctr_21d_slope_v062_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndppne (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_rndppneemad_42d_slope_v063_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndppne (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndppnesgsq_63d_slope_v064_signal(rnd, ppnenet):
    lv = rnd / ppnenet.replace(0, np.nan)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcassets (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_sbcassetsdn_21d_slope_v065_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcassets (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcassetspctr_42d_slope_v066_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcassets (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_sbcassetsemad_63d_slope_v067_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcassets (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcassetssgsq_126d_slope_v068_signal(sbcomp, assets):
    lv = sbcomp / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcppne (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_sbcppnedn_42d_slope_v069_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcppne (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcppnepctr_63d_slope_v070_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcppne (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_sbcppneemad_126d_slope_v071_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcppne (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcppnesgsq_21d_slope_v072_signal(sbcomp, ppnenet):
    lv = sbcomp / ppnenet.replace(0, np.nan)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revppne (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_revppnedn_63d_slope_v073_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revppne (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_revppnepctr_126d_slope_v074_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revppne (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_revppneemad_21d_slope_v075_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revppne (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_revppnesgsq_42d_slope_v076_signal(revenue, ppnenet):
    lv = revenue / ppnenet.replace(0, np.nan)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvassets (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_totinvassetsdn_126d_slope_v077_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvassets (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_totinvassetspctr_21d_slope_v078_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvassets (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_totinvassetsemad_42d_slope_v079_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvassets (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvassetssgsq_63d_slope_v080_signal(capex, rnd, sbcomp, assets):
    lv = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvppne (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_totinvppnedn_21d_slope_v081_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvppne (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_totinvppnepctr_42d_slope_v082_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvppne (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_totinvppneemad_63d_slope_v083_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of totinvppne (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_totinvppnesgsq_126d_slope_v084_signal(capex, rnd, sbcomp, ppnenet):
    lv = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexshare (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_capexsharedn_42d_slope_v085_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexshare (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_capexsharepctr_63d_slope_v086_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexshare (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_capexshareemad_126d_slope_v087_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexshare (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsharesgsq_21d_slope_v088_signal(capex, rnd, sbcomp):
    lv = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcshare (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_sbcsharedn_63d_slope_v089_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcshare (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcsharepctr_126d_slope_v090_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcshare (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_sbcshareemad_21d_slope_v091_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcshare (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcsharesgsq_42d_slope_v092_signal(capex, rnd, sbcomp):
    lv = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbccapexr (base ~252d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_sbccapexrdn_126d_slope_v093_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbccapexr (base ~252d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_sbccapexrpctr_21d_slope_v094_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbccapexr (base ~252d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_sbccapexremad_42d_slope_v095_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbccapexr (base ~252d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbccapexrsgsq_63d_slope_v096_signal(sbcomp, capex):
    lv = sbcomp / capex.replace(0, np.nan)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbcmix (base ~252d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixdn_21d_slope_v097_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbcmix (base ~252d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixpctr_42d_slope_v098_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbcmix (base ~252d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixemad_63d_slope_v099_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexsbcmix (base ~252d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexsbcmixsgsq_126d_slope_v100_signal(capex, sbcomp):
    lv = capex / (capex + sbcomp).replace(0, np.nan)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revassets (base ~252d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_revassetsdn_42d_slope_v101_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revassets (base ~252d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_revassetspctr_63d_slope_v102_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revassets (base ~252d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_revassetsemad_126d_slope_v103_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revassets (base ~252d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_revassetssgsq_21d_slope_v104_signal(revenue, assets):
    lv = revenue / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppneassets (base ~252d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_ppneassetsdn_63d_slope_v105_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppneassets (base ~252d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_ppneassetspctr_126d_slope_v106_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppneassets (base ~252d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_ppneassetsemad_21d_slope_v107_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppneassets (base ~252d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_ppneassetssgsq_42d_slope_v108_signal(ppnenet, assets):
    lv = ppnenet / assets.replace(0, np.nan)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrowlv (base ~126d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvdn_126d_slope_v109_signal(capex):
    lv = _glog(capex, 63)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrowlv (base ~126d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvpctr_21d_slope_v110_signal(capex):
    lv = _glog(capex, 63)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrowlv (base ~126d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvemad_42d_slope_v111_signal(capex):
    lv = _glog(capex, 63)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrowlv (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexgrowlvsgsq_63d_slope_v112_signal(capex):
    lv = _glog(capex, 63)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrowlv (base ~126d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvdn_21d_slope_v113_signal(rnd):
    lv = _glog(rnd, 63)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrowlv (base ~126d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvpctr_42d_slope_v114_signal(rnd):
    lv = _glog(rnd, 63)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrowlv (base ~126d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvemad_63d_slope_v115_signal(rnd):
    lv = _glog(rnd, 63)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrowlv (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndgrowlvsgsq_126d_slope_v116_signal(rnd):
    lv = _glog(rnd, 63)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrowlv (base ~126d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvdn_42d_slope_v117_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrowlv (base ~126d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvpctr_63d_slope_v118_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrowlv (base ~126d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvemad_126d_slope_v119_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrowlv (base ~126d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcgrowlvsgsq_21d_slope_v120_signal(sbcomp):
    lv = _glog(sbcomp, 63)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppnegrowlv (base ~126d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvdn_63d_slope_v121_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppnegrowlv (base ~126d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvpctr_126d_slope_v122_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppnegrowlv (base ~126d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvemad_21d_slope_v123_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of ppnegrowlv (base ~126d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_ppnegrowlvsgsq_42d_slope_v124_signal(ppnenet):
    lv = _glog(ppnenet, 63)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revgrowlv (base ~126d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_revgrowlvdn_126d_slope_v125_signal(revenue):
    lv = _glog(revenue, 63)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revgrowlv (base ~126d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_revgrowlvpctr_21d_slope_v126_signal(revenue):
    lv = _glog(revenue, 63)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revgrowlv (base ~126d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_revgrowlvemad_42d_slope_v127_signal(revenue):
    lv = _glog(revenue, 63)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of revgrowlv (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_revgrowlvsgsq_63d_slope_v128_signal(revenue):
    lv = _glog(revenue, 63)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of assetsgrowlv (base ~126d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvdn_21d_slope_v129_signal(assets):
    lv = _glog(assets, 63)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of assetsgrowlv (base ~126d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvpctr_42d_slope_v130_signal(assets):
    lv = _glog(assets, 63)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of assetsgrowlv (base ~126d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvemad_63d_slope_v131_signal(assets):
    lv = _glog(assets, 63)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of assetsgrowlv (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_assetsgrowlvsgsq_126d_slope_v132_signal(assets):
    lv = _glog(assets, 63)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrow126 (base ~126d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_capexgrow126dn_42d_slope_v133_signal(capex):
    lv = _glog(capex, 126)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrow126 (base ~126d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_capexgrow126pctr_63d_slope_v134_signal(capex):
    lv = _glog(capex, 126)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrow126 (base ~126d) via 126d emad operator
def f27ri_f27_reinvestment_dynamics_capexgrow126emad_126d_slope_v135_signal(capex):
    lv = _glog(capex, 126)
    b = lv.ewm(span=4*126, min_periods=126).mean() - lv.ewm(span=4*126, min_periods=126).mean().shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexgrow126 (base ~126d) via 21d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexgrow126sgsq_21d_slope_v136_signal(capex):
    lv = _glog(capex, 126)
    b = np.sign(lv - lv.shift(21)) * (lv - lv.shift(21)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrow126 (base ~126d) via 63d dn operator
def f27ri_f27_reinvestment_dynamics_rndgrow126dn_63d_slope_v137_signal(rnd):
    lv = _glog(rnd, 126)
    b = (lv - lv.shift(63)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrow126 (base ~126d) via 126d pctr operator
def f27ri_f27_reinvestment_dynamics_rndgrow126pctr_126d_slope_v138_signal(rnd):
    lv = _glog(rnd, 126)
    b = _rank(lv.pct_change(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrow126 (base ~126d) via 21d emad operator
def f27ri_f27_reinvestment_dynamics_rndgrow126emad_21d_slope_v139_signal(rnd):
    lv = _glog(rnd, 126)
    b = lv.ewm(span=4*21, min_periods=21).mean() - lv.ewm(span=4*21, min_periods=21).mean().shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rndgrow126 (base ~126d) via 42d sgsq operator
def f27ri_f27_reinvestment_dynamics_rndgrow126sgsq_42d_slope_v140_signal(rnd):
    lv = _glog(rnd, 126)
    b = np.sign(lv - lv.shift(42)) * (lv - lv.shift(42)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrow126 (base ~126d) via 126d dn operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126dn_126d_slope_v141_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = (lv - lv.shift(126)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrow126 (base ~126d) via 21d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126pctr_21d_slope_v142_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = _rank(lv.pct_change(21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrow126 (base ~126d) via 42d emad operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126emad_42d_slope_v143_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = lv.ewm(span=4*42, min_periods=42).mean() - lv.ewm(span=4*42, min_periods=42).mean().shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcgrow126 (base ~126d) via 63d sgsq operator
def f27ri_f27_reinvestment_dynamics_sbcgrow126sgsq_63d_slope_v144_signal(sbcomp):
    lv = _glog(sbcomp, 126)
    b = np.sign(lv - lv.shift(63)) * (lv - lv.shift(63)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexvsrndg (base ~126d) via 21d dn operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgdn_21d_slope_v145_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = (lv - lv.shift(21)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexvsrndg (base ~126d) via 42d pctr operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgpctr_42d_slope_v146_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = _rank(lv.pct_change(42), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexvsrndg (base ~126d) via 63d emad operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgemad_63d_slope_v147_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = lv.ewm(span=4*63, min_periods=63).mean() - lv.ewm(span=4*63, min_periods=63).mean().shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capexvsrndg (base ~126d) via 126d sgsq operator
def f27ri_f27_reinvestment_dynamics_capexvsrndgsgsq_126d_slope_v148_signal(capex, rnd):
    lv = _glog(capex, 63) - _glog(rnd, 63)
    b = np.sign(lv - lv.shift(126)) * (lv - lv.shift(126)).abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcvscapexg (base ~126d) via 42d dn operator
def f27ri_f27_reinvestment_dynamics_sbcvscapexgdn_42d_slope_v149_signal(sbcomp, capex):
    lv = _glog(sbcomp, 63) - _glog(capex, 63)
    b = (lv - lv.shift(42)) / _std(lv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of sbcvscapexg (base ~126d) via 63d pctr operator
def f27ri_f27_reinvestment_dynamics_sbcvscapexgpctr_63d_slope_v150_signal(sbcomp, capex):
    lv = _glog(sbcomp, 63) - _glog(capex, 63)
    b = _rank(lv.pct_change(63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ri_f27_reinvestment_dynamics_capexrevdn_21d_slope_v001_signal,
    f27ri_f27_reinvestment_dynamics_capexrevpctr_42d_slope_v002_signal,
    f27ri_f27_reinvestment_dynamics_capexrevemad_63d_slope_v003_signal,
    f27ri_f27_reinvestment_dynamics_capexrevsgsq_126d_slope_v004_signal,
    f27ri_f27_reinvestment_dynamics_rndrevdn_42d_slope_v005_signal,
    f27ri_f27_reinvestment_dynamics_rndrevpctr_63d_slope_v006_signal,
    f27ri_f27_reinvestment_dynamics_rndrevemad_126d_slope_v007_signal,
    f27ri_f27_reinvestment_dynamics_rndrevsgsq_21d_slope_v008_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevdn_63d_slope_v009_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevpctr_126d_slope_v010_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevemad_21d_slope_v011_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevsgsq_42d_slope_v012_signal,
    f27ri_f27_reinvestment_dynamics_reinvratedn_126d_slope_v013_signal,
    f27ri_f27_reinvestment_dynamics_reinvratepctr_21d_slope_v014_signal,
    f27ri_f27_reinvestment_dynamics_reinvrateemad_42d_slope_v015_signal,
    f27ri_f27_reinvestment_dynamics_reinvratesgsq_63d_slope_v016_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexdn_21d_slope_v017_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexpctr_42d_slope_v018_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexemad_63d_slope_v019_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexsgsq_126d_slope_v020_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsdn_42d_slope_v021_signal,
    f27ri_f27_reinvestment_dynamics_rndassetspctr_63d_slope_v022_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsemad_126d_slope_v023_signal,
    f27ri_f27_reinvestment_dynamics_rndassetssgsq_21d_slope_v024_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsdn_63d_slope_v025_signal,
    f27ri_f27_reinvestment_dynamics_capexassetspctr_126d_slope_v026_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsemad_21d_slope_v027_signal,
    f27ri_f27_reinvestment_dynamics_capexassetssgsq_42d_slope_v028_signal,
    f27ri_f27_reinvestment_dynamics_rndmixdn_126d_slope_v029_signal,
    f27ri_f27_reinvestment_dynamics_rndmixpctr_21d_slope_v030_signal,
    f27ri_f27_reinvestment_dynamics_rndmixemad_42d_slope_v031_signal,
    f27ri_f27_reinvestment_dynamics_rndmixsgsq_63d_slope_v032_signal,
    f27ri_f27_reinvestment_dynamics_totinvdn_21d_slope_v033_signal,
    f27ri_f27_reinvestment_dynamics_totinvpctr_42d_slope_v034_signal,
    f27ri_f27_reinvestment_dynamics_totinvemad_63d_slope_v035_signal,
    f27ri_f27_reinvestment_dynamics_totinvsgsq_126d_slope_v036_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsdn_42d_slope_v037_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetspctr_63d_slope_v038_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsemad_126d_slope_v039_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetssgsq_21d_slope_v040_signal,
    f27ri_f27_reinvestment_dynamics_reinvppnedn_63d_slope_v041_signal,
    f27ri_f27_reinvestment_dynamics_reinvppnepctr_126d_slope_v042_signal,
    f27ri_f27_reinvestment_dynamics_reinvppneemad_21d_slope_v043_signal,
    f27ri_f27_reinvestment_dynamics_reinvppnesgsq_42d_slope_v044_signal,
    f27ri_f27_reinvestment_dynamics_invtiltdn_126d_slope_v045_signal,
    f27ri_f27_reinvestment_dynamics_invtiltpctr_21d_slope_v046_signal,
    f27ri_f27_reinvestment_dynamics_invtiltemad_42d_slope_v047_signal,
    f27ri_f27_reinvestment_dynamics_invtiltsgsq_63d_slope_v048_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltdn_21d_slope_v049_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltpctr_42d_slope_v050_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltemad_63d_slope_v051_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctiltsgsq_126d_slope_v052_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltdn_42d_slope_v053_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltpctr_63d_slope_v054_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltemad_126d_slope_v055_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctiltsgsq_21d_slope_v056_signal,
    f27ri_f27_reinvestment_dynamics_capexppnesprdn_63d_slope_v057_signal,
    f27ri_f27_reinvestment_dynamics_capexppnesprpctr_126d_slope_v058_signal,
    f27ri_f27_reinvestment_dynamics_capexppnespremad_21d_slope_v059_signal,
    f27ri_f27_reinvestment_dynamics_capexppnesprsgsq_42d_slope_v060_signal,
    f27ri_f27_reinvestment_dynamics_rndppnedn_126d_slope_v061_signal,
    f27ri_f27_reinvestment_dynamics_rndppnepctr_21d_slope_v062_signal,
    f27ri_f27_reinvestment_dynamics_rndppneemad_42d_slope_v063_signal,
    f27ri_f27_reinvestment_dynamics_rndppnesgsq_63d_slope_v064_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetsdn_21d_slope_v065_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetspctr_42d_slope_v066_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetsemad_63d_slope_v067_signal,
    f27ri_f27_reinvestment_dynamics_sbcassetssgsq_126d_slope_v068_signal,
    f27ri_f27_reinvestment_dynamics_sbcppnedn_42d_slope_v069_signal,
    f27ri_f27_reinvestment_dynamics_sbcppnepctr_63d_slope_v070_signal,
    f27ri_f27_reinvestment_dynamics_sbcppneemad_126d_slope_v071_signal,
    f27ri_f27_reinvestment_dynamics_sbcppnesgsq_21d_slope_v072_signal,
    f27ri_f27_reinvestment_dynamics_revppnedn_63d_slope_v073_signal,
    f27ri_f27_reinvestment_dynamics_revppnepctr_126d_slope_v074_signal,
    f27ri_f27_reinvestment_dynamics_revppneemad_21d_slope_v075_signal,
    f27ri_f27_reinvestment_dynamics_revppnesgsq_42d_slope_v076_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetsdn_126d_slope_v077_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetspctr_21d_slope_v078_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetsemad_42d_slope_v079_signal,
    f27ri_f27_reinvestment_dynamics_totinvassetssgsq_63d_slope_v080_signal,
    f27ri_f27_reinvestment_dynamics_totinvppnedn_21d_slope_v081_signal,
    f27ri_f27_reinvestment_dynamics_totinvppnepctr_42d_slope_v082_signal,
    f27ri_f27_reinvestment_dynamics_totinvppneemad_63d_slope_v083_signal,
    f27ri_f27_reinvestment_dynamics_totinvppnesgsq_126d_slope_v084_signal,
    f27ri_f27_reinvestment_dynamics_capexsharedn_42d_slope_v085_signal,
    f27ri_f27_reinvestment_dynamics_capexsharepctr_63d_slope_v086_signal,
    f27ri_f27_reinvestment_dynamics_capexshareemad_126d_slope_v087_signal,
    f27ri_f27_reinvestment_dynamics_capexsharesgsq_21d_slope_v088_signal,
    f27ri_f27_reinvestment_dynamics_sbcsharedn_63d_slope_v089_signal,
    f27ri_f27_reinvestment_dynamics_sbcsharepctr_126d_slope_v090_signal,
    f27ri_f27_reinvestment_dynamics_sbcshareemad_21d_slope_v091_signal,
    f27ri_f27_reinvestment_dynamics_sbcsharesgsq_42d_slope_v092_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexrdn_126d_slope_v093_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexrpctr_21d_slope_v094_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexremad_42d_slope_v095_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexrsgsq_63d_slope_v096_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixdn_21d_slope_v097_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixpctr_42d_slope_v098_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixemad_63d_slope_v099_signal,
    f27ri_f27_reinvestment_dynamics_capexsbcmixsgsq_126d_slope_v100_signal,
    f27ri_f27_reinvestment_dynamics_revassetsdn_42d_slope_v101_signal,
    f27ri_f27_reinvestment_dynamics_revassetspctr_63d_slope_v102_signal,
    f27ri_f27_reinvestment_dynamics_revassetsemad_126d_slope_v103_signal,
    f27ri_f27_reinvestment_dynamics_revassetssgsq_21d_slope_v104_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetsdn_63d_slope_v105_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetspctr_126d_slope_v106_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetsemad_21d_slope_v107_signal,
    f27ri_f27_reinvestment_dynamics_ppneassetssgsq_42d_slope_v108_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvdn_126d_slope_v109_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvpctr_21d_slope_v110_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvemad_42d_slope_v111_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowlvsgsq_63d_slope_v112_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvdn_21d_slope_v113_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvpctr_42d_slope_v114_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvemad_63d_slope_v115_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowlvsgsq_126d_slope_v116_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvdn_42d_slope_v117_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvpctr_63d_slope_v118_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvemad_126d_slope_v119_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrowlvsgsq_21d_slope_v120_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvdn_63d_slope_v121_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvpctr_126d_slope_v122_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvemad_21d_slope_v123_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrowlvsgsq_42d_slope_v124_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvdn_126d_slope_v125_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvpctr_21d_slope_v126_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvemad_42d_slope_v127_signal,
    f27ri_f27_reinvestment_dynamics_revgrowlvsgsq_63d_slope_v128_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvdn_21d_slope_v129_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvpctr_42d_slope_v130_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvemad_63d_slope_v131_signal,
    f27ri_f27_reinvestment_dynamics_assetsgrowlvsgsq_126d_slope_v132_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126dn_42d_slope_v133_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126pctr_63d_slope_v134_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126emad_126d_slope_v135_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow126sgsq_21d_slope_v136_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126dn_63d_slope_v137_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126pctr_126d_slope_v138_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126emad_21d_slope_v139_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow126sgsq_42d_slope_v140_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126dn_126d_slope_v141_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126pctr_21d_slope_v142_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126emad_42d_slope_v143_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow126sgsq_63d_slope_v144_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgdn_21d_slope_v145_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgpctr_42d_slope_v146_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgemad_63d_slope_v147_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrndgsgsq_126d_slope_v148_signal,
    f27ri_f27_reinvestment_dynamics_sbcvscapexgdn_42d_slope_v149_signal,
    f27ri_f27_reinvestment_dynamics_sbcvscapexgpctr_63d_slope_v150_signal,
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

    print("OK f27_reinvestment_dynamics_2nd_derivatives_001_150_claude: %d features pass" % n_features)
