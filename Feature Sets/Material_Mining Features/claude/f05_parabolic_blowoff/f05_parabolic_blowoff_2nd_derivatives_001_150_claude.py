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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


def _atr(high, low, closeadj, w):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _stretch(closeadj, w):
    ma = closeadj.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))


def _runslope(closeadj, w):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    return lr.rolling(w, min_periods=max(1, w // 2)).mean()


def _above_ma_atr(closeadj, high, low, w_ma, w_atr):
    ma = closeadj.rolling(w_ma, min_periods=max(1, w_ma // 2)).mean()
    atr = _atr(high, low, closeadj, w_atr)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _volspike(volume, w):
    av = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / av.replace(0, np.nan)


# slope operator = 1st math derivative of a base series over an ROC window
def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# decorrelating slope variants (still 1st-derivative transforms of the base)
def _zslope(s, w, zw):
    # standardized slope: per-day change normalized by its own dispersion
    sl = (s - s.shift(w)) / float(w)
    return _z(sl, zw)


def _emaslope(s, span):
    # smoothed instantaneous slope via EMA-difference
    e = s.ewm(span=span, min_periods=max(2, span // 2)).mean()
    return e.diff()


def _rankslope(s, w, rw):
    # percentile-rank of the base's slope within a trailing window (regime-relative
    # momentum — a continuous, decorrelating 1st-derivative transform)
    sl = (s - s.shift(w)) / float(w)
    return sl.rolling(rw, min_periods=max(5, rw // 3)).rank(pct=True) - 0.5


def _residslope(s, w, lw):
    # slope minus its own longer-horizon slope (de-trended instantaneous slope)
    sl = (s - s.shift(w)) / float(w)
    slow = (s - s.shift(lw)) / float(lw)
    return sl - slow


# ============================================================
# Each feature: build a parabolic-blowoff BASE inline, then return its SLOPE.

# slope of stretch above 21d MA (rate of overextension change), 5d ROC
def f05pb_f05_parabolic_blowoff_stretch21_5d_slope_v001_signal(closeadj):
    base = _stretch(closeadj, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 21d MA, 21d ROC (slower extension trend)
def f05pb_f05_parabolic_blowoff_stretch21_21d_slope_v002_signal(closeadj):
    base = _stretch(closeadj, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 10d MA, 5d ROC
def f05pb_f05_parabolic_blowoff_stretch10_5d_slope_v003_signal(closeadj):
    base = _stretch(closeadj, 10)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 63d MA, 21d ROC
def f05pb_f05_parabolic_blowoff_stretch63_21d_slope_v004_signal(closeadj):
    base = _stretch(closeadj, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 34d MA, 10d ROC
def f05pb_f05_parabolic_blowoff_stretch34_10d_slope_v005_signal(closeadj):
    base = _stretch(closeadj, 34)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 8d-vs-34d EMA ribbon separation, 5d ROC
def f05pb_f05_parabolic_blowoff_ribbon8v34_5d_slope_v006_signal(closeadj):
    base = (_ema(closeadj, 8) - _ema(closeadj, 34)) / _ema(closeadj, 34).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 5/13/34 EMA ribbon width, 5d ROC
def f05pb_f05_parabolic_blowoff_ribbonwidth_5d_slope_v007_signal(closeadj):
    e5, e13, e34 = _ema(closeadj, 5), _ema(closeadj, 13), _ema(closeadj, 34)
    stacked = pd.concat([e5, e13, e34], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / e34.replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of distance above 21d MA in ATR units, 5d/126 (regime-relative)
def f05pb_f05_parabolic_blowoff_atrext21_5d_slope_v008_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 21, 21)
    result = _rankslope(base, 5, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of distance above 21d MA in ATR units (span 21)
def f05pb_f05_parabolic_blowoff_atrext21_21d_slope_v009_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 21, 21)
    result = _emaslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of distance above 63d MA in ATR units (span 21)
def f05pb_f05_parabolic_blowoff_atrext63_21d_slope_v010_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 63, 21)
    result = _emaslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of distance above 10d MA in ATR units (span 8)
def f05pb_f05_parabolic_blowoff_atrext10_5d_slope_v011_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 10, 10)
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 5d run-slope (acceleration of the vertical ascent), 5d ROC
def f05pb_f05_parabolic_blowoff_runslope5_5d_slope_v012_signal(closeadj):
    base = _runslope(closeadj, 5)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 10d run-slope, 5d ROC
def f05pb_f05_parabolic_blowoff_runslope10_5d_slope_v013_signal(closeadj):
    base = _runslope(closeadj, 10)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 21d run-slope, 21d ROC
def f05pb_f05_parabolic_blowoff_runslope21_21d_slope_v014_signal(closeadj):
    base = _runslope(closeadj, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the blowoff volume spike (5d/63d), 5d ROC
def f05pb_f05_parabolic_blowoff_volspike_5d_slope_v015_signal(volume):
    base = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of single-day volume z (63d), 5d ROC
def f05pb_f05_parabolic_blowoff_volz_5d_slope_v016_signal(volume):
    base = _z(volume, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of dollar-volume spike (span 8)
def f05pb_f05_parabolic_blowoff_dollvolspike_5d_slope_v017_signal(closeadj, volume):
    dv = closeadj * volume
    base = dv.rolling(5, min_periods=3).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of pullback-from-21d-high (fade momentum), 5d ROC
def f05pb_f05_parabolic_blowoff_fade21_5d_slope_v018_signal(closeadj):
    base = closeadj / _rmax(closeadj, 21).replace(0, np.nan) - 1.0
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Bollinger %B (band-position momentum), 5d ROC
def f05pb_f05_parabolic_blowoff_pctb_5d_slope_v019_signal(closeadj):
    ma, sd = _mean(closeadj, 20), _std(closeadj, 20)
    base = (closeadj - (ma - 2.0 * sd)) / (4.0 * sd).replace(0, np.nan) - 0.5
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of sigma-extension (price-MA in sd units), span 8
def f05pb_f05_parabolic_blowoff_sigmaext_5d_slope_v020_signal(closeadj):
    base = (closeadj - _mean(closeadj, 21)) / _std(closeadj, 21).replace(0, np.nan)
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of RSI-0.5 (overbought momentum), 5d ROC
def f05pb_f05_parabolic_blowoff_rsi_5d_slope_v021_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    base = up / (up + dn).replace(0, np.nan) - 0.5
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCI-style typical-price extension over 14d, 5d ROC (overbought thrust)
def f05pb_f05_parabolic_blowoff_williamsr_5d_slope_v022_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(14, min_periods=7).mean()
    md = (tp - sma).abs().rolling(14, min_periods=7).mean()
    base = (tp - sma) / (0.015 * md).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d-vs-63d range expansion ratio, 5d ROC
def f05pb_f05_parabolic_blowoff_rangeexp_5d_slope_v023_signal(closeadj, high, low):
    base = _atr(high, low, closeadj, 5) / _atr(high, low, closeadj, 63).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d-vs-63d realized-vol ratio, 5d ROC
def f05pb_f05_parabolic_blowoff_volratio_5d_slope_v024_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    v63 = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = v5 / v63.replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 5d-vs-63d MA spread (fast-MA separation), 5d ROC
def f05pb_f05_parabolic_blowoff_maspread_5d_slope_v025_signal(closeadj):
    base = (_mean(closeadj, 5) - _mean(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log(21d high / 63d MA) (peak-over-trend), 21d ROC
def f05pb_f05_parabolic_blowoff_peaktrend_21d_slope_v026_signal(closeadj):
    base = np.log(_rmax(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 63).replace(0, np.nan))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative positive-stretch energy over 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_stretchenergy_5d_slope_v027_signal(closeadj):
    base = _stretch(closeadj, 21).clip(lower=0).rolling(21, min_periods=10).sum()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-day volume imbalance over 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_volimbal_5d_slope_v028_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    upv = (volume * up).rolling(21, min_periods=10).sum()
    dnv = (volume * (1 - up)).rolling(21, min_periods=10).sum()
    base = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upside-semivariance share over 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_upsemivar_5d_slope_v029_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0).pow(2).rolling(21, min_periods=10).sum()
    tot = r.pow(2).rolling(21, min_periods=10).sum()
    base = up / tot.replace(0, np.nan) - 0.5
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stochastic %K, 5d ROC
def f05pb_f05_parabolic_blowoff_stoch_5d_slope_v030_signal(closeadj, high, low):
    hh, ll = _rmax(high, 14), _rmin(low, 14)
    base = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson hl-vol spike (5d/63d), 5d ROC
def f05pb_f05_parabolic_blowoff_parkinson_5d_slope_v031_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    base = hl.rolling(5, min_periods=3).mean() / hl.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume Herfindahl over 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_volherf_5d_slope_v032_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    share = volume / tot.replace(0, np.nan)
    base = (share ** 2).rolling(21, min_periods=10).sum()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of the 13d MA-stretch (span 8)
def f05pb_f05_parabolic_blowoff_stretch13_5d_slope_v033_signal(closeadj):
    base = _stretch(closeadj, 13)
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# standardized slope of EMA-stretch (price vs 10d EMA), 5d ROC z-scored
def f05pb_f05_parabolic_blowoff_emastretch10_5d_slope_v034_signal(closeadj):
    base = closeadj / _ema(closeadj, 10).replace(0, np.nan) - 1.0
    result = _zslope(base, 5, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 5d-vs-63d MA-in-ATR spread, 10d ROC
def f05pb_f05_parabolic_blowoff_maatr5v63_10d_slope_v035_signal(closeadj, high, low):
    base = (_mean(closeadj, 5) - _mean(closeadj, 63)) / _atr(high, low, closeadj, 21).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d return-skew, 5d ROC
def f05pb_f05_parabolic_blowoff_skew_5d_slope_v036_signal(closeadj):
    base = closeadj.pct_change().rolling(21, min_periods=10).skew()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d return-kurtosis, 5d ROC
def f05pb_f05_parabolic_blowoff_kurt_5d_slope_v037_signal(closeadj):
    base = closeadj.pct_change().rolling(21, min_periods=12).kurt()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol, 10d ROC
def f05pb_f05_parabolic_blowoff_volofvol_10d_slope_v038_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    base = v5.rolling(21, min_periods=10).std() / v5.rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the run-efficiency over 10d, 5d ROC
def f05pb_f05_parabolic_blowoff_runeff_5d_slope_v039_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    base = net / path.replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of volume-surge vs its 21d EMA (span 8)
def f05pb_f05_parabolic_blowoff_volsurgeema_5d_slope_v040_signal(volume):
    base = volume / _ema(volume, 21).replace(0, np.nan) - 1.0
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d-high / 63d-high freshness, 21d ROC
def f05pb_f05_parabolic_blowoff_freshpeak_21d_slope_v041_signal(closeadj):
    base = _rmax(closeadj, 21) / _rmax(closeadj, 63).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of distance-from-21d-high in ATR units (off-top), span 8
def f05pb_f05_parabolic_blowoff_offtop_5d_slope_v042_signal(closeadj, high, low):
    base = (closeadj - _rmax(closeadj, 21)) / _atr(high, low, closeadj, 21).replace(0, np.nan)
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mafan (5/21/63) dispersion, 5d ROC
def f05pb_f05_parabolic_blowoff_mafan_5d_slope_v043_signal(closeadj):
    m5, m21, m63 = _mean(closeadj, 5), _mean(closeadj, 21), _mean(closeadj, 63)
    stacked = pd.concat([m5, m21, m63], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / m63.replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of autocorrelation of returns over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_autocorr_10d_slope_v044_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=10).corr(r.shift(1))
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trend-residual from a 21d linear fit, 5d ROC
def f05pb_f05_parabolic_blowoff_trendresid_5d_slope_v045_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp - (2.0 * lp.rolling(11, min_periods=6).mean() - lp.rolling(21, min_periods=10).mean())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of the 50d-MA extension (regime-relative slow-trend speed), 10d/126
def f05pb_f05_parabolic_blowoff_ext50_10d_slope_v046_signal(closeadj):
    base = closeadj / _mean(closeadj, 50).replace(0, np.nan) - 1.0
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative gap-run over 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_gaprun_5d_slope_v047_signal(closeadj, high):
    base = ((closeadj - high.shift(1)).clip(lower=0) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).sum()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch-sharpness (stretch / its dispersion), 5d ROC
def f05pb_f05_parabolic_blowoff_stretchsharp_5d_slope_v048_signal(closeadj):
    s = _stretch(closeadj, 21)
    base = s / s.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the angle-of-ascent (arctan slope/vol), 10d ROC
def f05pb_f05_parabolic_blowoff_angle_10d_slope_v049_signal(closeadj):
    slope = _runslope(closeadj, 21)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = np.arctan(slope / vol.replace(0, np.nan))
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the max 3d burst within 21d, 5d ROC
def f05pb_f05_parabolic_blowoff_maxburst_5d_slope_v050_signal(closeadj):
    r3 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(3).replace(0, np.nan))
    base = r3.rolling(21, min_periods=10).max()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# --- second-window variants (different ROC) for additional decorrelated slopes ---

# slope of stretch above 21d MA, 10d ROC (medium extension trend)
def f05pb_f05_parabolic_blowoff_stretch21_10d_slope_v051_signal(closeadj):
    base = _stretch(closeadj, 21)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 10d MA, 10d ROC
def f05pb_f05_parabolic_blowoff_stretch10_10d_slope_v052_signal(closeadj):
    base = _stretch(closeadj, 10)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of stretch above 63d MA, span 13
def f05pb_f05_parabolic_blowoff_stretch63_10d_slope_v053_signal(closeadj):
    base = _stretch(closeadj, 63)
    result = _emaslope(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of ATR-ext above 21d MA (regime-relative extension speed), 10d/126
def f05pb_f05_parabolic_blowoff_atrext21_10d_slope_v054_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 21, 21)
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of ATR-ext above 34d MA, 10d/126 (regime-relative mid speed)
def f05pb_f05_parabolic_blowoff_atrext34_10d_slope_v055_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 34, 21)
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of run-slope(5), 3d ROC (fast acceleration)
def f05pb_f05_parabolic_blowoff_runslope5_3d_slope_v056_signal(closeadj):
    base = _runslope(closeadj, 5)
    result = _slope(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of run-slope(10), 10d ROC
def f05pb_f05_parabolic_blowoff_runslope10_10d_slope_v057_signal(closeadj):
    base = _runslope(closeadj, 10)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume spike (5d/63d), 10d ROC
def f05pb_f05_parabolic_blowoff_volspike_10d_slope_v058_signal(volume):
    base = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume z, 10d ROC
def f05pb_f05_parabolic_blowoff_volz_10d_slope_v059_signal(volume):
    base = _z(volume, 63)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fade-from-21d-high, 10d ROC
def f05pb_f05_parabolic_blowoff_fade21_10d_slope_v060_signal(closeadj):
    base = closeadj / _rmax(closeadj, 21).replace(0, np.nan) - 1.0
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# residual slope of Bollinger %B: 10d slope minus 21d slope (de-trended band momentum)
def f05pb_f05_parabolic_blowoff_pctb_10d_slope_v061_signal(closeadj):
    ma, sd = _mean(closeadj, 20), _std(closeadj, 20)
    base = (closeadj - (ma - 2.0 * sd)) / (4.0 * sd).replace(0, np.nan) - 0.5
    result = _residslope(base, 10, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of sigma-extension, 10d/126 (regime-relative statistical extension)
def f05pb_f05_parabolic_blowoff_sigmaext_10d_slope_v062_signal(closeadj):
    base = (closeadj - _mean(closeadj, 21)) / _std(closeadj, 21).replace(0, np.nan)
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of RSI-0.5, 10d ROC
def f05pb_f05_parabolic_blowoff_rsi_10d_slope_v063_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    base = up / (up + dn).replace(0, np.nan) - 0.5
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of range-expansion ratio, 10d ROC
def f05pb_f05_parabolic_blowoff_rangeexp_10d_slope_v064_signal(closeadj, high, low):
    base = _atr(high, low, closeadj, 5) / _atr(high, low, closeadj, 63).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-ratio 5v63, 10d ROC
def f05pb_f05_parabolic_blowoff_volratio_10d_slope_v065_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    v63 = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = v5 / v63.replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5v21 MA spread, 10d ROC
def f05pb_f05_parabolic_blowoff_maspread_10d_slope_v066_signal(closeadj):
    base = (_mean(closeadj, 5) - _mean(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch energy, 10d ROC
def f05pb_f05_parabolic_blowoff_stretchenergy_10d_slope_v067_signal(closeadj):
    base = _stretch(closeadj, 21).clip(lower=0).rolling(21, min_periods=10).sum()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume imbalance, 10d ROC
def f05pb_f05_parabolic_blowoff_volimbal_10d_slope_v068_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    upv = (volume * up).rolling(21, min_periods=10).sum()
    dnv = (volume * (1 - up)).rolling(21, min_periods=10).sum()
    base = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upside-semivariance share, 10d ROC
def f05pb_f05_parabolic_blowoff_upsemivar_10d_slope_v069_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0).pow(2).rolling(21, min_periods=10).sum()
    tot = r.pow(2).rolling(21, min_periods=10).sum()
    base = up / tot.replace(0, np.nan) - 0.5
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stochastic %K, 10d ROC
def f05pb_f05_parabolic_blowoff_stoch_10d_slope_v070_signal(closeadj, high, low):
    hh, ll = _rmax(high, 14), _rmin(low, 14)
    base = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson hl-vol spike, 10d ROC
def f05pb_f05_parabolic_blowoff_parkinson_10d_slope_v071_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    base = hl.rolling(5, min_periods=3).mean() / hl.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume Herfindahl, 10d ROC
def f05pb_f05_parabolic_blowoff_volherf_10d_slope_v072_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    share = volume / tot.replace(0, np.nan)
    base = (share ** 2).rolling(21, min_periods=10).sum()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# residual slope of 13d MA-stretch: 10d slope minus 21d slope (de-trended)
def f05pb_f05_parabolic_blowoff_stretch13_10d_slope_v073_signal(closeadj):
    base = _stretch(closeadj, 13)
    result = _residslope(base, 10, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of EMA(10)-stretch, 10d/126 (regime-relative fast-mean speed)
def f05pb_f05_parabolic_blowoff_emastretch10_10d_slope_v074_signal(closeadj):
    base = closeadj / _ema(closeadj, 10).replace(0, np.nan) - 1.0
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of peak-over-trend (21d high / 63d MA), 10d ROC
def f05pb_f05_parabolic_blowoff_peaktrend_10d_slope_v075_signal(closeadj):
    base = np.log(_rmax(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 63).replace(0, np.nan))
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return-skew, 10d ROC
def f05pb_f05_parabolic_blowoff_skew_10d_slope_v076_signal(closeadj):
    base = closeadj.pct_change().rolling(21, min_periods=10).skew()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of run-efficiency, 10d ROC
def f05pb_f05_parabolic_blowoff_runeff_10d_slope_v077_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    base = net / path.replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-vol spike, 10d ROC
def f05pb_f05_parabolic_blowoff_dollvolspike_10d_slope_v078_signal(closeadj, volume):
    dv = closeadj * volume
    base = dv.rolling(5, min_periods=3).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of the off-top distance (regime-relative top approach speed), 10d/126
def f05pb_f05_parabolic_blowoff_offtop_10d_slope_v079_signal(closeadj, high, low):
    base = (closeadj - _rmax(closeadj, 21)) / _atr(high, low, closeadj, 21).replace(0, np.nan)
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mafan dispersion, 10d ROC
def f05pb_f05_parabolic_blowoff_mafan_10d_slope_v080_signal(closeadj):
    m5, m21, m63 = _mean(closeadj, 5), _mean(closeadj, 21), _mean(closeadj, 63)
    stacked = pd.concat([m5, m21, m63], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / m63.replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-ribbon 8v34, 10d ROC
def f05pb_f05_parabolic_blowoff_ribbon8v34_10d_slope_v081_signal(closeadj):
    base = (_ema(closeadj, 8) - _ema(closeadj, 34)) / _ema(closeadj, 34).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trend-residual, 10d ROC
def f05pb_f05_parabolic_blowoff_trendresid_10d_slope_v082_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp - (2.0 * lp.rolling(11, min_periods=6).mean() - lp.rolling(21, min_periods=10).mean())
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# residual slope of 50d-MA extension: 21d slope minus 63d slope (de-trended)
def f05pb_f05_parabolic_blowoff_ext50_21d_slope_v083_signal(closeadj):
    base = closeadj / _mean(closeadj, 50).replace(0, np.nan) - 1.0
    result = _residslope(base, 21, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCI-style typical-price extension over 14d, 10d ROC
def f05pb_f05_parabolic_blowoff_williamsr_10d_slope_v084_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(14, min_periods=7).mean()
    md = (tp - sma).abs().rolling(14, min_periods=7).mean()
    base = (tp - sma) / (0.015 * md).replace(0, np.nan)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 8d MA minus its 21d median, 5d ROC
def f05pb_f05_parabolic_blowoff_stretchmed8_5d_slope_v085_signal(closeadj):
    s = _stretch(closeadj, 8)
    base = s - s.rolling(21, min_periods=10).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of run-intensity (10d ret x up-frac), 5d ROC
def f05pb_f05_parabolic_blowoff_runintensity_5d_slope_v086_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    upfrac = (closeadj.diff() > 0).astype(float).rolling(10, min_periods=5).mean()
    base = ret * upfrac
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume trend (21d log-vol slope), 10d ROC
def f05pb_f05_parabolic_blowoff_voltrend_10d_slope_v087_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = (lv - lv.shift(21)) / 21.0
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-ret correlation over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_volretcorr_10d_slope_v088_signal(closeadj, volume):
    base = closeadj.pct_change().abs().rolling(21, min_periods=10).corr(volume)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-dollar share over 10d, 5d ROC
def f05pb_f05_parabolic_blowoff_updollshare_5d_slope_v089_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    dv = closeadj * volume
    base = (dv * up).rolling(10, min_periods=5).sum() / dv.rolling(10, min_periods=5).sum().replace(0, np.nan) - 0.5
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of squeeze-pop bandwidth ratio, 10d ROC
def f05pb_f05_parabolic_blowoff_squeezepop_10d_slope_v090_signal(closeadj):
    bw = _std(closeadj, 20) / _mean(closeadj, 20).replace(0, np.nan)
    base = bw / (bw.shift(5).rolling(63, min_periods=21).min() + 1e-6)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of frothvspeak (extension vs 252d peak extension), 21d ROC
def f05pb_f05_parabolic_blowoff_frothpeak_21d_slope_v091_signal(closeadj):
    ext = (closeadj / _mean(closeadj, 21).replace(0, np.nan) - 1.0).clip(lower=0)
    base = ext / ext.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of obtime (overbought-fraction composite), 10d ROC
def f05pb_f05_parabolic_blowoff_obtime_10d_slope_v092_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    base = (rsi - 0.7).clip(lower=0).rolling(21, min_periods=10).mean()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accel-index (5d-2*10d+21d slope), 5d ROC
def f05pb_f05_parabolic_blowoff_accelindex_5d_slope_v093_signal(closeadj):
    base = _runslope(closeadj, 5) - 2.0 * _runslope(closeadj, 10) + _runslope(closeadj, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max-extension held over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_maxext_10d_slope_v094_signal(closeadj):
    base = _stretch(closeadj, 21).rolling(21, min_periods=10).max()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch-range over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_stretchrange_10d_slope_v095_signal(closeadj):
    s = _stretch(closeadj, 21)
    base = s.rolling(21, min_periods=10).max() - s.rolling(21, min_periods=10).min()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR-thrust-sum over 10d, 5d ROC
def f05pb_f05_parabolic_blowoff_atrthrust_5d_slope_v096_signal(closeadj, high, low):
    contrib = closeadj.diff().clip(lower=0) / _atr(high, low, closeadj, 21).replace(0, np.nan)
    base = contrib.rolling(10, min_periods=5).sum()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of move-vs-budget (21d move / ATR budget), 10d ROC
def f05pb_f05_parabolic_blowoff_movebudget_10d_slope_v097_signal(closeadj, high, low):
    move = (closeadj - closeadj.shift(21)).abs()
    budget = _atr(high, low, closeadj, 21) * np.sqrt(21.0)
    base = (move / budget.replace(0, np.nan) - 1.0)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fragility (stretch x downside semivol), 5d ROC
def f05pb_f05_parabolic_blowoff_fragility_5d_slope_v098_signal(closeadj):
    s = _stretch(closeadj, 21).clip(lower=0)
    dnvar = closeadj.pct_change().clip(upper=0).pow(2).rolling(21, min_periods=10).mean()
    base = s * np.sqrt(dnvar)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite z-score (stretch+slope+vol), 10d ROC
def f05pb_f05_parabolic_blowoff_compz_10d_slope_v099_signal(closeadj, volume):
    base = (_z(_stretch(closeadj, 21), 63) + _z(_runslope(closeadj, 10), 63) + _z(volume, 63)) / 3.0
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ribbon-width velocity base (5/13/34), 5d ROC
def f05pb_f05_parabolic_blowoff_ribbonwidth_3d_slope_v100_signal(closeadj):
    e5, e13, e34 = _ema(closeadj, 5), _ema(closeadj, 13), _ema(closeadj, 34)
    stacked = pd.concat([e5, e13, e34], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / e34.replace(0, np.nan)
    result = _slope(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# --- third-window variants (21d ROC) on key bases ---

# slope of stretch above 10d MA, 21d ROC
def f05pb_f05_parabolic_blowoff_stretch10_21d_slope_v101_signal(closeadj):
    base = _stretch(closeadj, 10)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of stretch above 34d MA (regime-relative mid-trend speed), 21d/126
def f05pb_f05_parabolic_blowoff_stretch34_21d_slope_v102_signal(closeadj):
    base = _stretch(closeadj, 34)
    result = _rankslope(base, 21, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR-ext above 21d MA, 3d ROC (fast extension change)
def f05pb_f05_parabolic_blowoff_atrext21_3d_slope_v103_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 21, 21)
    result = _slope(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of ATR-ext above 63d MA (regime-relative slow-extension speed), 10d/126
def f05pb_f05_parabolic_blowoff_atrext63_10d_slope_v104_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 63, 21)
    result = _rankslope(base, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of run-slope(21), span 13
def f05pb_f05_parabolic_blowoff_runslope21_10d_slope_v105_signal(closeadj):
    base = _runslope(closeadj, 21)
    result = _emaslope(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume spike, 21d ROC
def f05pb_f05_parabolic_blowoff_volspike_21d_slope_v106_signal(volume):
    base = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fade-from-21d-high, 21d ROC
def f05pb_f05_parabolic_blowoff_fade21_21d_slope_v107_signal(closeadj):
    base = closeadj / _rmax(closeadj, 21).replace(0, np.nan) - 1.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Bollinger %B, 21d ROC
def f05pb_f05_parabolic_blowoff_pctb_21d_slope_v108_signal(closeadj):
    ma, sd = _mean(closeadj, 20), _std(closeadj, 20)
    base = (closeadj - (ma - 2.0 * sd)) / (4.0 * sd).replace(0, np.nan) - 0.5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of sigma-extension, span 21
def f05pb_f05_parabolic_blowoff_sigmaext_21d_slope_v109_signal(closeadj):
    base = (closeadj - _mean(closeadj, 21)) / _std(closeadj, 21).replace(0, np.nan)
    result = _emaslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of RSI-0.5, 21d ROC
def f05pb_f05_parabolic_blowoff_rsi_21d_slope_v110_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    base = up / (up + dn).replace(0, np.nan) - 0.5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of range-expansion ratio, 21d ROC
def f05pb_f05_parabolic_blowoff_rangeexp_21d_slope_v111_signal(closeadj, high, low):
    base = _atr(high, low, closeadj, 5) / _atr(high, low, closeadj, 63).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-ratio 5v63, 21d ROC
def f05pb_f05_parabolic_blowoff_volratio_21d_slope_v112_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    v63 = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = v5 / v63.replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5v21 MA spread, 21d ROC
def f05pb_f05_parabolic_blowoff_maspread_21d_slope_v113_signal(closeadj):
    base = (_mean(closeadj, 5) - _mean(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch energy, 21d ROC
def f05pb_f05_parabolic_blowoff_stretchenergy_21d_slope_v114_signal(closeadj):
    base = _stretch(closeadj, 21).clip(lower=0).rolling(21, min_periods=10).sum()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume imbalance, 21d ROC
def f05pb_f05_parabolic_blowoff_volimbal_21d_slope_v115_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    upv = (volume * up).rolling(21, min_periods=10).sum()
    dnv = (volume * (1 - up)).rolling(21, min_periods=10).sum()
    base = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stochastic %K, 21d ROC
def f05pb_f05_parabolic_blowoff_stoch_21d_slope_v116_signal(closeadj, high, low):
    hh, ll = _rmax(high, 14), _rmin(low, 14)
    base = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of skew, 21d ROC
def f05pb_f05_parabolic_blowoff_skew_21d_slope_v117_signal(closeadj):
    base = closeadj.pct_change().rolling(21, min_periods=10).skew()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of kurtosis, 21d ROC
def f05pb_f05_parabolic_blowoff_kurt_21d_slope_v118_signal(closeadj):
    base = closeadj.pct_change().rolling(21, min_periods=12).kurt()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of run-efficiency, 21d ROC
def f05pb_f05_parabolic_blowoff_runeff_21d_slope_v119_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    base = net / path.replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of peak-over-trend, 21d ROC
def f05pb_f05_parabolic_blowoff_peaktrend_21db_slope_v120_signal(closeadj):
    base = np.log(_rmax(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 63).replace(0, np.nan))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch above 5d MA scaled by vol (micro-extension), 5d ROC
def f05pb_f05_parabolic_blowoff_stretchvol5_5d_slope_v121_signal(closeadj):
    s = _stretch(closeadj, 5)
    base = s / closeadj.pct_change().rolling(21, min_periods=10).std().replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d/63d run-acceleration, 10d ROC
def f05pb_f05_parabolic_blowoff_runaccel_10d_slope_v122_signal(closeadj):
    r21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    r63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    base = r21 - r63 / 3.0
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of spike-concentration over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_spikeconc_10d_slope_v123_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = (lr.rolling(21, min_periods=10).max() / lr.rolling(21, min_periods=10).sum().replace(0, np.nan)).clip(-3, 3)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of thrust(5d move in week-ATR), 5d/126 (regime-relative thrust speed)
def f05pb_f05_parabolic_blowoff_thrustweek_5d_slope_v124_signal(closeadj, high, low):
    base = (closeadj - closeadj.shift(5)) / _atr(high, low, closeadj, 5).replace(0, np.nan)
    result = _rankslope(base, 5, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-confirmed new-high tally, 10d ROC
def f05pb_f05_parabolic_blowoff_volconfhigh_10d_slope_v125_signal(closeadj, volume):
    fresh = (closeadj > closeadj.shift(1).rolling(21, min_periods=10).max()).astype(float)
    base = (fresh * _volspike(volume, 63)).rolling(21, min_periods=10).sum()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CCI-style typical-price extension over 14d, 21d ROC
def f05pb_f05_parabolic_blowoff_williamsr_21d_slope_v126_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(14, min_periods=7).mean()
    md = (tp - sma).abs().rolling(14, min_periods=7).mean()
    base = (tp - sma) / (0.015 * md).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA(13) convexity base, 5d ROC
def f05pb_f05_parabolic_blowoff_emaconvex_5d_slope_v127_signal(closeadj):
    lp = np.log(_ema(closeadj, 13).replace(0, np.nan))
    base = (lp.diff() - lp.diff().shift(3)).rolling(3, min_periods=2).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of give-back ratio (worst 3d drop / 21d run), 10d ROC
def f05pb_f05_parabolic_blowoff_giveback_10d_slope_v128_signal(closeadj):
    drop3 = (closeadj / _rmax(closeadj, 3).replace(0, np.nan) - 1.0)
    worst = drop3.rolling(21, min_periods=10).min().abs()
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan)).abs() + 0.02
    base = worst / run
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-froth (dollar-vol z x stretch), 10d ROC
def f05pb_f05_parabolic_blowoff_dollfroth_10d_slope_v129_signal(closeadj, volume):
    dz = _z(closeadj * volume, 63).clip(lower=0)
    base = dz * _stretch(closeadj, 21).clip(lower=0)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch-drop-from-peak (in vol units), 5d ROC
def f05pb_f05_parabolic_blowoff_stretchdrop_5d_slope_v130_signal(closeadj):
    s = _stretch(closeadj, 21)
    base = (s.rolling(10, min_periods=5).max() - s) / s.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of clean-run (63d ret / 63d maxdd), 21d ROC
def f05pb_f05_parabolic_blowoff_cleanrun_21d_slope_v131_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    peak = closeadj.rolling(63, min_periods=21).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).min().abs()
    base = ret.clip(lower=0) / (dd.replace(0, np.nan) + 0.05)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ext50-rank, 21d ROC
def f05pb_f05_parabolic_blowoff_ext50rank_21d_slope_v132_signal(closeadj):
    ext = closeadj / _mean(closeadj, 50).replace(0, np.nan) - 1.0
    base = ext.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fresh-high rate (composite), 10d ROC
def f05pb_f05_parabolic_blowoff_freshrate_10d_slope_v133_signal(closeadj):
    fresh = (closeadj > closeadj.shift(1).rolling(21, min_periods=10).max()).astype(float)
    base = fresh.rolling(21, min_periods=10).mean() + 2.0 * _stretch(closeadj, 21).clip(lower=0)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stretch-z-gap (21d minus 126d z), 10d ROC
def f05pb_f05_parabolic_blowoff_stretchzgap_10d_slope_v134_signal(closeadj):
    s = _stretch(closeadj, 21)
    base = _z(s, 21) - _z(s, 126)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# residual slope of ATR-ext above 10d MA: 10d slope minus 21d slope (de-trended)
def f05pb_f05_parabolic_blowoff_atrext10_10d_slope_v135_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 10, 10)
    result = _residslope(base, 10, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA(8)-vs-(34) ribbon, 21d ROC
def f05pb_f05_parabolic_blowoff_ribbon8v34_21d_slope_v136_signal(closeadj):
    base = (_ema(closeadj, 8) - _ema(closeadj, 34)) / _ema(closeadj, 34).replace(0, np.nan)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upper-wick rejection over 10d, 5d ROC
def f05pb_f05_parabolic_blowoff_rejectwick_5d_slope_v137_signal(closeadj, high, low):
    rng = (high - low).replace(0, np.nan)
    upsh = (high - np.maximum(closeadj, closeadj.shift(1))) / rng
    base = upsh.rolling(10, min_periods=5).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of RSI-divergence (px rank - rsi rank), 10d ROC
def f05pb_f05_parabolic_blowoff_rsidiverg_10d_slope_v138_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    px = closeadj.pct_change(21)
    base = px.rolling(63, min_periods=21).rank(pct=True) - rsi.rolling(63, min_periods=21).rank(pct=True)
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of stretch-asymmetry (s minus its 5d mean), span 8
def f05pb_f05_parabolic_blowoff_extasym_5d_slope_v139_signal(closeadj):
    s = _stretch(closeadj, 21)
    base = s - s.rolling(5, min_periods=3).mean()
    result = _emaslope(base, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max-burst, 10d ROC
def f05pb_f05_parabolic_blowoff_maxburst_10d_slope_v140_signal(closeadj):
    r3 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(3).replace(0, np.nan))
    base = r3.rolling(21, min_periods=10).max()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# standardized slope of volume-spike-accel (5d minus 21d normalized), z-scored
def f05pb_f05_parabolic_blowoff_volspikeaccel_5d_slope_v141_signal(volume):
    av = volume.rolling(63, min_periods=21).mean()
    base = volume.rolling(5, min_periods=3).mean() / av.replace(0, np.nan) - volume.rolling(21, min_periods=10).mean() / av.replace(0, np.nan)
    result = _zslope(base, 5, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of swing-top (run x lower-high), 5d ROC
def f05pb_f05_parabolic_blowoff_swingtop_5d_slope_v142_signal(closeadj):
    run = np.log(closeadj.shift(5).replace(0, np.nan) / closeadj.shift(15).replace(0, np.nan)).clip(lower=0)
    lower_high = (_rmax(closeadj, 5) < _rmax(closeadj, 5).shift(5)).astype(float)
    base = run * lower_high
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trend-residual, 21d ROC
def f05pb_f05_parabolic_blowoff_trendresid_21d_slope_v143_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp - (2.0 * lp.rolling(11, min_periods=6).mean() - lp.rolling(21, min_periods=10).mean())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slope of ATR-ext above 34d MA, span 21
def f05pb_f05_parabolic_blowoff_atrext34_21d_slope_v144_signal(closeadj, high, low):
    base = _above_ma_atr(closeadj, high, low, 34, 21)
    result = _emaslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upside-semivar share, 21d ROC
def f05pb_f05_parabolic_blowoff_upsemivar_21d_slope_v145_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0).pow(2).rolling(21, min_periods=10).sum()
    tot = r.pow(2).rolling(21, min_periods=10).sum()
    base = up / tot.replace(0, np.nan) - 0.5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-trend, 21d ROC
def f05pb_f05_parabolic_blowoff_voltrend_21d_slope_v146_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    base = (lv - lv.shift(21)) / 21.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-vol peak spike over 21d, 10d ROC
def f05pb_f05_parabolic_blowoff_dollpeak_10d_slope_v147_signal(closeadj, volume):
    dv = closeadj * volume
    spike = dv / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = spike.rolling(21, min_periods=10).max()
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of hi-fade momentum near the high, 5d ROC
def f05pb_f05_parabolic_blowoff_hifade_5d_slope_v148_signal(closeadj):
    prox = closeadj / _rmax(closeadj, 21).replace(0, np.nan)
    base = (prox - prox.shift(5)) * (prox > 0.95).astype(float)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# rank-of-slope of run-sigma (10d run in sigma units), 5d/126 (regime-relative)
def f05pb_f05_parabolic_blowoff_runsigma_5d_slope_v149_signal(closeadj):
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = run / (vol.replace(0, np.nan) * np.sqrt(10.0))
    result = _rankslope(base, 5, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of terminal-blowoff composite (stretch-rank x vol-rank x up-frac), 10d ROC
def f05pb_f05_parabolic_blowoff_terminal_10d_slope_v150_signal(closeadj, volume):
    sr = _stretch(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    vr = _z(volume, 63).rolling(252, min_periods=63).rank(pct=True)
    up = (closeadj.diff() > 0).astype(float).rolling(10, min_periods=5).mean()
    base = sr * vr * up
    result = _slope(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05pb_f05_parabolic_blowoff_stretch21_5d_slope_v001_signal,
    f05pb_f05_parabolic_blowoff_stretch21_21d_slope_v002_signal,
    f05pb_f05_parabolic_blowoff_stretch10_5d_slope_v003_signal,
    f05pb_f05_parabolic_blowoff_stretch63_21d_slope_v004_signal,
    f05pb_f05_parabolic_blowoff_stretch34_10d_slope_v005_signal,
    f05pb_f05_parabolic_blowoff_ribbon8v34_5d_slope_v006_signal,
    f05pb_f05_parabolic_blowoff_ribbonwidth_5d_slope_v007_signal,
    f05pb_f05_parabolic_blowoff_atrext21_5d_slope_v008_signal,
    f05pb_f05_parabolic_blowoff_atrext21_21d_slope_v009_signal,
    f05pb_f05_parabolic_blowoff_atrext63_21d_slope_v010_signal,
    f05pb_f05_parabolic_blowoff_atrext10_5d_slope_v011_signal,
    f05pb_f05_parabolic_blowoff_runslope5_5d_slope_v012_signal,
    f05pb_f05_parabolic_blowoff_runslope10_5d_slope_v013_signal,
    f05pb_f05_parabolic_blowoff_runslope21_21d_slope_v014_signal,
    f05pb_f05_parabolic_blowoff_volspike_5d_slope_v015_signal,
    f05pb_f05_parabolic_blowoff_volz_5d_slope_v016_signal,
    f05pb_f05_parabolic_blowoff_dollvolspike_5d_slope_v017_signal,
    f05pb_f05_parabolic_blowoff_fade21_5d_slope_v018_signal,
    f05pb_f05_parabolic_blowoff_pctb_5d_slope_v019_signal,
    f05pb_f05_parabolic_blowoff_sigmaext_5d_slope_v020_signal,
    f05pb_f05_parabolic_blowoff_rsi_5d_slope_v021_signal,
    f05pb_f05_parabolic_blowoff_williamsr_5d_slope_v022_signal,
    f05pb_f05_parabolic_blowoff_rangeexp_5d_slope_v023_signal,
    f05pb_f05_parabolic_blowoff_volratio_5d_slope_v024_signal,
    f05pb_f05_parabolic_blowoff_maspread_5d_slope_v025_signal,
    f05pb_f05_parabolic_blowoff_peaktrend_21d_slope_v026_signal,
    f05pb_f05_parabolic_blowoff_stretchenergy_5d_slope_v027_signal,
    f05pb_f05_parabolic_blowoff_volimbal_5d_slope_v028_signal,
    f05pb_f05_parabolic_blowoff_upsemivar_5d_slope_v029_signal,
    f05pb_f05_parabolic_blowoff_stoch_5d_slope_v030_signal,
    f05pb_f05_parabolic_blowoff_parkinson_5d_slope_v031_signal,
    f05pb_f05_parabolic_blowoff_volherf_5d_slope_v032_signal,
    f05pb_f05_parabolic_blowoff_stretch13_5d_slope_v033_signal,
    f05pb_f05_parabolic_blowoff_emastretch10_5d_slope_v034_signal,
    f05pb_f05_parabolic_blowoff_maatr5v63_10d_slope_v035_signal,
    f05pb_f05_parabolic_blowoff_skew_5d_slope_v036_signal,
    f05pb_f05_parabolic_blowoff_kurt_5d_slope_v037_signal,
    f05pb_f05_parabolic_blowoff_volofvol_10d_slope_v038_signal,
    f05pb_f05_parabolic_blowoff_runeff_5d_slope_v039_signal,
    f05pb_f05_parabolic_blowoff_volsurgeema_5d_slope_v040_signal,
    f05pb_f05_parabolic_blowoff_freshpeak_21d_slope_v041_signal,
    f05pb_f05_parabolic_blowoff_offtop_5d_slope_v042_signal,
    f05pb_f05_parabolic_blowoff_mafan_5d_slope_v043_signal,
    f05pb_f05_parabolic_blowoff_autocorr_10d_slope_v044_signal,
    f05pb_f05_parabolic_blowoff_trendresid_5d_slope_v045_signal,
    f05pb_f05_parabolic_blowoff_ext50_10d_slope_v046_signal,
    f05pb_f05_parabolic_blowoff_gaprun_5d_slope_v047_signal,
    f05pb_f05_parabolic_blowoff_stretchsharp_5d_slope_v048_signal,
    f05pb_f05_parabolic_blowoff_angle_10d_slope_v049_signal,
    f05pb_f05_parabolic_blowoff_maxburst_5d_slope_v050_signal,
    f05pb_f05_parabolic_blowoff_stretch21_10d_slope_v051_signal,
    f05pb_f05_parabolic_blowoff_stretch10_10d_slope_v052_signal,
    f05pb_f05_parabolic_blowoff_stretch63_10d_slope_v053_signal,
    f05pb_f05_parabolic_blowoff_atrext21_10d_slope_v054_signal,
    f05pb_f05_parabolic_blowoff_atrext34_10d_slope_v055_signal,
    f05pb_f05_parabolic_blowoff_runslope5_3d_slope_v056_signal,
    f05pb_f05_parabolic_blowoff_runslope10_10d_slope_v057_signal,
    f05pb_f05_parabolic_blowoff_volspike_10d_slope_v058_signal,
    f05pb_f05_parabolic_blowoff_volz_10d_slope_v059_signal,
    f05pb_f05_parabolic_blowoff_fade21_10d_slope_v060_signal,
    f05pb_f05_parabolic_blowoff_pctb_10d_slope_v061_signal,
    f05pb_f05_parabolic_blowoff_sigmaext_10d_slope_v062_signal,
    f05pb_f05_parabolic_blowoff_rsi_10d_slope_v063_signal,
    f05pb_f05_parabolic_blowoff_rangeexp_10d_slope_v064_signal,
    f05pb_f05_parabolic_blowoff_volratio_10d_slope_v065_signal,
    f05pb_f05_parabolic_blowoff_maspread_10d_slope_v066_signal,
    f05pb_f05_parabolic_blowoff_stretchenergy_10d_slope_v067_signal,
    f05pb_f05_parabolic_blowoff_volimbal_10d_slope_v068_signal,
    f05pb_f05_parabolic_blowoff_upsemivar_10d_slope_v069_signal,
    f05pb_f05_parabolic_blowoff_stoch_10d_slope_v070_signal,
    f05pb_f05_parabolic_blowoff_parkinson_10d_slope_v071_signal,
    f05pb_f05_parabolic_blowoff_volherf_10d_slope_v072_signal,
    f05pb_f05_parabolic_blowoff_stretch13_10d_slope_v073_signal,
    f05pb_f05_parabolic_blowoff_emastretch10_10d_slope_v074_signal,
    f05pb_f05_parabolic_blowoff_peaktrend_10d_slope_v075_signal,
    f05pb_f05_parabolic_blowoff_skew_10d_slope_v076_signal,
    f05pb_f05_parabolic_blowoff_runeff_10d_slope_v077_signal,
    f05pb_f05_parabolic_blowoff_dollvolspike_10d_slope_v078_signal,
    f05pb_f05_parabolic_blowoff_offtop_10d_slope_v079_signal,
    f05pb_f05_parabolic_blowoff_mafan_10d_slope_v080_signal,
    f05pb_f05_parabolic_blowoff_ribbon8v34_10d_slope_v081_signal,
    f05pb_f05_parabolic_blowoff_trendresid_10d_slope_v082_signal,
    f05pb_f05_parabolic_blowoff_ext50_21d_slope_v083_signal,
    f05pb_f05_parabolic_blowoff_williamsr_10d_slope_v084_signal,
    f05pb_f05_parabolic_blowoff_stretchmed8_5d_slope_v085_signal,
    f05pb_f05_parabolic_blowoff_runintensity_5d_slope_v086_signal,
    f05pb_f05_parabolic_blowoff_voltrend_10d_slope_v087_signal,
    f05pb_f05_parabolic_blowoff_volretcorr_10d_slope_v088_signal,
    f05pb_f05_parabolic_blowoff_updollshare_5d_slope_v089_signal,
    f05pb_f05_parabolic_blowoff_squeezepop_10d_slope_v090_signal,
    f05pb_f05_parabolic_blowoff_frothpeak_21d_slope_v091_signal,
    f05pb_f05_parabolic_blowoff_obtime_10d_slope_v092_signal,
    f05pb_f05_parabolic_blowoff_accelindex_5d_slope_v093_signal,
    f05pb_f05_parabolic_blowoff_maxext_10d_slope_v094_signal,
    f05pb_f05_parabolic_blowoff_stretchrange_10d_slope_v095_signal,
    f05pb_f05_parabolic_blowoff_atrthrust_5d_slope_v096_signal,
    f05pb_f05_parabolic_blowoff_movebudget_10d_slope_v097_signal,
    f05pb_f05_parabolic_blowoff_fragility_5d_slope_v098_signal,
    f05pb_f05_parabolic_blowoff_compz_10d_slope_v099_signal,
    f05pb_f05_parabolic_blowoff_ribbonwidth_3d_slope_v100_signal,
    f05pb_f05_parabolic_blowoff_stretch10_21d_slope_v101_signal,
    f05pb_f05_parabolic_blowoff_stretch34_21d_slope_v102_signal,
    f05pb_f05_parabolic_blowoff_atrext21_3d_slope_v103_signal,
    f05pb_f05_parabolic_blowoff_atrext63_10d_slope_v104_signal,
    f05pb_f05_parabolic_blowoff_runslope21_10d_slope_v105_signal,
    f05pb_f05_parabolic_blowoff_volspike_21d_slope_v106_signal,
    f05pb_f05_parabolic_blowoff_fade21_21d_slope_v107_signal,
    f05pb_f05_parabolic_blowoff_pctb_21d_slope_v108_signal,
    f05pb_f05_parabolic_blowoff_sigmaext_21d_slope_v109_signal,
    f05pb_f05_parabolic_blowoff_rsi_21d_slope_v110_signal,
    f05pb_f05_parabolic_blowoff_rangeexp_21d_slope_v111_signal,
    f05pb_f05_parabolic_blowoff_volratio_21d_slope_v112_signal,
    f05pb_f05_parabolic_blowoff_maspread_21d_slope_v113_signal,
    f05pb_f05_parabolic_blowoff_stretchenergy_21d_slope_v114_signal,
    f05pb_f05_parabolic_blowoff_volimbal_21d_slope_v115_signal,
    f05pb_f05_parabolic_blowoff_stoch_21d_slope_v116_signal,
    f05pb_f05_parabolic_blowoff_skew_21d_slope_v117_signal,
    f05pb_f05_parabolic_blowoff_kurt_21d_slope_v118_signal,
    f05pb_f05_parabolic_blowoff_runeff_21d_slope_v119_signal,
    f05pb_f05_parabolic_blowoff_peaktrend_21db_slope_v120_signal,
    f05pb_f05_parabolic_blowoff_stretchvol5_5d_slope_v121_signal,
    f05pb_f05_parabolic_blowoff_runaccel_10d_slope_v122_signal,
    f05pb_f05_parabolic_blowoff_spikeconc_10d_slope_v123_signal,
    f05pb_f05_parabolic_blowoff_thrustweek_5d_slope_v124_signal,
    f05pb_f05_parabolic_blowoff_volconfhigh_10d_slope_v125_signal,
    f05pb_f05_parabolic_blowoff_williamsr_21d_slope_v126_signal,
    f05pb_f05_parabolic_blowoff_emaconvex_5d_slope_v127_signal,
    f05pb_f05_parabolic_blowoff_giveback_10d_slope_v128_signal,
    f05pb_f05_parabolic_blowoff_dollfroth_10d_slope_v129_signal,
    f05pb_f05_parabolic_blowoff_stretchdrop_5d_slope_v130_signal,
    f05pb_f05_parabolic_blowoff_cleanrun_21d_slope_v131_signal,
    f05pb_f05_parabolic_blowoff_ext50rank_21d_slope_v132_signal,
    f05pb_f05_parabolic_blowoff_freshrate_10d_slope_v133_signal,
    f05pb_f05_parabolic_blowoff_stretchzgap_10d_slope_v134_signal,
    f05pb_f05_parabolic_blowoff_atrext10_10d_slope_v135_signal,
    f05pb_f05_parabolic_blowoff_ribbon8v34_21d_slope_v136_signal,
    f05pb_f05_parabolic_blowoff_rejectwick_5d_slope_v137_signal,
    f05pb_f05_parabolic_blowoff_rsidiverg_10d_slope_v138_signal,
    f05pb_f05_parabolic_blowoff_extasym_5d_slope_v139_signal,
    f05pb_f05_parabolic_blowoff_maxburst_10d_slope_v140_signal,
    f05pb_f05_parabolic_blowoff_volspikeaccel_5d_slope_v141_signal,
    f05pb_f05_parabolic_blowoff_swingtop_5d_slope_v142_signal,
    f05pb_f05_parabolic_blowoff_trendresid_21d_slope_v143_signal,
    f05pb_f05_parabolic_blowoff_atrext34_21d_slope_v144_signal,
    f05pb_f05_parabolic_blowoff_upsemivar_21d_slope_v145_signal,
    f05pb_f05_parabolic_blowoff_voltrend_21d_slope_v146_signal,
    f05pb_f05_parabolic_blowoff_dollpeak_10d_slope_v147_signal,
    f05pb_f05_parabolic_blowoff_hifade_5d_slope_v148_signal,
    f05pb_f05_parabolic_blowoff_runsigma_5d_slope_v149_signal,
    f05pb_f05_parabolic_blowoff_terminal_10d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_PARABOLIC_BLOWOFF_REGISTRY_2ND_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f05_parabolic_blowoff_2nd_derivatives_001_150_claude: %d features pass" % n_features)
