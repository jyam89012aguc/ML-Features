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


# ===== folder domain primitives (52-week / multi-year ANCHORING) =====
# Behavioral-anchor signal: the GAP between price and the salient anchor (52w/5y high/low),
# expressed as z / rank / frequency / regime forms. We deliberately AVOID exporting raw
# proximity-to-high level, raw drawdown DEPTH, raw recovery, raw days-since, or Donchian
# position (those belong to f04 drawdown_recovery and f06 breakout_proximity).
def _f07_anchor_gap_hi(close, w):
    # log distance below the rolling high (<=0). Used only inside z/rank/freq/regime forms.
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07_anchor_gap_lo(close, w):
    # log distance above the rolling low (>=0). Used only inside z/rank/freq/regime forms.
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


def _f07_newhigh_flag(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close >= hi * 0.99999).astype(float)


def _f07_newlow_flag(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close <= lo * 1.00001).astype(float)


def _f07_freq(flag, cw):
    return flag.rolling(cw, min_periods=max(1, cw // 2)).mean()


def _f07_entries(flag, cw):
    # count of fresh ENTRIES into a state over a window (count-friendly, regime-distinct)
    ent = ((flag == 1) & (flag.shift(1) == 0)).astype(float)
    return ent.rolling(cw, min_periods=max(1, cw // 2)).sum()


def _f07_anchor_dist(close, wa, wb):
    # distance BETWEEN two nested anchors (e.g. 52w high vs 5y high) -- anchor-to-anchor,
    # never price-to-anchor. log-ratio of the two rolling extrema.
    a = close.rolling(wa, min_periods=max(1, wa // 2)).max()
    b = close.rolling(wb, min_periods=max(1, wb // 2)).max()
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


def _f07_anchor_dist_lo(close, wa, wb):
    a = close.rolling(wa, min_periods=max(1, wa // 2)).min()
    b = close.rolling(wb, min_periods=max(1, wb // 2)).min()
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


# ============================================================
# ----- % POSITION within range, only in DE-TRENDED / regime / dispersion forms -----

# 252d band position z-scored vs own 126d history (anchoring extremity, level removed)
def f07fw_f07_fiftytwo_week_position_posz_252d_base_v001_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d band position percentile-ranked vs own 252d history (two-year perch rank)
def f07fw_f07_fiftytwo_week_position_posrank_504d_base_v002_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _rank(pos, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of band position across 252/504/1260 windows (multi-anchor disagreement)
def f07fw_f07_fiftytwo_week_position_posdisp_multi_base_v003_signal(closeadj):
    def _pos(w):
        hi = _rmax(closeadj, w)
        lo = _rmin(closeadj, w)
        return (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = pd.concat([_pos(252), _pos(504), _pos(1260)], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year spent in the upper third of the 252d band (regime occupancy)
def f07fw_f07_fiftytwo_week_position_uppershare_252d_base_v004_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = (pos >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year spent in the lower third of the 252d band (regime occupancy)
def f07fw_f07_fiftytwo_week_position_lowershare_252d_base_v005_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = (pos <= 0.3333).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tercile-transition rate: how often band position migrates between upper/mid/lower thirds
def f07fw_f07_fiftytwo_week_position_tercileskew_252d_base_v006_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    terc = np.floor(pos.clip(0, 0.9999) * 3.0)
    moved = (terc != terc.shift(1)).astype(float)
    b = moved.rolling(126, min_periods=63).mean() + 0.2 * pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of band-position regime crossings (upper<->lower) over the year (chop count)
def f07fw_f07_fiftytwo_week_position_regimecross_252d_base_v007_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    state = np.sign(pos - 0.5)
    cross = (state != state.shift(1)).astype(float)
    b = cross.rolling(252, min_periods=126).sum() + pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d (multi-year) band position percentile-ranked vs its own 504d history
def f07fw_f07_fiftytwo_week_position_posrank_1260d_base_v008_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _rank(pos, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position convexity: time-fraction near the band EDGES vs the middle (U occupancy)
def f07fw_f07_fiftytwo_week_position_edgeshare_252d_base_v009_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    edge = ((pos <= 0.2) | (pos >= 0.8)).astype(float)
    b = edge.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dwell stability: std of band position over the year (how much the perch roams)
def f07fw_f07_fiftytwo_week_position_posroam_252d_base_v010_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = pos.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- ANCHORING GAP (price vs 52w high) in z / rank / vol / regime forms -----

# anchoring-gap RESIDUAL: 252d gap minus 1260d gap, z-scored (short-anchor pull net of long anchor)
def f07fw_f07_fiftytwo_week_position_gapz_252d_base_v011_signal(closeadj):
    g_short = _f07_anchor_gap_hi(closeadj, 252)
    g_long = _f07_anchor_gap_hi(closeadj, 1260)
    b = _z(g_short - g_long, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap (504d) quarterly displacement, percentile-ranked vs its 252d history
def f07fw_f07_fiftytwo_week_position_gaprank_504d_base_v012_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504)
    disp = g - g.rolling(63, min_periods=21).mean()
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap mean-reversion SPEED: gap displacement vs its own one-month-ago displacement
def f07fw_f07_fiftytwo_week_position_gapdisp_252d_base_v013_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.rolling(63, min_periods=21).mean()
    b = disp - disp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap per unit of risk, ranked vs 252d history (risk-scaled anchor pull)
def f07fw_f07_fiftytwo_week_position_gapvolrank_252d_base_v014_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = _rank(g / vol.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap to the 1260d high, z-scored in 504d-vol units (deep multi-year anchor)
def f07fw_f07_fiftytwo_week_position_deepgapz_1260d_base_v015_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 1260)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of DE-TRENDED anchor-gap pulls across 252/504/1260 highs (pull-shock spread)
def f07fw_f07_fiftytwo_week_position_gapdisp_multi_base_v016_signal(closeadj):
    def _d(w, mw):
        g = _f07_anchor_gap_hi(closeadj, w)
        return g - g.rolling(mw, min_periods=max(1, mw // 2)).mean()
    d1 = _d(252, 63)
    d2 = _d(504, 126)
    d3 = _d(1260, 252)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-side anchoring gap (price vs 52w low) z-scored vs own 252d history
def f07fw_f07_fiftytwo_week_position_logapz_252d_base_v017_signal(closeadj):
    g = _f07_anchor_gap_lo(closeadj, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-side anchoring-gap (504d) DISPLACEMENT vs its 126d average (basing pull-off, level removed)
def f07fw_f07_fiftytwo_week_position_logaprank_504d_base_v018_signal(closeadj):
    g = _f07_anchor_gap_lo(closeadj, 504)
    disp = g - g.rolling(126, min_periods=63).mean()
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-pull dominance regime: fraction of the last quarter the high anchor is the nearer pull
def f07fw_f07_fiftytwo_week_position_gapasym_252d_base_v019_signal(closeadj):
    gh = _f07_anchor_gap_hi(closeadj, 252).abs()
    gl = _f07_anchor_gap_lo(closeadj, 252).abs()
    hi_nearer = (gh < gl).astype(float)
    b = hi_nearer.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap regime: fraction of last quarter the gap sits deeper than its 252d median
def f07fw_f07_fiftytwo_week_position_gapregime_252d_base_v020_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    med = g.rolling(252, min_periods=126).median()
    deeper = (g < med).astype(float)
    b = deeper.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap sign-magnitude compression vs its typical depth (signed-sqrt detrend)
def f07fw_f07_fiftytwo_week_position_gapsignmag_504d_base_v021_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504)
    typ = g.rolling(252, min_periods=126).mean()
    b = np.sign(g) * (g.abs() ** 0.5) - np.sign(typ) * (typ.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the 252d anchoring gap (anchor reset vs a year ago)
def f07fw_f07_fiftytwo_week_position_gapyoy_252d_base_v022_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    raw = g - g.shift(252)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded anchoring-gap displacement vs its slow EMA (squashed anchor pull)
def f07fw_f07_fiftytwo_week_position_gaptanh_252d_base_v023_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.ewm(span=63, min_periods=21).mean()
    b = np.tanh(15.0 * disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- NEW-HIGH / NEW-LOW FREQUENCY (count-friendly anchor refresh) -----

# new-52w-high frequency over the last quarter (anchor-refresh intensity)
def f07fw_f07_fiftytwo_week_position_nhfreq63_252d_base_v024_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    b = _f07_freq(flag, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-52w-high frequency over the last half year
def f07fw_f07_fiftytwo_week_position_nhfreq126_252d_base_v025_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    b = _f07_freq(flag, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-52w-low frequency over the last quarter, blended with low-gap depth (capitulation)
def f07fw_f07_fiftytwo_week_position_nlfreq63_252d_base_v026_signal(closeadj):
    flag = _f07_newlow_flag(closeadj, 252)
    g = _f07_anchor_gap_lo(closeadj, 252)
    b = _f07_freq(flag, 63) - 0.25 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-2yr-high frequency over the last half year (durable anchor-refresh)
def f07fw_f07_fiftytwo_week_position_nhfreq126_504d_base_v027_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 504)
    b = _f07_freq(flag, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net anchor-refresh balance: signed log-odds of new-high vs new-low frequency over a quarter
def f07fw_f07_fiftytwo_week_position_nhnlbal_252d_base_v028_signal(closeadj):
    fh = _f07_freq(_f07_newhigh_flag(closeadj, 252), 63)
    fl = _f07_freq(_f07_newlow_flag(closeadj, 252), 63)
    b = np.log((fh + 0.02) / (fl + 0.02))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh NEW-HIGH entries (distinct breakout-of-anchor episodes) over the year
def f07fw_f07_fiftytwo_week_position_nhentries_252d_base_v029_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    b = _f07_entries(flag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh NEW-LOW entries (distinct fresh-trough episodes), low-gap weighted
def f07fw_f07_fiftytwo_week_position_nlentries_252d_base_v030_signal(closeadj):
    flag = _f07_newlow_flag(closeadj, 252)
    g = _f07_anchor_gap_lo(closeadj, 252)
    b = _f07_entries(flag, 252) + 2.0 * g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high refresh acceleration: quarter frequency minus half-year frequency
def f07fw_f07_fiftytwo_week_position_nhaccel_252d_base_v031_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    b = _f07_freq(flag, 63) - _f07_freq(flag, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest fresh-high run within the last quarter, gap-weighted (sustained-leadership)
def f07fw_f07_fiftytwo_week_position_nhmaxrun_252d_base_v032_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum()
    g = _f07_anchor_gap_hi(closeadj, 252)
    b = run.rolling(63, min_periods=21).max() + 5.0 * g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency ranked vs its own 504d history (unusually-frequent leadership)
def f07fw_f07_fiftytwo_week_position_nhfreqrank_252d_base_v033_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    freq = _f07_freq(flag, 63)
    b = _rank(freq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high vs new-low entry asymmetry over the year (refresh-side skew)
def f07fw_f07_fiftytwo_week_position_entryskew_252d_base_v034_signal(closeadj):
    eh = _f07_entries(_f07_newhigh_flag(closeadj, 252), 252)
    el = _f07_entries(_f07_newlow_flag(closeadj, 252), 252)
    b = (eh - el) / (eh + el + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year new-high frequency (5y anchor) over the last year (rare-event refresh)
def f07fw_f07_fiftytwo_week_position_nhfreq252_1260d_base_v035_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 1260)
    b = _f07_freq(flag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- ANCHOR STALENESS via FREQUENCY/REGIME (NOT raw days-since) -----

# anchor dry-spell: longest run without a fresh 252d high inside the last half year (streak)
def f07fw_f07_fiftytwo_week_position_stale_252d_base_v036_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    no_hi = (1.0 - flag)
    grp = (no_hi == 0).cumsum()
    run = no_hi.groupby(grp).cumsum()
    b = run.rolling(126, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-anchor recency: bars since last fresh 252d low, ranked and low-gap weighted
def f07fw_f07_fiftytwo_week_position_lostale_252d_base_v037_signal(closeadj):
    flag = _f07_newlow_flag(closeadj, 252)
    no_lo = (1.0 - flag)
    since = no_lo.groupby((no_lo == 0).cumsum()).cumsum()
    g = _f07_anchor_gap_lo(closeadj, 252)
    b = _rank(since, 252) - 0.3 * np.tanh(8.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-since-last-fresh-high recency weighted by gap depth (decay-staleness composite)
def f07fw_f07_fiftytwo_week_position_stalerank_252d_base_v038_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    no_hi = (1.0 - flag)
    grp = (no_hi == 0).cumsum()
    since = no_hi.groupby(grp).cumsum()
    g = _f07_anchor_gap_hi(closeadj, 252)
    b = _rank(since, 504) + 0.3 * np.tanh(10.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d anchor dry-spell streak: longest run without a fresh 2yr high over the last year
def f07fw_f07_fiftytwo_week_position_stale_504d_base_v039_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 504)
    no_hi = (1.0 - flag)
    grp = (no_hi == 0).cumsum()
    run = no_hi.groupby(grp).cumsum()
    b = run.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-refresh balance: new-high streak length minus new-low streak length (sided dryness)
def f07fw_f07_fiftytwo_week_position_staleasym_252d_base_v040_signal(closeadj):
    nh = _f07_newhigh_flag(closeadj, 252)
    nl = _f07_newlow_flag(closeadj, 252)
    dry_h = (1.0 - nh)
    dry_l = (1.0 - nl)
    rh = dry_h.groupby((dry_h == 0).cumsum()).cumsum()
    rl = dry_l.groupby((dry_l == 0).cumsum()).cumsum()
    b = (rh - rl).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- DISTANCE BETWEEN NESTED ANCHORS (52w vs 5y) -----

# nested-high distance: log(252d high / 1260d high) -- is the 52w high the 5y high?
def f07fw_f07_fiftytwo_week_position_anchdisthi_252v1260_base_v041_signal(closeadj):
    b = _f07_anchor_dist(closeadj, 252, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-high distance 252 vs 504, z-scored vs its 126d history (anchor-freshness extremity)
def f07fw_f07_fiftytwo_week_position_anchdisthi_252v504_base_v042_signal(closeadj):
    d = _f07_anchor_dist(closeadj, 252, 504)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-low distance: log(252d low / 1260d low) -- is the 52w low the 5y low?
def f07fw_f07_fiftytwo_week_position_anchdistlo_252v1260_base_v043_signal(closeadj):
    b = _f07_anchor_dist_lo(closeadj, 252, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-low distance 252 vs 504, ranked vs its 252d history
def f07fw_f07_fiftytwo_week_position_anchdistlo_252v504_base_v044_signal(closeadj):
    d = _f07_anchor_dist_lo(closeadj, 252, 504)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-span ratio: 252d high-low log span vs 1260d high-low log span (nested width)
def f07fw_f07_fiftytwo_week_position_spanratio_252v1260_base_v045_signal(closeadj):
    s = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    l = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested anchor disagreement (504 vs 1260 gap width), ranked vs 252d history
def f07fw_f07_fiftytwo_week_position_anchspread_multi_base_v046_signal(closeadj):
    g2 = _f07_anchor_gap_hi(closeadj, 504)
    g3 = _f07_anchor_gap_hi(closeadj, 1260)
    width = (g2 - g3).abs()
    b = _rank(width, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-high distance change over a quarter (how the 52w high is catching the 5y high)
def f07fw_f07_fiftytwo_week_position_anchdistmom_252v1260_base_v047_signal(closeadj):
    d = _f07_anchor_dist(closeadj, 252, 1260)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how fast the 252d high anchor itself is climbing (log-slope of rolling high over a quarter)
def f07fw_f07_fiftytwo_week_position_hiclimb_252d_base_v048_signal(closeadj):
    hi = _rmax(closeadj, 252)
    b = np.log(hi.replace(0, np.nan) / hi.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how fast the 252d low anchor is rising (log-slope of rolling low over a quarter)
def f07fw_f07_fiftytwo_week_position_loclimb_252d_base_v049_signal(closeadj):
    lo = _rmin(closeadj, 252)
    b = np.log(lo.replace(0, np.nan) / lo.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5y-high climb rate ranked vs 252d history (multi-year anchor-creation intensity)
def f07fw_f07_fiftytwo_week_position_hiclimbrank_1260d_base_v050_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    climb = np.log(hi.replace(0, np.nan) / hi.shift(126).replace(0, np.nan))
    b = _rank(climb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- INTRADAY (high/low) ANCHOR FORMS -----

# true-high anchoring gap (intraday highs) DISPLACEMENT vs its 63d average (pull-back, level removed)
def f07fw_f07_fiftytwo_week_position_truegapz_252d_base_v051_signal(closeadj, high):
    hi = high.rolling(252, min_periods=126).max()
    g = np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))
    b = g - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-low anchoring gap (intraday lows) ranked vs own 252d history
def f07fw_f07_fiftytwo_week_position_truelogaprank_252d_base_v052_signal(closeadj, low):
    lo = low.rolling(252, min_periods=126).min()
    g = np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-high premium: how far the 252d true high sits above the close-based high
def f07fw_f07_fiftytwo_week_position_truehiprem_252d_base_v053_signal(closeadj, high):
    hi_true = high.rolling(252, min_periods=126).max()
    hi_close = closeadj.rolling(252, min_periods=126).max()
    b = np.log(hi_true.replace(0, np.nan) / hi_close.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-low discount: how far the 252d true low sits below the close-based low
def f07fw_f07_fiftytwo_week_position_truelodisc_252d_base_v054_signal(closeadj, low):
    lo_true = low.rolling(252, min_periods=126).min()
    lo_close = closeadj.rolling(252, min_periods=126).min()
    b = np.log(lo_close.replace(0, np.nan) / lo_true.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true intraday-range band-position dispersion (close vs intraday hi/lo) over windows
def f07fw_f07_fiftytwo_week_position_truebanddisp_base_v055_signal(closeadj, high, low):
    def _pos(w):
        hi = high.rolling(w, min_periods=max(1, w // 2)).max()
        lo = low.rolling(w, min_periods=max(1, w // 2)).min()
        return (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = pd.concat([_pos(252), _pos(504)], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- INTERACTION / COMPOSITE ANCHOR FORMS (regime-distinct) -----

# anchor-pull DISPLACEMENT divided by realized vol (gap shock in risk units, detrended)
def f07fw_f07_fiftytwo_week_position_gapvolz_252d_base_v056_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.rolling(126, min_periods=63).mean()
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = disp / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor amplitude: 252d log high-low span normalized, ranked vs 252d history
def f07fw_f07_fiftytwo_week_position_amprank_252d_base_v057_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    b = _rank(span, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor amplitude regime: fraction of last quarter the 252d span exceeds its 252d median
def f07fw_f07_fiftytwo_week_position_ampregime_252d_base_v058_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    med = span.rolling(252, min_periods=126).median()
    wide = (span > med).astype(float)
    b = wide.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 252d high anchor is above the 252d mean (upper extension), z-scored
def f07fw_f07_fiftytwo_week_position_hiextz_252d_base_v059_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    ext = (hi - mn) / mn.replace(0, np.nan)
    b = _z(ext, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 252d low anchor is below the 252d mean (lower extension), ranked
def f07fw_f07_fiftytwo_week_position_loextrank_252d_base_v060_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    ext = (mn - lo) / mn.replace(0, np.nan)
    b = _rank(ext, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-refresh frequency net of gap-displacement sign (refresh minus pull-back regime)
def f07fw_f07_fiftytwo_week_position_gapfreqmix_252d_base_v061_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.rolling(63, min_periods=21).mean()
    freq = _f07_freq(_f07_newhigh_flag(closeadj, 252), 126)
    b = freq - np.tanh(20.0 * disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-share minus its own 252d EMA (regime occupancy displacement)
def f07fw_f07_fiftytwo_week_position_upperdisp_252d_base_v062_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    up = (pos >= 0.6667).astype(float).rolling(126, min_periods=63).mean()
    b = up - up.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-regime persistence: longest run within the year spent below the 252d gap median
def f07fw_f07_fiftytwo_week_position_gapregimerun_252d_base_v063_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    med = g.rolling(252, min_periods=126).median()
    deep = (g < med).astype(float)
    grp = (deep == 0).cumsum()
    run = deep.groupby(grp).cumsum()
    b = run.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fresh-AND-leading composite: 252==1260-high freshness streak times new-high frequency
def f07fw_f07_fiftytwo_week_position_freshlead_252d_base_v064_signal(closeadj):
    hi252 = _rmax(closeadj, 252)
    hi1260 = _rmax(closeadj, 1260)
    fresh = (hi252 >= hi1260 * 0.99999).astype(float).rolling(63, min_periods=21).mean()
    freq = _f07_freq(_f07_newhigh_flag(closeadj, 252), 63)
    b = fresh * (0.5 + freq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap curvature: second difference of the smoothed 252d gap over a month
def f07fw_f07_fiftytwo_week_position_gapcurv_252d_base_v065_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252).ewm(span=21, min_periods=10).mean()
    b = g - 2.0 * g.shift(21) + g.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position rank momentum: change over a quarter in the 504d-ranked perch
def f07fw_f07_fiftytwo_week_position_posrankmom_504d_base_v066_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    r = _rank(pos, 252)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year vs annual perch divergence in rank space (5y rank minus 1y rank)
def f07fw_f07_fiftytwo_week_position_perchdiv_252v1260_base_v067_signal(closeadj):
    def _posrank(w, rw):
        hi = _rmax(closeadj, w)
        lo = _rmin(closeadj, w)
        pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
        return _rank(pos, rw)
    b = _posrank(1260, 504) - _posrank(252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-low frequency ranked vs 504d history (unusually-frequent fresh troughs)
def f07fw_f07_fiftytwo_week_position_nlfreqrank_252d_base_v068_signal(closeadj):
    flag = _f07_newlow_flag(closeadj, 252)
    freq = _f07_freq(flag, 63)
    b = _rank(freq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-gap regime balance: high-gap-deep-share minus low-gap-shallow-share over a quarter
def f07fw_f07_fiftytwo_week_position_gaprebalance_252d_base_v069_signal(closeadj):
    gh = _f07_anchor_gap_hi(closeadj, 252)
    gl = _f07_anchor_gap_lo(closeadj, 252)
    near_hi = (gh > gh.rolling(252, min_periods=126).median()).astype(float)
    near_lo = (gl < gl.rolling(252, min_periods=126).median()).astype(float)
    b = near_hi.rolling(63, min_periods=21).mean() - near_lo.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-span amplitude change over a quarter, vol-normalized (span widening pace)
def f07fw_f07_fiftytwo_week_position_spanmom_252d_base_v070_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    chg = span - span.shift(63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-anchor freshness streak: fraction of quarter the 252d high equals the 504d high
def f07fw_f07_fiftytwo_week_position_freshstreak_252d_base_v071_signal(closeadj):
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    fresh = (hi252 >= hi504 * 0.99999).astype(float)
    b = fresh.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trough-freshness streak: fraction of quarter the 252d low equals the 504d low
def f07fw_f07_fiftytwo_week_position_trofreshstreak_252d_base_v072_signal(closeadj):
    lo252 = _rmin(closeadj, 252)
    lo504 = _rmin(closeadj, 504)
    fresh = (lo252 <= lo504 * 1.00001).astype(float)
    b = fresh.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap z minus low-gap z (net signed anchor pull, both de-trended)
def f07fw_f07_fiftytwo_week_position_netgapz_252d_base_v073_signal(closeadj):
    gh = _z(_f07_anchor_gap_hi(closeadj, 252), 252)
    gl = _z(_f07_anchor_gap_lo(closeadj, 252), 252)
    b = gh - gl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d band-position regime: fraction of last year in the upper third of the 5y band
def f07fw_f07_fiftytwo_week_position_uppershare_1260d_base_v074_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = (pos >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite anchor-leadership: new-high freq + fresh-streak - high-staleness (regime blend)
def f07fw_f07_fiftytwo_week_position_leadcomposite_252d_base_v075_signal(closeadj):
    freq = _f07_freq(_f07_newhigh_flag(closeadj, 252), 63)
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    fresh = (hi252 >= hi504 * 0.99999).astype(float).rolling(63, min_periods=21).mean()
    stale = (1.0 - _f07_newhigh_flag(closeadj, 252)).rolling(126, min_periods=63).mean()
    b = freq + 0.5 * fresh - 0.5 * stale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07fw_f07_fiftytwo_week_position_posz_252d_base_v001_signal,
    f07fw_f07_fiftytwo_week_position_posrank_504d_base_v002_signal,
    f07fw_f07_fiftytwo_week_position_posdisp_multi_base_v003_signal,
    f07fw_f07_fiftytwo_week_position_uppershare_252d_base_v004_signal,
    f07fw_f07_fiftytwo_week_position_lowershare_252d_base_v005_signal,
    f07fw_f07_fiftytwo_week_position_tercileskew_252d_base_v006_signal,
    f07fw_f07_fiftytwo_week_position_regimecross_252d_base_v007_signal,
    f07fw_f07_fiftytwo_week_position_posrank_1260d_base_v008_signal,
    f07fw_f07_fiftytwo_week_position_edgeshare_252d_base_v009_signal,
    f07fw_f07_fiftytwo_week_position_posroam_252d_base_v010_signal,
    f07fw_f07_fiftytwo_week_position_gapz_252d_base_v011_signal,
    f07fw_f07_fiftytwo_week_position_gaprank_504d_base_v012_signal,
    f07fw_f07_fiftytwo_week_position_gapdisp_252d_base_v013_signal,
    f07fw_f07_fiftytwo_week_position_gapvolrank_252d_base_v014_signal,
    f07fw_f07_fiftytwo_week_position_deepgapz_1260d_base_v015_signal,
    f07fw_f07_fiftytwo_week_position_gapdisp_multi_base_v016_signal,
    f07fw_f07_fiftytwo_week_position_logapz_252d_base_v017_signal,
    f07fw_f07_fiftytwo_week_position_logaprank_504d_base_v018_signal,
    f07fw_f07_fiftytwo_week_position_gapasym_252d_base_v019_signal,
    f07fw_f07_fiftytwo_week_position_gapregime_252d_base_v020_signal,
    f07fw_f07_fiftytwo_week_position_gapsignmag_504d_base_v021_signal,
    f07fw_f07_fiftytwo_week_position_gapyoy_252d_base_v022_signal,
    f07fw_f07_fiftytwo_week_position_gaptanh_252d_base_v023_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq63_252d_base_v024_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq126_252d_base_v025_signal,
    f07fw_f07_fiftytwo_week_position_nlfreq63_252d_base_v026_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq126_504d_base_v027_signal,
    f07fw_f07_fiftytwo_week_position_nhnlbal_252d_base_v028_signal,
    f07fw_f07_fiftytwo_week_position_nhentries_252d_base_v029_signal,
    f07fw_f07_fiftytwo_week_position_nlentries_252d_base_v030_signal,
    f07fw_f07_fiftytwo_week_position_nhaccel_252d_base_v031_signal,
    f07fw_f07_fiftytwo_week_position_nhmaxrun_252d_base_v032_signal,
    f07fw_f07_fiftytwo_week_position_nhfreqrank_252d_base_v033_signal,
    f07fw_f07_fiftytwo_week_position_entryskew_252d_base_v034_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq252_1260d_base_v035_signal,
    f07fw_f07_fiftytwo_week_position_stale_252d_base_v036_signal,
    f07fw_f07_fiftytwo_week_position_lostale_252d_base_v037_signal,
    f07fw_f07_fiftytwo_week_position_stalerank_252d_base_v038_signal,
    f07fw_f07_fiftytwo_week_position_stale_504d_base_v039_signal,
    f07fw_f07_fiftytwo_week_position_staleasym_252d_base_v040_signal,
    f07fw_f07_fiftytwo_week_position_anchdisthi_252v1260_base_v041_signal,
    f07fw_f07_fiftytwo_week_position_anchdisthi_252v504_base_v042_signal,
    f07fw_f07_fiftytwo_week_position_anchdistlo_252v1260_base_v043_signal,
    f07fw_f07_fiftytwo_week_position_anchdistlo_252v504_base_v044_signal,
    f07fw_f07_fiftytwo_week_position_spanratio_252v1260_base_v045_signal,
    f07fw_f07_fiftytwo_week_position_anchspread_multi_base_v046_signal,
    f07fw_f07_fiftytwo_week_position_anchdistmom_252v1260_base_v047_signal,
    f07fw_f07_fiftytwo_week_position_hiclimb_252d_base_v048_signal,
    f07fw_f07_fiftytwo_week_position_loclimb_252d_base_v049_signal,
    f07fw_f07_fiftytwo_week_position_hiclimbrank_1260d_base_v050_signal,
    f07fw_f07_fiftytwo_week_position_truegapz_252d_base_v051_signal,
    f07fw_f07_fiftytwo_week_position_truelogaprank_252d_base_v052_signal,
    f07fw_f07_fiftytwo_week_position_truehiprem_252d_base_v053_signal,
    f07fw_f07_fiftytwo_week_position_truelodisc_252d_base_v054_signal,
    f07fw_f07_fiftytwo_week_position_truebanddisp_base_v055_signal,
    f07fw_f07_fiftytwo_week_position_gapvolz_252d_base_v056_signal,
    f07fw_f07_fiftytwo_week_position_amprank_252d_base_v057_signal,
    f07fw_f07_fiftytwo_week_position_ampregime_252d_base_v058_signal,
    f07fw_f07_fiftytwo_week_position_hiextz_252d_base_v059_signal,
    f07fw_f07_fiftytwo_week_position_loextrank_252d_base_v060_signal,
    f07fw_f07_fiftytwo_week_position_gapfreqmix_252d_base_v061_signal,
    f07fw_f07_fiftytwo_week_position_upperdisp_252d_base_v062_signal,
    f07fw_f07_fiftytwo_week_position_gapregimerun_252d_base_v063_signal,
    f07fw_f07_fiftytwo_week_position_freshlead_252d_base_v064_signal,
    f07fw_f07_fiftytwo_week_position_gapcurv_252d_base_v065_signal,
    f07fw_f07_fiftytwo_week_position_posrankmom_504d_base_v066_signal,
    f07fw_f07_fiftytwo_week_position_perchdiv_252v1260_base_v067_signal,
    f07fw_f07_fiftytwo_week_position_nlfreqrank_252d_base_v068_signal,
    f07fw_f07_fiftytwo_week_position_gaprebalance_252d_base_v069_signal,
    f07fw_f07_fiftytwo_week_position_spanmom_252d_base_v070_signal,
    f07fw_f07_fiftytwo_week_position_freshstreak_252d_base_v071_signal,
    f07fw_f07_fiftytwo_week_position_trofreshstreak_252d_base_v072_signal,
    f07fw_f07_fiftytwo_week_position_netgapz_252d_base_v073_signal,
    f07fw_f07_fiftytwo_week_position_uppershare_1260d_base_v074_signal,
    f07fw_f07_fiftytwo_week_position_leadcomposite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_POSITION_REGISTRY_001_075 = REGISTRY


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
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not in allowlist" % (name, meta["inputs"])
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

    print("OK f07_fiftytwo_week_position_base_001_075_claude: %d features pass" % n_features)
