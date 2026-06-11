import pandas as pd
import numpy as np

# Helpers
def _sma(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=w//2 if w>1 else 1, adjust=False).mean()
def _z(s, w):
    rolling = s.rolling(w, min_periods=w//2 if w>1 else 1)
    return (s - rolling.mean()) / rolling.std().replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).min()
def _max(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).max()
def _skew(s, w): return s.rolling(w, min_periods=w//2 if w>2 else 3).skew()

# Domain Primitives
def _vol_regime_rank(v, w):
    return v.rolling(w, min_periods=w//2 if w>1 else 1).rank(pct=True)

def _vol_stability(v, w):
    return v.rolling(w, min_periods=w//2 if w>1 else 1).mean() / v.rolling(w, min_periods=w//2 if w>1 else 1).std().replace(0, np.nan)

def _vol_shock_score(v, w):
    return v / v.rolling(w, min_periods=w//2 if w>1 else 1).max().replace(0, np.nan)

# Features 001-015: Volume Regime Rank Jerk
# Jerk of volume percentile rank (5d) over 5d
def f27vr_f27_volume_regime_rank_5d_jerk_v001_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 5)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (10d) over 5d
def f27vr_f27_volume_regime_rank_10d_jerk_v002_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 10)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (21d) over 5d
def f27vr_f27_volume_regime_rank_21d_jerk_v003_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 21)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (42d) over 21d
def f27vr_f27_volume_regime_rank_42d_jerk_v004_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 42)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (63d) over 21d
def f27vr_f27_volume_regime_rank_63d_jerk_v005_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (126d) over 21d
def f27vr_f27_volume_regime_rank_126d_jerk_v006_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (252d) over 63d
def f27vr_f27_volume_regime_rank_252d_jerk_v007_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 252)
    return res.diff(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (30d) over 5d
def f27vr_f27_volume_regime_rank_30d_jerk_v008_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 30)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (90d) over 21d
def f27vr_f27_volume_regime_rank_90d_jerk_v009_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 90)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (180d) over 21d
def f27vr_f27_volume_regime_rank_180d_jerk_v010_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 180)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (200d) over 63d
def f27vr_f27_volume_regime_rank_200d_jerk_v011_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 200)
    return res.diff(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (3d) over 2d
def f27vr_f27_volume_regime_rank_3d_jerk_v012_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 3)
    return res.diff(2).diff(2).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (7d) over 5d
def f27vr_f27_volume_regime_rank_7d_jerk_v013_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 7)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (14d) over 5d
def f27vr_f27_volume_regime_rank_14d_jerk_v014_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 14)
    return res.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume percentile rank (50d) over 21d
def f27vr_f27_volume_regime_rank_50d_jerk_v015_signal(volume: pd.Series) -> pd.Series:
    res = _vol_regime_rank(volume, 50)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 016-030: Volume Stability Jerk
# Jerk of volume stability (5d) over 5d
def f27vr_f27_volume_regime_stability_5d_jerk_v016_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (10d) over 5d
def f27vr_f27_volume_regime_stability_10d_jerk_v017_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 10)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (21d) over 5d
def f27vr_f27_volume_regime_stability_21d_jerk_v018_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (42d) over 21d
def f27vr_f27_volume_regime_stability_42d_jerk_v019_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 42)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (63d) over 21d
def f27vr_f27_volume_regime_stability_63d_jerk_v020_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (126d) over 21d
def f27vr_f27_volume_regime_stability_126d_jerk_v021_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (252d) over 63d
def f27vr_f27_volume_regime_stability_252d_jerk_v022_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (30d) over 5d
def f27vr_f27_volume_regime_stability_30d_jerk_v023_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 30)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (90d) over 21d
def f27vr_f27_volume_regime_stability_90d_jerk_v024_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 90)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (180d) over 21d
def f27vr_f27_volume_regime_stability_180d_jerk_v025_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 180)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (200d) over 63d
def f27vr_f27_volume_regime_stability_200d_jerk_v026_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 200)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (3d) over 2d
def f27vr_f27_volume_regime_stability_3d_jerk_v027_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 3)
    return res.pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (7d) over 5d
