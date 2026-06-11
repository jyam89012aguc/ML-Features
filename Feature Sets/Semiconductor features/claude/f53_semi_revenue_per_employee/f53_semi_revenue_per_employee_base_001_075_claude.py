import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f53rp_rev_opex(rev, opex):
    return rev / opex.replace(0, np.nan)


def _f53rp_rev_ppne(rev, ppne):
    return rev / ppne.replace(0, np.nan)


def _f53rp_rev_assets(rev, assets):
    return rev / assets.replace(0, np.nan)


def _f53rp_align(q, idx):
    return q.reindex(idx).ffill()


# level 21d mean-centered (revopex)
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_base_v001_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 21d mean-centered (revppne)
def f53rp_f53_semi_revenue_per_employee_revppne_level_21d_base_v002_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 21d mean-centered (revassets)
def f53rp_f53_semi_revenue_per_employee_revassets_level_21d_base_v003_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (revopex)
def f53rp_f53_semi_revenue_per_employee_revopex_level_63d_base_v004_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (revppne)
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_base_v005_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (revassets)
def f53rp_f53_semi_revenue_per_employee_revassets_level_63d_base_v006_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (revopex)
def f53rp_f53_semi_revenue_per_employee_revopex_level_126d_base_v007_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (revppne)
def f53rp_f53_semi_revenue_per_employee_revppne_level_126d_base_v008_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (revassets)
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_base_v009_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (revopex)
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_base_v010_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (revppne)
def f53rp_f53_semi_revenue_per_employee_revppne_level_252d_base_v011_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (revassets)
def f53rp_f53_semi_revenue_per_employee_revassets_level_252d_base_v012_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (revopex)
def f53rp_f53_semi_revenue_per_employee_revopex_level_504d_base_v013_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (revppne)
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_base_v014_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (revassets)
def f53rp_f53_semi_revenue_per_employee_revassets_level_504d_base_v015_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_21d_base_v016_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_21d_base_v017_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_base_v018_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_base_v019_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_63d_base_v020_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_63d_base_v021_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_126d_base_v022_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_base_v023_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_126d_base_v024_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_252d_base_v025_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_252d_base_v026_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_base_v027_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_base_v028_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_504d_base_v029_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_504d_base_v030_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_robustz_21d_base_v031_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_robustz_21d_base_v032_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_robustz_21d_base_v033_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_robustz_63d_base_v034_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_robustz_63d_base_v035_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_robustz_63d_base_v036_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_robustz_126d_base_v037_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_robustz_126d_base_v038_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_robustz_126d_base_v039_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_robustz_252d_base_v040_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_robustz_252d_base_v041_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_robustz_252d_base_v042_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_robustz_504d_base_v043_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_robustz_504d_base_v044_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_robustz_504d_base_v045_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_21d_base_v046_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_base_v047_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_21d_base_v048_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_63d_base_v049_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_63d_base_v050_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_base_v051_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_base_v052_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_126d_base_v053_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_126d_base_v054_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_252d_base_v055_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_base_v056_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_252d_base_v057_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_504d_base_v058_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_504d_base_v059_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_base_v060_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_base_v061_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_21d_base_v062_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_21d_base_v063_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_63d_base_v064_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_base_v065_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_63d_base_v066_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_126d_base_v067_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_126d_base_v068_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_base_v069_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_base_v070_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_252d_base_v071_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_252d_base_v072_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_504d_base_v073_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_base_v074_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_504d_base_v075_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

