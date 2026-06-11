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

# Features 001-015: Volume Regime Rank
# Volume percentile rank over 5-day window
def f27vr_f27_volume_regime_rank_5d_base_v001_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 5).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 10-day window
def f27vr_f27_volume_regime_rank_10d_base_v002_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 10).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 21-day window
def f27vr_f27_volume_regime_rank_21d_base_v003_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 21).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 42-day window
def f27vr_f27_volume_regime_rank_42d_base_v004_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 42).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 63-day window
def f27vr_f27_volume_regime_rank_63d_base_v005_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 63).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 126-day window
def f27vr_f27_volume_regime_rank_126d_base_v006_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 126).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 252-day window
def f27vr_f27_volume_regime_rank_252d_base_v007_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 252).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 2-day window
def f27vr_f27_volume_regime_rank_2d_base_v008_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 2).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 3-day window
def f27vr_f27_volume_regime_rank_3d_base_v009_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 3).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 7-day window
def f27vr_f27_volume_regime_rank_7d_base_v010_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 7).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 14-day window
def f27vr_f27_volume_regime_rank_14d_base_v011_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 14).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 30-day window
def f27vr_f27_volume_regime_rank_30d_base_v012_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 30).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 90-day window
def f27vr_f27_volume_regime_rank_90d_base_v013_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 90).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 180-day window
def f27vr_f27_volume_regime_rank_180d_base_v014_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 180).replace([np.inf, -np.inf], np.nan)

# Volume percentile rank over 200-day window
def f27vr_f27_volume_regime_rank_200d_base_v015_signal(volume: pd.Series) -> pd.Series:
    return _vol_regime_rank(volume, 200).replace([np.inf, -np.inf], np.nan)

# Features 016-030: Volume Stability
# Volume stability (mean/std) over 5-day window
def f27vr_f27_volume_regime_stability_5d_base_v016_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 5).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 10-day window
def f27vr_f27_volume_regime_stability_10d_base_v017_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 10).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 21-day window
def f27vr_f27_volume_regime_stability_21d_base_v018_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 21).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 42-day window
def f27vr_f27_volume_regime_stability_42d_base_v019_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 42).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 63-day window
def f27vr_f27_volume_regime_stability_63d_base_v020_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 63).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 126-day window
def f27vr_f27_volume_regime_stability_126d_base_v021_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 126).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 252-day window
def f27vr_f27_volume_regime_stability_252d_base_v022_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 252).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 2-day window
def f27vr_f27_volume_regime_stability_2d_base_v023_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 2).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 3-day window
def f27vr_f27_volume_regime_stability_3d_base_v024_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 3).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 7-day window
def f27vr_f27_volume_regime_stability_7d_base_v025_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 7).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 14-day window
def f27vr_f27_volume_regime_stability_14d_base_v026_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 14).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 30-day window
def f27vr_f27_volume_regime_stability_30d_base_v027_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 30).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 90-day window
def f27vr_f27_volume_regime_stability_90d_base_v028_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 90).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 180-day window
def f27vr_f27_volume_regime_stability_180d_base_v029_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 180).replace([np.inf, -np.inf], np.nan)

# Volume stability (mean/std) over 200-day window
def f27vr_f27_volume_regime_stability_200d_base_v030_signal(volume: pd.Series) -> pd.Series:
    return _vol_stability(volume, 200).replace([np.inf, -np.inf], np.nan)

# Features 031-045: Volume Shock Score
# Volume shock (current/max) over 5-day window
def f27vr_f27_volume_regime_shock_5d_base_v031_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 5).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 10-day window
def f27vr_f27_volume_regime_shock_10d_base_v032_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 10).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 21-day window
def f27vr_f27_volume_regime_shock_21d_base_v033_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 21).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 42-day window
def f27vr_f27_volume_regime_shock_42d_base_v034_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 42).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 63-day window
def f27vr_f27_volume_regime_shock_63d_base_v035_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 63).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 126-day window
def f27vr_f27_volume_regime_shock_126d_base_v036_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 126).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 252-day window
def f27vr_f27_volume_regime_shock_252d_base_v037_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 252).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 2-day window
def f27vr_f27_volume_regime_shock_2d_base_v038_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 2).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 3-day window
def f27vr_f27_volume_regime_shock_3d_base_v039_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 3).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 7-day window
def f27vr_f27_volume_regime_shock_7d_base_v040_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 7).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 14-day window
def f27vr_f27_volume_regime_shock_14d_base_v041_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 14).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 30-day window
def f27vr_f27_volume_regime_shock_30d_base_v042_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 30).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 90-day window
def f27vr_f27_volume_regime_shock_90d_base_v043_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 90).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 180-day window
def f27vr_f27_volume_regime_shock_180d_base_v044_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 180).replace([np.inf, -np.inf], np.nan)

