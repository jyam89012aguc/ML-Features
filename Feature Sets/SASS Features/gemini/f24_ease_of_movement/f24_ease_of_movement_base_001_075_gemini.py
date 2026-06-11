# Real indicator: Ease of Movement (EMV)
# distance_moved = (high+low)/2 - prior((high+low)/2)
# box_ratio     = (volume/scale) / (high-low)
# emv           = distance_moved / box_ratio
# smoothed emv  = SMA(n, emv)  (also EMA variants)
# Facets: EMV level, smoothed (SMA/EMA), z-score, slope/delta, sign streak,
#         price confirmation, cumulative, zero-cross, |EMV| magnitude,
#         short-vs-long spread, percentile rank, distance/box components.
import numpy as np
import pandas as pd

_SCALE = 1e8  # box-ratio volume scaling constant
_EPS = 1e-12


def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _emv_components(df):
    """Return (distance_moved, box_ratio, emv) raw series."""
    high = df['high'].astype(float)
    low = df['low'].astype(float)
    vol = df['volume'].astype(float)
    mid = (high + low) / 2.0
    dist = mid - mid.shift(1)
    rng = (high - low)
    box = (vol / _SCALE) / rng.replace(0.0, np.nan)
    emv = dist / box.replace(0.0, np.nan)
    return _safe(dist), _safe(box), _safe(emv)


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return _safe((s - m) / sd.replace(0.0, np.nan))


def _roc(s, w):
    return _safe(s / s.shift(w) - 1.0)


def _slope(s, w):
    return _safe((s - s.shift(w)) / float(w))


def _sign_streak(s):
    sign = np.sign(s.fillna(0.0))
    grp = (sign != sign.shift(1)).cumsum()
    streak = sign.groupby(grp).cumcount() + 1
    return (streak * sign).where(s.notna())


def _pct_rank(s, w):
    return s.rolling(w).apply(
        lambda x: (x.argsort().argsort()[-1] + 1) / len(x)
        if np.isfinite(x[-1]) else np.nan, raw=True)


def _zero_cross(s, w):
    sign = np.sign(s)
    crossed = (sign != sign.shift(1)).astype(float)
    return crossed.rolling(w).sum()


