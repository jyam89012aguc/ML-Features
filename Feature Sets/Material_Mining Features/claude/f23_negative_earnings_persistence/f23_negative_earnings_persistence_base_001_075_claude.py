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


# ===== folder domain primitives (negative earnings persistence) =====
# Pre-revenue explorers: netinc/ncfo/eps/ebit/retearn swing across zero.
# These quantify loss persistence, loss-quarter tallies, burn-quarter counts,
# loss-narrowing/widening, time-since-profitable, accumulated-deficit growth.
def _f23_isloss(s):
    # 1.0 when the earnings flow is negative (a loss), else 0.0
    return (s < 0.0).astype(float)


def _f23_losscount(s, w):
    # fraction of the trailing window spent in loss (loss persistence)
    return _f23_isloss(s).rolling(w, min_periods=max(1, w // 2)).mean()


def _f23_losssum(s, w):
    # count of loss days in the trailing window (count-friendly tally)
    return _f23_isloss(s).rolling(w, min_periods=max(1, w // 2)).sum()


def _f23_lossdepth(s, scale):
    # magnitude of loss only (0 when profitable), scaled to ~O(1)
    return (-s).clip(lower=0.0) / float(scale)


def _f23_profitdepth(s, scale):
    # magnitude of profit only (0 when losing)
    return s.clip(lower=0.0) / float(scale)


def _f23_streak_loss(s):
    # consecutive-day loss streak length (resets to 0 on any profit)
    loss = _f23_isloss(s)
    grp = (loss == 0).cumsum()
    return loss.groupby(grp).cumsum()


def _f23_streak_profit(s):
    # consecutive-day profit streak length (resets to 0 on any loss)
    prof = (s > 0.0).astype(float)
    grp = (prof == 0).cumsum()
    return prof.groupby(grp).cumsum()


def _f23_time_since_profit(s):
    # days since the last profitable observation (time-since-profitable)
    prof = (s > 0.0)
    idx = np.arange(len(s), dtype=float)
    last = pd.Series(np.where(prof.values, idx, np.nan), index=s.index).ffill()
    out = pd.Series(idx, index=s.index) - last
    return out


def _f23_deficit_growth(retearn, w):
    # growth of accumulated deficit: how much retained earnings sank over w
    return (retearn.shift(w) - retearn) / float(w)


# ============================================================
# --- LOSS PERSISTENCE / COUNTS (netinc) ---
# fraction of trailing year net income was negative (loss persistence)
def f23ne_f23_negative_earnings_persistence_lossfrac_252d_base_v001_signal(netinc):
    b = _f23_losscount(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of net-loss days over the trailing 504d (loss-quarter tally proxy)
def f23ne_f23_negative_earnings_persistence_losscnt_504d_base_v002_signal(netinc):
    b = _f23_losssum(netinc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive net-loss streak length (uninterrupted loss persistence)
def f23ne_f23_negative_earnings_persistence_lossstreak_base_v003_signal(netinc):
    b = _f23_streak_loss(netinc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss persistence over a quarter, z-scored vs its own year history
def f23ne_f23_negative_earnings_persistence_lossfracz_63d_base_v004_signal(netinc):
    lf = _f23_losscount(netinc, 63)
    b = _z(lf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long loss persistence ratio (worsening loss regime, multiplicative)
def f23ne_f23_negative_earnings_persistence_lossfracspr_base_v005_signal(netinc):
    s = _f23_losscount(netinc, 42)
    l = _f23_losscount(netinc, 252)
    b = (s + 0.05) / (l + 0.05) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-BURN QUARTER TALLY (ncfo) ---
# fraction of trailing year operating cash flow was negative (cash-burn quarters)
def f23ne_f23_negative_earnings_persistence_burnfrac_252d_base_v006_signal(ncfo):
    b = _f23_losscount(ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of cash-burn days over the trailing 504d (burn-quarter tally)
def f23ne_f23_negative_earnings_persistence_burncnt_504d_base_v007_signal(ncfo):
    b = _f23_losssum(ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive cash-burn streak length (sustained operating cash drain)
def f23ne_f23_negative_earnings_persistence_burnstreak_base_v008_signal(ncfo):
    b = _f23_streak_loss(ncfo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn persistence over a half-year, z-scored vs its 504d history
def f23ne_f23_negative_earnings_persistence_burnfracz_126d_base_v009_signal(ncfo):
    bf = _f23_losscount(ncfo, 126)
    b = _z(bf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS LOSS PERSISTENCE ---
# fraction of trailing year EPS was negative (per-share loss persistence)
def f23ne_f23_negative_earnings_persistence_epslossfrac_252d_base_v010_signal(eps):
    b = _f23_losscount(eps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive negative-EPS streak length
def f23ne_f23_negative_earnings_persistence_epslossstreak_base_v011_signal(eps):
    b = _f23_streak_loss(eps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of negative-EPS days over the trailing 1260d (multi-year loss tally)
def f23ne_f23_negative_earnings_persistence_epslosscnt_1260d_base_v012_signal(eps):
    b = _f23_losssum(eps, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBIT LOSS PERSISTENCE ---
# fraction of trailing year operating earnings (EBIT) were negative
def f23ne_f23_negative_earnings_persistence_ebitlossfrac_252d_base_v013_signal(ebit):
    b = _f23_losscount(ebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive negative-EBIT streak (operating-loss persistence)
def f23ne_f23_negative_earnings_persistence_ebitlossstreak_base_v014_signal(ebit):
    b = _f23_streak_loss(ebit)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT loss persistence over a quarter minus over two years (acute vs chronic)
def f23ne_f23_negative_earnings_persistence_ebitlossspr_base_v015_signal(ebit):
    s = _f23_losscount(ebit, 63)
    l = _f23_losscount(ebit, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TIME-SINCE-PROFITABLE ---
# days since net income was last positive (time-since-profitable), log-compressed
def f23ne_f23_negative_earnings_persistence_tsprofit_ni_base_v016_signal(netinc):
    t = _f23_time_since_profit(netinc)
    b = np.log1p(t.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since EBIT was last positive (time-since-operating-profit)
def f23ne_f23_negative_earnings_persistence_tsprofit_ebit_base_v017_signal(ebit):
    t = _f23_time_since_profit(ebit)
    b = np.log1p(t.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since operating cash flow was last positive (time-since-cash-positive)
def f23ne_f23_negative_earnings_persistence_tsprofit_ncfo_base_v018_signal(ncfo):
    t = _f23_time_since_profit(ncfo)
    b = np.log1p(t.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share dry spell: days-since-positive-EPS as a fraction of the trailing year window
def f23ne_f23_negative_earnings_persistence_tsprofit_eps_base_v019_signal(eps):
    t = _f23_time_since_profit(eps)
    frac = (t / 252.0).clip(upper=1.0)
    b = frac.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ACCUMULATED-DEFICIT GROWTH (retearn) ---
# accumulated-deficit growth: rate retained earnings sank over the trailing year
def f23ne_f23_negative_earnings_persistence_deficitgr_252d_base_v020_signal(retearn):
    raw = _f23_deficit_growth(retearn, 252)
    b = np.tanh(raw / 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit depth: how negative retained earnings is relative to its own scale
def f23ne_f23_negative_earnings_persistence_deficitdepth_base_v021_signal(retearn):
    neg = (-retearn).clip(lower=0.0)
    b = np.log1p(neg / 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trailing 504d retained earnings was negative (deficit regime)
def f23ne_f23_negative_earnings_persistence_deficitfrac_504d_base_v022_signal(retearn):
    b = _f23_losscount(retearn, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings drawdown from its trailing-2y peak (deficit deepening)
def f23ne_f23_negative_earnings_persistence_retdrawdown_504d_base_v023_signal(retearn):
    peak = _rmax(retearn, 504)
    b = (retearn - peak) / (peak.abs() + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS NARROWING / WIDENING SLOPE ---
# net-income trend over a year scaled by typical magnitude (loss narrowing/widening)
def f23ne_f23_negative_earnings_persistence_nitrend_252d_base_v024_signal(netinc):
    sl = _slope(netinc, 252)
    typ = netinc.abs().rolling(252, min_periods=126).mean()
    b = sl / (typ + 1e6) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss-depth trend: is the net loss getting deeper or shallower (252d slope)
def f23ne_f23_negative_earnings_persistence_lossdepthtr_252d_base_v025_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7)
    b = _slope(d, 252) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT loss-depth trend over a half-year (operating-loss widening/narrowing)
def f23ne_f23_negative_earnings_persistence_ebitlossdepthtr_126d_base_v026_signal(ebit):
    d = _f23_lossdepth(ebit, 1e7)
    b = _slope(d, 126) * 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS direction: change in EPS over a year normalized by its dispersion
def f23ne_f23_negative_earnings_persistence_epstrend_252d_base_v027_signal(eps):
    sl = eps - eps.shift(252)
    disp = eps.rolling(252, min_periods=126).std()
    b = sl / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS DEPTH LEVELS ---
# net loss depth (magnitude of loss only), log-compressed level
def f23ne_f23_negative_earnings_persistence_nilossdepth_base_v028_signal(netinc):
    d = _f23_lossdepth(netinc, 1.0)
    b = np.log1p(d / 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT loss depth averaged over the trailing quarter (sustained operating-loss size)
def f23ne_f23_negative_earnings_persistence_ebitlossdepth_63d_base_v029_signal(ebit):
    d = _f23_lossdepth(ebit, 1e7)
    b = d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn depth (magnitude of negative operating cash flow), trailing-year mean
def f23ne_f23_negative_earnings_persistence_burndepth_252d_base_v030_signal(ncfo):
    d = _f23_lossdepth(ncfo, 1e7)
    b = d.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE (signed loss intensity) ---
# signed-magnitude net income (sign x sqrt-magnitude), de-trended vs 252d
def f23ne_f23_negative_earnings_persistence_nisignmag_base_v031_signal(netinc):
    sm = np.sign(netinc) * np.sqrt(netinc.abs() / 1e6)
    b = sm - sm.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-magnitude EBIT z-scored vs its own year history (operating-sign extremity)
def f23ne_f23_negative_earnings_persistence_ebitsignmag_base_v032_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(ebit.abs() / 1e6)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS / PROFIT BALANCE (count asymmetry) ---
# loss tilt change over a quarter: is the depth-weighted loss balance worsening
def f23ne_f23_negative_earnings_persistence_lossbalance_252d_base_v033_signal(netinc):
    lossw = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    profw = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    bal = (lossw - profw) / (lossw + profw + 1e6)
    b = _z(bal, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn vs cash-generation magnitude balance over two years, z-scored (ncfo tilt regime)
def f23ne_f23_negative_earnings_persistence_burnbalance_504d_base_v034_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0).rolling(504, min_periods=252).sum()
    gen = ncfo.clip(lower=0.0).rolling(504, min_periods=252).sum()
    bal = (burn - gen) / (burn + gen + 1e6)
    b = _z(bal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PROFIT STREAK (recovery side) ---
# consecutive profitable net-income streak length (durability of recovery)
def f23ne_f23_negative_earnings_persistence_profstreak_ni_base_v035_signal(netinc):
    b = _f23_streak_profit(netinc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest loss streak within the trailing year, depth-weighted (worst loss episode)
def f23ne_f23_negative_earnings_persistence_maxlossstreak_252d_base_v036_signal(netinc):
    streak = _f23_streak_loss(netinc)
    longest = streak.rolling(252, min_periods=126).max()
    depth = _f23_lossdepth(netinc, 1e7).rolling(126, min_periods=63).mean()
    b = longest + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-QUARTER TRANSITIONS (count of entries into loss) ---
# count of fresh dips into net loss over the year, depth-weighted (loss-episode load)
def f23ne_f23_negative_earnings_persistence_lossentries_252d_base_v037_signal(netinc):
    loss = _f23_isloss(netinc)
    entries = ((loss == 1) & (loss.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = _f23_lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    b = cnt + 3.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recoveries out of cash-burn over two years, tilted by burn-persistence (burn-exit load)
def f23ne_f23_negative_earnings_persistence_burnexits_504d_base_v038_signal(ncfo):
    burn = _f23_isloss(ncfo)
    exits = ((burn == 0) & (burn.shift(1) == 1)).astype(float)
    cnt = exits.rolling(504, min_periods=252).sum()
    persist = _f23_losscount(ncfo, 126)
    b = cnt - 5.0 * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-METRIC LOSS AGREEMENT ---
# how many of {netinc, ncfo, ebit} are negative, smoothed over a quarter (distress breadth)
def f23ne_f23_negative_earnings_persistence_lossbreadth_base_v039_signal(netinc, ncfo, ebit):
    raw = _f23_isloss(netinc) + _f23_isloss(ncfo) + _f23_isloss(ebit)
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence of all-three-negative regime over the trailing year (deep-distress time)
def f23ne_f23_negative_earnings_persistence_triplelossfrac_252d_base_v040_signal(netinc, ncfo, ebit):
    triple = ((netinc < 0) & (ncfo < 0) & (ebit < 0)).astype(float)
    b = triple.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: EBIT in loss but operating cash flow positive (accrual-loss only)
def f23ne_f23_negative_earnings_persistence_ebitvncfo_252d_base_v041_signal(ebit, ncfo):
    div = ((ebit < 0) & (ncfo > 0)).astype(float)
    b = div.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS DEPTH RELATIVE TO RETAINED EARNINGS ---
# annual net loss relative to accumulated deficit (deficit replenishment burden)
def f23ne_f23_negative_earnings_persistence_lossvsdeficit_base_v042_signal(netinc, retearn):
    lossann = _f23_lossdepth(netinc, 1.0).rolling(252, min_periods=126).mean()
    b = lossann / (retearn.abs() + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash burn relative to accumulated deficit base (burn-to-deficit ratio)
def f23ne_f23_negative_earnings_persistence_burnvsdeficit_base_v043_signal(ncfo, retearn):
    burn = _f23_lossdepth(ncfo, 1.0).rolling(126, min_periods=63).mean()
    b = burn / (retearn.abs() + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS PERSISTENCE RANK ---
# loss persistence (252d) percentile-ranked vs its own 504d history
def f23ne_f23_negative_earnings_persistence_lossfracrank_base_v044_signal(netinc):
    lf = _f23_losscount(netinc, 252)
    b = _rank(lf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-depth (not just frequency) percentile-ranked vs its own 504d history
def f23ne_f23_negative_earnings_persistence_burnfracrank_base_v045_signal(ncfo):
    bd = _f23_lossdepth(ncfo, 1e7).rolling(126, min_periods=63).mean()
    b = _rank(bd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS VOLATILITY (swing amplitude across zero) ---
# net-income dispersion over the year scaled by level (loss/profit swing amplitude)
def f23ne_f23_negative_earnings_persistence_niswing_252d_base_v046_signal(netinc):
    sd = netinc.rolling(252, min_periods=126).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    b = sd / (lvl + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT swing amplitude across zero over two years (operating-loss volatility)
def f23ne_f23_negative_earnings_persistence_ebitswing_504d_base_v047_signal(ebit):
    sd = ebit.rolling(504, min_periods=252).std()
    lvl = ebit.abs().rolling(504, min_periods=252).mean()
    b = sd / (lvl + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TIME-SINCE-PROFITABLE INTERACTIONS ---
# time-since-profit (netinc) weighted by current loss depth (deep & chronic loss)
def f23ne_f23_negative_earnings_persistence_chronicloss_base_v048_signal(netinc):
    t = _f23_time_since_profit(netinc) / 252.0
    d = _f23_lossdepth(netinc, 1e7)
    b = t * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-since-cash-positive (ncfo) weighted by burn depth (deep & chronic burn)
def f23ne_f23_negative_earnings_persistence_chronicburn_base_v049_signal(ncfo):
    t = _f23_time_since_profit(ncfo) / 252.0
    d = _f23_lossdepth(ncfo, 1e7)
    b = t * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ACCUMULATED-DEFICIT TRAJECTORY ---
# retained-earnings velocity over a half-year, signed-magnitude compressed
def f23ne_f23_negative_earnings_persistence_retvel_126d_base_v050_signal(retearn):
    sl = _slope(retearn, 126)
    b = np.sign(sl) * np.log1p(sl.abs() / 1e5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings z-score vs its own two-year history (deficit position)
def f23ne_f23_negative_earnings_persistence_retz_504d_base_v051_signal(retearn):
    b = _z(retearn, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# years-of-deficit: accumulated deficit relative to recent annual loss run-rate
def f23ne_f23_negative_earnings_persistence_deficitvsrun_base_v052_signal(retearn, netinc):
    deficit = (-retearn).clip(lower=0.0)
    runrate = _f23_lossdepth(netinc, 1.0).rolling(252, min_periods=126).mean() * 252.0
    b = np.log1p(deficit / (runrate + 1e6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS PERSISTENCE ACROSS WINDOWS (term structure) ---
# loss-persistence term structure: 63d minus 1260d (acute vs chronic, netinc)
def f23ne_f23_negative_earnings_persistence_lossterm_base_v053_signal(netinc):
    s = _f23_losscount(netinc, 63)
    l = _f23_losscount(netinc, 1260)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-persistence term structure: 21d minus 252d (acute vs chronic, ncfo)
def f23ne_f23_negative_earnings_persistence_burnterm_base_v054_signal(ncfo):
    s = _f23_losscount(ncfo, 21)
    l = _f23_losscount(ncfo, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS-SPECIFIC DEPTH ---
# EPS loss depth (negative EPS magnitude) averaged over a quarter
def f23ne_f23_negative_earnings_persistence_epslossdepth_63d_base_v055_signal(eps):
    d = (-eps).clip(lower=0.0)
    b = d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS signed-magnitude de-trended (per-share loss intensity swing)
def f23ne_f23_negative_earnings_persistence_epssignmag_base_v056_signal(eps):
    sm = np.sign(eps) * np.sqrt(eps.abs())
    b = sm - sm.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTERACTION: LOSS PERSISTENCE x DEFICIT GROWTH ---
# loss persistence (netinc) gated by whether the deficit is actively growing (regime AND)
def f23ne_f23_negative_earnings_persistence_persistxdeficit_base_v057_signal(netinc, retearn):
    lf = _f23_losscount(netinc, 252)
    growing = (retearn < retearn.shift(126)).astype(float)
    gate = growing.rolling(63, min_periods=21).mean()
    b = lf * gate - 0.5 * (1.0 - gate)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN-QUARTER TALLY (multi-window) ---
# burn concentration: share of the year's total burn falling in its worst quarter
def f23ne_f23_negative_earnings_persistence_burnqtrtally_base_v058_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0)
    yr = burn.rolling(252, min_periods=126).sum()
    worstq = burn.rolling(63, min_periods=21).sum().rolling(252, min_periods=126).max()
    b = worstq / (yr + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-loss-quarter tally weighted by how deep the worst loss ran (severity-scaled count)
def f23ne_f23_negative_earnings_persistence_lossqtrtally_base_v059_signal(netinc):
    cnt = _f23_losssum(netinc, 504) / 63.0
    worst = (-netinc).clip(lower=0.0).rolling(504, min_periods=252).max()
    b = cnt * np.log1p(worst / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBIT-NCFO BURN GAP ---
# operating-loss vs cash-burn gap (EBIT loss not matched by cash burn)
def f23ne_f23_negative_earnings_persistence_ebitncfogap_base_v060_signal(ebit, ncfo):
    eloss = _f23_lossdepth(ebit, 1e7)
    bloss = _f23_lossdepth(ncfo, 1e7)
    b = (eloss - bloss).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-NARROWING MOMENTUM ---
# is the loss narrowing? change in loss persistence over a quarter (netinc)
def f23ne_f23_negative_earnings_persistence_lossnarrow_base_v061_signal(netinc):
    lf = _f23_losscount(netinc, 252)
    b = -(lf - lf.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss-depth narrowing: change in net loss depth over a quarter (improving)
def f23ne_f23_negative_earnings_persistence_depthnarrow_base_v062_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    b = -(d - d.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RETAINED-EARNINGS DEFICIT FRACTION RANK ---
# deficit-regime persistence (504d) ranked vs 1260d history
def f23ne_f23_negative_earnings_persistence_deficitfracrank_base_v063_signal(retearn):
    df = _f23_losscount(retearn, 504)
    b = _rank(df, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PROFITABILITY ATTEMPTS (sign flips) ---
# profit<->loss sign flips in netinc over the year, swing-weighted (earnings instability)
def f23ne_f23_negative_earnings_persistence_niflips_252d_base_v064_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    sd = netinc.rolling(63, min_periods=21).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    b = cnt + 30.0 * sd / (lvl + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn sign flips in ncfo over two years, burn-depth-weighted (cash-flow instability)
def f23ne_f23_negative_earnings_persistence_ncfoflips_504d_base_v065_signal(ncfo):
    flip = (np.sign(ncfo) != np.sign(ncfo.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    depth = _f23_lossdepth(ncfo, 1e7).rolling(126, min_periods=63).mean()
    b = cnt + 10.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEEPEST LOSS WITHIN WINDOW ---
# deepest single net loss within the trailing year (worst-loss magnitude)
def f23ne_f23_negative_earnings_persistence_worstloss_252d_base_v066_signal(netinc):
    worst = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).max()
    b = np.log1p(worst / 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deepest EBIT operating loss within two years, ranked vs history
def f23ne_f23_negative_earnings_persistence_worstebit_504d_base_v067_signal(ebit):
    worst = (-ebit).clip(lower=0.0).rolling(504, min_periods=252).max()
    b = _rank(worst, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS PERSISTENCE x SWING ---
# earnings swing amplitude conditioned on recent loss-depth direction (volatile distress)
def f23ne_f23_negative_earnings_persistence_persistxswing_base_v068_signal(netinc):
    sd = netinc.rolling(126, min_periods=63).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    swing = sd / (lvl + 1e6)
    depthdir = np.sign(_slope(_f23_lossdepth(netinc, 1e7), 63))
    b = swing * depthdir
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CUMULATIVE LOSS LOAD ---
# cumulative net loss accrued over the trailing year (total cash destroyed)
def f23ne_f23_negative_earnings_persistence_cumloss_252d_base_v069_signal(netinc):
    loss = (-netinc).clip(lower=0.0)
    b = np.log1p(loss.rolling(252, min_periods=126).sum() / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative cash burn over two years (total operating cash destroyed)
def f23ne_f23_negative_earnings_persistence_cumburn_504d_base_v070_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0)
    b = np.log1p(burn.rolling(504, min_periods=252).sum() / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NET-LOSS vs PROFIT INTENSITY RATIO ---
# loss dominance over the year, change vs a quarter ago (dominance momentum)
def f23ne_f23_negative_earnings_persistence_lossdominance_base_v071_signal(netinc):
    loss = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    prof = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    dom = (loss - prof) / (loss + prof + 1e6)
    b = dom - dom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of cumulative burn to cumulative cash generation (burn dominance, ncfo)
def f23ne_f23_negative_earnings_persistence_burndominance_base_v072_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).sum()
    gen = ncfo.clip(lower=0.0).rolling(252, min_periods=126).sum()
    b = (burn - gen) / (burn + gen + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS PERSISTENCE TERM ---
# EPS loss persistence 126d minus 504d (per-share acute-vs-chronic)
def f23ne_f23_negative_earnings_persistence_epslossterm_base_v073_signal(eps):
    s = _f23_losscount(eps, 126)
    l = _f23_losscount(eps, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEFICIT ACCELERATION (via slope of slope at base level) ---
# accumulated-deficit growth z-scored vs its own history (deficit-growth regime)
def f23ne_f23_negative_earnings_persistence_deficitgrz_base_v074_signal(retearn):
    dg = _f23_deficit_growth(retearn, 126)
    b = _z(dg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE LOSS-PERSISTENCE SCORE ---
# composite: net-loss persistence + burn persistence + deficit regime (distress load)
def f23ne_f23_negative_earnings_persistence_composite_base_v075_signal(netinc, ncfo, retearn):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    d = _f23_losscount(retearn, 252)
    b = (a + c + d) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23ne_f23_negative_earnings_persistence_lossfrac_252d_base_v001_signal,
    f23ne_f23_negative_earnings_persistence_losscnt_504d_base_v002_signal,
    f23ne_f23_negative_earnings_persistence_lossstreak_base_v003_signal,
    f23ne_f23_negative_earnings_persistence_lossfracz_63d_base_v004_signal,
    f23ne_f23_negative_earnings_persistence_lossfracspr_base_v005_signal,
    f23ne_f23_negative_earnings_persistence_burnfrac_252d_base_v006_signal,
    f23ne_f23_negative_earnings_persistence_burncnt_504d_base_v007_signal,
    f23ne_f23_negative_earnings_persistence_burnstreak_base_v008_signal,
    f23ne_f23_negative_earnings_persistence_burnfracz_126d_base_v009_signal,
    f23ne_f23_negative_earnings_persistence_epslossfrac_252d_base_v010_signal,
    f23ne_f23_negative_earnings_persistence_epslossstreak_base_v011_signal,
    f23ne_f23_negative_earnings_persistence_epslosscnt_1260d_base_v012_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossfrac_252d_base_v013_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossstreak_base_v014_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossspr_base_v015_signal,
    f23ne_f23_negative_earnings_persistence_tsprofit_ni_base_v016_signal,
    f23ne_f23_negative_earnings_persistence_tsprofit_ebit_base_v017_signal,
    f23ne_f23_negative_earnings_persistence_tsprofit_ncfo_base_v018_signal,
    f23ne_f23_negative_earnings_persistence_tsprofit_eps_base_v019_signal,
    f23ne_f23_negative_earnings_persistence_deficitgr_252d_base_v020_signal,
    f23ne_f23_negative_earnings_persistence_deficitdepth_base_v021_signal,
    f23ne_f23_negative_earnings_persistence_deficitfrac_504d_base_v022_signal,
    f23ne_f23_negative_earnings_persistence_retdrawdown_504d_base_v023_signal,
    f23ne_f23_negative_earnings_persistence_nitrend_252d_base_v024_signal,
    f23ne_f23_negative_earnings_persistence_lossdepthtr_252d_base_v025_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossdepthtr_126d_base_v026_signal,
    f23ne_f23_negative_earnings_persistence_epstrend_252d_base_v027_signal,
    f23ne_f23_negative_earnings_persistence_nilossdepth_base_v028_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossdepth_63d_base_v029_signal,
    f23ne_f23_negative_earnings_persistence_burndepth_252d_base_v030_signal,
    f23ne_f23_negative_earnings_persistence_nisignmag_base_v031_signal,
    f23ne_f23_negative_earnings_persistence_ebitsignmag_base_v032_signal,
    f23ne_f23_negative_earnings_persistence_lossbalance_252d_base_v033_signal,
    f23ne_f23_negative_earnings_persistence_burnbalance_504d_base_v034_signal,
    f23ne_f23_negative_earnings_persistence_profstreak_ni_base_v035_signal,
    f23ne_f23_negative_earnings_persistence_maxlossstreak_252d_base_v036_signal,
    f23ne_f23_negative_earnings_persistence_lossentries_252d_base_v037_signal,
    f23ne_f23_negative_earnings_persistence_burnexits_504d_base_v038_signal,
    f23ne_f23_negative_earnings_persistence_lossbreadth_base_v039_signal,
    f23ne_f23_negative_earnings_persistence_triplelossfrac_252d_base_v040_signal,
    f23ne_f23_negative_earnings_persistence_ebitvncfo_252d_base_v041_signal,
    f23ne_f23_negative_earnings_persistence_lossvsdeficit_base_v042_signal,
    f23ne_f23_negative_earnings_persistence_burnvsdeficit_base_v043_signal,
    f23ne_f23_negative_earnings_persistence_lossfracrank_base_v044_signal,
    f23ne_f23_negative_earnings_persistence_burnfracrank_base_v045_signal,
    f23ne_f23_negative_earnings_persistence_niswing_252d_base_v046_signal,
    f23ne_f23_negative_earnings_persistence_ebitswing_504d_base_v047_signal,
    f23ne_f23_negative_earnings_persistence_chronicloss_base_v048_signal,
    f23ne_f23_negative_earnings_persistence_chronicburn_base_v049_signal,
    f23ne_f23_negative_earnings_persistence_retvel_126d_base_v050_signal,
    f23ne_f23_negative_earnings_persistence_retz_504d_base_v051_signal,
    f23ne_f23_negative_earnings_persistence_deficitvsrun_base_v052_signal,
    f23ne_f23_negative_earnings_persistence_lossterm_base_v053_signal,
    f23ne_f23_negative_earnings_persistence_burnterm_base_v054_signal,
    f23ne_f23_negative_earnings_persistence_epslossdepth_63d_base_v055_signal,
    f23ne_f23_negative_earnings_persistence_epssignmag_base_v056_signal,
    f23ne_f23_negative_earnings_persistence_persistxdeficit_base_v057_signal,
    f23ne_f23_negative_earnings_persistence_burnqtrtally_base_v058_signal,
    f23ne_f23_negative_earnings_persistence_lossqtrtally_base_v059_signal,
    f23ne_f23_negative_earnings_persistence_ebitncfogap_base_v060_signal,
    f23ne_f23_negative_earnings_persistence_lossnarrow_base_v061_signal,
    f23ne_f23_negative_earnings_persistence_depthnarrow_base_v062_signal,
    f23ne_f23_negative_earnings_persistence_deficitfracrank_base_v063_signal,
    f23ne_f23_negative_earnings_persistence_niflips_252d_base_v064_signal,
    f23ne_f23_negative_earnings_persistence_ncfoflips_504d_base_v065_signal,
    f23ne_f23_negative_earnings_persistence_worstloss_252d_base_v066_signal,
    f23ne_f23_negative_earnings_persistence_worstebit_504d_base_v067_signal,
    f23ne_f23_negative_earnings_persistence_persistxswing_base_v068_signal,
    f23ne_f23_negative_earnings_persistence_cumloss_252d_base_v069_signal,
    f23ne_f23_negative_earnings_persistence_cumburn_504d_base_v070_signal,
    f23ne_f23_negative_earnings_persistence_lossdominance_base_v071_signal,
    f23ne_f23_negative_earnings_persistence_burndominance_base_v072_signal,
    f23ne_f23_negative_earnings_persistence_epslossterm_base_v073_signal,
    f23ne_f23_negative_earnings_persistence_deficitgrz_base_v074_signal,
    f23ne_f23_negative_earnings_persistence_composite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_NEGATIVE_EARNINGS_PERSISTENCE_REGISTRY_001_075 = REGISTRY


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

    # pre-revenue explorers: every earnings flow GENUINELY swings across zero so
    # loss-count / streak / time-since-profitable features vary over time. Each
    # flow = a zero-mean cyclical _fund center (allow_neg) + a faster within-quarter
    # wobble + a second _fund noise draw, all centered so the sign flips often.
    def _swing(seed, seed2, base, vol, amp, period):
        raw = _fund(seed, base=base, vol=vol, allow_neg=True)
        center = raw - raw.rolling(252, min_periods=1).mean()
        t = np.arange(n)
        wob = amp * base * np.sin(2.0 * np.pi * t / period)
        nz = _fund(seed2, base=base, vol=vol, allow_neg=True)
        nz = (nz - nz.rolling(252, min_periods=1).mean()) * 0.5
        return center + wob + nz

    netinc = _swing(2301, 2311, 4.0e7, 0.30, 0.50, 80).rename("netinc")
    ncfo = _swing(2302, 2312, 3.5e7, 0.28, 0.50, 95).rename("ncfo")
    eps = _swing(2303, 2313, 2.0, 0.32, 0.50, 70).rename("eps")
    ebit = _swing(2304, 2314, 4.5e7, 0.27, 0.50, 110).rename("ebit")
    retearn = _swing(2305, 2315, 8.0e7, 0.18, 0.35, 160).rename("retearn")

    cols = {"netinc": netinc, "ncfo": ncfo, "eps": eps,
            "ebit": ebit, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("netinc", "ncfo", "eps", "ebit", "retearn")
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

    print("OK f23_negative_earnings_persistence_base_001_075_claude: %d features pass" % n_features)
