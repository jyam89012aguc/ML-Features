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

def _bd_risk(debt, cash, w): return (debt - cash).rolling(w).mean()

def f49_balance_sheet_death_spiral_cash_slope_w22_s6_v001_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 1. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s7_v002_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 2. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s8_v003_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 3. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s9_v004_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 4. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s10_v005_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 5. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s11_v006_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 6. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s12_v007_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 7. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s13_v008_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 8. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s14_v009_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 9. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s5_v010_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 10. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s6_v011_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 11. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s7_v012_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 12. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s8_v013_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 13. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s9_v014_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 14. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s10_v015_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 15. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s11_v016_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 16. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s12_v017_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 17. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s13_v018_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 18. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s14_v019_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 19. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s5_v020_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 20. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s6_v021_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 21. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s7_v022_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 22. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s8_v023_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 23. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s9_v024_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 24. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s10_v025_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 25. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s11_v026_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 26. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s12_v027_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 27. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s13_v028_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 28. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s14_v029_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 29. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s5_v030_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 30. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s6_v031_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 31. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s7_v032_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 32. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s8_v033_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 33. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s9_v034_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 34. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s10_v035_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 35. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s11_v036_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 36. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s12_v037_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 37. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s13_v038_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 38. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s14_v039_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 39. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s5_v040_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 40. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s6_v041_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 41. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s7_v042_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 42. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s8_v043_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 43. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s9_v044_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 44. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s10_v045_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 45. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s11_v046_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 46. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s12_v047_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 47. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s13_v048_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 48. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s14_v049_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 49. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s5_v050_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 50. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s6_v051_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 51. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s7_v052_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 52. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s8_v053_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 53. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s9_v054_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 54. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s10_v055_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 55. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s11_v056_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 56. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s12_v057_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 57. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s13_v058_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 58. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s14_v059_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 59. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s5_v060_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 60. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s6_v061_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 61. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s7_v062_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 62. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s8_v063_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 63. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s9_v064_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 64. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s10_v065_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 65. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s11_v066_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 66. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s12_v067_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 67. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s13_v068_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 68. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s14_v069_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 69. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s5_v070_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 70. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s6_v071_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 71. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s7_v072_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 72. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s8_v073_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 73. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s9_v074_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 74. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s10_v075_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 75. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s11_v076_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 76. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s12_v077_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 77. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s13_v078_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 78. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s14_v079_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 79. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s5_v080_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 80. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s6_v081_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 81. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s7_v082_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 82. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s8_v083_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 83. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s9_v084_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 84. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s10_v085_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 85. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s11_v086_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 86. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s12_v087_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 87. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s13_v088_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 88. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s14_v089_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 89. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s5_v090_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 90. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s6_v091_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 91. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s7_v092_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 92. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s8_v093_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 93. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s9_v094_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 94. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s10_v095_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 95. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s11_v096_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 96. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s12_v097_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 97. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s13_v098_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 98. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s14_v099_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 99. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s5_v100_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 100. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s6_v101_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 101. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s7_v102_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 102. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s8_v103_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 103. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s9_v104_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 104. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s10_v105_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 105. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s11_v106_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 106. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s12_v107_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 107. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s13_v108_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 108. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s14_v109_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 109. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s5_v110_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 110. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s6_v111_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 111. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s7_v112_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 112. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s8_v113_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 113. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s9_v114_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 114. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s10_v115_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 115. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s11_v116_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 116. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s12_v117_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 117. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s13_v118_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 118. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s14_v119_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 119. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s5_v120_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 120. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s6_v121_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 121. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s7_v122_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 122. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s8_v123_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 123. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s9_v124_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 124. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s10_v125_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 125. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s11_v126_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 126. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s12_v127_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 127. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s13_v128_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 128. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s14_v129_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 129. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w25_s5_v130_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 130. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 25)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w26_s6_v131_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 131. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 26)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w27_s7_v132_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 132. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 27)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w28_s8_v133_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 133. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 28)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w29_s9_v134_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 134. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 29)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w30_s10_v135_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 135. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 30)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w31_s11_v136_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 136. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 31)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w32_s12_v137_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 137. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 32)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w33_s13_v138_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 138. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 33)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w34_s14_v139_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 139. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 34)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w35_s5_v140_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 140. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 35)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w36_s6_v141_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 141. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 36)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w37_s7_v142_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 142. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 37)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w38_s8_v143_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 143. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 38)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w39_s9_v144_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 144. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 39)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w40_s10_v145_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 145. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 40)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w41_s11_v146_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 146. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 41)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w21_s12_v147_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 147. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 21)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_cash_slope_w22_s13_v148_signal(cash) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: cash, Variation: 148. Captures rate of change."""
    base = _bd_risk(cash, cash if 'cash' != 'cash' else debt, 22)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_equity_slope_w23_s14_v149_signal(equity) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: equity, Variation: 149. Captures rate of change."""
    base = _bd_risk(equity, cash if 'equity' != 'cash' else debt, 23)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_balance_sheet_death_spiral_debt_slope_w24_s5_v150_signal(debt) -> pd.Series:
    """Slope feature for f49_balance_sheet_death_spiral. Input: debt, Variation: 150. Captures rate of change."""
    base = _bd_risk(debt, cash if 'debt' != 'cash' else debt, 24)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "debt": np.random.normal(500, 100, n).cumsum() + 1000,
        "cash": np.random.normal(1000, 100, n).cumsum() + 1000,
        "equity": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f49_balance_sheet_death_spiral_"))]
    
    print(f"Testing {len(funcs)} functions for f49_balance_sheet_death_spiral...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f49_balance_sheet_death_spiral_"))]}
F49_BALANCE_SHEET_DEATH_SPIRAL_REGISTRY_SLOPE_001_150 = REGISTRY
