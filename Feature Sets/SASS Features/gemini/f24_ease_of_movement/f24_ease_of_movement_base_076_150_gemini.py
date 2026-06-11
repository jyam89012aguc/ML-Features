# Real indicator: Ease of Movement (EMV) - features 076..150
# distance_moved = (high+low)/2 - prior((high+low)/2)
# box_ratio     = (volume/scale) / (high-low)
# emv           = distance_moved / box_ratio
# smoothed emv  = SMA(n, emv)  (also EMA variants)
# Facets continue the variant set with additional distinct expressions.
import numpy as np
import pandas as pd

_SCALE = 1e8
_EPS = 1e-12


def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _emv_components(df):
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


def get_f24_ease_of_movement_base_076_150(df):
    dist, box, emv = _emv_components(df)
    semv14 = emv.rolling(14).mean()
    semv21 = emv.rolling(21).mean()
    semv63 = emv.rolling(63).mean()
    semv126 = emv.rolling(126).mean()
    emv14 = emv.ewm(span=14, adjust=False).mean()
    emv21 = emv.ewm(span=21, adjust=False).mean()
    emv63 = emv.ewm(span=63, adjust=False).mean()
    emv126 = emv.ewm(span=126, adjust=False).mean()
    price_long = df['closeadj'].astype(float)

    f = {}
    # 076-079: EMA z-score (distinct from SMA z-score in file 1)
    f['f24_ease_of_movement_076'] = _z(emv14, 14)
    f['f24_ease_of_movement_077'] = _z(emv21, 21)
    f['f24_ease_of_movement_078'] = _z(emv63, 63)
    f['f24_ease_of_movement_079'] = _z(emv126, 126)
    # 080-083: short-vs-long EMV ratio (spread already in file1; here ratio)
    f['f24_ease_of_movement_080'] = _safe(semv14 / semv63.replace(0.0, np.nan))
    f['f24_ease_of_movement_081'] = _safe(semv21 / semv126.replace(0.0, np.nan))
    f['f24_ease_of_movement_082'] = _safe(emv14 / emv63.replace(0.0, np.nan))
    f['f24_ease_of_movement_083'] = _safe(emv21 / emv126.replace(0.0, np.nan))
    # 084-087: EMA short-vs-long spread
    f['f24_ease_of_movement_084'] = emv14 - emv21
    f['f24_ease_of_movement_085'] = emv14 - emv63
    f['f24_ease_of_movement_086'] = emv21 - emv126
    f['f24_ease_of_movement_087'] = emv63 - emv126
    # 088-091: smoothed |EMV| magnitude via EMA windows
    f['f24_ease_of_movement_088'] = emv.abs().ewm(span=14, adjust=False).mean()
    f['f24_ease_of_movement_089'] = emv.abs().ewm(span=21, adjust=False).mean()
    f['f24_ease_of_movement_090'] = emv.abs().ewm(span=63, adjust=False).mean()
    f['f24_ease_of_movement_091'] = emv.abs().ewm(span=126, adjust=False).mean()
    # 092-095: distance-moved z-score over windows
    f['f24_ease_of_movement_092'] = _z(dist, 14)
    f['f24_ease_of_movement_093'] = _z(dist, 21)
    f['f24_ease_of_movement_094'] = _z(dist, 63)
    f['f24_ease_of_movement_095'] = _z(dist, 126)
    # 096-099: box-ratio z-score over windows
    f['f24_ease_of_movement_096'] = _z(box, 14)
    f['f24_ease_of_movement_097'] = _z(box, 21)
    f['f24_ease_of_movement_098'] = _z(box, 63)
    f['f24_ease_of_movement_099'] = _z(box, 126)
    # 100-103: EMV percentile rank of smoothed EMV
    f['f24_ease_of_movement_100'] = _pct_rank(semv14, 14)
    f['f24_ease_of_movement_101'] = _pct_rank(semv21, 21)
    f['f24_ease_of_movement_102'] = _pct_rank(semv63, 63)
    f['f24_ease_of_movement_103'] = _pct_rank(semv126, 126)
    # 104-107: cumulative EMV level over windows (vs cumsum slope in file1)
    cum = emv.cumsum()
    f['f24_ease_of_movement_104'] = cum - cum.shift(14)
    f['f24_ease_of_movement_105'] = cum - cum.shift(21)
    f['f24_ease_of_movement_106'] = cum - cum.shift(63)
    f['f24_ease_of_movement_107'] = cum - cum.shift(126)
    # 108-111: EMV zero-cross on smoothed EMV
    f['f24_ease_of_movement_108'] = _zero_cross(semv14, 14)
    f['f24_ease_of_movement_109'] = _zero_cross(semv21, 21)
    f['f24_ease_of_movement_110'] = _zero_cross(semv63, 63)
    f['f24_ease_of_movement_111'] = _zero_cross(semv126, 126)
    # 112-115: EMV sign streak of EMA-smoothed EMV / longer
    f['f24_ease_of_movement_112'] = _sign_streak(semv126)
    f['f24_ease_of_movement_113'] = _sign_streak(emv14)
    f['f24_ease_of_movement_114'] = _sign_streak(emv63)
    f['f24_ease_of_movement_115'] = _sign_streak(emv126)
    # 116-119: EMV slope of EMA-smoothed EMV
    f['f24_ease_of_movement_116'] = _slope(emv14, 5)
    f['f24_ease_of_movement_117'] = _slope(emv21, 5)
    f['f24_ease_of_movement_118'] = _slope(emv63, 10)
    f['f24_ease_of_movement_119'] = _slope(emv126, 21)
    # 120-123: EMV-vs-price confirmation magnitude (signed product of strengths)
    pret14 = df['close'].astype(float).pct_change(14)
    pret21 = df['close'].astype(float).pct_change(21)
    pret63 = price_long.pct_change(63)
    pret126 = price_long.pct_change(126)
    f['f24_ease_of_movement_120'] = _safe(_z(semv14, 14) * _z(pret14, 14))
    f['f24_ease_of_movement_121'] = _safe(_z(semv21, 21) * _z(pret21, 21))
    f['f24_ease_of_movement_122'] = _safe(_z(semv63, 63) * _z(pret63, 63))
    f['f24_ease_of_movement_123'] = _safe(_z(semv126, 126) * _z(pret126, 126))
    # 124-127: distance/box component ratio (raw EMV is dist/box; here dist*box-ish variants)
    f['f24_ease_of_movement_124'] = _safe(dist.rolling(14).mean() / box.rolling(14).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_125'] = _safe(dist.rolling(21).mean() / box.rolling(21).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_126'] = _safe(dist.rolling(63).mean() / box.rolling(63).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_127'] = _safe(dist.rolling(126).mean() / box.rolling(126).mean().replace(0.0, np.nan))
    # 128-131: EMV roc on raw EMV (cumulative smoothing via short SMA)
    e3 = emv.rolling(3).mean()
    f['f24_ease_of_movement_128'] = _roc(e3, 14)
    f['f24_ease_of_movement_129'] = _roc(e3, 21)
    f['f24_ease_of_movement_130'] = _roc(e3, 63)
    f['f24_ease_of_movement_131'] = _roc(e3, 126)
    # 132-135: EMV dispersion ratio short/long (volatility regime of ease)
    s14 = emv.rolling(14).std()
    s21 = emv.rolling(21).std()
    s63 = emv.rolling(63).std()
    s126 = emv.rolling(126).std()
    f['f24_ease_of_movement_132'] = _safe(s14 / s63.replace(0.0, np.nan))
    f['f24_ease_of_movement_133'] = _safe(s21 / s126.replace(0.0, np.nan))
    f['f24_ease_of_movement_134'] = _safe(s14 / s21.replace(0.0, np.nan))
    f['f24_ease_of_movement_135'] = _safe(s63 / s126.replace(0.0, np.nan))
    # 136-139: positive-EMV fraction over windows (ease-of-up dominance)
    pos = (emv > 0).astype(float).where(emv.notna())
    f['f24_ease_of_movement_136'] = pos.rolling(14).mean()
    f['f24_ease_of_movement_137'] = pos.rolling(21).mean()
    f['f24_ease_of_movement_138'] = pos.rolling(63).mean()
    f['f24_ease_of_movement_139'] = pos.rolling(126).mean()
    # 140-143: smoothed EMV normalized by |EMV| magnitude (signal-to-activity)
    f['f24_ease_of_movement_140'] = _safe(semv14 / emv.abs().rolling(14).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_141'] = _safe(semv21 / emv.abs().rolling(21).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_142'] = _safe(semv63 / emv.abs().rolling(63).mean().replace(0.0, np.nan))
    f['f24_ease_of_movement_143'] = _safe(semv126 / emv.abs().rolling(126).mean().replace(0.0, np.nan))
    # 144-147: distance-moved slope (price-mid momentum used in EMV)
    f['f24_ease_of_movement_144'] = _slope(dist.rolling(14).mean(), 5)
    f['f24_ease_of_movement_145'] = _slope(dist.rolling(21).mean(), 5)
    f['f24_ease_of_movement_146'] = _slope(dist.rolling(63).mean(), 10)
    f['f24_ease_of_movement_147'] = _slope(dist.rolling(126).mean(), 21)
    # 148-150: EMV threshold/regime distance (smoothed EMV minus its rolling median)
    f['f24_ease_of_movement_148'] = _safe(semv14 - semv14.rolling(63).median())
    f['f24_ease_of_movement_149'] = _safe(semv21 - semv21.rolling(126).median())
    f['f24_ease_of_movement_150'] = _safe(semv63 - semv63.rolling(126).median())

    out = pd.DataFrame(f, index=df.index)
    out = out.replace([np.inf, -np.inf], np.nan)
    return out