# Volume shock (current/max) over 200-day window
def f27vr_f27_volume_regime_shock_200d_base_v045_signal(volume: pd.Series) -> pd.Series:
    return _vol_shock_score(volume, 200).replace([np.inf, -np.inf], np.nan)

# Features 046-060: Stability of Shocks
# Stability of 5-day shock score over 21-day window
def f27vr_f27_volume_regime_shock_stability_5_21d_base_v046_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 5)
    return _vol_stability(shock, 21).replace([np.inf, -np.inf], np.nan)

# Stability of 10-day shock score over 42-day window
def f27vr_f27_volume_regime_shock_stability_10_42d_base_v047_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 10)
    return _vol_stability(shock, 42).replace([np.inf, -np.inf], np.nan)

# Stability of 21-day shock score over 63-day window
def f27vr_f27_volume_regime_shock_stability_21_63d_base_v048_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 21)
    return _vol_stability(shock, 63).replace([np.inf, -np.inf], np.nan)

# Rank of 21-day stability over 63-day window
def f27vr_f27_volume_regime_stability_rank_21_63d_base_v049_signal(volume: pd.Series) -> pd.Series:
    stab = _vol_stability(volume, 21)
    return _vol_regime_rank(stab, 63).replace([np.inf, -np.inf], np.nan)

# Rank of 63-day stability over 126-day window
def f27vr_f27_volume_regime_stability_rank_63_126d_base_v050_signal(volume: pd.Series) -> pd.Series:
    stab = _vol_stability(volume, 63)
    return _vol_regime_rank(stab, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of stability over 21-day window
def f27vr_f27_volume_regime_stability_shock_21_21d_base_v051_signal(volume: pd.Series) -> pd.Series:
    stab = _vol_stability(volume, 21)
    return _vol_shock_score(stab, 21).replace([np.inf, -np.inf], np.nan)

# Stability of regime rank (21d rank stability over 63d)
def f27vr_f27_volume_regime_rank_stability_21_63d_base_v052_signal(volume: pd.Series) -> pd.Series:
    rank = _vol_regime_rank(volume, 21)
    return _vol_stability(rank, 63).replace([np.inf, -np.inf], np.nan)

# Rank of 5-day shock score over 63-day window
def f27vr_f27_volume_regime_shock_rank_5_63d_base_v053_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 5)
    return _vol_regime_rank(shock, 63).replace([np.inf, -np.inf], np.nan)

