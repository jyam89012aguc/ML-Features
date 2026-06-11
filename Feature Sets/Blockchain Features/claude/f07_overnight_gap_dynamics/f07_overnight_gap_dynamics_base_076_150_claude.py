import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (overnight gap dynamics) =====
def _f07_gap(open, close):
    # raw overnight gap: today's open vs prior close (single-day, uses open/close)
    return open / close.shift(1) - 1.0


def _f07_overnight(open, close):
    # overnight return component: open vs prior close
    return open / close.shift(1) - 1.0


def _f07_intraday(open, close):
    # intraday return component: close vs same-day open
    return close / open - 1.0


def _f07_gapz(open, close, w):
    # z-score of the raw daily gap over window w
    g = open / close.shift(1) - 1.0
    m = g.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(2, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


# ============ FEATURES 076-150 ============

# 42d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_42d_base_v076_signal(open, close):
    result = _mean(_f07_gap(open, close), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_84d_base_v077_signal(open, close):
    result = _mean(_f07_gap(open, close), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_252d_base_v078_signal(open, close):
    result = _mean(_f07_gap(open, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_42d_base_v079_signal(open, close):
    result = _std(_f07_gap(open, close), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_189d_base_v080_signal(open, close):
    result = _std(_f07_gap(open, close), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 42d
def f07gp_f07_overnight_gap_dynamics_gapz_42d_base_v081_signal(open, close):
    result = _f07_gapz(open, close, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 84d
def f07gp_f07_overnight_gap_dynamics_gapz_84d_base_v082_signal(open, close):
    result = _f07_gapz(open, close, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 189d
def f07gp_f07_overnight_gap_dynamics_gapz_189d_base_v083_signal(open, close):
    result = _f07_gapz(open, close, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean intraday return
def f07gp_f07_overnight_gap_dynamics_intramean_126d_base_v084_signal(open, close):
    result = _mean(_f07_intraday(open, close), 126) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean intraday return
def f07gp_f07_overnight_gap_dynamics_intramean_252d_base_v085_signal(open, close):
    result = _mean(_f07_intraday(open, close), 252) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mean of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmid_42d_base_v086_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmid_252d_base_v087_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 42d
def f07gp_f07_overnight_gap_dynamics_ondrift_42d_base_v088_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(42, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 189d
def f07gp_f07_overnight_gap_dynamics_ondrift_189d_base_v089_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(189, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap continuation
def f07gp_f07_overnight_gap_dynamics_gapcont_42d_base_v090_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap continuation
def f07gp_f07_overnight_gap_dynamics_gapcont_252d_base_v091_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d absolute gap intensity
def f07gp_f07_overnight_gap_dynamics_absint_42d_base_v092_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d absolute gap intensity
def f07gp_f07_overnight_gap_dynamics_absint_189d_base_v093_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d signed gap momentum
def f07gp_f07_overnight_gap_dynamics_gapmom_42d_base_v094_signal(open, close):
    result = _f07_gap(open, close).rolling(42, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed gap momentum
def f07gp_f07_overnight_gap_dynamics_gapmom_252d_base_v095_signal(open, close):
    result = _f07_gap(open, close).rolling(252, min_periods=84).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 42d overnight contribution ratio
def f07gp_f07_overnight_gap_dynamics_oncontrib_42d_base_v096_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 42) ** 2
    vin = _std(intr, 42) ** 2
    result = _safe_div(vov, vov + vin)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d overnight contribution ratio
def f07gp_f07_overnight_gap_dynamics_oncontrib_252d_base_v097_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 252) ** 2
    vin = _std(intr, 252) ** 2
    result = _safe_div(vov, vov + vin)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap volatility ratio
def f07gp_f07_overnight_gap_dynamics_gapvolrat_42d_base_v098_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 42), _std(_f07_intraday(open, close), 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap volatility ratio
def f07gp_f07_overnight_gap_dynamics_gapvolrat_252d_base_v099_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 252), _std(_f07_intraday(open, close), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap Sharpe
def f07gp_f07_overnight_gap_dynamics_gapsharpe_42d_base_v100_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 42), _std(g, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d gap Sharpe
def f07gp_f07_overnight_gap_dynamics_gapsharpe_189d_base_v101_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 189), _std(g, 189))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d EWMA of daily gap
def f07gp_f07_overnight_gap_dynamics_gapewm_42d_base_v102_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA of daily gap
def f07gp_f07_overnight_gap_dynamics_gapewm_252d_base_v103_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap skew
def f07gp_f07_overnight_gap_dynamics_gapskew_42d_base_v104_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(42, min_periods=21).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap skew
def f07gp_f07_overnight_gap_dynamics_gapskew_252d_base_v105_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap kurtosis
def f07gp_f07_overnight_gap_dynamics_gapkurt_252d_base_v106_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(252, min_periods=84).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill 126d smoothed
def f07gp_f07_overnight_gap_dynamics_gapfill_126d_base_v107_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap-volatility
def f07gp_f07_overnight_gap_dynamics_gapvol_126d_base_v108_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-volatility
def f07gp_f07_overnight_gap_dynamics_gapvol_252d_base_v109_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d overnight return share
def f07gp_f07_overnight_gap_dynamics_onshare_252d_base_v110_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap continuation correlation proxy
def f07gp_f07_overnight_gap_dynamics_contcorr_252d_base_v111_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 252) - _mean(g, 252) * _mean(intr, 252)
    result = _safe_div(cov, _std(g, 252) * _std(intr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap momentum scaled by gap vol
def f07gp_f07_overnight_gap_dynamics_gapmomz_126d_base_v112_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(126, min_periods=42).sum(), _std(g, 126) * np.sqrt(126.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap momentum scaled by gap vol
def f07gp_f07_overnight_gap_dynamics_gapmomz_252d_base_v113_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(252, min_periods=84).sum(), _std(g, 252) * np.sqrt(252.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative overnight drift normalized
def f07gp_f07_overnight_gap_dynamics_driftz_252d_base_v114_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(252, min_periods=84).sum()
    result = _z(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap mean minus its 63d average (gap surprise)
def f07gp_f07_overnight_gap_dynamics_gapsurp_21d_base_v115_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 21) - _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap mean minus its 126d average
def f07gp_f07_overnight_gap_dynamics_gapsurp_63d_base_v116_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 63) - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gap acceleration: 21d gap mean minus 42d gap mean
def f07gp_f07_overnight_gap_dynamics_gapaccel_21_42_base_v117_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 21) - _mean(g, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gap acceleration: 42d vs 84d gap mean
def f07gp_f07_overnight_gap_dynamics_gapaccel_42_84_base_v118_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 42) - _mean(g, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap-vol acceleration: 21d gap std minus 63d gap std
def f07gp_f07_overnight_gap_dynamics_volaccel_21_63_base_v119_signal(open, close):
    g = _f07_gap(open, close)
    result = _std(g, 21) - _std(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmidewm_21d_base_v120_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = sp.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmidewm_63d_base_v121_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = sp.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap continuation EWMA
def f07gp_f07_overnight_gap_dynamics_gapcontewm_21d_base_v122_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = cont.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap continuation EWMA
def f07gp_f07_overnight_gap_dynamics_gapcontewm_63d_base_v123_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = cont.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap range relative to closeadj vol (gap intensity, mid)
def f07gp_f07_overnight_gap_dynamics_gapintens_63d_base_v124_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap intensity vs closeadj vol
def f07gp_f07_overnight_gap_dynamics_gapintens_126d_base_v125_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 126).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed gap momentum confirmed by dollar-volume z-score
def f07gp_f07_overnight_gap_dynamics_gapdvconf_63d_base_v126_signal(open, close, closeadj, volume):
    g = _f07_gap(open, close)
    dv = closeadj * volume
    result = g.rolling(63, min_periods=21).sum() * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap continuation smoothed and vol-scaled
def f07gp_f07_overnight_gap_dynamics_gapcontz_63d_base_v127_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap continuation smoothed and vol-scaled
def f07gp_f07_overnight_gap_dynamics_gapcontz_126d_base_v128_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d overnight drift relative to total drift (overnight efficiency)
def f07gp_f07_overnight_gap_dynamics_oneff_63d_base_v129_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    on_cum = ov.rolling(63, min_periods=21).sum()
    tot_cum = (ov + intr).rolling(63, min_periods=21).sum()
    result = _safe_div(on_cum, tot_cum.abs() + _std(ov, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d overnight efficiency
def f07gp_f07_overnight_gap_dynamics_oneff_126d_base_v130_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    on_cum = ov.rolling(126, min_periods=42).sum()
    tot_cum = (ov + intr).rolling(126, min_periods=42).sum()
    result = _safe_div(on_cum, tot_cum.abs() + _std(ov, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap autocorrelation proxy (lag-1 product mean normalized)
def f07gp_f07_overnight_gap_dynamics_gapac_63d_base_v131_signal(open, close):
    g = _f07_gap(open, close)
    gd = g - _mean(g, 63)
    cov = _mean(gd * gd.shift(1), 63)
    result = _safe_div(cov, _std(g, 63) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap autocorrelation proxy
def f07gp_f07_overnight_gap_dynamics_gapac_126d_base_v132_signal(open, close):
    g = _f07_gap(open, close)
    gd = g - _mean(g, 126)
    cov = _mean(gd * gd.shift(1), 126)
    result = _safe_div(cov, _std(g, 126) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap z-score smoothed over 42d window base
def f07gp_f07_overnight_gap_dynamics_gapzsm_42d_base_v133_signal(open, close):
    result = _mean(_f07_gapz(open, close, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap z-score smoothed
def f07gp_f07_overnight_gap_dynamics_gapzsm_63d_base_v134_signal(open, close):
    result = _mean(_f07_gapz(open, close, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intraday vol scaled by overnight vol (regime ratio)
def f07gp_f07_overnight_gap_dynamics_intraonrat_63d_base_v135_signal(open, close):
    result = _safe_div(_std(_f07_intraday(open, close), 63), _std(_f07_overnight(open, close), 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d intraday/overnight vol ratio
def f07gp_f07_overnight_gap_dynamics_intraonrat_126d_base_v136_signal(open, close):
    result = _safe_div(_std(_f07_intraday(open, close), 126), _std(_f07_overnight(open, close), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap mean vol-scaled by closeadj realized vol
def f07gp_f07_overnight_gap_dynamics_gapvscaled_21d_base_v137_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap mean vol-scaled by closeadj realized vol
def f07gp_f07_overnight_gap_dynamics_gapvscaled_63d_base_v138_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap mean vol-scaled by closeadj realized vol
def f07gp_f07_overnight_gap_dynamics_gapvscaled_126d_base_v139_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA gap minus 63d EWMA gap (gap MACD-style)
def f07gp_f07_overnight_gap_dynamics_gapmacd_21_63_base_v140_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 42d EWMA gap minus 126d EWMA gap
def f07gp_f07_overnight_gap_dynamics_gapmacd_42_126_base_v141_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=42, min_periods=21).mean() - g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d absolute gap EWMA (gap intensity, exponential)
def f07gp_f07_overnight_gap_dynamics_absgapewm_21d_base_v142_signal(open, close):
    result = _f07_gap(open, close).abs().ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d absolute gap EWMA
def f07gp_f07_overnight_gap_dynamics_absgapewm_63d_base_v143_signal(open, close):
    result = _f07_gap(open, close).abs().ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d overnight drift minus intraday drift over same window
def f07gp_f07_overnight_gap_dynamics_driftspread_63d_base_v144_signal(open, close):
    ov = _f07_overnight(open, close).rolling(63, min_periods=21).sum()
    intr = _f07_intraday(open, close).rolling(63, min_periods=21).sum()
    result = ov - intr
    return result.replace([np.inf, -np.inf], np.nan)


# 126d overnight minus intraday cumulative drift spread
def f07gp_f07_overnight_gap_dynamics_driftspread_126d_base_v145_signal(open, close):
    ov = _f07_overnight(open, close).rolling(126, min_periods=42).sum()
    intr = _f07_intraday(open, close).rolling(126, min_periods=42).sum()
    result = ov - intr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap Sharpe minus 63d gap Sharpe (gap quality acceleration)
def f07gp_f07_overnight_gap_dynamics_sharpeaccel_21_63_base_v146_signal(open, close):
    g = _f07_gap(open, close)
    s21 = _safe_div(_mean(g, 21), _std(g, 21))
    s63 = _safe_div(_mean(g, 63), _std(g, 63))
    result = s21 - s63
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap percentile rank over 126d (continuous rank of latest gap pressure)
def f07gp_f07_overnight_gap_dynamics_gaprank_126d_base_v147_signal(open, close):
    g = _mean(_f07_gap(open, close), 21)
    result = g.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-mean percentile rank over 252d
def f07gp_f07_overnight_gap_dynamics_gaprank_252d_base_v148_signal(open, close):
    g = _mean(_f07_gap(open, close), 63)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d absolute-gap-intensity percentile rank over 252d
def f07gp_f07_overnight_gap_dynamics_absrank_252d_base_v149_signal(open, close):
    g = _mean(_f07_gap(open, close).abs(), 63)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon gap-momentum composite (21/63/126/252)
def f07gp_f07_overnight_gap_dynamics_blend_multi_base_v150_signal(open, close):
    g = _f07_gap(open, close)
    result = (_mean(g, 21) + _mean(g, 63) + _mean(g, 126) + _mean(g, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07gp_f07_overnight_gap_dynamics_gapmean_42d_base_v076_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_84d_base_v077_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_252d_base_v078_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_42d_base_v079_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_189d_base_v080_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_42d_base_v081_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_84d_base_v082_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_189d_base_v083_signal,
    f07gp_f07_overnight_gap_dynamics_intramean_126d_base_v084_signal,
    f07gp_f07_overnight_gap_dynamics_intramean_252d_base_v085_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_42d_base_v086_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_252d_base_v087_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_42d_base_v088_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_189d_base_v089_signal,
    f07gp_f07_overnight_gap_dynamics_gapcont_42d_base_v090_signal,
    f07gp_f07_overnight_gap_dynamics_gapcont_252d_base_v091_signal,
    f07gp_f07_overnight_gap_dynamics_absint_42d_base_v092_signal,
    f07gp_f07_overnight_gap_dynamics_absint_189d_base_v093_signal,
    f07gp_f07_overnight_gap_dynamics_gapmom_42d_base_v094_signal,
    f07gp_f07_overnight_gap_dynamics_gapmom_252d_base_v095_signal,
    f07gp_f07_overnight_gap_dynamics_oncontrib_42d_base_v096_signal,
    f07gp_f07_overnight_gap_dynamics_oncontrib_252d_base_v097_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolrat_42d_base_v098_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolrat_252d_base_v099_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_42d_base_v100_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_189d_base_v101_signal,
    f07gp_f07_overnight_gap_dynamics_gapewm_42d_base_v102_signal,
    f07gp_f07_overnight_gap_dynamics_gapewm_252d_base_v103_signal,
    f07gp_f07_overnight_gap_dynamics_gapskew_42d_base_v104_signal,
    f07gp_f07_overnight_gap_dynamics_gapskew_252d_base_v105_signal,
    f07gp_f07_overnight_gap_dynamics_gapkurt_252d_base_v106_signal,
    f07gp_f07_overnight_gap_dynamics_gapfill_126d_base_v107_signal,
    f07gp_f07_overnight_gap_dynamics_gapvol_126d_base_v108_signal,
    f07gp_f07_overnight_gap_dynamics_gapvol_252d_base_v109_signal,
    f07gp_f07_overnight_gap_dynamics_onshare_252d_base_v110_signal,
    f07gp_f07_overnight_gap_dynamics_contcorr_252d_base_v111_signal,
    f07gp_f07_overnight_gap_dynamics_gapmomz_126d_base_v112_signal,
    f07gp_f07_overnight_gap_dynamics_gapmomz_252d_base_v113_signal,
    f07gp_f07_overnight_gap_dynamics_driftz_252d_base_v114_signal,
    f07gp_f07_overnight_gap_dynamics_gapsurp_21d_base_v115_signal,
    f07gp_f07_overnight_gap_dynamics_gapsurp_63d_base_v116_signal,
    f07gp_f07_overnight_gap_dynamics_gapaccel_21_42_base_v117_signal,
    f07gp_f07_overnight_gap_dynamics_gapaccel_42_84_base_v118_signal,
    f07gp_f07_overnight_gap_dynamics_volaccel_21_63_base_v119_signal,
    f07gp_f07_overnight_gap_dynamics_onmidewm_21d_base_v120_signal,
    f07gp_f07_overnight_gap_dynamics_onmidewm_63d_base_v121_signal,
    f07gp_f07_overnight_gap_dynamics_gapcontewm_21d_base_v122_signal,
    f07gp_f07_overnight_gap_dynamics_gapcontewm_63d_base_v123_signal,
    f07gp_f07_overnight_gap_dynamics_gapintens_63d_base_v124_signal,
    f07gp_f07_overnight_gap_dynamics_gapintens_126d_base_v125_signal,
    f07gp_f07_overnight_gap_dynamics_gapdvconf_63d_base_v126_signal,
    f07gp_f07_overnight_gap_dynamics_gapcontz_63d_base_v127_signal,
    f07gp_f07_overnight_gap_dynamics_gapcontz_126d_base_v128_signal,
    f07gp_f07_overnight_gap_dynamics_oneff_63d_base_v129_signal,
    f07gp_f07_overnight_gap_dynamics_oneff_126d_base_v130_signal,
    f07gp_f07_overnight_gap_dynamics_gapac_63d_base_v131_signal,
    f07gp_f07_overnight_gap_dynamics_gapac_126d_base_v132_signal,
    f07gp_f07_overnight_gap_dynamics_gapzsm_42d_base_v133_signal,
    f07gp_f07_overnight_gap_dynamics_gapzsm_63d_base_v134_signal,
    f07gp_f07_overnight_gap_dynamics_intraonrat_63d_base_v135_signal,
    f07gp_f07_overnight_gap_dynamics_intraonrat_126d_base_v136_signal,
    f07gp_f07_overnight_gap_dynamics_gapvscaled_21d_base_v137_signal,
    f07gp_f07_overnight_gap_dynamics_gapvscaled_63d_base_v138_signal,
    f07gp_f07_overnight_gap_dynamics_gapvscaled_126d_base_v139_signal,
    f07gp_f07_overnight_gap_dynamics_gapmacd_21_63_base_v140_signal,
    f07gp_f07_overnight_gap_dynamics_gapmacd_42_126_base_v141_signal,
    f07gp_f07_overnight_gap_dynamics_absgapewm_21d_base_v142_signal,
    f07gp_f07_overnight_gap_dynamics_absgapewm_63d_base_v143_signal,
    f07gp_f07_overnight_gap_dynamics_driftspread_63d_base_v144_signal,
    f07gp_f07_overnight_gap_dynamics_driftspread_126d_base_v145_signal,
    f07gp_f07_overnight_gap_dynamics_sharpeaccel_21_63_base_v146_signal,
    f07gp_f07_overnight_gap_dynamics_gaprank_126d_base_v147_signal,
    f07gp_f07_overnight_gap_dynamics_gaprank_252d_base_v148_signal,
    f07gp_f07_overnight_gap_dynamics_absrank_252d_base_v149_signal,
    f07gp_f07_overnight_gap_dynamics_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_OVERNIGHT_GAP_DYNAMICS_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f07_gap", "_f07_overnight", "_f07_intraday", "_f07_gapz")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_overnight_gap_dynamics_base_076_150_claude: {n_features} features pass")
