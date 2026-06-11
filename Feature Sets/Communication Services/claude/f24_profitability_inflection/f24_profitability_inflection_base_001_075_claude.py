import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _slope(s, w):
    # OLS slope vs time index over a rolling window (per-step change)
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== f24 profitability-inflection primitives =====
def _f24pi_pos_frac(s, w):
    # fraction of the window where the metric is positive (profit fraction)
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _f24pi_loss_frac(s, w):
    # fraction of the window where the metric is negative (loss-quarter tally proxy)
    neg = (s < 0).astype(float)
    return neg.rolling(w, min_periods=max(1, w // 2)).mean()


def _f24pi_time_since_pos(s, w):
    # normalized distance since last positive print inside the window
    def _f(a):
        pos = np.where(a > 0)[0]
        if pos.size == 0:
            return 1.0
        return (len(a) - 1 - int(pos[-1])) / float(len(a))
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f24pi_time_since_neg(s, w):
    # normalized distance since last negative (loss) print inside the window
    def _f(a):
        neg = np.where(a < 0)[0]
        if neg.size == 0:
            return 1.0
        return (len(a) - 1 - int(neg[-1])) / float(len(a))
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f24pi_cross_up(s):
    # event: metric crosses from <=0 to >0 (return-to-profit)
    return ((s > 0) & (s.shift(1) <= 0)).astype(float)


def _f24pi_cross_down(s):
    # event: metric crosses from >=0 to <0 (slip-to-loss)
    return ((s < 0) & (s.shift(1) >= 0)).astype(float)


def _f24pi_signmag(s):
    # signed sqrt magnitude (compresses large swings, keeps sign of profit/loss)
    return np.sign(s) * np.sqrt(np.abs(s))


def _f24pi_streak_pos(s):
    # running length of consecutive positive prints, reset on non-positive
    pos = (s > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()


def _f24pi_streak_neg(s):
    # running length of consecutive negative (loss) prints
    neg = (s < 0).astype(float)
    grp = (neg == 0).cumsum()
    return neg.groupby(grp).cumsum()


# ============================================================
# --- netinc: path-to-profit core ---

# net-income positive-fraction over the last year (profit prevalence)
def f24pi_f24_profitability_inflection_niposfrac_252d_base_v001_signal(netinc):
    b = _f24pi_pos_frac(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income loss intensity: aggregate loss depth as a share of gross |netinc| over 504d
def f24pi_f24_profitability_inflection_nilossintensity_504d_base_v002_signal(netinc):
    loss = (-netinc).clip(lower=0).rolling(504, min_periods=252).sum()
    gross = netinc.abs().rolling(504, min_periods=252).sum()
    b = loss / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-decayed recency of net profitability (recent profit prints weighted)
def f24pi_f24_profitability_inflection_niprofitrecency_base_v003_signal(netinc):
    pos = (netinc > 0).astype(float)
    b = pos.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durability of current profit run: profit-weighted recency, EW-decayed loss memory
def f24pi_f24_profitability_inflection_nilossmemory_base_v004_signal(netinc):
    neg = (netinc < 0).astype(float)
    # exponentially weighted loss prevalence; high => recent losses still weigh on regime
    b = neg.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing slope: OLS slope of net income over a quarter (toward zero)
def f24pi_f24_profitability_inflection_nislope_63d_base_v005_signal(netinc):
    b = _slope(netinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income loss-narrowing scaled by its own typical magnitude (relative climb)
def f24pi_f24_profitability_inflection_ninarrow_126d_base_v006_signal(netinc):
    sl = _slope(netinc, 126)
    scale = netinc.abs().rolling(126, min_periods=63).mean()
    b = sl / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-to-profit crossing events for net income, depth-weighted by climb above zero
def f24pi_f24_profitability_inflection_nicrossup_252d_base_v007_signal(netinc):
    ev = _f24pi_cross_up(netinc)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = netinc.clip(lower=0)
    relief = (depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slip-to-loss crossing events for net income, depth-weighted by loss below zero
def f24pi_f24_profitability_inflection_nicrossdn_252d_base_v008_signal(netinc):
    ev = _f24pi_cross_down(netinc)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = (-netinc).clip(lower=0)
    pain = (depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = cnt + 0.3 * pain.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-profit-run streak length, augmented with current-print profit depth
def f24pi_f24_profitability_inflection_niposstreak_base_v009_signal(netinc):
    st = _f24pi_streak_pos(netinc)
    depth = netinc.clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-loss-run streak length, augmented with current-print loss depth
def f24pi_f24_profitability_inflection_nilosstreak_base_v010_signal(netinc):
    st = _f24pi_streak_neg(netinc)
    depth = (-netinc).clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt net income, z-scored vs own year (inflection-sensitive level)
def f24pi_f24_profitability_inflection_nisignmagz_252d_base_v011_signal(netinc):
    sm = _f24pi_signmag(netinc)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income vs its 252d level a quarter ago (year-shape profit momentum)
def f24pi_f24_profitability_inflection_nilevelmom_252d_base_v012_signal(netinc):
    sm = _f24pi_signmag(netinc)
    avg = sm.rolling(252, min_periods=126).mean()
    b = avg - avg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit: operating-profit path ---

# ebit positive-fraction over the last year (operating-profit prevalence)
def f24pi_f24_profitability_inflection_ebitposfrac_252d_base_v013_signal(ebit):
    b = _f24pi_pos_frac(ebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit loss intensity: aggregate operating-loss depth vs gross |ebit| over 504d
def f24pi_f24_profitability_inflection_ebitlossintensity_504d_base_v014_signal(ebit):
    loss = (-ebit).clip(lower=0).rolling(504, min_periods=252).sum()
    gross = ebit.abs().rolling(504, min_periods=252).sum()
    b = loss / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-decayed recency of operating profitability (ebit profit prints)
def f24pi_f24_profitability_inflection_ebitprofitrecency_base_v015_signal(ebit):
    pos = (ebit > 0).astype(float)
    b = pos.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit path curvature over a quarter (quadratic-fit acceleration of operating profit)
def f24pi_f24_profitability_inflection_ebitconvex_63d_base_v016_signal(ebit):
    w = 63
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    i2 = idx ** 2
    i2 = i2 - i2.mean()
    denom = (i2 ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(i2, a) / denom)
    curv = ebit.rolling(w, min_periods=w).apply(_f, raw=True)
    scale = ebit.abs().rolling(252, min_periods=126).mean()
    b = curv / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit slope scaled by own magnitude over a half-year (relative operating climb)
def f24pi_f24_profitability_inflection_ebitnarrow_126d_base_v017_signal(ebit):
    sl = _slope(ebit, 126)
    scale = ebit.abs().rolling(126, min_periods=63).mean()
    b = sl / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit return-to-profit crossings over the year, depth-weighted by operating relief
def f24pi_f24_profitability_inflection_ebitcrossup_252d_base_v018_signal(ebit):
    ev = _f24pi_cross_up(ebit)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = ebit.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit profit-run streak length, augmented with current operating-profit depth
def f24pi_f24_profitability_inflection_ebitposstreak_base_v019_signal(ebit):
    st = _f24pi_streak_pos(ebit)
    depth = ebit.clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit loss-run streak length, augmented with current operating-loss depth
def f24pi_f24_profitability_inflection_ebitlosstreak_base_v020_signal(ebit):
    st = _f24pi_streak_neg(ebit)
    depth = (-ebit).clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt ebit z-scored vs own year
def f24pi_f24_profitability_inflection_ebitsignmagz_252d_base_v021_signal(ebit):
    sm = _f24pi_signmag(ebit)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opinc: operating-income path ---

# operating-income positive-fraction over the year
def f24pi_f24_profitability_inflection_opincposfrac_252d_base_v022_signal(opinc):
    b = _f24pi_pos_frac(opinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-income loss-intensity trend: is the loss share narrowing quarter-on-quarter
def f24pi_f24_profitability_inflection_opinclossnarrowtrend_base_v023_signal(opinc):
    loss = (-opinc).clip(lower=0).rolling(126, min_periods=63).sum()
    gross = opinc.abs().rolling(126, min_periods=63).sum()
    inten = loss / gross.replace(0, np.nan)
    b = -(inten - inten.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since opinc last positive
def f24pi_f24_profitability_inflection_opinctsincepos_252d_base_v024_signal(opinc):
    b = _f24pi_time_since_pos(opinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc loss-narrowing slope over a quarter
def f24pi_f24_profitability_inflection_opincslope_63d_base_v025_signal(opinc):
    b = _slope(opinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc slope scaled by magnitude (relative operating-income climb)
def f24pi_f24_profitability_inflection_opincnarrow_126d_base_v026_signal(opinc):
    sl = _slope(opinc, 126)
    scale = opinc.abs().rolling(126, min_periods=63).mean()
    b = sl / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc return-to-profit crossings over the year, depth-weighted by operating relief
def f24pi_f24_profitability_inflection_opinccrossup_252d_base_v027_signal(opinc):
    ev = _f24pi_cross_up(opinc)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = opinc.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc profit-run streak length, augmented with current operating-income depth
def f24pi_f24_profitability_inflection_opincposstreak_base_v028_signal(opinc):
    st = _f24pi_streak_pos(opinc)
    depth = opinc.clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt opinc z-scored vs own year
def f24pi_f24_profitability_inflection_opincsignmagz_252d_base_v029_signal(opinc):
    sm = _f24pi_signmag(opinc)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ncfo: operating-cash-flow path ---

# operating-cash-flow positive-fraction over the year (cash-profit prevalence)
def f24pi_f24_profitability_inflection_ncfoposfrac_252d_base_v030_signal(ncfo):
    b = _f24pi_pos_frac(ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn intensity trend: is the operating cash-burn share narrowing quarter-on-quarter
def f24pi_f24_profitability_inflection_ncfoburnnarrowtrend_base_v031_signal(ncfo):
    burn = (-ncfo).clip(lower=0).rolling(126, min_periods=63).sum()
    gross = ncfo.abs().rolling(126, min_periods=63).sum()
    inten = burn / gross.replace(0, np.nan)
    b = -(inten - inten.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-decayed recency of positive operating cash flow (cash-generation)
def f24pi_f24_profitability_inflection_ncfogenrecency_base_v032_signal(ncfo):
    pos = (ncfo > 0).astype(float)
    b = pos.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo slope over a quarter (cash-burn narrowing)
def f24pi_f24_profitability_inflection_ncfoslope_63d_base_v033_signal(ncfo):
    b = _slope(ncfo, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo slope scaled by magnitude (relative cash-flow climb)
def f24pi_f24_profitability_inflection_ncfonarrow_126d_base_v034_signal(ncfo):
    sl = _slope(ncfo, 126)
    scale = ncfo.abs().rolling(126, min_periods=63).mean()
    b = sl / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo return-to-positive crossings over the year, depth-weighted by cash relief
def f24pi_f24_profitability_inflection_ncfocrossup_252d_base_v035_signal(ncfo):
    ev = _f24pi_cross_up(ncfo)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = ncfo.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo positive-run streak length, augmented with current cash-generation depth
def f24pi_f24_profitability_inflection_ncfoposstreak_base_v036_signal(ncfo):
    st = _f24pi_streak_pos(ncfo)
    depth = ncfo.clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo burn-run streak length, augmented with current cash-burn depth
def f24pi_f24_profitability_inflection_ncfoburnstreak_base_v037_signal(ncfo):
    st = _f24pi_streak_neg(ncfo)
    depth = (-ncfo).clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt ncfo z-scored vs own year
def f24pi_f24_profitability_inflection_ncfosignmagz_252d_base_v038_signal(ncfo):
    sm = _f24pi_signmag(ncfo)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- eps: per-share earnings inflection ---

# eps near-breakeven dwell: fraction of the year eps sits inside a tight band around zero
def f24pi_f24_profitability_inflection_epsdwell_252d_base_v039_signal(eps):
    scale = eps.abs().rolling(252, min_periods=126).median()
    in_band = (eps.abs() < 0.5 * scale.replace(0, np.nan)).astype(float)
    b = in_band.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps loss-recovery clock: bars elapsed since the worst per-share loss of the last year
def f24pi_f24_profitability_inflection_epslossrecovery_252d_base_v040_signal(eps):
    def _f(a):
        i = int(np.argmin(a))
        return (len(a) - 1 - i) / float(len(a))
    elapsed = eps.rolling(252, min_periods=126).apply(_f, raw=True)
    worst = eps.rolling(252, min_periods=126).min()
    depth = (-worst).clip(lower=0)
    relief = elapsed * np.tanh(depth / depth.rolling(504, min_periods=126).mean().replace(0, np.nan))
    b = relief
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since eps last positive
def f24pi_f24_profitability_inflection_epstsincepos_252d_base_v041_signal(eps):
    b = _f24pi_time_since_pos(eps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps inflection slope over a quarter
def f24pi_f24_profitability_inflection_epsslope_63d_base_v042_signal(eps):
    b = _slope(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level autocorrelation: mean-reversion vs trending of per-share earnings (half-year)
def f24pi_f24_profitability_inflection_epslevelac_126d_base_v043_signal(eps):
    sm = _f24pi_signmag(eps)
    lag = sm.shift(1)
    m = sm.rolling(126, min_periods=63).mean()
    cov = ((sm - m) * (lag - m)).rolling(126, min_periods=63).mean()
    var = ((sm - m) ** 2).rolling(126, min_periods=63).mean()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps return-to-profit crossings over the year, depth-weighted by eps relief
def f24pi_f24_profitability_inflection_epscrossup_252d_base_v044_signal(eps):
    ev = _f24pi_cross_up(eps)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = eps.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps slip-to-loss crossings over the year, depth-weighted by eps pain
def f24pi_f24_profitability_inflection_epscrossdn_252d_base_v045_signal(eps):
    ev = _f24pi_cross_down(eps)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = (-eps).clip(lower=0)
    pain = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * pain.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps profit-run streak length, augmented with current per-share profit depth
def f24pi_f24_profitability_inflection_epsposstreak_base_v046_signal(eps):
    st = _f24pi_streak_pos(eps)
    depth = eps.clip(lower=0)
    frac = depth / depth.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = st + 0.4 * np.tanh(frac)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps distribution skew over the year (asymmetry of per-share earnings prints)
def f24pi_f24_profitability_inflection_epsskew_252d_base_v047_signal(eps):
    b = eps.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level momentum: signed-sqrt eps now vs a year ago
def f24pi_f24_profitability_inflection_epsyoy_252d_base_v048_signal(eps):
    sm = _f24pi_signmag(eps)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- retearn: accumulated-deficit trajectory ---

# accumulated-deficit indicator fraction (fraction of year with retearn<0)
def f24pi_f24_profitability_inflection_retdeficitfrac_252d_base_v049_signal(retearn):
    b = _f24pi_loss_frac(retearn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings trajectory slope over a half-year (deficit shrinking/growing)
def f24pi_f24_profitability_inflection_retslope_126d_base_v050_signal(retearn):
    b = _slope(retearn, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated-deficit log-repair: log-growth of the |deficit| gap toward zero
def f24pi_f24_profitability_inflection_retdeficitclose_126d_base_v051_signal(retearn):
    deficit = (-retearn).clip(lower=0)
    gap_now = deficit + 1.0
    gap_then = deficit.shift(126) + 1.0
    b = np.log(gap_then / gap_now)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn deficit-to-surplus crossings, depth-weighted by accumulated surplus
def f24pi_f24_profitability_inflection_retcrossup_504d_base_v052_signal(retearn):
    ev = _f24pi_cross_up(retearn)
    cnt = ev.rolling(504, min_periods=252).sum()
    depth = retearn.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since retearn last positive (accumulated-surplus staleness)
def f24pi_f24_profitability_inflection_rettsincepos_504d_base_v053_signal(retearn):
    b = _f24pi_time_since_pos(retearn, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt retained earnings z-scored vs own year (deficit-depth level)
def f24pi_f24_profitability_inflection_retsignmagz_252d_base_v054_signal(retearn):
    sm = _f24pi_signmag(retearn)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn year-over-year change (accumulated-deficit repair over a year)
def f24pi_f24_profitability_inflection_retyoy_252d_base_v055_signal(retearn):
    sm = _f24pi_signmag(retearn)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-metric inflection composites ---

# net-income minus ncfo positive-fraction spread (accrual vs cash profit-timing)
def f24pi_f24_profitability_inflection_niVncfoposSpr_252d_base_v056_signal(netinc, ncfo):
    a = _f24pi_pos_frac(netinc, 252)
    c = _f24pi_pos_frac(ncfo, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-minus-netinc loss-fraction spread (below-the-line drag on profitability)
def f24pi_f24_profitability_inflection_ebitVniLossSpr_252d_base_v057_signal(ebit, netinc):
    a = _f24pi_loss_frac(ebit, 252)
    c = _f24pi_loss_frac(netinc, 252)
    b = c - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-vs-ebit positive-fraction spread (non-operating contribution to profit)
def f24pi_f24_profitability_inflection_opincVebitPos_252d_base_v058_signal(opinc, ebit):
    a = _f24pi_pos_frac(opinc, 252)
    c = _f24pi_pos_frac(ebit, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth of profitability: how many of ni/ebit/opinc/ncfo are positive (smoothed)
def f24pi_f24_profitability_inflection_profitbreadth_base_v059_signal(netinc, ebit, opinc, ncfo):
    breadth = ((netinc > 0).astype(float) + (ebit > 0).astype(float)
               + (opinc > 0).astype(float) + (ncfo > 0).astype(float))
    b = breadth.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profitability-breadth momentum: change over a quarter in the breadth count
def f24pi_f24_profitability_inflection_breadthmom_63d_base_v060_signal(netinc, ebit, opinc, ncfo):
    breadth = ((netinc > 0).astype(float) + (ebit > 0).astype(float)
               + (opinc > 0).astype(float) + (ncfo > 0).astype(float))
    sm = breadth.rolling(21, min_periods=10).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps-vs-netinc sign agreement (per-share inflection consistency)
def f24pi_f24_profitability_inflection_epsniagree_252d_base_v061_signal(eps, netinc):
    agree = (np.sign(eps) == np.sign(netinc)).astype(float)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined cross-up density across ni/ebit/ncfo, blended with profit-breadth depth
def f24pi_f24_profitability_inflection_multicrossup_252d_base_v062_signal(netinc, ebit, ncfo):
    ev = _f24pi_cross_up(netinc) + _f24pi_cross_up(ebit) + _f24pi_cross_up(ncfo)
    cnt = ev.rolling(252, min_periods=126).sum()
    breadth = ((netinc > 0).astype(float) + (ebit > 0).astype(float)
               + (ncfo > 0).astype(float))
    b = cnt + 0.2 * breadth.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income relative to accumulated deficit (current profit vs legacy losses)
def f24pi_f24_profitability_inflection_niVretscale_base_v063_signal(netinc, retearn):
    denom = retearn.abs().rolling(252, min_periods=126).mean()
    b = netinc / denom.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo-vs-opinc cash-conversion sign-spread (cash backing of operating profit)
def f24pi_f24_profitability_inflection_ncfoVopincPos_252d_base_v064_signal(ncfo, opinc):
    a = _f24pi_pos_frac(ncfo, 252)
    c = _f24pi_pos_frac(opinc, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- magnitude/dispersion facets ---

# net-income dispersion (how volatile the profit print is) over a year
def f24pi_f24_profitability_inflection_nidisp_252d_base_v065_signal(netinc):
    sm = _f24pi_signmag(netinc)
    sd = _std(sm, 252)
    scale = sm.abs().rolling(252, min_periods=126).mean()
    b = sd / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit dispersion over a year (operating-profit instability)
def f24pi_f24_profitability_inflection_ebitdisp_252d_base_v066_signal(ebit):
    sm = _f24pi_signmag(ebit)
    sd = _std(sm, 252)
    scale = sm.abs().rolling(252, min_periods=126).mean()
    b = sd / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps near-zero proximity: how close eps sits to breakeven (inflection zone)
def f24pi_f24_profitability_inflection_epsbreakeven_252d_base_v067_signal(eps):
    scale = eps.abs().rolling(252, min_periods=126).mean()
    b = -(eps.abs() / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc near-breakeven proximity (distance to zero in own-scale units, inverted)
def f24pi_f24_profitability_inflection_nibreakeven_252d_base_v068_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).mean()
    b = 1.0 - (netinc.abs() / scale.replace(0, np.nan)).clip(upper=3.0) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo magnitude-weighted profitability tilt: net positive cash vs gross cash flow
def f24pi_f24_profitability_inflection_ncfomagtilt_252d_base_v069_signal(ncfo):
    pos = ncfo.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = ncfo.abs().rolling(252, min_periods=126).sum()
    b = pos / gross.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc magnitude-weighted profitability tilt: net operating profit vs gross flow
def f24pi_f24_profitability_inflection_opincmagtilt_252d_base_v070_signal(opinc):
    pos = opinc.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = opinc.abs().rolling(252, min_periods=126).sum()
    b = pos / gross.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn second-difference: is deficit-repair accelerating (curvature of trajectory)
def f24pi_f24_profitability_inflection_retcurv_252d_base_v071_signal(retearn):
    sm = _f24pi_signmag(retearn)
    d = sm.diff(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income inflection asymmetry: positive-run minus loss-run streak, depth-tilted
def f24pi_f24_profitability_inflection_nistreakasym_base_v072_signal(netinc):
    asym = _f24pi_streak_pos(netinc) - _f24pi_streak_neg(netinc)
    sm = _f24pi_signmag(netinc)
    tilt = sm / sm.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = asym + 0.4 * np.tanh(tilt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit time-since-positive minus time-since-negative (operating regime memory)
def f24pi_f24_profitability_inflection_ebittsasym_252d_base_v073_signal(ebit):
    a = _f24pi_time_since_pos(ebit, 252)
    c = _f24pi_time_since_neg(ebit, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps positive-fraction trend (is the profit-print rate itself improving)
def f24pi_f24_profitability_inflection_epsposfractrend_252d_base_v074_signal(eps):
    pf = _f24pi_pos_frac(eps, 126)
    b = pf - pf.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income loss-magnitude narrowing: avg loss depth shrinking over a year
def f24pi_f24_profitability_inflection_nilossmagnarrow_252d_base_v075_signal(netinc):
    loss_depth = (-netinc).clip(lower=0)
    sm = np.sqrt(loss_depth)
    avg = sm.rolling(126, min_periods=63).mean()
    b = -(avg - avg.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24pi_f24_profitability_inflection_niposfrac_252d_base_v001_signal,
    f24pi_f24_profitability_inflection_nilossintensity_504d_base_v002_signal,
    f24pi_f24_profitability_inflection_niprofitrecency_base_v003_signal,
    f24pi_f24_profitability_inflection_nilossmemory_base_v004_signal,
    f24pi_f24_profitability_inflection_nislope_63d_base_v005_signal,
    f24pi_f24_profitability_inflection_ninarrow_126d_base_v006_signal,
    f24pi_f24_profitability_inflection_nicrossup_252d_base_v007_signal,
    f24pi_f24_profitability_inflection_nicrossdn_252d_base_v008_signal,
    f24pi_f24_profitability_inflection_niposstreak_base_v009_signal,
    f24pi_f24_profitability_inflection_nilosstreak_base_v010_signal,
    f24pi_f24_profitability_inflection_nisignmagz_252d_base_v011_signal,
    f24pi_f24_profitability_inflection_nilevelmom_252d_base_v012_signal,
    f24pi_f24_profitability_inflection_ebitposfrac_252d_base_v013_signal,
    f24pi_f24_profitability_inflection_ebitlossintensity_504d_base_v014_signal,
    f24pi_f24_profitability_inflection_ebitprofitrecency_base_v015_signal,
    f24pi_f24_profitability_inflection_ebitconvex_63d_base_v016_signal,
    f24pi_f24_profitability_inflection_ebitnarrow_126d_base_v017_signal,
    f24pi_f24_profitability_inflection_ebitcrossup_252d_base_v018_signal,
    f24pi_f24_profitability_inflection_ebitposstreak_base_v019_signal,
    f24pi_f24_profitability_inflection_ebitlosstreak_base_v020_signal,
    f24pi_f24_profitability_inflection_ebitsignmagz_252d_base_v021_signal,
    f24pi_f24_profitability_inflection_opincposfrac_252d_base_v022_signal,
    f24pi_f24_profitability_inflection_opinclossnarrowtrend_base_v023_signal,
    f24pi_f24_profitability_inflection_opinctsincepos_252d_base_v024_signal,
    f24pi_f24_profitability_inflection_opincslope_63d_base_v025_signal,
    f24pi_f24_profitability_inflection_opincnarrow_126d_base_v026_signal,
    f24pi_f24_profitability_inflection_opinccrossup_252d_base_v027_signal,
    f24pi_f24_profitability_inflection_opincposstreak_base_v028_signal,
    f24pi_f24_profitability_inflection_opincsignmagz_252d_base_v029_signal,
    f24pi_f24_profitability_inflection_ncfoposfrac_252d_base_v030_signal,
    f24pi_f24_profitability_inflection_ncfoburnnarrowtrend_base_v031_signal,
    f24pi_f24_profitability_inflection_ncfogenrecency_base_v032_signal,
    f24pi_f24_profitability_inflection_ncfoslope_63d_base_v033_signal,
    f24pi_f24_profitability_inflection_ncfonarrow_126d_base_v034_signal,
    f24pi_f24_profitability_inflection_ncfocrossup_252d_base_v035_signal,
    f24pi_f24_profitability_inflection_ncfoposstreak_base_v036_signal,
    f24pi_f24_profitability_inflection_ncfoburnstreak_base_v037_signal,
    f24pi_f24_profitability_inflection_ncfosignmagz_252d_base_v038_signal,
    f24pi_f24_profitability_inflection_epsdwell_252d_base_v039_signal,
    f24pi_f24_profitability_inflection_epslossrecovery_252d_base_v040_signal,
    f24pi_f24_profitability_inflection_epstsincepos_252d_base_v041_signal,
    f24pi_f24_profitability_inflection_epsslope_63d_base_v042_signal,
    f24pi_f24_profitability_inflection_epslevelac_126d_base_v043_signal,
    f24pi_f24_profitability_inflection_epscrossup_252d_base_v044_signal,
    f24pi_f24_profitability_inflection_epscrossdn_252d_base_v045_signal,
    f24pi_f24_profitability_inflection_epsposstreak_base_v046_signal,
    f24pi_f24_profitability_inflection_epsskew_252d_base_v047_signal,
    f24pi_f24_profitability_inflection_epsyoy_252d_base_v048_signal,
    f24pi_f24_profitability_inflection_retdeficitfrac_252d_base_v049_signal,
    f24pi_f24_profitability_inflection_retslope_126d_base_v050_signal,
    f24pi_f24_profitability_inflection_retdeficitclose_126d_base_v051_signal,
    f24pi_f24_profitability_inflection_retcrossup_504d_base_v052_signal,
    f24pi_f24_profitability_inflection_rettsincepos_504d_base_v053_signal,
    f24pi_f24_profitability_inflection_retsignmagz_252d_base_v054_signal,
    f24pi_f24_profitability_inflection_retyoy_252d_base_v055_signal,
    f24pi_f24_profitability_inflection_niVncfoposSpr_252d_base_v056_signal,
    f24pi_f24_profitability_inflection_ebitVniLossSpr_252d_base_v057_signal,
    f24pi_f24_profitability_inflection_opincVebitPos_252d_base_v058_signal,
    f24pi_f24_profitability_inflection_profitbreadth_base_v059_signal,
    f24pi_f24_profitability_inflection_breadthmom_63d_base_v060_signal,
    f24pi_f24_profitability_inflection_epsniagree_252d_base_v061_signal,
    f24pi_f24_profitability_inflection_multicrossup_252d_base_v062_signal,
    f24pi_f24_profitability_inflection_niVretscale_base_v063_signal,
    f24pi_f24_profitability_inflection_ncfoVopincPos_252d_base_v064_signal,
    f24pi_f24_profitability_inflection_nidisp_252d_base_v065_signal,
    f24pi_f24_profitability_inflection_ebitdisp_252d_base_v066_signal,
    f24pi_f24_profitability_inflection_epsbreakeven_252d_base_v067_signal,
    f24pi_f24_profitability_inflection_nibreakeven_252d_base_v068_signal,
    f24pi_f24_profitability_inflection_ncfomagtilt_252d_base_v069_signal,
    f24pi_f24_profitability_inflection_opincmagtilt_252d_base_v070_signal,
    f24pi_f24_profitability_inflection_retcurv_252d_base_v071_signal,
    f24pi_f24_profitability_inflection_nistreakasym_base_v072_signal,
    f24pi_f24_profitability_inflection_ebittsasym_252d_base_v073_signal,
    f24pi_f24_profitability_inflection_epsposfractrend_252d_base_v074_signal,
    f24pi_f24_profitability_inflection_nilossmagnarrow_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_PROFITABILITY_INFLECTION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _swing(seed, base, amp, per, allow_neg=True):
        # _fund trend that genuinely oscillates across zero so inflection / loss /
        # cross / streak / pos-fraction features vary over the panel.
        core = _fund(seed, base=base, drift=0.0, vol=0.10, allow_neg=allow_neg)
        g = np.random.default_rng(seed + 7000)
        t = np.arange(n, dtype=float)
        osc = np.sin(2.0 * np.pi * t / per + g.uniform(0, 6.28))
        noise = g.normal(0.0, 0.35, n)
        return pd.Series(core.values - base * 0.6 + amp * base * (osc + noise))

    # build fundamentals that swing across zero so inflection/loss-count vary
    netinc = _swing(101, base=8e7, amp=0.9, per=180).rename("netinc")
    ebit = _swing(102, base=9e7, amp=0.85, per=150).rename("ebit")
    opinc = _swing(103, base=9e7, amp=0.8, per=210).rename("opinc")
    ncfo = _swing(104, base=7e7, amp=1.0, per=130).rename("ncfo")
    eps = _swing(105, base=1.5, amp=0.95, per=160).rename("eps")
    retearn = _swing(106, base=2e8, amp=0.7, per=320).rename("retearn")

    cols = {"netinc": netinc, "ebit": ebit, "opinc": opinc, "ncfo": ncfo,
            "eps": eps, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f24_profitability_inflection_base_001_075_claude: %d features pass" % n_features)
