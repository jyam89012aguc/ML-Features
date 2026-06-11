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

def _fg_divergence(s1, s2, w): return s1.pct_change(w) - s2.pct_change(w)

def f47_fake_growth_detector_receivables_base_w22_v001_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 1. This monitors 22-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w23_v002_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 2. This monitors 23-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w24_v003_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 3. This monitors 24-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w25_v004_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 4. This monitors 25-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w26_v005_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 5. This monitors 26-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w27_v006_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 6. This monitors 27-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w28_v007_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 7. This monitors 28-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w29_v008_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 8. This monitors 29-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w30_v009_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 9. This monitors 30-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w31_v010_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 10. This monitors 31-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w32_v011_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 11. This monitors 32-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w33_v012_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 12. This monitors 33-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w34_v013_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 13. This monitors 34-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w35_v014_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 14. This monitors 35-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w36_v015_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 15. This monitors 36-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w37_v016_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 16. This monitors 37-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w38_v017_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 17. This monitors 38-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w39_v018_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 18. This monitors 39-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w40_v019_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 19. This monitors 40-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w41_v020_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 20. This monitors 41-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w42_v021_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 21. This monitors 42-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w43_v022_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 22. This monitors 43-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w44_v023_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 23. This monitors 44-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w45_v024_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 24. This monitors 45-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w46_v025_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 25. This monitors 46-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w47_v026_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 26. This monitors 47-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w48_v027_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 27. This monitors 48-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w49_v028_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 28. This monitors 49-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w50_v029_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 29. This monitors 50-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w51_v030_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 30. This monitors 51-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w52_v031_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 31. This monitors 52-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w53_v032_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 32. This monitors 53-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w54_v033_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 33. This monitors 54-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w55_v034_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 34. This monitors 55-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w56_v035_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 35. This monitors 56-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w57_v036_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 36. This monitors 57-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w58_v037_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 37. This monitors 58-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w59_v038_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 38. This monitors 59-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w60_v039_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 39. This monitors 60-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w61_v040_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 40. This monitors 61-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w62_v041_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 41. This monitors 62-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w63_v042_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 42. This monitors 63-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w64_v043_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 43. This monitors 64-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w65_v044_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 44. This monitors 65-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w66_v045_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 45. This monitors 66-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w67_v046_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 46. This monitors 67-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w68_v047_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 47. This monitors 68-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w69_v048_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 48. This monitors 69-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w70_v049_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 49. This monitors 70-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w71_v050_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 50. This monitors 71-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w72_v051_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 51. This monitors 72-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w73_v052_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 52. This monitors 73-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w74_v053_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 53. This monitors 74-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w75_v054_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 54. This monitors 75-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w76_v055_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 55. This monitors 76-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w77_v056_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 56. This monitors 77-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w78_v057_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 57. This monitors 78-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w79_v058_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 58. This monitors 79-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w80_v059_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 59. This monitors 80-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w81_v060_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 60. This monitors 81-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w82_v061_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 61. This monitors 82-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w83_v062_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 62. This monitors 83-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w21_v063_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 63. This monitors 21-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w22_v064_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 64. This monitors 22-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w23_v065_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 65. This monitors 23-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w24_v066_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 66. This monitors 24-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w25_v067_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 67. This monitors 25-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w26_v068_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 68. This monitors 26-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w27_v069_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 69. This monitors 27-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w28_v070_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 70. This monitors 28-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w29_v071_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 71. This monitors 29-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w30_v072_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 72. This monitors 30-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_receivables_base_w31_v073_signal(receivables) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: receivables, Variation: 73. This monitors 31-period trends."""
    res = _fg_divergence(receivables, revenue if 'receivables' != 'revenue' else receivables, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_inventory_base_w32_v074_signal(inventory) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: inventory, Variation: 74. This monitors 32-period trends."""
    res = _fg_divergence(inventory, revenue if 'inventory' != 'revenue' else receivables, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_fake_growth_detector_revenue_base_w33_v075_signal(revenue) -> pd.Series:
    """Base feature for f47_fake_growth_detector. Input: revenue, Variation: 75. This monitors 33-period trends."""
    res = _fg_divergence(revenue, revenue if 'revenue' != 'revenue' else receivables, 33)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "receivables": np.random.normal(1000, 100, n).cumsum() + 1000,
        "inventory": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f47_fake_growth_detector_"))]
    
    print(f"Testing {len(funcs)} functions for f47_fake_growth_detector...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f47_fake_growth_detector_"))]}
F47_FAKE_GROWTH_DETECTOR_REGISTRY_BASE_001_075 = REGISTRY