def get_f24_ease_of_movement_base_001_075(df):
    dist, box, emv = _emv_components(df)
    semv14 = emv.rolling(14).mean()
    semv21 = emv.rolling(21).mean()
    semv63 = emv.rolling(63).mean()
    semv126 = emv.rolling(126).mean()
    price_long = df['closeadj'].astype(float)

    f = {}
    # 001-004: EMV smoothed level (SMA) across windows
    f['f24_ease_of_movement_001'] = semv14
    f['f24_ease_of_movement_002'] = semv21
    f['f24_ease_of_movement_003'] = semv63
    f['f24_ease_of_movement_004'] = semv126
    # 005-008: smoothed EMV (EMA) across windows
    f['f24_ease_of_movement_005'] = emv.ewm(span=14, adjust=False).mean()
    f['f24_ease_of_movement_006'] = emv.ewm(span=21, adjust=False).mean()
    f['f24_ease_of_movement_007'] = emv.ewm(span=63, adjust=False).mean()
    f['f24_ease_of_movement_008'] = emv.ewm(span=126, adjust=False).mean()
    # 009-012: raw EMV level (lightly smoothed by 3 to denoise) - distinct from SMA(n)
    f['f24_ease_of_movement_009'] = emv.rolling(3).mean()
    f['f24_ease_of_movement_010'] = emv.rolling(5).mean()
    f['f24_ease_of_movement_011'] = emv.rolling(7).mean()
    f['f24_ease_of_movement_012'] = emv.rolling(10).mean()
    # 013-016: z-score of smoothed EMV
    f['f24_ease_of_movement_013'] = _z(semv14, 14)
    f['f24_ease_of_movement_014'] = _z(semv21, 21)
    f['f24_ease_of_movement_015'] = _z(semv63, 63)
    f['f24_ease_of_movement_016'] = _z(semv126, 126)
    # 017-020: z-score of raw EMV over windows
    f['f24_ease_of_movement_017'] = _z(emv, 14)
    f['f24_ease_of_movement_018'] = _z(emv, 21)
    f['f24_ease_of_movement_019'] = _z(emv, 63)
    f['f24_ease_of_movement_020'] = _z(emv, 126)
    # 021-024: slope of smoothed EMV
    f['f24_ease_of_movement_021'] = _slope(semv14, 5)
    f['f24_ease_of_movement_022'] = _slope(semv21, 5)
    f['f24_ease_of_movement_023'] = _slope(semv63, 10)
    f['f24_ease_of_movement_024'] = _slope(semv126, 21)
    # 025-028: delta (1-step change) of smoothed EMV
    f['f24_ease_of_movement_025'] = semv14.diff()
    f['f24_ease_of_movement_026'] = semv21.diff()
    f['f24_ease_of_movement_027'] = semv63.diff()
    f['f24_ease_of_movement_028'] = semv126.diff()
    # 029-032: EMV sign streak (raw and smoothed)
    f['f24_ease_of_movement_029'] = _sign_streak(emv)
    f['f24_ease_of_movement_030'] = _sign_streak(semv14)
    f['f24_ease_of_movement_031'] = _sign_streak(semv21)
    f['f24_ease_of_movement_032'] = _sign_streak(semv63)
    # 033-036: cumulative EMV over windows (rolling sum)
    f['f24_ease_of_movement_033'] = emv.rolling(14).sum()
    f['f24_ease_of_movement_034'] = emv.rolling(21).sum()
    f['f24_ease_of_movement_035'] = emv.rolling(63).sum()
    f['f24_ease_of_movement_036'] = emv.rolling(126).sum()
    # 037-040: EMV zero-cross frequency over windows
    f['f24_ease_of_movement_037'] = _zero_cross(emv, 14)
    f['f24_ease_of_movement_038'] = _zero_cross(emv, 21)
    f['f24_ease_of_movement_039'] = _zero_cross(emv, 63)
    f['f24_ease_of_movement_040'] = _zero_cross(emv, 126)
    # 041-044: |EMV| magnitude (mean of absolute over windows)
    f['f24_ease_of_movement_041'] = emv.abs().rolling(14).mean()
    f['f24_ease_of_movement_042'] = emv.abs().rolling(21).mean()
    f['f24_ease_of_movement_043'] = emv.abs().rolling(63).mean()
    f['f24_ease_of_movement_044'] = emv.abs().rolling(126).mean()
    # 045-047: short-vs-long smoothed EMV spread
    f['f24_ease_of_movement_045'] = semv14 - semv21
    f['f24_ease_of_movement_046'] = semv14 - semv63
    f['f24_ease_of_movement_047'] = semv21 - semv126
    # 048-051: EMV percentile rank over windows
    f['f24_ease_of_movement_048'] = _pct_rank(emv, 14)
    f['f24_ease_of_movement_049'] = _pct_rank(emv, 21)
    f['f24_ease_of_movement_050'] = _pct_rank(emv, 63)
    f['f24_ease_of_movement_051'] = _pct_rank(emv, 126)
    # 052-055: distance-moved component (smoothed) over windows
    f['f24_ease_of_movement_052'] = dist.rolling(14).mean()
    f['f24_ease_of_movement_053'] = dist.rolling(21).mean()
    f['f24_ease_of_movement_054'] = dist.rolling(63).mean()
    f['f24_ease_of_movement_055'] = dist.rolling(126).mean()
    # 056-059: box-ratio component (smoothed) over windows
    f['f24_ease_of_movement_056'] = box.rolling(14).mean()
    f['f24_ease_of_movement_057'] = box.rolling(21).mean()
    f['f24_ease_of_movement_058'] = box.rolling(63).mean()
    f['f24_ease_of_movement_059'] = box.rolling(126).mean()
    # 060-063: EMV vs price confirmation (sign agreement), >21d uses closeadj
    pret14 = df['close'].astype(float).pct_change(14)
    pret21 = df['close'].astype(float).pct_change(21)
    pret63 = price_long.pct_change(63)
    pret126 = price_long.pct_change(126)
    f['f24_ease_of_movement_060'] = _safe(np.sign(semv14) * np.sign(pret14))
    f['f24_ease_of_movement_061'] = _safe(np.sign(semv21) * np.sign(pret21))
    f['f24_ease_of_movement_062'] = _safe(np.sign(semv63) * np.sign(pret63))
    f['f24_ease_of_movement_063'] = _safe(np.sign(semv126) * np.sign(pret126))
    # 064-067: EMV roc (rate of change of smoothed EMV)
    f['f24_ease_of_movement_064'] = _roc(semv14, 5)
    f['f24_ease_of_movement_065'] = _roc(semv21, 5)
    f['f24_ease_of_movement_066'] = _roc(semv63, 10)
    f['f24_ease_of_movement_067'] = _roc(semv126, 21)
    # 068-071: cumulative EMV slope (accumulation/distribution line behaviour)
    cum = emv.cumsum()
    f['f24_ease_of_movement_068'] = _slope(cum, 14)
    f['f24_ease_of_movement_069'] = _slope(cum, 21)
    f['f24_ease_of_movement_070'] = _slope(cum, 63)
    f['f24_ease_of_movement_071'] = _slope(cum, 126)
    # 072-075: EMV dispersion (rolling std) over windows
    f['f24_ease_of_movement_072'] = emv.rolling(14).std()
    f['f24_ease_of_movement_073'] = emv.rolling(21).std()
    f['f24_ease_of_movement_074'] = emv.rolling(63).std()
    f['f24_ease_of_movement_075'] = emv.rolling(126).std()

    out = pd.DataFrame(f, index=df.index)
    out = out.replace([np.inf, -np.inf], np.nan)
    return out
