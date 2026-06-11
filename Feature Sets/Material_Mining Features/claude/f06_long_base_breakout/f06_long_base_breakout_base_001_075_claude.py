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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (long-base / breakout) =====
def _f06_base_range(close, w):
    # normalized base range: (high-low)/midpoint over window -> tight base => small
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _f06_tightness(close, w):
    # coefficient of variation of price = base tightness (low => tight base)
    return _std(close, w) / _mean(close, w).replace(0, np.nan)


def _f06_ceiling_dist(close, w):
    # distance from base ceiling (prior rolling max excluding today)
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return close / ceil.replace(0, np.nan) - 1.0


def _f06_floor_dist(close, w):
    floor = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return close / floor.replace(0, np.nan) - 1.0


def _f06_in_base(close, w, thresh):
    # boolean-ish: is the normalized base range tight relative to its own history.
    # `thresh` is interpreted as a percentile (0..1) of the base range's history so
    # the flag varies across regimes regardless of absolute volatility scale.
    br = _f06_base_range(close, w)
    ref = br.rolling(max(w, 252), min_periods=max(1, w // 2)).quantile(thresh)
    return (br <= ref).astype(float)


def _f06_breakout(close, w):
    # breakout magnitude above prior base ceiling, floored at 0
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return (close / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)


def _f06_days_in_base(close, w, thresh):
    # consecutive days the normalized range has stayed tight vs history (base age)
    tight = _f06_in_base(close, w, thresh)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    return tight.rolling(w, min_periods=max(1, w // 4)).apply(_streak, raw=True)


# ============================================================
# multi-year base detection: 252d normalized range (tight => low value)
def f06lb_f06_long_base_breakout_baserange_252d_base_v001_signal(closeadj):
    b = _f06_base_range(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d normalized base range (two-year base width)
def f06lb_f06_long_base_breakout_baserange_504d_base_v002_signal(closeadj):
    b = _f06_base_range(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d normalized base range (multi-year base width)
def f06lb_f06_long_base_breakout_baserange_1260d_base_v003_signal(closeadj):
    b = _f06_base_range(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base tightness (coeff of variation) over 252d
def f06lb_f06_long_base_breakout_tight_252d_base_v004_signal(closeadj):
    b = _f06_tightness(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base tightness over 504d
def f06lb_f06_long_base_breakout_tight_504d_base_v005_signal(closeadj):
    b = _f06_tightness(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base tightness over 1260d, z-scored vs its own 252d history (tightening regime)
def f06lb_f06_long_base_breakout_tightz_1260d_base_v006_signal(closeadj):
    t = _f06_tightness(closeadj, 1260)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d base ceiling (prior high) — near 0 => pressing the ceiling
def f06lb_f06_long_base_breakout_ceildist_252d_base_v007_signal(closeadj):
    b = _f06_ceiling_dist(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# approach speed to the 504d base ceiling: change in ceiling distance over a quarter
# (price closing in on the two-year lid => positive; backing away => negative)
def f06lb_f06_long_base_breakout_ceildist_504d_base_v008_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 504)
    b = cd - cd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from the 1260d base ceiling, z-scored vs its own 252d history
# (de-trended multi-year ceiling pressure; differs in shape from raw distances)
def f06lb_f06_long_base_breakout_ceildist_1260d_base_v009_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 1260)
    b = _z(cd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 252d base floor (cushion off support)
def f06lb_f06_long_base_breakout_floordist_252d_base_v010_signal(closeadj):
    b = _f06_floor_dist(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 504d base floor
def f06lb_f06_long_base_breakout_floordist_504d_base_v011_signal(closeadj):
    b = _f06_floor_dist(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude above 252d ceiling (clipped at 0)
def f06lb_f06_long_base_breakout_brkout_252d_base_v012_signal(closeadj):
    b = _f06_breakout(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude above 504d ceiling
def f06lb_f06_long_base_breakout_brkout_504d_base_v013_signal(closeadj):
    b = _f06_breakout(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated multi-year breakout thrust: 63d sum of daily breakout magnitudes above
# the 1260d ceiling (how much net upside has been carved out above the long lid)
def f06lb_f06_long_base_breakout_brkout_1260d_base_v014_signal(closeadj):
    bo = _f06_breakout(closeadj, 1260)
    b = bo.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is-in-tight-base flag (252d range <= 35%) fraction over last quarter
def f06lb_f06_long_base_breakout_inbasefr_252d_base_v015_signal(closeadj):
    flag = _f06_in_base(closeadj, 252, 0.35)
    b = flag.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is-in-tight-base flag (504d range <= 50%) fraction over last half-year
def f06lb_f06_long_base_breakout_inbasefr_504d_base_v016_signal(closeadj):
    flag = _f06_in_base(closeadj, 504, 0.50)
    b = flag.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-in-base streak (252d, range<=0.35) normalized by window (base age)
def f06lb_f06_long_base_breakout_daysinbase_252d_base_v017_signal(closeadj):
    b = _f06_days_in_base(closeadj, 252, 0.35) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-in-base streak (504d, range<=0.5) normalized by window
def f06lb_f06_long_base_breakout_daysinbase_504d_base_v018_signal(closeadj):
    b = _f06_days_in_base(closeadj, 504, 0.50) / 504.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-position: where in the 252d base price sits, percentile-ranked vs its own
# 504d history (relative base position; decorrelated from raw ceiling distance)
def f06lb_f06_long_base_breakout_basepos_252d_base_v019_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _rank(pos, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-position 504d, de-trended by subtracting its own slow EMA (displacement
# of price within the two-year base relative to its recent typical position)
def f06lb_f06_long_base_breakout_basepos_504d_base_v020_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year position within the long base, percentile-ranked vs its own 504d
# history (where in the 1260d base price sits relative to how it usually sits)
def f06lb_f06_long_base_breakout_basepos_1260d_base_v021_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _rank(pos, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume confirmation: breakout magnitude x volume surge (63d ref)
def f06lb_f06_long_base_breakout_brkvol_252d_base_v022_signal(closeadj, volume):
    bo = _f06_breakout(closeadj, 252)
    vsurge = volume / _mean(volume, 63).replace(0, np.nan)
    b = bo * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume confirmation 504d
def f06lb_f06_long_base_breakout_brkvol_504d_base_v023_signal(closeadj, volume):
    bo = _f06_breakout(closeadj, 504)
    vsurge = volume / _mean(volume, 126).replace(0, np.nan)
    b = bo * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout confirmed by accumulation trend: breakout magnitude gated by the 21d
# slope of on-balance-volume (smart-money flow building into the breakout)
def f06lb_f06_long_base_breakout_brkdvol_252d_base_v024_signal(closeadj, volume):
    bo = _f06_breakout(closeadj, 252)
    direction = np.sign(closeadj.diff())
    signed_vol = (direction * volume)
    # 21d net signed volume normalized by avg volume = accumulation-trend proxy
    net = signed_vol.rolling(21, min_periods=10).sum()
    obv_slope = net / _mean(volume, 21).replace(0, np.nan) / 21.0
    b = bo * obv_slope
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# false-breakout proxy: poked above the 252d ceiling intrabar but closed back below.
# weighted by how far the high overshot the lid -> continuous failed-breakout pressure.
def f06lb_f06_long_base_breakout_falsebrk_252d_base_v025_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    b = failed.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# false-breakout proxy 504d: intrabar poke above the two-year lid that failed to hold
def f06lb_f06_long_base_breakout_falsebrk_504d_base_v026_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    b = failed.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base tightness percentile vs its own long history (rank: how tight vs usual)
def f06lb_f06_long_base_breakout_tightrank_252d_base_v027_signal(closeadj):
    t = _f06_tightness(closeadj, 252)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-range contraction: 252d range relative to 504d range (tightening into apex)
def f06lb_f06_long_base_breakout_contract_252v504_base_v028_signal(closeadj):
    s = _f06_base_range(closeadj, 252)
    l = _f06_base_range(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-range contraction 126 vs 504 (fast tightening)
def f06lb_f06_long_base_breakout_contract_126v504_base_v029_signal(closeadj):
    s = _f06_base_range(closeadj, 126)
    l = _f06_base_range(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ceiling proximity momentum: change in 252d ceiling distance over a month
def f06lb_f06_long_base_breakout_ceilmom_252d_base_v030_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 252)
    b = cd - cd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension in ATR units (how far above ceiling vs daily range)
def f06lb_f06_long_base_breakout_brkatr_252d_base_v031_signal(closeadj, high, low):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    atr = (high - low).rolling(21, min_periods=5).mean()
    b = (closeadj - ceil) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-floor support test in ATR units (how far above floor vs daily range)
def f06lb_f06_long_base_breakout_flooratr_252d_base_v032_signal(closeadj, high, low):
    floor = closeadj.shift(1).rolling(252, min_periods=126).min()
    atr = (high - low).rolling(21, min_periods=5).mean()
    b = (closeadj - floor) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base volume dry-up: current volume vs base-period avg (low => accumulation base)
def f06lb_f06_long_base_breakout_voldry_252d_base_v033_signal(volume):
    b = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base volume dry-up 504d
def f06lb_f06_long_base_breakout_voldry_504d_base_v034_signal(volume):
    b = _mean(volume, 42) / _mean(volume, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightness slope: is the base getting tighter? change in CoV over a quarter
def f06lb_f06_long_base_breakout_tightchg_252d_base_v035_signal(closeadj):
    t = _f06_tightness(closeadj, 252)
    b = t.shift(63) - t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base ceiling staleness: days since the 504d high was set (long flat lid)
def f06lb_f06_long_base_breakout_ceilstale_504d_base_v036_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = closeadj.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base floor staleness: days since the 504d low was set
def f06lb_f06_long_base_breakout_floorstale_504d_base_v037_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = closeadj.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pivot drift: log-slope of the 252d base midpoint over a quarter — is the whole
# base structure migrating up (constructive) or down (decay)?
def f06lb_f06_long_base_breakout_pivotprox_252d_base_v038_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    b = np.log(mid.replace(0, np.nan) / mid.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-range z-score: how unusual the current 252d base width is
def f06lb_f06_long_base_breakout_brangez_252d_base_v039_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    b = _z(br, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-base-high frequency: count of fresh 252d highs over last quarter (emergence)
def f06lb_f06_long_base_breakout_newhifreq_252d_base_v040_signal(closeadj):
    hi = _rmax(closeadj, 252)
    is_high = (closeadj >= hi * 0.99999).astype(float)
    b = is_high.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout hold quality: avg proximity to the 252d lid over last month (pressing it)
def f06lb_f06_long_base_breakout_brkhold_252d_base_v041_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = closeadj / ceil.replace(0, np.nan)
    b = prox.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation: volume-weighted base position (smart money lifting in base)
def f06lb_f06_long_base_breakout_volwtpos_252d_base_v042_signal(closeadj, volume):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    vw = (pos * volume).rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = vw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year apex squeeze: current 252d base range vs the tightest 252d range seen
# over the trailing 1260d (~1 => price is at its most-coiled in years)
def f06lb_f06_long_base_breakout_squeeze_252v1260_base_v043_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    brmin = br.rolling(1260, min_periods=504).min()
    b = br / brmin.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout thrust: 5d return weighted by proximity to the 252d ceiling (lid-pressing thrust)
def f06lb_f06_long_base_breakout_thrust_252d_base_v044_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.05)
    r5 = closeadj / closeadj.shift(5) - 1.0
    b = prox * r5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base maturity: fraction of last 2y spent within +/-15% of the 504d midpoint
def f06lb_f06_long_base_breakout_maturity_504d_base_v045_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    inband = (((closeadj - mid).abs() / mid.replace(0, np.nan)) <= 0.15).astype(float)
    b = inband.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead supply: fraction of the prior 504d that traded ABOVE today's price
# (trapped longs overhead). High => heavy resistance still to absorb in the base.
def f06lb_f06_long_base_breakout_overhead_504d_base_v046_signal(closeadj):
    def _f(a):
        cur = a[-1]
        return float(np.mean(a[:-1] > cur)) if len(a) > 1 else np.nan
    b = closeadj.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume confirmation z: volume z-score weighted by proximity to the lid
def f06lb_f06_long_base_breakout_brkvolz_252d_base_v047_signal(closeadj, volume):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(lower=0.0, upper=1.05)
    vz = _z(volume, 63)
    b = prox * vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-base + near-ceiling combo (coiled spring): low range AND pressing lid
def f06lb_f06_long_base_breakout_coil_252d_base_v048_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    cd = _f06_ceiling_dist(closeadj, 252)
    b = (1.0 / br.replace(0, np.nan)) * (1.0 + cd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger squeeze ratio at base scale: current 252d bandwidth vs its 252d minimum.
# ~1 => bandwidth at its tightest of the year (squeeze); larger => expanded.
def f06lb_f06_long_base_breakout_bandwidth_252d_base_v049_signal(closeadj):
    m = _mean(closeadj, 252)
    sd = _std(closeadj, 252)
    bw = (4.0 * sd) / m.replace(0, np.nan)
    bwmin = bw.rolling(252, min_periods=126).min()
    b = bw / bwmin.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth contraction streak: consecutive days bandwidth below its 252d median
def f06lb_f06_long_base_breakout_bwstreak_252d_base_v050_signal(closeadj):
    m = _mean(closeadj, 252)
    sd = _std(closeadj, 252)
    bw = (4.0 * sd) / m.replace(0, np.nan)
    med = bw.rolling(252, min_periods=126).median()
    below = (bw < med).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    b = below.rolling(126, min_periods=42).apply(_streak, raw=True) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base drift: slope of price within the base (flat base => near 0)
def f06lb_f06_long_base_breakout_basedrift_252d_base_v051_signal(closeadj):
    b = np.log(_mean(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base flatness: 1 minus |drift|, scaled — high when the base is horizontal
def f06lb_f06_long_base_breakout_flatness_504d_base_v052_signal(closeadj):
    drift = np.log(_mean(closeadj, 42).replace(0, np.nan) / _mean(closeadj, 504).replace(0, np.nan))
    b = 1.0 / (1.0 + 10.0 * drift.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout follow-through: forward 21d return weighted by current lid proximity
def f06lb_f06_long_base_breakout_followthru_252d_base_v053_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.05)
    ft = closeadj.shift(-21) / closeadj - 1.0
    b = (prox * ft).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tests of the lid over last year: fraction of days within 5% of the 252d ceiling
def f06lb_f06_long_base_breakout_attempts_252d_base_v054_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    cnt = near.rolling(252, min_periods=126).sum()
    prox = closeadj / ceil.replace(0, np.nan)
    b = cnt + prox
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base symmetry: is price closer to floor or ceiling (skew within base)
def f06lb_f06_long_base_breakout_symmetry_504d_base_v055_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    b = (closeadj - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year low-anchored lift, momentum form: change over a quarter in how far
# price sits above the 1260d base floor (acceleration off the deep base low)
def f06lb_f06_long_base_breakout_baselift_1260d_base_v056_signal(closeadj):
    lo = _rmin(closeadj, 1260)
    lift = np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))
    b = lift - lift.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightness ratio short vs long (21d vol / 252d vol) — micro-coil inside base
def f06lb_f06_long_base_breakout_microcoil_base_v057_signal(closeadj):
    short = _std(closeadj.pct_change(), 21)
    long = _std(closeadj.pct_change(), 252)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base ceiling rising slope: is the lid drifting up (ascending base)?
def f06lb_f06_long_base_breakout_ceilslope_252d_base_v058_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    b = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base floor rising slope: is support being lifted (higher lows in base)?
def f06lb_f06_long_base_breakout_floorslope_252d_base_v059_signal(closeadj):
    floor = _rmin(closeadj, 252)
    b = np.log(floor.replace(0, np.nan) / floor.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# converging base: floor rising faster than ceiling (triangle apex) 252d
def f06lb_f06_long_base_breakout_converge_252d_base_v060_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    floor = _rmin(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    fs = np.log(floor.replace(0, np.nan) / floor.shift(63).replace(0, np.nan))
    b = fs - cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout cleanliness: breakout magnitude divided by base width (decisiveness)
def f06lb_f06_long_base_breakout_clean_252d_base_v061_signal(closeadj):
    bo = _f06_breakout(closeadj, 252)
    br = _f06_base_range(closeadj, 252)
    b = bo / br.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# in-base low-volatility persistence: fraction of year daily-range stays small
def f06lb_f06_long_base_breakout_lowvolfr_252d_base_v062_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    quiet = (rng <= rng.rolling(252, min_periods=126).median()).astype(float)
    b = quiet.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout gap from intraday high vs base ceiling (true-high breakout strength)
def f06lb_f06_long_base_breakout_truebrk_252d_base_v063_signal(high, closeadj):
    ceil = high.shift(1).rolling(252, min_periods=126).max()
    b = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shakeout pressure: how often/deep price probed the lower fifth of the 252d base
# then closed back up over 5d (spring off support), averaged over a quarter.
def f06lb_f06_long_base_breakout_shakeout_252d_base_v064_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    near_floor = (0.2 - pos).clip(lower=0.0)
    snap = (closeadj / closeadj.shift(5) - 1.0).clip(lower=0.0)
    b = (near_floor.shift(5) * snap).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ceiling-approach acceleration: short-horizon z-score of the 252d ceiling distance
# (is price pressing the lid unusually hard vs the last quarter of behaviour?)
def f06lb_f06_long_base_breakout_ceildistrank_252d_base_v065_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 252)
    b = _z(cd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base age via low-range duration: fraction of 1260d window range stayed < 60%
def f06lb_f06_long_base_breakout_baseage_1260d_base_v066_signal(closeadj):
    flag = _f06_in_base(closeadj, 252, 0.60)
    b = flag.rolling(1260, min_periods=504).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume expansion on up-days near ceiling vs down-days (demand confirmation)
def f06lb_f06_long_base_breakout_demandvol_252d_base_v067_signal(closeadj, volume):
    up = (closeadj > closeadj.shift(1)).astype(float)
    upvol = (up * volume).rolling(63, min_periods=21).sum()
    dnvol = ((1 - up) * volume).rolling(63, min_periods=21).sum()
    b = upvol / dnvol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pre-breakout compression score: low bandwidth AND high base position
def f06lb_f06_long_base_breakout_prebrk_252d_base_v068_signal(closeadj):
    m = _mean(closeadj, 252)
    sd = _std(closeadj, 252)
    bw = (4.0 * sd) / m.replace(0, np.nan)
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = pos / bw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout sustainability: close-position within last 21d range scaled by lid proximity
def f06lb_f06_long_base_breakout_sustain_252d_base_v069_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.05)
    hi21 = _rmax(closeadj, 21)
    lo21 = _rmin(closeadj, 21)
    posn = (closeadj - lo21) / (hi21 - lo21).replace(0, np.nan)
    b = prox * posn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year emergence pulse: change over a quarter in days-since-1260d-high
# (sharply drops to ~0 right when a long base breaks to new multi-year highs)
def f06lb_f06_long_base_breakout_drought_1260d_base_v070_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    dsh = closeadj.rolling(1260, min_periods=504).apply(_f, raw=True)
    b = dsh - dsh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightness vs breakout interaction: tight base then thrust (spring score) signmag
def f06lb_f06_long_base_breakout_spring_252d_base_v071_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    bo = _f06_breakout(closeadj, 252)
    b = np.sign(bo) * np.sqrt(bo.abs()) / np.sqrt(br.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-range slope over 1260d: is the multi-year base widening or narrowing?
def f06lb_f06_long_base_breakout_brangeslope_1260d_base_v072_signal(closeadj):
    br = _f06_base_range(closeadj, 504)
    b = br - br.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net breakout quality: avg breakout magnitude minus avg failed-overshoot pressure
def f06lb_f06_long_base_breakout_netbrk_252d_base_v073_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    good = (closeadj / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    bad = overshoot * (closeadj <= ceil).astype(float)
    b = good.rolling(63, min_periods=21).mean() - 2.0 * bad.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base ceiling test count weighted by tightness (tested lid in a tight base)
def f06lb_f06_long_base_breakout_testedlid_504d_base_v074_signal(closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.97).astype(float)
    cnt = near.rolling(252, min_periods=126).sum()
    tight = 1.0 / _f06_base_range(closeadj, 504).replace(0, np.nan)
    b = cnt * tight
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# measured-move target progress: how far price has travelled above the 504d base
# floor as a fraction of the full base height (0 at floor, 1 at ceiling, >1 breakout)
def f06lb_f06_long_base_breakout_moveheight_504d_base_v075_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    span = (hi - lo).replace(0, np.nan)
    progress = (closeadj - lo) / span
    b = progress - progress.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06lb_f06_long_base_breakout_baserange_252d_base_v001_signal,
    f06lb_f06_long_base_breakout_baserange_504d_base_v002_signal,
    f06lb_f06_long_base_breakout_baserange_1260d_base_v003_signal,
    f06lb_f06_long_base_breakout_tight_252d_base_v004_signal,
    f06lb_f06_long_base_breakout_tight_504d_base_v005_signal,
    f06lb_f06_long_base_breakout_tightz_1260d_base_v006_signal,
    f06lb_f06_long_base_breakout_ceildist_252d_base_v007_signal,
    f06lb_f06_long_base_breakout_ceildist_504d_base_v008_signal,
    f06lb_f06_long_base_breakout_ceildist_1260d_base_v009_signal,
    f06lb_f06_long_base_breakout_floordist_252d_base_v010_signal,
    f06lb_f06_long_base_breakout_floordist_504d_base_v011_signal,
    f06lb_f06_long_base_breakout_brkout_252d_base_v012_signal,
    f06lb_f06_long_base_breakout_brkout_504d_base_v013_signal,
    f06lb_f06_long_base_breakout_brkout_1260d_base_v014_signal,
    f06lb_f06_long_base_breakout_inbasefr_252d_base_v015_signal,
    f06lb_f06_long_base_breakout_inbasefr_504d_base_v016_signal,
    f06lb_f06_long_base_breakout_daysinbase_252d_base_v017_signal,
    f06lb_f06_long_base_breakout_daysinbase_504d_base_v018_signal,
    f06lb_f06_long_base_breakout_basepos_252d_base_v019_signal,
    f06lb_f06_long_base_breakout_basepos_504d_base_v020_signal,
    f06lb_f06_long_base_breakout_basepos_1260d_base_v021_signal,
    f06lb_f06_long_base_breakout_brkvol_252d_base_v022_signal,
    f06lb_f06_long_base_breakout_brkvol_504d_base_v023_signal,
    f06lb_f06_long_base_breakout_brkdvol_252d_base_v024_signal,
    f06lb_f06_long_base_breakout_falsebrk_252d_base_v025_signal,
    f06lb_f06_long_base_breakout_falsebrk_504d_base_v026_signal,
    f06lb_f06_long_base_breakout_tightrank_252d_base_v027_signal,
    f06lb_f06_long_base_breakout_contract_252v504_base_v028_signal,
    f06lb_f06_long_base_breakout_contract_126v504_base_v029_signal,
    f06lb_f06_long_base_breakout_ceilmom_252d_base_v030_signal,
    f06lb_f06_long_base_breakout_brkatr_252d_base_v031_signal,
    f06lb_f06_long_base_breakout_flooratr_252d_base_v032_signal,
    f06lb_f06_long_base_breakout_voldry_252d_base_v033_signal,
    f06lb_f06_long_base_breakout_voldry_504d_base_v034_signal,
    f06lb_f06_long_base_breakout_tightchg_252d_base_v035_signal,
    f06lb_f06_long_base_breakout_ceilstale_504d_base_v036_signal,
    f06lb_f06_long_base_breakout_floorstale_504d_base_v037_signal,
    f06lb_f06_long_base_breakout_pivotprox_252d_base_v038_signal,
    f06lb_f06_long_base_breakout_brangez_252d_base_v039_signal,
    f06lb_f06_long_base_breakout_newhifreq_252d_base_v040_signal,
    f06lb_f06_long_base_breakout_brkhold_252d_base_v041_signal,
    f06lb_f06_long_base_breakout_volwtpos_252d_base_v042_signal,
    f06lb_f06_long_base_breakout_squeeze_252v1260_base_v043_signal,
    f06lb_f06_long_base_breakout_thrust_252d_base_v044_signal,
    f06lb_f06_long_base_breakout_maturity_504d_base_v045_signal,
    f06lb_f06_long_base_breakout_overhead_504d_base_v046_signal,
    f06lb_f06_long_base_breakout_brkvolz_252d_base_v047_signal,
    f06lb_f06_long_base_breakout_coil_252d_base_v048_signal,
    f06lb_f06_long_base_breakout_bandwidth_252d_base_v049_signal,
    f06lb_f06_long_base_breakout_bwstreak_252d_base_v050_signal,
    f06lb_f06_long_base_breakout_basedrift_252d_base_v051_signal,
    f06lb_f06_long_base_breakout_flatness_504d_base_v052_signal,
    f06lb_f06_long_base_breakout_followthru_252d_base_v053_signal,
    f06lb_f06_long_base_breakout_attempts_252d_base_v054_signal,
    f06lb_f06_long_base_breakout_symmetry_504d_base_v055_signal,
    f06lb_f06_long_base_breakout_baselift_1260d_base_v056_signal,
    f06lb_f06_long_base_breakout_microcoil_base_v057_signal,
    f06lb_f06_long_base_breakout_ceilslope_252d_base_v058_signal,
    f06lb_f06_long_base_breakout_floorslope_252d_base_v059_signal,
    f06lb_f06_long_base_breakout_converge_252d_base_v060_signal,
    f06lb_f06_long_base_breakout_clean_252d_base_v061_signal,
    f06lb_f06_long_base_breakout_lowvolfr_252d_base_v062_signal,
    f06lb_f06_long_base_breakout_truebrk_252d_base_v063_signal,
    f06lb_f06_long_base_breakout_shakeout_252d_base_v064_signal,
    f06lb_f06_long_base_breakout_ceildistrank_252d_base_v065_signal,
    f06lb_f06_long_base_breakout_baseage_1260d_base_v066_signal,
    f06lb_f06_long_base_breakout_demandvol_252d_base_v067_signal,
    f06lb_f06_long_base_breakout_prebrk_252d_base_v068_signal,
    f06lb_f06_long_base_breakout_sustain_252d_base_v069_signal,
    f06lb_f06_long_base_breakout_drought_1260d_base_v070_signal,
    f06lb_f06_long_base_breakout_spring_252d_base_v071_signal,
    f06lb_f06_long_base_breakout_brangeslope_1260d_base_v072_signal,
    f06lb_f06_long_base_breakout_netbrk_252d_base_v073_signal,
    f06lb_f06_long_base_breakout_testedlid_504d_base_v074_signal,
    f06lb_f06_long_base_breakout_moveheight_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_LONG_BASE_BREAKOUT_REGISTRY_001_075 = REGISTRY


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

    print("OK f06_long_base_breakout_base_001_075_claude: %d features pass" % n_features)
