import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f007_liquid(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f007_liquid_to_liab(cashneq, investmentsc, liabilities):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilities.replace(0, np.nan).abs()


def _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilitiesc.replace(0, np.nan).abs()


def cg_f007_liabilities_coverage_liq_to_liab_mean_21d_base_v001_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_mean_63d_base_v002_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_mean_126d_base_v003_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_mean_252d_base_v004_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_mean_504d_base_v005_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_mean_21d_base_v006_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_mean_63d_base_v007_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_mean_126d_base_v008_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_mean_252d_base_v009_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_mean_504d_base_v010_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_mean_21d_base_v011_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_mean_63d_base_v012_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_mean_126d_base_v013_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_mean_252d_base_v014_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_mean_504d_base_v015_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_mean_21d_base_v016_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_mean_63d_base_v017_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_mean_126d_base_v018_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_mean_252d_base_v019_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_mean_504d_base_v020_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_mean_21d_base_v021_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_mean_63d_base_v022_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_mean_126d_base_v023_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_mean_252d_base_v024_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_mean_504d_base_v025_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_mean_21d_base_v026_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_mean_63d_base_v027_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_mean_126d_base_v028_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_mean_252d_base_v029_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_mean_504d_base_v030_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_mean_21d_base_v031_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_mean_63d_base_v032_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_mean_126d_base_v033_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_mean_252d_base_v034_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_mean_504d_base_v035_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_median_63d_base_v036_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_median_252d_base_v037_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_median_504d_base_v038_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_median_63d_base_v039_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_median_252d_base_v040_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_median_504d_base_v041_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_median_63d_base_v042_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_median_252d_base_v043_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_median_504d_base_v044_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_median_63d_base_v045_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_median_252d_base_v046_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_median_504d_base_v047_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_median_63d_base_v048_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_median_252d_base_v049_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_median_504d_base_v050_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_median_63d_base_v051_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_median_252d_base_v052_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_median_504d_base_v053_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_median_63d_base_v054_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_median_252d_base_v055_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_median_504d_base_v056_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_rmax_252d_base_v057_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_rmax_504d_base_v058_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_rmax_252d_base_v059_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_rmax_504d_base_v060_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_rmax_252d_base_v061_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_rmax_504d_base_v062_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_rmax_252d_base_v063_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_curliab_share_rmax_504d_base_v064_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_rmax_252d_base_v065_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_minus_curliab_rmax_504d_base_v066_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_rmax_252d_base_v067_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_netliq_to_mcap_rmax_504d_base_v068_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_rmax_252d_base_v069_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_drev_rmax_504d_base_v070_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_rmin_252d_base_v071_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_liab_rmin_504d_base_v072_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_rmin_252d_base_v073_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_curliab_rmin_504d_base_v074_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f007_liabilities_coverage_liq_to_ncliab_rmin_252d_base_v075_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

