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

def f37_hypergrowth_signature_revenue_growth_w34_v076_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 34-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 76.
    """
    res = _hs_growth(revenue, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w35_v077_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 35-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 77.
    """
    res = _hs_growth(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w36_v078_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 36-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 78.
    """
    res = _hs_growth(revenue, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w37_v079_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 37-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 79.
    """
    res = _hs_growth(opinc, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w38_v080_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 38-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 80.
    """
    res = _hs_growth(revenue, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w39_v081_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 39-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 81.
    """
    res = _hs_growth(opinc, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w40_v082_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 40-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 82.
    """
    res = _hs_growth(revenue, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w41_v083_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 41-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 83.
    """
    res = _hs_growth(opinc, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w42_v084_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 42-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 84.
    """
    res = _hs_growth(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w43_v085_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 43-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 85.
    """
    res = _hs_growth(opinc, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w44_v086_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 44-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 86.
    """
    res = _hs_growth(revenue, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w45_v087_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 45-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 87.
    """
    res = _hs_growth(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w46_v088_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 46-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 88.
    """
    res = _hs_growth(revenue, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w47_v089_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 47-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 89.
    """
    res = _hs_growth(opinc, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w48_v090_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 48-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 90.
    """
    res = _hs_growth(revenue, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w49_v091_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 49-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 91.
    """
    res = _hs_growth(opinc, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w50_v092_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 50-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 92.
    """
    res = _hs_growth(revenue, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w51_v093_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 51-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 93.
    """
    res = _hs_growth(opinc, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w52_v094_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 52-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 94.
    """
    res = _hs_growth(revenue, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w53_v095_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 53-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 95.
    """
    res = _hs_growth(opinc, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w54_v096_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 54-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 96.
    """
    res = _hs_growth(revenue, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w55_v097_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 55-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 97.
    """
    res = _hs_growth(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w56_v098_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 56-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 98.
    """
    res = _hs_growth(revenue, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w57_v099_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 57-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 99.
    """
    res = _hs_growth(opinc, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w58_v100_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 58-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 100.
    """
    res = _hs_growth(revenue, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w59_v101_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 59-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 101.
    """
    res = _hs_growth(opinc, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w60_v102_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 60-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 102.
    """
    res = _hs_growth(revenue, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w61_v103_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 61-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 103.
    """
    res = _hs_growth(opinc, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w62_v104_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 62-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 104.
    """
    res = _hs_growth(revenue, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w63_v105_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 63-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 105.
    """
    res = _hs_growth(opinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w64_v106_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 64-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 106.
    """
    res = _hs_growth(revenue, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w65_v107_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 65-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 107.
    """
    res = _hs_growth(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w66_v108_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 66-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 108.
    """
    res = _hs_growth(revenue, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w67_v109_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 67-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 109.
    """
    res = _hs_growth(opinc, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w68_v110_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 68-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 110.
    """
    res = _hs_growth(revenue, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w69_v111_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 69-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 111.
    """
    res = _hs_growth(opinc, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w70_v112_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 70-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 112.
    """
    res = _hs_growth(revenue, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w71_v113_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 71-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 113.
    """
    res = _hs_growth(opinc, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w72_v114_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 72-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 114.
    """
    res = _hs_growth(revenue, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w73_v115_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 73-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 115.
    """
    res = _hs_growth(opinc, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w74_v116_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 74-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 116.
    """
    res = _hs_growth(revenue, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w75_v117_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 75-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 117.
    """
    res = _hs_growth(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w76_v118_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 76-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 118.
    """
    res = _hs_growth(revenue, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w77_v119_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 77-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 119.
    """
    res = _hs_growth(opinc, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w78_v120_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 78-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 120.
    """
    res = _hs_growth(revenue, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w79_v121_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 79-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 121.
    """
    res = _hs_growth(opinc, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w80_v122_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 80-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 122.
    """
    res = _hs_growth(revenue, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w81_v123_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 81-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 123.
    """
    res = _hs_growth(opinc, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w82_v124_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 82-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 124.
    """
    res = _hs_growth(revenue, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w83_v125_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 83-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 125.
    """
    res = _hs_growth(opinc, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w21_v126_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 21-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 126.
    """
    res = _hs_growth(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w22_v127_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 22-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 127.
    """
    res = _hs_growth(opinc, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w23_v128_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 23-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 128.
    """
    res = _hs_growth(revenue, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w24_v129_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 24-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 129.
    """
    res = _hs_growth(opinc, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w25_v130_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 25-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 130.
    """
    res = _hs_growth(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w26_v131_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 26-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 131.
    """
    res = _hs_growth(opinc, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w27_v132_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 27-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 132.
    """
    res = _hs_growth(revenue, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w28_v133_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 28-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 133.
    """
    res = _hs_growth(opinc, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w29_v134_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 29-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 134.
    """
    res = _hs_growth(revenue, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w30_v135_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 30-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 135.
    """
    res = _hs_growth(opinc, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w31_v136_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 31-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 136.
    """
    res = _hs_growth(revenue, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w32_v137_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 32-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 137.
    """
    res = _hs_growth(opinc, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w33_v138_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 33-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 138.
    """
    res = _hs_growth(revenue, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w34_v139_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 34-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 139.
    """
    res = _hs_growth(opinc, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w35_v140_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 35-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 140.
    """
    res = _hs_growth(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w36_v141_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 36-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 141.
    """
    res = _hs_growth(opinc, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w37_v142_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 37-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 142.
    """
    res = _hs_growth(revenue, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w38_v143_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 38-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 143.
    """
    res = _hs_growth(opinc, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w39_v144_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 39-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 144.
    """
    res = _hs_growth(revenue, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w40_v145_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 40-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 145.
    """
    res = _hs_growth(opinc, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w41_v146_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 41-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 146.
    """
    res = _hs_growth(revenue, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w42_v147_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 42-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 147.
    """
    res = _hs_growth(opinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w43_v148_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 43-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 148.
    """
    res = _hs_growth(revenue, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_growth_w44_v149_signal(opinc) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 44-period growth rate of opinc.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 149.
    """
    res = _hs_growth(opinc, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_growth_w45_v150_signal(revenue) -> pd.Series:
    """
    Calculates the hypergrowth signature using the growth primitive.
    This feature monitors the 45-period growth rate of revenue.
    It is a fundamental component of identifying hypergrowth companies.
    Variation: 150.
    """
    res = _hs_growth(revenue, 45)
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
F37_HYPERGROWTH_SIGNATURE_REGISTRY_076_150 = REGISTRY
