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


def _f25_rnd_rev(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f25_rnd_assets(rnd, assets):
    return rnd / assets.replace(0, np.nan)


def _f25_capex_rev(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f25_capex_assets(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f25_reinvest_rev(rnd, capex, revenue):
    return (rnd + capex) / revenue.replace(0, np.nan)


def _f25_reinvest_assets(rnd, capex, assets):
    return (rnd + capex) / assets.replace(0, np.nan)


def _f25_sbc_rev(sbcomp, revenue):
    return sbcomp / revenue.replace(0, np.nan)


def _f25_sbc_rnd(sbcomp, rnd):
    return sbcomp / rnd.replace(0, np.nan)


def _f25_sbc_capex(sbcomp, capex):
    return sbcomp / capex.replace(0, np.nan)


def _f25_sbc_reinvest(sbcomp, rnd, capex):
    return sbcomp / (rnd + capex).replace(0, np.nan)


def _f25_sbc_assets(sbcomp, assets):
    return sbcomp / assets.replace(0, np.nan)


def _f25_rnd_capex(rnd, capex):
    return rnd / capex.replace(0, np.nan)


def _f25_rnd_mix(rnd, capex):
    return rnd / (rnd + capex).replace(0, np.nan)


def _f25_reinv_per_sbc(rnd, capex, sbcomp):
    return (rnd + capex) / sbcomp.replace(0, np.nan)


def _f25_intensbal(rnd, revenue, capex, assets):
    return _f25_rnd_rev(rnd, revenue) / _f25_capex_assets(capex, assets).replace(0, np.nan)


def f25rd_f25_content_rd_intensity_rndrev_63d_rawslope_v001_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_126d_nrmslope_v002_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_252d_zprslope_v003_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_189d_emaslope_v004_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_84d_logslope_v005_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_378d_rnkslope_v006_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_105d_ratslope_v007_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_315d_ctrslope_v008_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_63d_rawslope_v009_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_126d_nrmslope_v010_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_252d_zprslope_v011_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_189d_emaslope_v012_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_84d_logslope_v013_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_378d_rnkslope_v014_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_105d_ratslope_v015_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_315d_ctrslope_v016_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_63d_rawslope_v017_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_126d_nrmslope_v018_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_252d_zprslope_v019_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_189d_emaslope_v020_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_378d_rnkslope_v021_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_105d_ratslope_v022_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_315d_ctrslope_v023_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_63d_rawslope_v024_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_126d_nrmslope_v025_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_252d_zprslope_v026_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_189d_emaslope_v027_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_84d_logslope_v028_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_378d_rnkslope_v029_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_105d_ratslope_v030_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_315d_ctrslope_v031_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_63d_rawslope_v032_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_126d_nrmslope_v033_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_252d_zprslope_v034_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_189d_emaslope_v035_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_105d_ratslope_v036_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_315d_ctrslope_v037_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_63d_rawslope_v038_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_126d_nrmslope_v039_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_252d_zprslope_v040_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_189d_emaslope_v041_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_84d_logslope_v042_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_378d_rnkslope_v043_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_105d_ratslope_v044_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_315d_ctrslope_v045_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_63d_rawslope_v046_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_126d_nrmslope_v047_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_252d_zprslope_v048_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_189d_emaslope_v049_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_84d_logslope_v050_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_378d_rnkslope_v051_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_105d_ratslope_v052_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrev_315d_ctrslope_v053_signal(sbcomp, revenue):
    base = _f25_sbc_rev(sbcomp, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_63d_rawslope_v054_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_126d_nrmslope_v055_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_252d_zprslope_v056_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_189d_emaslope_v057_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_84d_logslope_v058_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_378d_rnkslope_v059_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_105d_ratslope_v060_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcrnd_315d_ctrslope_v061_signal(sbcomp, rnd):
    base = _f25_sbc_rnd(sbcomp, rnd)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_63d_rawslope_v062_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_126d_nrmslope_v063_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_252d_zprslope_v064_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_189d_emaslope_v065_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_84d_logslope_v066_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_378d_rnkslope_v067_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_105d_ratslope_v068_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbccapex_315d_ctrslope_v069_signal(sbcomp, capex):
    base = _f25_sbc_capex(sbcomp, capex)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_63d_rawslope_v070_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_126d_nrmslope_v071_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_252d_zprslope_v072_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_189d_emaslope_v073_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_84d_logslope_v074_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_378d_rnkslope_v075_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_105d_ratslope_v076_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcreinv_315d_ctrslope_v077_signal(sbcomp, rnd, capex):
    base = _f25_sbc_reinvest(sbcomp, rnd, capex)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_63d_rawslope_v078_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_126d_nrmslope_v079_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_252d_zprslope_v080_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_189d_emaslope_v081_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_84d_logslope_v082_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_378d_rnkslope_v083_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_105d_ratslope_v084_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcassets_315d_ctrslope_v085_signal(sbcomp, assets):
    base = _f25_sbc_assets(sbcomp, assets)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_63d_rawslope_v086_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_126d_nrmslope_v087_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_252d_zprslope_v088_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_189d_emaslope_v089_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_84d_logslope_v090_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_378d_rnkslope_v091_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_105d_ratslope_v092_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmix_315d_ctrslope_v093_signal(rnd, capex):
    base = _f25_rnd_mix(rnd, capex)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_63d_rawslope_v094_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_126d_nrmslope_v095_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_252d_zprslope_v096_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_189d_emaslope_v097_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_378d_rnkslope_v098_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_intensbal_315d_ctrslope_v099_signal(rnd, revenue, capex, assets):
    base = _f25_intensbal(rnd, revenue, capex, assets)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmcapexrev_126d_nrmslope_v100_signal(rnd, capex, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmcapexrev_84d_logslope_v101_signal(rnd, capex, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_capex_rev(capex, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmcapexrev_105d_ratslope_v102_signal(rnd, capex, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmsbcrev_126d_nrmslope_v103_signal(rnd, sbcomp, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmsbcrev_84d_logslope_v104_signal(rnd, sbcomp, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_sbc_rev(sbcomp, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndmsbcrev_105d_ratslope_v105_signal(rnd, sbcomp, revenue):
    base = _f25_rnd_rev(rnd, revenue) - _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_63d_rawslope_v106_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_126d_nrmslope_v107_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_252d_zprslope_v108_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_189d_emaslope_v109_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_378d_rnkslope_v110_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_105d_ratslope_v111_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndsbcload_315d_ctrslope_v112_signal(rnd, revenue, sbcomp):
    base = _f25_rnd_rev(rnd, revenue) + _f25_sbc_rev(sbcomp, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_63d_rawslope_v113_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_126d_nrmslope_v114_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_252d_zprslope_v115_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = _z(base, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_189d_emaslope_v116_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_84d_logslope_v117_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_378d_rnkslope_v118_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(378) / float(378)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_105d_ratslope_v119_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndglog_315d_ctrslope_v120_signal(rnd):
    base = np.log(rnd.clip(lower=1e-12))
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(315) / float(315)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcgcapexspread_126d_nrmslope_v121_signal(sbcomp, capex, assets):
    base = _f25_sbc_assets(sbcomp, assets) - _f25_capex_assets(capex, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcgcapexspread_84d_logslope_v122_signal(sbcomp, capex, assets):
    base = _f25_sbc_assets(sbcomp, assets) - _f25_capex_assets(capex, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_sbcgcapexspread_105d_ratslope_v123_signal(sbcomp, capex, assets):
    base = _f25_sbc_assets(sbcomp, assets) - _f25_capex_assets(capex, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_42d_rawslope_v124_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_210d_nrmslope_v125_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(210) / float(210)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_126d_emaslope_v126_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_168d_logslope_v127_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_252d_rnkslope_v128_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_63d_ratslope_v129_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndrev_189d_ctrslope_v130_signal(rnd, revenue):
    base = _f25_rnd_rev(rnd, revenue)
    base = base - base.rolling(252, min_periods=63).median()
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_42d_rawslope_v131_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_210d_nrmslope_v132_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(210) / float(210)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_168d_logslope_v133_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_rndassets_63d_ratslope_v134_signal(rnd, assets):
    base = _f25_rnd_assets(rnd, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_42d_rawslope_v135_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_210d_nrmslope_v136_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(210) / float(210)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_504d_zprslope_v137_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = _z(base, 252)
    d = base.diff(504) / float(504)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_168d_logslope_v138_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexrev_63d_ratslope_v139_signal(capex, revenue):
    base = _f25_capex_rev(capex, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_42d_rawslope_v140_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_210d_nrmslope_v141_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(210) / float(210)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_126d_emaslope_v142_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_168d_logslope_v143_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_capexassets_63d_ratslope_v144_signal(capex, assets):
    base = _f25_capex_assets(capex, assets)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_210d_nrmslope_v145_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base / _mean(base, 252).replace(0, np.nan)
    d = base.diff(210) / float(210)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_504d_zprslope_v146_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = _z(base, 252)
    d = base.diff(504) / float(504)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_126d_emaslope_v147_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base - base.ewm(span=189, min_periods=63).mean()
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_168d_logslope_v148_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = np.log(base.clip(lower=1e-12))
    d = base.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvrev_63d_ratslope_v149_signal(rnd, capex, revenue):
    base = _f25_reinvest_rev(rnd, capex, revenue)
    base = base / _mean(base, 126).replace(0, np.nan) - 1.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f25rd_f25_content_rd_intensity_reinvassets_42d_rawslope_v150_signal(rnd, capex, assets):
    base = _f25_reinvest_assets(rnd, capex, assets)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f25rd_f25_content_rd_intensity_rndrev_63d_rawslope_v001_signal,
    f25rd_f25_content_rd_intensity_rndrev_126d_nrmslope_v002_signal,
    f25rd_f25_content_rd_intensity_rndrev_252d_zprslope_v003_signal,
    f25rd_f25_content_rd_intensity_rndrev_189d_emaslope_v004_signal,
    f25rd_f25_content_rd_intensity_rndrev_84d_logslope_v005_signal,
    f25rd_f25_content_rd_intensity_rndrev_378d_rnkslope_v006_signal,
    f25rd_f25_content_rd_intensity_rndrev_105d_ratslope_v007_signal,
    f25rd_f25_content_rd_intensity_rndrev_315d_ctrslope_v008_signal,
    f25rd_f25_content_rd_intensity_rndassets_63d_rawslope_v009_signal,
    f25rd_f25_content_rd_intensity_rndassets_126d_nrmslope_v010_signal,
    f25rd_f25_content_rd_intensity_rndassets_252d_zprslope_v011_signal,
    f25rd_f25_content_rd_intensity_rndassets_189d_emaslope_v012_signal,
    f25rd_f25_content_rd_intensity_rndassets_84d_logslope_v013_signal,
    f25rd_f25_content_rd_intensity_rndassets_378d_rnkslope_v014_signal,
    f25rd_f25_content_rd_intensity_rndassets_105d_ratslope_v015_signal,
    f25rd_f25_content_rd_intensity_rndassets_315d_ctrslope_v016_signal,
    f25rd_f25_content_rd_intensity_capexrev_63d_rawslope_v017_signal,
    f25rd_f25_content_rd_intensity_capexrev_126d_nrmslope_v018_signal,
    f25rd_f25_content_rd_intensity_capexrev_252d_zprslope_v019_signal,
    f25rd_f25_content_rd_intensity_capexrev_189d_emaslope_v020_signal,
    f25rd_f25_content_rd_intensity_capexrev_378d_rnkslope_v021_signal,
    f25rd_f25_content_rd_intensity_capexrev_105d_ratslope_v022_signal,
    f25rd_f25_content_rd_intensity_capexrev_315d_ctrslope_v023_signal,
    f25rd_f25_content_rd_intensity_capexassets_63d_rawslope_v024_signal,
    f25rd_f25_content_rd_intensity_capexassets_126d_nrmslope_v025_signal,
    f25rd_f25_content_rd_intensity_capexassets_252d_zprslope_v026_signal,
    f25rd_f25_content_rd_intensity_capexassets_189d_emaslope_v027_signal,
    f25rd_f25_content_rd_intensity_capexassets_84d_logslope_v028_signal,
    f25rd_f25_content_rd_intensity_capexassets_378d_rnkslope_v029_signal,
    f25rd_f25_content_rd_intensity_capexassets_105d_ratslope_v030_signal,
    f25rd_f25_content_rd_intensity_capexassets_315d_ctrslope_v031_signal,
    f25rd_f25_content_rd_intensity_reinvrev_63d_rawslope_v032_signal,
    f25rd_f25_content_rd_intensity_reinvrev_126d_nrmslope_v033_signal,
    f25rd_f25_content_rd_intensity_reinvrev_252d_zprslope_v034_signal,
    f25rd_f25_content_rd_intensity_reinvrev_189d_emaslope_v035_signal,
    f25rd_f25_content_rd_intensity_reinvrev_105d_ratslope_v036_signal,
    f25rd_f25_content_rd_intensity_reinvrev_315d_ctrslope_v037_signal,
    f25rd_f25_content_rd_intensity_reinvassets_63d_rawslope_v038_signal,
    f25rd_f25_content_rd_intensity_reinvassets_126d_nrmslope_v039_signal,
    f25rd_f25_content_rd_intensity_reinvassets_252d_zprslope_v040_signal,
    f25rd_f25_content_rd_intensity_reinvassets_189d_emaslope_v041_signal,
    f25rd_f25_content_rd_intensity_reinvassets_84d_logslope_v042_signal,
    f25rd_f25_content_rd_intensity_reinvassets_378d_rnkslope_v043_signal,
    f25rd_f25_content_rd_intensity_reinvassets_105d_ratslope_v044_signal,
    f25rd_f25_content_rd_intensity_reinvassets_315d_ctrslope_v045_signal,
    f25rd_f25_content_rd_intensity_sbcrev_63d_rawslope_v046_signal,
    f25rd_f25_content_rd_intensity_sbcrev_126d_nrmslope_v047_signal,
    f25rd_f25_content_rd_intensity_sbcrev_252d_zprslope_v048_signal,
    f25rd_f25_content_rd_intensity_sbcrev_189d_emaslope_v049_signal,
    f25rd_f25_content_rd_intensity_sbcrev_84d_logslope_v050_signal,
    f25rd_f25_content_rd_intensity_sbcrev_378d_rnkslope_v051_signal,
    f25rd_f25_content_rd_intensity_sbcrev_105d_ratslope_v052_signal,
    f25rd_f25_content_rd_intensity_sbcrev_315d_ctrslope_v053_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_63d_rawslope_v054_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_126d_nrmslope_v055_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_252d_zprslope_v056_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_189d_emaslope_v057_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_84d_logslope_v058_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_378d_rnkslope_v059_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_105d_ratslope_v060_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_315d_ctrslope_v061_signal,
    f25rd_f25_content_rd_intensity_sbccapex_63d_rawslope_v062_signal,
    f25rd_f25_content_rd_intensity_sbccapex_126d_nrmslope_v063_signal,
    f25rd_f25_content_rd_intensity_sbccapex_252d_zprslope_v064_signal,
    f25rd_f25_content_rd_intensity_sbccapex_189d_emaslope_v065_signal,
    f25rd_f25_content_rd_intensity_sbccapex_84d_logslope_v066_signal,
    f25rd_f25_content_rd_intensity_sbccapex_378d_rnkslope_v067_signal,
    f25rd_f25_content_rd_intensity_sbccapex_105d_ratslope_v068_signal,
    f25rd_f25_content_rd_intensity_sbccapex_315d_ctrslope_v069_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_63d_rawslope_v070_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_126d_nrmslope_v071_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_252d_zprslope_v072_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_189d_emaslope_v073_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_84d_logslope_v074_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_378d_rnkslope_v075_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_105d_ratslope_v076_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_315d_ctrslope_v077_signal,
    f25rd_f25_content_rd_intensity_sbcassets_63d_rawslope_v078_signal,
    f25rd_f25_content_rd_intensity_sbcassets_126d_nrmslope_v079_signal,
    f25rd_f25_content_rd_intensity_sbcassets_252d_zprslope_v080_signal,
    f25rd_f25_content_rd_intensity_sbcassets_189d_emaslope_v081_signal,
    f25rd_f25_content_rd_intensity_sbcassets_84d_logslope_v082_signal,
    f25rd_f25_content_rd_intensity_sbcassets_378d_rnkslope_v083_signal,
    f25rd_f25_content_rd_intensity_sbcassets_105d_ratslope_v084_signal,
    f25rd_f25_content_rd_intensity_sbcassets_315d_ctrslope_v085_signal,
    f25rd_f25_content_rd_intensity_rndmix_63d_rawslope_v086_signal,
    f25rd_f25_content_rd_intensity_rndmix_126d_nrmslope_v087_signal,
    f25rd_f25_content_rd_intensity_rndmix_252d_zprslope_v088_signal,
    f25rd_f25_content_rd_intensity_rndmix_189d_emaslope_v089_signal,
    f25rd_f25_content_rd_intensity_rndmix_84d_logslope_v090_signal,
    f25rd_f25_content_rd_intensity_rndmix_378d_rnkslope_v091_signal,
    f25rd_f25_content_rd_intensity_rndmix_105d_ratslope_v092_signal,
    f25rd_f25_content_rd_intensity_rndmix_315d_ctrslope_v093_signal,
    f25rd_f25_content_rd_intensity_intensbal_63d_rawslope_v094_signal,
    f25rd_f25_content_rd_intensity_intensbal_126d_nrmslope_v095_signal,
    f25rd_f25_content_rd_intensity_intensbal_252d_zprslope_v096_signal,
    f25rd_f25_content_rd_intensity_intensbal_189d_emaslope_v097_signal,
    f25rd_f25_content_rd_intensity_intensbal_378d_rnkslope_v098_signal,
    f25rd_f25_content_rd_intensity_intensbal_315d_ctrslope_v099_signal,
    f25rd_f25_content_rd_intensity_rndmcapexrev_126d_nrmslope_v100_signal,
    f25rd_f25_content_rd_intensity_rndmcapexrev_84d_logslope_v101_signal,
    f25rd_f25_content_rd_intensity_rndmcapexrev_105d_ratslope_v102_signal,
    f25rd_f25_content_rd_intensity_rndmsbcrev_126d_nrmslope_v103_signal,
    f25rd_f25_content_rd_intensity_rndmsbcrev_84d_logslope_v104_signal,
    f25rd_f25_content_rd_intensity_rndmsbcrev_105d_ratslope_v105_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_63d_rawslope_v106_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_126d_nrmslope_v107_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_252d_zprslope_v108_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_189d_emaslope_v109_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_378d_rnkslope_v110_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_105d_ratslope_v111_signal,
    f25rd_f25_content_rd_intensity_rndsbcload_315d_ctrslope_v112_signal,
    f25rd_f25_content_rd_intensity_rndglog_63d_rawslope_v113_signal,
    f25rd_f25_content_rd_intensity_rndglog_126d_nrmslope_v114_signal,
    f25rd_f25_content_rd_intensity_rndglog_252d_zprslope_v115_signal,
    f25rd_f25_content_rd_intensity_rndglog_189d_emaslope_v116_signal,
    f25rd_f25_content_rd_intensity_rndglog_84d_logslope_v117_signal,
    f25rd_f25_content_rd_intensity_rndglog_378d_rnkslope_v118_signal,
    f25rd_f25_content_rd_intensity_rndglog_105d_ratslope_v119_signal,
    f25rd_f25_content_rd_intensity_rndglog_315d_ctrslope_v120_signal,
    f25rd_f25_content_rd_intensity_sbcgcapexspread_126d_nrmslope_v121_signal,
    f25rd_f25_content_rd_intensity_sbcgcapexspread_84d_logslope_v122_signal,
    f25rd_f25_content_rd_intensity_sbcgcapexspread_105d_ratslope_v123_signal,
    f25rd_f25_content_rd_intensity_rndrev_42d_rawslope_v124_signal,
    f25rd_f25_content_rd_intensity_rndrev_210d_nrmslope_v125_signal,
    f25rd_f25_content_rd_intensity_rndrev_126d_emaslope_v126_signal,
    f25rd_f25_content_rd_intensity_rndrev_168d_logslope_v127_signal,
    f25rd_f25_content_rd_intensity_rndrev_252d_rnkslope_v128_signal,
    f25rd_f25_content_rd_intensity_rndrev_63d_ratslope_v129_signal,
    f25rd_f25_content_rd_intensity_rndrev_189d_ctrslope_v130_signal,
    f25rd_f25_content_rd_intensity_rndassets_42d_rawslope_v131_signal,
    f25rd_f25_content_rd_intensity_rndassets_210d_nrmslope_v132_signal,
    f25rd_f25_content_rd_intensity_rndassets_168d_logslope_v133_signal,
    f25rd_f25_content_rd_intensity_rndassets_63d_ratslope_v134_signal,
    f25rd_f25_content_rd_intensity_capexrev_42d_rawslope_v135_signal,
    f25rd_f25_content_rd_intensity_capexrev_210d_nrmslope_v136_signal,
    f25rd_f25_content_rd_intensity_capexrev_504d_zprslope_v137_signal,
    f25rd_f25_content_rd_intensity_capexrev_168d_logslope_v138_signal,
    f25rd_f25_content_rd_intensity_capexrev_63d_ratslope_v139_signal,
    f25rd_f25_content_rd_intensity_capexassets_42d_rawslope_v140_signal,
    f25rd_f25_content_rd_intensity_capexassets_210d_nrmslope_v141_signal,
    f25rd_f25_content_rd_intensity_capexassets_126d_emaslope_v142_signal,
    f25rd_f25_content_rd_intensity_capexassets_168d_logslope_v143_signal,
    f25rd_f25_content_rd_intensity_capexassets_63d_ratslope_v144_signal,
    f25rd_f25_content_rd_intensity_reinvrev_210d_nrmslope_v145_signal,
    f25rd_f25_content_rd_intensity_reinvrev_504d_zprslope_v146_signal,
    f25rd_f25_content_rd_intensity_reinvrev_126d_emaslope_v147_signal,
    f25rd_f25_content_rd_intensity_reinvrev_168d_logslope_v148_signal,
    f25rd_f25_content_rd_intensity_reinvrev_63d_ratslope_v149_signal,
    f25rd_f25_content_rd_intensity_reinvassets_42d_rawslope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_CONTENT_RD_INTENSITY_REGISTRY_001_150 = REGISTRY


_ALLOWLIST = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
    "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
    "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
    "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
    "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
    "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
    "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
    "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
    "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
    "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}


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

    rnd = _fund(101, base=4e7, drift=0.035, vol=0.08).rename("rnd")
    capex = _fund(102, base=3e7, drift=0.025, vol=0.10).rename("capex")
    revenue = _fund(103, base=2e8, drift=0.030, vol=0.05).rename("revenue")
    assets = _fund(104, base=6e8, drift=0.020, vol=0.04).rename("assets")
    sbcomp = _fund(105, base=2e7, drift=0.040, vol=0.12).rename("sbcomp")

    cols = {"rnd": rnd, "capex": capex, "revenue": revenue,
            "assets": assets, "sbcomp": sbcomp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= _ALLOWLIST, \
            "%s inputs not subset of allowlist: %s" % (name, meta["inputs"])
        assert len(meta["inputs"]) >= 1, name
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

    print("OK %s: %d features pass" % ('f25_content_rd_intensity_2nd_derivatives_001_150_claude', n_features))
