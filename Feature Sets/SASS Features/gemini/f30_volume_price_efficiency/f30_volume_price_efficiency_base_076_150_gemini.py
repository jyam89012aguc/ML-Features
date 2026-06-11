# f30_volume_price_efficiency — REAL indicator: volume-price efficiency / Amihud illiquidity
# Part 2 (features 076..150). Distinct facets from part 1: interactions, regimes,
# dispersion, rank trends, spreads, ratios, smoothed efficiency, signed-impact.
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
    return ((s - s.shift(w)) / float(w)).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda a: (a[:-1] < a[-1]).mean() if np.isfinite(a[-1]) else np.nan,
        raw=True,
    )


def _ret(df):
    return df['closeadj'].pct_change().replace([np.inf, -np.inf], np.nan)


def _dollar_vol(df):
    return (df['closeadj'] * df['volume']).replace([np.inf, -np.inf], np.nan)


def _amihud(df, w):
    dv = _dollar_vol(df)
    raw = (_ret(df).abs() / dv).replace([np.inf, -np.inf], np.nan)
    return (raw.rolling(w).mean() * 1e9)


def _eff_move_per_dollar(df, w):
    mv = df['closeadj'].diff().abs()
    dv = _dollar_vol(df)
    return (mv.rolling(w).sum() / dv.rolling(w).sum()).replace([np.inf, -np.inf], np.nan)


def _eff_netvsgross(df, w):
    d = df['closeadj'].diff()
    net = (df['closeadj'] - df['closeadj'].shift(w)).abs()
    gross_path = d.abs().rolling(w).sum()
    vw = (d.abs() * df['volume']).rolling(w).sum() / df['volume'].rolling(w).sum()
    return (net / gross_path * (vw / vw.rolling(w).mean())).replace(
        [np.inf, -np.inf], np.nan)


def _kyle_lambda(df, w):
    r = _ret(df)
    sv = (np.sign(df['closeadj'].diff()) * df['volume'])
    cov = r.rolling(w).cov(sv)
    var = sv.rolling(w).var()
    return ((cov / var) * 1e6).replace([np.inf, -np.inf], np.nan)


def _vol_per_move(df, w):
    mv = df['closeadj'].diff().abs()
    return (df['volume'].rolling(w).sum() / mv.rolling(w).sum() / 1e6).replace(
        [np.inf, -np.inf], np.nan)


_W = [21, 63, 126, 252]


def get_f30_volume_price_efficiency_base_076_150(df):
    features = {}

    amihud = {w: _amihud(df, w) for w in _W}
    eff_dollar = {w: _eff_move_per_dollar(df, w) for w in _W}
    eff_nvg = {w: _eff_netvsgross(df, w) for w in _W}
    kyle = {w: _kyle_lambda(df, w) for w in _W}
    vpm = {w: _vol_per_move(df, w) for w in _W}
    vol = {w: _ret(df).rolling(w).std() for w in _W}

    feats = []

    # 1) Kyle-lambda slope / Δ (4)
    for w in _W:
        feats.append(_slope(kyle[w], max(5, w // 3)))
    # 2) Kyle-lambda short-vs-long spread (3)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((kyle[a] - kyle[b]).replace([np.inf, -np.inf], np.nan))
    # 3) eff_dollar ROC (4)
    for w in _W:
        feats.append(_roc(eff_dollar[w], max(5, w // 3)))
    # 4) eff_dollar percentile rank trend (slope of rank) (4)
    for w in _W:
        feats.append(_slope(_pctrank(eff_dollar[w], w), max(5, w // 3)))
    # 5) eff_netvsgross level (4)
    for w in _W:
        feats.append(eff_nvg[w])
    # 6) eff_netvsgross slope (4)
    for w in _W:
        feats.append(_slope(eff_nvg[w], max(5, w // 3)))
    # 7) eff_netvsgross percentile rank (4)
    for w in _W:
        feats.append(_pctrank(eff_nvg[w], w))
    # 8) illiquidity regime distance: z of amihud vs 252 baseline (4)
    for w in _W:
        feats.append(((amihud[w] - amihud[w].rolling(252).mean())
                      / amihud[w].rolling(252).std()).replace([np.inf, -np.inf], np.nan))
    # 9) liquidity trend: ROC of vol_per_move (4)
    for w in _W:
        feats.append(_roc(vpm[w], max(5, w // 3)))
    # 10) vpm short-vs-long ratio (3)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((vpm[a] / vpm[b]).replace([np.inf, -np.inf], np.nan))
    # 11) amihud dispersion: rolling std of daily illiquidity (4)
    dv = _dollar_vol(df)
    illiq_daily = (_ret(df).abs() / dv * 1e9).replace([np.inf, -np.inf], np.nan)
    for w in _W:
        feats.append(illiq_daily.rolling(w).std())
    # 12) illiquidity x volatility interaction z-score (4)
    for w in _W:
        feats.append(_z((amihud[w] * vol[w] * 1e2).replace([np.inf, -np.inf], np.nan), w))
    # 13) signed price impact: Kyle x sign of recent return (4)
    for w in _W:
        feats.append((kyle[w] * np.sign(df['closeadj'] - df['closeadj'].shift(w))
                      ).replace([np.inf, -np.inf], np.nan))
    # 14) amihud smoothed (ema) level (4)
    for w in _W:
        feats.append(amihud[w].ewm(span=max(3, w // 4)).mean())
    # 15) eff_dollar x volatility interaction (4)
    for w in _W:
        feats.append((eff_dollar[w] * vol[w] * 1e3).replace([np.inf, -np.inf], np.nan))
    # 16) eff_dollar regime distance vs 252 mean (4)
    for w in _W:
        feats.append((eff_dollar[w] - eff_dollar[w].rolling(252).mean()).replace(
            [np.inf, -np.inf], np.nan))
    # 17) vpm percentile rank (4)
    for w in _W:
        feats.append(_pctrank(vpm[w], w))
    # 18) kyle percentile rank (4)
    for w in _W:
        feats.append(_pctrank(kyle[w], w))
    # 19) eff_nvg short-vs-long spread (3)
    for (a, b) in [(21, 63), (21, 126), (63, 252)]:
        feats.append((eff_nvg[a] - eff_nvg[b]).replace([np.inf, -np.inf], np.nan))
    # 20) amihud x amihud-dispersion interaction (2) -> total 75
    for w in (63, 252):
        feats.append((amihud[w] * illiq_daily.rolling(w).std()).replace(
            [np.inf, -np.inf], np.nan))

    feats = feats[:75]
    for k, s in enumerate(feats):
        i = 76 + k
        features[f'f30_volume_price_efficiency_{i:03d}'] = s
    return pd.DataFrame(features)
