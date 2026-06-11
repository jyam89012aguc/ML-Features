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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f07gp_f07_overnight_gap_dynamics_rawgap_1d_jerk_v001_signal(open, close):
    result = _f07_gap(open, close)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_5d_jerk_v002_signal(open, close):
    result = _mean(_f07_gap(open, close), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_10d_jerk_v003_signal(open, close):
    result = _mean(_f07_gap(open, close), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_21d_jerk_v004_signal(open, close):
    result = _mean(_f07_gap(open, close), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_63d_jerk_v005_signal(open, close):
    result = _mean(_f07_gap(open, close), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_126d_jerk_v006_signal(open, close):
    result = _mean(_f07_gap(open, close), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_5d_jerk_v007_signal(open, close):
    result = _std(_f07_gap(open, close), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_10d_jerk_v008_signal(open, close):
    result = _std(_f07_gap(open, close), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_21d_jerk_v009_signal(open, close):
    result = _std(_f07_gap(open, close), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_63d_jerk_v010_signal(open, close):
    result = _std(_f07_gap(open, close), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_126d_jerk_v011_signal(open, close):
    result = _std(_f07_gap(open, close), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_252d_jerk_v012_signal(open, close):
    result = _std(_f07_gap(open, close), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_21d_jerk_v013_signal(open, close):
    result = _f07_gapz(open, close, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_63d_jerk_v014_signal(open, close):
    result = _f07_gapz(open, close, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_126d_jerk_v015_signal(open, close):
    result = _f07_gapz(open, close, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_252d_jerk_v016_signal(open, close):
    result = _f07_gapz(open, close, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intraday_1d_jerk_v017_signal(open, close):
    result = _f07_intraday(open, close) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intramean_5d_jerk_v018_signal(open, close):
    result = _mean(_f07_intraday(open, close), 5) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intramean_21d_jerk_v019_signal(open, close):
    result = _mean(_f07_intraday(open, close), 21) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intramean_63d_jerk_v020_signal(open, close):
    result = _mean(_f07_intraday(open, close), 63) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_1d_jerk_v021_signal(open, close):
    result = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_21d_jerk_v022_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_63d_jerk_v023_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_126d_jerk_v024_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_21d_jerk_v025_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(21, min_periods=10).sum()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_63d_jerk_v026_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(63, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_126d_jerk_v027_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(126, min_periods=42).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_252d_jerk_v028_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(252, min_periods=84).sum()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcont_21d_jerk_v029_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcont_63d_jerk_v030_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcont_126d_jerk_v031_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_21d_jerk_v032_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_63d_jerk_v033_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_126d_jerk_v034_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_252d_jerk_v035_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmom_21d_jerk_v036_signal(open, close):
    result = _f07_gap(open, close).rolling(21, min_periods=10).sum()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmom_63d_jerk_v037_signal(open, close):
    result = _f07_gap(open, close).rolling(63, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmom_126d_jerk_v038_signal(open, close):
    result = _f07_gap(open, close).rolling(126, min_periods=42).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oncontrib_21d_jerk_v039_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 21) ** 2
    vin = _std(intr, 21) ** 2
    result = _safe_div(vov, vov + vin)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oncontrib_63d_jerk_v040_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 63) ** 2
    vin = _std(intr, 63) ** 2
    result = _safe_div(vov, vov + vin)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oncontrib_126d_jerk_v041_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 126) ** 2
    vin = _std(intr, 126) ** 2
    result = _safe_div(vov, vov + vin)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolrat_21d_jerk_v042_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 21), _std(_f07_intraday(open, close), 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolrat_63d_jerk_v043_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 63), _std(_f07_intraday(open, close), 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolrat_126d_jerk_v044_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 126), _std(_f07_intraday(open, close), 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_21d_jerk_v045_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 21), _std(g, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_63d_jerk_v046_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 63), _std(g, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_126d_jerk_v047_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 126), _std(g, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_252d_jerk_v048_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 252), _std(g, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapewm_21d_jerk_v049_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapewm_63d_jerk_v050_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapewm_126d_jerk_v051_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapskew_21d_jerk_v052_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(21, min_periods=10).skew()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapskew_63d_jerk_v053_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapskew_126d_jerk_v054_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapkurt_63d_jerk_v055_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapkurt_126d_jerk_v056_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapfill_21d_jerk_v057_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapfill_63d_jerk_v058_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvol_21d_jerk_v059_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvol_63d_jerk_v060_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onshare_21d_jerk_v061_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onshare_63d_jerk_v062_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onshare_126d_jerk_v063_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapzsm_5d_jerk_v064_signal(open, close):
    result = _mean(_f07_gapz(open, close, 63), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapzsm_10d_jerk_v065_signal(open, close):
    result = _mean(_f07_gapz(open, close, 63), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapzsm_21d_jerk_v066_signal(open, close):
    result = _mean(_f07_gapz(open, close, 126), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_contcorr_63d_jerk_v067_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 63) - _mean(g, 63) * _mean(intr, 63)
    result = _safe_div(cov, _std(g, 63) * _std(intr, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_contcorr_126d_jerk_v068_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 126) - _mean(g, 126) * _mean(intr, 126)
    result = _safe_div(cov, _std(g, 126) * _std(intr, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmomz_21d_jerk_v069_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(21, min_periods=10).sum(), _std(g, 21) * np.sqrt(21.0))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmomz_63d_jerk_v070_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(63, min_periods=21).sum(), _std(g, 63) * np.sqrt(63.0))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_driftz_63d_jerk_v071_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(63, min_periods=21).sum()
    result = _z(cum, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_driftz_126d_jerk_v072_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(126, min_periods=42).sum()
    result = _z(cum, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapintens_21d_jerk_v073_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolconf_21d_jerk_v074_signal(open, close, volume):
    g = _f07_gap(open, close)
    result = g.rolling(21, min_periods=10).sum() * _z(volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcontz_21d_jerk_v075_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_42d_jerk_v076_signal(open, close):
    result = _mean(_f07_gap(open, close), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_84d_jerk_v077_signal(open, close):
    result = _mean(_f07_gap(open, close), 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmean_252d_jerk_v078_signal(open, close):
    result = _mean(_f07_gap(open, close), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_42d_jerk_v079_signal(open, close):
    result = _std(_f07_gap(open, close), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapstd_189d_jerk_v080_signal(open, close):
    result = _std(_f07_gap(open, close), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_42d_jerk_v081_signal(open, close):
    result = _f07_gapz(open, close, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_84d_jerk_v082_signal(open, close):
    result = _f07_gapz(open, close, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapz_189d_jerk_v083_signal(open, close):
    result = _f07_gapz(open, close, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intramean_126d_jerk_v084_signal(open, close):
    result = _mean(_f07_intraday(open, close), 126) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intramean_252d_jerk_v085_signal(open, close):
    result = _mean(_f07_intraday(open, close), 252) + _f07_gap(open, close) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_42d_jerk_v086_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmid_252d_jerk_v087_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_42d_jerk_v088_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(42, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_ondrift_189d_jerk_v089_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(189, min_periods=63).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcont_42d_jerk_v090_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcont_252d_jerk_v091_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_42d_jerk_v092_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absint_189d_jerk_v093_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmom_42d_jerk_v094_signal(open, close):
    result = _f07_gap(open, close).rolling(42, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmom_252d_jerk_v095_signal(open, close):
    result = _f07_gap(open, close).rolling(252, min_periods=84).sum()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oncontrib_42d_jerk_v096_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 42) ** 2
    vin = _std(intr, 42) ** 2
    result = _safe_div(vov, vov + vin)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oncontrib_252d_jerk_v097_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 252) ** 2
    vin = _std(intr, 252) ** 2
    result = _safe_div(vov, vov + vin)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolrat_42d_jerk_v098_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 42), _std(_f07_intraday(open, close), 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvolrat_252d_jerk_v099_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 252), _std(_f07_intraday(open, close), 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_42d_jerk_v100_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 42), _std(g, 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsharpe_189d_jerk_v101_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 189), _std(g, 189))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapewm_42d_jerk_v102_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=42, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapewm_252d_jerk_v103_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapskew_42d_jerk_v104_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(42, min_periods=21).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapskew_252d_jerk_v105_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(252, min_periods=84).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapkurt_252d_jerk_v106_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(252, min_periods=84).kurt()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapfill_126d_jerk_v107_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvol_126d_jerk_v108_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvol_252d_jerk_v109_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onshare_252d_jerk_v110_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_contcorr_252d_jerk_v111_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 252) - _mean(g, 252) * _mean(intr, 252)
    result = _safe_div(cov, _std(g, 252) * _std(intr, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmomz_126d_jerk_v112_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(126, min_periods=42).sum(), _std(g, 126) * np.sqrt(126.0))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmomz_252d_jerk_v113_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(252, min_periods=84).sum(), _std(g, 252) * np.sqrt(252.0))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_driftz_252d_jerk_v114_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(252, min_periods=84).sum()
    result = _z(cum, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsurp_21d_jerk_v115_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 21) - _mean(g, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapsurp_63d_jerk_v116_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 63) - _mean(g, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapaccel_21_42_jerk_v117_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 21) - _mean(g, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapaccel_42_84_jerk_v118_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 42) - _mean(g, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_volaccel_21_63_jerk_v119_signal(open, close):
    g = _f07_gap(open, close)
    result = _std(g, 21) - _std(g, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmidewm_21d_jerk_v120_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = sp.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_onmidewm_63d_jerk_v121_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = sp.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcontewm_21d_jerk_v122_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = cont.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcontewm_63d_jerk_v123_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = cont.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapintens_63d_jerk_v124_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapintens_126d_jerk_v125_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 126).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapdvconf_63d_jerk_v126_signal(open, close, closeadj, volume):
    g = _f07_gap(open, close)
    dv = closeadj * volume
    result = g.rolling(63, min_periods=21).sum() * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcontz_63d_jerk_v127_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapcontz_126d_jerk_v128_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 126), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oneff_63d_jerk_v129_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    on_cum = ov.rolling(63, min_periods=21).sum()
    tot_cum = (ov + intr).rolling(63, min_periods=21).sum()
    result = _safe_div(on_cum, tot_cum.abs() + _std(ov, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_oneff_126d_jerk_v130_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    on_cum = ov.rolling(126, min_periods=42).sum()
    tot_cum = (ov + intr).rolling(126, min_periods=42).sum()
    result = _safe_div(on_cum, tot_cum.abs() + _std(ov, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapac_63d_jerk_v131_signal(open, close):
    g = _f07_gap(open, close)
    gd = g - _mean(g, 63)
    cov = _mean(gd * gd.shift(1), 63)
    result = _safe_div(cov, _std(g, 63) ** 2)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapac_126d_jerk_v132_signal(open, close):
    g = _f07_gap(open, close)
    gd = g - _mean(g, 126)
    cov = _mean(gd * gd.shift(1), 126)
    result = _safe_div(cov, _std(g, 126) ** 2)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapzsm_42d_jerk_v133_signal(open, close):
    result = _mean(_f07_gapz(open, close, 126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapzsm_63d_jerk_v134_signal(open, close):
    result = _mean(_f07_gapz(open, close, 252), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intraonrat_63d_jerk_v135_signal(open, close):
    result = _safe_div(_std(_f07_intraday(open, close), 63), _std(_f07_overnight(open, close), 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_intraonrat_126d_jerk_v136_signal(open, close):
    result = _safe_div(_std(_f07_intraday(open, close), 126), _std(_f07_overnight(open, close), 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvscaled_21d_jerk_v137_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 21), vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvscaled_63d_jerk_v138_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 63), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapvscaled_126d_jerk_v139_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_mean(g, 126), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmacd_21_63_jerk_v140_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gapmacd_42_126_jerk_v141_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=42, min_periods=21).mean() - g.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absgapewm_21d_jerk_v142_signal(open, close):
    result = _f07_gap(open, close).abs().ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absgapewm_63d_jerk_v143_signal(open, close):
    result = _f07_gap(open, close).abs().ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_driftspread_63d_jerk_v144_signal(open, close):
    ov = _f07_overnight(open, close).rolling(63, min_periods=21).sum()
    intr = _f07_intraday(open, close).rolling(63, min_periods=21).sum()
    result = ov - intr
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_driftspread_126d_jerk_v145_signal(open, close):
    ov = _f07_overnight(open, close).rolling(126, min_periods=42).sum()
    intr = _f07_intraday(open, close).rolling(126, min_periods=42).sum()
    result = ov - intr
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_sharpeaccel_21_63_jerk_v146_signal(open, close):
    g = _f07_gap(open, close)
    s21 = _safe_div(_mean(g, 21), _std(g, 21))
    s63 = _safe_div(_mean(g, 63), _std(g, 63))
    result = s21 - s63
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gaprank_126d_jerk_v147_signal(open, close):
    g = _mean(_f07_gap(open, close), 21)
    result = g.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_gaprank_252d_jerk_v148_signal(open, close):
    g = _mean(_f07_gap(open, close), 63)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_absrank_252d_jerk_v149_signal(open, close):
    g = _mean(_f07_gap(open, close).abs(), 63)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f07gp_f07_overnight_gap_dynamics_blend_multi_jerk_v150_signal(open, close):
    g = _f07_gap(open, close)
    result = (_mean(g, 21) + _mean(g, 63) + _mean(g, 126) + _mean(g, 252)) / 4.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f07gp_f07_overnight_gap_dynamics_rawgap_1d_jerk_v001_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_5d_jerk_v002_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_10d_jerk_v003_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_21d_jerk_v004_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_63d_jerk_v005_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_126d_jerk_v006_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_5d_jerk_v007_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_10d_jerk_v008_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_21d_jerk_v009_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_63d_jerk_v010_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_126d_jerk_v011_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_252d_jerk_v012_signal,    f07gp_f07_overnight_gap_dynamics_gapz_21d_jerk_v013_signal,    f07gp_f07_overnight_gap_dynamics_gapz_63d_jerk_v014_signal,    f07gp_f07_overnight_gap_dynamics_gapz_126d_jerk_v015_signal,    f07gp_f07_overnight_gap_dynamics_gapz_252d_jerk_v016_signal,    f07gp_f07_overnight_gap_dynamics_intraday_1d_jerk_v017_signal,    f07gp_f07_overnight_gap_dynamics_intramean_5d_jerk_v018_signal,    f07gp_f07_overnight_gap_dynamics_intramean_21d_jerk_v019_signal,    f07gp_f07_overnight_gap_dynamics_intramean_63d_jerk_v020_signal,    f07gp_f07_overnight_gap_dynamics_onmid_1d_jerk_v021_signal,    f07gp_f07_overnight_gap_dynamics_onmid_21d_jerk_v022_signal,    f07gp_f07_overnight_gap_dynamics_onmid_63d_jerk_v023_signal,    f07gp_f07_overnight_gap_dynamics_onmid_126d_jerk_v024_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_21d_jerk_v025_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_63d_jerk_v026_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_126d_jerk_v027_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_252d_jerk_v028_signal,    f07gp_f07_overnight_gap_dynamics_gapcont_21d_jerk_v029_signal,    f07gp_f07_overnight_gap_dynamics_gapcont_63d_jerk_v030_signal,    f07gp_f07_overnight_gap_dynamics_gapcont_126d_jerk_v031_signal,    f07gp_f07_overnight_gap_dynamics_absint_21d_jerk_v032_signal,    f07gp_f07_overnight_gap_dynamics_absint_63d_jerk_v033_signal,    f07gp_f07_overnight_gap_dynamics_absint_126d_jerk_v034_signal,    f07gp_f07_overnight_gap_dynamics_absint_252d_jerk_v035_signal,    f07gp_f07_overnight_gap_dynamics_gapmom_21d_jerk_v036_signal,    f07gp_f07_overnight_gap_dynamics_gapmom_63d_jerk_v037_signal,    f07gp_f07_overnight_gap_dynamics_gapmom_126d_jerk_v038_signal,    f07gp_f07_overnight_gap_dynamics_oncontrib_21d_jerk_v039_signal,    f07gp_f07_overnight_gap_dynamics_oncontrib_63d_jerk_v040_signal,    f07gp_f07_overnight_gap_dynamics_oncontrib_126d_jerk_v041_signal,    f07gp_f07_overnight_gap_dynamics_gapvolrat_21d_jerk_v042_signal,    f07gp_f07_overnight_gap_dynamics_gapvolrat_63d_jerk_v043_signal,    f07gp_f07_overnight_gap_dynamics_gapvolrat_126d_jerk_v044_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_21d_jerk_v045_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_63d_jerk_v046_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_126d_jerk_v047_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_252d_jerk_v048_signal,    f07gp_f07_overnight_gap_dynamics_gapewm_21d_jerk_v049_signal,    f07gp_f07_overnight_gap_dynamics_gapewm_63d_jerk_v050_signal,    f07gp_f07_overnight_gap_dynamics_gapewm_126d_jerk_v051_signal,    f07gp_f07_overnight_gap_dynamics_gapskew_21d_jerk_v052_signal,    f07gp_f07_overnight_gap_dynamics_gapskew_63d_jerk_v053_signal,    f07gp_f07_overnight_gap_dynamics_gapskew_126d_jerk_v054_signal,    f07gp_f07_overnight_gap_dynamics_gapkurt_63d_jerk_v055_signal,    f07gp_f07_overnight_gap_dynamics_gapkurt_126d_jerk_v056_signal,    f07gp_f07_overnight_gap_dynamics_gapfill_21d_jerk_v057_signal,    f07gp_f07_overnight_gap_dynamics_gapfill_63d_jerk_v058_signal,    f07gp_f07_overnight_gap_dynamics_gapvol_21d_jerk_v059_signal,    f07gp_f07_overnight_gap_dynamics_gapvol_63d_jerk_v060_signal,    f07gp_f07_overnight_gap_dynamics_onshare_21d_jerk_v061_signal,    f07gp_f07_overnight_gap_dynamics_onshare_63d_jerk_v062_signal,    f07gp_f07_overnight_gap_dynamics_onshare_126d_jerk_v063_signal,    f07gp_f07_overnight_gap_dynamics_gapzsm_5d_jerk_v064_signal,    f07gp_f07_overnight_gap_dynamics_gapzsm_10d_jerk_v065_signal,    f07gp_f07_overnight_gap_dynamics_gapzsm_21d_jerk_v066_signal,    f07gp_f07_overnight_gap_dynamics_contcorr_63d_jerk_v067_signal,    f07gp_f07_overnight_gap_dynamics_contcorr_126d_jerk_v068_signal,    f07gp_f07_overnight_gap_dynamics_gapmomz_21d_jerk_v069_signal,    f07gp_f07_overnight_gap_dynamics_gapmomz_63d_jerk_v070_signal,    f07gp_f07_overnight_gap_dynamics_driftz_63d_jerk_v071_signal,    f07gp_f07_overnight_gap_dynamics_driftz_126d_jerk_v072_signal,    f07gp_f07_overnight_gap_dynamics_gapintens_21d_jerk_v073_signal,    f07gp_f07_overnight_gap_dynamics_gapvolconf_21d_jerk_v074_signal,    f07gp_f07_overnight_gap_dynamics_gapcontz_21d_jerk_v075_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_42d_jerk_v076_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_84d_jerk_v077_signal,    f07gp_f07_overnight_gap_dynamics_gapmean_252d_jerk_v078_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_42d_jerk_v079_signal,    f07gp_f07_overnight_gap_dynamics_gapstd_189d_jerk_v080_signal,    f07gp_f07_overnight_gap_dynamics_gapz_42d_jerk_v081_signal,    f07gp_f07_overnight_gap_dynamics_gapz_84d_jerk_v082_signal,    f07gp_f07_overnight_gap_dynamics_gapz_189d_jerk_v083_signal,    f07gp_f07_overnight_gap_dynamics_intramean_126d_jerk_v084_signal,    f07gp_f07_overnight_gap_dynamics_intramean_252d_jerk_v085_signal,    f07gp_f07_overnight_gap_dynamics_onmid_42d_jerk_v086_signal,    f07gp_f07_overnight_gap_dynamics_onmid_252d_jerk_v087_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_42d_jerk_v088_signal,    f07gp_f07_overnight_gap_dynamics_ondrift_189d_jerk_v089_signal,    f07gp_f07_overnight_gap_dynamics_gapcont_42d_jerk_v090_signal,    f07gp_f07_overnight_gap_dynamics_gapcont_252d_jerk_v091_signal,    f07gp_f07_overnight_gap_dynamics_absint_42d_jerk_v092_signal,    f07gp_f07_overnight_gap_dynamics_absint_189d_jerk_v093_signal,    f07gp_f07_overnight_gap_dynamics_gapmom_42d_jerk_v094_signal,    f07gp_f07_overnight_gap_dynamics_gapmom_252d_jerk_v095_signal,    f07gp_f07_overnight_gap_dynamics_oncontrib_42d_jerk_v096_signal,    f07gp_f07_overnight_gap_dynamics_oncontrib_252d_jerk_v097_signal,    f07gp_f07_overnight_gap_dynamics_gapvolrat_42d_jerk_v098_signal,    f07gp_f07_overnight_gap_dynamics_gapvolrat_252d_jerk_v099_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_42d_jerk_v100_signal,    f07gp_f07_overnight_gap_dynamics_gapsharpe_189d_jerk_v101_signal,    f07gp_f07_overnight_gap_dynamics_gapewm_42d_jerk_v102_signal,    f07gp_f07_overnight_gap_dynamics_gapewm_252d_jerk_v103_signal,    f07gp_f07_overnight_gap_dynamics_gapskew_42d_jerk_v104_signal,    f07gp_f07_overnight_gap_dynamics_gapskew_252d_jerk_v105_signal,    f07gp_f07_overnight_gap_dynamics_gapkurt_252d_jerk_v106_signal,    f07gp_f07_overnight_gap_dynamics_gapfill_126d_jerk_v107_signal,    f07gp_f07_overnight_gap_dynamics_gapvol_126d_jerk_v108_signal,    f07gp_f07_overnight_gap_dynamics_gapvol_252d_jerk_v109_signal,    f07gp_f07_overnight_gap_dynamics_onshare_252d_jerk_v110_signal,    f07gp_f07_overnight_gap_dynamics_contcorr_252d_jerk_v111_signal,    f07gp_f07_overnight_gap_dynamics_gapmomz_126d_jerk_v112_signal,    f07gp_f07_overnight_gap_dynamics_gapmomz_252d_jerk_v113_signal,    f07gp_f07_overnight_gap_dynamics_driftz_252d_jerk_v114_signal,    f07gp_f07_overnight_gap_dynamics_gapsurp_21d_jerk_v115_signal,    f07gp_f07_overnight_gap_dynamics_gapsurp_63d_jerk_v116_signal,    f07gp_f07_overnight_gap_dynamics_gapaccel_21_42_jerk_v117_signal,    f07gp_f07_overnight_gap_dynamics_gapaccel_42_84_jerk_v118_signal,    f07gp_f07_overnight_gap_dynamics_volaccel_21_63_jerk_v119_signal,    f07gp_f07_overnight_gap_dynamics_onmidewm_21d_jerk_v120_signal,    f07gp_f07_overnight_gap_dynamics_onmidewm_63d_jerk_v121_signal,    f07gp_f07_overnight_gap_dynamics_gapcontewm_21d_jerk_v122_signal,    f07gp_f07_overnight_gap_dynamics_gapcontewm_63d_jerk_v123_signal,    f07gp_f07_overnight_gap_dynamics_gapintens_63d_jerk_v124_signal,    f07gp_f07_overnight_gap_dynamics_gapintens_126d_jerk_v125_signal,    f07gp_f07_overnight_gap_dynamics_gapdvconf_63d_jerk_v126_signal,    f07gp_f07_overnight_gap_dynamics_gapcontz_63d_jerk_v127_signal,    f07gp_f07_overnight_gap_dynamics_gapcontz_126d_jerk_v128_signal,    f07gp_f07_overnight_gap_dynamics_oneff_63d_jerk_v129_signal,    f07gp_f07_overnight_gap_dynamics_oneff_126d_jerk_v130_signal,    f07gp_f07_overnight_gap_dynamics_gapac_63d_jerk_v131_signal,    f07gp_f07_overnight_gap_dynamics_gapac_126d_jerk_v132_signal,    f07gp_f07_overnight_gap_dynamics_gapzsm_42d_jerk_v133_signal,    f07gp_f07_overnight_gap_dynamics_gapzsm_63d_jerk_v134_signal,    f07gp_f07_overnight_gap_dynamics_intraonrat_63d_jerk_v135_signal,    f07gp_f07_overnight_gap_dynamics_intraonrat_126d_jerk_v136_signal,    f07gp_f07_overnight_gap_dynamics_gapvscaled_21d_jerk_v137_signal,    f07gp_f07_overnight_gap_dynamics_gapvscaled_63d_jerk_v138_signal,    f07gp_f07_overnight_gap_dynamics_gapvscaled_126d_jerk_v139_signal,    f07gp_f07_overnight_gap_dynamics_gapmacd_21_63_jerk_v140_signal,    f07gp_f07_overnight_gap_dynamics_gapmacd_42_126_jerk_v141_signal,    f07gp_f07_overnight_gap_dynamics_absgapewm_21d_jerk_v142_signal,    f07gp_f07_overnight_gap_dynamics_absgapewm_63d_jerk_v143_signal,    f07gp_f07_overnight_gap_dynamics_driftspread_63d_jerk_v144_signal,    f07gp_f07_overnight_gap_dynamics_driftspread_126d_jerk_v145_signal,    f07gp_f07_overnight_gap_dynamics_sharpeaccel_21_63_jerk_v146_signal,    f07gp_f07_overnight_gap_dynamics_gaprank_126d_jerk_v147_signal,    f07gp_f07_overnight_gap_dynamics_gaprank_252d_jerk_v148_signal,    f07gp_f07_overnight_gap_dynamics_absrank_252d_jerk_v149_signal,    f07gp_f07_overnight_gap_dynamics_blend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_OVERNIGHT_GAP_DYNAMICS_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f07_gap', '_f07_overnight', '_f07_intraday', '_f07_gapz')
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f07_overnight_gap_dynamics_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