def f27vr_f27_volume_regime_stability_7d_jerk_v028_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 7)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (14d) over 5d
def f27vr_f27_volume_regime_stability_14d_jerk_v029_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 14)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume stability (50d) over 21d
def f27vr_f27_volume_regime_stability_50d_jerk_v030_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(volume, 50)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 031-045: Volume Shock Jerk
# Jerk of volume shock score (5d) over 5d
def f27vr_f27_volume_regime_shock_5d_jerk_v031_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (10d) over 5d
def f27vr_f27_volume_regime_shock_10d_jerk_v032_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 10)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (21d) over 5d
def f27vr_f27_volume_regime_shock_21d_jerk_v033_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (42d) over 21d
def f27vr_f27_volume_regime_shock_42d_jerk_v034_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 42)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (63d) over 21d
def f27vr_f27_volume_regime_shock_63d_jerk_v035_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (126d) over 21d
def f27vr_f27_volume_regime_shock_126d_jerk_v036_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (252d) over 63d
def f27vr_f27_volume_regime_shock_252d_jerk_v037_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (2d) over 2d
def f27vr_f27_volume_regime_shock_2d_jerk_v038_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 2)
    return res.pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (30d) over 5d
def f27vr_f27_volume_regime_shock_30d_jerk_v039_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 30)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (90d) over 21d
def f27vr_f27_volume_regime_shock_90d_jerk_v040_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 90)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (180d) over 21d
def f27vr_f27_volume_regime_shock_180d_jerk_v041_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 180)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (200d) over 63d
def f27vr_f27_volume_regime_shock_200d_jerk_v042_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 200)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (7d) over 5d
def f27vr_f27_volume_regime_shock_7d_jerk_v043_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 7)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (14d) over 5d
def f27vr_f27_volume_regime_shock_14d_jerk_v044_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 14)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume shock score (50d) over 21d
def f27vr_f27_volume_regime_shock_50d_jerk_v045_signal(volume: pd.Series) -> pd.Series:
    res = _vol_shock_score(volume, 50)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 046-060: Stability of Shocks Jerk
