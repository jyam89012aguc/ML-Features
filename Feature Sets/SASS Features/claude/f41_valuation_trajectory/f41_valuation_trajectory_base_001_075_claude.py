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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s vs time over window w (handles variable warm-up length)
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(np.dot(x, a) / denom)

    raw = s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)
    return raw


# ===== folder domain primitives (valuation re-rating / trajectory) =====
def _f41_logmult(m):
    # log of a multiple (re-rating works multiplicatively)
    return np.log(m.replace(0, np.nan).clip(lower=1e-9))


def _f41_rerate(m, w):
    # log re-rating over window w: how much the multiple expanded/compressed
    lm = _f41_logmult(m)
    return lm - lm.shift(w)


def _f41_rerate_slope(m, w):
    # per-day re-rating slope of the log multiple
    lm = _f41_logmult(m)
    return _slope(lm, w)


def _f41_compress(m, w):
    # multiplicative compression/expansion ratio over window
    return m / m.shift(w).replace(0, np.nan) - 1.0


def _f41_zhist(m, w):
    # valuation z vs own history
    return _z(m, w)


def _f41_revgap(m, w):
    # mean-reversion gap: current multiple vs its own rolling mean (log)
    lm = _f41_logmult(m)
    return lm - lm.rolling(w, min_periods=max(2, w // 2)).mean()


def _f41_evtrend(ev, w):
    # log trend of EV
    lev = _f41_logmult(ev)
    return lev - lev.shift(w)


# ============================================================
# --- PE re-rating slope family ---
def f41vj_f41_valuation_trajectory_pererate_63d_base_v001_signal(pe):
    b = _f41_rerate(pe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pererate_126d_base_v002_signal(pe):
    b = _f41_rerate(pe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pererate_252d_base_v003_signal(pe):
    b = _f41_rerate(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pereslope_252d_base_v004_signal(pe):
    b = _f41_rerate_slope(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pereslopecurv_126d_base_v005_signal(pe):
    # curvature of the re-rating path: difference of consecutive 63d slopes
    lm = _f41_logmult(pe)
    sl = _slope(lm, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PB re-rating slope family ---
def f41vj_f41_valuation_trajectory_pbrerate_63d_base_v006_signal(pb):
    b = _f41_rerate(pb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbrerate_252d_base_v007_signal(pb):
    b = _f41_rerate(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbeslope_252d_base_v008_signal(pb):
    b = _f41_rerate_slope(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PS re-rating slope family ---
def f41vj_f41_valuation_trajectory_psrerate_126d_base_v009_signal(ps):
    b = _f41_rerate(ps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerate_252d_base_v010_signal(ps):
    b = _f41_rerate(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pseslope_126d_base_v011_signal(ps):
    b = _f41_rerate_slope(ps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/EBITDA re-rating slope family ---
def f41vj_f41_valuation_trajectory_evebrerate_63d_base_v012_signal(evebitda):
    b = _f41_rerate(evebitda, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerate_252d_base_v013_signal(evebitda):
    b = _f41_rerate(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebslope_252d_base_v014_signal(evebitda):
    b = _f41_rerate_slope(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple compression / expansion (ratio form) ---
def f41vj_f41_valuation_trajectory_pecompressstreak_base_v015_signal(pe):
    # net compression streak: signed run-length balance of daily multiple moves
    d = np.sign(_f41_logmult(pe).diff())
    b = d.rolling(63, min_periods=21).sum() / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbcompress_126d_base_v016_signal(pb):
    b = _f41_compress(pb, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pscompress_63d_base_v017_signal(ps):
    b = _f41_compress(ps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebcompress_126d_base_v018_signal(evebitda):
    b = _f41_compress(evebitda, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation z vs own history ---
def f41vj_f41_valuation_trajectory_pezhist_252d_base_v019_signal(pe):
    b = _f41_zhist(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbzhist_252d_base_v020_signal(pb):
    b = _f41_zhist(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pszhist_504d_base_v021_signal(ps):
    b = _f41_zhist(ps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebzhist_252d_base_v022_signal(evebitda):
    b = _f41_zhist(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_mcapzhist_504d_base_v023_signal(marketcap):
    b = _f41_zhist(marketcap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV trend ---
def f41vj_f41_valuation_trajectory_evtrend_126d_base_v024_signal(ev):
    b = _f41_evtrend(ev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evtrend_252d_base_v025_signal(ev):
    b = _f41_evtrend(ev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evaccel_252d_base_v026_signal(ev):
    # EV trend acceleration: recent-half EV trend minus older-half EV trend
    let = _f41_logmult(ev)
    recent = let - let.shift(126)
    older = let.shift(126) - let.shift(252)
    b = recent - older
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple mean-reversion gap ---
def f41vj_f41_valuation_trajectory_perevgap_252d_base_v027_signal(pe):
    b = _f41_revgap(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbrevgap_252d_base_v028_signal(pb):
    b = _f41_revgap(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrevgap_126d_base_v029_signal(ps):
    b = _f41_revgap(ps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrevgap_252d_base_v030_signal(evebitda):
    b = _f41_revgap(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating momentum: change of the re-rating itself ---
def f41vj_f41_valuation_trajectory_pemomrank_63d_base_v031_signal(pe):
    # re-rating momentum ranked vs its own 252d history (bounded acceleration)
    r = _f41_rerate(pe, 63)
    chg = r - r.shift(63)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbmom_63d_base_v032_signal(pb):
    r = _f41_rerate(pb, 63)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebmom_63d_base_v033_signal(evebitda):
    r = _f41_rerate(evebitda, 63)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating percentile rank vs history ---
def f41vj_f41_valuation_trajectory_pererank_252d_base_v034_signal(pe):
    r = _f41_rerate(pe, 63)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerank_252d_base_v035_signal(ps):
    r = _f41_rerate(ps, 63)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerank_252d_base_v036_signal(evebitda):
    r = _f41_rerate(evebitda, 63)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation level rank vs own multi-year history (cheap/rich percentile) ---
def f41vj_f41_valuation_trajectory_pelvlrank_504d_base_v037_signal(pe):
    b = _rank(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pblvlrank_504d_base_v038_signal(pb):
    b = _rank(pb, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebvlrank_504d_base_v039_signal(evebitda):
    b = _rank(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating dispersion / instability (vol of the re-rating) ---
def f41vj_f41_valuation_trajectory_pererevol_252d_base_v040_signal(pe):
    chg = _f41_logmult(pe).diff()
    b = _std(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerevol_126d_base_v041_signal(ps):
    chg = _f41_logmult(ps).diff()
    b = _std(chg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerevol_252d_base_v042_signal(evebitda):
    chg = _f41_logmult(evebitda).diff()
    b = _std(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- short vs long re-rating spread (acceleration of re-rating) ---
def f41vj_f41_valuation_trajectory_perespread_base_v043_signal(pe):
    s = _f41_rerate(pe, 63)
    l = _f41_rerate(pe, 252) / 4.0
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbrespread_base_v044_signal(pb):
    s = _f41_rerate(pb, 63)
    l = _f41_rerate(pb, 252) / 4.0
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrespread_base_v045_signal(evebitda):
    s = _f41_rerate(evebitda, 63)
    l = _f41_rerate(evebitda, 252) / 4.0
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV vs marketcap trajectory divergence (capital structure re-rating) ---
def f41vj_f41_valuation_trajectory_evmcapdivslope_126d_base_v046_signal(ev, marketcap):
    # EV-vs-marketcap divergence as a regression slope of the log premium
    prem = _f41_logmult(ev) - _f41_logmult(marketcap)
    b = _slope(prem, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evmcapdiv_252d_base_v047_signal(ev, marketcap):
    re = _f41_evtrend(ev, 252)
    rm = _f41_logmult(marketcap) - _f41_logmult(marketcap).shift(252)
    b = re - rm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- marketcap re-rating slope ---
def f41vj_f41_valuation_trajectory_mcapslope_252d_base_v048_signal(marketcap):
    b = _slope(_f41_logmult(marketcap), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_mcaprerate_126d_base_v049_signal(marketcap):
    b = _f41_logmult(marketcap) - _f41_logmult(marketcap).shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-multiple re-rating breadth (how many multiples expanding) ---
def f41vj_f41_valuation_trajectory_rerbreadth_126d_base_v050_signal(pe, pb, ps, evebitda):
    up = (
        (_f41_rerate(pe, 126) > 0).astype(float)
        + (_f41_rerate(pb, 126) > 0).astype(float)
        + (_f41_rerate(ps, 126) > 0).astype(float)
        + (_f41_rerate(evebitda, 126) > 0).astype(float)
    )
    # smooth the breadth count over a quarter so it varies continuously
    b = up.rolling(63, min_periods=21).mean() / 4.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-multiple re-rating dispersion (multiples disagree) ---
def f41vj_f41_valuation_trajectory_rerdisp_252d_base_v051_signal(pe, pb, ps, evebitda):
    r1 = _f41_rerate(pe, 252)
    r2 = _f41_rerate(pb, 252)
    r3 = _f41_rerate(ps, 252)
    r4 = _f41_rerate(evebitda, 252)
    b = pd.concat([r1, r2, r3, r4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite re-rating: average log re-rating across multiples ---
def f41vj_f41_valuation_trajectory_rercomp_252d_base_v052_signal(pe, ps, evebitda):
    r = pd.concat(
        [_f41_rerate(pe, 252), _f41_rerate(ps, 252), _f41_rerate(evebitda, 252)],
        axis=1,
    ).mean(axis=1)
    result = r
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple distance from its own 504d max (rich exhaustion) ---
def f41vj_f41_valuation_trajectory_perichexh_504d_base_v053_signal(pe):
    hi = _rmax(pe, 504)
    b = _f41_logmult(pe) - _f41_logmult(hi)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrichexh_504d_base_v054_signal(evebitda):
    hi = _rmax(evebitda, 504)
    b = _f41_logmult(evebitda) - _f41_logmult(hi)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple distance from its own 504d min (cheap floor proximity) ---
def f41vj_f41_valuation_trajectory_pscheapfloor_504d_base_v055_signal(ps):
    lo = _rmin(ps, 504)
    b = _f41_logmult(ps) - _f41_logmult(lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbcheapfloor_504d_base_v056_signal(pb):
    lo = _rmin(pb, 504)
    b = _f41_logmult(pb) - _f41_logmult(lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating range position within own history (0..1 of valuation band) ---
def f41vj_f41_valuation_trajectory_pebandpos_504d_base_v057_signal(pe):
    hi = _rmax(pe, 504)
    lo = _rmin(pe, 504)
    b = (pe - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebbandposmom_504d_base_v058_signal(evebitda):
    # momentum of where the multiple sits in its 504d band (band-position drift)
    hi = _rmax(evebitda, 504)
    lo = _rmin(evebitda, 504)
    pos = (evebitda - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating momentum via EMA displacement of log-multiple ---
def f41vj_f41_valuation_trajectory_pedisp_base_v059_signal(pe):
    lm = _f41_logmult(pe)
    b = lm - lm.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerangeexp_base_v060_signal(ps):
    # re-rating range expansion: recent 21d log-multiple span vs its 126d typical span
    lm = _f41_logmult(ps)
    span = _rmax(lm, 21) - _rmin(lm, 21)
    typ = (_rmax(lm, 126) - _rmin(lm, 126)) / 6.0
    b = span / typ.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tanh-bounded re-rating momentum ---
def f41vj_f41_valuation_trajectory_evebrevsnap_126d_base_v061_signal(evebitda):
    # mean-reversion snap: reversion gap relative to recent re-rating direction
    g = _f41_revgap(evebitda, 252)
    r = _f41_rerate(evebitda, 21)
    b = np.tanh(2.0 * g) * np.sign(r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pevsps_rerspread_v062_signal(pe, ps):
    # cross-multiple re-rating spread: earnings multiple vs sales multiple re-rating
    b = _f41_rerate(pe, 126) - _f41_rerate(ps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion gap z-scored (extremity of cheapness/richness) ---
def f41vj_f41_valuation_trajectory_perevgapz_252d_base_v063_signal(pe):
    g = _f41_revgap(pe, 252)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrevgapz_252d_base_v064_signal(ps):
    g = _f41_revgap(ps, 252)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating sign x magnitude (signed compression strength) ---
def f41vj_f41_valuation_trajectory_pbgapsignmag_252d_base_v065_signal(pb):
    # signed sqrt of the price-to-book mean-reversion gap (extremity, compressed tails)
    g = _f41_revgap(pb, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbsignmag_252d_base_v066_signal(pb):
    r = _f41_rerate(pb, 252)
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/sales-style: ev trend per marketcap level (re-rating of enterprise premium) ---
def f41vj_f41_valuation_trajectory_evpremrevgap_252d_base_v067_signal(ev, marketcap):
    # enterprise-premium mean-reversion gap: current EV/mcap premium vs its own mean
    prem = _f41_logmult(ev) - _f41_logmult(marketcap)
    b = prem - prem.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evpremz_252d_base_v068_signal(ev, marketcap):
    prem = _f41_logmult(ev) - _f41_logmult(marketcap)
    b = _z(prem, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple acceleration via second-difference proxy at base level ---
def f41vj_f41_valuation_trajectory_evebpsgapmom_base_v069_signal(evebitda, ps):
    # cross-multiple reversion-gap divergence momentum (EV/EBITDA gap vs sales gap)
    spread = _f41_revgap(evebitda, 252) - _f41_revgap(ps, 252)
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psaccel_base_v070_signal(ps):
    lm = _f41_logmult(ps)
    b = (lm - lm.shift(63)) - (lm.shift(63) - lm.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite cheapness-rank momentum (rank now vs rank a quarter ago) ---
def f41vj_f41_valuation_trajectory_perankmom_504d_base_v071_signal(pe):
    rk = _rank(pe, 504)
    b = rk - rk.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrankmom_504d_base_v072_signal(evebitda):
    rk = _rank(evebitda, 504)
    b = rk - rk.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating consistency: hit-rate of expansion days over a year ---
def f41vj_f41_valuation_trajectory_pehitrate_252d_base_v073_signal(pe):
    up = (_f41_logmult(pe).diff() > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebhitrate_252d_base_v074_signal(evebitda):
    up = (_f41_logmult(evebitda).diff() > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- enterprise-multiple gap vs equity-multiple gap (structural re-rating tilt) ---
def f41vj_f41_valuation_trajectory_structtilt_252d_base_v075_signal(evebitda, pe):
    ge = _f41_revgap(evebitda, 252)
    gp = _f41_revgap(pe, 252)
    b = ge - gp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41vj_f41_valuation_trajectory_pererate_63d_base_v001_signal,
    f41vj_f41_valuation_trajectory_pererate_126d_base_v002_signal,
    f41vj_f41_valuation_trajectory_pererate_252d_base_v003_signal,
    f41vj_f41_valuation_trajectory_pereslope_252d_base_v004_signal,
    f41vj_f41_valuation_trajectory_pereslopecurv_126d_base_v005_signal,
    f41vj_f41_valuation_trajectory_pbrerate_63d_base_v006_signal,
    f41vj_f41_valuation_trajectory_pbrerate_252d_base_v007_signal,
    f41vj_f41_valuation_trajectory_pbeslope_252d_base_v008_signal,
    f41vj_f41_valuation_trajectory_psrerate_126d_base_v009_signal,
    f41vj_f41_valuation_trajectory_psrerate_252d_base_v010_signal,
    f41vj_f41_valuation_trajectory_pseslope_126d_base_v011_signal,
    f41vj_f41_valuation_trajectory_evebrerate_63d_base_v012_signal,
    f41vj_f41_valuation_trajectory_evebrerate_252d_base_v013_signal,
    f41vj_f41_valuation_trajectory_evebslope_252d_base_v014_signal,
    f41vj_f41_valuation_trajectory_pecompressstreak_base_v015_signal,
    f41vj_f41_valuation_trajectory_pbcompress_126d_base_v016_signal,
    f41vj_f41_valuation_trajectory_pscompress_63d_base_v017_signal,
    f41vj_f41_valuation_trajectory_evebcompress_126d_base_v018_signal,
    f41vj_f41_valuation_trajectory_pezhist_252d_base_v019_signal,
    f41vj_f41_valuation_trajectory_pbzhist_252d_base_v020_signal,
    f41vj_f41_valuation_trajectory_pszhist_504d_base_v021_signal,
    f41vj_f41_valuation_trajectory_evebzhist_252d_base_v022_signal,
    f41vj_f41_valuation_trajectory_mcapzhist_504d_base_v023_signal,
    f41vj_f41_valuation_trajectory_evtrend_126d_base_v024_signal,
    f41vj_f41_valuation_trajectory_evtrend_252d_base_v025_signal,
    f41vj_f41_valuation_trajectory_evaccel_252d_base_v026_signal,
    f41vj_f41_valuation_trajectory_perevgap_252d_base_v027_signal,
    f41vj_f41_valuation_trajectory_pbrevgap_252d_base_v028_signal,
    f41vj_f41_valuation_trajectory_psrevgap_126d_base_v029_signal,
    f41vj_f41_valuation_trajectory_evebrevgap_252d_base_v030_signal,
    f41vj_f41_valuation_trajectory_pemomrank_63d_base_v031_signal,
    f41vj_f41_valuation_trajectory_pbmom_63d_base_v032_signal,
    f41vj_f41_valuation_trajectory_evebmom_63d_base_v033_signal,
    f41vj_f41_valuation_trajectory_pererank_252d_base_v034_signal,
    f41vj_f41_valuation_trajectory_psrerank_252d_base_v035_signal,
    f41vj_f41_valuation_trajectory_evebrerank_252d_base_v036_signal,
    f41vj_f41_valuation_trajectory_pelvlrank_504d_base_v037_signal,
    f41vj_f41_valuation_trajectory_pblvlrank_504d_base_v038_signal,
    f41vj_f41_valuation_trajectory_evebvlrank_504d_base_v039_signal,
    f41vj_f41_valuation_trajectory_pererevol_252d_base_v040_signal,
    f41vj_f41_valuation_trajectory_psrerevol_126d_base_v041_signal,
    f41vj_f41_valuation_trajectory_evebrerevol_252d_base_v042_signal,
    f41vj_f41_valuation_trajectory_perespread_base_v043_signal,
    f41vj_f41_valuation_trajectory_pbrespread_base_v044_signal,
    f41vj_f41_valuation_trajectory_evebrespread_base_v045_signal,
    f41vj_f41_valuation_trajectory_evmcapdivslope_126d_base_v046_signal,
    f41vj_f41_valuation_trajectory_evmcapdiv_252d_base_v047_signal,
    f41vj_f41_valuation_trajectory_mcapslope_252d_base_v048_signal,
    f41vj_f41_valuation_trajectory_mcaprerate_126d_base_v049_signal,
    f41vj_f41_valuation_trajectory_rerbreadth_126d_base_v050_signal,
    f41vj_f41_valuation_trajectory_rerdisp_252d_base_v051_signal,
    f41vj_f41_valuation_trajectory_rercomp_252d_base_v052_signal,
    f41vj_f41_valuation_trajectory_perichexh_504d_base_v053_signal,
    f41vj_f41_valuation_trajectory_evebrichexh_504d_base_v054_signal,
    f41vj_f41_valuation_trajectory_pscheapfloor_504d_base_v055_signal,
    f41vj_f41_valuation_trajectory_pbcheapfloor_504d_base_v056_signal,
    f41vj_f41_valuation_trajectory_pebandpos_504d_base_v057_signal,
    f41vj_f41_valuation_trajectory_evebbandposmom_504d_base_v058_signal,
    f41vj_f41_valuation_trajectory_pedisp_base_v059_signal,
    f41vj_f41_valuation_trajectory_psrerangeexp_base_v060_signal,
    f41vj_f41_valuation_trajectory_evebrevsnap_126d_base_v061_signal,
    f41vj_f41_valuation_trajectory_pevsps_rerspread_v062_signal,
    f41vj_f41_valuation_trajectory_perevgapz_252d_base_v063_signal,
    f41vj_f41_valuation_trajectory_psrevgapz_252d_base_v064_signal,
    f41vj_f41_valuation_trajectory_pbgapsignmag_252d_base_v065_signal,
    f41vj_f41_valuation_trajectory_pbsignmag_252d_base_v066_signal,
    f41vj_f41_valuation_trajectory_evpremrevgap_252d_base_v067_signal,
    f41vj_f41_valuation_trajectory_evpremz_252d_base_v068_signal,
    f41vj_f41_valuation_trajectory_evebpsgapmom_base_v069_signal,
    f41vj_f41_valuation_trajectory_psaccel_base_v070_signal,
    f41vj_f41_valuation_trajectory_perankmom_504d_base_v071_signal,
    f41vj_f41_valuation_trajectory_evebrankmom_504d_base_v072_signal,
    f41vj_f41_valuation_trajectory_pehitrate_252d_base_v073_signal,
    f41vj_f41_valuation_trajectory_evebhitrate_252d_base_v074_signal,
    f41vj_f41_valuation_trajectory_structtilt_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_VALUATION_TRAJECTORY_REGISTRY_001_075 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    pe = _fund(101, base=18.0, drift=0.03, vol=0.06).rename("pe")
    pb = _fund(102, base=2.5, drift=0.02, vol=0.05).rename("pb")
    ps = _fund(103, base=3.0, drift=0.025, vol=0.055).rename("ps")
    evebitda = _fund(104, base=11.0, drift=0.028, vol=0.05).rename("evebitda")
    ev = _fund(105, base=5e9, drift=0.03, vol=0.05).rename("ev")
    marketcap = _fund(106, base=4e9, drift=0.028, vol=0.05).rename("marketcap")
    return {
        "pe": pe, "pb": pb, "ps": ps,
        "evebitda": evebitda, "ev": ev, "marketcap": marketcap,
    }


if __name__ == "__main__":
    cols = _build_synth()

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f41_valuation_trajectory_base_001_075_claude: %d features pass" % n_features)
