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


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (margin cyclicality) =====
# NOTE on REAL-DATA distinctness: on real mining data the gross/operating/gp-margin
# triplet is ~0.99 collinear, and net/ebitda-margin is ~0.99 collinear. Therefore
# each facet (level/vol/amplitude/range-pos/...) is computed on ONLY ONE member of a
# collinear cluster; cross-cluster SPREADS and structurally different facets supply
# the distinct signal. We never repeat the same facet+window across collinear margins.
def _f25_amplitude(s, w):
    # peak-to-trough margin swing over the window (cycle amplitude)
    return _rmax(s, w) - _rmin(s, w)


def _f25_range_pos(s, w):
    # where current margin sits in its own cyclical range [0,1]
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f25_trough_dist(s, w):
    # distance above the cyclical trough (recovery off margin low)
    return s - _rmin(s, w)


def _f25_peak_dist(s, w):
    # distance below the cyclical peak (compression off margin high)
    return _rmax(s, w) - s


def _f25_gp_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f25_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f25_days_since_min(s, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return s.rolling(w, min_periods=max(1, w // 3)).apply(_f, raw=True)


def _f25_days_since_max(s, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return s.rolling(w, min_periods=max(1, w // 3)).apply(_f, raw=True)


# ============================================================
# ==== BLOCK 1: MARGIN LEVEL (one facet per collinear cluster) ====

# gross-margin level, smoothed over a quarter (persistent gross-margin level)
def f25mc_f25_margin_cyclicality_gmlevel_63d_base_v001_signal(grossmargin):
    b = grossmargin.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level, smoothed over a half-year (persistent bottom-line level)
def f25mc_f25_margin_cyclicality_nmlevel_126d_base_v002_signal(netmargin):
    b = netmargin.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level z-scored vs its own 252d cyclical history (de-trended level)
def f25mc_f25_margin_cyclicality_gmlevelz_252d_base_v003_signal(grossmargin):
    b = _z(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level z-scored vs its own 504d cyclical history
def f25mc_f25_margin_cyclicality_nmlevelz_504d_base_v004_signal(netmargin):
    b = _z(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin percentile rank within its 504d cycle (rich/cheap gross margin)
def f25mc_f25_margin_cyclicality_gmrank_504d_base_v005_signal(grossmargin):
    b = _rank(grossmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin percentile rank within its 252d cycle
def f25mc_f25_margin_cyclicality_nmrank_252d_base_v006_signal(netmargin):
    b = _rank(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin level percentile-ranked within its own 504d cycle (rich/cheap cash margin)
def f25mc_f25_margin_cyclicality_emlevel_63d_base_v007_signal(ebitdamargin):
    b = _rank(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level expressed as deviation from its slow 504d baseline (mid-cycle gap)
def f25mc_f25_margin_cyclicality_gmmidgap_504d_base_v008_signal(grossmargin):
    base = grossmargin.rolling(504, min_periods=168).mean()
    b = grossmargin - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level as a fraction of its own 504d peak (how close to best-ever gross margin)
def f25mc_f25_margin_cyclicality_nmvspeak_252d_base_v009_signal(grossmargin):
    pk = _rmax(grossmargin, 504)
    b = grossmargin / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin (gp/revenue) distributional skew over the cycle (asymmetry of top-line margin swings)
def f25mc_f25_margin_cyclicality_gpmdrag_63d_base_v010_signal(gp, revenue):
    gm = _f25_gp_margin(gp, revenue)
    b = gm.rolling(252, min_periods=84).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 2: MARGIN VOLATILITY THROUGH CYCLE ====

# gross-margin volatility (std) over a year — gross-margin instability
def f25mc_f25_margin_cyclicality_gmvol_252d_base_v011_signal(grossmargin):
    b = _std(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin volatility over a half-year — bottom-line instability
def f25mc_f25_margin_cyclicality_nmvol_126d_base_v012_signal(netmargin):
    b = _std(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin vol-fill ratio: realized std relative to its peak-to-trough range
def f25mc_f25_margin_cyclicality_gmcov_252d_base_v013_signal(grossmargin):
    sd = _std(grossmargin, 252)
    amp = _f25_amplitude(grossmargin, 252)
    b = sd / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of gross margin (instability of the gross-margin instability)
def f25mc_f25_margin_cyclicality_gmvov_252d_base_v014_signal(grossmargin):
    v = _std(grossmargin, 63)
    b = _std(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin downside semi-deviation (only below-mean bottom-line swings)
def f25mc_f25_margin_cyclicality_nmsemidev_252d_base_v015_signal(netmargin):
    mu = _mean(netmargin, 252)
    dev = (netmargin - mu).clip(upper=0.0)
    b = (dev * dev).rolling(252, min_periods=84).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin upside semi-deviation (only above-mean swings) — asymmetry vs nm downside
def f25mc_f25_margin_cyclicality_gmupsemidev_252d_base_v016_signal(grossmargin):
    mu = _mean(grossmargin, 252)
    dev = (grossmargin - mu).clip(lower=0.0)
    b = (dev * dev).rolling(252, min_periods=84).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin vol term structure: short 63d vol vs long 252d vol ratio
def f25mc_f25_margin_cyclicality_emvolterm_252d_base_v017_signal(ebitdamargin):
    vs = _std(ebitdamargin, 63)
    vl = _std(ebitdamargin, 252)
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin instability z-scored vs its own long history (vol regime)
def f25mc_f25_margin_cyclicality_gmvolz_504d_base_v018_signal(grossmargin):
    v = _std(grossmargin, 126)
    b = _z(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin mean-absolute-deviation over a year (robust cyclical dispersion)
def f25mc_f25_margin_cyclicality_nmmad_252d_base_v019_signal(netmargin):
    mu = _mean(netmargin, 252)
    b = (netmargin - mu).abs().rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-vol amplification ratio: net-margin instability per unit of gross-margin instability
def f25mc_f25_margin_cyclicality_volwedge_252d_base_v020_signal(grossmargin, netmargin):
    b = _std(netmargin, 252) / _std(grossmargin, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 3: MARGIN SWING AMPLITUDE ====

# gross-margin annual swing as a share of its full 504d cyclical range (recent-swing fraction)
def f25mc_f25_margin_cyclicality_gmamp_252d_base_v021_signal(grossmargin):
    short = _f25_amplitude(grossmargin, 252)
    long = _f25_amplitude(grossmargin, 504)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin range crush: how much the 126d swing sits inside the 504d swing (compression)
def f25mc_f25_margin_cyclicality_nmamp_504d_base_v022_signal(netmargin):
    short = _f25_amplitude(netmargin, 126)
    long = _f25_amplitude(netmargin, 504)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amplitude in vol-units: gross-margin swing span per short-vol unit (swing efficiency)
def f25mc_f25_margin_cyclicality_gmamprel_252d_base_v023_signal(grossmargin):
    amp = _f25_amplitude(grossmargin, 252)
    sd = _std(grossmargin, 63)
    b = amp / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin amplitude expansion: current amplitude vs its level a half-year ago
def f25mc_f25_margin_cyclicality_nmampexp_252d_base_v024_signal(netmargin):
    amp = _f25_amplitude(netmargin, 252)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin short-vs-long amplitude ratio (cyclical swing tightening)
def f25mc_f25_margin_cyclicality_gmampratio_base_v025_signal(grossmargin):
    short = _f25_amplitude(grossmargin, 126)
    long = _f25_amplitude(grossmargin, 504)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin amplitude percentile rank within its long cycle (extreme-swing regime)
def f25mc_f25_margin_cyclicality_nmamprank_504d_base_v026_signal(netmargin):
    amp = _f25_amplitude(netmargin, 252)
    b = _rank(amp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread percentile rank within its 504d cycle (rich/cheap cost-wedge phase)
def f25mc_f25_margin_cyclicality_spreadamp_252d_base_v027_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = _rank(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin swing energy: sum of squared daily margin moves over a year
def f25mc_f25_margin_cyclicality_gmenergy_252d_base_v028_signal(grossmargin):
    d = grossmargin.diff()
    b = (d * d).rolling(252, min_periods=84).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin directional efficiency: net 252d displacement over total path (trend vs chop)
def f25mc_f25_margin_cyclicality_nmpathlen_252d_base_v029_signal(netmargin):
    net = (netmargin - netmargin.shift(252)).abs()
    path = netmargin.diff().abs().rolling(252, min_periods=84).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amplitude asymmetry: how much of the gross-margin swing is above vs below its median
def f25mc_f25_margin_cyclicality_gmampskew_252d_base_v030_signal(grossmargin):
    hi = _rmax(grossmargin, 252)
    lo = _rmin(grossmargin, 252)
    med = grossmargin.rolling(252, min_periods=84).median()
    b = (hi - med) - (med - lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 4: GROSS-VS-NET SPREAD (cross-cluster — genuinely distinct) ====

# gross-minus-net spread level, smoothed (below-the-line cost drag level)
def f25mc_f25_margin_cyclicality_gnspread_63d_base_v031_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = sp.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-net spread z-scored vs its own cycle (cost-wedge regime)
def f25mc_f25_margin_cyclicality_gnspreadz_252d_base_v032_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-compression regime: fraction of the year gross margin sat below its 252d mean (count-friendly)
def f25mc_f25_margin_cyclicality_gespread_63d_base_v033_signal(grossmargin):
    mu = grossmargin.rolling(252, min_periods=84).mean()
    below = (grossmargin < mu).astype(float)
    b = below.rolling(252, min_periods=84).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-minus-net spread level (interest + tax wedge below EBITDA)
def f25mc_f25_margin_cyclicality_enspread_63d_base_v034_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    b = sp.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread as a fraction of gross margin (fraction of margin lost below line)
def f25mc_f25_margin_cyclicality_gnspreadfrac_63d_base_v035_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    frac = sp / grossmargin.abs().replace(0, np.nan)
    b = frac.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of the gross-vs-net spread (cost-structure instability)
def f25mc_f25_margin_cyclicality_gnspreadvol_252d_base_v036_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = _std(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin minus net-margin spread (interest+tax wedge below EBIT)
def f25mc_f25_margin_cyclicality_onspread_63d_base_v037_signal(opinc, revenue, netmargin):
    om = _f25_op_margin(opinc, revenue)
    b = (om - netmargin).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin convexity: curvature of the recent EBIT-margin path (2nd-difference mean)
def f25mc_f25_margin_cyclicality_gospread_63d_base_v038_signal(opinc, revenue):
    om = _f25_op_margin(opinc, revenue)
    d2 = om.diff().diff()
    b = d2.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread trend: is the below-the-line drag widening or narrowing
def f25mc_f25_margin_cyclicality_gnspreadtrend_126d_base_v039_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = _slope(sp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-minus-net spread percentile rank vs its long cycle (rich/cheap tax+interest wedge)
def f25mc_f25_margin_cyclicality_enspreadrank_504d_base_v040_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    b = _rank(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 5: MARGIN TREND ====

# gross-margin trend: slope over a half-year (gross-margin direction)
def f25mc_f25_margin_cyclicality_gmtrend_126d_base_v041_signal(grossmargin):
    b = _slope(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend: slope over a quarter (bottom-line direction)
def f25mc_f25_margin_cyclicality_nmtrend_63d_base_v042_signal(netmargin):
    b = _slope(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin MA-crossover trend (fast 63d minus slow 252d mean)
def f25mc_f25_margin_cyclicality_gmmacross_base_v043_signal(grossmargin):
    fast = grossmargin.rolling(63, min_periods=21).mean()
    slow = grossmargin.rolling(252, min_periods=84).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin MA-crossover trend (fast 42d minus slow 168d mean) — different windows
def f25mc_f25_margin_cyclicality_nmmacross_base_v044_signal(netmargin):
    fast = netmargin.rolling(42, min_periods=14).mean()
    slow = netmargin.rolling(168, min_periods=56).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend strength: slope divided by margin vol (t-stat-like reliability)
def f25mc_f25_margin_cyclicality_gmtrendstr_126d_base_v045_signal(grossmargin):
    sl = _slope(grossmargin, 126)
    vol = _std(grossmargin, 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin year-over-year change (cyclical YoY bottom-line shift)
def f25mc_f25_margin_cyclicality_nmyoy_252d_base_v046_signal(netmargin):
    b = netmargin - netmargin.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend acceleration: slope now minus slope a quarter ago
def f25mc_f25_margin_cyclicality_gmtrendaccel_base_v047_signal(grossmargin):
    sl = _slope(grossmargin, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend sign persistence (fraction of quarter the bottom line improved)
def f25mc_f25_margin_cyclicality_nmtrendpersist_base_v048_signal(netmargin):
    up = (netmargin.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin EWMA displacement: level minus its slow EMA (trend displacement)
def f25mc_f25_margin_cyclicality_gmemadisp_base_v049_signal(grossmargin):
    b = grossmargin - grossmargin.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin tail kurtosis over the cycle (fat-tailed cash-margin shocks)
def f25mc_f25_margin_cyclicality_emtrend_252d_base_v050_signal(ebitdamargin):
    b = ebitdamargin.rolling(252, min_periods=84).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 6: MARGIN TROUGH / PEAK DISTANCE ====

# distance of gross margin above its 252d cyclical trough (margin recovery)
def f25mc_f25_margin_cyclicality_gmtrough_252d_base_v051_signal(grossmargin):
    b = _f25_trough_dist(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of net margin below its 252d cyclical peak (bottom-line compression)
def f25mc_f25_margin_cyclicality_nmpeak_252d_base_v052_signal(netmargin):
    b = _f25_peak_dist(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin position within its 252d cyclical range (0=trough, 1=peak)
def f25mc_f25_margin_cyclicality_gmrangepos_252d_base_v053_signal(grossmargin):
    b = _f25_range_pos(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin position within its 126d cyclical range (short-cycle phase)
def f25mc_f25_margin_cyclicality_nmrangepos_504d_base_v054_signal(netmargin):
    b = _f25_range_pos(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin recovery off the 252d trough measured in short-vol units (vol-scaled rebound)
def f25mc_f25_margin_cyclicality_gmtroughrel_252d_base_v055_signal(grossmargin):
    tr = _f25_trough_dist(grossmargin, 252)
    sd = _std(grossmargin, 63)
    b = tr / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin compression in vol-units: distance below 504d peak per short-vol unit
def f25mc_f25_margin_cyclicality_nmpeakrel_252d_base_v056_signal(netmargin):
    pk = _f25_peak_dist(netmargin, 504)
    sd = _std(netmargin, 63)
    b = pk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since gross-margin cyclical trough (staleness of the margin low)
def f25mc_f25_margin_cyclicality_gmdsl_252d_base_v057_signal(grossmargin):
    b = _f25_days_since_min(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since net-margin cyclical peak (staleness of the bottom-line high)
def f25mc_f25_margin_cyclicality_nmdsh_252d_base_v058_signal(netmargin):
    b = _f25_days_since_max(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin run-up off its trailing 504d trough (long recovery run)
def f25mc_f25_margin_cyclicality_gmrunup_504d_base_v059_signal(grossmargin):
    b = grossmargin - _rmin(grossmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin distance to its 504d mid relative to amplitude (long mid-cycle skew)
def f25mc_f25_margin_cyclicality_nmmidskew_126d_base_v060_signal(grossmargin):
    hi = _rmax(grossmargin, 504)
    lo = _rmin(grossmargin, 504)
    mid = (hi + lo) / 2.0
    b = (grossmargin - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 7: REGIME / STREAK / ASYMMETRY (count-friendly, cyclical) ====

# operating-income sign regime: fraction of the year with positive operating income
def f25mc_f25_margin_cyclicality_opincposfreq_252d_base_v061_signal(opinc):
    pos = (opinc > 0).astype(float)
    b = pos.rolling(252, min_periods=84).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin weakness regime: fraction of the year below its own 504d median (sub-par bottom line)
def f25mc_f25_margin_cyclicality_nmlossfreq_252d_base_v062_signal(netmargin):
    med = netmargin.rolling(504, min_periods=126).median()
    weak = (netmargin < med).astype(float)
    b = weak.rolling(252, min_periods=84).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin good-time fraction: share of the year in the upper third of its cycle
def f25mc_f25_margin_cyclicality_gmuppertime_252d_base_v063_signal(grossmargin):
    pos = _f25_range_pos(grossmargin, 252)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trough-touch time: avg closeness to the 126d cyclical low over a year
def f25mc_f25_margin_cyclicality_nmtroughtouch_252d_base_v064_signal(netmargin):
    lo = _rmin(netmargin, 126)
    hi = _rmax(netmargin, 126)
    nearness = (hi - netmargin) / (hi - lo).replace(0, np.nan)
    b = nearness.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin improvement streak: consecutive up-quarters of the smoothed level
def f25mc_f25_margin_cyclicality_gmupstreak_base_v065_signal(grossmargin):
    sm = grossmargin.rolling(21, min_periods=7).mean()
    up = (sm.diff() > 0).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin distributional skew over the cycle (asymmetry of bottom-line swings)
def f25mc_f25_margin_cyclicality_nmskew_252d_base_v066_signal(netmargin):
    b = netmargin.rolling(252, min_periods=84).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin tail kurtosis over the cycle (fat-tailed margin shocks)
def f25mc_f25_margin_cyclicality_gmkurt_252d_base_v067_signal(grossmargin):
    b = grossmargin.rolling(252, min_periods=84).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-underwater duration: share of the year >20% of amplitude below the gross peak
def f25mc_f25_margin_cyclicality_gmdd_252d_base_v068_signal(grossmargin):
    pk = _rmax(grossmargin, 252)
    amp = _f25_amplitude(grossmargin, 252)
    underwater = (pk - grossmargin) / amp.replace(0, np.nan)
    deep = (underwater >= 0.20).astype(float)
    b = deep.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin regime balance: magnitude-weighted time spent above vs below its 252d mean
def f25mc_f25_margin_cyclicality_nmflipcount_252d_base_v069_signal(netmargin):
    mu = netmargin.rolling(252, min_periods=84).mean()
    dev = netmargin - mu
    up = dev.clip(lower=0.0).rolling(252, min_periods=84).sum()
    dn = (-dev).clip(lower=0.0).rolling(252, min_periods=84).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin tanh-squashed YoY change (bounded cyclical margin swing)
def f25mc_f25_margin_cyclicality_gmyoytanh_base_v070_signal(grossmargin):
    chg = grossmargin - grossmargin.shift(252)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 8: CROSS-MARGIN INTERACTION / COMPOSITE ====

# cyclical co-movement: rolling corr of gross & net margins (do they move together)
def f25mc_f25_margin_cyclicality_gncorr_252d_base_v071_signal(grossmargin, netmargin):
    b = grossmargin.rolling(252, min_periods=84).corr(netmargin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling beta of net margin to gross margin (below-line leverage to top-line margin)
def f25mc_f25_margin_cyclicality_nmbeta_252d_base_v072_signal(grossmargin, netmargin):
    cov = grossmargin.rolling(252, min_periods=84).cov(netmargin)
    var = grossmargin.rolling(252, min_periods=84).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion across the three margin measures (cyclical margin disagreement)
def f25mc_f25_margin_cyclicality_margindisp_base_v073_signal(grossmargin, netmargin, ebitdamargin):
    stacked = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-phase spread: net-margin range-pos minus gross-margin range-pos (lead/lag)
def f25mc_f25_margin_cyclicality_phasespread_252d_base_v074_signal(grossmargin, netmargin):
    b = _f25_range_pos(netmargin, 252) - _f25_range_pos(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin stability quality: mean gp-margin per unit of its own volatility (durable margin)
def f25mc_f25_margin_cyclicality_gpstab_252d_base_v075_signal(gp, revenue):
    gm = _f25_gp_margin(gp, revenue)
    mu = _mean(gm, 252)
    sd = _std(gm, 252)
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25mc_f25_margin_cyclicality_gmlevel_63d_base_v001_signal,
    f25mc_f25_margin_cyclicality_nmlevel_126d_base_v002_signal,
    f25mc_f25_margin_cyclicality_gmlevelz_252d_base_v003_signal,
    f25mc_f25_margin_cyclicality_nmlevelz_504d_base_v004_signal,
    f25mc_f25_margin_cyclicality_gmrank_504d_base_v005_signal,
    f25mc_f25_margin_cyclicality_nmrank_252d_base_v006_signal,
    f25mc_f25_margin_cyclicality_emlevel_63d_base_v007_signal,
    f25mc_f25_margin_cyclicality_gmmidgap_504d_base_v008_signal,
    f25mc_f25_margin_cyclicality_nmvspeak_252d_base_v009_signal,
    f25mc_f25_margin_cyclicality_gpmdrag_63d_base_v010_signal,
    f25mc_f25_margin_cyclicality_gmvol_252d_base_v011_signal,
    f25mc_f25_margin_cyclicality_nmvol_126d_base_v012_signal,
    f25mc_f25_margin_cyclicality_gmcov_252d_base_v013_signal,
    f25mc_f25_margin_cyclicality_gmvov_252d_base_v014_signal,
    f25mc_f25_margin_cyclicality_nmsemidev_252d_base_v015_signal,
    f25mc_f25_margin_cyclicality_gmupsemidev_252d_base_v016_signal,
    f25mc_f25_margin_cyclicality_emvolterm_252d_base_v017_signal,
    f25mc_f25_margin_cyclicality_gmvolz_504d_base_v018_signal,
    f25mc_f25_margin_cyclicality_nmmad_252d_base_v019_signal,
    f25mc_f25_margin_cyclicality_volwedge_252d_base_v020_signal,
    f25mc_f25_margin_cyclicality_gmamp_252d_base_v021_signal,
    f25mc_f25_margin_cyclicality_nmamp_504d_base_v022_signal,
    f25mc_f25_margin_cyclicality_gmamprel_252d_base_v023_signal,
    f25mc_f25_margin_cyclicality_nmampexp_252d_base_v024_signal,
    f25mc_f25_margin_cyclicality_gmampratio_base_v025_signal,
    f25mc_f25_margin_cyclicality_nmamprank_504d_base_v026_signal,
    f25mc_f25_margin_cyclicality_spreadamp_252d_base_v027_signal,
    f25mc_f25_margin_cyclicality_gmenergy_252d_base_v028_signal,
    f25mc_f25_margin_cyclicality_nmpathlen_252d_base_v029_signal,
    f25mc_f25_margin_cyclicality_gmampskew_252d_base_v030_signal,
    f25mc_f25_margin_cyclicality_gnspread_63d_base_v031_signal,
    f25mc_f25_margin_cyclicality_gnspreadz_252d_base_v032_signal,
    f25mc_f25_margin_cyclicality_gespread_63d_base_v033_signal,
    f25mc_f25_margin_cyclicality_enspread_63d_base_v034_signal,
    f25mc_f25_margin_cyclicality_gnspreadfrac_63d_base_v035_signal,
    f25mc_f25_margin_cyclicality_gnspreadvol_252d_base_v036_signal,
    f25mc_f25_margin_cyclicality_onspread_63d_base_v037_signal,
    f25mc_f25_margin_cyclicality_gospread_63d_base_v038_signal,
    f25mc_f25_margin_cyclicality_gnspreadtrend_126d_base_v039_signal,
    f25mc_f25_margin_cyclicality_enspreadrank_504d_base_v040_signal,
    f25mc_f25_margin_cyclicality_gmtrend_126d_base_v041_signal,
    f25mc_f25_margin_cyclicality_nmtrend_63d_base_v042_signal,
    f25mc_f25_margin_cyclicality_gmmacross_base_v043_signal,
    f25mc_f25_margin_cyclicality_nmmacross_base_v044_signal,
    f25mc_f25_margin_cyclicality_gmtrendstr_126d_base_v045_signal,
    f25mc_f25_margin_cyclicality_nmyoy_252d_base_v046_signal,
    f25mc_f25_margin_cyclicality_gmtrendaccel_base_v047_signal,
    f25mc_f25_margin_cyclicality_nmtrendpersist_base_v048_signal,
    f25mc_f25_margin_cyclicality_gmemadisp_base_v049_signal,
    f25mc_f25_margin_cyclicality_emtrend_252d_base_v050_signal,
    f25mc_f25_margin_cyclicality_gmtrough_252d_base_v051_signal,
    f25mc_f25_margin_cyclicality_nmpeak_252d_base_v052_signal,
    f25mc_f25_margin_cyclicality_gmrangepos_252d_base_v053_signal,
    f25mc_f25_margin_cyclicality_nmrangepos_504d_base_v054_signal,
    f25mc_f25_margin_cyclicality_gmtroughrel_252d_base_v055_signal,
    f25mc_f25_margin_cyclicality_nmpeakrel_252d_base_v056_signal,
    f25mc_f25_margin_cyclicality_gmdsl_252d_base_v057_signal,
    f25mc_f25_margin_cyclicality_nmdsh_252d_base_v058_signal,
    f25mc_f25_margin_cyclicality_gmrunup_504d_base_v059_signal,
    f25mc_f25_margin_cyclicality_nmmidskew_126d_base_v060_signal,
    f25mc_f25_margin_cyclicality_opincposfreq_252d_base_v061_signal,
    f25mc_f25_margin_cyclicality_nmlossfreq_252d_base_v062_signal,
    f25mc_f25_margin_cyclicality_gmuppertime_252d_base_v063_signal,
    f25mc_f25_margin_cyclicality_nmtroughtouch_252d_base_v064_signal,
    f25mc_f25_margin_cyclicality_gmupstreak_base_v065_signal,
    f25mc_f25_margin_cyclicality_nmskew_252d_base_v066_signal,
    f25mc_f25_margin_cyclicality_gmkurt_252d_base_v067_signal,
    f25mc_f25_margin_cyclicality_gmdd_252d_base_v068_signal,
    f25mc_f25_margin_cyclicality_nmflipcount_252d_base_v069_signal,
    f25mc_f25_margin_cyclicality_gmyoytanh_base_v070_signal,
    f25mc_f25_margin_cyclicality_gncorr_252d_base_v071_signal,
    f25mc_f25_margin_cyclicality_nmbeta_252d_base_v072_signal,
    f25mc_f25_margin_cyclicality_margindisp_base_v073_signal,
    f25mc_f25_margin_cyclicality_phasespread_252d_base_v074_signal,
    f25mc_f25_margin_cyclicality_gpstab_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_MARGIN_CYCLICALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    grossmargin = _fund(2501, base=0.32, drift=0.0, vol=0.16).rename("grossmargin")
    netmargin = _fund(2502, base=0.12, drift=0.0, vol=0.30, allow_neg=False).rename("netmargin")
    ebitdamargin = _fund(2503, base=0.22, drift=0.0, vol=0.22).rename("ebitdamargin")
    opinc = _fund(2504, base=8e7, drift=0.0, vol=0.26, allow_neg=True).rename("opinc")
    revenue = _fund(2505, base=6e8, drift=0.01, vol=0.12).rename("revenue")
    gp = _fund(2506, base=2e8, drift=0.0, vol=0.16).rename("gp")

    cols = {"grossmargin": grossmargin, "netmargin": netmargin,
            "ebitdamargin": ebitdamargin, "opinc": opinc,
            "revenue": revenue, "gp": gp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("grossmargin", "netmargin", "ebitdamargin",
                         "opinc", "revenue", "gp")
                   for c in meta["inputs"]), name
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

    print("OK f25_margin_cyclicality_base_001_075_claude: %d features pass" % n_features)
