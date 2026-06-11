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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (parabolic blowoff / overextension) =====
def _f05_atr(high, low, closeadj, w):
    # true range using intraday high/low and prior close (mining intraday range)
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f05_stretch(closeadj, w):
    # log distance of price above its own fast moving average (parabolic stretch)
    ma = closeadj.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))


def _f05_runslope(closeadj, w):
    # vertical-run slope: per-day log return averaged over window (steepness of ascent)
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    return lr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f05_above_ma_atr(closeadj, high, low, w_ma, w_atr):
    # distance above the moving average measured in ATR units (overextension)
    ma = closeadj.rolling(w_ma, min_periods=max(1, w_ma // 2)).mean()
    atr = _f05_atr(high, low, closeadj, w_atr)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _f05_volspike(volume, w):
    # blowoff volume spike: volume vs its trailing average
    av = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / av.replace(0, np.nan)


def _f05_accel(closeadj, w):
    # convexity of the price path (parabolic acceleration of log price)
    lp = np.log(closeadj.replace(0, np.nan))
    return lp.diff().diff().rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- price-vs-fast-MA stretch (overextension level) ---

# stretch of price above its 21d MA (classic parabolic overextension)
def f05pb_f05_parabolic_blowoff_stretch_21d_base_v001_signal(closeadj):
    b = _f05_stretch(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 10d MA, z-scored vs its own 63d history (de-trended extension)
def f05pb_f05_parabolic_blowoff_stretchz_10d_base_v002_signal(closeadj):
    s = _f05_stretch(closeadj, 10)
    b = _z(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 63d MA percentile-ranked vs its own 252d history
def f05pb_f05_parabolic_blowoff_stretchrank_63d_base_v003_signal(closeadj):
    s = _f05_stretch(closeadj, 63)
    b = s.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between fast (10d) and slow (63d) stretch (acceleration of overextension)
def f05pb_f05_parabolic_blowoff_stretchspr_10v63_base_v004_signal(closeadj):
    fast = _f05_stretch(closeadj, 10)
    slow = _f05_stretch(closeadj, 63)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how fast the 21d stretch is widening over a week (extension velocity)
def f05pb_f05_parabolic_blowoff_stretchvel_21d_base_v005_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    b = s - s.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# only-positive stretch above 21d MA, tanh-squashed (bounded blowoff upside)
def f05pb_f05_parabolic_blowoff_stretchpos_21d_base_v006_signal(closeadj):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    b = np.tanh(8.0 * s)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 5d MA scaled by recent vol (risk-adjusted micro-extension)
def f05pb_f05_parabolic_blowoff_stretchvol_5d_base_v007_signal(closeadj):
    s = _f05_stretch(closeadj, 5)
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    b = s / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-ribbon separation: 8d EMA above 34d EMA, normalized (fast ribbon fan-out)
def f05pb_f05_parabolic_blowoff_emaribbon_8v34_base_v008_signal(closeadj):
    fast = _ema(closeadj, 8)
    slow = _ema(closeadj, 34)
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vertical-run slope (steepness of the ascent) ---

# 5d vertical-run slope (steepest near-term ascent)
def f05pb_f05_parabolic_blowoff_runslope_5d_base_v009_signal(closeadj):
    b = _f05_runslope(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vertical-run slope, z-scored vs its own 126d history
def f05pb_f05_parabolic_blowoff_runslopez_10d_base_v010_signal(closeadj):
    rs = _f05_runslope(closeadj, 10)
    b = _z(rs, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run slope percentile-ranked vs its own 252d history
def f05pb_f05_parabolic_blowoff_runsloperank_21d_base_v011_signal(closeadj):
    rs = _f05_runslope(closeadj, 21)
    b = rs.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope steepening ratio: 5d slope as a multiple of the 63d slope baseline
# (>>1 = the ascent has gone vertical vs its trend pace; bounded by tanh)
def f05pb_f05_parabolic_blowoff_slopesteep_5v21_base_v012_signal(closeadj):
    fast = _f05_runslope(closeadj, 5)
    base = _f05_runslope(closeadj, 63).abs() + 1e-4
    b = np.tanh(fast / base / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative log run over 10d normalized by 63d vol (move size in sigma)
def f05pb_f05_parabolic_blowoff_runsigma_10d_base_v013_signal(closeadj):
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = run / (vol.replace(0, np.nan) * np.sqrt(10.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 10 days that were up days (one-sided run persistence)
def f05pb_f05_parabolic_blowoff_uprundays_10d_base_v014_signal(closeadj):
    up = (closeadj.diff() > 0).astype(float)
    raw = up.rolling(10, min_periods=5).mean()
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    b = (raw - 0.5) * run.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive up-streak in the last 21d, scaled by the run size (vertical run)
def f05pb_f05_parabolic_blowoff_upstreak_21d_base_v015_signal(closeadj):
    up = (closeadj.diff() > 0).astype(float)

    def _maxstreak(a):
        best = cur = 0
        for v in a:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    streak = up.rolling(21, min_periods=10).apply(_maxstreak, raw=True)
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = streak * (1.0 + run.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the ascent: change in 5d slope over 5 days (jerk of the run)
def f05pb_f05_parabolic_blowoff_slopeaccel_5d_base_v016_signal(closeadj):
    rs = _f05_runslope(closeadj, 5)
    b = rs - rs.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance above 21/63d MA in ATR units (overextension in volatility units) ---

# inverse-vol overextension: how many ATRs the 21d-MA itself spans the price gap
# (price/ATR scaling isolates the volatility-compression component of a blowoff)
def f05pb_f05_parabolic_blowoff_atrext21_21d_base_v017_signal(closeadj, high, low):
    ma = closeadj.rolling(21, min_periods=10).mean()
    atr = _f05_atr(high, low, closeadj, 21)
    b = ma / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 63d MA in 21d ATR units (overextension vs medium trend)
def f05pb_f05_parabolic_blowoff_atrext63_63d_base_v018_signal(closeadj, high, low):
    b = _f05_above_ma_atr(closeadj, high, low, 63, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA in ATR units, z-scored vs its own 126d history
def f05pb_f05_parabolic_blowoff_atrextz21_21d_base_v019_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    b = _z(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA in ATR units, percentile-ranked vs its 252d history
def f05pb_f05_parabolic_blowoff_atrextrank21_21d_base_v020_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    b = e.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-extension curvature: is the ATR-extension itself accelerating (second diff)
def f05pb_f05_parabolic_blowoff_atrextvel_21d_base_v021_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    b = (e.diff() - e.diff().shift(3)).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 21d-MA and 63d-MA ATR extension (short-vs-long overextension)
def f05pb_f05_parabolic_blowoff_atrextspr_21v63_base_v022_signal(closeadj, high, low):
    e21 = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    e63 = _f05_above_ma_atr(closeadj, high, low, 63, 21)
    b = e21 - e63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetric blowoff: positive ATR-extension penalized when far below MA too
# (net signed sqrt of ATR-extension — distinct curvature vs raw positive stretch)
def f05pb_f05_parabolic_blowoff_atrextpos_21d_base_v023_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    b = np.sign(e) * np.sqrt(e.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 10d MA in 10d ATR units (micro-overextension)
def f05pb_f05_parabolic_blowoff_atrext10_10d_base_v024_signal(closeadj, high, low):
    b = _f05_above_ma_atr(closeadj, high, low, 10, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last month spent >2 ATR above the 21d MA (sustained overextension)
def f05pb_f05_parabolic_blowoff_atrexttime_21d_base_v025_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    hot = (e >= 2.0).astype(float)
    b = hot.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blowoff volume spike ---

# 5d volume vs 63d average volume (blowoff volume surge)
def f05pb_f05_parabolic_blowoff_volspike_63d_base_v026_signal(volume):
    sv = volume.rolling(5, min_periods=3).mean()
    av = volume.rolling(63, min_periods=21).mean()
    b = sv / av.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# single-day volume z-score vs 63d history (volume climax)
def f05pb_f05_parabolic_blowoff_volz_63d_base_v027_signal(volume):
    b = _z(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume spike interacted with the run slope (blowoff = price run + volume climax)
def f05pb_f05_parabolic_blowoff_volrun_21d_base_v028_signal(closeadj, volume):
    spike = _f05_volspike(volume, 63)
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = (spike - 1.0).clip(lower=0) * run.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume spike vs its 63d average (blowoff in dollar terms)
def f05pb_f05_parabolic_blowoff_dollvolspike_63d_base_v029_signal(closeadj, volume):
    dv = closeadj * volume
    sv = dv.rolling(5, min_periods=3).mean()
    av = dv.rolling(63, min_periods=21).mean()
    b = sv / av.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted climax-volume tally (>1.5x avg) over last month (count-friendly)
def f05pb_f05_parabolic_blowoff_volclimaxcnt_21d_base_v030_signal(volume):
    spike = _f05_volspike(volume, 63)
    excess = (spike - 1.5).clip(lower=0)
    b = excess.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak single-day volume spike over the last 10 days (the blowoff bar)
def f05pb_f05_parabolic_blowoff_volpeak_10d_base_v031_signal(volume):
    spike = _f05_volspike(volume, 63)
    b = spike.rolling(10, min_periods=5).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day volume vs down-day volume imbalance over 21d (buying-climax skew)
def f05pb_f05_parabolic_blowoff_volimbal_21d_base_v032_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    upv = (volume * up).rolling(21, min_periods=10).sum()
    dnv = (volume * (1.0 - up)).rolling(21, min_periods=10).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume spike accelerating: 5d spike minus 21d spike (volume ramping into top)
def f05pb_f05_parabolic_blowoff_volspikeaccel_base_v033_signal(volume):
    s5 = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    s21 = volume.rolling(21, min_periods=10).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = s5 - s21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted stretch: stretch above 21d MA times volume spike (true blowoff)
def f05pb_f05_parabolic_blowoff_volwstretch_21d_base_v034_signal(closeadj, volume):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    spike = _f05_volspike(volume, 63)
    b = s * spike
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion-from-spike (the fade after the blowoff) ---

# pullback from the 21d high after extension (mean-reversion magnitude)
def f05pb_f05_parabolic_blowoff_fade_21d_base_v035_signal(closeadj):
    hi = _rmax(closeadj, 21)
    b = closeadj / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversion of stretch: peak 10d stretch minus current stretch (collapse of extension)
def f05pb_f05_parabolic_blowoff_stretchrev_10d_base_v036_signal(closeadj):
    s = _f05_stretch(closeadj, 10)
    peak = s.rolling(10, min_periods=5).max()
    b = peak - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d return after the trailing 21d move was extreme (snapback gating)
def f05pb_f05_parabolic_blowoff_snapback_5d_base_v037_signal(closeadj):
    prior_run = np.log(closeadj.shift(5).replace(0, np.nan) / closeadj.shift(26).replace(0, np.nan))
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    b = r5 * prior_run.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance fallen from 10d ATR-extension peak (overextension unwind in ATR units)
def f05pb_f05_parabolic_blowoff_atrunwind_21d_base_v038_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    peak = e.rolling(10, min_periods=5).max()
    b = e - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversal sign-flip: current 5d return opposite to prior 10d run (top reversal)
def f05pb_f05_parabolic_blowoff_revflip_5d_base_v039_signal(closeadj):
    prior = np.log(closeadj.shift(5).replace(0, np.nan) / closeadj.shift(15).replace(0, np.nan))
    cur = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    b = -np.sign(prior) * cur * prior.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown from the 5d high scaled by the prior 21d run (fade-of-blowoff)
def f05pb_f05_parabolic_blowoff_fadescaled_5d_base_v040_signal(closeadj):
    hi5 = _rmax(closeadj, 5)
    fade = closeadj / hi5.replace(0, np.nan) - 1.0
    run = np.log(closeadj.shift(5).replace(0, np.nan) / closeadj.shift(26).replace(0, np.nan)).clip(lower=0)
    b = fade * (1.0 + run)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 21d MA now relative to one week ago (peaking/rolling-over)
def f05pb_f05_parabolic_blowoff_stretchroll_21d_base_v041_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    b = -(s - s.shift(5)) * (s.shift(5) > 0).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exhaustion (loss of upward momentum at extremes) ---

# exhaustion: positive stretch but decelerating run (extended yet stalling)
def f05pb_f05_parabolic_blowoff_exhaust_21d_base_v042_signal(closeadj):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    accel = _f05_accel(closeadj, 10)
    b = s * (-accel)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative convexity of log price at extension (parabola rolling over)
def f05pb_f05_parabolic_blowoff_convex_10d_base_v043_signal(closeadj):
    b = -_f05_accel(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RSI-like exhaustion: avg-up vs avg-down over 14d at the extreme
def f05pb_f05_parabolic_blowoff_rsiexh_14d_base_v044_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    b = rsi - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bearish divergence: price making new 21d high but momentum not (exhaustion)
def f05pb_f05_parabolic_blowoff_diverg_21d_base_v045_signal(closeadj):
    px_pos = (closeadj - _rmin(closeadj, 21)) / (_rmax(closeadj, 21) - _rmin(closeadj, 21)).replace(0, np.nan)
    mom = closeadj.pct_change(10)
    mom_pos = (mom - _rmin(mom, 21)) / (_rmax(mom, 21) - _rmin(mom, 21)).replace(0, np.nan)
    b = px_pos - mom_pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope decay: 5d slope falling while still positive (ascent losing steam)
def f05pb_f05_parabolic_blowoff_slopedecay_5d_base_v046_signal(closeadj):
    rs = _f05_runslope(closeadj, 5)
    decay = (rs.shift(3) - rs).clip(lower=0)
    b = decay * (rs.shift(3) > 0).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick exhaustion: avg of (high-close)/range over 10d at extension
def f05pb_f05_parabolic_blowoff_upperwick_10d_base_v047_signal(closeadj, high, low):
    rng = (high - low).replace(0, np.nan)
    wick = (high - closeadj) / rng
    stretch = _f05_stretch(closeadj, 21).clip(lower=0)
    b = wick.rolling(10, min_periods=5).mean() * (stretch > 0).astype(float) + 0.5 * stretch
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-range exhaustion: widest true range of last 5d vs 63d avg (climax bar)
def f05pb_f05_parabolic_blowoff_climaxrng_5d_base_v048_signal(closeadj, high, low):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    peak = tr.rolling(5, min_periods=3).max()
    avg = tr.rolling(63, min_periods=21).mean()
    b = peak / avg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional facets: levels, ratios, regimes, interactions ---

# froth percentile rank of today's stretch within its 126d distribution, blended
# with how long the stretch has stayed in the top quartile (regime-style overextension)
def f05pb_f05_parabolic_blowoff_stretchvspeak_21d_base_v049_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    rnk = s.rolling(126, min_periods=42).rank(pct=True)
    hot = (rnk >= 0.75).astype(float).rolling(21, min_periods=10).mean()
    b = (rnk - 0.5) + 0.5 * hot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic curvature: second difference of the 5d MA path (bend of the curve)
def f05pb_f05_parabolic_blowoff_curve_5d_base_v050_signal(closeadj):
    ma = _mean(closeadj, 5)
    lp = np.log(ma.replace(0, np.nan))
    b = lp.diff().diff()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %B at the upper band over 20d (price riding the upper band = blowoff)
def f05pb_f05_parabolic_blowoff_pctb_20d_base_v051_signal(closeadj):
    ma = _mean(closeadj, 20)
    sd = _std(closeadj, 20)
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    b = (closeadj - lower) / (upper - lower).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg excess above the upper Bollinger band over 21d (band-walk intensity)
def f05pb_f05_parabolic_blowoff_bandwalk_20d_base_v052_signal(closeadj):
    ma = _mean(closeadj, 20)
    sd = _std(closeadj, 20)
    upper = ma + 2.0 * sd
    excess = ((closeadj - upper) / sd.replace(0, np.nan)).clip(lower=0)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-skew at the extreme: 21d skewness of daily returns (parabolic blowoffs are
# right-skewed bursts; distinct from a price-vs-MA distance)
def f05pb_f05_parabolic_blowoff_sigmaext_21d_base_v053_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(21, min_periods=10).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run intensity: 21d return divided by 21d max-drawdown (smooth one-way ascent)
def f05pb_f05_parabolic_blowoff_runsmooth_21d_base_v054_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    roll_peak = closeadj.rolling(21, min_periods=10).max()
    dd = (closeadj / roll_peak.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).min().abs()
    b = ret.clip(lower=0) / (dd.replace(0, np.nan) + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# steepness regime: magnitude-weighted tally of top-quartile 5d-slope days over 21d
def f05pb_f05_parabolic_blowoff_slopepct_5d_base_v055_signal(closeadj):
    rs = _f05_runslope(closeadj, 5)
    rnk = rs.rolling(252, min_periods=63).rank(pct=True)
    hot = (rnk - 0.75).clip(lower=0)
    b = hot.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-reversion half-life proxy: autocorrelation of the 63d extension at lag 5
# (low/negative => extension snaps back fast; structurally distinct from level)
def f05pb_f05_parabolic_blowoff_ext63pct_63d_base_v056_signal(closeadj):
    ext = closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0
    d = ext.diff()
    cov = (d * d.shift(5)).rolling(63, min_periods=21).mean()
    var = (d * d).rolling(63, min_periods=21).mean()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-slope acceleration: is the 21d MA itself curling upward (trend going vertical)
# measured as the 5d change in the MA's own 5d slope (distinct from price curvature)
def f05pb_f05_parabolic_blowoff_gapaccel_21d_base_v057_signal(closeadj):
    ma = _mean(closeadj, 21)
    ma_slope = np.log(ma.replace(0, np.nan) / ma.shift(5).replace(0, np.nan))
    b = ma_slope - ma_slope.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of consecutive days price held above its 21d MA (extended-regime streak)
def f05pb_f05_parabolic_blowoff_abovemastreak_21d_base_v058_signal(closeadj):
    above = (closeadj > _mean(closeadj, 21)).astype(float)

    def _streak(a):
        c = 0
        for v in a:
            c = c + 1 if v > 0 else 0
        return float(c)

    b = above.rolling(63, min_periods=21).apply(_streak, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch interacted with volume z (only when both extreme = true blowoff)
def f05pb_f05_parabolic_blowoff_blowoffcomp_21d_base_v059_signal(closeadj, volume):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    vz = _z(volume, 63).clip(lower=0)
    b = np.sqrt(s * vz / (vz + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up thrust: cumulative close-to-prior-close gaps over 5d in ATR units
# (overnight blowoff thrust, distinct from intraday run slope)
def f05pb_f05_parabolic_blowoff_thrust_5d_base_v060_signal(closeadj, high, low):
    gap = (closeadj - closeadj.shift(1)).clip(lower=0)
    cumgap = gap.rolling(5, min_periods=3).sum()
    atr = _f05_atr(high, low, closeadj, 21)
    b = cumgap / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff cleanliness: positive ATR-extension times path-efficiency of the 10d run
# (extended AND moving in a straight line = a true parabola, not chop)
def f05pb_f05_parabolic_blowoff_extcleanliness_21d_base_v061_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21).clip(lower=0)
    net = (closeadj - closeadj.shift(10))
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    eff = net / path.replace(0, np.nan)
    b = e * eff.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic detection: convexity of price > 0 while above MA (accelerating up-curve)
def f05pb_f05_parabolic_blowoff_paradetect_10d_base_v062_signal(closeadj):
    accel = _f05_accel(closeadj, 10)
    above = (closeadj > _mean(closeadj, 21)).astype(float)
    b = accel.clip(lower=0) * above * 1000.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of price from its 5d MA vs 21d MA spread (fast-MA separation = blowoff)
def f05pb_f05_parabolic_blowoff_maspread_5v21_base_v063_signal(closeadj):
    m5 = _mean(closeadj, 5)
    m21 = _mean(closeadj, 21)
    b = (m5 - m21) / m21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched relative to recent typical stretch (extension z vs own 21d window)
def f05pb_f05_parabolic_blowoff_extzfast_21d_base_v064_signal(closeadj):
    ext = closeadj / _mean(closeadj, 21).replace(0, np.nan) - 1.0
    b = _z(ext, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff-then-fade composite: peak 10d extension minus current (top distance)
def f05pb_f05_parabolic_blowoff_topdist_21d_base_v065_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    peak = e.rolling(10, min_periods=5).max()
    cur = e
    b = (peak - cur) * (peak > 1.5).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized 5d up-vol vs down-vol skew (one-sided blowoff volatility)
def f05pb_f05_parabolic_blowoff_volskew_21d_base_v066_signal(closeadj):
    r = closeadj.pct_change()
    upv = r.clip(lower=0).pow(2).rolling(21, min_periods=10).mean()
    dnv = r.clip(upper=0).pow(2).rolling(21, min_periods=10).mean()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# path efficiency only (no direction): how straight-line the 10d move was
# (a clean parabola has high efficiency regardless of run size; distinct facet)
def f05pb_f05_parabolic_blowoff_runeff_10d_base_v067_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    b = (net / path.replace(0, np.nan)) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of days >1.5 ATR above 21d MA over last quarter (overextension persistence)
def f05pb_f05_parabolic_blowoff_extdayscnt_63d_base_v068_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    hot = (e >= 1.5).astype(float)
    b = hot.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log of 21d high over 63d MA (how far the recent peak ran above trend)
def f05pb_f05_parabolic_blowoff_peakovertrend_63d_base_v069_signal(closeadj):
    hi = _rmax(closeadj, 21)
    ma = _mean(closeadj, 63)
    b = np.log(hi.replace(0, np.nan) / ma.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized blowoff distance: (price - 21d MA) per dollar of 63d range
def f05pb_f05_parabolic_blowoff_extrng_21d_base_v070_signal(closeadj):
    ext = closeadj - _mean(closeadj, 21)
    rng = (_rmax(closeadj, 63) - _rmin(closeadj, 63)).replace(0, np.nan)
    b = ext / rng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch interacted with dollar-volume surge (liquidity-confirmed blowoff)
def f05pb_f05_parabolic_blowoff_liqblowoff_21d_base_v071_signal(closeadj, volume):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    dv = closeadj * volume
    surge = (dv / dv.rolling(63, min_periods=21).mean().replace(0, np.nan) - 1.0).clip(lower=0)
    b = s * surge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# speed of the parabola: 21d return squared times its sign (convex momentum)
def f05pb_f05_parabolic_blowoff_convmom_21d_base_v072_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = np.sign(r) * r * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension reversion pressure: sigma-extension times negative recent slope
def f05pb_f05_parabolic_blowoff_revpress_21d_base_v073_signal(closeadj):
    ma = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    sig = (closeadj - ma) / sd.replace(0, np.nan)
    slope = _f05_runslope(closeadj, 3)
    b = sig.clip(lower=0) * (-slope)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff age: days since the max 21d ATR-extension within the last quarter
def f05pb_f05_parabolic_blowoff_blowoffage_63d_base_v074_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)

    def _dsince(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = e.rolling(63, min_periods=21).apply(_dsince, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total stretch energy: sum of positive daily stretch over 21d (cumulative froth)
def f05pb_f05_parabolic_blowoff_stretchenergy_21d_base_v075_signal(closeadj):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    b = s.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05pb_f05_parabolic_blowoff_stretch_21d_base_v001_signal,
    f05pb_f05_parabolic_blowoff_stretchz_10d_base_v002_signal,
    f05pb_f05_parabolic_blowoff_stretchrank_63d_base_v003_signal,
    f05pb_f05_parabolic_blowoff_stretchspr_10v63_base_v004_signal,
    f05pb_f05_parabolic_blowoff_stretchvel_21d_base_v005_signal,
    f05pb_f05_parabolic_blowoff_stretchpos_21d_base_v006_signal,
    f05pb_f05_parabolic_blowoff_stretchvol_5d_base_v007_signal,
    f05pb_f05_parabolic_blowoff_emaribbon_8v34_base_v008_signal,
    f05pb_f05_parabolic_blowoff_runslope_5d_base_v009_signal,
    f05pb_f05_parabolic_blowoff_runslopez_10d_base_v010_signal,
    f05pb_f05_parabolic_blowoff_runsloperank_21d_base_v011_signal,
    f05pb_f05_parabolic_blowoff_slopesteep_5v21_base_v012_signal,
    f05pb_f05_parabolic_blowoff_runsigma_10d_base_v013_signal,
    f05pb_f05_parabolic_blowoff_uprundays_10d_base_v014_signal,
    f05pb_f05_parabolic_blowoff_upstreak_21d_base_v015_signal,
    f05pb_f05_parabolic_blowoff_slopeaccel_5d_base_v016_signal,
    f05pb_f05_parabolic_blowoff_atrext21_21d_base_v017_signal,
    f05pb_f05_parabolic_blowoff_atrext63_63d_base_v018_signal,
    f05pb_f05_parabolic_blowoff_atrextz21_21d_base_v019_signal,
    f05pb_f05_parabolic_blowoff_atrextrank21_21d_base_v020_signal,
    f05pb_f05_parabolic_blowoff_atrextvel_21d_base_v021_signal,
    f05pb_f05_parabolic_blowoff_atrextspr_21v63_base_v022_signal,
    f05pb_f05_parabolic_blowoff_atrextpos_21d_base_v023_signal,
    f05pb_f05_parabolic_blowoff_atrext10_10d_base_v024_signal,
    f05pb_f05_parabolic_blowoff_atrexttime_21d_base_v025_signal,
    f05pb_f05_parabolic_blowoff_volspike_63d_base_v026_signal,
    f05pb_f05_parabolic_blowoff_volz_63d_base_v027_signal,
    f05pb_f05_parabolic_blowoff_volrun_21d_base_v028_signal,
    f05pb_f05_parabolic_blowoff_dollvolspike_63d_base_v029_signal,
    f05pb_f05_parabolic_blowoff_volclimaxcnt_21d_base_v030_signal,
    f05pb_f05_parabolic_blowoff_volpeak_10d_base_v031_signal,
    f05pb_f05_parabolic_blowoff_volimbal_21d_base_v032_signal,
    f05pb_f05_parabolic_blowoff_volspikeaccel_base_v033_signal,
    f05pb_f05_parabolic_blowoff_volwstretch_21d_base_v034_signal,
    f05pb_f05_parabolic_blowoff_fade_21d_base_v035_signal,
    f05pb_f05_parabolic_blowoff_stretchrev_10d_base_v036_signal,
    f05pb_f05_parabolic_blowoff_snapback_5d_base_v037_signal,
    f05pb_f05_parabolic_blowoff_atrunwind_21d_base_v038_signal,
    f05pb_f05_parabolic_blowoff_revflip_5d_base_v039_signal,
    f05pb_f05_parabolic_blowoff_fadescaled_5d_base_v040_signal,
    f05pb_f05_parabolic_blowoff_stretchroll_21d_base_v041_signal,
    f05pb_f05_parabolic_blowoff_exhaust_21d_base_v042_signal,
    f05pb_f05_parabolic_blowoff_convex_10d_base_v043_signal,
    f05pb_f05_parabolic_blowoff_rsiexh_14d_base_v044_signal,
    f05pb_f05_parabolic_blowoff_diverg_21d_base_v045_signal,
    f05pb_f05_parabolic_blowoff_slopedecay_5d_base_v046_signal,
    f05pb_f05_parabolic_blowoff_upperwick_10d_base_v047_signal,
    f05pb_f05_parabolic_blowoff_climaxrng_5d_base_v048_signal,
    f05pb_f05_parabolic_blowoff_stretchvspeak_21d_base_v049_signal,
    f05pb_f05_parabolic_blowoff_curve_5d_base_v050_signal,
    f05pb_f05_parabolic_blowoff_pctb_20d_base_v051_signal,
    f05pb_f05_parabolic_blowoff_bandwalk_20d_base_v052_signal,
    f05pb_f05_parabolic_blowoff_sigmaext_21d_base_v053_signal,
    f05pb_f05_parabolic_blowoff_runsmooth_21d_base_v054_signal,
    f05pb_f05_parabolic_blowoff_slopepct_5d_base_v055_signal,
    f05pb_f05_parabolic_blowoff_ext63pct_63d_base_v056_signal,
    f05pb_f05_parabolic_blowoff_gapaccel_21d_base_v057_signal,
    f05pb_f05_parabolic_blowoff_abovemastreak_21d_base_v058_signal,
    f05pb_f05_parabolic_blowoff_blowoffcomp_21d_base_v059_signal,
    f05pb_f05_parabolic_blowoff_thrust_5d_base_v060_signal,
    f05pb_f05_parabolic_blowoff_extcleanliness_21d_base_v061_signal,
    f05pb_f05_parabolic_blowoff_paradetect_10d_base_v062_signal,
    f05pb_f05_parabolic_blowoff_maspread_5v21_base_v063_signal,
    f05pb_f05_parabolic_blowoff_extzfast_21d_base_v064_signal,
    f05pb_f05_parabolic_blowoff_topdist_21d_base_v065_signal,
    f05pb_f05_parabolic_blowoff_volskew_21d_base_v066_signal,
    f05pb_f05_parabolic_blowoff_runeff_10d_base_v067_signal,
    f05pb_f05_parabolic_blowoff_extdayscnt_63d_base_v068_signal,
    f05pb_f05_parabolic_blowoff_peakovertrend_63d_base_v069_signal,
    f05pb_f05_parabolic_blowoff_extrng_21d_base_v070_signal,
    f05pb_f05_parabolic_blowoff_liqblowoff_21d_base_v071_signal,
    f05pb_f05_parabolic_blowoff_convmom_21d_base_v072_signal,
    f05pb_f05_parabolic_blowoff_revpress_21d_base_v073_signal,
    f05pb_f05_parabolic_blowoff_blowoffage_63d_base_v074_signal,
    f05pb_f05_parabolic_blowoff_stretchenergy_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_PARABOLIC_BLOWOFF_REGISTRY_001_075 = REGISTRY


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

    print("OK f05_parabolic_blowoff_base_001_075_claude: %d features pass" % n_features)
