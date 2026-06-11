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


def _f25_growth(s, k):
    return np.log(s.replace(0, np.nan) / s.shift(k).replace(0, np.nan))


def _f25_accel(s, k):
    g = s.diff(k)
    return g - g.shift(k)


# ============================================================
# rnd/revenue year-over-year change (research intensity YoY shift)
def f25rd_f25_content_rd_intensity_rndrev_yoy_252d_base_v076_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue year-over-year change (content-spend intensity YoY shift)
def f25rd_f25_content_rd_intensity_capexrev_yoy_252d_base_v077_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate year-over-year change
def f25rd_f25_content_rd_intensity_reinv_yoy_252d_base_v078_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue year-over-year change (dilution intensity YoY shift)
def f25rd_f25_content_rd_intensity_sbcrev_yoy_252d_base_v079_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue quarterly acceleration (2nd difference of intensity)
def f25rd_f25_content_rd_intensity_rndrev_accel_63d_base_v080_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _f25_accel(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue quarterly acceleration
def f25rd_f25_content_rd_intensity_capexrev_accel_63d_base_v081_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = _f25_accel(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/(rnd+capex) quarterly acceleration (dilution-funding 2nd difference)
def f25rd_f25_content_rd_intensity_sbcreinv_accel_63d_base_v082_signal(sbcomp, rnd, capex):
    r = _f25_sbc_reinvest(sbcomp, rnd, capex)
    b = _f25_accel(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets year-over-year change
def f25rd_f25_content_rd_intensity_rndassets_yoy_252d_base_v083_signal(rnd, assets):
    r = _f25_rnd_assets(rnd, assets)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/capex ratio quarterly change de-trended (stock-vs-hard-spend tilt momentum)
def f25rd_f25_content_rd_intensity_sbccapex_chg_63d_base_v084_signal(sbcomp, capex):
    r = _f25_sbc_capex(sbcomp, capex)
    b = r.diff(63) - r.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/capex z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_sbccapex_z_504d_base_v085_signal(sbcomp, capex):
    b = _z(_f25_sbc_capex(sbcomp, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/assets short-vs-long mean ratio (balance-sheet dilution-load acceleration)
def f25rd_f25_content_rd_intensity_sbcassets_sl_126v504_base_v086_signal(sbcomp, assets):
    r = _f25_sbc_assets(sbcomp, assets)
    b = _mean(r, 126) / _mean(r, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex EMA momentum oscillator (research-vs-capex tilt acceleration)
def f25rd_f25_content_rd_intensity_rndcapex_osc_base_v087_signal(rnd, capex):
    r = _f25_rnd_capex(rnd, capex)
    b = r.ewm(span=63, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/capex EMA momentum oscillator (stock-comp vs hard-spend acceleration)
def f25rd_f25_content_rd_intensity_sbccapex_osc_base_v088_signal(sbcomp, capex):
    r = _f25_sbc_capex(sbcomp, capex)
    b = r.ewm(span=63, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets EMA momentum oscillator (content-deepening acceleration)
def f25rd_f25_content_rd_intensity_capexassets_osc_base_v089_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    b = r.ewm(span=63, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-growth minus capex-growth (which leg of reinvestment is accelerating)
def f25rd_f25_content_rd_intensity_rndvscapex_grow_126d_base_v090_signal(rnd, capex):
    b = _f25_growth(rnd, 126) - _f25_growth(capex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC-growth minus reinvestment-growth (dilution outrunning real reinvestment)
def f25rd_f25_content_rd_intensity_sbcvsreinv_grow_252d_base_v091_signal(sbcomp, rnd, capex):
    reinv = rnd + capex
    b = _f25_growth(sbcomp, 252) - _f25_growth(reinv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue regime: fraction of last year intensity exceeds its 504d median band
def f25rd_f25_content_rd_intensity_rndrev_hiregime_252d_base_v092_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    med = r.rolling(504, min_periods=252).median()
    hot = (r > med * 1.05).astype(float)
    b = hot.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue lumpy-spend regime: fraction of last year above 1.1x its 252d mean
def f25rd_f25_content_rd_intensity_capexrev_burst_252d_base_v093_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    burst = (r > _mean(r, 252) * 1.10).astype(float)
    b = burst.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate rising-streak length (consecutive quarters of higher reinvestment)
def f25rd_f25_content_rd_intensity_reinv_streak_base_v094_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    up = (r > r.shift(63)).astype(float)
    grp = (up != up.shift(1)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research-minus-content intensity spread, sign x magnitude vs 504d mean (tilt extremity)
def f25rd_f25_content_rd_intensity_rndmcapex_signmag_504d_base_v095_signal(rnd, revenue, capex):
    spread = _f25_rnd_rev(rnd, revenue) - _f25_capex_rev(capex, revenue)
    dev = spread - _mean(spread, 504)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets sign x magnitude vs 504d mean (content-deepening extremity)
def f25rd_f25_content_rd_intensity_capexassets_signmag_504d_base_v096_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    dev = r - _mean(r, 504)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue tanh of z-score (bounded de-trended research intensity)
def f25rd_f25_content_rd_intensity_rndrev_tanhz_252d_base_v097_signal(rnd, revenue):
    z = _z(_f25_rnd_rev(rnd, revenue), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/R&D tanh of z-score (bounded dilution-funded-research intensity)
def f25rd_f25_content_rd_intensity_sbcrnd_tanhz_252d_base_v098_signal(sbcomp, rnd):
    z = _z(_f25_sbc_rnd(sbcomp, rnd), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd-revenue gap: rnd growth in excess of revenue growth, ranked (productive scaling)
def f25rd_f25_content_rd_intensity_rndexcess_rank_504d_base_v099_signal(rnd, revenue):
    gap = _f25_growth(rnd, 252) - _f25_growth(revenue, 252)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-revenue gap ranked (content capex outrunning revenue)
def f25rd_f25_content_rd_intensity_capexexcess_rank_504d_base_v100_signal(capex, revenue):
    gap = _f25_growth(capex, 252) - _f25_growth(revenue, 252)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets EMA displacement (research-on-balance-sheet vs trend)
def f25rd_f25_content_rd_intensity_rndassets_disp_ema_base_v101_signal(rnd, assets):
    r = _f25_rnd_assets(rnd, assets)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue EMA displacement (content-spend vs trend)
def f25rd_f25_content_rd_intensity_capexrev_disp_ema_base_v102_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment/assets EMA displacement
def f25rd_f25_content_rd_intensity_reinvassets_disp_ema_base_v103_signal(rnd, capex, assets):
    r = _f25_reinvest_assets(rnd, capex, assets)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth half-year minus quarter (research-growth term structure)
def f25rd_f25_content_rd_intensity_rndgrow_term_base_v104_signal(rnd):
    b = _f25_growth(rnd, 126) - 2.0 * _f25_growth(rnd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth term structure (half-year vs quarter)
def f25rd_f25_content_rd_intensity_capexgrow_term_base_v105_signal(capex):
    b = _f25_growth(capex, 126) - 2.0 * _f25_growth(capex, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth term structure (half-year vs quarter)
def f25rd_f25_content_rd_intensity_sbcgrow_term_base_v106_signal(sbcomp):
    b = _f25_growth(sbcomp, 126) - 2.0 * _f25_growth(sbcomp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue distance above its 504d min in std units (build-up off trough intensity)
def f25rd_f25_content_rd_intensity_rndrev_trough_504d_base_v107_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    mn = r.rolling(504, min_periods=252).min()
    sd = _std(r, 504).replace(0, np.nan)
    b = (r - mn) / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue distance below its 504d max in std units (pullback depth from peak)
def f25rd_f25_content_rd_intensity_capexrev_peak_504d_base_v108_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    mx = r.rolling(504, min_periods=252).max()
    sd = _std(r, 504).replace(0, np.nan)
    b = (mx - r) / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate range position within its own 504d band (0..1 minus 0.5)
def f25rd_f25_content_rd_intensity_reinv_rngpos_504d_base_v109_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    mx = r.rolling(504, min_periods=252).max()
    mn = r.rolling(504, min_periods=252).min()
    b = (r - mn) / (mx - mn).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue range position within its 504d band
def f25rd_f25_content_rd_intensity_sbcrev_rngpos_504d_base_v110_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    mx = r.rolling(504, min_periods=252).max()
    mn = r.rolling(504, min_periods=252).min()
    b = (r - mn) / (mx - mn).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd intensity vs sbc intensity spread (research vs dilution per dollar of revenue)
def f25rd_f25_content_rd_intensity_rndmsbc_rev_252d_base_v111_signal(rnd, sbcomp, revenue):
    spread = _f25_rnd_rev(rnd, revenue) - _f25_sbc_rev(sbcomp, revenue)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vs sbc intensity spread, z-scored
def f25rd_f25_content_rd_intensity_capexmsbc_rev_252d_base_v112_signal(capex, sbcomp, revenue):
    spread = _f25_capex_rev(capex, revenue) - _f25_sbc_rev(sbcomp, revenue)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue half-year z-score (medium-window research intensity surprise)
def f25rd_f25_content_rd_intensity_rndrev_z_126d_base_v113_signal(rnd, revenue):
    b = _z(_f25_rnd_rev(rnd, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC-funded reinvestment half-year z-score
def f25rd_f25_content_rd_intensity_sbcreinv_z_126d_base_v114_signal(sbcomp, rnd, capex):
    b = _z(_f25_sbc_reinvest(sbcomp, rnd, capex), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex ratio quarterly change de-trended (research tilt momentum)
def f25rd_f25_content_rd_intensity_rndcapex_chg_63d_base_v115_signal(rnd, capex):
    r = _f25_rnd_capex(rnd, capex)
    b = r.diff(63) - r.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue x reinvestment-rate interaction, z-scored (intensity stacking)
def f25rd_f25_content_rd_intensity_rndrevxreinv_z_252d_base_v116_signal(rnd, revenue, capex):
    a = _f25_rnd_rev(rnd, revenue)
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _z(a * r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue x capex/revenue interaction, z-scored (dilution-heavy content build)
def f25rd_f25_content_rd_intensity_sbcxcapex_z_252d_base_v117_signal(sbcomp, revenue, capex):
    s = _f25_sbc_rev(sbcomp, revenue)
    c = _f25_capex_rev(capex, revenue)
    b = _z(s * c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue volatility ratio short-vs-long (regime change in research stability)
def f25rd_f25_content_rd_intensity_rndrev_volratio_base_v118_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _std(r, 63) / _std(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue volatility ratio short-vs-long (lumpiness regime change)
def f25rd_f25_content_rd_intensity_capexrev_volratio_base_v119_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = _std(r, 63) / _std(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate vs SBC intensity ratio (real reinvestment per unit dilution)
def f25rd_f25_content_rd_intensity_reinvpersbc_252d_base_v120_signal(rnd, capex, sbcomp):
    b = _mean((rnd + capex) / sbcomp.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-per-SBC z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_reinvpersbc_z_504d_base_v121_signal(rnd, capex, sbcomp):
    r = (rnd + capex) / sbcomp.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue 63d slope normalized by its 252d mean (fast research-intensity drift)
def f25rd_f25_content_rd_intensity_rndrev_drift_63d_base_v122_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = (r.diff(63) / 63.0) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets 63d slope normalized by its 252d mean
def f25rd_f25_content_rd_intensity_capexassets_drift_63d_base_v123_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    b = (r.diff(63) / 63.0) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D mix (rnd share of reinvestment) z-scored vs own 504d history
def f25rd_f25_content_rd_intensity_rndmix_z_504d_base_v124_signal(rnd, capex):
    b = _z(_f25_rnd_mix(rnd, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue percentile rank vs 504d history (long research-intensity standing)
def f25rd_f25_content_rd_intensity_rndrev_rank_504d_base_v125_signal(rnd, revenue):
    b = _rank(_f25_rnd_rev(rnd, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue percentile rank vs 504d history
def f25rd_f25_content_rd_intensity_capexrev_rank_504d_base_v126_signal(capex, revenue):
    b = _rank(_f25_capex_rev(capex, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue percentile rank vs 504d history
def f25rd_f25_content_rd_intensity_sbcrev_rank_504d_base_v127_signal(sbcomp, revenue):
    b = _rank(_f25_sbc_rev(sbcomp, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue quarterly acceleration ranked (research-intensity 2nd-difference standing)
def f25rd_f25_content_rd_intensity_rndrev_accelrank_504d_base_v128_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _rank(_f25_accel(r, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate accel ranked (where reinvestment acceleration sits historically)
def f25rd_f25_content_rd_intensity_reinv_accelrank_504d_base_v129_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _rank(_f25_accel(r, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue dispersion regime (volatility of dilution intensity, coefficient of variation)
def f25rd_f25_content_rd_intensity_sbcrev_cv_252d_base_v130_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    b = _std(r, 126) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue x revenue-growth sign interaction (intensity in growth vs shrink regimes)
def f25rd_f25_content_rd_intensity_rndrevxrsign_252d_base_v131_signal(rnd, revenue):
    a = _f25_rnd_rev(rnd, revenue)
    rg = _f25_growth(revenue, 126)
    b = a * np.sign(rg) * np.tanh(5.0 * rg.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue minus its 1-year-ago value, z-scored (intensity step de-trended)
def f25rd_f25_content_rd_intensity_capexrev_step_z_252d_base_v132_signal(capex, revenue):
    r = _f25_capex_rev(capex, revenue)
    b = _z(r - r.shift(252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets short-vs-long mean ratio (research-deepening acceleration on assets)
def f25rd_f25_content_rd_intensity_rndassets_sl_126v504_base_v133_signal(rnd, assets):
    r = _f25_rnd_assets(rnd, assets)
    b = _mean(r, 126) / _mean(r, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets short-vs-long mean ratio
def f25rd_f25_content_rd_intensity_capexassets_sl_126v504_base_v134_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    b = _mean(r, 126) / _mean(r, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/R&D quarterly change de-trended (stock-funded research momentum)
def f25rd_f25_content_rd_intensity_sbcrnd_chg_63d_base_v135_signal(sbcomp, rnd):
    r = _f25_sbc_rnd(sbcomp, rnd)
    b = r.diff(63) - r.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate convexity: level minus average of short & long means (curvature)
def f25rd_f25_content_rd_intensity_reinv_convex_base_v136_signal(rnd, capex, revenue):
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _mean(r, 126) - 0.5 * (_mean(r, 63) + _mean(r, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue convexity (curvature of research-intensity term structure)
def f25rd_f25_content_rd_intensity_rndrev_convex_base_v137_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _mean(r, 126) - 0.5 * (_mean(r, 63) + _mean(r, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/(rnd+capex) range position within its 504d band
def f25rd_f25_content_rd_intensity_sbcreinv_rngpos_504d_base_v138_signal(sbcomp, rnd, capex):
    r = _f25_sbc_reinvest(sbcomp, rnd, capex)
    mx = r.rolling(504, min_periods=252).max()
    mn = r.rolling(504, min_periods=252).min()
    b = (r - mn) / (mx - mn).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue minus capex/assets tilt, quarterly change de-trended (tilt momentum)
def f25rd_f25_content_rd_intensity_rndcapextilt_chg_63d_base_v139_signal(rnd, revenue, capex, assets):
    tilt = _f25_rnd_rev(rnd, revenue) - _f25_capex_assets(capex, assets)
    b = tilt.diff(63) - tilt.diff(63).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/assets EMA displacement (balance-sheet dilution load vs its own trend)
def f25rd_f25_content_rd_intensity_sbcassets_disp_ema_base_v140_signal(sbcomp, assets):
    r = _f25_sbc_assets(sbcomp, assets)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd growth x SBC growth co-movement sign (joint research+dilution expansion)
def f25rd_f25_content_rd_intensity_rndsbc_comove_252d_base_v141_signal(rnd, sbcomp):
    gr = _f25_growth(rnd, 126)
    gs = _f25_growth(sbcomp, 126)
    b = np.sign(gr) * np.sign(gs) * (gr.abs() + gs.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue tanh of z-score (bounded de-trended content-spend intensity)
def f25rd_f25_content_rd_intensity_capexrev_tanhz_252d_base_v142_signal(capex, revenue):
    z = _z(_f25_capex_rev(capex, revenue), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate tanh of z-score
def f25rd_f25_content_rd_intensity_reinv_tanhz_252d_base_v143_signal(rnd, capex, revenue):
    z = _z(_f25_reinvest_rev(rnd, capex, revenue), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/revenue half-year vs quarter mean ratio (very short intensity acceleration)
def f25rd_f25_content_rd_intensity_rndrev_sl_21v126_base_v144_signal(rnd, revenue):
    r = _f25_rnd_rev(rnd, revenue)
    b = _mean(r, 21) / _mean(r, 126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue convexity (curvature of dilution-intensity term structure)
def f25rd_f25_content_rd_intensity_sbcrev_convex_base_v145_signal(sbcomp, revenue):
    r = _f25_sbc_rev(sbcomp, revenue)
    b = _mean(r, 126) - 0.5 * (_mean(r, 63) + _mean(r, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/assets x reinvestment-rate interaction, z-scored (balance-sheet research load)
def f25rd_f25_content_rd_intensity_rndassetsxreinv_z_252d_base_v146_signal(rnd, assets, capex, revenue):
    a = _f25_rnd_assets(rnd, assets)
    r = _f25_reinvest_rev(rnd, capex, revenue)
    b = _z(a * r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets quarterly acceleration ranked (content-deepening 2nd-difference standing)
def f25rd_f25_content_rd_intensity_capexassets_accelrank_504d_base_v147_signal(capex, assets):
    r = _f25_capex_assets(capex, assets)
    b = _rank(_f25_accel(r, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-per-SBC quarterly acceleration de-trended (real-vs-dilution 2nd difference)
def f25rd_f25_content_rd_intensity_reinvpersbc_accel_63d_base_v148_signal(rnd, capex, sbcomp):
    r = (rnd + capex) / sbcomp.replace(0, np.nan)
    g = r.diff(63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex balance YoY change (research-vs-content tilt shift over a year)
def f25rd_f25_content_rd_intensity_rndcapexbal_yoy_base_v149_signal(rnd, capex):
    bal = (rnd - capex) / (rnd + capex).replace(0, np.nan)
    b = bal - bal.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research-to-dilution efficiency: rnd / sbcomp, de-trended by its 252d mean
def f25rd_f25_content_rd_intensity_rndpersbc_252d_base_v150_signal(rnd, sbcomp):
    r = rnd / sbcomp.replace(0, np.nan)
    b = r - _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25rd_f25_content_rd_intensity_rndrev_yoy_252d_base_v076_signal,
    f25rd_f25_content_rd_intensity_capexrev_yoy_252d_base_v077_signal,
    f25rd_f25_content_rd_intensity_reinv_yoy_252d_base_v078_signal,
    f25rd_f25_content_rd_intensity_sbcrev_yoy_252d_base_v079_signal,
    f25rd_f25_content_rd_intensity_rndrev_accel_63d_base_v080_signal,
    f25rd_f25_content_rd_intensity_capexrev_accel_63d_base_v081_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_accel_63d_base_v082_signal,
    f25rd_f25_content_rd_intensity_rndassets_yoy_252d_base_v083_signal,
    f25rd_f25_content_rd_intensity_sbccapex_chg_63d_base_v084_signal,
    f25rd_f25_content_rd_intensity_sbccapex_z_504d_base_v085_signal,
    f25rd_f25_content_rd_intensity_sbcassets_sl_126v504_base_v086_signal,
    f25rd_f25_content_rd_intensity_rndcapex_osc_base_v087_signal,
    f25rd_f25_content_rd_intensity_sbccapex_osc_base_v088_signal,
    f25rd_f25_content_rd_intensity_capexassets_osc_base_v089_signal,
    f25rd_f25_content_rd_intensity_rndvscapex_grow_126d_base_v090_signal,
    f25rd_f25_content_rd_intensity_sbcvsreinv_grow_252d_base_v091_signal,
    f25rd_f25_content_rd_intensity_rndrev_hiregime_252d_base_v092_signal,
    f25rd_f25_content_rd_intensity_capexrev_burst_252d_base_v093_signal,
    f25rd_f25_content_rd_intensity_reinv_streak_base_v094_signal,
    f25rd_f25_content_rd_intensity_rndmcapex_signmag_504d_base_v095_signal,
    f25rd_f25_content_rd_intensity_capexassets_signmag_504d_base_v096_signal,
    f25rd_f25_content_rd_intensity_rndrev_tanhz_252d_base_v097_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_tanhz_252d_base_v098_signal,
    f25rd_f25_content_rd_intensity_rndexcess_rank_504d_base_v099_signal,
    f25rd_f25_content_rd_intensity_capexexcess_rank_504d_base_v100_signal,
    f25rd_f25_content_rd_intensity_rndassets_disp_ema_base_v101_signal,
    f25rd_f25_content_rd_intensity_capexrev_disp_ema_base_v102_signal,
    f25rd_f25_content_rd_intensity_reinvassets_disp_ema_base_v103_signal,
    f25rd_f25_content_rd_intensity_rndgrow_term_base_v104_signal,
    f25rd_f25_content_rd_intensity_capexgrow_term_base_v105_signal,
    f25rd_f25_content_rd_intensity_sbcgrow_term_base_v106_signal,
    f25rd_f25_content_rd_intensity_rndrev_trough_504d_base_v107_signal,
    f25rd_f25_content_rd_intensity_capexrev_peak_504d_base_v108_signal,
    f25rd_f25_content_rd_intensity_reinv_rngpos_504d_base_v109_signal,
    f25rd_f25_content_rd_intensity_sbcrev_rngpos_504d_base_v110_signal,
    f25rd_f25_content_rd_intensity_rndmsbc_rev_252d_base_v111_signal,
    f25rd_f25_content_rd_intensity_capexmsbc_rev_252d_base_v112_signal,
    f25rd_f25_content_rd_intensity_rndrev_z_126d_base_v113_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_z_126d_base_v114_signal,
    f25rd_f25_content_rd_intensity_rndcapex_chg_63d_base_v115_signal,
    f25rd_f25_content_rd_intensity_rndrevxreinv_z_252d_base_v116_signal,
    f25rd_f25_content_rd_intensity_sbcxcapex_z_252d_base_v117_signal,
    f25rd_f25_content_rd_intensity_rndrev_volratio_base_v118_signal,
    f25rd_f25_content_rd_intensity_capexrev_volratio_base_v119_signal,
    f25rd_f25_content_rd_intensity_reinvpersbc_252d_base_v120_signal,
    f25rd_f25_content_rd_intensity_reinvpersbc_z_504d_base_v121_signal,
    f25rd_f25_content_rd_intensity_rndrev_drift_63d_base_v122_signal,
    f25rd_f25_content_rd_intensity_capexassets_drift_63d_base_v123_signal,
    f25rd_f25_content_rd_intensity_rndmix_z_504d_base_v124_signal,
    f25rd_f25_content_rd_intensity_rndrev_rank_504d_base_v125_signal,
    f25rd_f25_content_rd_intensity_capexrev_rank_504d_base_v126_signal,
    f25rd_f25_content_rd_intensity_sbcrev_rank_504d_base_v127_signal,
    f25rd_f25_content_rd_intensity_rndrev_accelrank_504d_base_v128_signal,
    f25rd_f25_content_rd_intensity_reinv_accelrank_504d_base_v129_signal,
    f25rd_f25_content_rd_intensity_sbcrev_cv_252d_base_v130_signal,
    f25rd_f25_content_rd_intensity_rndrevxrsign_252d_base_v131_signal,
    f25rd_f25_content_rd_intensity_capexrev_step_z_252d_base_v132_signal,
    f25rd_f25_content_rd_intensity_rndassets_sl_126v504_base_v133_signal,
    f25rd_f25_content_rd_intensity_capexassets_sl_126v504_base_v134_signal,
    f25rd_f25_content_rd_intensity_sbcrnd_chg_63d_base_v135_signal,
    f25rd_f25_content_rd_intensity_reinv_convex_base_v136_signal,
    f25rd_f25_content_rd_intensity_rndrev_convex_base_v137_signal,
    f25rd_f25_content_rd_intensity_sbcreinv_rngpos_504d_base_v138_signal,
    f25rd_f25_content_rd_intensity_rndcapextilt_chg_63d_base_v139_signal,
    f25rd_f25_content_rd_intensity_sbcassets_disp_ema_base_v140_signal,
    f25rd_f25_content_rd_intensity_rndsbc_comove_252d_base_v141_signal,
    f25rd_f25_content_rd_intensity_capexrev_tanhz_252d_base_v142_signal,
    f25rd_f25_content_rd_intensity_reinv_tanhz_252d_base_v143_signal,
    f25rd_f25_content_rd_intensity_rndrev_sl_21v126_base_v144_signal,
    f25rd_f25_content_rd_intensity_sbcrev_convex_base_v145_signal,
    f25rd_f25_content_rd_intensity_rndassetsxreinv_z_252d_base_v146_signal,
    f25rd_f25_content_rd_intensity_capexassets_accelrank_504d_base_v147_signal,
    f25rd_f25_content_rd_intensity_reinvpersbc_accel_63d_base_v148_signal,
    f25rd_f25_content_rd_intensity_rndcapexbal_yoy_base_v149_signal,
    f25rd_f25_content_rd_intensity_rndpersbc_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_CONTENT_RD_INTENSITY_REGISTRY_076_150 = REGISTRY


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

    print("OK f25_content_rd_intensity_base_076_150_claude: %d features pass" % n_features)
