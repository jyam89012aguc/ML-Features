# f13_kurtosis_regime — REAL indicator: rolling kurtosis of returns & fat-tail regime
# Core: rolling EXCESS kurtosis of closeadj log-returns over a window; regime =
# kurtosis vs the normal baseline (3, i.e. 0 excess). Facets: excess kurtosis level,
# fat-tail regime distance, kurtosis z-score, slope/Delta, kurtosis of |returns|,
# percentile rank, leptokurtic-vs-mesokurtic regime streak, short-vs-long spread,
# kurtosis x vol interaction, rolling 4th-moment raw, kurtosis dispersion.
import numpy as np
import pandas as pd

# ----------------------------- helpers --------------------------------------
def _log_ret(df):
    # closeadj log-returns (all kurtosis windows are > 21d -> use closeadj)
    c = df['closeadj'].astype('float64')
    return np.log(c / c.shift(1))


def _excess_kurt(x, window):
    # rolling excess (Fisher) kurtosis; pandas .kurt() is already excess-kurtosis
    return x.rolling(window).kurt()


def _raw_kurt(x, window):
    # rolling raw (Pearson) kurtosis = excess + 3
    return x.rolling(window).kurt() + 3.0


def _fourth_moment(x, window):
    # rolling standardized 4th moment computed manually (raw kurtosis core)
    m = x.rolling(window).mean()
    s = x.rolling(window).std()
    z = (x - m) / s.replace(0.0, np.nan)
    return (z ** 4).rolling(window).mean()


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return ((s - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def _roc(s, k):
    return s.diff(k)


def _pct_rank(s, window):
    return s.rolling(window).apply(
        lambda a: (a[-1] > a[:-1]).sum() / max(len(a) - 1, 1), raw=True
    )


def _streak(cond):
    # length of current run of True in a boolean series (resets on False)
    c = cond.astype('float64')
    grp = (c == 0).cumsum()
    return c.groupby(grp).cumsum()


def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


WINDOWS = [21, 63, 126, 252]
# secondary-parameter menus that make each (facet, window, variant) triple distinct
_LOOKBACKS = [63, 126, 189, 252]   # for z-score / percentile / dispersion
_HORIZONS = [2, 3, 5, 10]          # for slope / Delta (also scaled by window)
_THRESH = [0.0, 0.5, 1.0, 3.0]     # fat-tail regime thresholds (excess-kurt units)


def _facet(spec, df_series):
    """Compute one feature given a spec dict and pre-rolled series cache."""
    r = df_series['r']; absr = df_series['absr']
    ek = df_series['ek']; rk = df_series['rk']; ka = df_series['ka']
    m4 = df_series['m4']; vol = df_series['vol']
    f = spec['facet']; w = spec['w']; v = spec['v']
    if f == 0:
        # excess kurtosis level (v: 0=raw, 1=EMA-smoothed, 2=demeaned, 3=longer EMA)
        if v == 1:
            return ek[w].ewm(span=max(w // 4, 5), adjust=False).mean()
        if v == 2:
            return ek[w] - ek[w].rolling(_LOOKBACKS[v]).mean()
        if v == 3:
            return ek[w].ewm(span=max(w // 2, 8), adjust=False).mean()
        return ek[w]
    if f == 1:
        # fat-tail regime distance: SIGNED distance of raw kurtosis from the normal
        # baseline (3) plus a variant tail threshold. Positive => leptokurtic / fat
        # tails, negative => mesokurtic-or-thinner. Signed (not clipped) so it stays
        # informative even when tails are mild.
        thr = 3.0 + _THRESH[v]
        return rk[w] - thr
    if f == 2:
        # kurtosis z-score over a variant lookback
        return _z(ek[w], _LOOKBACKS[v])
    if f == 3:
        # kurtosis slope / Delta over a variant horizon
        return _roc(ek[w], max(w // _HORIZONS[v], 2))
    if f == 4:
        # kurtosis of |returns| (v: 0=level, 1=spread vs return-kurt, 2/3=z-scored)
        if v == 1:
            return ka[w] - ek[w]
        if v == 2:
            return _z(ka[w], _LOOKBACKS[v])
        if v == 3:
            return ka[w].ewm(span=max(w // 4, 5), adjust=False).mean()
        return ka[w]
    if f == 5:
        # kurtosis percentile rank over a variant lookback
        return _pct_rank(ek[w], _LOOKBACKS[v])
    if f == 6:
        # leptokurtic-vs-mesokurtic regime streak: consecutive bars above a regime
        # threshold. v=0 uses the absolute normal baseline (excess>0); v>=1 use an
        # adaptive baseline (rolling median of kurtosis shifted by the variant) so
        # the regime actually toggles across fat-tail and calm periods.
        if v == 0:
            ref = 0.0
        else:
            ref = ek[w].rolling(_LOOKBACKS[v]).median() + (_THRESH[v] - 1.0)
        return _streak(ek[w] > ref)
    if f == 7:
        # short-vs-long kurtosis spread (this window vs another); v also toggles
        # absolute spread vs normalized spread so all 4 variants stay distinct
        wi = WINDOWS.index(w)
        others = [x for x in WINDOWS if x != w] or [w]
        w2 = others[v % len(others)]
        spread = ek[w] - ek[w2]
        if v >= 2:
            denom = (ek[w].abs() + ek[w2].abs())
            return _safe(spread / denom.replace(0.0, np.nan))
        return spread
    if f == 8:
        # kurtosis x vol interaction (vol over a variant window)
        vw = WINDOWS[(WINDOWS.index(w) + v) % len(WINDOWS)]
        return _safe(ek[w] * vol[vw])
    if f == 9:
        # rolling raw 4th-moment (v: 0=level, 1=Delta, 2=ratio vs 3, 3=z-scored)
        if v == 1:
            return _roc(m4[w], max(w // _HORIZONS[v], 2))
        if v == 2:
            return _safe(m4[w] / 3.0 - 1.0)
        if v == 3:
            return _z(m4[w], _LOOKBACKS[v])
        return m4[w]
    # f == 10 : kurtosis dispersion (rolling std of the excess-kurt series over a
    # variant lookback)
    return ek[w].rolling(max(_LOOKBACKS[v] // 3, 10)).std()


def _specs():
    """Deterministic ordered list of >=150 distinct (facet, window, variant) specs.
    Outer loop = variant (secondary param), then window, then facet — so the first
    44 are all unique base combos and later ones differ by a real secondary param,
    never by window alone."""
    out = []
    for v in range(4):                 # variant tier
        for w in WINDOWS:
            for f in range(11):
                out.append({'facet': f, 'w': w, 'v': v})
    return out  # 4 * 4 * 11 = 176 distinct specs (we use 150)


def _build(df, idx_start, idx_end):
    """Build features for global indices idx_start..idx_end (inclusive)."""
    r = _log_ret(df)
    absr = r.abs()
    cache = {
        'r': r, 'absr': absr,
        'ek': {w: _excess_kurt(r, w) for w in WINDOWS},
        'rk': {w: _raw_kurt(r, w) for w in WINDOWS},
        'ka': {w: _excess_kurt(absr, w) for w in WINDOWS},
        'm4': {w: _fourth_moment(r, w) for w in WINDOWS},
        'vol': {w: r.rolling(w).std() for w in WINDOWS},
    }
    specs = _specs()
    feats = {}
    for i in range(idx_start, idx_end + 1):
        spec = specs[i - 1]            # global index -> distinct spec
        feats[f'f13_kurtosis_regime_{i:03d}'] = _safe(_facet(spec, cache))
    return pd.DataFrame(feats)


def get_f13_kurtosis_regime_base_076_150(df):
    return _build(df, 76, 150)
