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


def f18ic_f18_interest_coverage_solvency_icovlvld2_63d_jerk_v001_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovlogd2_126d_jerk_v002_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovzd2_63d_jerk_v003_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovemad2_63d_jerk_v004_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovdispd2_63d_jerk_v005_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlvld2_63d_jerk_v006_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlogd2_126d_jerk_v007_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovzd2_63d_jerk_v008_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovemad2_63d_jerk_v009_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovdispd2_63d_jerk_v010_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlvld2_63d_jerk_v011_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlogd2_126d_jerk_v012_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovzd2_63d_jerk_v013_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovemad2_63d_jerk_v014_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovdispd2_63d_jerk_v015_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlvld2_63d_jerk_v016_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlogd2_126d_jerk_v017_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdzd2_63d_jerk_v018_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdemad2_63d_jerk_v019_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebddispd2_63d_jerk_v020_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlvld2_63d_jerk_v021_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdlogd2_126d_jerk_v022_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdzd2_63d_jerk_v023_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebdemad2_63d_jerk_v024_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_liabebddispd2_63d_jerk_v025_signal(liabilities, ebitda):
    R = liabilities / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharelvld2_63d_jerk_v026_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharelogd2_126d_jerk_v027_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharezd2_63d_jerk_v028_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stshareemad2_63d_jerk_v029_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stsharedispd2_63d_jerk_v030_signal(debtc, debt):
    R = debtc / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscaplvld2_63d_jerk_v031_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscaplogd2_126d_jerk_v032_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapzd2_63d_jerk_v033_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapemad2_63d_jerk_v034_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dscapdispd2_63d_jerk_v035_signal(ebitda, debtc, intexp):
    R = ebitda / (debtc + intexp).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelvld2_63d_jerk_v036_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratelogd2_126d_jerk_v037_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratezd2_63d_jerk_v038_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effrateemad2_63d_jerk_v039_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_effratedispd2_63d_jerk_v040_signal(intexp, debt):
    R = intexp / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intopsharedispd2_63d_jerk_v041_signal(intexp, opinc):
    R = intexp / opinc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stdebtebdlvld2_63d_jerk_v042_signal(debtc, ebitda):
    R = debtc / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stdebtebdemad2_63d_jerk_v043_signal(debtc, ebitda):
    R = debtc / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlvld2_63d_jerk_v044_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdlogd2_126d_jerk_v045_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdzd2_63d_jerk_v046_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstdemad2_63d_jerk_v047_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitstddispd2_63d_jerk_v048_signal(ebit, debtc):
    R = ebit / debtc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliablvld2_63d_jerk_v049_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliablogd2_126d_jerk_v050_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabzd2_63d_jerk_v051_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabemad2_63d_jerk_v052_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincliabdispd2_63d_jerk_v053_signal(opinc, liabilities):
    R = opinc / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliablvld2_63d_jerk_v054_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliablogd2_126d_jerk_v055_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabzd2_63d_jerk_v056_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabemad2_63d_jerk_v057_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitliabdispd2_63d_jerk_v058_signal(ebit, liabilities):
    R = ebit / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratelvld2_63d_jerk_v059_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratelogd2_126d_jerk_v060_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratezd2_63d_jerk_v061_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffrateemad2_63d_jerk_v062_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_streffratedispd2_63d_jerk_v063_signal(intexp, debtc):
    R = intexp / debtc.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliablvld2_63d_jerk_v064_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliablogd2_126d_jerk_v065_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliabzd2_63d_jerk_v066_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliabemad2_63d_jerk_v067_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_intliabdispd2_63d_jerk_v068_signal(intexp, liabilities):
    R = intexp / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliablvld2_63d_jerk_v069_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliablogd2_126d_jerk_v070_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliabzd2_63d_jerk_v071_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliabemad2_63d_jerk_v072_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_debtliabdispd2_63d_jerk_v073_signal(debt, liabilities):
    R = debt / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliablvld2_63d_jerk_v074_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliablogd2_126d_jerk_v075_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliabzd2_63d_jerk_v076_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliabemad2_63d_jerk_v077_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_stliabdispd2_63d_jerk_v078_signal(debtc, liabilities):
    R = debtc / liabilities.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtlvld2_63d_jerk_v079_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtlogd2_126d_jerk_v080_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtzd2_63d_jerk_v081_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtemad2_63d_jerk_v082_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opincdebtdispd2_63d_jerk_v083_signal(opinc, debt):
    R = opinc / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtlvld2_63d_jerk_v084_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtlogd2_126d_jerk_v085_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtzd2_63d_jerk_v086_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtemad2_63d_jerk_v087_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ebitdebtdispd2_63d_jerk_v088_signal(ebit, debt):
    R = ebit / debt.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundlvld2_63d_jerk_v089_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundlogd2_126d_jerk_v090_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundzd2_63d_jerk_v091_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffundemad2_63d_jerk_v092_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opselffunddispd2_63d_jerk_v093_signal(opinc, debtc, intexp):
    R = opinc / (debtc + intexp).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionlvld2_63d_jerk_v094_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionlogd2_126d_jerk_v095_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionzd2_63d_jerk_v096_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushionemad2_63d_jerk_v097_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dacushiondispd2_63d_jerk_v098_signal(ebit, ebitda, intexp):
    R = (ebitda - ebit) / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgaplvld2_63d_jerk_v099_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgaplogd2_126d_jerk_v100_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgapzd2_63d_jerk_v101_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgapemad2_63d_jerk_v102_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covqualgapdispd2_63d_jerk_v103_signal(ebit, opinc, intexp):
    R = (ebit - opinc) / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtlvld2_63d_jerk_v104_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtlogd2_126d_jerk_v105_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtzd2_63d_jerk_v106_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtemad2_63d_jerk_v107_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_nondebtdispd2_63d_jerk_v108_signal(liabilities, debt, ebitda):
    R = (liabilities - debt) / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ltdebtebddispd2_63d_jerk_v109_signal(debt, debtc, ebitda):
    R = (debt - debtc) / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covefflvld2_63d_jerk_v110_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covefflogd2_126d_jerk_v111_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_coveffzd2_63d_jerk_v112_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_coveffemad2_63d_jerk_v113_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_coveffdispd2_63d_jerk_v114_signal(ebitda, intexp, debt):
    R = (ebitda / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnlvld2_63d_jerk_v115_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnlogd2_126d_jerk_v116_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnzd2_63d_jerk_v117_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturnemad2_63d_jerk_v118_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_covperturndispd2_63d_jerk_v119_signal(ebit, intexp, debt, ebitda):
    R = (ebit / intexp.replace(0, np.nan)) / (debt / ebitda.replace(0, np.nan)).replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollrisklvld2_63d_jerk_v120_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollriskzd2_63d_jerk_v121_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollriskemad2_63d_jerk_v122_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_rollriskdispd2_63d_jerk_v123_signal(debtc, debt, intexp):
    R = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevlvld2_63d_jerk_v124_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevlogd2_126d_jerk_v125_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevzd2_63d_jerk_v126_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevemad2_63d_jerk_v127_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_refilevdispd2_63d_jerk_v128_signal(debtc, debt, liabilities, ebitda):
    R = (debtc / debt.replace(0, np.nan)) * (liabilities / ebitda.replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafelvld2_63d_jerk_v129_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _mean(R, 63)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafelogd2_126d_jerk_v130_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafezd2_63d_jerk_v131_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _z(R, 252)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafeemad2_63d_jerk_v132_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_compoundsafedispd2_63d_jerk_v133_signal(ebit, intexp, ebitda, debtc):
    R = ((ebit - intexp) / intexp.replace(0, np.nan)) * (ebitda / (debtc + intexp).replace(0, np.nan))
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovlvld2_63d_jerk_v134_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovlogd2_126d_jerk_v135_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovzd2_63d_jerk_v136_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_icovdispd2_63d_jerk_v137_signal(ebit, intexp):
    R = ebit / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlvld2_63d_jerk_v138_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovlogd2_126d_jerk_v139_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovzd2_63d_jerk_v140_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_ecovdispd2_63d_jerk_v141_signal(ebitda, intexp):
    R = ebitda / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlvld2_63d_jerk_v142_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovlogd2_126d_jerk_v143_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovzd2_63d_jerk_v144_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_opcovdispd2_63d_jerk_v145_signal(opinc, intexp):
    R = opinc / intexp.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlvld2_63d_jerk_v146_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(R, 63)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdlogd2_126d_jerk_v147_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _mean(np.sign(R) * np.log1p(R.abs()), 126)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdzd2_63d_jerk_v148_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _z(R, 252)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebdemad2_63d_jerk_v149_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = R.ewm(span=63, min_periods=max(2, 63//2)).mean()
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f18ic_f18_interest_coverage_solvency_dbtebddispd2_63d_jerk_v150_signal(debt, ebitda):
    R = debt / ebitda.replace(0, np.nan)
    B = _std(R, 252) / _mean(R, 252).abs().replace(0, np.nan)
    d1 = B - B.shift(63)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f18ic_f18_interest_coverage_solvency_icovlvld2_63d_jerk_v001_signal,
    f18ic_f18_interest_coverage_solvency_icovlogd2_126d_jerk_v002_signal,
    f18ic_f18_interest_coverage_solvency_icovzd2_63d_jerk_v003_signal,
    f18ic_f18_interest_coverage_solvency_icovemad2_63d_jerk_v004_signal,
    f18ic_f18_interest_coverage_solvency_icovdispd2_63d_jerk_v005_signal,
    f18ic_f18_interest_coverage_solvency_ecovlvld2_63d_jerk_v006_signal,
    f18ic_f18_interest_coverage_solvency_ecovlogd2_126d_jerk_v007_signal,
    f18ic_f18_interest_coverage_solvency_ecovzd2_63d_jerk_v008_signal,
    f18ic_f18_interest_coverage_solvency_ecovemad2_63d_jerk_v009_signal,
    f18ic_f18_interest_coverage_solvency_ecovdispd2_63d_jerk_v010_signal,
    f18ic_f18_interest_coverage_solvency_opcovlvld2_63d_jerk_v011_signal,
    f18ic_f18_interest_coverage_solvency_opcovlogd2_126d_jerk_v012_signal,
    f18ic_f18_interest_coverage_solvency_opcovzd2_63d_jerk_v013_signal,
    f18ic_f18_interest_coverage_solvency_opcovemad2_63d_jerk_v014_signal,
    f18ic_f18_interest_coverage_solvency_opcovdispd2_63d_jerk_v015_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlvld2_63d_jerk_v016_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlogd2_126d_jerk_v017_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdzd2_63d_jerk_v018_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdemad2_63d_jerk_v019_signal,
    f18ic_f18_interest_coverage_solvency_dbtebddispd2_63d_jerk_v020_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlvld2_63d_jerk_v021_signal,
    f18ic_f18_interest_coverage_solvency_liabebdlogd2_126d_jerk_v022_signal,
    f18ic_f18_interest_coverage_solvency_liabebdzd2_63d_jerk_v023_signal,
    f18ic_f18_interest_coverage_solvency_liabebdemad2_63d_jerk_v024_signal,
    f18ic_f18_interest_coverage_solvency_liabebddispd2_63d_jerk_v025_signal,
    f18ic_f18_interest_coverage_solvency_stsharelvld2_63d_jerk_v026_signal,
    f18ic_f18_interest_coverage_solvency_stsharelogd2_126d_jerk_v027_signal,
    f18ic_f18_interest_coverage_solvency_stsharezd2_63d_jerk_v028_signal,
    f18ic_f18_interest_coverage_solvency_stshareemad2_63d_jerk_v029_signal,
    f18ic_f18_interest_coverage_solvency_stsharedispd2_63d_jerk_v030_signal,
    f18ic_f18_interest_coverage_solvency_dscaplvld2_63d_jerk_v031_signal,
    f18ic_f18_interest_coverage_solvency_dscaplogd2_126d_jerk_v032_signal,
    f18ic_f18_interest_coverage_solvency_dscapzd2_63d_jerk_v033_signal,
    f18ic_f18_interest_coverage_solvency_dscapemad2_63d_jerk_v034_signal,
    f18ic_f18_interest_coverage_solvency_dscapdispd2_63d_jerk_v035_signal,
    f18ic_f18_interest_coverage_solvency_effratelvld2_63d_jerk_v036_signal,
    f18ic_f18_interest_coverage_solvency_effratelogd2_126d_jerk_v037_signal,
    f18ic_f18_interest_coverage_solvency_effratezd2_63d_jerk_v038_signal,
    f18ic_f18_interest_coverage_solvency_effrateemad2_63d_jerk_v039_signal,
    f18ic_f18_interest_coverage_solvency_effratedispd2_63d_jerk_v040_signal,
    f18ic_f18_interest_coverage_solvency_intopsharedispd2_63d_jerk_v041_signal,
    f18ic_f18_interest_coverage_solvency_stdebtebdlvld2_63d_jerk_v042_signal,
    f18ic_f18_interest_coverage_solvency_stdebtebdemad2_63d_jerk_v043_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlvld2_63d_jerk_v044_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdlogd2_126d_jerk_v045_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdzd2_63d_jerk_v046_signal,
    f18ic_f18_interest_coverage_solvency_ebitstdemad2_63d_jerk_v047_signal,
    f18ic_f18_interest_coverage_solvency_ebitstddispd2_63d_jerk_v048_signal,
    f18ic_f18_interest_coverage_solvency_opincliablvld2_63d_jerk_v049_signal,
    f18ic_f18_interest_coverage_solvency_opincliablogd2_126d_jerk_v050_signal,
    f18ic_f18_interest_coverage_solvency_opincliabzd2_63d_jerk_v051_signal,
    f18ic_f18_interest_coverage_solvency_opincliabemad2_63d_jerk_v052_signal,
    f18ic_f18_interest_coverage_solvency_opincliabdispd2_63d_jerk_v053_signal,
    f18ic_f18_interest_coverage_solvency_ebitliablvld2_63d_jerk_v054_signal,
    f18ic_f18_interest_coverage_solvency_ebitliablogd2_126d_jerk_v055_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabzd2_63d_jerk_v056_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabemad2_63d_jerk_v057_signal,
    f18ic_f18_interest_coverage_solvency_ebitliabdispd2_63d_jerk_v058_signal,
    f18ic_f18_interest_coverage_solvency_streffratelvld2_63d_jerk_v059_signal,
    f18ic_f18_interest_coverage_solvency_streffratelogd2_126d_jerk_v060_signal,
    f18ic_f18_interest_coverage_solvency_streffratezd2_63d_jerk_v061_signal,
    f18ic_f18_interest_coverage_solvency_streffrateemad2_63d_jerk_v062_signal,
    f18ic_f18_interest_coverage_solvency_streffratedispd2_63d_jerk_v063_signal,
    f18ic_f18_interest_coverage_solvency_intliablvld2_63d_jerk_v064_signal,
    f18ic_f18_interest_coverage_solvency_intliablogd2_126d_jerk_v065_signal,
    f18ic_f18_interest_coverage_solvency_intliabzd2_63d_jerk_v066_signal,
    f18ic_f18_interest_coverage_solvency_intliabemad2_63d_jerk_v067_signal,
    f18ic_f18_interest_coverage_solvency_intliabdispd2_63d_jerk_v068_signal,
    f18ic_f18_interest_coverage_solvency_debtliablvld2_63d_jerk_v069_signal,
    f18ic_f18_interest_coverage_solvency_debtliablogd2_126d_jerk_v070_signal,
    f18ic_f18_interest_coverage_solvency_debtliabzd2_63d_jerk_v071_signal,
    f18ic_f18_interest_coverage_solvency_debtliabemad2_63d_jerk_v072_signal,
    f18ic_f18_interest_coverage_solvency_debtliabdispd2_63d_jerk_v073_signal,
    f18ic_f18_interest_coverage_solvency_stliablvld2_63d_jerk_v074_signal,
    f18ic_f18_interest_coverage_solvency_stliablogd2_126d_jerk_v075_signal,
    f18ic_f18_interest_coverage_solvency_stliabzd2_63d_jerk_v076_signal,
    f18ic_f18_interest_coverage_solvency_stliabemad2_63d_jerk_v077_signal,
    f18ic_f18_interest_coverage_solvency_stliabdispd2_63d_jerk_v078_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtlvld2_63d_jerk_v079_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtlogd2_126d_jerk_v080_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtzd2_63d_jerk_v081_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtemad2_63d_jerk_v082_signal,
    f18ic_f18_interest_coverage_solvency_opincdebtdispd2_63d_jerk_v083_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtlvld2_63d_jerk_v084_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtlogd2_126d_jerk_v085_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtzd2_63d_jerk_v086_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtemad2_63d_jerk_v087_signal,
    f18ic_f18_interest_coverage_solvency_ebitdebtdispd2_63d_jerk_v088_signal,
    f18ic_f18_interest_coverage_solvency_opselffundlvld2_63d_jerk_v089_signal,
    f18ic_f18_interest_coverage_solvency_opselffundlogd2_126d_jerk_v090_signal,
    f18ic_f18_interest_coverage_solvency_opselffundzd2_63d_jerk_v091_signal,
    f18ic_f18_interest_coverage_solvency_opselffundemad2_63d_jerk_v092_signal,
    f18ic_f18_interest_coverage_solvency_opselffunddispd2_63d_jerk_v093_signal,
    f18ic_f18_interest_coverage_solvency_dacushionlvld2_63d_jerk_v094_signal,
    f18ic_f18_interest_coverage_solvency_dacushionlogd2_126d_jerk_v095_signal,
    f18ic_f18_interest_coverage_solvency_dacushionzd2_63d_jerk_v096_signal,
    f18ic_f18_interest_coverage_solvency_dacushionemad2_63d_jerk_v097_signal,
    f18ic_f18_interest_coverage_solvency_dacushiondispd2_63d_jerk_v098_signal,
    f18ic_f18_interest_coverage_solvency_covqualgaplvld2_63d_jerk_v099_signal,
    f18ic_f18_interest_coverage_solvency_covqualgaplogd2_126d_jerk_v100_signal,
    f18ic_f18_interest_coverage_solvency_covqualgapzd2_63d_jerk_v101_signal,
    f18ic_f18_interest_coverage_solvency_covqualgapemad2_63d_jerk_v102_signal,
    f18ic_f18_interest_coverage_solvency_covqualgapdispd2_63d_jerk_v103_signal,
    f18ic_f18_interest_coverage_solvency_nondebtlvld2_63d_jerk_v104_signal,
    f18ic_f18_interest_coverage_solvency_nondebtlogd2_126d_jerk_v105_signal,
    f18ic_f18_interest_coverage_solvency_nondebtzd2_63d_jerk_v106_signal,
    f18ic_f18_interest_coverage_solvency_nondebtemad2_63d_jerk_v107_signal,
    f18ic_f18_interest_coverage_solvency_nondebtdispd2_63d_jerk_v108_signal,
    f18ic_f18_interest_coverage_solvency_ltdebtebddispd2_63d_jerk_v109_signal,
    f18ic_f18_interest_coverage_solvency_covefflvld2_63d_jerk_v110_signal,
    f18ic_f18_interest_coverage_solvency_covefflogd2_126d_jerk_v111_signal,
    f18ic_f18_interest_coverage_solvency_coveffzd2_63d_jerk_v112_signal,
    f18ic_f18_interest_coverage_solvency_coveffemad2_63d_jerk_v113_signal,
    f18ic_f18_interest_coverage_solvency_coveffdispd2_63d_jerk_v114_signal,
    f18ic_f18_interest_coverage_solvency_covperturnlvld2_63d_jerk_v115_signal,
    f18ic_f18_interest_coverage_solvency_covperturnlogd2_126d_jerk_v116_signal,
    f18ic_f18_interest_coverage_solvency_covperturnzd2_63d_jerk_v117_signal,
    f18ic_f18_interest_coverage_solvency_covperturnemad2_63d_jerk_v118_signal,
    f18ic_f18_interest_coverage_solvency_covperturndispd2_63d_jerk_v119_signal,
    f18ic_f18_interest_coverage_solvency_rollrisklvld2_63d_jerk_v120_signal,
    f18ic_f18_interest_coverage_solvency_rollriskzd2_63d_jerk_v121_signal,
    f18ic_f18_interest_coverage_solvency_rollriskemad2_63d_jerk_v122_signal,
    f18ic_f18_interest_coverage_solvency_rollriskdispd2_63d_jerk_v123_signal,
    f18ic_f18_interest_coverage_solvency_refilevlvld2_63d_jerk_v124_signal,
    f18ic_f18_interest_coverage_solvency_refilevlogd2_126d_jerk_v125_signal,
    f18ic_f18_interest_coverage_solvency_refilevzd2_63d_jerk_v126_signal,
    f18ic_f18_interest_coverage_solvency_refilevemad2_63d_jerk_v127_signal,
    f18ic_f18_interest_coverage_solvency_refilevdispd2_63d_jerk_v128_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafelvld2_63d_jerk_v129_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafelogd2_126d_jerk_v130_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafezd2_63d_jerk_v131_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafeemad2_63d_jerk_v132_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafedispd2_63d_jerk_v133_signal,
    f18ic_f18_interest_coverage_solvency_icovlvld2_63d_jerk_v134_signal,
    f18ic_f18_interest_coverage_solvency_icovlogd2_126d_jerk_v135_signal,
    f18ic_f18_interest_coverage_solvency_icovzd2_63d_jerk_v136_signal,
    f18ic_f18_interest_coverage_solvency_icovdispd2_63d_jerk_v137_signal,
    f18ic_f18_interest_coverage_solvency_ecovlvld2_63d_jerk_v138_signal,
    f18ic_f18_interest_coverage_solvency_ecovlogd2_126d_jerk_v139_signal,
    f18ic_f18_interest_coverage_solvency_ecovzd2_63d_jerk_v140_signal,
    f18ic_f18_interest_coverage_solvency_ecovdispd2_63d_jerk_v141_signal,
    f18ic_f18_interest_coverage_solvency_opcovlvld2_63d_jerk_v142_signal,
    f18ic_f18_interest_coverage_solvency_opcovlogd2_126d_jerk_v143_signal,
    f18ic_f18_interest_coverage_solvency_opcovzd2_63d_jerk_v144_signal,
    f18ic_f18_interest_coverage_solvency_opcovdispd2_63d_jerk_v145_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlvld2_63d_jerk_v146_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdlogd2_126d_jerk_v147_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdzd2_63d_jerk_v148_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdemad2_63d_jerk_v149_signal,
    f18ic_f18_interest_coverage_solvency_dbtebddispd2_63d_jerk_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INTEREST_COVERAGE_SOLVENCY_REGISTRY_JERK_001_150 = REGISTRY


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

    print("OK f18_interest_coverage_solvency_3rd_derivatives_001_150_claude: %d features pass" % n_features)
