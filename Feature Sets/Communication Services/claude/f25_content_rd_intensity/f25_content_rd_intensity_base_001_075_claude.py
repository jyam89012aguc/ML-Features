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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, k):
    return s.diff(k) / float(k)


# ===== folder domain primitives (R&D / content reinvestment intensity) =====
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


def _f25_sbc_reinvest(sbcomp, rnd, capex):
    return sbcomp / (rnd + capex).replace(0, np.nan)


def _f25_rnd_capex(rnd, capex):
    return rnd / capex.replace(0, np.nan)


def _f25_rnd_mix(rnd, capex):
    return rnd / (rnd + capex).replace(0, np.nan)


def _f25_growth(s, k):
    return np.log(s.replace(0, np.nan) / s.shift(k).replace(0, np.nan))


# ============================================================
# rnd / revenue intensity (level)
def f25rd_f25_content_rd_intensity_rndrev_lvl_252d_base_v001_signal(rnd, revenue):
    b = _mean(_f25_rnd_rev(rnd, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd / revenue z-scored vs own 504d history (de-trended intensity)
def f25rd_f25_content_rd_intensity_rndrev_z_504d_base_v002_signal(rnd, revenue):
    b = _z(_f25_rnd_rev(rnd, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd / revenue percentile rank vs own 252d history
def f25rd_f25_content_rd_intensity_rndrev_rank_252d_base_v003_signal(rnd, revenue):
    b = _rank(_f25_rnd_rev(rnd, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd / assets intensity (level)
def f25rd_f25_content_rd_intensity_rndassets_lvl_252d_base_v004_signal(rnd, assets):
    b = _mean(_f25_rnd_assets(rnd, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd / assets z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_rndassets_z_504d_base_v005_signal(rnd, assets):
    b = _z(_f25_rnd_assets(rnd, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth (year-over-year log change of rnd)
def f25rd_f25_content_rd_intensity_rndgrow_252d_base_v006_signal(rnd):
    b = _f25_growth(rnd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth (half-year log change)
def f25rd_f25_content_rd_intensity_rndgrow_126d_base_v007_signal(rnd):
    b = _f25_growth(rnd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex / revenue intensity (content/platform spend, level)
def f25rd_f25_content_rd_intensity_capexrev_lvl_252d_base_v008_signal(capex, revenue):
    b = _mean(_f25_capex_rev(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex / revenue z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_capexrev_z_504d_base_v009_signal(capex, revenue):
    b = _z(_f25_capex_rev(capex, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate (rnd+capex)/revenue (level)
def f25rd_f25_content_rd_intensity_reinvrev_lvl_252d_base_v010_signal(rnd, capex, revenue):
    b = _mean(_f25_reinvest_rev(rnd, capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate (rnd+capex)/revenue z-scored
def f25rd_f25_content_rd_intensity_reinvrev_z_504d_base_v011_signal(rnd, capex, revenue):
    b = _z(_f25_reinvest_rev(rnd, capex, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC / revenue intensity (dilution-funded spend, level)
def f25rd_f25_content_rd_intensity_sbcrev_lvl_252d_base_v012_signal(sbcomp, revenue):
    b = _mean(_f25_sbc_rev(sbcomp, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC / R&D EMA displacement (how much stock-funded research deviates from its trend)
def f25rd_f25_content_rd_intensity_sbcrnd_disp_ema_base_v013_signal(sbcomp, rnd):
    r = _f25_sbc_rnd(sbcomp, rnd)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC-funded reinvestment: sbcomp / (rnd+capex) (level)
def f25rd_f25_content_rd_intensity_sbcreinv_lvl_252d_base_v014_signal(sbcomp, rnd, capex):
    b = _mean(_f25_sbc_reinvest(sbcomp, rnd, capex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd / capex: research vs physical/content capex tilt (level)
def f25rd_f25_content_rd_intensity_rndcapex_lvl_252d_base_v015_signal(rnd, capex):
    b = _mean(_f25_rnd_capex(rnd, capex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D mix change: quarterly shift in research share of reinvestment (de-trended)
def f25rd_f25_content_rd_intensity_rndmix_chg_63d_base_v016_signal(rnd, capex):
    r = _f25_rnd_mix(rnd, capex)
    b = r.diff(63) - r.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue short vs long ratio (intensity acceleration regime)
def f25rd_f25_content_rd_intensity_rndrev_sl_63v252_base_v017_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue short vs long ratio
def f25rd_f25_content_rd_intensity_capexrev_sl_63v252_base_v018_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate short vs long ratio
def f25rd_f25_content_rd_intensity_reinv_sl_63v252_base_v019_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue dispersion (volatility of intensity over 252d)
def f25rd_f25_content_rd_intensity_rndrev_disp_252d_base_v020_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue dispersion (lumpiness of content spend)
def f25rd_f25_content_rd_intensity_capexrev_disp_252d_base_v021_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue EMA displacement (level minus slow EMA)
def f25rd_f25_content_rd_intensity_rndrev_disp_ema_base_v022_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth vs R&D growth gap (is R&D outrunning revenue?)
def f25rd_f25_content_rd_intensity_rndvsrev_grow_252d_base_v023_signal(rnd, revenue):
    b = _f25_growth(rnd, 252) - _f25_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth vs revenue growth gap
def f25rd_f25_content_rd_intensity_capexvsrev_grow_252d_base_v024_signal(capex, revenue):
    b = _f25_growth(capex, 252) - _f25_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth vs R&D growth gap (dilution outrunning research)
def f25rd_f25_content_rd_intensity_sbcvsrnd_grow_252d_base_v025_signal(sbcomp, rnd):
    b = _f25_growth(sbcomp, 252) - _f25_growth(rnd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets rising regime: fraction of last year above its 126d-ago level (count-friendly)
def f25rd_f25_content_rd_intensity_rndassets_rising_252d_base_v026_signal(rnd, assets):
    r = _f25_rnd_assets(rnd, assets)
    rising = (r > r.shift(126)).astype(float)
    b = rising.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets percentile rank vs own 504d history
def f25rd_f25_content_rd_intensity_capexassets_rank_504d_base_v027_signal(capex, assets):
    b = _rank(_f25_capex_assets(capex, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment / assets short-vs-long ratio (capital-deepening acceleration)
def f25rd_f25_content_rd_intensity_reinvassets_sl_63v252_base_v028_signal(rnd, capex, assets):
    r = _f25_reinvest_assets(rnd, capex, assets)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC / revenue z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_sbcrev_z_504d_base_v029_signal(sbcomp, revenue):
    b = _z(_f25_sbc_rev(sbcomp, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC / R&D z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_sbcrnd_z_504d_base_v030_signal(sbcomp, rnd):
    b = _z(_f25_sbc_rnd(sbcomp, rnd), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue tanh-squashed growth (bounded R&D intensity momentum)
def f25rd_f25_content_rd_intensity_rndrev_tanh_126d_base_v031_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    chg = r - r.shift(126)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate tanh-squashed growth
def f25rd_f25_content_rd_intensity_reinv_tanh_126d_base_v032_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    chg = r - r.shift(126)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D acceleration regime: rnd/revenue above its own 252d mean (fraction of last year)
def f25rd_f25_content_rd_intensity_rndrev_above_252d_base_v033_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    above = (r > _mean(r, 252)).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue above-its-mean regime (fraction of last year content-spend elevated)
def f25rd_f25_content_rd_intensity_capexrev_above_252d_base_v034_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    above = (r > _mean(r, 252)).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: R&D intensity x revenue growth (productive research scaling)
def f25rd_f25_content_rd_intensity_rndxrevgrow_252d_base_v035_signal(rnd, revenue):
    intens = _f25_rnd_rev(rnd, revenue)
    rg = _f25_growth(revenue, 252)
    b = intens * rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: SBC intensity x reinvestment rate (dilution-funded reinvestment burden)
def f25rd_f25_content_rd_intensity_sbcxreinv_252d_base_v036_signal(sbcomp, rnd, capex, revenue):
    s = _f25_sbc_rev(sbcomp, revenue)
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = s * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue sign x sqrt magnitude of deviation from 504d mean (compressed extremity)
def f25rd_f25_content_rd_intensity_rndrev_signmag_504d_base_v037_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    dev = r - _mean(r, 504)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex ratio z-scored (research-vs-content tilt de-trended)
def f25rd_f25_content_rd_intensity_rndcapex_z_504d_base_v038_signal(rnd, capex):
    b = _z(_f25_rnd_capex(rnd, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D mix percentile rank (share of reinvestment that is R&D, ranked)
def f25rd_f25_content_rd_intensity_rndmix_rank_504d_base_v039_signal(rnd, capex):
    b = _rank(_f25_rnd_mix(rnd, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC-funded reinvestment z-scored vs own history
def f25rd_f25_content_rd_intensity_sbcreinv_z_504d_base_v040_signal(sbcomp, rnd, capex):
    b = _z(_f25_sbc_reinvest(sbcomp, rnd, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd growth minus its own 252d-ago value (R&D growth acceleration)
def f25rd_f25_content_rd_intensity_rndgrow_accel_252d_base_v041_signal(rnd):
    g = _f25_growth(rnd, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth acceleration
def f25rd_f25_content_rd_intensity_capexgrow_accel_252d_base_v042_signal(capex):
    g = _f25_growth(capex, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue distance from its 504d max (intensity drawdown from peak research)
def f25rd_f25_content_rd_intensity_rndrev_ddmax_504d_base_v043_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    mx = r.rolling(504, min_periods=252).max()
    b = r / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue distance from its 504d max (content-spend pullback from peak)
def f25rd_f25_content_rd_intensity_capexrev_ddmax_504d_base_v044_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    mx = r.rolling(504, min_periods=252).max()
    b = r / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate distance from its 504d min (recovery off trough reinvestment)
def f25rd_f25_content_rd_intensity_reinv_recovmin_504d_base_v045_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    mn = r.rolling(504, min_periods=252).min()
    b = r / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets short vs long ratio
def f25rd_f25_content_rd_intensity_rndassets_sl_63v252_base_v046_signal(rnd, assets):
    r = _f25_rnd_assets(rnd, assets)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue short vs long ratio (dilution intensity acceleration)
def f25rd_f25_content_rd_intensity_sbcrev_sl_63v252_base_v047_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue 126d half-year mean (medium-window intensity level)
def f25rd_f25_content_rd_intensity_rndrev_lvl_126d_base_v048_signal(rnd, revenue):
    b = _mean(_f25_rnd_rev(rnd, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment / assets z-scored vs own history
def f25rd_f25_content_rd_intensity_reinvassets_z_504d_base_v049_signal(rnd, capex, assets):
    b = _z(_f25_reinvest_assets(rnd, capex, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/R&D short vs long ratio (acceleration of stock-funded research)
def f25rd_f25_content_rd_intensity_sbcrnd_sl_63v252_base_v050_signal(sbcomp, rnd):
    r = _f25_sbc_rnd(sbcomp, rnd)
    b = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research vs content-spend intensity spread, z-scored vs its own 252d history
def f25rd_f25_content_rd_intensity_rndmcapex_rev_z_252d_base_v051_signal(rnd, capex, revenue):
    spread = _f25_rnd_rev(rnd, revenue) - _f25_capex_rev(capex, revenue)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue dispersion-normalized z over 126d (intensity surprise)
def f25rd_f25_content_rd_intensity_rndrev_z_126d_base_v052_signal(rnd, revenue):
    b = _z(_f25_rnd_rev(rnd, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue z over 126d
def f25rd_f25_content_rd_intensity_capexrev_z_126d_base_v053_signal(capex, revenue):
    b = _z(_f25_capex_rev(capex, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate rising regime: fraction of last year above its 63d-ago level
def f25rd_f25_content_rd_intensity_reinv_rising_252d_base_v054_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    rising = (r > r.shift(63)).astype(float)
    b = rising.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC-funded reinvestment quarterly growth (acceleration of dilution-funding share)
def f25rd_f25_content_rd_intensity_sbcreinv_chg_63d_base_v055_signal(sbcomp, rnd, capex):
    r = _f25_sbc_reinvest(sbcomp, rnd, capex)
    b = r.diff(63) - r.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd intensity x SBC intensity interaction, z-scored vs own 252d history
def f25rd_f25_content_rd_intensity_rndxsbc_z_252d_base_v056_signal(rnd, revenue, sbcomp):
    a = _f25_rnd_rev(rnd, revenue)
    s = _f25_sbc_rev(sbcomp, revenue)
    b = _z(a * s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue 504d-vs-252d level ratio (long intensity drift)
def f25rd_f25_content_rd_intensity_rndrev_drift_252v504_base_v057_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _mean(r, 252) / _mean(r, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets level (content/platform capital deepening)
def f25rd_f25_content_rd_intensity_capexassets_lvl_252d_base_v058_signal(capex, assets):
    b = _mean(_f25_capex_assets(capex, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research-intensity vs capex-intensity balance: (rnd/rev) / (capex/assets), de-trended
def f25rd_f25_content_rd_intensity_intensbal_252d_base_v059_signal(rnd, revenue, capex, assets):
    bal = _f25_rnd_rev(rnd, revenue) / _f25_capex_assets(capex, assets).replace(0, np.nan)
    b = bal - _mean(bal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue dispersion (volatility of dilution intensity)
def f25rd_f25_content_rd_intensity_sbcrev_disp_252d_base_v060_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue EMA-fast minus EMA-slow (intensity momentum oscillator)
def f25rd_f25_content_rd_intensity_rndrev_osc_base_v061_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = r.ewm(span=63, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets EMA momentum oscillator (balance-sheet content-spend acceleration)
def f25rd_f25_content_rd_intensity_capexassets_osc_base_v062_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    b = r.ewm(span=63, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth percentile rank (where current research growth sits historically)
def f25rd_f25_content_rd_intensity_rndgrow_rank_504d_base_v063_signal(rnd):
    b = _rank(_f25_growth(rnd, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth percentile rank
def f25rd_f25_content_rd_intensity_capexgrow_rank_504d_base_v064_signal(capex):
    b = _rank(_f25_growth(capex, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate dispersion (cyclicality of total reinvestment)
def f25rd_f25_content_rd_intensity_reinv_disp_252d_base_v065_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research-vs-capex balance: (rnd-capex)/(rnd+capex), de-trended by its 252d mean
def f25rd_f25_content_rd_intensity_rndcapex_bal_252d_base_v066_signal(rnd, capex):
    bal = (rnd - capex) / (rnd + capex).replace(0, np.nan)
    b = bal - _mean(bal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/(rnd+capex) sign x magnitude vs 504d mean (dilution-funding extremity)
def f25rd_f25_content_rd_intensity_sbcreinv_signmag_504d_base_v067_signal(sbcomp, rnd, capex):
    r = _f25_sbc_reinvest(sbcomp, rnd, capex)
    dev = r - _mean(r, 504)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-mix interaction with reinvestment momentum (research tilt x reinvest acceleration)
def f25rd_f25_content_rd_intensity_rndmixxmom_126d_base_v068_signal(rnd, capex, revenue):
    mix = _f25_rnd_mix(rnd, capex)
    reinv = _f25_reinvest_rev(rnd, capex, revenue)
    mom = reinv - reinv.shift(126)
    b = (mix - 0.5) * np.tanh(15.0 * mom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment / revenue distance from its 252d mean in std units, then ranked
def f25rd_f25_content_rd_intensity_reinv_zrank_252d_base_v069_signal(rnd, capex, revenue):
    z = _z(_f25_reinvest_rev(rnd, capex, revenue), 252)
    b = _rank(z, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue acceleration: quarterly change minus prior quarterly change (jerk-like)
def f25rd_f25_content_rd_intensity_sbcrev_accel_126d_base_v070_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    g = r.diff(63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue 63d short-window intensity (fast research signal)
def f25rd_f25_content_rd_intensity_rndrev_lvl_63d_base_v071_signal(rnd, revenue):
    b = _mean(_f25_rnd_rev(rnd, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex vs rnd growth gap (content capex outrunning research)
def f25rd_f25_content_rd_intensity_capexvsrnd_grow_252d_base_v072_signal(capex, rnd):
    b = _f25_growth(capex, 252) - _f25_growth(rnd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/R&D dispersion (volatility of stock-funded research share)
def f25rd_f25_content_rd_intensity_sbcrnd_disp_252d_base_v073_signal(sbcomp, rnd):
    r = _f25_sbc_rnd(sbcomp, rnd)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D mix EMA displacement (shift in research share of reinvestment)
def f25rd_f25_content_rd_intensity_rndmix_disp_ema_base_v074_signal(rnd, capex):
    r = _f25_rnd_mix(rnd, capex)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate x SBC-intensity rank interaction (stress of dilution-heavy reinvestment)
def f25rd_f25_content_rd_intensity_reinvxsbc_rank_504d_base_v075_signal(rnd, capex, revenue, sbcomp):
    rr = _rank(_f25_reinvest_rev(rnd, capex, revenue), 504)
    sr = _rank(_f25_sbc_rev(sbcomp, revenue), 504)
    b = rr * sr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25rd_f25_content_rd_intensity_rndrev_lvl_252d_base_v001_signal,
    f25rd_f25_content_rd_intensity_rndrev_z_504d_base_v002_signal,
    f25rd_f25_content_rd_intensity_rndrev_rank_252d_base_v003_signal,
    f25rd_f25_content_rd_intensity_rndassets_lvl_252d_base_v004_signal,
    f25rd_f25_content_rd_intensity_rndassets_z_504d_base_v005_signal,
    f25rd_f25_content_rd_intensity_rndgrow_252d_base_v006_signal,
    f25rd_f25_content_rd_intensity_rndgrow_126d_base_v007_signal,
    f25rd_f25_content_rd_intensity_capexrev_lvl_252d_base_v008_signal,
    f25rd_f25_content_rd_intensity_capexrev_z_504d_base_v009_signal,
    f25rd_f25_content_rd_intensity_reinvrev_lvl_252d_base_v010_signal,
    f25rd_f25_content_rd_intensity_reinvrev_z_504d_base_v011_signal,
    f25rd_f25_content_rd_intensity_sbcrev_lvl_252d_base_v012_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_disp_ema_base_v013_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_lvl_252d_base_v014_signal,
    f25rd_f25_content_rd_intensity_rndcapex_lvl_252d_base_v015_signal,
    f25rd_f25_content_rd_intensity_rndmix_chg_63d_base_v016_signal,
    f25rd_f25_content_rd_intensity_rndrev_sl_63v252_base_v017_signal,
    f25rd_f25_content_rd_intensity_capexrev_sl_63v252_base_v018_signal,
    f25rd_f25_content_rd_intensity_reinv_sl_63v252_base_v019_signal,
    f25rd_f25_content_rd_intensity_rndrev_disp_252d_base_v020_signal,
    f25rd_f25_content_rd_intensity_capexrev_disp_252d_base_v021_signal,
    f25rd_f25_content_rd_intensity_rndrev_disp_ema_base_v022_signal,
    f25rd_f25_content_rd_intensity_rndvsrev_grow_252d_base_v023_signal,
    f25rd_f25_content_rd_intensity_capexvsrev_grow_252d_base_v024_signal,
    f25rd_f25_content_rd_intensity_sbcvsrnd_grow_252d_base_v025_signal,
    f25rd_f25_content_rd_intensity_rndassets_rising_252d_base_v026_signal,
    f25rd_f25_content_rd_intensity_capexassets_rank_504d_base_v027_signal,
    f25rd_f25_content_rd_intensity_reinvassets_sl_63v252_base_v028_signal,
    f25rd_f25_content_rd_intensity_sbcrev_z_504d_base_v029_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_z_504d_base_v030_signal,
    f25rd_f25_content_rd_intensity_rndrev_tanh_126d_base_v031_signal,
    f25rd_f25_content_rd_intensity_reinv_tanh_126d_base_v032_signal,
    f25rd_f25_content_rd_intensity_rndrev_above_252d_base_v033_signal,
    f25rd_f25_content_rd_intensity_capexrev_above_252d_base_v034_signal,
    f25rd_f25_content_rd_intensity_rndxrevgrow_252d_base_v035_signal,
    f25rd_f25_content_rd_intensity_sbcxreinv_252d_base_v036_signal,
    f25rd_f25_content_rd_intensity_rndrev_signmag_504d_base_v037_signal,
    f25rd_f25_content_rd_intensity_rndcapex_z_504d_base_v038_signal,
    f25rd_f25_content_rd_intensity_rndmix_rank_504d_base_v039_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_z_504d_base_v040_signal,
    f25rd_f25_content_rd_intensity_rndgrow_accel_252d_base_v041_signal,
    f25rd_f25_content_rd_intensity_capexgrow_accel_252d_base_v042_signal,
    f25rd_f25_content_rd_intensity_rndrev_ddmax_504d_base_v043_signal,
    f25rd_f25_content_rd_intensity_capexrev_ddmax_504d_base_v044_signal,
    f25rd_f25_content_rd_intensity_reinv_recovmin_504d_base_v045_signal,
    f25rd_f25_content_rd_intensity_rndassets_sl_63v252_base_v046_signal,
    f25rd_f25_content_rd_intensity_sbcrev_sl_63v252_base_v047_signal,
    f25rd_f25_content_rd_intensity_rndrev_lvl_126d_base_v048_signal,
    f25rd_f25_content_rd_intensity_reinvassets_z_504d_base_v049_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_sl_63v252_base_v050_signal,
    f25rd_f25_content_rd_intensity_rndmcapex_rev_z_252d_base_v051_signal,
    f25rd_f25_content_rd_intensity_rndrev_z_126d_base_v052_signal,
    f25rd_f25_content_rd_intensity_capexrev_z_126d_base_v053_signal,
    f25rd_f25_content_rd_intensity_reinv_rising_252d_base_v054_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_chg_63d_base_v055_signal,
    f25rd_f25_content_rd_intensity_rndxsbc_z_252d_base_v056_signal,
    f25rd_f25_content_rd_intensity_rndrev_drift_252v504_base_v057_signal,
    f25rd_f25_content_rd_intensity_capexassets_lvl_252d_base_v058_signal,
    f25rd_f25_content_rd_intensity_intensbal_252d_base_v059_signal,
    f25rd_f25_content_rd_intensity_sbcrev_disp_252d_base_v060_signal,
    f25rd_f25_content_rd_intensity_rndrev_osc_base_v061_signal,
    f25rd_f25_content_rd_intensity_capexassets_osc_base_v062_signal,
    f25rd_f25_content_rd_intensity_rndgrow_rank_504d_base_v063_signal,
    f25rd_f25_content_rd_intensity_capexgrow_rank_504d_base_v064_signal,
    f25rd_f25_content_rd_intensity_reinv_disp_252d_base_v065_signal,
    f25rd_f25_content_rd_intensity_rndcapex_bal_252d_base_v066_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_signmag_504d_base_v067_signal,
    f25rd_f25_content_rd_intensity_rndmixxmom_126d_base_v068_signal,
    f25rd_f25_content_rd_intensity_reinv_zrank_252d_base_v069_signal,
    f25rd_f25_content_rd_intensity_sbcrev_accel_126d_base_v070_signal,
    f25rd_f25_content_rd_intensity_rndrev_lvl_63d_base_v071_signal,
    f25rd_f25_content_rd_intensity_capexvsrnd_grow_252d_base_v072_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_disp_252d_base_v073_signal,
    f25rd_f25_content_rd_intensity_rndmix_disp_ema_base_v074_signal,
    f25rd_f25_content_rd_intensity_reinvxsbc_rank_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_CONTENT_RD_INTENSITY_REGISTRY_001_075 = REGISTRY


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

    assert n_features == 75, n_features
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

    print("OK f25_content_rd_intensity_base_001_075_claude: %d features pass" % n_features)
