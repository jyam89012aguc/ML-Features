# Real indicator: Bollinger Bands bandwidth & %B
#   middle = SMA_n ; upper/lower = middle +/- k*STD_n
#   bandwidth = (upper - lower)/middle = 2k*STD_n/SMA_n
#   %B = (price - lower)/(upper - lower)
# Facets: bandwidth level, %B position, bandwidth z-score (squeeze),
#   bandwidth percentile rank, bandwidth slope/delta (expansion),
#   %B extremes, band-walk streak, squeeze-then-expand flag,
#   bandwidth regime distance, short-vs-long bandwidth ratio, %B divergence.
import numpy as np
import pandas as pd

# Windows > 21d use 'closeadj'; <= 21d may use 'close'.
WINDOWS = [10, 20, 21, 50, 63, 126]
KS = [1.0, 2.0, 2.5, 3.0]


def _price(df, window):
    return df['closeadj'] if window > 21 else df['close']


def _bb_parts(price, n, k):
    mid = price.rolling(n).mean()
    sd = price.rolling(n).std()
    upper = mid + k * sd
    lower = mid - k * sd
    bw = (upper - lower) / mid
    pctb = (price - lower) / (upper - lower)
    bw = bw.replace([np.inf, -np.inf], np.nan)
    pctb = pctb.replace([np.inf, -np.inf], np.nan)
    return mid, sd, upper, lower, bw, pctb


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda a: (a <= a[-1]).sum() / len(a), raw=True)


def _streak_pos(cond):
    # length of current run of True values
    grp = (~cond).cumsum()
    return cond.groupby(grp).cumsum()


# Enumerate distinct (window, k, facet) variant specs.
# Facets cycle so that no two features are the same expression up to window only.
FACETS = [
    'bw_level', 'pctb_pos', 'bw_z', 'bw_pctile', 'bw_slope',
    'pctb_extreme_hi', 'pctb_extreme_lo', 'bandwalk_up', 'bandwalk_dn',
    'squeeze_expand', 'bw_regime_dist', 'bw_ratio_sl', 'pctb_diverg',
]


def _build_specs():
    specs = []
    fi = 0
    for n in WINDOWS:
        for k in KS:
            facet = FACETS[fi % len(FACETS)]
            specs.append((n, k, facet))
            fi += 1
    # Pad / extend to reach 150 by cycling windows+ks while rotating facets
    extra_combos = [(n, k) for n in WINDOWS for k in KS]
    ci = 0
    while len(specs) < 150:
        n, k = extra_combos[ci % len(extra_combos)]
        facet = FACETS[fi % len(FACETS)]
        specs.append((n, k, facet))
        fi += 1
        ci += 1
    return specs


_SPECS = _build_specs()


def _compute(df, n, k, facet):
    price = _price(df, n)
    mid, sd, upper, lower, bw, pctb = _bb_parts(price, n, k)

    if facet == 'bw_level':
        return bw
    if facet == 'pctb_pos':
        return pctb
    if facet == 'bw_z':
        return _z(bw, max(n, 20))
    if facet == 'bw_pctile':
        # low percentile == squeeze
        return _pctrank(bw, max(n * 2, 40))
    if facet == 'bw_slope':
        # expansion: change in bandwidth over n//4
        return bw.diff(max(n // 4, 1))
    if facet == 'pctb_extreme_hi':
        return (pctb > 1.0).astype(float)
    if facet == 'pctb_extreme_lo':
        return (pctb < 0.0).astype(float)
    if facet == 'bandwalk_up':
        return _streak_pos(pctb > 0.8).astype(float)
    if facet == 'bandwalk_dn':
        return _streak_pos(pctb < 0.2).astype(float)
    if facet == 'squeeze_expand':
        # was squeezed (low pctile) then bandwidth expanding now
        pr = _pctrank(bw, max(n * 2, 40))
        was_squeeze = (pr.shift(1) < 0.2).astype(float)
        expanding = (bw.diff() > 0).astype(float)
        return was_squeeze * expanding
    if facet == 'bw_regime_dist':
        # distance of current bw from its longer-run median (regime)
        med = bw.rolling(max(n * 2, 40)).median()
        return (bw - med).replace([np.inf, -np.inf], np.nan)
    if facet == 'bw_ratio_sl':
        # short-vs-long bandwidth ratio
        short_n = max(n // 2, 5)
        _, _, _, _, bw_s, _ = _bb_parts(price, short_n, k)
        return (bw_s / bw).replace([np.inf, -np.inf], np.nan)
    if facet == 'pctb_diverg':
        # %B vs price momentum divergence
        pctb_chg = pctb.diff(max(n // 4, 1))
        price_chg = price.pct_change(max(n // 4, 1))
        return (pctb_chg - price_chg).replace([np.inf, -np.inf], np.nan)
    return bw


def get_f20_bollinger_bandwidth_base_001_075(df):
    features = {}
    for i in range(1, 76):
        n, k, facet = _SPECS[i - 1]
        features[f'f20_bollinger_bandwidth_{i:03d}'] = _compute(df, n, k, facet)
    return pd.DataFrame(features)
