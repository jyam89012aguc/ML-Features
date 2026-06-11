import inspect
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# f47_ma_rollup_acquisition -- 2nd-derivative file: SLOPE features (150).
# Each feature is the 1st math derivative (slope / rate-of-change) of a distinct
# M&A / roll-up base expression, fully expanded (no factories / loops / exec).
# Slope window is chosen appropriate to the base window.
# Columns: ncfbus, ncfinv, investments, intangibles, revenue, marketcap, ncfo.
# Every feature uses >=1 fundamental column.
# ---------------------------------------------------------------------------

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _sum(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _acq_spend(ncfbus):
    return (-ncfbus).clip(lower=0)


def _divest_in(ncfbus):
    return ncfbus.clip(lower=0)


def _intensity(ncfbus, revenue, w):
    return _sum(_acq_spend(ncfbus), w) / _sum(revenue, w).replace(0, np.nan)


def _material_q(ncfbus, revenue, thresh):
    return (ncfbus.abs() > (thresh * revenue)).astype(float)


def _ops_funding(ncfbus, ncfo, w):
    return _sum(ncfo.clip(lower=0), w) / _sum(_acq_spend(ncfbus), w).replace(0, np.nan)


def _goodwill_build(intangibles, revenue, w):
    return (intangibles - intangibles.shift(w)) / _mean(revenue, w).replace(0, np.nan)


def _acquirer_sign(ncfbus, w):
    return _mean(ncfbus, w) / _mean(ncfbus.abs(), w).replace(0, np.nan)


def _deal_vs_cap(ncfbus, marketcap, w):
    return _sum(_acq_spend(ncfbus), w) / marketcap.replace(0, np.nan)


# ============================================================
# slope = 1st discrete derivative of a base expression over window sw, per-day.

def f47ma_f47_ma_rollup_acquisition_intensity_252d_slope_v001_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensity_126d_slope_v002_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 126)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensity_63d_slope_v003_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 63)
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_cadence_252d_slope_v004_signal(ncfbus, revenue):
    base = _material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_cadence_504d_slope_v005_signal(ncfbus, revenue):
    base = _material_q(ncfbus, revenue, 0.05).rolling(504, min_periods=252).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_bigcadence_252d_slope_v006_signal(ncfbus, revenue):
    base = _material_q(ncfbus, revenue, 0.15).rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_opscover_252d_slope_v007_signal(ncfbus, ncfo):
    base = _ops_funding(ncfbus, ncfo, 252).clip(upper=10.0)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_opscover_126d_slope_v008_signal(ncfbus, ncfo):
    base = _ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuild_252d_slope_v009_signal(intangibles, revenue):
    base = _goodwill_build(intangibles, revenue, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuild_126d_slope_v010_signal(intangibles, revenue):
    base = _goodwill_build(intangibles, revenue, 126)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwfootprint_252d_slope_v011_signal(intangibles, revenue):
    base = _safe_div(_mean(intangibles, 252), _mean(revenue, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwgrowth_252d_slope_v012_signal(intangibles):
    base = np.log(intangibles.replace(0, np.nan) / intangibles.shift(252).replace(0, np.nan))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakebuild_252d_slope_v013_signal(investments, revenue):
    base = (investments - investments.shift(252)) / _mean(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invflowint_252d_slope_v014_signal(ncfinv, revenue):
    base = _sum((-ncfinv).clip(lower=0), 252) / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invsign_252d_slope_v015_signal(ncfinv):
    base = -_mean(ncfinv, 252) / _mean(ncfinv.abs(), 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqsign_252d_slope_v016_signal(ncfbus):
    base = _acquirer_sign(ncfbus, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqsign_504d_slope_v017_signal(ncfbus):
    base = _acquirer_sign(ncfbus, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_divestint_252d_slope_v018_signal(ncfbus, revenue):
    base = _sum(_divest_in(ncfbus), 252) / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealvscap_252d_slope_v019_signal(ncfbus, marketcap):
    base = _deal_vs_cap(ncfbus, marketcap, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealvscap_504d_slope_v020_signal(ncfbus, marketcap):
    base = _deal_vs_cap(ncfbus, marketcap, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwvscap_252d_slope_v021_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 252), _mean(marketcap, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_selffund_252d_slope_v022_signal(ncfbus, ncfo):
    gap = _sum(ncfo, 252) - _sum(_acq_spend(ncfbus), 252)
    scale = (_sum(ncfo.abs(), 252) + _sum(_acq_spend(ncfbus), 252)).replace(0, np.nan)
    base = gap / scale
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_burnbuy_252d_slope_v023_signal(ncfbus, ncfo):
    both = ((_acq_spend(ncfbus) > 0).astype(float) * (ncfo < 0).astype(float))
    base = both.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwperspend_252d_slope_v024_signal(intangibles, ncfbus):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_acq_spend(ncfbus), 252).replace(0, np.nan)
    base = build / spend
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_totaldeploy_252d_slope_v025_signal(ncfbus, ncfinv, revenue):
    deploy = _sum(_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    base = deploy / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakevsdeal_252d_slope_v026_signal(ncfinv, ncfbus):
    stake = _mean((-ncfinv).clip(lower=0), 252)
    deal = _mean(_acq_spend(ncfbus), 252)
    base = (stake - deal) / (stake + deal).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_pruning_252d_slope_v027_signal(ncfbus):
    pruning = (_mean(ncfbus, 63) > 0).astype(float)
    base = pruning.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensburst_63d_slope_v028_signal(ncfbus, revenue):
    fast = _intensity(ncfbus, revenue, 63)
    slow = _intensity(ncfbus, revenue, 252).replace(0, np.nan)
    base = fast / slow - 1.0
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_peakdeal_252d_slope_v029_signal(ncfbus, revenue):
    si = _safe_div(_acq_spend(ncfbus), _mean(revenue, 21))
    base = si.rolling(252, min_periods=126).max() / _mean(si, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_lumpiness_252d_slope_v030_signal(ncfbus):
    spend = _acq_spend(ncfbus)
    base = spend.rolling(252, min_periods=126).max() / _sum(spend, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealconc_252d_slope_v031_signal(ncfbus):
    spend = _acq_spend(ncfbus).replace(0, np.nan)
    base = _safe_div(_std(spend, 252), _mean(spend, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealskew_252d_slope_v032_signal(ncfbus, revenue):
    si = _safe_div(_acq_spend(ncfbus), _mean(revenue, 21))
    base = si.rolling(252, min_periods=126).skew()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealshare_126d_slope_v033_signal(ncfbus, ncfo):
    spend = _mean(_acq_spend(ncfbus), 126)
    ops = _mean(ncfo.abs(), 126)
    base = spend / (spend + ops).replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwgrowth_504d_slope_v034_signal(intangibles):
    base = np.log(intangibles.replace(0, np.nan) / intangibles.shift(504).replace(0, np.nan))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakevolnorm_252d_slope_v035_signal(investments, revenue):
    base = _safe_div(_std(investments - investments.shift(21), 252), _mean(revenue, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_fundstress_252d_slope_v036_signal(ncfbus, ncfo):
    spend = _sum(_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + _divest_in(ncfbus), 252).replace(0, np.nan)
    base = spend / internal
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealvol_252d_slope_v037_signal(ncfbus, revenue):
    qspend = _safe_div(_acq_spend(ncfbus), _mean(revenue, 63))
    base = _std(qspend, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_busvol_252d_slope_v038_signal(ncfbus):
    base = _safe_div(_std(ncfbus, 252), _mean(ncfbus.abs(), 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwvol_252d_slope_v039_signal(intangibles, revenue):
    qbuild = _safe_div(intangibles - intangibles.shift(63), _mean(revenue, 63))
    base = _std(qbuild, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_cumintens_504d_slope_v040_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuild_504d_slope_v041_signal(intangibles, revenue):
    base = _goodwill_build(intangibles, revenue, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakebuild_504d_slope_v042_signal(investments, revenue):
    base = (investments - investments.shift(504)) / _mean(revenue, 504).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_opscover_504d_slope_v043_signal(ncfbus, ncfo):
    base = _ops_funding(ncfbus, ncfo, 504).clip(upper=10.0)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_deployvscap_252d_slope_v044_signal(ncfbus, ncfinv, marketcap):
    deploy = _sum(_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    base = deploy / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwfootabs_252d_slope_v045_signal(intangibles, revenue):
    base = _safe_div(_mean(intangibles, 126), _mean(revenue, 126))
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_healthyacq_252d_slope_v046_signal(ncfbus, ncfo):
    healthy = ((_acq_spend(ncfbus) > 0) & (ncfo > 0)).astype(float)
    base = healthy.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revvsgw_252d_slope_v047_signal(revenue, intangibles):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    gwg = np.log(_mean(intangibles, 63).replace(0, np.nan) / _mean(intangibles, 63).shift(252).replace(0, np.nan))
    base = revg - gwg
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_inorglift_252d_slope_v048_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    cad = _material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    base = revg * cad
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_rollupsig_252d_slope_v049_signal(ncfbus, revenue):
    intens = _intensity(ncfbus, revenue, 252)
    cad = _material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    base = intens * cad
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_extrollrisk_252d_slope_v050_signal(ncfbus, revenue, ncfo):
    intens = _intensity(ncfbus, revenue, 252)
    cover = _ops_funding(ncfbus, ncfo, 252).clip(0.0, 1.0)
    base = intens * (1.0 - cover)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakefoot_252d_slope_v051_signal(investments, revenue):
    base = _safe_div(_mean(investments, 252), _mean(revenue, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_spendrevlevel_252d_slope_v052_signal(ncfbus, revenue):
    base = _sum(_acq_spend(ncfbus), 252) / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_busturnrev_504d_slope_v053_signal(ncfbus, revenue):
    base = _sum(ncfbus.abs(), 504) / _sum(revenue, 504).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealvscap_126d_slope_v054_signal(ncfbus, marketcap):
    base = _deal_vs_cap(ncfbus, marketcap, 126)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_richbuy_252d_slope_v055_signal(ncfbus, intangibles, marketcap):
    dvc = _deal_vs_cap(ncfbus, marketcap, 252)
    gvc = _safe_div(_mean(intangibles, 252), _mean(marketcap, 252))
    base = dvc * gvc
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_inorgsig_252d_slope_v056_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    intens = _intensity(ncfbus, revenue, 252)
    hi = (intens > intens.rolling(504, min_periods=252).median()).astype(float)
    base = revg * hi
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_organicgw_252d_slope_v057_signal(revenue, intangibles):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    gwg = np.log(_mean(intangibles, 63).replace(0, np.nan) / _mean(intangibles, 63).shift(252).replace(0, np.nan))
    base = revg - 1.5 * gwg
    d = (base - base.shift(126)) / 126.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_divrevlevel_126d_slope_v058_signal(ncfbus, revenue):
    base = _sum(_divest_in(ncfbus), 126) / _sum(revenue, 126).replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_internalfund_252d_slope_v059_signal(ncfbus, ncfo, ncfinv):
    spend = _sum(_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + ncfinv.clip(lower=0), 252)
    base = (internal - spend) / (internal + spend).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwimpair_252d_slope_v060_signal(intangibles, revenue):
    impair = (-(intangibles - intangibles.shift(63))).clip(lower=0)
    base = _sum(impair, 252) / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invintens63_slope_v061_signal(ncfinv, revenue):
    base = _sum((-ncfinv).clip(lower=0), 63) / _sum(revenue, 63).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invdeploycap_252d_slope_v062_signal(ncfinv, marketcap):
    out = _sum((-ncfinv).clip(lower=0), 252)
    base = out / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwcumfoot_504d_slope_v063_signal(intangibles, revenue):
    base = _safe_div(_mean(intangibles, 504), _sum(revenue, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_discipline_252d_slope_v064_signal(ncfbus, ncfo):
    disc = (_acq_spend(ncfbus) <= ncfo).astype(float)
    base = disc.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_footslope_252d_slope_v065_signal(intangibles, revenue):
    base = _safe_div(intangibles, revenue)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revperspend_252d_slope_v066_signal(revenue, ncfbus):
    revgain = (_mean(revenue, 63) - _mean(revenue, 63).shift(252)).clip(lower=0)
    spend = _sum(_acq_spend(ncfbus), 252).replace(0, np.nan)
    base = revgain / spend
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_buildmix_252d_slope_v067_signal(intangibles, investments):
    gwb = (intangibles - intangibles.shift(252)).clip(lower=0)
    stb = (investments - investments.shift(252)).clip(lower=0)
    base = (gwb - stb) / (gwb + stb).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_overpay_252d_slope_v068_signal(intangibles, ncfbus, marketcap):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_acq_spend(ncfbus), 252).replace(0, np.nan)
    base = (build / spend) * _deal_vs_cap(ncfbus, marketcap, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_divintens63_slope_v069_signal(ncfbus, revenue):
    base = _sum(_divest_in(ncfbus), 63) / _sum(revenue, 63).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_netinvest_252d_slope_v070_signal(ncfbus, ncfinv, revenue):
    base = _sum(ncfbus + ncfinv, 252) / _sum(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_deployburden_252d_slope_v071_signal(ncfbus, ncfinv, ncfo):
    deploy = _sum(_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    base = deploy / _sum(ncfo.abs(), 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqturn_252d_slope_v072_signal(revenue, intangibles, investments):
    base = _safe_div(_mean(revenue, 252), _mean(intangibles + investments, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_divestcap_252d_slope_v073_signal(ncfbus, marketcap):
    din = _sum(_divest_in(ncfbus), 252)
    base = din / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakeweight_252d_slope_v074_signal(investments, marketcap):
    base = _safe_div(_mean(investments, 63), _mean(marketcap, 63))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_boltoncad_252d_slope_v075_signal(ncfbus, revenue):
    spend = _acq_spend(ncfbus)
    bolt = ((spend > 0.02 * revenue) & (spend < 0.08 * revenue)).astype(float)
    base = bolt.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensregime_252d_slope_v076_signal(ncfbus, revenue):
    intens = _intensity(ncfbus, revenue, 252)
    base = intens - intens.rolling(504, min_periods=252).median()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensdisp_504d_slope_v077_signal(ncfbus, revenue):
    qi = _intensity(ncfbus, revenue, 63)
    base = _std(qi, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensyoy_252d_slope_v078_signal(ncfbus, revenue):
    intens = _intensity(ncfbus, revenue, 252)
    base = np.log((intens + 0.01) / (intens.shift(252) + 0.01))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuildrank_252d_slope_v079_signal(intangibles, revenue):
    g = _goodwill_build(intangibles, revenue, 252)
    base = _rank(g, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuildovcapb_252d_slope_v080_signal(intangibles, marketcap):
    gwb = (intangibles - intangibles.shift(252)).clip(lower=0)
    capb = (marketcap - marketcap.shift(252)).abs()
    base = gwb / (gwb + capb).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invvol_252d_slope_v081_signal(ncfinv):
    base = _safe_div(_std(ncfinv, 252), _mean(ncfinv.abs(), 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_invsign_504d_slope_v082_signal(ncfinv):
    base = -_mean(ncfinv, 504) / _mean(ncfinv.abs(), 504).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_netflowcap_252d_slope_v083_signal(ncfbus, marketcap):
    base = _sum(ncfbus, 252) / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwcapz_252d_slope_v084_signal(intangibles, marketcap):
    r = _safe_div(intangibles, marketcap)
    base = _z(r, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealcapmom_252d_slope_v085_signal(ncfbus, marketcap):
    dvc = _deal_vs_cap(ncfbus, marketcap, 252)
    base = dvc - dvc.shift(63)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_lagdealrev_252d_slope_v086_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(126).replace(0, np.nan))
    past = _intensity(ncfbus, revenue, 126).shift(126)
    base = revg * (1.0 + past)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revpergw_252d_slope_v087_signal(revenue, intangibles):
    revg = (_mean(revenue, 63) - _mean(revenue, 63).shift(252)).clip(lower=0)
    gwb = (intangibles - intangibles.shift(252)).clip(lower=0).replace(0, np.nan)
    base = revg / gwb
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakevol_252d_slope_v088_signal(investments):
    chg = investments - investments.shift(63)
    base = _safe_div(_std(chg, 252), _mean(investments, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_assetmix_252d_slope_v089_signal(intangibles, investments):
    g = _mean(intangibles, 252)
    s = _mean(investments, 252)
    base = (g - s) / (g + s).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwloadrank_252d_slope_v090_signal(intangibles, marketcap):
    r = _safe_div(_mean(intangibles, 126), _mean(marketcap, 126))
    base = _rank(r, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intspr_126v504_slope_v091_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 126) - _intensity(ncfbus, revenue, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwspr_126v504_slope_v092_signal(intangibles, revenue):
    base = _goodwill_build(intangibles, revenue, 126) - 0.5 * _goodwill_build(intangibles, revenue, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealcapspr_252v504_slope_v093_signal(ncfbus, marketcap):
    base = _deal_vs_cap(ncfbus, marketcap, 252) - 0.5 * _deal_vs_cap(ncfbus, marketcap, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_coverspr_126v504_slope_v094_signal(ncfbus, ncfo):
    s = _ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    l = _ops_funding(ncfbus, ncfo, 504).clip(upper=10.0)
    base = s - l
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_spendpct_504d_slope_v095_signal(ncfbus, revenue):
    si = _safe_div(_acq_spend(ncfbus), _mean(revenue, 21))
    base = _rank(si, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_busskew_252d_slope_v096_signal(ncfbus):
    base = ncfbus.rolling(252, min_periods=126).skew()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_buskurt_252d_slope_v097_signal(ncfbus):
    base = ncfbus.rolling(252, min_periods=126).kurt()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_signsmooth_252d_slope_v098_signal(ncfbus):
    base = _acquirer_sign(ncfbus, 126).ewm(span=126, min_periods=42).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwmomz_252d_slope_v099_signal(intangibles):
    g = np.log(intangibles.replace(0, np.nan)).diff(63)
    base = _z(g, 252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_extreliance_252d_slope_v100_signal(ncfbus, ncfo, ncfinv):
    spend = _sum(_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + ncfinv.clip(lower=0) + _divest_in(ncfbus), 252)
    base = (spend - internal) / (spend + internal).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuildcap_252d_slope_v101_signal(intangibles, marketcap):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    base = build / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_spendvsrevg_252d_slope_v102_signal(ncfbus, revenue):
    spendg = np.log((_mean(_acq_spend(ncfbus), 63) + 1.0) / (_mean(_acq_spend(ncfbus), 63).shift(252) + 1.0))
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    base = spendg - revg
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwcapyoy_252d_slope_v103_signal(intangibles, marketcap):
    r = _safe_div(_mean(intangibles, 21), _mean(marketcap, 21))
    base = r - r.shift(252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_spendgwlag_252d_slope_v104_signal(ncfbus, intangibles, revenue):
    spendt = _safe_div(_sum(_acq_spend(ncfbus), 126), _sum(revenue, 126))
    gwt = _goodwill_build(intangibles, revenue, 126)
    base = spendt - gwt
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_spendmedshare_252d_slope_v105_signal(ncfbus):
    spend = _acq_spend(ncfbus)
    med = spend.rolling(252, min_periods=126).median()
    base = med / _mean(spend, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_coverfail_252d_slope_v106_signal(ncfbus, ncfo):
    short = (_acq_spend(ncfbus) > ncfo.clip(lower=0)).astype(float)
    active = (_acq_spend(ncfbus) > 0).astype(float)
    num = (short * active).rolling(252, min_periods=126).sum()
    den = active.rolling(252, min_periods=126).sum().replace(0, np.nan)
    base = num / den
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqentries_252d_slope_v107_signal(ncfbus, revenue):
    mat = _material_q(ncfbus, revenue, 0.05)
    entries = ((mat == 1) & (mat.shift(63) == 0)).astype(float)
    base = entries.rolling(252, min_periods=126).sum()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_cadstab_504d_slope_v108_signal(ncfbus, revenue):
    base = -_std(_material_q(ncfbus, revenue, 0.05), 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqpersist_252d_slope_v109_signal(ncfbus, revenue):
    mat = _material_q(ncfbus, revenue, 0.05)
    # smooth deal-persistence: EWMA of the indicator weighted by intensity
    base = mat.ewm(span=63, min_periods=21).mean() * (1.0 + _intensity(ncfbus, revenue, 126))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_sizedisp_504d_slope_v110_signal(ncfbus, revenue):
    qsize = _safe_div(_mean(_acq_spend(ncfbus), 63), _mean(revenue, 63))
    base = _safe_div(_std(qsize, 504), _mean(qsize, 504))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_coveryoy_252d_slope_v111_signal(ncfbus, ncfo):
    cov = _ops_funding(ncfbus, ncfo, 252).clip(upper=10.0)
    base = cov - cov.shift(252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_opsdealratio_252d_slope_v112_signal(ncfbus, ncfo):
    spend = _mean(_acq_spend(ncfbus), 252)
    ops = _mean(ncfo.abs(), 252).replace(0, np.nan)
    base = spend / ops
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwdisp504_slope_v113_signal(intangibles, revenue):
    qbuild = _safe_div(intangibles - intangibles.shift(63), _mean(revenue, 63))
    base = _std(qbuild, 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_wavephase_slope_v114_signal(ncfbus):
    agree = (np.sign(_mean(ncfbus, 126)) == np.sign(_mean(ncfbus, 504))).astype(float)
    base = agree.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revgwcorr_252d_slope_v115_signal(revenue, intangibles):
    rg = np.log(revenue.replace(0, np.nan)).diff(21)
    gg = np.log(intangibles.replace(0, np.nan)).diff(21)
    rm = rg - _mean(rg, 252)
    gm = gg - _mean(gg, 252)
    cov = _mean(rm * gm, 252)
    denom = (_std(rg, 252) * _std(gg, 252)).replace(0, np.nan)
    base = cov / denom
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuildmcg_252d_slope_v116_signal(intangibles, marketcap):
    build = (intangibles - intangibles.shift(126)).clip(lower=0)
    capg = (marketcap - marketcap.shift(126)).abs()
    base = build / (build + capg).replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakeaccrev_126d_slope_v117_signal(investments, revenue):
    build = _safe_div(investments - investments.shift(126), _mean(revenue, 126))
    base = build - build.shift(126)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakeleaddeal_slope_v118_signal(ncfinv, ncfbus, revenue):
    stake = _safe_div(_sum((-ncfinv).clip(lower=0), 126), _sum(revenue, 126))
    deal_prior = _safe_div(_sum(_acq_spend(ncfbus), 126), _sum(revenue, 126)).shift(126)
    base = stake - deal_prior
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensrank_252d_slope_v119_signal(ncfbus, revenue):
    base = _rank(_intensity(ncfbus, revenue, 252), 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_drystreak_252d_slope_v120_signal(ncfbus, revenue):
    mat = _material_q(ncfbus, revenue, 0.05)
    fresh = mat.ewm(span=126, min_periods=42).mean()
    base = (1.0 - fresh) * (1.0 + _intensity(ncfbus, revenue, 252))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dirskew2_252d_slope_v121_signal(ncfbus, revenue):
    di = _safe_div(_divest_in(ncfbus), _mean(revenue, 21))
    base = di.rolling(252, min_periods=126).skew()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_divburst_252d_slope_v122_signal(ncfbus, revenue):
    di = _safe_div(_divest_in(ncfbus), _mean(revenue, 21))
    base = di.rolling(252, min_periods=126).max() / _mean(di, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealpersist_252d_slope_v123_signal(ncfbus, revenue):
    qs = _safe_div(_mean(_acq_spend(ncfbus), 63), _mean(revenue, 63))
    cur = qs - _mean(qs, 252)
    lag = qs.shift(63) - _mean(qs.shift(63), 252)
    cov = _mean(cur * lag, 252)
    denom = (_std(qs, 252) * _std(qs.shift(63), 252)).replace(0, np.nan)
    base = cov / denom
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_realisetilt_252d_slope_v124_signal(ncfinv, investments):
    inflow = _sum(ncfinv.clip(lower=0), 252)
    outflow = _sum((-ncfinv).clip(lower=0), 252)
    direction = (inflow - outflow) / (inflow + outflow).replace(0, np.nan)
    base = direction * (1.0 + 0.5 * np.sign(investments - investments.shift(252)))
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_churnrepl_252d_slope_v125_signal(ncfbus, revenue):
    spend = _safe_div(_mean(_acq_spend(ncfbus), 63), _mean(revenue, 63))
    div = _safe_div(_mean(_divest_in(ncfbus), 63), _mean(revenue, 63))
    sm = spend - _mean(spend, 252)
    dm = div - _mean(div, 252)
    cov = _mean(sm * dm, 252)
    denom = (_std(spend, 252) * _std(div, 252)).replace(0, np.nan)
    base = cov / denom
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakeaccel_126d_slope_v126_signal(investments):
    g = np.log(investments.replace(0, np.nan) / investments.shift(126).replace(0, np.nan))
    base = g - g.shift(63)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwaccel_slope_v127_signal(intangibles, revenue):
    g = _goodwill_build(intangibles, revenue, 126)
    base = g - g.shift(126)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwstep_252d_slope_v128_signal(intangibles, revenue):
    qbuild = (intangibles - intangibles.shift(63)).clip(lower=0)
    big = (qbuild > (0.10 * _mean(revenue, 63))).astype(float)
    base = big.rolling(252, min_periods=126).mean()
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_signflip_252d_slope_v129_signal(ncfbus):
    s = _acquirer_sign(ncfbus, 252)
    base = s - s.shift(252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revgcad_252d_slope_v130_signal(revenue, ncfbus):
    g1 = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    cad = _material_q(ncfbus, revenue, 0.15).rolling(252, min_periods=126).mean()
    base = g1 * cad
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revaccel_126d_slope_v131_signal(revenue, ncfbus):
    rl = np.log(revenue.replace(0, np.nan))
    g = rl - rl.shift(126)
    acc = g - g.shift(126)
    base = acc * (1.0 + _intensity(ncfbus, revenue, 252))
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_revperdeal504_slope_v132_signal(revenue, ncfbus):
    rev_gain = (_mean(revenue, 63) - _mean(revenue, 63).shift(504)).clip(lower=0)
    spend = _sum(_acq_spend(ncfbus), 504).replace(0, np.nan)
    base = rev_gain / spend
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intenstanh_126d_slope_v133_signal(ncfbus, revenue):
    intens = _intensity(ncfbus, revenue, 126)
    base = np.tanh(8.0 * (intens - intens.shift(63)))
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stockdeal_252d_slope_v134_signal(intangibles, ncfbus, revenue):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_acq_spend(ncfbus), 252)
    base = (build - spend) / _mean(revenue, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_codeploy_252d_slope_v135_signal(ncfinv, ncfbus):
    stake = (-ncfinv).clip(lower=0)
    deal = _acq_spend(ncfbus)
    sm = stake - _mean(stake, 252)
    dm = deal - _mean(deal, 252)
    cov = _mean(sm * dm, 252)
    denom = (_std(stake, 252) * _std(deal, 252)).replace(0, np.nan)
    base = cov / denom
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_extintens_126d_slope_v136_signal(ncfbus, revenue, ncfo):
    intens = _intensity(ncfbus, revenue, 126)
    burnfrac = (ncfo < 0).astype(float).rolling(126, min_periods=63).mean()
    base = intens * burnfrac
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_impulse_63d_slope_v137_signal(ncfbus, revenue):
    si = _safe_div(_acq_spend(ncfbus), _mean(revenue, 63))
    base = si - si.ewm(span=126, min_periods=42).mean()
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_impulsez_63d_slope_v138_signal(ncfbus, revenue):
    si = _safe_div(_mean(_acq_spend(ncfbus), 63), _mean(revenue, 63))
    base = (si - si.ewm(span=252, min_periods=63).mean()) / _std(si, 252).replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwmomgap_126d_slope_v139_signal(intangibles, revenue):
    gwm = np.log(_mean(intangibles, 21).replace(0, np.nan) / _mean(intangibles, 21).shift(126).replace(0, np.nan))
    revm = np.log(_mean(revenue, 21).replace(0, np.nan) / _mean(revenue, 21).shift(126).replace(0, np.nan))
    base = gwm - revm
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensacc_slope_v140_signal(ncfbus, revenue):
    intens = _intensity(ncfbus, revenue, 126)
    g = intens - intens.shift(63)
    base = g - g.shift(63)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_acqassetlevel_252d_slope_v141_signal(revenue, intangibles, investments):
    base = _safe_div(_mean(revenue, 126), _mean(intangibles + investments, 126))
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwdisp_126d_slope_v142_signal(intangibles, revenue):
    g = _goodwill_build(intangibles, revenue, 126)
    base = g - g.ewm(span=252, min_periods=63).mean()
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_postacc_126d_slope_v143_signal(revenue, ncfbus):
    rl = np.log(revenue.replace(0, np.nan))
    g = rl.diff(63)
    acc = g - g.shift(63)
    cad = _material_q(ncfbus, revenue, 0.05).rolling(126, min_periods=63).mean()
    base = acc * (0.5 + cad)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_gwbuild63_slope_v144_signal(intangibles, revenue):
    base = _goodwill_build(intangibles, revenue, 63)
    d = (base - base.shift(21)) / 21.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_covertrend_126d_slope_v145_signal(ncfbus, ncfo):
    cov = _ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    base = cov - cov.shift(63)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_intensspr252v126_slope_v146_signal(ncfbus, revenue):
    base = _intensity(ncfbus, revenue, 252) - _intensity(ncfbus, revenue, 126)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakez_126d_slope_v147_signal(investments, revenue):
    build = (investments - investments.shift(126)) / _mean(revenue, 126).replace(0, np.nan)
    base = _z(build, 252)
    d = (base - base.shift(42)) / 42.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_dealcaprank_252d_slope_v148_signal(ncfbus, marketcap):
    base = _rank(_deal_vs_cap(ncfbus, marketcap, 252), 504)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_stakevscap_252d_slope_v149_signal(investments, marketcap):
    base = _mean(investments, 252) / _mean(marketcap, 252).replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


def f47ma_f47_ma_rollup_acquisition_buftrend_252d_slope_v150_signal(ncfo, ncfbus, marketcap):
    buf = _safe_div(_sum(ncfo, 252) - _sum(_acq_spend(ncfbus), 252), _mean(marketcap, 252))
    base = buf - buf.shift(252)
    d = (base - base.shift(63)) / 63.0
    return d.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ma_f47_ma_rollup_acquisition_intensity_252d_slope_v001_signal,
    f47ma_f47_ma_rollup_acquisition_intensity_126d_slope_v002_signal,
    f47ma_f47_ma_rollup_acquisition_intensity_63d_slope_v003_signal,
    f47ma_f47_ma_rollup_acquisition_cadence_252d_slope_v004_signal,
    f47ma_f47_ma_rollup_acquisition_cadence_504d_slope_v005_signal,
    f47ma_f47_ma_rollup_acquisition_bigcadence_252d_slope_v006_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_252d_slope_v007_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_126d_slope_v008_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_252d_slope_v009_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_126d_slope_v010_signal,
    f47ma_f47_ma_rollup_acquisition_gwfootprint_252d_slope_v011_signal,
    f47ma_f47_ma_rollup_acquisition_gwgrowth_252d_slope_v012_signal,
    f47ma_f47_ma_rollup_acquisition_stakebuild_252d_slope_v013_signal,
    f47ma_f47_ma_rollup_acquisition_invflowint_252d_slope_v014_signal,
    f47ma_f47_ma_rollup_acquisition_invsign_252d_slope_v015_signal,
    f47ma_f47_ma_rollup_acquisition_acqsign_252d_slope_v016_signal,
    f47ma_f47_ma_rollup_acquisition_acqsign_504d_slope_v017_signal,
    f47ma_f47_ma_rollup_acquisition_divestint_252d_slope_v018_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_252d_slope_v019_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_504d_slope_v020_signal,
    f47ma_f47_ma_rollup_acquisition_gwvscap_252d_slope_v021_signal,
    f47ma_f47_ma_rollup_acquisition_selffund_252d_slope_v022_signal,
    f47ma_f47_ma_rollup_acquisition_burnbuy_252d_slope_v023_signal,
    f47ma_f47_ma_rollup_acquisition_gwperspend_252d_slope_v024_signal,
    f47ma_f47_ma_rollup_acquisition_totaldeploy_252d_slope_v025_signal,
    f47ma_f47_ma_rollup_acquisition_stakevsdeal_252d_slope_v026_signal,
    f47ma_f47_ma_rollup_acquisition_pruning_252d_slope_v027_signal,
    f47ma_f47_ma_rollup_acquisition_intensburst_63d_slope_v028_signal,
    f47ma_f47_ma_rollup_acquisition_peakdeal_252d_slope_v029_signal,
    f47ma_f47_ma_rollup_acquisition_lumpiness_252d_slope_v030_signal,
    f47ma_f47_ma_rollup_acquisition_dealconc_252d_slope_v031_signal,
    f47ma_f47_ma_rollup_acquisition_dealskew_252d_slope_v032_signal,
    f47ma_f47_ma_rollup_acquisition_dealshare_126d_slope_v033_signal,
    f47ma_f47_ma_rollup_acquisition_gwgrowth_504d_slope_v034_signal,
    f47ma_f47_ma_rollup_acquisition_stakevolnorm_252d_slope_v035_signal,
    f47ma_f47_ma_rollup_acquisition_fundstress_252d_slope_v036_signal,
    f47ma_f47_ma_rollup_acquisition_dealvol_252d_slope_v037_signal,
    f47ma_f47_ma_rollup_acquisition_busvol_252d_slope_v038_signal,
    f47ma_f47_ma_rollup_acquisition_gwvol_252d_slope_v039_signal,
    f47ma_f47_ma_rollup_acquisition_cumintens_504d_slope_v040_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_504d_slope_v041_signal,
    f47ma_f47_ma_rollup_acquisition_stakebuild_504d_slope_v042_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_504d_slope_v043_signal,
    f47ma_f47_ma_rollup_acquisition_deployvscap_252d_slope_v044_signal,
    f47ma_f47_ma_rollup_acquisition_gwfootabs_252d_slope_v045_signal,
    f47ma_f47_ma_rollup_acquisition_healthyacq_252d_slope_v046_signal,
    f47ma_f47_ma_rollup_acquisition_revvsgw_252d_slope_v047_signal,
    f47ma_f47_ma_rollup_acquisition_inorglift_252d_slope_v048_signal,
    f47ma_f47_ma_rollup_acquisition_rollupsig_252d_slope_v049_signal,
    f47ma_f47_ma_rollup_acquisition_extrollrisk_252d_slope_v050_signal,
    f47ma_f47_ma_rollup_acquisition_stakefoot_252d_slope_v051_signal,
    f47ma_f47_ma_rollup_acquisition_spendrevlevel_252d_slope_v052_signal,
    f47ma_f47_ma_rollup_acquisition_busturnrev_504d_slope_v053_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_126d_slope_v054_signal,
    f47ma_f47_ma_rollup_acquisition_richbuy_252d_slope_v055_signal,
    f47ma_f47_ma_rollup_acquisition_inorgsig_252d_slope_v056_signal,
    f47ma_f47_ma_rollup_acquisition_organicgw_252d_slope_v057_signal,
    f47ma_f47_ma_rollup_acquisition_divrevlevel_126d_slope_v058_signal,
    f47ma_f47_ma_rollup_acquisition_internalfund_252d_slope_v059_signal,
    f47ma_f47_ma_rollup_acquisition_gwimpair_252d_slope_v060_signal,
    f47ma_f47_ma_rollup_acquisition_invintens63_slope_v061_signal,
    f47ma_f47_ma_rollup_acquisition_invdeploycap_252d_slope_v062_signal,
    f47ma_f47_ma_rollup_acquisition_gwcumfoot_504d_slope_v063_signal,
    f47ma_f47_ma_rollup_acquisition_discipline_252d_slope_v064_signal,
    f47ma_f47_ma_rollup_acquisition_footslope_252d_slope_v065_signal,
    f47ma_f47_ma_rollup_acquisition_revperspend_252d_slope_v066_signal,
    f47ma_f47_ma_rollup_acquisition_buildmix_252d_slope_v067_signal,
    f47ma_f47_ma_rollup_acquisition_overpay_252d_slope_v068_signal,
    f47ma_f47_ma_rollup_acquisition_divintens63_slope_v069_signal,
    f47ma_f47_ma_rollup_acquisition_netinvest_252d_slope_v070_signal,
    f47ma_f47_ma_rollup_acquisition_deployburden_252d_slope_v071_signal,
    f47ma_f47_ma_rollup_acquisition_acqturn_252d_slope_v072_signal,
    f47ma_f47_ma_rollup_acquisition_divestcap_252d_slope_v073_signal,
    f47ma_f47_ma_rollup_acquisition_stakeweight_252d_slope_v074_signal,
    f47ma_f47_ma_rollup_acquisition_boltoncad_252d_slope_v075_signal,
    f47ma_f47_ma_rollup_acquisition_intensregime_252d_slope_v076_signal,
    f47ma_f47_ma_rollup_acquisition_intensdisp_504d_slope_v077_signal,
    f47ma_f47_ma_rollup_acquisition_intensyoy_252d_slope_v078_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildrank_252d_slope_v079_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildovcapb_252d_slope_v080_signal,
    f47ma_f47_ma_rollup_acquisition_invvol_252d_slope_v081_signal,
    f47ma_f47_ma_rollup_acquisition_invsign_504d_slope_v082_signal,
    f47ma_f47_ma_rollup_acquisition_netflowcap_252d_slope_v083_signal,
    f47ma_f47_ma_rollup_acquisition_gwcapz_252d_slope_v084_signal,
    f47ma_f47_ma_rollup_acquisition_dealcapmom_252d_slope_v085_signal,
    f47ma_f47_ma_rollup_acquisition_lagdealrev_252d_slope_v086_signal,
    f47ma_f47_ma_rollup_acquisition_revpergw_252d_slope_v087_signal,
    f47ma_f47_ma_rollup_acquisition_stakevol_252d_slope_v088_signal,
    f47ma_f47_ma_rollup_acquisition_assetmix_252d_slope_v089_signal,
    f47ma_f47_ma_rollup_acquisition_gwloadrank_252d_slope_v090_signal,
    f47ma_f47_ma_rollup_acquisition_intspr_126v504_slope_v091_signal,
    f47ma_f47_ma_rollup_acquisition_gwspr_126v504_slope_v092_signal,
    f47ma_f47_ma_rollup_acquisition_dealcapspr_252v504_slope_v093_signal,
    f47ma_f47_ma_rollup_acquisition_coverspr_126v504_slope_v094_signal,
    f47ma_f47_ma_rollup_acquisition_spendpct_504d_slope_v095_signal,
    f47ma_f47_ma_rollup_acquisition_busskew_252d_slope_v096_signal,
    f47ma_f47_ma_rollup_acquisition_buskurt_252d_slope_v097_signal,
    f47ma_f47_ma_rollup_acquisition_signsmooth_252d_slope_v098_signal,
    f47ma_f47_ma_rollup_acquisition_gwmomz_252d_slope_v099_signal,
    f47ma_f47_ma_rollup_acquisition_extreliance_252d_slope_v100_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildcap_252d_slope_v101_signal,
    f47ma_f47_ma_rollup_acquisition_spendvsrevg_252d_slope_v102_signal,
    f47ma_f47_ma_rollup_acquisition_gwcapyoy_252d_slope_v103_signal,
    f47ma_f47_ma_rollup_acquisition_spendgwlag_252d_slope_v104_signal,
    f47ma_f47_ma_rollup_acquisition_spendmedshare_252d_slope_v105_signal,
    f47ma_f47_ma_rollup_acquisition_coverfail_252d_slope_v106_signal,
    f47ma_f47_ma_rollup_acquisition_acqentries_252d_slope_v107_signal,
    f47ma_f47_ma_rollup_acquisition_cadstab_504d_slope_v108_signal,
    f47ma_f47_ma_rollup_acquisition_acqpersist_252d_slope_v109_signal,
    f47ma_f47_ma_rollup_acquisition_sizedisp_504d_slope_v110_signal,
    f47ma_f47_ma_rollup_acquisition_coveryoy_252d_slope_v111_signal,
    f47ma_f47_ma_rollup_acquisition_opsdealratio_252d_slope_v112_signal,
    f47ma_f47_ma_rollup_acquisition_gwdisp504_slope_v113_signal,
    f47ma_f47_ma_rollup_acquisition_wavephase_slope_v114_signal,
    f47ma_f47_ma_rollup_acquisition_revgwcorr_252d_slope_v115_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildmcg_252d_slope_v116_signal,
    f47ma_f47_ma_rollup_acquisition_stakeaccrev_126d_slope_v117_signal,
    f47ma_f47_ma_rollup_acquisition_stakeleaddeal_slope_v118_signal,
    f47ma_f47_ma_rollup_acquisition_intensrank_252d_slope_v119_signal,
    f47ma_f47_ma_rollup_acquisition_drystreak_252d_slope_v120_signal,
    f47ma_f47_ma_rollup_acquisition_dirskew2_252d_slope_v121_signal,
    f47ma_f47_ma_rollup_acquisition_divburst_252d_slope_v122_signal,
    f47ma_f47_ma_rollup_acquisition_dealpersist_252d_slope_v123_signal,
    f47ma_f47_ma_rollup_acquisition_realisetilt_252d_slope_v124_signal,
    f47ma_f47_ma_rollup_acquisition_churnrepl_252d_slope_v125_signal,
    f47ma_f47_ma_rollup_acquisition_stakeaccel_126d_slope_v126_signal,
    f47ma_f47_ma_rollup_acquisition_gwaccel_slope_v127_signal,
    f47ma_f47_ma_rollup_acquisition_gwstep_252d_slope_v128_signal,
    f47ma_f47_ma_rollup_acquisition_signflip_252d_slope_v129_signal,
    f47ma_f47_ma_rollup_acquisition_revgcad_252d_slope_v130_signal,
    f47ma_f47_ma_rollup_acquisition_revaccel_126d_slope_v131_signal,
    f47ma_f47_ma_rollup_acquisition_revperdeal504_slope_v132_signal,
    f47ma_f47_ma_rollup_acquisition_intenstanh_126d_slope_v133_signal,
    f47ma_f47_ma_rollup_acquisition_stockdeal_252d_slope_v134_signal,
    f47ma_f47_ma_rollup_acquisition_codeploy_252d_slope_v135_signal,
    f47ma_f47_ma_rollup_acquisition_extintens_126d_slope_v136_signal,
    f47ma_f47_ma_rollup_acquisition_impulse_63d_slope_v137_signal,
    f47ma_f47_ma_rollup_acquisition_impulsez_63d_slope_v138_signal,
    f47ma_f47_ma_rollup_acquisition_gwmomgap_126d_slope_v139_signal,
    f47ma_f47_ma_rollup_acquisition_intensacc_slope_v140_signal,
    f47ma_f47_ma_rollup_acquisition_acqassetlevel_252d_slope_v141_signal,
    f47ma_f47_ma_rollup_acquisition_gwdisp_126d_slope_v142_signal,
    f47ma_f47_ma_rollup_acquisition_postacc_126d_slope_v143_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild63_slope_v144_signal,
    f47ma_f47_ma_rollup_acquisition_covertrend_126d_slope_v145_signal,
    f47ma_f47_ma_rollup_acquisition_intensspr252v126_slope_v146_signal,
    f47ma_f47_ma_rollup_acquisition_stakez_126d_slope_v147_signal,
    f47ma_f47_ma_rollup_acquisition_dealcaprank_252d_slope_v148_signal,
    f47ma_f47_ma_rollup_acquisition_stakevscap_252d_slope_v149_signal,
    f47ma_f47_ma_rollup_acquisition_buftrend_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_MA_ROLLUP_ACQUISITION_REGISTRY_2ND_001_150 = REGISTRY


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _signed(seed, base, phase, amp, period):
        raw = _fund(seed, base=base, drift=0.0, vol=0.08, allow_neg=True)
        centered = raw - raw.rolling(252, min_periods=1).mean()
        gn = np.random.default_rng(seed + 9000)
        cyc = amp * base * 0.4 * np.sin(np.arange(n) / period * 2 * np.pi + phase)
        jitter = gn.normal(0.0, base * 0.12, n)
        return centered + pd.Series(cyc) + pd.Series(jitter)

    ncfbus = _signed(201, 6e7, 0.0, 1.0, 73.0).rename("ncfbus")
    ncfinv = _signed(202, 5e7, 1.3, 1.1, 91.0).rename("ncfinv")
    ncfo = _signed(203, 8e7, 2.1, 0.9, 67.0).rename("ncfo")

    revenue = _fund(204, base=1.5e8, drift=0.030, vol=0.07).rename("revenue")
    intangibles = _fund(205, base=4.0e8, drift=0.040, vol=0.10).rename("intangibles")
    investments = _fund(206, base=2.0e8, drift=0.025, vol=0.11).rename("investments")
    marketcap = _fund(207, base=2.0e9, drift=0.020, vol=0.09).rename("marketcap")

    cols = {"ncfbus": ncfbus, "ncfinv": ncfinv, "ncfo": ncfo,
            "revenue": revenue, "intangibles": intangibles,
            "investments": investments, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
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

    print("OK f47_ma_rollup_acquisition_2nd_derivatives_001_150_claude: %d features pass" % n_features)
