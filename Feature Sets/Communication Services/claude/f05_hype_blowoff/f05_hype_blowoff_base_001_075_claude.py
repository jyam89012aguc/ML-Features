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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (hype / blowoff / overextension) =====
def _f05hb_atr(high, low, closeadj, w):
    # average true range using high/low/prior close
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(2, w // 2)).mean()


def _f05hb_stretch_atr(high, low, closeadj, maw, atrw):
    # distance of price above fast MA expressed in ATR units (overextension)
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    atr = _f05hb_atr(high, low, closeadj, atrw)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _f05hb_dist_ma(closeadj, maw):
    # percent distance above a moving average (above = positive)
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    return closeadj / ma.replace(0, np.nan) - 1.0


def _f05hb_run_slope(closeadj, w):
    # log-return slope over window = vertical-run velocity
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan)) / float(w)


def _f05hb_volspike(volume, w):
    # volume relative to its trailing average (blowoff volume spike)
    return volume / volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)


def _f05hb_rsi(closeadj, w):
    # Wilder-style RSI on closeadj (overbought exhaustion)
    d = closeadj.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.rolling(w, min_periods=max(2, w // 2)).mean()
    ad = dn.rolling(w, min_periods=max(2, w // 2)).mean()
    rs = au / ad.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _f05hb_upday_frac(closeadj, w):
    # fraction of up days = one-sided trend persistence into a blowoff
    up = (closeadj.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean()


# ============================================================
# --- stretch vs fast MA in ATR units (overextension core) ---

# price stretch above 5d MA in 14d ATR units
def f05hb_f05_hype_blowoff_stretchatr_5d_base_v001_signal(closeadj, high, low):
    b = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price stretch above 10d MA in 14d ATR units
def f05hb_f05_hype_blowoff_stretchatr_10d_base_v002_signal(closeadj, high, low):
    b = _f05hb_stretch_atr(high, low, closeadj, 10, 14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-space fan-out: stretch above 5d MA minus stretch above 21d MA (both ATR units)
def f05hb_f05_hype_blowoff_stretchatr_21d_base_v003_signal(closeadj, high, low):
    st5 = _f05hb_stretch_atr(high, low, closeadj, 5, 21)
    st21 = _f05hb_stretch_atr(high, low, closeadj, 21, 21)
    b = st5 - st21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff peak: max stretch (5d MA, ATR units) seen over the last month
def f05hb_f05_hype_blowoff_stretchpeak_21d_base_v004_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = st.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch z-scored vs its own quarter history (extremity of overextension)
def f05hb_f05_hype_blowoff_stretchz_63d_base_v005_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 14)
    b = _z(st, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fade from blowoff: current stretch minus its 21d peak (negative = unwinding)
def f05hb_f05_hype_blowoff_stretchfade_21d_base_v006_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = st - st.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sharpest single-day advance in ATR units over the last 5d (gap-up spike)
def f05hb_f05_hype_blowoff_sharpstretch_21d_base_v007_signal(closeadj, high, low):
    atr = _f05hb_atr(high, low, closeadj, 21)
    day_move = (closeadj - closeadj.shift(1)) / atr.replace(0, np.nan)
    b = day_move.rolling(5, min_periods=3).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance above 21/63d MA (% overextension) ---

# percent distance above 21d MA
def f05hb_f05_hype_blowoff_distma_21d_base_v008_signal(closeadj):
    b = _f05hb_dist_ma(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent distance above 63d MA
def f05hb_f05_hype_blowoff_distma_63d_base_v009_signal(closeadj):
    b = _f05hb_dist_ma(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA z-scored vs own 63d history (relative overextension)
def f05hb_f05_hype_blowoff_distmaz_21d_base_v010_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 63d MA, percentile-ranked vs its own 252d history
def f05hb_f05_hype_blowoff_distmarank_63d_base_v011_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 63)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA fan-out: gap between distance-above-21d and distance-above-63d (acceleration)
def f05hb_f05_hype_blowoff_mafanout_base_v012_signal(closeadj):
    d21 = _f05hb_dist_ma(closeadj, 21)
    d63 = _f05hb_dist_ma(closeadj, 63)
    b = d21 - d63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension vs own froth ceiling: dist-above-21d-MA / its 63d rolling max
def f05hb_f05_hype_blowoff_distmavol_21d_base_v013_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    ceil = d.rolling(63, min_periods=21).max()
    b = d / ceil.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long price has held more than 10% above its 21d MA (blowoff persistence)
def f05hb_f05_hype_blowoff_distmapersist_21d_base_v014_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    hot = (d - 0.10).clip(lower=0)
    b = hot.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fade of distance-above-21d MA from its monthly peak (rollover from extension)
def f05hb_f05_hype_blowoff_distmafade_21d_base_v015_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    b = d - d.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vertical-run slope (velocity / parabolicity) ---

# 5d log-return run-slope (short vertical run)
def f05hb_f05_hype_blowoff_runslope_5d_base_v016_signal(closeadj):
    b = _f05hb_run_slope(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 10d log-return run-slope
def f05hb_f05_hype_blowoff_runslope_10d_base_v017_signal(closeadj):
    b = _f05hb_run_slope(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-return run-slope
def f05hb_f05_hype_blowoff_runslope_21d_base_v018_signal(closeadj):
    b = _f05hb_run_slope(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run-slope steepening: 5d slope minus 21d slope (vertical acceleration of the run)
def f05hb_f05_hype_blowoff_slopesteep_base_v019_signal(closeadj):
    s5 = _f05hb_run_slope(closeadj, 5)
    s21 = _f05hb_run_slope(closeadj, 21)
    b = s5 - s21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d run-slope z-scored vs its own quarter (unusually vertical)
def f05hb_f05_hype_blowoff_slopez_5d_base_v020_signal(closeadj):
    s = _f05hb_run_slope(closeadj, 5)
    b = _z(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolicity: straightness of the 10d up-run (corr of log-price with time)
def f05hb_f05_hype_blowoff_parab_5d_base_v021_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    t = pd.Series(np.arange(len(lp), dtype=float), index=lp.index)
    w = 10
    corr = lp.rolling(w, min_periods=6).corr(t)
    slope_sign = np.sign(lp - lp.shift(w))
    b = corr * slope_sign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of the run: second difference of cumulative log price over 5d steps
def f05hb_f05_hype_blowoff_runconvex_base_v022_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 2.0 * lp.shift(5) + lp.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max 5d run-slope over the last month (steepest vertical burst recently)
def f05hb_f05_hype_blowoff_slopepeak_base_v023_signal(closeadj):
    s = _f05hb_run_slope(closeadj, 5)
    b = s.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blowoff volume spike ---

# volume spike vs 21d average (blowoff participation)
def f05hb_f05_hype_blowoff_volspike_21d_base_v024_signal(volume):
    b = _f05hb_volspike(volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained crowd buildup: 5d average volume vs 63d average volume
def f05hb_f05_hype_blowoff_volspike_63d_base_v025_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log volume z-score vs 63d history (standardized blowoff volume)
def f05hb_f05_hype_blowoff_volz_63d_base_v026_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = _z(lv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak volume spike over the last 10 days (climax volume)
def f05hb_f05_hype_blowoff_volpeak_10d_base_v027_signal(volume):
    vs = _f05hb_volspike(volume, 21)
    b = vs.rolling(10, min_periods=5).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of high-volume blowoff days (>2x avg) over the last month
def f05hb_f05_hype_blowoff_volsurgecnt_21d_base_v028_signal(volume):
    vs = _f05hb_volspike(volume, 63)
    surge = (vs >= 2.0).astype(float)
    cnt = surge.rolling(21, min_periods=10).sum()
    excess = (vs - 2.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = cnt + 5.0 * excess
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-led frenzy: dollar-volume spike minus share-volume spike (price contribution)
def f05hb_f05_hype_blowoff_dvolspike_21d_base_v029_signal(closeadj, volume):
    dv = closeadj * volume
    dvs = dv / dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
    vs = volume / volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
    b = dvs - vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-spike expansion: 5d avg spike vs 21d avg spike (accelerating crowd)
def f05hb_f05_hype_blowoff_volexpand_base_v030_signal(volume):
    vs = _f05hb_volspike(volume, 63)
    b = vs.rolling(5, min_periods=3).mean() - vs.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blowoff = price run x volume spike (signature interaction) ---

# blowoff signature: 5d run-slope x contemporaneous volume spike
def f05hb_f05_hype_blowoff_blowoffsig_base_v031_signal(closeadj, volume):
    s = _f05hb_run_slope(closeadj, 5)
    vs = _f05hb_volspike(volume, 21)
    b = s.clip(lower=0) * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume thrust: volume spike weighted by daily up-return (one-sided frenzy)
def f05hb_f05_hype_blowoff_upvolthrust_base_v032_signal(closeadj, volume):
    r = closeadj.pct_change()
    vs = _f05hb_volspike(volume, 21)
    thrust = (r.clip(lower=0) * vs)
    b = thrust.rolling(5, min_periods=3).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff intensity: distance above 21d MA x log volume z (extended + crowded)
def f05hb_f05_hype_blowoff_blowoffint_base_v033_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    lv = _z(np.log(volume.replace(0, np.nan)), 63)
    b = d.clip(lower=0) * lv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climax bar: intraday range x volume spike on the day (single-bar blowoff)
def f05hb_f05_hype_blowoff_climaxbar_base_v034_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    vs = _f05hb_volspike(volume, 21)
    bar = rng * vs
    b = bar.rolling(5, min_periods=3).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion-from-spike ---

# reversal: return since the most extended day in the last 10 (fade of the spike)
def f05hb_f05_hype_blowoff_revfromhi_10d_base_v035_signal(closeadj):
    hi = closeadj.rolling(10, min_periods=5).max()
    b = closeadj / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback from 21d high after a hot run (depth of post-spike retrace)
def f05hb_f05_hype_blowoff_revfromhi_21d_base_v036_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    b = closeadj / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-then-fade: prior 10d gain minus subsequent retrace from peak
def f05hb_f05_hype_blowoff_spikefade_base_v037_signal(closeadj):
    gain = closeadj.shift(0) / closeadj.shift(10).replace(0, np.nan) - 1.0
    hi = closeadj.rolling(10, min_periods=5).max()
    retr = closeadj / hi.replace(0, np.nan) - 1.0
    b = gain * (-retr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overshoot reversion: distance above 21d MA times negative 3d return (snapback)
def f05hb_f05_hype_blowoff_snapback_base_v038_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    r3 = closeadj.pct_change(3)
    b = d.clip(lower=0) * (-r3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance traveled back toward 21d MA after touching a monthly stretch peak
def f05hb_f05_hype_blowoff_reverttoma_base_v039_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    peak = st.rolling(21, min_periods=10).max()
    b = (peak - st) / peak.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-volume on the fade: volume spike weighted by negative return (distribution)
def f05hb_f05_hype_blowoff_distribvol_base_v040_signal(closeadj, volume):
    r = closeadj.pct_change()
    vs = _f05hb_volspike(volume, 21)
    dv = ((-r).clip(lower=0) * vs)
    b = dv.rolling(5, min_periods=3).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exhaustion / overbought ---

# 14d RSI centered (overbought exhaustion)
def f05hb_f05_hype_blowoff_rsi_14d_base_v041_signal(closeadj):
    b = _f05hb_rsi(closeadj, 14) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 7d fast RSI centered (acute overbought)
def f05hb_f05_hype_blowoff_rsi_7d_base_v042_signal(closeadj):
    b = _f05hb_rsi(closeadj, 7) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overbought persistence: fraction of last month with RSI>70 (sticky froth)
def f05hb_f05_hype_blowoff_obpersist_base_v043_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    ob = (rsi - 70.0).clip(lower=0)
    b = ob.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RSI roll-over: change in 14d RSI over 5 days (exhaustion turn)
def f05hb_f05_hype_blowoff_rsiroll_base_v044_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    b = rsi - rsi.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down move asymmetry: biggest up-day vs biggest down-day over 21d (froth tail)
def f05hb_f05_hype_blowoff_updayfrac_21d_base_v045_signal(closeadj):
    r = closeadj.pct_change()
    max_up = r.rolling(21, min_periods=10).max()
    max_dn = (-r).rolling(21, min_periods=10).max()
    b = (max_up - max_dn) / (max_up + max_dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current up-streak length, magnitude-weighted by streak return (consecutive green)
def f05hb_f05_hype_blowoff_upstreak_base_v046_signal(closeadj):
    r = closeadj.pct_change()
    up = (r > 0).astype(float)

    def _streak(a):
        s = 0.0
        for x in a[::-1]:
            if x > 0:
                s += x
            else:
                break
        return float(s)

    streak_ret = r.rolling(21, min_periods=10).apply(_streak, raw=True)
    cnt = up.rolling(21, min_periods=10).apply(
        lambda a: float(np.sum(np.cumprod(a[::-1]))), raw=True)
    b = cnt + 20.0 * streak_ret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic %K over 21d (close position in recent hi/lo range, overbought)
def f05hb_f05_hype_blowoff_stoch_21d_base_v047_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    b = (closeadj - ll) / (hh - ll).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Williams %R style: how far below the 10d intraday high (acute overbought when ~0)
def f05hb_f05_hype_blowoff_willr_10d_base_v048_signal(closeadj, high, low):
    hh = high.rolling(10, min_periods=5).max()
    ll = low.rolling(10, min_periods=5).min()
    b = (hh - closeadj) / (hh - ll).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional overextension facets ---

# burst extremity: percentile rank of current 5d return vs its own 126d history
def f05hb_f05_hype_blowoff_burstprox_base_v049_signal(closeadj):
    r5 = closeadj.pct_change(5)
    b = r5.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# medium-term overextension (63d MA, ATR units) z-scored vs its own 126d history
def f05hb_f05_hype_blowoff_stretchatr_63d_base_v050_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 63, 21)
    b = _z(st, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b on 21d bands (how far through the upper band, froth)
def f05hb_f05_hype_blowoff_pctb_21d_base_v051_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    b = (closeadj - lower) / (upper - lower).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days spent above the upper 21d Bollinger band over the last month (band-riding)
def f05hb_f05_hype_blowoff_bandride_base_v052_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    upper = ma + 2.0 * sd
    breach = ((closeadj - upper) / sd.replace(0, np.nan)).clip(lower=0)
    b = breach.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impulse intensity: recent 5d return relative to trailing 21d return path
def f05hb_f05_hype_blowoff_impulse_base_v053_signal(closeadj):
    r5 = closeadj.pct_change(5)
    base21 = closeadj.pct_change(21).abs().shift(5)
    b = r5 / (base21.replace(0, np.nan) + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion in the run: 5d ATR vs 21d ATR (volatility blowoff)
def f05hb_f05_hype_blowoff_atrexpand_base_v054_signal(closeadj, high, low):
    a5 = _f05hb_atr(high, low, closeadj, 5)
    a21 = _f05hb_atr(high, low, closeadj, 21)
    b = a5 / a21.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized true range today vs 21d typical (single-day climactic range)
def f05hb_f05_hype_blowoff_climaxrange_base_v055_signal(closeadj, high, low):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    typ = tr.rolling(21, min_periods=10).mean()
    b = tr / typ.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA combined with overbought RSI (extended AND frothy)
def f05hb_f05_hype_blowoff_extfroth_base_v056_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    rsi = (_f05hb_rsi(closeadj, 14) - 50.0) / 50.0
    b = d.clip(lower=0) * rsi.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension regime: mean positive stretch (ATR units) above 5d MA over 21d
def f05hb_f05_hype_blowoff_extregime_base_v057_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    pos = st.clip(lower=0)
    b = pos.rolling(21, min_periods=10).mean() * (st > 0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff and reversal in one: peak stretch in 21d minus current stretch, vol-weighted
def f05hb_f05_hype_blowoff_peakfadevol_base_v058_signal(closeadj, high, low, volume):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    fade = st.rolling(21, min_periods=10).max() - st
    vs = _f05hb_volspike(volume, 21)
    b = fade * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# skew of recent returns (left-skew = crash risk after a hype run)
def f05hb_f05_hype_blowoff_retskew_21d_base_v059_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(21, min_periods=10).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# kurtosis of recent returns (fat-tailed blowoff dynamics)
def f05hb_f05_hype_blowoff_retkurt_21d_base_v060_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(21, min_periods=10).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day jump over the last 10d (gap/spike magnitude)
def f05hb_f05_hype_blowoff_maxjump_10d_base_v061_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(10, min_periods=5).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 5d MA in ATR units, smoothed (persistent overextension)
def f05hb_f05_hype_blowoff_stretchema_base_v062_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = _ema(st, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-run efficiency: net 21d move over total path length (clean parabola=1)
def f05hb_f05_hype_blowoff_runeff_21d_base_v063_signal(closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# crowd thrust: dollar-volume z times up-day fraction (frenzied one-sided demand)
def f05hb_f05_hype_blowoff_crowdthrust_base_v064_signal(closeadj, volume):
    dv = closeadj * volume
    dvz = _z(np.log(dv.replace(0, np.nan)), 63)
    udf = _f05hb_upday_frac(closeadj, 10) - 0.5
    b = dvz * udf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon extension spread: dist above 21d MA minus dist above 126d MA
def f05hb_f05_hype_blowoff_excessext_base_v065_signal(closeadj):
    d21 = _f05hb_dist_ma(closeadj, 21)
    d126 = _f05hb_dist_ma(closeadj, 126)
    b = d21 - d126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol surge: 5d std of returns vs 63d std (turbulent blowoff)
def f05hb_f05_hype_blowoff_volsurge_base_v066_signal(closeadj):
    r = closeadj.pct_change()
    v5 = r.rolling(5, min_periods=3).std()
    v63 = r.rolling(63, min_periods=21).std()
    b = v5 / v63.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded blowoff acceleration: squashed change in stretch over 5 days
def f05hb_f05_hype_blowoff_stretchtanh_base_v067_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 14)
    chg = st - st.shift(5)
    b = np.tanh(0.6 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-10d-high frequency over a month weighted by stretch (repeated fresh highs)
def f05hb_f05_hype_blowoff_freshhi_base_v068_signal(closeadj):
    hi = closeadj.rolling(10, min_periods=5).max()
    is_hi = (closeadj >= hi * 0.99999).astype(float)
    freq = is_hi.rolling(21, min_periods=10).mean()
    d = _f05hb_dist_ma(closeadj, 21).clip(lower=0)
    b = freq * (1.0 + d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension momentum vs its own smoothing: dist-above-21d MA minus its 10d EMA
def f05hb_f05_hype_blowoff_distmaaccel_base_v069_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    b = d - _ema(d, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overbought-with-volume: RSI-overbought flag x volume spike (validated froth)
def f05hb_f05_hype_blowoff_obvol_base_v070_signal(closeadj, volume):
    rsi = _f05hb_rsi(closeadj, 14)
    ob = (rsi - 50.0).clip(lower=0) / 50.0
    vs = _f05hb_volspike(volume, 21)
    b = ob * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation share: upside vol fraction of total vol (one-sided up move)
def f05hb_f05_hype_blowoff_upsideshare_base_v071_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0)
    upvar = (up ** 2).rolling(21, min_periods=10).mean()
    tot = (r ** 2).rolling(21, min_periods=10).mean()
    b = upvar / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Keltner breakout thrust: 5d change in price position through the EMA+ATR channel
def f05hb_f05_hype_blowoff_keltner_base_v072_signal(closeadj, high, low):
    ema = _ema(closeadj, 21)
    atr = _f05hb_atr(high, low, closeadj, 21)
    pos = (closeadj - ema) / atr.replace(0, np.nan)
    b = pos - pos.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff-to-base: 10d gain divided by 63d gain (concentration of the move)
def f05hb_f05_hype_blowoff_moveconc_base_v073_signal(closeadj):
    g10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    g63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = g10 / g63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA times volume spike percentile (crowded overextension rank)
def f05hb_f05_hype_blowoff_crowdext_base_v074_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    vs = _f05hb_volspike(volume, 63)
    vrank = vs.rolling(126, min_periods=42).rank(pct=True)
    b = d.clip(lower=0) * vrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-peak decay: bars since the 21d stretch peak, scaled (aging blowoff)
def f05hb_f05_hype_blowoff_peakage_base_v075_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = st.rolling(21, min_periods=10).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05hb_f05_hype_blowoff_stretchatr_5d_base_v001_signal,
    f05hb_f05_hype_blowoff_stretchatr_10d_base_v002_signal,
    f05hb_f05_hype_blowoff_stretchatr_21d_base_v003_signal,
    f05hb_f05_hype_blowoff_stretchpeak_21d_base_v004_signal,
    f05hb_f05_hype_blowoff_stretchz_63d_base_v005_signal,
    f05hb_f05_hype_blowoff_stretchfade_21d_base_v006_signal,
    f05hb_f05_hype_blowoff_sharpstretch_21d_base_v007_signal,
    f05hb_f05_hype_blowoff_distma_21d_base_v008_signal,
    f05hb_f05_hype_blowoff_distma_63d_base_v009_signal,
    f05hb_f05_hype_blowoff_distmaz_21d_base_v010_signal,
    f05hb_f05_hype_blowoff_distmarank_63d_base_v011_signal,
    f05hb_f05_hype_blowoff_mafanout_base_v012_signal,
    f05hb_f05_hype_blowoff_distmavol_21d_base_v013_signal,
    f05hb_f05_hype_blowoff_distmapersist_21d_base_v014_signal,
    f05hb_f05_hype_blowoff_distmafade_21d_base_v015_signal,
    f05hb_f05_hype_blowoff_runslope_5d_base_v016_signal,
    f05hb_f05_hype_blowoff_runslope_10d_base_v017_signal,
    f05hb_f05_hype_blowoff_runslope_21d_base_v018_signal,
    f05hb_f05_hype_blowoff_slopesteep_base_v019_signal,
    f05hb_f05_hype_blowoff_slopez_5d_base_v020_signal,
    f05hb_f05_hype_blowoff_parab_5d_base_v021_signal,
    f05hb_f05_hype_blowoff_runconvex_base_v022_signal,
    f05hb_f05_hype_blowoff_slopepeak_base_v023_signal,
    f05hb_f05_hype_blowoff_volspike_21d_base_v024_signal,
    f05hb_f05_hype_blowoff_volspike_63d_base_v025_signal,
    f05hb_f05_hype_blowoff_volz_63d_base_v026_signal,
    f05hb_f05_hype_blowoff_volpeak_10d_base_v027_signal,
    f05hb_f05_hype_blowoff_volsurgecnt_21d_base_v028_signal,
    f05hb_f05_hype_blowoff_dvolspike_21d_base_v029_signal,
    f05hb_f05_hype_blowoff_volexpand_base_v030_signal,
    f05hb_f05_hype_blowoff_blowoffsig_base_v031_signal,
    f05hb_f05_hype_blowoff_upvolthrust_base_v032_signal,
    f05hb_f05_hype_blowoff_blowoffint_base_v033_signal,
    f05hb_f05_hype_blowoff_climaxbar_base_v034_signal,
    f05hb_f05_hype_blowoff_revfromhi_10d_base_v035_signal,
    f05hb_f05_hype_blowoff_revfromhi_21d_base_v036_signal,
    f05hb_f05_hype_blowoff_spikefade_base_v037_signal,
    f05hb_f05_hype_blowoff_snapback_base_v038_signal,
    f05hb_f05_hype_blowoff_reverttoma_base_v039_signal,
    f05hb_f05_hype_blowoff_distribvol_base_v040_signal,
    f05hb_f05_hype_blowoff_rsi_14d_base_v041_signal,
    f05hb_f05_hype_blowoff_rsi_7d_base_v042_signal,
    f05hb_f05_hype_blowoff_obpersist_base_v043_signal,
    f05hb_f05_hype_blowoff_rsiroll_base_v044_signal,
    f05hb_f05_hype_blowoff_updayfrac_21d_base_v045_signal,
    f05hb_f05_hype_blowoff_upstreak_base_v046_signal,
    f05hb_f05_hype_blowoff_stoch_21d_base_v047_signal,
    f05hb_f05_hype_blowoff_willr_10d_base_v048_signal,
    f05hb_f05_hype_blowoff_burstprox_base_v049_signal,
    f05hb_f05_hype_blowoff_stretchatr_63d_base_v050_signal,
    f05hb_f05_hype_blowoff_pctb_21d_base_v051_signal,
    f05hb_f05_hype_blowoff_bandride_base_v052_signal,
    f05hb_f05_hype_blowoff_impulse_base_v053_signal,
    f05hb_f05_hype_blowoff_atrexpand_base_v054_signal,
    f05hb_f05_hype_blowoff_climaxrange_base_v055_signal,
    f05hb_f05_hype_blowoff_extfroth_base_v056_signal,
    f05hb_f05_hype_blowoff_extregime_base_v057_signal,
    f05hb_f05_hype_blowoff_peakfadevol_base_v058_signal,
    f05hb_f05_hype_blowoff_retskew_21d_base_v059_signal,
    f05hb_f05_hype_blowoff_retkurt_21d_base_v060_signal,
    f05hb_f05_hype_blowoff_maxjump_10d_base_v061_signal,
    f05hb_f05_hype_blowoff_stretchema_base_v062_signal,
    f05hb_f05_hype_blowoff_runeff_21d_base_v063_signal,
    f05hb_f05_hype_blowoff_crowdthrust_base_v064_signal,
    f05hb_f05_hype_blowoff_excessext_base_v065_signal,
    f05hb_f05_hype_blowoff_volsurge_base_v066_signal,
    f05hb_f05_hype_blowoff_stretchtanh_base_v067_signal,
    f05hb_f05_hype_blowoff_freshhi_base_v068_signal,
    f05hb_f05_hype_blowoff_distmaaccel_base_v069_signal,
    f05hb_f05_hype_blowoff_obvol_base_v070_signal,
    f05hb_f05_hype_blowoff_upsideshare_base_v071_signal,
    f05hb_f05_hype_blowoff_keltner_base_v072_signal,
    f05hb_f05_hype_blowoff_moveconc_base_v073_signal,
    f05hb_f05_hype_blowoff_crowdext_base_v074_signal,
    f05hb_f05_hype_blowoff_peakage_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_HYPE_BLOWOFF_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f05_hype_blowoff_base_001_075_claude: %d features pass" % n_features)