# Jerk of stability of 5-day shock over 21d (slope over 5d)
def f27vr_f27_volume_regime_shock_stability_5_21d_jerk_v046_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 5)
    res = _vol_stability(shock, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of stability of 10-day shock over 42d (slope over 21d)
def f27vr_f27_volume_regime_shock_stability_10_42d_jerk_v047_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 10)
    res = _vol_stability(shock, 42)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of rank of 21-day stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_stability_rank_21_63d_jerk_v048_signal(volume: pd.Series) -> pd.Series:
    stab = _vol_stability(volume, 21)
    res = _vol_regime_rank(stab, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of shock score of stability over 21d (slope over 5d)
def f27vr_f27_volume_regime_stability_shock_21_21d_jerk_v049_signal(volume: pd.Series) -> pd.Series:
    stab = _vol_stability(volume, 21)
    res = _vol_shock_score(stab, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of stability of volume z-score over 21d (slope over 5d)
def f27vr_f27_volume_regime_zscore_stability_21d_jerk_v050_signal(volume: pd.Series) -> pd.Series:
    z = _z(volume, 21)
    res = _vol_stability(z, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of rank of volume z-score over 63d (slope over 21d)
def f27vr_f27_volume_regime_zscore_rank_63d_jerk_v051_signal(volume: pd.Series) -> pd.Series:
    z = _z(volume, 21)
    res = _vol_regime_rank(z, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of stability of volume skewness over 63d (slope over 21d)
def f27vr_f27_volume_regime_skew_stability_63d_jerk_v052_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 63)
    res = _vol_stability(sk, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of rank of volume skewness over 126d (slope over 21d)
def f27vr_f27_volume_regime_skew_rank_126d_jerk_v053_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 63)
    res = _vol_regime_rank(sk, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume volatility stability over 21d (slope over 5d)
def f27vr_f27_volume_regime_vol_change_stability_21d_jerk_v054_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    res = _vol_stability(v_diff, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume volatility rank over 63d (slope over 21d)
def f27vr_f27_volume_regime_vol_change_rank_63d_jerk_v055_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    res = _vol_regime_rank(v_diff, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume volatility shock over 21d (slope over 5d)
def f27vr_f27_volume_regime_vol_change_shock_21d_jerk_v056_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    res = _vol_shock_score(v_diff, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume logret stability over 21d (slope over 5d)
def f27vr_f27_volume_regime_vol_logret_stability_21d_jerk_v057_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    res = _vol_stability(v_logret, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of volume logret rank over 63d (slope over 21d)
def f27vr_f27_volume_regime_vol_logret_rank_63d_jerk_v058_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    res = _vol_regime_rank(v_logret, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume logret shock over 21d (slope over 5d)
def f27vr_f27_volume_regime_vol_logret_shock_21d_jerk_v059_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    res = _vol_shock_score(v_logret, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Jerk of SMA5 volume stability over 42d (slope over 21d)
def f27vr_f27_volume_regime_sma5_stability_42d_jerk_v060_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 5)
    res = _vol_stability(v_sma, 42)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 061-075: Multi-window Variations Jerk
# Jerk of rank of SMA10 volume over 63d (slope over 21d)
def f27vr_f27_volume_regime_sma10_rank_63d_jerk_v061_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 10)
    res = _vol_regime_rank(v_sma, 63)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume/closeadj ratio stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_vol_price_stability_63d_jerk_v062_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    res = _vol_stability(ratio, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume/closeadj ratio rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_vol_price_rank_126d_jerk_v063_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    res = _vol_regime_rank(ratio, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume/closeadj ratio shock over 252d (slope over 63d)
def f27vr_f27_volume_regime_vol_price_shock_252d_jerk_v064_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    res = _vol_shock_score(ratio, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of dollar volume stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_dollar_vol_stability_63d_jerk_v065_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    res = _vol_stability(dv, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of dollar volume rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_dollar_vol_rank_126d_jerk_v066_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    res = _vol_regime_rank(dv, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of dollar volume shock over 252d (slope over 63d)
def f27vr_f27_volume_regime_dollar_vol_shock_252d_jerk_v067_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    res = _vol_shock_score(dv, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Jerk of up-vol stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_up_vol_stability_63d_jerk_v068_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    res = _vol_stability(up_vol, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of up-vol rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_up_vol_rank_126d_jerk_v069_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    res = _vol_regime_rank(up_vol, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of down-vol stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_down_vol_stability_63d_jerk_v070_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    res = _vol_stability(dn_vol, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of up-dn ratio stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_up_dn_ratio_stability_63d_jerk_v071_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0).rolling(21).sum()
    dn_vol = volume.where(close < close.shift(1), 0).rolling(21).sum()
    ratio = up_vol / dn_vol.replace(0, np.nan)
    res = _vol_stability(ratio, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of up-dn ratio rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_up_dn_ratio_rank_126d_jerk_v072_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0).rolling(21).sum()
    dn_vol = volume.where(close < close.shift(1), 0).rolling(21).sum()
    ratio = up_vol / dn_vol.replace(0, np.nan)
    res = _vol_regime_rank(ratio, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of VWAP stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_vwap_stability_63d_jerk_v073_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    res = _vol_stability(vwap, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of top5 vol stability over 126d (slope over 21d)
def f27vr_f27_volume_regime_top5_vol_stability_126d_jerk_v074_signal(volume: pd.Series) -> pd.Series:
    top5 = volume.where(volume > volume.rolling(252).quantile(0.95), 0)
    res = _vol_stability(top5, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of kurtosis stability over 126d (slope over 21d)
def f27vr_f27_volume_regime_kurt_stability_126d_jerk_v075_signal(volume: pd.Series) -> pd.Series:
    kurt = volume.rolling(63).kurt()
    res = _vol_stability(kurt, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 076-090: Volume efficiency and diversions Jerk
# Jerk of volume efficiency stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_vol_eff_stability_63d_jerk_v076_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    eff = close.pct_change(21).abs() / volume.rolling(21).sum().replace(0, np.nan)
    res = _vol_stability(eff, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of VP divergence stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_vp_divergence_stability_63d_jerk_v077_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    v_rank = _vol_regime_rank(volume, 63)
    p_rank = _vol_regime_rank(closeadj, 63)
    div = v_rank - p_rank
    res = _vol_stability(div, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume-weighted-std stability over 63d (slope over 21d)
def f27vr_f27_volume_regime_vol_std_stability_63d_jerk_v078_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    v_std = volume * close.rolling(21).std()
    res = _vol_stability(v_std, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume thrust rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_vol_thrust_rank_126d_jerk_v079_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(5).sum() / volume.rolling(63).sum().replace(0, np.nan)
    res = _vol_regime_rank(thrust, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Jerk of volume-weighted-ROC rank over 126d (slope over 21d)
def f27vr_f27_volume_regime_vwroc_rank_126d_jerk_v080_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    vwroc = (volume * np.sign(close.diff())).rolling(21).sum()
    res = _vol_regime_rank(vwroc, 126)
    return res.diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 081-150: Systematic Variations and mixed window jerks
def f27vr_f27_volume_regime_rank_60d_jerk_v081_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 60).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_60d_jerk_v082_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 60).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_60d_jerk_v083_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 60).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_100d_jerk_v084_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 100).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_100d_jerk_v085_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 100).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_100d_jerk_v086_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 100).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_150d_jerk_v087_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 150).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_150d_jerk_v088_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 150).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_150d_jerk_v089_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 150).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_300d_jerk_v090_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 300).diff(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_300d_jerk_v091_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 300).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_300d_jerk_v092_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 300).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_500d_jerk_v093_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 500).diff(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_500d_jerk_v094_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 500).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_500d_jerk_v095_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 500).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# More descriptive ones for the remaining
def f27vr_f27_volume_regime_zscore5_stability_21d_jerk_v096_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(_z(volume, 5), 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_zscore10_stability_42d_jerk_v097_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(_z(volume, 10), 42)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_zscore21_stability_63d_jerk_v098_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(_z(volume, 21), 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_zscore63_stability_126d_jerk_v099_signal(volume: pd.Series) -> pd.Series:
    res = _vol_stability(_z(volume, 63), 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_sma5_rank_21d_jerk_v100_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(_sma(volume, 5), 21).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_sma21_rank_63d_jerk_v101_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(_sma(volume, 21), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_sma63_rank_126d_jerk_v102_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(_sma(volume, 63), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_sma5_shock_21d_jerk_v103_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(_sma(volume, 5), 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_sma21_shock_63d_jerk_v104_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(_sma(volume, 21), 63).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_sma63_shock_126d_jerk_v105_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(_sma(volume, 63), 126).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_up_vol_stability_21d_jerk_v106_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    return _vol_stability(up_vol, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_up_vol_stability_42d_jerk_v107_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    return _vol_stability(up_vol, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_down_vol_stability_21d_jerk_v108_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    return _vol_stability(dn_vol, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_down_vol_stability_42d_jerk_v109_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    return _vol_stability(dn_vol, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_vol_eff5_stability_21d_jerk_v110_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    eff = close.pct_change(5).abs() / volume.rolling(5).sum().replace(0, np.nan)
    return _vol_stability(eff, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_eff10_stability_42d_jerk_v111_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    eff = close.pct_change(10).abs() / volume.rolling(10).sum().replace(0, np.nan)
    return _vol_stability(eff, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_conc_stability_21d_jerk_v112_signal(volume: pd.Series) -> pd.Series:
    conc = volume.rolling(21).apply(lambda x: np.sort(x)[-4:].sum() / x.sum() if x.sum() > 0 else np.nan, raw=True)
    return _vol_stability(conc, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_conc_stability_42d_jerk_v113_signal(volume: pd.Series) -> pd.Series:
    conc = volume.rolling(21).apply(lambda x: np.sort(x)[-4:].sum() / x.sum() if x.sum() > 0 else np.nan, raw=True)
    return _vol_stability(conc, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_p75_stability_21d_jerk_v114_signal(volume: pd.Series) -> pd.Series:
    p75 = volume.rolling(21).quantile(0.75)
    return _vol_stability(p75, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_p90_stability_42d_jerk_v115_signal(volume: pd.Series) -> pd.Series:
    p90 = volume.rolling(21).quantile(0.90)
    return _vol_stability(p90, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_thrust5_stability_21d_jerk_v116_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(5).sum() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_stability(thrust, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_thrust10_stability_42d_jerk_v117_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(10).sum() / volume.rolling(42).sum().replace(0, np.nan)
    return _vol_stability(thrust, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_vol_std5_stability_21d_jerk_v118_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    v_std = volume * close.rolling(5).std()
    return _vol_stability(v_std, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_std10_stability_42d_jerk_v119_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    v_std = volume * close.rolling(10).std()
    return _vol_stability(v_std, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_vwap5_stability_21d_jerk_v120_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(5).sum() / volume.rolling(5).sum().replace(0, np.nan)
    return _vol_stability(vwap, 21).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vwap10_stability_42d_jerk_v121_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(10).sum() / volume.rolling(10).sum().replace(0, np.nan)
    return _vol_stability(vwap, 42).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_rank_40d_jerk_v122_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 40).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_80d_jerk_v123_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 80).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_160d_jerk_v124_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 160).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_rank_320d_jerk_v125_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 320).diff(63).diff(63).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_stability_40d_jerk_v126_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 40).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_80d_jerk_v127_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 80).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_160d_jerk_v128_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 160).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_320d_jerk_v129_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 320).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_shock_40d_jerk_v130_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 40).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_80d_jerk_v131_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 80).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_160d_jerk_v132_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 160).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_320d_jerk_v133_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 320).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_rank_252d_jerk5_v134_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 252).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_252d_jerk5_v135_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 252).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_252d_jerk5_v136_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 252).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_rank_126d_jerk5_v137_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 126).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_126d_jerk5_v138_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 126).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_126d_jerk5_v139_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 126).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_rank_63d_jerk5_v140_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 63).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_63d_jerk5_v141_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 63).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_63d_jerk5_v142_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 63).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_rank_21d_jerk21_v143_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 21).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_stability_21d_jerk21_v144_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 21).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_shock_21d_jerk21_v145_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 21).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

def f27vr_f27_volume_regime_vol_change_stability_63d_jerk_v146_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume.diff().abs(), 63).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_change_rank_126d_jerk_v147_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume.diff().abs(), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_logret_stability_63d_jerk_v148_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_stability(v_logret, 63).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_logret_rank_126d_jerk_v149_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_regime_rank(v_logret, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_vol_logret_shock_63d_jerk_v150_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_shock_score(v_logret, 63).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

F27_VOLUME_REGIME_JERK_REGISTRY = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["volume", "close", "closeadj"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f27vr_f27_volume_regime_") and "jerk" in name
}

if __name__ == "__main__":
    import numpy as np
    np.random.seed(42)
    n = 1000
    volume = pd.Series(np.random.lognormal(10, 1, n), name="volume")
    close = pd.Series(np.random.normal(100, 5, n), name="close")
    closeadj = close * 1.05
    
    input_map = {"volume": volume, "close": close, "closeadj": closeadj}
    
    for name, info in F27_VOLUME_REGIME_JERK_REGISTRY.items():
        func = info["func"]
        inputs = [input_map[arg] for arg in info["inputs"]]
        
        # Determinism check
        y1 = func(*inputs)
        y2 = func(*inputs)
        pd.testing.assert_series_equal(y1, y2)
        
        # Non-trivial output check
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, f"Feature {name} returned all NaNs after warmup"
        print(f"Feature {name}: OK")
