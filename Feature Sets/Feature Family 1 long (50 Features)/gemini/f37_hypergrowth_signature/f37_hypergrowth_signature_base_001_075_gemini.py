import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    """Standard Deviation with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _z(s, w):
    """Z-score calculation."""
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _hs_growth(s, w):
    """Domain Primitive: Growth over a window."""
    return s.pct_change(w)

def _hs_consistency(s, w):
    """Domain Primitive: Consistency of growth over a window."""
    growth = s.pct_change(21)
    return _sma(growth, w) / _std(growth, w).replace(0, np.nan)

def _hs_zscore(s, w):
    """Domain Primitive: Z-score of a series."""
    return _z(s, w)

def _hs_acceleration(s, w1, w2):
    """Domain Primitive: Acceleration of growth."""
    return s.pct_change(w1).diff(w2)

def f37_hypergrowth_signature_opinc_growth_w22_v001_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 22-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 1.
    """
    res = _hs_growth(opinc, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w23_v002_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 23-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 2.
    """
    res = _hs_growth(revenue, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w24_v003_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 24-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 3.
    """
    res = _hs_growth(opinc, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w25_v004_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 25-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 4.
    """
    res = _hs_growth(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w26_v005_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 26-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 5.
    """
    res = _hs_growth(opinc, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w27_v006_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 27-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 6.
    """
    res = _hs_growth(revenue, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w28_v007_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 28-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 7.
    """
    res = _hs_growth(opinc, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w29_v008_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 29-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 8.
    """
    res = _hs_growth(revenue, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w30_v009_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 30-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 9.
    """
    res = _hs_growth(opinc, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w31_v010_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 31-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 10.
    """
    res = _hs_growth(revenue, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w32_v011_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 32-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 11.
    """
    res = _hs_growth(opinc, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w33_v012_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 33-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 12.
    """
    res = _hs_growth(revenue, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w34_v013_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 34-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 13.
    """
    res = _hs_growth(opinc, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w35_v014_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 35-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 14.
    """
    res = _hs_growth(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w36_v015_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 36-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 15.
    """
    res = _hs_growth(opinc, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w37_v016_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 37-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 16.
    """
    res = _hs_growth(revenue, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w38_v017_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 38-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 17.
    """
    res = _hs_growth(opinc, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w39_v018_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 39-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 18.
    """
    res = _hs_growth(revenue, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w40_v019_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 40-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 19.
    """
    res = _hs_growth(opinc, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w41_v020_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 41-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 20.
    """
    res = _hs_growth(revenue, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w42_v021_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 42-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 21.
    """
    res = _hs_growth(opinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w43_v022_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 43-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 22.
    """
    res = _hs_growth(revenue, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w44_v023_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 44-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 23.
    """
    res = _hs_growth(opinc, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w45_v024_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 45-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 24.
    """
    res = _hs_growth(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w46_v025_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 46-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 25.
    """
    res = _hs_growth(opinc, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w47_v026_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 47-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 26.
    """
    res = _hs_growth(revenue, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w48_v027_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 48-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 27.
    """
    res = _hs_growth(opinc, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w49_v028_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 49-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 28.
    """
    res = _hs_growth(revenue, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w50_v029_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 50-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 29.
    """
    res = _hs_growth(opinc, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w51_v030_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 51-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 30.
    """
    res = _hs_growth(revenue, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w52_v031_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 52-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 31.
    """
    res = _hs_growth(opinc, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w53_v032_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 53-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 32.
    """
    res = _hs_growth(revenue, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w54_v033_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 54-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 33.
    """
    res = _hs_growth(opinc, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w55_v034_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 55-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 34.
    """
    res = _hs_growth(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w56_v035_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 56-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 35.
    """
    res = _hs_growth(opinc, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w57_v036_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 57-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 36.
    """
    res = _hs_growth(revenue, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w58_v037_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 58-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 37.
    """
    res = _hs_growth(opinc, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w59_v038_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 59-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 38.
    """
    res = _hs_growth(revenue, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w60_v039_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 60-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 39.
    """
    res = _hs_growth(opinc, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w61_v040_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 61-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 40.
    """
    res = _hs_growth(revenue, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w62_v041_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 62-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 41.
    """
    res = _hs_growth(opinc, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w63_v042_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 63-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 42.
    """
    res = _hs_growth(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w64_v043_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 64-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 43.
    """
    res = _hs_growth(opinc, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w65_v044_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 65-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 44.
    """
    res = _hs_growth(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w66_v045_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 66-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 45.
    """
    res = _hs_growth(opinc, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w67_v046_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 67-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 46.
    """
    res = _hs_growth(revenue, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w68_v047_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 68-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 47.
    """
    res = _hs_growth(opinc, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w69_v048_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 69-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 48.
    """
    res = _hs_growth(revenue, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w70_v049_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 70-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 49.
    """
    res = _hs_growth(opinc, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w71_v050_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 71-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 50.
    """
    res = _hs_growth(revenue, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w72_v051_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 72-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 51.
    """
    res = _hs_growth(opinc, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w73_v052_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 73-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 52.
    """
    res = _hs_growth(revenue, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w74_v053_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 74-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 53.
    """
    res = _hs_growth(opinc, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w75_v054_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 75-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 54.
    """
    res = _hs_growth(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w76_v055_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 76-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 55.
    """
    res = _hs_growth(opinc, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w77_v056_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 77-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 56.
    """
    res = _hs_growth(revenue, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w78_v057_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 78-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 57.
    """
    res = _hs_growth(opinc, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w79_v058_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 79-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 58.
    """
    res = _hs_growth(revenue, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w80_v059_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 80-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 59.
    """
    res = _hs_growth(opinc, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w81_v060_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 81-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 60.
    """
    res = _hs_growth(revenue, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w82_v061_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 82-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 61.
    """
    res = _hs_growth(opinc, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w83_v062_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 83-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 62.
    """
    res = _hs_growth(revenue, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w21_v063_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 21-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 63.
    """
    res = _hs_growth(opinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w22_v064_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 22-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 64.
    """
    res = _hs_growth(revenue, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w23_v065_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 23-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 65.
    """
    res = _hs_growth(opinc, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w24_v066_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 24-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 66.
    """
    res = _hs_growth(revenue, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w25_v067_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 25-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 67.
    """
    res = _hs_growth(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w26_v068_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 26-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 68.
    """
    res = _hs_growth(revenue, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w27_v069_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 27-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 69.
    """
    res = _hs_growth(opinc, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w28_v070_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 28-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 70.
    """
    res = _hs_growth(revenue, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w29_v071_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 29-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 71.
    """
    res = _hs_growth(opinc, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w30_v072_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 30-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 72.
    """
    res = _hs_growth(revenue, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w31_v073_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 31-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 73.
    """
    res = _hs_growth(opinc, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w32_v074_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 32-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 74.
    """
    res = _hs_growth(revenue, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w33_v075_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 33-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 75.
    """
    res = _hs_growth(opinc, 33)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum(),
        "opinc": np.random.normal(100, 20, n).cumsum(),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f37_hypergrowth_signature_"))]
    
    print(f"Testing {len(funcs)} functions for f37_hypergrowth_signature...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            print(f"Warning: {func.__name__} produced all NaNs in test range.")
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f37_hypergrowth_signature_"))]}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_001_075 = REGISTRY