# Rank of 21-day shock score over 126-day window
def f27vr_f27_volume_regime_shock_rank_21_126d_base_v054_signal(volume: pd.Series) -> pd.Series:
    shock = _vol_shock_score(volume, 21)
    return _vol_regime_rank(shock, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of rank (21d rank shock over 63d)
def f27vr_f27_volume_regime_rank_shock_21_63d_base_v055_signal(volume: pd.Series) -> pd.Series:
    rank = _vol_regime_rank(volume, 21)
    return _vol_shock_score(rank, 63).replace([np.inf, -np.inf], np.nan)

# Stability of volume z-score over 21-day window
def f27vr_f27_volume_regime_zscore_stability_21d_base_v056_signal(volume: pd.Series) -> pd.Series:
    z = _z(volume, 21)
    return _vol_stability(z, 21).replace([np.inf, -np.inf], np.nan)

# Rank of volume z-score over 63-day window
def f27vr_f27_volume_regime_zscore_rank_63d_base_v057_signal(volume: pd.Series) -> pd.Series:
    z = _z(volume, 21)
    return _vol_regime_rank(z, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of volume z-score over 21-day window
def f27vr_f27_volume_regime_zscore_shock_21d_base_v058_signal(volume: pd.Series) -> pd.Series:
    z = _z(volume, 21)
    return _vol_shock_score(z, 21).replace([np.inf, -np.inf], np.nan)

# Stability of volume skewness over 63-day window
def f27vr_f27_volume_regime_skew_stability_63d_base_v059_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 63)
    return _vol_stability(sk, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume skewness over 126-day window
def f27vr_f27_volume_regime_skew_rank_126d_base_v060_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 63)
    return _vol_regime_rank(sk, 126).replace([np.inf, -np.inf], np.nan)

# Features 061-075: Multi-window Stability & Rank
# 21-day stability relative to 252-day stability rank
def f27vr_f27_volume_regime_stability_rel_rank_21_252d_base_v061_signal(volume: pd.Series) -> pd.Series:
    s21 = _vol_stability(volume, 21)
    s252 = _vol_stability(volume, 252)
    return _vol_regime_rank(s21 / s252.replace(0, np.nan), 63).replace([np.inf, -np.inf], np.nan)

# 5-day shock relative to 63-day shock rank
def f27vr_f27_volume_regime_shock_rel_rank_5_63d_base_v062_signal(volume: pd.Series) -> pd.Series:
    sh5 = _vol_shock_score(volume, 5)
    sh63 = _vol_shock_score(volume, 63)
    return _vol_regime_rank(sh5 / sh63.replace(0, np.nan), 63).replace([np.inf, -np.inf], np.nan)

# Stability of SMA-smoothed volume over 21-day window
def f27vr_f27_volume_regime_smooth_stability_21d_base_v063_signal(volume: pd.Series) -> pd.Series:
    v_smooth = _sma(volume, 5)
    return _vol_stability(v_smooth, 21).replace([np.inf, -np.inf], np.nan)

# Rank of EMA-smoothed volume over 63-day window
def f27vr_f27_volume_regime_smooth_rank_63d_base_v064_signal(volume: pd.Series) -> pd.Series:
    v_smooth = _ema(volume, 10)
    return _vol_regime_rank(v_smooth, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of smoothed volume over 21-day window
def f27vr_f27_volume_regime_smooth_shock_21d_base_v065_signal(volume: pd.Series) -> pd.Series:
    v_smooth = _sma(volume, 5)
    return _vol_shock_score(v_smooth, 21).replace([np.inf, -np.inf], np.nan)

# Stability of high-volume spikes (vol > 2*SMA) count over 63d
def f27vr_f27_volume_regime_spike_count_stability_63d_base_v066_signal(volume: pd.Series) -> pd.Series:
    spikes = (volume > 2 * _sma(volume, 21)).astype(float)
    return _vol_stability(spikes.rolling(21).sum(), 63).replace([np.inf, -np.inf], np.nan)

# Rank of high-volume spikes count over 126d
def f27vr_f27_volume_regime_spike_count_rank_126d_base_v067_signal(volume: pd.Series) -> pd.Series:
    spikes = (volume > 2 * _sma(volume, 21)).astype(float)
    return _vol_regime_rank(spikes.rolling(21).sum(), 126).replace([np.inf, -np.inf], np.nan)

# Stability of volume/range ratio over 21-day window
def f27vr_f27_volume_regime_vol_range_stability_21d_base_v068_signal(volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ratio = volume / (high - low).replace(0, np.nan)
    return _vol_stability(ratio, 21).replace([np.inf, -np.inf], np.nan)

# Rank of volume/range ratio over 63-day window
def f27vr_f27_volume_regime_vol_range_rank_63d_base_v069_signal(volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ratio = volume / (high - low).replace(0, np.nan)
    return _vol_regime_rank(ratio, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of volume/range ratio over 21-day window
def f27vr_f27_volume_regime_vol_range_shock_21d_base_v070_signal(volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ratio = volume / (high - low).replace(0, np.nan)
    return _vol_shock_score(ratio, 21).replace([np.inf, -np.inf], np.nan)

# Stability of volume concentration (top 1/5 sum) over 63d
def f27vr_f27_volume_regime_concentration_stability_63d_base_v071_signal(volume: pd.Series) -> pd.Series:
    conc = volume.rolling(21).apply(lambda x: np.sort(x)[-4:].sum() / x.sum() if x.sum() > 0 else np.nan, raw=True)
    return _vol_stability(conc, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume concentration over 126d
def f27vr_f27_volume_regime_concentration_rank_126d_base_v072_signal(volume: pd.Series) -> pd.Series:
    conc = volume.rolling(21).apply(lambda x: np.sort(x)[-4:].sum() / x.sum() if x.sum() > 0 else np.nan, raw=True)
    return _vol_regime_rank(conc, 126).replace([np.inf, -np.inf], np.nan)

# Stability of volume percentile (75th) over 63d
def f27vr_f27_volume_regime_p75_stability_63d_base_v073_signal(volume: pd.Series) -> pd.Series:
    p75 = volume.rolling(21).quantile(0.75)
    return _vol_stability(p75, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume percentile (90th) over 126d
def f27vr_f27_volume_regime_p90_rank_126d_base_v074_signal(volume: pd.Series) -> pd.Series:
    p90 = volume.rolling(21).quantile(0.90)
    return _vol_regime_rank(p90, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume percentile (99th) over 21d
def f27vr_f27_volume_regime_p99_shock_21d_base_v075_signal(volume: pd.Series) -> pd.Series:
    p99 = volume.rolling(63).quantile(0.99)
    return _vol_shock_score(p99, 21).replace([np.inf, -np.inf], np.nan)

F27_VOLUME_REGIME_BASE_REGISTRY_001_075 = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["volume", "high", "low"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f27vr_f27_volume_regime_")
}

if __name__ == "__main__":
    import numpy as np
    np.random.seed(42)
    n = 1000
    volume = pd.Series(np.random.lognormal(10, 1, n), name="volume")
    high = pd.Series(np.random.normal(105, 5, n), name="high")
    low = pd.Series(np.random.normal(95, 5, n), name="low")
    
    input_map = {"volume": volume, "high": high, "low": low}
    
    for name, info in F27_VOLUME_REGIME_BASE_REGISTRY_001_075.items():
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
