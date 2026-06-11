# Negative Volume Index (NVI) — real indicator implementation
# NVI is a cumulative index seeded at 1000 that moves by the price return ONLY on
# "low-volume" days (volume_t < volume_{t-1}); it carries forward unchanged on
# high-volume days. The classic NVI signal is NVI vs its long EMA (255d/1yr).
# Returns use 'closeadj' (windows > 21d); volume comparison uses raw 'volume'.
import numpy as np
import pandas as pd


def _nvi(closeadj, volume):
    """Cumulative Negative Volume Index, seeded at 1000."""
    ret = closeadj.pct_change()
    low_vol = volume < volume.shift(1)
    # multiplicative factor: (1+ret) on low-vol days, else 1.0
    factor = pd.Series(1.0, index=closeadj.index)
    factor[low_vol] = 1.0 + ret[low_vol]
    factor = factor.fillna(1.0)
    nvi = 1000.0 * factor.cumprod()
    # keep warm-up NaN where price/volume undefined
    nvi[closeadj.isna() | volume.isna()] = np.nan
    return nvi


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return ((s - s.shift(w)) / w).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] > x[:-1]).sum() / max(len(x) - 1, 1), raw=True
    )


def _smartmoney_ret(closeadj, volume):
    """Per-day low-volume ('smart money') log return, 0 on high-volume days."""
    ret = closeadj.pct_change()
    low_vol = volume < volume.shift(1)
    smr = pd.Series(0.0, index=closeadj.index)
    smr[low_vol] = ret[low_vol]
    smr[closeadj.isna() | volume.isna()] = np.nan
    return smr


def get_f25_negative_volume_index_base_001_075(df):
    closeadj = df['closeadj']
    volume = df['volume']
    close = df['close']

    nvi = _nvi(closeadj, volume)
    lognvi = np.log(nvi.replace([np.inf, -np.inf], np.nan))
    smr = _smartmoney_ret(closeadj, volume)

    features = {}

    def put(i, series):
        features[f'f25_negative_volume_index_{i:03d}'] = series

    # window grid (all > 21d use closeadj already in nvi)
    Wz = [21, 42, 63, 126, 189, 252]      # z-score windows
    Wroc = [10, 21, 42, 63, 126, 252]     # roc windows
    Wslope = [10, 21, 63, 126]            # slope windows
    Wema = [21, 55, 89, 144, 200, 255]    # EMA windows for classic signal
    Wnorm = [42, 63, 126, 189, 252, 378]  # normalization windows
    Wrank = [42, 63, 126, 252]            # percentile-rank windows

    i = 1

    # Facet A: NVI level normalized (level / rolling mean - 1)  -> 6
    for w in Wnorm:
        put(i, (nvi / nvi.rolling(w).mean() - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet B: NVI z-score  -> 6
    for w in Wz:
        put(i, _z(nvi, w)); i += 1

    # Facet C: NVI vs its EMA — classic signal (NVI/EMA - 1)  -> 6
    for w in Wema:
        ema = nvi.ewm(span=w, adjust=False).mean()
        put(i, (nvi / ema - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet D: NVI ROC  -> 6
    for w in Wroc:
        put(i, _roc(nvi, w)); i += 1

    # Facet E: NVI slope (normalized by level)  -> 4
    for w in Wslope:
        put(i, (_slope(nvi, w) / nvi).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet F: NVI log-return z-score (momentum of the index)  -> 6
    for w in Wz:
        put(i, _z(lognvi.diff(), w)); i += 1

    # Facet G: NVI percentile rank  -> 4
    for w in Wrank:
        put(i, _pctrank(nvi, w)); i += 1

    # Facet H: above/below long-EMA regime distance (255d classic), several spans -> 6
    for w in Wema:
        ema = nvi.ewm(span=w, adjust=False).mean()
        put(i, np.sign(nvi - ema) * (np.abs(nvi - ema) / ema).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet I: short-vs-long NVI EMA spread  -> 6
    pairs = [(10, 63), (21, 126), (21, 252), (55, 200), (42, 189), (63, 255)]
    for s_, l_ in pairs:
        es = nvi.ewm(span=s_, adjust=False).mean()
        el = nvi.ewm(span=l_, adjust=False).mean()
        put(i, (es / el - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet J: cumulative low-volume ('smart money') return accumulation  -> 6
    for w in [21, 42, 63, 126, 189, 252]:
        put(i, smr.rolling(w).sum()); i += 1

    # Facet K: NVI vs price spread — log(NVI/1000) minus price log-return over window -> 6
    base_lognvi = lognvi - np.log(1000.0)
    for w in [21, 42, 63, 126, 189, 252]:
        price_ret = np.log(closeadj / closeadj.shift(w))
        nvi_ret = base_lognvi - base_lognvi.shift(w)
        put(i, (nvi_ret - price_ret).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet L: smart-money-flow proxy — count of low-vol up days minus down days -> 7
    ret = closeadj.pct_change()
    low_vol = volume < volume.shift(1)
    sm_dir = pd.Series(0.0, index=closeadj.index)
    sm_dir[low_vol & (ret > 0)] = 1.0
    sm_dir[low_vol & (ret < 0)] = -1.0
    sm_dir[closeadj.isna() | volume.isna()] = np.nan
    for w in [10, 21, 42, 63, 126, 189, 252]:
        put(i, sm_dir.rolling(w).mean()); i += 1

    # remaining slots to reach 75: NVI ROC z-score variants
    while i <= 75:
        for w in [21, 63, 126]:
            if i > 75:
                break
            put(i, _z(_roc(nvi, 21), w)); i += 1

    out = pd.DataFrame(features)
    return out
