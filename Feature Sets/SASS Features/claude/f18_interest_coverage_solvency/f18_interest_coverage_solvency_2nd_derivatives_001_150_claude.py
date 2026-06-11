import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def f18ic_f18_interest_coverage_solvency_icovlvld_63d_slope_v001_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovlogd_126d_slope_v002_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovzd_63d_slope_v003_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovdispd_63d_slope_v004_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlvld_63d_slope_v005_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlogd_126d_slope_v006_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovzd_63d_slope_v007_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovdispd_63d_slope_v008_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlvld_63d_slope_v009_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlogd_126d_slope_v010_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovzd_63d_slope_v011_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovdispd_63d_slope_v012_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlvld_63d_slope_v013_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlogd_126d_slope_v014_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdzd_63d_slope_v015_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdemad_63d_slope_v016_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebddispd_63d_slope_v017_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlvld_63d_slope_v018_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlogd_126d_slope_v019_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdzd_63d_slope_v020_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebddispd_63d_slope_v021_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharelvld_63d_slope_v022_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharelogd_126d_slope_v023_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharezd_63d_slope_v024_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharedispd_63d_slope_v025_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscaplvld_63d_slope_v026_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscaplogd_126d_slope_v027_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapzd_63d_slope_v028_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapdispd_63d_slope_v029_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelvld_63d_slope_v030_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelogd_126d_slope_v031_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratezd_63d_slope_v032_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effrateemad_63d_slope_v033_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratedispd_63d_slope_v034_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intburdenemad_63d_slope_v035_signal(intexp, ebitda):
    R = intexp / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stdebtebdlvld_63d_slope_v036_signal(debtc, ebitda):
    R = debtc / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlvld_63d_slope_v037_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlogd_126d_slope_v038_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdzd_63d_slope_v039_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstddispd_63d_slope_v040_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliablvld_63d_slope_v041_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliablogd_126d_slope_v042_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabzd_63d_slope_v043_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabdispd_63d_slope_v044_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliablvld_63d_slope_v045_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliablogd_126d_slope_v046_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabzd_63d_slope_v047_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabdispd_63d_slope_v048_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratelvld_63d_slope_v049_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratelogd_126d_slope_v050_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratezd_63d_slope_v051_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratedispd_63d_slope_v052_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliablvld_63d_slope_v053_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliablogd_126d_slope_v054_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliabzd_63d_slope_v055_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliabdispd_63d_slope_v056_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliablvld_63d_slope_v057_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliablogd_126d_slope_v058_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliabzd_63d_slope_v059_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliabdispd_63d_slope_v060_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliablvld_63d_slope_v061_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliablogd_126d_slope_v062_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliabzd_63d_slope_v063_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliabdispd_63d_slope_v064_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtlvld_63d_slope_v065_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtlogd_126d_slope_v066_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtzd_63d_slope_v067_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtdispd_63d_slope_v068_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtlvld_63d_slope_v069_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtlogd_126d_slope_v070_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtzd_63d_slope_v071_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtdispd_63d_slope_v072_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundlvld_63d_slope_v073_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundlogd_126d_slope_v074_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundzd_63d_slope_v075_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffunddispd_63d_slope_v076_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionlvld_63d_slope_v077_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionlogd_126d_slope_v078_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionzd_63d_slope_v079_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushiondispd_63d_slope_v080_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgaplvld_63d_slope_v081_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgaplogd_126d_slope_v082_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgapzd_63d_slope_v083_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgapdispd_63d_slope_v084_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtlvld_63d_slope_v085_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtzd_63d_slope_v086_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtdispd_63d_slope_v087_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ltdebtebdlvld_63d_slope_v088_signal(debt, debtc, ebitda):
    R = (debt - debtc) / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ltdebtebdlogd_126d_slope_v089_signal(debt, debtc, ebitda):
    R = (debt - debtc) / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ltdebtebdzd_63d_slope_v090_signal(debt, debtc, ebitda):
    R = (debt - debtc) / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ltdebtebddispd_63d_slope_v091_signal(debt, debtc, ebitda):
    R = (debt - debtc) / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covefflvld_63d_slope_v092_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covefflogd_126d_slope_v093_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_coveffzd_63d_slope_v094_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_coveffdispd_63d_slope_v095_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnlvld_63d_slope_v096_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnlogd_126d_slope_v097_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnzd_63d_slope_v098_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturndispd_63d_slope_v099_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollrisklvld_63d_slope_v100_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollrisklogd_126d_slope_v101_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollriskzd_63d_slope_v102_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollriskdispd_63d_slope_v103_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stressemad_63d_slope_v104_signal(debt, ebitda, intexp):
    R = (debt / ebitda.replace(0, np.nan)) * (intexp / ebitda.replace(0, np.nan))
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevlvld_63d_slope_v105_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevlogd_126d_slope_v106_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevzd_63d_slope_v107_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevdispd_63d_slope_v108_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafelvld_63d_slope_v109_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _mean(R, 63)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafelogd_126d_slope_v110_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafezd_63d_slope_v111_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _z(R, 252)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafedispd_63d_slope_v112_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovlvld_63d_slope_v113_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovzd_63d_slope_v114_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovdispd_63d_slope_v115_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovconvd_126d_slope_v116_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * R.abs() ** 0.5, 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlvld_63d_slope_v117_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovzd_63d_slope_v118_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovdispd_63d_slope_v119_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlogd_126d_slope_v120_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovzd_63d_slope_v121_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovdispd_63d_slope_v122_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlvld_63d_slope_v123_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlogd_126d_slope_v124_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdzd_63d_slope_v125_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebddispd_63d_slope_v126_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlvld_63d_slope_v127_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlogd_126d_slope_v128_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdzd_63d_slope_v129_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebddispd_63d_slope_v130_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharelvld_63d_slope_v131_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharezd_63d_slope_v132_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharedispd_63d_slope_v133_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapzd_63d_slope_v134_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapdispd_63d_slope_v135_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapconvd_126d_slope_v136_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _mean(np.sign(R) * R.abs() ** 0.5, 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelvld_63d_slope_v137_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelogd_126d_slope_v138_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratezd_63d_slope_v139_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratedispd_63d_slope_v140_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intopsharelvld_63d_slope_v141_signal(intexp, opinc):
    R = intexp / opinc.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stdebtebdlvld_63d_slope_v142_signal(debtc, ebitda):
    R = debtc / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlvld_63d_slope_v143_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(R, 63)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlogd_126d_slope_v144_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdzd_63d_slope_v145_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstddispd_63d_slope_v146_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliablogd_126d_slope_v147_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabzd_63d_slope_v148_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabdispd_63d_slope_v149_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabzd_63d_slope_v150_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d = B - B.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f18ic_f18_interest_coverage_solvency_icovlvld_63d_slope_v001_signal,
    f18ic_f18_interest_coverage_solvency_icovlogd_126d_slope_v002_signal,
    f18ic_f18_interest_coverage_solvency_icovzd_63d_slope_v003_signal,
    f18ic_f18_interest_coverage_solvency_icovdispd_63d_slope_v004_signal,
    f18ic_f18_interest_coverage_solvency_ecovlvld_63d_slope_v005_signal,
    f18ic_f18_interest_coverage_solvency_ecovlogd_126d_slope_v006_signal,
    f18ic_f18_interest_coverage_solvency_ecovzd_63d_slope_v007_signal,
    f18ic_f18_interest_coverage_solvency_ecovdispd_63d_slope_v008_signal,
    f18ic_f18_interest_coverage_solvency_opcovlvld_63d_slope_v009_signal,
    f18ic_f18_interest_coverage_solvency_opcovlogd_126d_slope_v010_signal,
    f18ic_f18_interest_coverage_solvency_opcovzd_63d_slope_v011_signal,
    f18ic_f18_interest_coverage_solvency_opcovdispd_63d_slope_v012_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlvld_63d_slope_v013_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlogd_126d_slope_v014_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdzd_63d_slope_v015_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdemad_63d_slope_v016_signal,
    f18ic_f18_interest_coverage_solvency_dbtebddispd_63d_slope_v017_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlvld_63d_slope_v018_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlogd_126d_slope_v019_signal,
    f18ic_f18_interest_coverage_solvency_liabebdzd_63d_slope_v020_signal,
    f18ic_f18_interest_coverage_solvency_liabebddispd_63d_slope_v021_signal,
    f18ic_f18_interest_coverage_solvency_stsharelvld_63d_slope_v022_signal,
    f18ic_f18_interest_coverage_solvency_stsharelogd_126d_slope_v023_signal,
    f18ic_f18_interest_coverage_solvency_stsharezd_63d_slope_v024_signal,
    f18ic_f18_interest_coverage_solvency_stsharedispd_63d_slope_v025_signal,
    f18ic_f18_interest_coverage_solvency_dscaplvld_63d_slope_v026_signal,
    f18ic_f18_interest_coverage_solvency_dscaplogd_126d_slope_v027_signal,
    f18ic_f18_interest_coverage_solvency_dscapzd_63d_slope_v028_signal,
    f18ic_f18_interest_coverage_solvency_dscapdispd_63d_slope_v029_signal,
    f18ic_f18_interest_coverage_solvency_effratelvld_63d_slope_v030_signal,
    f18ic_f18_interest_coverage_solvency_effratelogd_126d_slope_v031_signal,
    f18ic_f18_interest_coverage_solvency_effratezd_63d_slope_v032_signal,
    f18ic_f18_interest_coverage_solvency_effrateemad_63d_slope_v033_signal,
    f18ic_f18_interest_coverage_solvency_effratedispd_63d_slope_v034_signal,
    f18ic_f18_interest_coverage_solvency_intburdenemad_63d_slope_v035_signal,
    f18ic_f18_interest_coverage_solvency_stdebtebdlvld_63d_slope_v036_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlvld_63d_slope_v037_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlogd_126d_slope_v038_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdzd_63d_slope_v039_signal,
    f18ic_f18_interest_coverage_solvency_ebitstddispd_63d_slope_v040_signal,
    f18ic_f18_interest_coverage_solvency_opincliablvld_63d_slope_v041_signal,
    f18ic_f18_interest_coverage_solvency_opincliablogd_126d_slope_v042_signal,
    f18ic_f18_interest_coverage_solvency_opincliabzd_63d_slope_v043_signal,
    f18ic_f18_interest_coverage_solvency_opincliabdispd_63d_slope_v044_signal,
    f18ic_f18_interest_coverage_solvency_ebitliablvld_63d_slope_v045_signal,
    f18ic_f18_interest_coverage_solvency_ebitliablogd_126d_slope_v046_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabzd_63d_slope_v047_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabdispd_63d_slope_v048_signal,
    f18ic_f18_interest_coverage_solvency_streffratelvld_63d_slope_v049_signal,
    f18ic_f18_interest_coverage_solvency_streffratelogd_126d_slope_v050_signal,
    f18ic_f18_interest_coverage_solvency_streffratezd_63d_slope_v051_signal,
    f18ic_f18_interest_coverage_solvency_streffratedispd_63d_slope_v052_signal,
    f18ic_f18_interest_coverage_solvency_intliablvld_63d_slope_v053_signal,
    f18ic_f18_interest_coverage_solvency_intliablogd_126d_slope_v054_signal,
    f18ic_f18_interest_coverage_solvency_intliabzd_63d_slope_v055_signal,
    f18ic_f18_interest_coverage_solvency_intliabdispd_63d_slope_v056_signal,
    f18ic_f18_interest_coverage_solvency_debtliablvld_63d_slope_v057_signal,
    f18ic_f18_interest_coverage_solvency_debtliablogd_126d_slope_v058_signal,
    f18ic_f18_interest_coverage_solvency_debtliabzd_63d_slope_v059_signal,
    f18ic_f18_interest_coverage_solvency_debtliabdispd_63d_slope_v060_signal,
    f18ic_f18_interest_coverage_solvency_stliablvld_63d_slope_v061_signal,
    f18ic_f18_interest_coverage_solvency_stliablogd_126d_slope_v062_signal,
    f18ic_f18_interest_coverage_solvency_stliabzd_63d_slope_v063_signal,
    f18ic_f18_interest_coverage_solvency_stliabdispd_63d_slope_v064_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtlvld_63d_slope_v065_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtlogd_126d_slope_v066_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtzd_63d_slope_v067_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtdispd_63d_slope_v068_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtlvld_63d_slope_v069_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtlogd_126d_slope_v070_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtzd_63d_slope_v071_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtdispd_63d_slope_v072_signal,
    f18ic_f18_interest_coverage_solvency_opselffundlvld_63d_slope_v073_signal,
    f18ic_f18_interest_coverage_solvency_opselffundlogd_126d_slope_v074_signal,
    f18ic_f18_interest_coverage_solvency_opselffundzd_63d_slope_v075_signal,
    f18ic_f18_interest_coverage_solvency_opselffunddispd_63d_slope_v076_signal,
    f18ic_f18_interest_coverage_solvency_dacushionlvld_63d_slope_v077_signal,
    f18ic_f18_interest_coverage_solvency_dacushionlogd_126d_slope_v078_signal,
    f18ic_f18_interest_coverage_solvency_dacushionzd_63d_slope_v079_signal,
    f18ic_f18_interest_coverage_solvency_dacushiondispd_63d_slope_v080_signal,
    f18ic_f18_interest_coverage_solvency_covqualgaplvld_63d_slope_v081_signal,
    f18ic_f18_interest_coverage_solvency_covqualgaplogd_126d_slope_v082_signal,
    f18ic_f18_interest_coverage_solvency_covqualgapzd_63d_slope_v083_signal,
    f18ic_f18_interest_coverage_solvency_covqualgapdispd_63d_slope_v084_signal,
    f18ic_f18_interest_coverage_solvency_nondebtlvld_63d_slope_v085_signal,
    f18ic_f18_interest_coverage_solvency_nondebtzd_63d_slope_v086_signal,
    f18ic_f18_interest_coverage_solvency_nondebtdispd_63d_slope_v087_signal,
    f18ic_f18_interest_coverage_solvency_ltdebtebdlvld_63d_slope_v088_signal,
    f18ic_f18_interest_coverage_solvency_ltdebtebdlogd_126d_slope_v089_signal,
    f18ic_f18_interest_coverage_solvency_ltdebtebdzd_63d_slope_v090_signal,
    f18ic_f18_interest_coverage_solvency_ltdebtebddispd_63d_slope_v091_signal,
    f18ic_f18_interest_coverage_solvency_covefflvld_63d_slope_v092_signal,
    f18ic_f18_interest_coverage_solvency_covefflogd_126d_slope_v093_signal,
    f18ic_f18_interest_coverage_solvency_coveffzd_63d_slope_v094_signal,
    f18ic_f18_interest_coverage_solvency_coveffdispd_63d_slope_v095_signal,
    f18ic_f18_interest_coverage_solvency_covperturnlvld_63d_slope_v096_signal,
    f18ic_f18_interest_coverage_solvency_covperturnlogd_126d_slope_v097_signal,
    f18ic_f18_interest_coverage_solvency_covperturnzd_63d_slope_v098_signal,
    f18ic_f18_interest_coverage_solvency_covperturndispd_63d_slope_v099_signal,
    f18ic_f18_interest_coverage_solvency_rollrisklvld_63d_slope_v100_signal,
    f18ic_f18_interest_coverage_solvency_rollrisklogd_126d_slope_v101_signal,
    f18ic_f18_interest_coverage_solvency_rollriskzd_63d_slope_v102_signal,
    f18ic_f18_interest_coverage_solvency_rollriskdispd_63d_slope_v103_signal,
    f18ic_f18_interest_coverage_solvency_stressemad_63d_slope_v104_signal,
    f18ic_f18_interest_coverage_solvency_refilevlvld_63d_slope_v105_signal,
    f18ic_f18_interest_coverage_solvency_refilevlogd_126d_slope_v106_signal,
    f18ic_f18_interest_coverage_solvency_refilevzd_63d_slope_v107_signal,
    f18ic_f18_interest_coverage_solvency_refilevdispd_63d_slope_v108_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafelvld_63d_slope_v109_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafelogd_126d_slope_v110_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafezd_63d_slope_v111_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafedispd_63d_slope_v112_signal,
    f18ic_f18_interest_coverage_solvency_icovlvld_63d_slope_v113_signal,
    f18ic_f18_interest_coverage_solvency_icovzd_63d_slope_v114_signal,
    f18ic_f18_interest_coverage_solvency_icovdispd_63d_slope_v115_signal,
    f18ic_f18_interest_coverage_solvency_icovconvd_126d_slope_v116_signal,
    f18ic_f18_interest_coverage_solvency_ecovlvld_63d_slope_v117_signal,
    f18ic_f18_interest_coverage_solvency_ecovzd_63d_slope_v118_signal,
    f18ic_f18_interest_coverage_solvency_ecovdispd_63d_slope_v119_signal,
    f18ic_f18_interest_coverage_solvency_opcovlogd_126d_slope_v120_signal,
    f18ic_f18_interest_coverage_solvency_opcovzd_63d_slope_v121_signal,
    f18ic_f18_interest_coverage_solvency_opcovdispd_63d_slope_v122_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlvld_63d_slope_v123_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlogd_126d_slope_v124_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdzd_63d_slope_v125_signal,
    f18ic_f18_interest_coverage_solvency_dbtebddispd_63d_slope_v126_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlvld_63d_slope_v127_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlogd_126d_slope_v128_signal,
    f18ic_f18_interest_coverage_solvency_liabebdzd_63d_slope_v129_signal,
    f18ic_f18_interest_coverage_solvency_liabebddispd_63d_slope_v130_signal,
    f18ic_f18_interest_coverage_solvency_stsharelvld_63d_slope_v131_signal,
    f18ic_f18_interest_coverage_solvency_stsharezd_63d_slope_v132_signal,
    f18ic_f18_interest_coverage_solvency_stsharedispd_63d_slope_v133_signal,
    f18ic_f18_interest_coverage_solvency_dscapzd_63d_slope_v134_signal,
    f18ic_f18_interest_coverage_solvency_dscapdispd_63d_slope_v135_signal,
    f18ic_f18_interest_coverage_solvency_dscapconvd_126d_slope_v136_signal,
    f18ic_f18_interest_coverage_solvency_effratelvld_63d_slope_v137_signal,
    f18ic_f18_interest_coverage_solvency_effratelogd_126d_slope_v138_signal,
    f18ic_f18_interest_coverage_solvency_effratezd_63d_slope_v139_signal,
    f18ic_f18_interest_coverage_solvency_effratedispd_63d_slope_v140_signal,
    f18ic_f18_interest_coverage_solvency_intopsharelvld_63d_slope_v141_signal,
    f18ic_f18_interest_coverage_solvency_stdebtebdlvld_63d_slope_v142_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlvld_63d_slope_v143_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlogd_126d_slope_v144_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdzd_63d_slope_v145_signal,
    f18ic_f18_interest_coverage_solvency_ebitstddispd_63d_slope_v146_signal,
    f18ic_f18_interest_coverage_solvency_opincliablogd_126d_slope_v147_signal,
    f18ic_f18_interest_coverage_solvency_opincliabzd_63d_slope_v148_signal,
    f18ic_f18_interest_coverage_solvency_opincliabdispd_63d_slope_v149_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabzd_63d_slope_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INTEREST_COVERAGE_SOLVENCY_REGISTRY_SLOPE_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ebit = _fund(101, base=2e8, drift=0.02, vol=0.06, allow_neg=True).rename("ebit")
    ebitda = _fund(102, base=3e8, drift=0.02, vol=0.05).rename("ebitda")
    intexp = _fund(103, base=2e7, drift=0.01, vol=0.04).rename("intexp")
    debt = _fund(104, base=1.2e9, drift=0.015, vol=0.04).rename("debt")
    debtc = _fund(105, base=3e8, drift=0.015, vol=0.05).rename("debtc")
    liabilities = _fund(106, base=2e9, drift=0.015, vol=0.04).rename("liabilities")
    opinc = _fund(107, base=2.2e8, drift=0.02, vol=0.06, allow_neg=True).rename("opinc")

    cols = {"ebit": ebit, "ebitda": ebitda, "intexp": intexp, "debt": debt,
            "debtc": debtc, "liabilities": liabilities, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f18_interest_coverage_solvency_2nd_derivatives_001_150_claude: %d features pass" % n_features)
