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


# ===== folder domain primitives (cash-flow cyclicality) =====
def _f32_fcf_margin(fcf, revenue):
    # free-cash-flow margin (FCF per dollar of revenue)
    return fcf / revenue.replace(0, np.nan)


def _f32_ocf_margin(ncfo, revenue):
    # operating-cash-flow margin
    return ncfo / revenue.replace(0, np.nan)


def _f32_fcf_after_capex(ncfo, capex):
    # FCF rebuilt from operating cash flow after capex (FCF-after-capex)
    return ncfo - capex


def _f32_capex_cover(ncfo, capex):
    # how many times operating cash flow covers capex
    return ncfo / capex.replace(0, np.nan)


def _f32_fcf_conversion(fcf, ncfo):
    # fraction of operating cash flow that survives to free cash flow
    return fcf / ncfo.replace(0, np.nan)


def _f32_sign_sqrt(s):
    return np.sign(s) * (s.abs() ** 0.5)


# ============================================================
# --- FCF MARGIN LEVELS ---
# free-cash-flow margin level, smoothed over a quarter (cyclical cash profitability)
def f32cf_f32_cash_flow_cyclicality_fcfmargin_63d_base_v001_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.clip(lower=-3.0, upper=3.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin z-scored vs its own 252d history (de-trended cyclical margin)
def f32cf_f32_cash_flow_cyclicality_fcfmarginz_252d_base_v002_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin percentile-rank vs 504d (where in the cash-margin cycle)
def f32cf_f32_cash_flow_cyclicality_fcfmarginrank_504d_base_v003_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-flow margin level, smoothed (OCF profitability)
def f32cf_f32_cash_flow_cyclicality_ocfmargin_63d_base_v004_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    b = m.clip(lower=-3.0, upper=3.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin z-scored vs its own 252d history
def f32cf_f32_cash_flow_cyclicality_ocfmarginz_252d_base_v005_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between OCF margin and FCF margin (capex drag on cash profitability)
def f32cf_f32_cash_flow_cyclicality_marginspread_63d_base_v006_signal(ncfo, fcf, revenue):
    om = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    fm = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = (om - fm).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF MARGIN SWING / AMPLITUDE (cyclicality) ---
# FCF-margin swing amplitude: peak-to-trough range over a year (cyclical span)
def f32cf_f32_cash_flow_cyclicality_fcfswing_252d_base_v007_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _rmax(m, 252) - _rmin(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin swing amplitude over two years (longer cyclical span)
def f32cf_f32_cash_flow_cyclicality_fcfswing_504d_base_v008_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _rmax(m, 504) - _rmin(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position of current FCF margin within its 252d peak-trough band (cycle phase)
def f32cf_f32_cash_flow_cyclicality_fcfcyclepos_252d_base_v009_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    b = (m - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of FCF margin below its 252d cyclical peak (downcycle depth)
def f32cf_f32_cash_flow_cyclicality_fcfpeakgap_252d_base_v010_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m - _rmax(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of FCF margin above its 504d cyclical trough (recovery height)
def f32cf_f32_cash_flow_cyclicality_fcftroughgap_504d_base_v011_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m - _rmin(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF / OCF VOLATILITY (cyclicality magnitude) ---
# FCF-margin volatility over a year (erratic vs steady cash generation)
def f32cf_f32_cash_flow_cyclicality_fcfvol_252d_base_v012_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin volatility over a year
def f32cf_f32_cash_flow_cyclicality_ocfvol_252d_base_v013_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = m.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of FCF-after-capex over a year (cash-flow instability)
def f32cf_f32_cash_flow_cyclicality_fcfcv_252d_base_v014_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    sd = _std(f, 252)
    m = _mean(f.abs(), 252)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short-window to long-window FCF-margin vol (vol term structure)
def f32cf_f32_cash_flow_cyclicality_fcfvolterm_base_v015_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    short = m.rolling(63, min_periods=21).std()
    long = m.rolling(252, min_periods=126).std()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share volatility over a year (per-share cash cyclicality)
def f32cf_f32_cash_flow_cyclicality_fcfpsvol_252d_base_v016_signal(fcfps):
    b = fcfps.rolling(252, min_periods=126).std() / _mean(fcfps.abs(), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF INFLECTION (negative -> positive) ---
# fraction of last year FCF-after-capex was positive (cash-positive prevalence)
def f32cf_f32_cash_flow_cyclicality_fcfpostime_252d_base_v017_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    pos = (f > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh negative->positive FCF crossings over the last year (inflection tally)
def f32cf_f32_cash_flow_cyclicality_fcfinflect_252d_base_v018_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    pos = (f > 0).astype(float)
    cross_up = ((pos == 1) & (pos.shift(1) == 0)).astype(float)
    b = cross_up.rolling(252, min_periods=126).sum() + 0.25 * pos.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed proximity to FCF break-even (distance from zero, sign x sqrt magnitude)
def f32cf_f32_cash_flow_cyclicality_fcfbreakeven_63d_base_v019_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _f32_sign_sqrt(m).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since FCF last turned positive (staleness of cash-positive inflection)
def f32cf_f32_cash_flow_cyclicality_fcfsincepos_252d_base_v020_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    pos = (f > 0).astype(float)

    def _dsl(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))
    b = pos.rolling(252, min_periods=126).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin sign flipped to mostly-positive regime: signed avg over a half year
def f32cf_f32_cash_flow_cyclicality_fcfsignavg_126d_base_v021_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = np.sign(m).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF CONSISTENCY / QUALITY ---
# FCF consistency: fraction of quarters in last year with positive FCF-after-capex
def f32cf_f32_cash_flow_cyclicality_fcfconsist_252d_base_v022_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    pos = (f > 0).astype(float)
    frac = pos.rolling(252, min_periods=126).mean()
    # weight by how deep positive when positive (steadiness x strength)
    depth = f.clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.0 * depth + np.tanh(depth / (f.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion (fcf/ncfo) smoothed: how much OCF survives capex (quality)
def f32cf_f32_cash_flow_cyclicality_fcfconv_63d_base_v023_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = c.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion z-scored vs 252d (conversion regime shift)
def f32cf_f32_cash_flow_cyclicality_fcfconvz_252d_base_v024_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime churn: rolling mean absolute quarter-over-quarter change in FCF margin
def f32cf_f32_cash_flow_cyclicality_fcfchurn_252d_base_v025_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    step = (m - m.shift(21)).abs()
    b = step.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- OCF TREND ---
# operating-cash-flow log-trend over a quarter (cash-generation momentum)
def f32cf_f32_cash_flow_cyclicality_ocftrend_63d_base_v026_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF year-over-year change (cyclical OCF shift)
def f32cf_f32_cash_flow_cyclicality_ocfyoy_252d_base_v027_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin trend over half a year (path of cash profitability)
def f32cf_f32_cash_flow_cyclicality_ocfmargintrend_126d_base_v028_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF drawdown from its trailing 252d peak (loss of cash-generation strength)
def f32cf_f32_cash_flow_cyclicality_ocfdd_252d_base_v029_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    peak = _rmax(s, 252)
    b = s - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF percentile-rank vs 504d (where OCF sits in its multi-year range)
def f32cf_f32_cash_flow_cyclicality_ocfrank_504d_base_v030_signal(ncfo):
    b = _rank(ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF-AFTER-CAPEX COVERAGE ---
# OCF coverage of capex, smoothed (can operations self-fund development?)
def f32cf_f32_cash_flow_cyclicality_capexcover_63d_base_v031_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = c.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage z-scored vs 252d (coverage regime)
def f32cf_f32_cash_flow_cyclicality_capexcoverz_252d_base_v032_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# under-coverage onset tally: count of fresh entries into capex-uncovered regime over a year
def f32cf_f32_cash_flow_cyclicality_undercoveronset_252d_base_v033_signal(ncfo, capex):
    uncov = (ncfo < capex).astype(float)
    entries = ((uncov == 1) & (uncov.shift(1) == 0)).astype(float)
    shortfall = (capex - ncfo).clip(lower=0) / capex.replace(0, np.nan)
    b = entries.rolling(252, min_periods=126).sum() + 0.5 * shortfall.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity (capex/revenue) smoothed — investment phase of the cash cycle
def f32cf_f32_cash_flow_cyclicality_capexintensity_63d_base_v034_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity z-scored vs 252d (over/under-investment vs own norm)
def f32cf_f32_cash_flow_cyclicality_capexintensz_252d_base_v035_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-after-capex scaled by revenue, ranked vs 504d (cash-yield percentile)
def f32cf_f32_cash_flow_cyclicality_fcfyieldrank_504d_base_v036_signal(ncfo, capex, revenue):
    f = _f32_fcf_after_capex(ncfo, capex)
    y = (f / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    b = _rank(y, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF PER SHARE FORMS ---
# FCF-per-share level, smoothed via signed-sqrt (per-share cash level)
def f32cf_f32_cash_flow_cyclicality_fcfps_63d_base_v037_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share z-scored vs 252d (de-trended per-share cash cycle)
def f32cf_f32_cash_flow_cyclicality_fcfpsz_252d_base_v038_signal(fcfps):
    b = _z(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share cyclical position within its 252d range (per-share cycle phase)
def f32cf_f32_cash_flow_cyclicality_fcfpspos_252d_base_v039_signal(fcfps):
    hi = _rmax(fcfps, 252)
    lo = _rmin(fcfps, 252)
    b = (fcfps - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share year-over-year change (per-share cash growth across cycle)
def f32cf_f32_cash_flow_cyclicality_fcfpsyoy_252d_base_v040_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year FCF-per-share positive (per-share cash-positive prevalence)
def f32cf_f32_cash_flow_cyclicality_fcfpspostime_252d_base_v041_signal(fcfps):
    pos = (fcfps > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RATIOS SHORT/LONG (term structure of cash generation) ---
# short-vs-long FCF margin ratio (recent cash margin vs structural)
def f32cf_f32_cash_flow_cyclicality_fcfmarginterm_base_v042_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    short = m.rolling(63, min_periods=21).mean()
    long = m.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long OCF level ratio (recent cash gen vs structural, signed)
def f32cf_f32_cash_flow_cyclicality_ocfterm_base_v043_signal(ncfo):
    short = ncfo.rolling(63, min_periods=21).mean()
    long = ncfo.rolling(252, min_periods=126).mean()
    b = (short - long) / long.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long FCF-after-capex coverage ratio (recent vs structural self-funding)
def f32cf_f32_cash_flow_cyclicality_coverterm_base_v044_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    short = c.rolling(63, min_periods=21).mean()
    long = c.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / DRAWDOWN of FCF ---
# FCF-after-capex drawdown from its 252d peak (loss of free-cash strength)
def f32cf_f32_cash_flow_cyclicality_fcfdd_252d_base_v045_signal(ncfo, capex):
    f = _f32_sign_sqrt(_f32_fcf_after_capex(ncfo, capex))
    peak = _rmax(f, 252)
    b = f - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# minimum FCF margin over last half year (worst recent cash point)
def f32cf_f32_cash_flow_cyclicality_fcfmin_126d_base_v046_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _rmin(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of cash margins across short/medium/long windows (margin disagreement)
def f32cf_f32_cash_flow_cyclicality_fcfdisp_multi_base_v047_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    a = m.rolling(63, min_periods=21).mean()
    b2 = m.rolling(126, min_periods=63).mean()
    c = m.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTERACTIONS ---
# cyclicality interaction: FCF-margin swing x how negative the trough is (deep-cycle)
def f32cf_f32_cash_flow_cyclicality_swingXtrough_252d_base_v048_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    swing = _rmax(m, 252) - _rmin(m, 252)
    trough = (-_rmin(m, 252)).clip(lower=0)
    b = swing * trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-into-weak-cash: capex intensity x (1 - FCF positivity) over a year
def f32cf_f32_cash_flow_cyclicality_capexXweak_252d_base_v049_signal(ncfo, capex, revenue):
    f = _f32_fcf_after_capex(ncfo, capex)
    weak = 1.0 - (f > 0).astype(float).rolling(252, min_periods=126).mean()
    intens = (capex / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = intens * weak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin x revenue-growth interaction (cash conversion during ramp)
def f32cf_f32_cash_flow_cyclicality_ocfXrevgrow_126d_base_v050_signal(ncfo, revenue):
    om = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    revg = np.log(revenue.replace(0, np.nan)) - np.log(revenue.shift(126).replace(0, np.nan))
    b = om * revg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MORE LEVEL / NORMALIZATION VARIANTS ---
# FCF margin smoothed over half a year (structural cash profitability)
def f32cf_f32_cash_flow_cyclicality_fcfmargin_126d_base_v051_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year vs full-year OCF-margin gap (medium-term cash-margin tilt)
def f32cf_f32_cash_flow_cyclicality_ocfmargintilt_252d_base_v052_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    half = m.rolling(126, min_periods=63).mean()
    full = m.rolling(252, min_periods=126).median()
    b = half - full
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin displacement: level minus its slow EMA (acute vs chronic cash margin)
def f32cf_f32_cash_flow_cyclicality_fcfmargindisp_63d_base_v053_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage displacement: level minus its slow EMA (acute vs chronic self-funding)
def f32cf_f32_cash_flow_cyclicality_capexcoverdisp_63d_base_v054_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = c - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# critical-cash time: fraction of last year FCF margin below zero, weighted by depth
def f32cf_f32_cash_flow_cyclicality_critcashtime_252d_base_v055_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    crit = (m < 0).astype(float)
    frac = crit.rolling(252, min_periods=126).mean()
    depth = (-m).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-FLOW CURVATURE-LIKE (base second differences) ---
# FCF-margin second difference (cyclical acceleration, base form)
def f32cf_f32_cash_flow_cyclicality_fcfaccel_63d_base_v056_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    d1 = m - m.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin curvature: minus average of lead/lag (concavity, base form)
def f32cf_f32_cash_flow_cyclicality_ocfcurv_63d_base_v057_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = m - 0.5 * (m.shift(63) + m.shift(-63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage acceleration (base second difference)
def f32cf_f32_cash_flow_cyclicality_coveraccel_42d_base_v058_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    d1 = c - c.shift(42)
    b = d1 - d1.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REVENUE-NORMALIZED CASH FORMS ---
# revenue-scaled FCF (cash output per revenue dollar) ranked vs 252d
def f32cf_f32_cash_flow_cyclicality_fcfrevrank_252d_base_v059_signal(fcf, revenue):
    y = (fcf / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    b = _rank(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclicality of cash: corr-like product of revenue-change and FCF-change sign
def f32cf_f32_cash_flow_cyclicality_cashrevsync_126d_base_v060_signal(fcf, revenue):
    dfcf = np.sign(fcf - fcf.shift(63))
    drev = np.sign(revenue - revenue.shift(63))
    sync = (dfcf * drev)
    b = sync.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted OCF margin: level divided by its own 126d volatility (cash Sharpe)
def f32cf_f32_cash_flow_cyclicality_ocfrisadj_126d_base_v061_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    vol = m.rolling(126, min_periods=63).std()
    b = (m.rolling(63, min_periods=21).mean()) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE CYCLICALITY SCORES ---
# cash-cyclicality ratio: short-horizon churn relative to full-cycle swing
# (how jagged the path is per unit of its peak-trough span)
def f32cf_f32_cash_flow_cyclicality_cyccomposite_252d_base_v062_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    swing = (_rmax(m, 252) - _rmin(m, 252)).replace(0, np.nan)
    step = (m - m.shift(21)).abs().rolling(252, min_periods=126).mean()
    b = step / swing
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trough-recovery quality: FCF height above trough x time-since-trough (matured recovery)
def f32cf_f32_cash_flow_cyclicality_recovqual_252d_base_v063_signal(ncfo, capex):
    f = _f32_sign_sqrt(_f32_fcf_after_capex(ncfo, capex))
    lo = _rmin(f, 252)
    rec = f - lo

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dst = f.rolling(252, min_periods=126).apply(_dsl, raw=True)
    b = rec * dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-case coverage: OCF over peak capex in last year (cushion at peak investment)
def f32cf_f32_cash_flow_cyclicality_worstcover_252d_base_v064_signal(ncfo, capex):
    peak_capex = _rmax(capex, 252)
    b = (ncfo / peak_capex.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF / OCF CROSS FORMS ---
# OCF-margin minus FCF-margin trend (capex drag building/easing)
def f32cf_f32_cash_flow_cyclicality_dragtrend_126d_base_v065_signal(ncfo, fcf, revenue):
    drag = (_f32_ocf_margin(ncfo, revenue) - _f32_fcf_margin(fcf, revenue)).clip(lower=-3.0, upper=3.0)
    b = drag - drag.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-OCF conversion stability (1 - dispersion of conversion over a year)
def f32cf_f32_cash_flow_cyclicality_convstab_252d_base_v066_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = -c.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash margin net of investment: OCF margin minus capex intensity (free-cash spread)
def f32cf_f32_cash_flow_cyclicality_netcashmargin_63d_base_v067_signal(ncfo, capex, revenue):
    om = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    capint = (capex / revenue.replace(0, np.nan)).clip(lower=0.0, upper=3.0)
    b = (om - capint).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANK / Z VARIANTS ---
# FCF dispersion-of-changes: std of 21d FCF differences over a year (cash-flow jaggedness)
def f32cf_f32_cash_flow_cyclicality_fcfchgvol_252d_base_v068_signal(fcf):
    chg = fcf - fcf.shift(21)
    scale = fcf.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = (chg / scale).rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity percentile-rank vs 504d (investment-phase percentile)
def f32cf_f32_cash_flow_cyclicality_capexrank_504d_base_v069_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share percentile-rank vs 504d (per-share cash percentile)
def f32cf_f32_cash_flow_cyclicality_fcfpsrank_504d_base_v070_signal(fcfps):
    b = _rank(fcfps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EXTREME / TAIL FORMS ---
# down-cycle prevalence: fraction of last year FCF margin sat below its 252d median
def f32cf_f32_cash_flow_cyclicality_downcycletime_252d_base_v071_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    below = (m < med).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current FCF-positive streak length (consecutive days of free-cash generation), log-scaled
def f32cf_f32_cash_flow_cyclicality_fcfposstreak_base_v072_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    pos = (f > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    b = np.log1p(streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin tanh-squashed momentum (bounded cyclical change over a quarter)
def f32cf_f32_cash_flow_cyclicality_fcftanh_63d_base_v073_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    chg = m - m.shift(63)
    b = np.tanh(3.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-vs-OCF divergence: capex ramp minus OCF ramp (over-investing into weak cash)
def f32cf_f32_cash_flow_cyclicality_capexocfdiverge_63d_base_v074_signal(ncfo, capex):
    capex_ramp = np.log(capex.replace(0, np.nan)) - np.log(capex.shift(63).replace(0, np.nan))
    s = _f32_sign_sqrt(ncfo)
    ocf_ramp = (s - s.shift(63)) / s.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = capex_ramp - ocf_ramp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cash-cycle phase: FCF cycle position minus capex intensity rank (phase score)
def f32cf_f32_cash_flow_cyclicality_cyclephase_252d_base_v075_signal(fcf, revenue, capex):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    pos = (m - lo) / (hi - lo).replace(0, np.nan)
    capint = _rank(capex / revenue.replace(0, np.nan), 252)
    b = pos - capint
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32cf_f32_cash_flow_cyclicality_fcfmargin_63d_base_v001_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginz_252d_base_v002_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginrank_504d_base_v003_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin_63d_base_v004_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmarginz_252d_base_v005_signal,
    f32cf_f32_cash_flow_cyclicality_marginspread_63d_base_v006_signal,
    f32cf_f32_cash_flow_cyclicality_fcfswing_252d_base_v007_signal,
    f32cf_f32_cash_flow_cyclicality_fcfswing_504d_base_v008_signal,
    f32cf_f32_cash_flow_cyclicality_fcfcyclepos_252d_base_v009_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpeakgap_252d_base_v010_signal,
    f32cf_f32_cash_flow_cyclicality_fcftroughgap_504d_base_v011_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvol_252d_base_v012_signal,
    f32cf_f32_cash_flow_cyclicality_ocfvol_252d_base_v013_signal,
    f32cf_f32_cash_flow_cyclicality_fcfcv_252d_base_v014_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvolterm_base_v015_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsvol_252d_base_v016_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpostime_252d_base_v017_signal,
    f32cf_f32_cash_flow_cyclicality_fcfinflect_252d_base_v018_signal,
    f32cf_f32_cash_flow_cyclicality_fcfbreakeven_63d_base_v019_signal,
    f32cf_f32_cash_flow_cyclicality_fcfsincepos_252d_base_v020_signal,
    f32cf_f32_cash_flow_cyclicality_fcfsignavg_126d_base_v021_signal,
    f32cf_f32_cash_flow_cyclicality_fcfconsist_252d_base_v022_signal,
    f32cf_f32_cash_flow_cyclicality_fcfconv_63d_base_v023_signal,
    f32cf_f32_cash_flow_cyclicality_fcfconvz_252d_base_v024_signal,
    f32cf_f32_cash_flow_cyclicality_fcfchurn_252d_base_v025_signal,
    f32cf_f32_cash_flow_cyclicality_ocftrend_63d_base_v026_signal,
    f32cf_f32_cash_flow_cyclicality_ocfyoy_252d_base_v027_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargintrend_126d_base_v028_signal,
    f32cf_f32_cash_flow_cyclicality_ocfdd_252d_base_v029_signal,
    f32cf_f32_cash_flow_cyclicality_ocfrank_504d_base_v030_signal,
    f32cf_f32_cash_flow_cyclicality_capexcover_63d_base_v031_signal,
    f32cf_f32_cash_flow_cyclicality_capexcoverz_252d_base_v032_signal,
    f32cf_f32_cash_flow_cyclicality_undercoveronset_252d_base_v033_signal,
    f32cf_f32_cash_flow_cyclicality_capexintensity_63d_base_v034_signal,
    f32cf_f32_cash_flow_cyclicality_capexintensz_252d_base_v035_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyieldrank_504d_base_v036_signal,
    f32cf_f32_cash_flow_cyclicality_fcfps_63d_base_v037_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsz_252d_base_v038_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpspos_252d_base_v039_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsyoy_252d_base_v040_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpspostime_252d_base_v041_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginterm_base_v042_signal,
    f32cf_f32_cash_flow_cyclicality_ocfterm_base_v043_signal,
    f32cf_f32_cash_flow_cyclicality_coverterm_base_v044_signal,
    f32cf_f32_cash_flow_cyclicality_fcfdd_252d_base_v045_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmin_126d_base_v046_signal,
    f32cf_f32_cash_flow_cyclicality_fcfdisp_multi_base_v047_signal,
    f32cf_f32_cash_flow_cyclicality_swingXtrough_252d_base_v048_signal,
    f32cf_f32_cash_flow_cyclicality_capexXweak_252d_base_v049_signal,
    f32cf_f32_cash_flow_cyclicality_ocfXrevgrow_126d_base_v050_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmargin_126d_base_v051_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargintilt_252d_base_v052_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmargindisp_63d_base_v053_signal,
    f32cf_f32_cash_flow_cyclicality_capexcoverdisp_63d_base_v054_signal,
    f32cf_f32_cash_flow_cyclicality_critcashtime_252d_base_v055_signal,
    f32cf_f32_cash_flow_cyclicality_fcfaccel_63d_base_v056_signal,
    f32cf_f32_cash_flow_cyclicality_ocfcurv_63d_base_v057_signal,
    f32cf_f32_cash_flow_cyclicality_coveraccel_42d_base_v058_signal,
    f32cf_f32_cash_flow_cyclicality_fcfrevrank_252d_base_v059_signal,
    f32cf_f32_cash_flow_cyclicality_cashrevsync_126d_base_v060_signal,
    f32cf_f32_cash_flow_cyclicality_ocfrisadj_126d_base_v061_signal,
    f32cf_f32_cash_flow_cyclicality_cyccomposite_252d_base_v062_signal,
    f32cf_f32_cash_flow_cyclicality_recovqual_252d_base_v063_signal,
    f32cf_f32_cash_flow_cyclicality_worstcover_252d_base_v064_signal,
    f32cf_f32_cash_flow_cyclicality_dragtrend_126d_base_v065_signal,
    f32cf_f32_cash_flow_cyclicality_convstab_252d_base_v066_signal,
    f32cf_f32_cash_flow_cyclicality_netcashmargin_63d_base_v067_signal,
    f32cf_f32_cash_flow_cyclicality_fcfchgvol_252d_base_v068_signal,
    f32cf_f32_cash_flow_cyclicality_capexrank_504d_base_v069_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsrank_504d_base_v070_signal,
    f32cf_f32_cash_flow_cyclicality_downcycletime_252d_base_v071_signal,
    f32cf_f32_cash_flow_cyclicality_fcfposstreak_base_v072_signal,
    f32cf_f32_cash_flow_cyclicality_fcftanh_63d_base_v073_signal,
    f32cf_f32_cash_flow_cyclicality_capexocfdiverge_63d_base_v074_signal,
    f32cf_f32_cash_flow_cyclicality_cyclephase_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_CASH_FLOW_CYCLICALITY_REGISTRY_001_075 = REGISTRY


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

    # fcf/ncfo/fcfps swing across zero so inflection/sign features vary;
    # revenue/capex stay positive.
    fcf = _fund(3201, base=1.0e8, drift=-0.01, vol=0.24, allow_neg=True).rename("fcf")
    ncfo = _fund(3202, base=1.2e8, drift=0.0, vol=0.20, allow_neg=True).rename("ncfo")
    fcfps = _fund(3203, base=4.0, drift=-0.005, vol=0.26, allow_neg=True).rename("fcfps")
    revenue = _fund(3204, base=3.0e8, drift=0.015, vol=0.07).rename("revenue")
    capex = _fund(3205, base=7.0e7, drift=0.01, vol=0.16).rename("capex")

    cols = {"fcf": fcf, "ncfo": ncfo, "fcfps": fcfps,
            "revenue": revenue, "capex": capex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("fcf", "ncfo", "fcfps", "revenue", "capex")
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

    print("OK f32_cash_flow_cyclicality_base_001_075_claude: %d features pass" % n_features)
