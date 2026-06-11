import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f019_rev_per_rnd(revenue, rnd):
    return revenue / rnd.abs().replace(0, np.nan)


def _f019_gp_per_rnd(gp, rnd):
    return gp / rnd.abs().replace(0, np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_mean_21d_base_v001_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_mean_63d_base_v002_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_mean_126d_base_v003_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_mean_252d_base_v004_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_mean_504d_base_v005_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_mean_21d_base_v006_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_mean_63d_base_v007_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_mean_126d_base_v008_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_mean_252d_base_v009_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_mean_504d_base_v010_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_mean_21d_base_v011_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_mean_63d_base_v012_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_mean_126d_base_v013_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_mean_252d_base_v014_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_mean_504d_base_v015_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_mean_21d_base_v016_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_mean_63d_base_v017_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_mean_126d_base_v018_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_mean_252d_base_v019_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_mean_504d_base_v020_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_mean_21d_base_v021_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_mean_63d_base_v022_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_mean_126d_base_v023_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_mean_252d_base_v024_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_mean_504d_base_v025_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_mean_21d_base_v026_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_mean_63d_base_v027_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_mean_126d_base_v028_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_mean_252d_base_v029_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_mean_504d_base_v030_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_mean_21d_base_v031_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_mean_63d_base_v032_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_mean_126d_base_v033_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_mean_252d_base_v034_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_mean_504d_base_v035_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_median_63d_base_v036_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_median_252d_base_v037_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_median_504d_base_v038_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_median_63d_base_v039_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_median_252d_base_v040_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_median_504d_base_v041_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_median_63d_base_v042_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_median_252d_base_v043_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_median_504d_base_v044_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_median_63d_base_v045_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_median_252d_base_v046_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_median_504d_base_v047_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_median_63d_base_v048_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_median_252d_base_v049_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_median_504d_base_v050_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_median_63d_base_v051_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_median_252d_base_v052_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_median_504d_base_v053_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_median_63d_base_v054_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_median_252d_base_v055_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_median_504d_base_v056_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_rmax_252d_base_v057_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_rmax_504d_base_v058_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_rmax_252d_base_v059_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_rmax_504d_base_v060_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_rmax_252d_base_v061_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_rmax_504d_base_v062_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_rmax_252d_base_v063_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_growth_per_rnd_rmax_504d_base_v064_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_rmax_252d_base_v065_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ebitda_per_rnd_rmax_504d_base_v066_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_rmax_252d_base_v067_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_fcf_per_rnd_rmax_504d_base_v068_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_rmax_252d_base_v069_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_ocf_per_rnd_rmax_504d_base_v070_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_rmin_252d_base_v071_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_rev_per_rnd_rmin_504d_base_v072_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_rmin_252d_base_v073_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_gp_per_rnd_rmin_504d_base_v074_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f019_rnd_productivity_opinc_per_rnd_rmin_252d_base_v075_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

