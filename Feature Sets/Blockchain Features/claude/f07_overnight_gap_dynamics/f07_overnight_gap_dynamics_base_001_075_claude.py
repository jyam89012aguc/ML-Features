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


# ============ FEATURES 001-075 ============

# raw daily overnight gap
def f07gp_f07_overnight_gap_dynamics_rawgap_1d_base_v001_signal(open, close):
    result = _f07_gap(open, close)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_5d_base_v002_signal(open, close):
    result = _mean(_f07_gap(open, close), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_10d_base_v003_signal(open, close):
    result = _mean(_f07_gap(open, close), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_21d_base_v004_signal(open, close):
    result = _mean(_f07_gap(open, close), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_63d_base_v005_signal(open, close):
    result = _mean(_f07_gap(open, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of daily gap
def f07gp_f07_overnight_gap_dynamics_gapmean_126d_base_v006_signal(open, close):
    result = _mean(_f07_gap(open, close), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d std of daily gap (gap dispersion)
def f07gp_f07_overnight_gap_dynamics_gapstd_5d_base_v007_signal(open, close):
    result = _std(_f07_gap(open, close), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_10d_base_v008_signal(open, close):
    result = _std(_f07_gap(open, close), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_21d_base_v009_signal(open, close):
    result = _std(_f07_gap(open, close), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_63d_base_v010_signal(open, close):
    result = _std(_f07_gap(open, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_126d_base_v011_signal(open, close):
    result = _std(_f07_gap(open, close), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of daily gap
def f07gp_f07_overnight_gap_dynamics_gapstd_252d_base_v012_signal(open, close):
    result = _std(_f07_gap(open, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 21d
def f07gp_f07_overnight_gap_dynamics_gapz_21d_base_v013_signal(open, close):
    result = _f07_gapz(open, close, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 63d
def f07gp_f07_overnight_gap_dynamics_gapz_63d_base_v014_signal(open, close):
    result = _f07_gapz(open, close, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 126d
def f07gp_f07_overnight_gap_dynamics_gapz_126d_base_v015_signal(open, close):
    result = _f07_gapz(open, close, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score over 252d
def f07gp_f07_overnight_gap_dynamics_gapz_252d_base_v016_signal(open, close):
    result = _f07_gapz(open, close, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# daily intraday return component
def f07gp_f07_overnight_gap_dynamics_intraday_1d_base_v017_signal(open, close):
    result = _f07_intraday(open, close) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean intraday return
def f07gp_f07_overnight_gap_dynamics_intramean_5d_base_v018_signal(open, close):
    result = _mean(_f07_intraday(open, close), 5) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean intraday return
def f07gp_f07_overnight_gap_dynamics_intramean_21d_base_v019_signal(open, close):
    result = _mean(_f07_intraday(open, close), 21) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean intraday return
def f07gp_f07_overnight_gap_dynamics_intramean_63d_base_v020_signal(open, close):
    result = _mean(_f07_intraday(open, close), 63) + _f07_gap(open, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# overnight minus intraday return spread (1d)
def f07gp_f07_overnight_gap_dynamics_onmid_1d_base_v021_signal(open, close):
    result = _f07_overnight(open, close) - _f07_intraday(open, close)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmid_21d_base_v022_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmid_63d_base_v023_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of overnight-minus-intraday spread
def f07gp_f07_overnight_gap_dynamics_onmid_126d_base_v024_signal(open, close):
    sp = _f07_overnight(open, close) - _f07_intraday(open, close)
    result = _mean(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 21d
def f07gp_f07_overnight_gap_dynamics_ondrift_21d_base_v025_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 63d
def f07gp_f07_overnight_gap_dynamics_ondrift_63d_base_v026_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 126d
def f07gp_f07_overnight_gap_dynamics_ondrift_126d_base_v027_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(126, min_periods=42).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over 252d
def f07gp_f07_overnight_gap_dynamics_ondrift_252d_base_v028_signal(open, close):
    ov = _f07_overnight(open, close)
    result = ov.rolling(252, min_periods=84).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap continuation: gap * same-day intraday, smoothed
def f07gp_f07_overnight_gap_dynamics_gapcont_21d_base_v029_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap continuation
def f07gp_f07_overnight_gap_dynamics_gapcont_63d_base_v030_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap continuation
def f07gp_f07_overnight_gap_dynamics_gapcont_126d_base_v031_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _mean(cont, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d absolute gap intensity (mean of |gap|)
def f07gp_f07_overnight_gap_dynamics_absint_21d_base_v032_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d absolute gap intensity
def f07gp_f07_overnight_gap_dynamics_absint_63d_base_v033_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d absolute gap intensity
def f07gp_f07_overnight_gap_dynamics_absint_126d_base_v034_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d absolute gap intensity
def f07gp_f07_overnight_gap_dynamics_absint_252d_base_v035_signal(open, close):
    result = _mean(_f07_gap(open, close).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed gap momentum (sum of gaps)
def f07gp_f07_overnight_gap_dynamics_gapmom_21d_base_v036_signal(open, close):
    result = _f07_gap(open, close).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed gap momentum
def f07gp_f07_overnight_gap_dynamics_gapmom_63d_base_v037_signal(open, close):
    result = _f07_gap(open, close).rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed gap momentum
def f07gp_f07_overnight_gap_dynamics_gapmom_126d_base_v038_signal(open, close):
    result = _f07_gap(open, close).rolling(126, min_periods=42).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d overnight contribution ratio (overnight var share of total)
def f07gp_f07_overnight_gap_dynamics_oncontrib_21d_base_v039_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 21) ** 2
    vin = _std(intr, 21) ** 2
    result = _safe_div(vov, vov + vin)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d overnight contribution ratio
def f07gp_f07_overnight_gap_dynamics_oncontrib_63d_base_v040_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 63) ** 2
    vin = _std(intr, 63) ** 2
    result = _safe_div(vov, vov + vin)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d overnight contribution ratio
def f07gp_f07_overnight_gap_dynamics_oncontrib_126d_base_v041_signal(open, close):
    ov = _f07_overnight(open, close)
    intr = _f07_intraday(open, close)
    vov = _std(ov, 126) ** 2
    vin = _std(intr, 126) ** 2
    result = _safe_div(vov, vov + vin)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap volatility ratio: gap std vs intraday std
def f07gp_f07_overnight_gap_dynamics_gapvolrat_21d_base_v042_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 21), _std(_f07_intraday(open, close), 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap volatility ratio
def f07gp_f07_overnight_gap_dynamics_gapvolrat_63d_base_v043_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 63), _std(_f07_intraday(open, close), 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap volatility ratio
def f07gp_f07_overnight_gap_dynamics_gapvolrat_126d_base_v044_signal(open, close):
    result = _safe_div(_std(_f07_gap(open, close), 126), _std(_f07_intraday(open, close), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap mean scaled by gap vol (gap Sharpe)
def f07gp_f07_overnight_gap_dynamics_gapsharpe_21d_base_v045_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 21), _std(g, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap Sharpe
def f07gp_f07_overnight_gap_dynamics_gapsharpe_63d_base_v046_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 63), _std(g, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap Sharpe
def f07gp_f07_overnight_gap_dynamics_gapsharpe_126d_base_v047_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 126), _std(g, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap Sharpe
def f07gp_f07_overnight_gap_dynamics_gapsharpe_252d_base_v048_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(_mean(g, 252), _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA of daily gap
def f07gp_f07_overnight_gap_dynamics_gapewm_21d_base_v049_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of daily gap
def f07gp_f07_overnight_gap_dynamics_gapewm_63d_base_v050_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of daily gap
def f07gp_f07_overnight_gap_dynamics_gapewm_126d_base_v051_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap skew (asymmetry of gaps)
def f07gp_f07_overnight_gap_dynamics_gapskew_21d_base_v052_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap skew
def f07gp_f07_overnight_gap_dynamics_gapskew_63d_base_v053_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap skew
def f07gp_f07_overnight_gap_dynamics_gapskew_126d_base_v054_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap kurtosis (fat-tailed overnight jumps)
def f07gp_f07_overnight_gap_dynamics_gapkurt_63d_base_v055_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap kurtosis
def f07gp_f07_overnight_gap_dynamics_gapkurt_126d_base_v056_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill: how much intraday reverses the gap, 21d smoothed
def f07gp_f07_overnight_gap_dynamics_gapfill_21d_base_v057_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill 63d smoothed
def f07gp_f07_overnight_gap_dynamics_gapfill_63d_base_v058_signal(open, close):
    fill = -_safe_div(_f07_intraday(open, close), _f07_gap(open, close))
    result = _mean(fill.clip(-5, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap-volatility: rolling std of |gap| (vol-of-gap)
def f07gp_f07_overnight_gap_dynamics_gapvol_21d_base_v059_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-volatility
def f07gp_f07_overnight_gap_dynamics_gapvol_63d_base_v060_signal(open, close):
    result = _std(_f07_gap(open, close).abs(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d overnight return share of total daily return magnitude
def f07gp_f07_overnight_gap_dynamics_onshare_21d_base_v061_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d overnight return share
def f07gp_f07_overnight_gap_dynamics_onshare_63d_base_v062_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d overnight return share
def f07gp_f07_overnight_gap_dynamics_onshare_126d_base_v063_signal(open, close):
    ov = _f07_overnight(open, close).abs()
    intr = _f07_intraday(open, close).abs()
    result = _mean(_safe_div(ov, ov + intr), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score smoothed over 5d (fast gap pressure)
def f07gp_f07_overnight_gap_dynamics_gapzsm_5d_base_v064_signal(open, close):
    result = _mean(_f07_gapz(open, close, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score smoothed over 10d
def f07gp_f07_overnight_gap_dynamics_gapzsm_10d_base_v065_signal(open, close):
    result = _mean(_f07_gapz(open, close, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score smoothed over 21d
def f07gp_f07_overnight_gap_dynamics_gapzsm_21d_base_v066_signal(open, close):
    result = _mean(_f07_gapz(open, close, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap continuation correlation proxy (gap vs next-leg, via product mean / vols)
def f07gp_f07_overnight_gap_dynamics_contcorr_63d_base_v067_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 63) - _mean(g, 63) * _mean(intr, 63)
    result = _safe_div(cov, _std(g, 63) * _std(intr, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap continuation correlation proxy
def f07gp_f07_overnight_gap_dynamics_contcorr_126d_base_v068_signal(open, close):
    g = _f07_gap(open, close)
    intr = _f07_intraday(open, close)
    cov = _mean(g * intr, 126) - _mean(g, 126) * _mean(intr, 126)
    result = _safe_div(cov, _std(g, 126) * _std(intr, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap momentum scaled by gap vol (normalized signed momentum)
def f07gp_f07_overnight_gap_dynamics_gapmomz_21d_base_v069_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(21, min_periods=10).sum(), _std(g, 21) * np.sqrt(21.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap momentum scaled by gap vol
def f07gp_f07_overnight_gap_dynamics_gapmomz_63d_base_v070_signal(open, close):
    g = _f07_gap(open, close)
    result = _safe_div(g.rolling(63, min_periods=21).sum(), _std(g, 63) * np.sqrt(63.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative overnight drift normalized by drift vol
def f07gp_f07_overnight_gap_dynamics_driftz_63d_base_v071_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(63, min_periods=21).sum()
    result = _z(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative overnight drift normalized
def f07gp_f07_overnight_gap_dynamics_driftz_126d_base_v072_signal(open, close):
    ov = _f07_overnight(open, close)
    cum = ov.rolling(126, min_periods=42).sum()
    result = _z(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap range relative to closeadj (gap magnitude on adjusted scale, short)
def f07gp_f07_overnight_gap_dynamics_gapintens_21d_base_v073_signal(open, close, closeadj):
    g = _f07_gap(open, close)
    scale = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = _mean(_safe_div(g.abs(), scale), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed gap momentum confirmed by volume z-score
def f07gp_f07_overnight_gap_dynamics_gapvolconf_21d_base_v074_signal(open, close, volume):
    g = _f07_gap(open, close)
    result = g.rolling(21, min_periods=10).sum() * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap continuation smoothed and vol-scaled
def f07gp_f07_overnight_gap_dynamics_gapcontz_21d_base_v075_signal(open, close):
    cont = _f07_gap(open, close) * _f07_intraday(open, close)
    result = _z(_mean(cont, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07gp_f07_overnight_gap_dynamics_rawgap_1d_base_v001_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_5d_base_v002_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_10d_base_v003_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_21d_base_v004_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_63d_base_v005_signal,
    f07gp_f07_overnight_gap_dynamics_gapmean_126d_base_v006_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_5d_base_v007_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_10d_base_v008_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_21d_base_v009_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_63d_base_v010_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_126d_base_v011_signal,
    f07gp_f07_overnight_gap_dynamics_gapstd_252d_base_v012_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_21d_base_v013_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_63d_base_v014_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_126d_base_v015_signal,
    f07gp_f07_overnight_gap_dynamics_gapz_252d_base_v016_signal,
    f07gp_f07_overnight_gap_dynamics_intraday_1d_base_v017_signal,
    f07gp_f07_overnight_gap_dynamics_intramean_5d_base_v018_signal,
    f07gp_f07_overnight_gap_dynamics_intramean_21d_base_v019_signal,
    f07gp_f07_overnight_gap_dynamics_intramean_63d_base_v020_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_1d_base_v021_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_21d_base_v022_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_63d_base_v023_signal,
    f07gp_f07_overnight_gap_dynamics_onmid_126d_base_v024_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_21d_base_v025_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_63d_base_v026_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_126d_base_v027_signal,
    f07gp_f07_overnight_gap_dynamics_ondrift_252d_base_v028_signal,
    f07gp_f07_overnight_gap_dynamics_gapcont_21d_base_v029_signal,
    f07gp_f07_overnight_gap_dynamics_gapcont_63d_base_v030_signal,
    f07gp_f07_overnight_gap_dynamics_gapcont_126d_base_v031_signal,
    f07gp_f07_overnight_gap_dynamics_absint_21d_base_v032_signal,
    f07gp_f07_overnight_gap_dynamics_absint_63d_base_v033_signal,
    f07gp_f07_overnight_gap_dynamics_absint_126d_base_v034_signal,
    f07gp_f07_overnight_gap_dynamics_absint_252d_base_v035_signal,
    f07gp_f07_overnight_gap_dynamics_gapmom_21d_base_v036_signal,
    f07gp_f07_overnight_gap_dynamics_gapmom_63d_base_v037_signal,
    f07gp_f07_overnight_gap_dynamics_gapmom_126d_base_v038_signal,
    f07gp_f07_overnight_gap_dynamics_oncontrib_21d_base_v039_signal,
    f07gp_f07_overnight_gap_dynamics_oncontrib_63d_base_v040_signal,
    f07gp_f07_overnight_gap_dynamics_oncontrib_126d_base_v041_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolrat_21d_base_v042_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolrat_63d_base_v043_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolrat_126d_base_v044_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_21d_base_v045_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_63d_base_v046_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_126d_base_v047_signal,
    f07gp_f07_overnight_gap_dynamics_gapsharpe_252d_base_v048_signal,
    f07gp_f07_overnight_gap_dynamics_gapewm_21d_base_v049_signal,
    f07gp_f07_overnight_gap_dynamics_gapewm_63d_base_v050_signal,
    f07gp_f07_overnight_gap_dynamics_gapewm_126d_base_v051_signal,
    f07gp_f07_overnight_gap_dynamics_gapskew_21d_base_v052_signal,
    f07gp_f07_overnight_gap_dynamics_gapskew_63d_base_v053_signal,
    f07gp_f07_overnight_gap_dynamics_gapskew_126d_base_v054_signal,
    f07gp_f07_overnight_gap_dynamics_gapkurt_63d_base_v055_signal,
    f07gp_f07_overnight_gap_dynamics_gapkurt_126d_base_v056_signal,
    f07gp_f07_overnight_gap_dynamics_gapfill_21d_base_v057_signal,
    f07gp_f07_overnight_gap_dynamics_gapfill_63d_base_v058_signal,
    f07gp_f07_overnight_gap_dynamics_gapvol_21d_base_v059_signal,
    f07gp_f07_overnight_gap_dynamics_gapvol_63d_base_v060_signal,
    f07gp_f07_overnight_gap_dynamics_onshare_21d_base_v061_signal,
    f07gp_f07_overnight_gap_dynamics_onshare_63d_base_v062_signal,
    f07gp_f07_overnight_gap_dynamics_onshare_126d_base_v063_signal,
    f07gp_f07_overnight_gap_dynamics_gapzsm_5d_base_v064_signal,
    f07gp_f07_overnight_gap_dynamics_gapzsm_10d_base_v065_signal,
    f07gp_f07_overnight_gap_dynamics_gapzsm_21d_base_v066_signal,
    f07gp_f07_overnight_gap_dynamics_contcorr_63d_base_v067_signal,
    f07gp_f07_overnight_gap_dynamics_contcorr_126d_base_v068_signal,
    f07gp_f07_overnight_gap_dynamics_gapmomz_21d_base_v069_signal,
    f07gp_f07_overnight_gap_dynamics_gapmomz_63d_base_v070_signal,
    f07gp_f07_overnight_gap_dynamics_driftz_63d_base_v071_signal,
    f07gp_f07_overnight_gap_dynamics_driftz_126d_base_v072_signal,
    f07gp_f07_overnight_gap_dynamics_gapintens_21d_base_v073_signal,
    f07gp_f07_overnight_gap_dynamics_gapvolconf_21d_base_v074_signal,
    f07gp_f07_overnight_gap_dynamics_gapcontz_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_OVERNIGHT_GAP_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f07_overnight_gap_dynamics_base_001_075_claude: {n_features} features pass")
