# f15_ulcer_index_efficiency — REAL indicator: Ulcer Index & Ulcer Performance Index
#
# Ulcer Index UI(n) = sqrt( mean( drawdown_pct^2 ) ) over a window, where
#   drawdown_pct = 100 * (price - rolling_max) / rolling_max   (<= 0)
# Ulcer Performance Index (Martin ratio) = (return over n) / UI(n).
# All drawdown/price math uses 'closeadj' (windows used here are all > 21d).
#
# This file produces features 076..150 of the same deterministic recipe space
# used by the 001..075 file, so the two slices are disjoint and together cover
# 150 distinct (facet, window) variants across windows {21, 63, 126, 252, ...}:
# UI level, UPI/Martin ratio, UI z-score, UI slope/Delta, max drawdown depth,
# drawdown duration, pain index, recovery factor, return/UI efficiency, UI
# regime distance, short-vs-long UI spread, UI percentile rank.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------- helpers ----
def _z(s, w):
    """Rolling z-score of a series over window w."""
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    """Rolling rate-of-change (fractional) over w."""
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    """Per-bar slope of s over window w via endpoint delta."""
    return (s - s.shift(w)) / float(w)


def _pctrank(s, w):
    """Rolling percentile rank (0..1) of the last value within the window."""
    return s.rolling(w).apply(
        lambda a: (a <= a[-1]).mean() if np.isfinite(a[-1]) else np.nan, raw=True
    )


def _drawdown_pct(price, w):
    """drawdown_pct = 100*(price - rolling_max)/rolling_max over trailing window w."""
    rmax = price.rolling(w, min_periods=1).max()
    return (100.0 * (price - rmax) / rmax).replace([np.inf, -np.inf], np.nan)


def _ulcer_index(price, w):
    """UI(w) = sqrt( mean( drawdown_pct^2 ) ) over window w."""
    dd = _drawdown_pct(price, w)
    return np.sqrt((dd * dd).rolling(w).mean())


def _ret_over(price, w):
    """Total fractional return over window w (percent units)."""
    return 100.0 * (price / price.shift(w) - 1.0)


def _upi(price, w):
    """Ulcer Performance Index (Martin ratio) = return(w) / UI(w)."""
    ui = _ulcer_index(price, w)
    r = _ret_over(price, w)
    return (r / ui).replace([np.inf, -np.inf], np.nan)


def _max_dd_depth(price, w):
    """Deepest (most negative) drawdown_pct within window w; returned as positive depth."""
    dd = _drawdown_pct(price, w)
    return -dd.rolling(w).min()


def _pain_index(price, w):
    """Pain index = mean absolute drawdown over window w (positive)."""
    dd = _drawdown_pct(price, w)
    return (-dd).rolling(w).mean()


def _underwater_duration(price, w):
    """Time underwater: fraction of bars in window with strictly negative drawdown."""
    dd = _drawdown_pct(price, w)
    uw = (dd < 0).astype(float)
    return uw.rolling(w).mean()


def _recovery_factor(price, w):
    """Recovery factor = return(w) / max_drawdown_depth(w)."""
    r = _ret_over(price, w)
    mdd = _max_dd_depth(price, w)
    return (r / mdd).replace([np.inf, -np.inf], np.nan)


_WINS = [21, 63, 126, 252]


def _recipes():
    """Ordered list of (facet_name, window) producing exactly 150 distinct variants.

    Must match the 001..075 file so the two 75-feature slices are disjoint.
    """
    facets = [
        'ui_level',
        'upi',
        'ui_z',
        'ui_slope',
        'ui_delta',
        'max_dd',
        'uw_dur',
        'pain',
        'recovery',
        'eff',
        'regime',
        'spread',
        'pctrank',
        'ui_roc',
        'upi_z',
    ]
    recipes = []
    for f in facets:
        for w in _WINS:
            recipes.append((f, w))
    extra_wins = [10, 42, 189, 5, 84, 168]
    for f in facets:
        for w in extra_wins:
            recipes.append((f, w))
    return recipes


_RECIPES = _recipes()


def _compute_one(df, facet, w):
    """Compute a single facet/window Series using closeadj for all price math."""
    px = df['closeadj']
    ui = _ulcer_index(px, w)
    if facet == 'ui_level':
        return ui
    if facet == 'upi':
        return _upi(px, w)
    if facet == 'ui_z':
        return _z(ui, max(w, 21))
    if facet == 'ui_slope':
        return _slope(ui, max(w // 2, 5))
    if facet == 'ui_delta':
        return ui - ui.shift(w)
    if facet == 'max_dd':
        return _max_dd_depth(px, w)
    if facet == 'uw_dur':
        return _underwater_duration(px, w)
    if facet == 'pain':
        return _pain_index(px, w)
    if facet == 'recovery':
        return _recovery_factor(px, w)
    if facet == 'eff':
        return (_ret_over(px, w) / ui).replace([np.inf, -np.inf], np.nan)
    if facet == 'regime':
        return ui - ui.rolling(252, min_periods=21).mean()
    if facet == 'spread':
        longw = min(w * 3, 252) if w * 3 > w else 252
        ui_long = _ulcer_index(px, longw)
        return ui - ui_long
    if facet == 'pctrank':
        return _pctrank(ui, max(w, 63))
    if facet == 'ui_roc':
        return _roc(ui, max(w // 2, 5))
    if facet == 'upi_z':
        return _z(_upi(px, w), max(w, 21))
    return ui


def get_f15_ulcer_index_efficiency_base_076_150(df):
    features = {}
    for i in range(76, 151):
        facet, w = _RECIPES[i - 1]
        features[f'f15_ulcer_index_efficiency_{i:03d}'] = _compute_one(df, facet, w)
    return pd.DataFrame(features)
