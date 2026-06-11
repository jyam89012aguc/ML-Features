# f30_volume_price_efficiency — REAL indicator: volume-price efficiency / Amihud illiquidity
# Core: price impact per unit volume.
#   Amihud illiquidity = mean(|daily_return| / dollar_volume) over n
#   volume-price efficiency = |price change| per unit volume (move per unit traded)
# Returns use closeadj (windows > 21d), raw volume, dollar-volume = closeadj * volume.
import numpy as np
import pandas as pd


# ---------------------------------------------------------------- helpers
def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    # per-bar linear slope = (level - level w bars ago) / w
    return ((s - s.shift(w)) / float(w)).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda a: (a[:-1] < a[-1]).mean() if np.isfinite(a[-1]) else np.nan,
        raw=True,
    )


def _ret(df):
    # daily simple return on closeadj (adjusted, safe for >21d windows)
    return df['closeadj'].pct_change().replace([np.inf, -np.inf], np.nan)


def _dollar_vol(df):
    return (df['closeadj'] * df['volume']).replace([np.inf, -np.inf], np.nan)


def _amihud(df, w):
    # classic Amihud illiquidity: mean(|ret| / dollar_volume) over window, scaled
    dv = _dollar_vol(df)
    raw = (_ret(df).abs() / dv).replace([np.inf, -np.inf], np.nan)
    return (raw.rolling(w).mean() * 1e9)


def _eff_move_per_dollar(df, w):
    # price-move-per-dollar-volume: cumulative |move| per cumulative dollar volume
    mv = df['closeadj'].diff().abs()
    dv = _dollar_vol(df)
    return (mv.rolling(w).sum() / dv.rolling(w).sum()).replace([np.inf, -np.inf], np.nan)


def _eff_netvsgross(df, w):
    # efficiency = |net move| / sum(|moves|), volume-weighted gross path
    d = df['closeadj'].diff()
    net = (df['closeadj'] - df['closeadj'].shift(w)).abs()
    gross = (d.abs() * df['volume']).rolling(w).sum() / df['volume'].rolling(w).sum()
    gross_path = d.abs().rolling(w).sum()
    return (net / gross_path * (gross / gross.rolling(w).mean())).replace(
        [np.inf, -np.inf], np.nan)


def _kyle_lambda(df, w):
    # Kyle-lambda style: rolling regression slope of return on signed volume
    r = _ret(df)
    sv = (np.sign(df['closeadj'].diff()) * df['volume'])
    cov = r.rolling(w).cov(sv)
    var = sv.rolling(w).var()
    return ((cov / var) * 1e6).replace([np.inf, -np.inf], np.nan)


def _vol_per_move(df, w):
    # inverse efficiency: volume traded per unit absolute price move
    mv = df['closeadj'].diff().abs()
    return (df['volume'].rolling(w).sum() / mv.rolling(w).sum() / 1e6).replace(
        [np.inf, -np.inf], np.nan)


# Window pool used to assign distinct windows across facets
_W = [21, 63, 126, 252]


def get_f30_volume_price_efficiency_base_001_075(df):
    features = {}

    # Precompute core illiquidity / efficiency series per window
    amihud = {w: _amihud(df, w) for w in _W}
    eff_dollar = {w: _eff_move_per_dollar(df, w) for w in _W}
    eff_nvg = {w: _eff_netvsgross(df, w) for w in _W}
    kyle = {w: _kyle_lambda(df, w) for w in _W}
    vpm = {w: _vol_per_move(df, w) for w in _W}

    feats = []  # ordered list of (series); we slice 75

    # 1) Amihud illiquidity level  (4 windows)
    for w in _W:
        feats.append(amihud[w])
    # 2) price-move-per-dollar-volume level (4)
    for w in _W:
        feats.append(eff_dollar[w])
    # 3) efficiency = |net|/Σ|moves| vol-weighted (4)
    for w in _W:
        feats.append(eff_nvg[w])
    # 4) Kyle-lambda regression (4)
    for w in _W:
        feats.append(kyle[w])
    # 5) volume-per-unit-price-move inverse (4)
    for w in _W:
        feats.append(vpm[w])
    # 6) Amihud z-score (4)
    for w in _W:
        feats.append(_z(amihud[w], w))
    # 7) Amihud slope / Δ (4)
    for w in _W:
        feats.append(_slope(amihud[w], max(5, w // 3)))
    # 8) Amihud ROC (4)
    for w in _W:
        feats.append(_roc(amihud[w], max(5, w // 3)))
    # 9) efficiency (dollar) percentile rank (4)
    for w in _W:
        feats.append(_pctrank(eff_dollar[w], w))
    # 10) illiquidity regime / threshold distance: level vs its own long mean (4)
    for w in _W:
        feats.append((amihud[w] - amihud[w].rolling(252).mean()).replace(
            [np.inf, -np.inf], np.nan))
    # 11) liquidity trend: slope of (inverse illiquidity) i.e. vol_per_move (4)
    for w in _W:
        feats.append(_slope(vpm[w], max(5, w // 3)))
    # 12) short-vs-long illiquidity spread (amihud short - long) (3 pairs)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((amihud[a] - amihud[b]).replace([np.inf, -np.inf], np.nan))
    # 13) short/long illiquidity ratio (3 pairs)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((amihud[a] / amihud[b]).replace([np.inf, -np.inf], np.nan))
    # 14) illiquidity x volatility interaction (4)
    vol = {w: _ret(df).rolling(w).std() for w in _W}
    for w in _W:
        feats.append((amihud[w] * vol[w] * 1e2).replace([np.inf, -np.inf], np.nan))
    # 15) efficiency netvsgross z-score (4)
    for w in _W:
        feats.append(_z(eff_nvg[w], w))
    # 16) Kyle-lambda z-score (4)
    for w in _W:
        feats.append(_z(kyle[w], w))
    # 17) eff_dollar slope (4)
    for w in _W:
        feats.append(_slope(eff_dollar[w], max(5, w // 3)))
    # 18) eff_dollar short-vs-long spread (3)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((eff_dollar[a] - eff_dollar[b]).replace([np.inf, -np.inf], np.nan))
    # 19) amihud percentile rank (4)
    for w in _W:
        feats.append(_pctrank(amihud[w], w))
    # 20) vpm z-score (4) -> brings total to 75
    for w in _W:
        feats.append(_z(vpm[w], w))

    feats = feats[:75]
    for i, s in enumerate(feats, start=1):
        features[f'f30_volume_price_efficiency_{i:03d}'] = s
    return pd.DataFrame(features)
