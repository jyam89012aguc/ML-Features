# Real indicator: volume-weighted rate of change / momentum
# Core: ROC(n) = closeadj.pct_change(n), weighted by relative volume (volume / SMA_volume).
# Windows > 21d use 'closeadj' for returns; raw 'volume' for weights; closeadj*volume = dollar-volume.
import numpy as np
import pandas as pd

WINDOWS = [5, 10, 21, 63, 126, 252]


def _ret_col(window):
    # rolling windows > 21d use closeadj; <=21d may use raw close
    return 'close' if window <= 21 else 'closeadj'


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(price, n):
    return price.pct_change(n).replace([np.inf, -np.inf], np.nan)


def _relvol(volume, window):
    sv = volume.rolling(window).mean()
    return (volume / sv).replace([np.inf, -np.inf], np.nan)


def _vw_roc(df, n):
    # volume-weighted ROC = ROC(n) * relative-volume
    price = df[_ret_col(n)]
    rv = _relvol(df['volume'], n)
    return (_roc(price, n) * rv).replace([np.inf, -np.inf], np.nan)


def _vw_momentum(df, n):
    # Sum of daily ret * relative-volume over the window
    price = df[_ret_col(n)]
    ret = price.pct_change().replace([np.inf, -np.inf], np.nan)
    rv = _relvol(df['volume'], n)
    return (ret * rv).rolling(n).sum()


def _dollar_vw_roc(df, n):
    # dollar-volume-weighted ROC: ROC * (dollar-volume / SMA dollar-volume)
    price = df[_ret_col(n)]
    dv = df['closeadj'] * df['volume']
    sdv = dv.rolling(n).mean()
    rel = (dv / sdv).replace([np.inf, -np.inf], np.nan)
    return (_roc(price, n) * rel).replace([np.inf, -np.inf], np.nan)


def _volzscore_roc(df, n):
    # ROC weighted by volume z-score
    price = df[_ret_col(n)]
    vz = _z(df['volume'], n)
    return (_roc(price, n) * vz).replace([np.inf, -np.inf], np.nan)


def get_f27_volume_weighted_roc_base_001_075(df):
    features = {}
    f = {}

    # Build the family of distinct facets, then map them onto i=001..075.
    # Facet builders keyed by window.
    for w in WINDOWS:
        # 1. volume-weighted ROC level
        f[('vw_roc', w)] = _vw_roc(df, w)
        # 2. volume-weighted momentum (Sigma ret*relvol)
        f[('vw_mom', w)] = _vw_momentum(df, w)
        # 3. relative-volume-confirmed ROC: keep ROC only when relvol>1, else damp by 0.25x
        rv = _relvol(df['volume'], w)
        roc = _roc(df[_ret_col(w)], w)
        conf = np.where(rv > 1.0, 1.0, 0.25)
        f[('rv_conf_roc', w)] = (roc * pd.Series(conf, index=roc.index)).replace([np.inf, -np.inf], np.nan)
        # 4. dollar-volume-weighted ROC
        f[('dv_roc', w)] = _dollar_vw_roc(df, w)
        # 5. ROC weighted by volume z-score
        f[('volz_roc', w)] = _volzscore_roc(df, w)
        # 6. vw-ROC z-score
        f[('vwroc_z', w)] = _z(_vw_roc(df, w), max(w, 21))
        # 7. vw-ROC slope/delta (change in vw-ROC)
        f[('vwroc_d', w)] = _vw_roc(df, w).diff(max(1, w // 3))
        # 8. volume-weighted vs plain ROC divergence
        f[('vw_div', w)] = (_vw_roc(df, w) - roc).replace([np.inf, -np.inf], np.nan)
        # 9. volume-weighted ROC sign streak
        sign = np.sign(_vw_roc(df, w))
        grp = (sign != sign.shift()).cumsum()
        f[('vwroc_streak', w)] = (sign * sign.groupby(grp).cumcount().add(1))
        # 10. vw-ROC percentile rank
        f[('vwroc_rank', w)] = _vw_roc(df, w).rolling(max(w, 21)).rank(pct=True)
        # 11. volume-confirmed breakout strength: vw-ROC * sign(price - rolling max approach)
        price = df[_ret_col(w)]
        hh = price.rolling(w).max()
        bo = ((price - hh.shift(1)) / hh.shift(1)).replace([np.inf, -np.inf], np.nan)
        f[('vw_breakout', w)] = (_vw_roc(df, w) * (1 + bo.clip(lower=0))).replace([np.inf, -np.inf], np.nan)
        # 12. dispersion of vw-ROC
        f[('vwroc_std', w)] = _vw_roc(df, w).rolling(max(w, 21)).std()

    # short-vs-long vw-ROC spreads (cross-window facet)
    spreads = {}
    pairs = [(5, 21), (10, 63), (21, 126), (63, 252), (5, 63), (10, 252)]
    for (s, l) in pairs:
        spreads[(s, l)] = (_vw_roc(df, s) - _vw_roc(df, l)).replace([np.inf, -np.inf], np.nan)

    # Flatten facets into an ordered list, then assign to columns 001..150.
    ordered = []
    facet_order = ['vw_roc', 'vw_mom', 'rv_conf_roc', 'dv_roc', 'volz_roc',
                   'vwroc_z', 'vwroc_d', 'vw_div', 'vwroc_streak', 'vwroc_rank',
                   'vw_breakout', 'vwroc_std']
    for fac in facet_order:
        for w in WINDOWS:
            ordered.append(f[(fac, w)])
    # 12 facets * 6 windows = 72
    for (s, l) in pairs:
        ordered.append(spreads[(s, l)])  # +6 = 78 total available

    # File 1 takes the first 75.
    for idx in range(75):
        features[f'f27_volume_weighted_roc_{idx + 1:03d}'] = ordered[idx]

    return pd.DataFrame(features)
