"""insider_activity_snapshot base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py — role-buy snapshots, cluster/breadth/
form-4 filing patterns, planned-vs-unplanned (10b5-1) mix, insider holdings
decay, 10% holder activity, and composite topping scores. PIT-clean.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)


def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)


def _max_streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        best = cur = 0
        for v in w:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag_series.rolling(window, min_periods=min_periods).apply(_ms, raw=True)


def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f18_iasp_076_ceo_buy_value_zscore_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily CEO buy $ vs 252d."""
    return _rolling_zscore(ceo_buy_value, YDAYS)


def f18_iasp_077_days_since_ceo_buy_event_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Bars since the last CEO buy event in 252d."""
    flag = (ceo_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS)


def f18_iasp_078_ceo_buy_to_sell_log_ratio_63d(ceo_buy_value: pd.Series, ceo_sell_value: pd.Series) -> pd.Series:
    """log(63d CEO buy sum / 63d CEO sell sum) — CEO conviction balance."""
    b = ceo_buy_value.rolling(QDAYS, min_periods=MDAYS).sum()
    s = ceo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_log(_safe_div(b, s))


def f18_iasp_079_cfo_buy_value_zscore_252d(cfo_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily CFO buy $ vs 252d."""
    return _rolling_zscore(cfo_buy_value, YDAYS)


def f18_iasp_080_days_since_cfo_buy_event_252d(cfo_buy_value: pd.Series) -> pd.Series:
    """Bars since the last CFO buy event in 252d."""
    flag = (cfo_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS)


def f18_iasp_081_ceo_cfo_joint_sell_days_count_63d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    """Bars in last 63d where CEO and CFO BOTH had a sell event (same day)."""
    flag = ((ceo_sell_value.fillna(0) > 0) & (cfo_sell_value.fillna(0) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_082_multi_role_sell_days_count_63d(officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Bars in last 63d where officer AND director both had a sell event same day — non-C-suite breadth."""
    flag = ((officer_sell_value.fillna(0) > 0) & (director_sell_value.fillna(0) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_083_mass_sell_event_count_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Bars in last 63d with sell_count >= 3 (3+ different insiders on same day) — broad-base sell events."""
    flag = (insider_sell_count >= 3).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_084_insider_breadth_sell_pct_63d(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean over 63d of sell_count/(sell_count+buy_count) — sell-side share of insider participation."""
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    ratio = _safe_div(insider_sell_count, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_085_insider_breadth_buy_pct_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Mean over 63d of buy_count/(buy_count+sell_count) — buy-side share of insider participation."""
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    ratio = _safe_div(insider_buy_count, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_086_insider_breadth_net_count_pct_63d(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean over 63d of (sell_count − buy_count)/(sell+buy) — net sell breadth."""
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    num = insider_sell_count.fillna(0) - insider_buy_count.fillna(0)
    ratio = _safe_div(num, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_087_cross_role_sell_dominance_index_63d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """63d sum of (CEO+CFO sell $) / (CEO+CFO+officer+director sell $) — C-suite sell dominance."""
    csuite = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    total = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0) + officer_sell_value.fillna(0) + director_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(csuite, total)


def f18_iasp_088_c_suite_sell_share_of_total_63d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63d sum (CEO+CFO sell $) / 63d sum (all insider sell $) — C-suite contribution share."""
    csuite = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    all_ = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(csuite, all_)


def f18_iasp_089_director_sell_share_of_total_63d(director_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63d sum (director sell $) / 63d sum (all insider sell $)."""
    d = director_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    all_ = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(d, all_)


def f18_iasp_090_insider_sell_concentration_top_role_63d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """63d max(role sum) / 63d sum(all role sums) — largest-role concentration share."""
    ceo = ceo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    cfo = cfo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    off_ = officer_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    dir_ = director_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    df = pd.concat([ceo, cfo, off_, dir_], axis=1)
    mx = df.max(axis=1)
    tot = df.sum(axis=1)
    return _safe_div(mx, tot)


def f18_iasp_091_mass_buy_event_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Bars in last 63d with buy_count >= 3 — broad-base buy events."""
    flag = (insider_buy_count >= 3).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_092_insider_breadth_buy_minus_sell_count_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63d sum of (buy_count − sell_count) — raw net breadth difference."""
    return (insider_buy_count.fillna(0) - insider_sell_count.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_093_form4_filings_count_zscore_252d(form4_filings_count: pd.Series) -> pd.Series:
    """Z-score of daily Form 4 filings count vs 252d — extreme filing-day activity."""
    return _rolling_zscore(form4_filings_count, YDAYS)


def f18_iasp_094_form4_filings_count_sum_63d(form4_filings_count: pd.Series) -> pd.Series:
    """Trailing-63d sum of Form 4 filings count."""
    return form4_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_095_form4_filings_count_top_decile_count_63d(form4_filings_count: pd.Series) -> pd.Series:
    """Bars in last 63d with filings count in trailing-252d top decile."""
    thr = form4_filings_count.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (form4_filings_count >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_096_form4_late_filings_count_63d(late_filings_count: pd.Series) -> pd.Series:
    """Trailing-63d sum of late Form 4 filings — quarterly late-filing burden."""
    return late_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_097_form4_late_filings_pct_63d(late_filings_count: pd.Series, form4_filings_count: pd.Series) -> pd.Series:
    """63d (late filings sum) / (total filings sum) — fraction of filings filed late."""
    late = late_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()
    tot = form4_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(late, tot)


def f18_iasp_098_form4_late_filings_zscore_252d(late_filings_count: pd.Series) -> pd.Series:
    """Z-score of daily late-filing count vs 252d."""
    return _rolling_zscore(late_filings_count, YDAYS)


def f18_iasp_099_form4_late_burst_count_63d(late_filings_count: pd.Series) -> pd.Series:
    """Bars in last 63d with >=2 late filings on the same day — late-burst event count."""
    flag = (late_filings_count >= 2).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_100_form4_filings_concentration_top5_days_63d(form4_filings_count: pd.Series) -> pd.Series:
    """Fraction of 63d filing-count sum from top-5 days — filing-day concentration."""
    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-5:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return form4_filings_count.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True)


def f18_iasp_101_planned_sell_value_zscore_252d(planned_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily 10b5-1 planned sell $ vs 252d."""
    return _rolling_zscore(planned_sell_value, YDAYS)


def f18_iasp_102_unplanned_sell_value_zscore_252d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily UN-planned (outside-plan) sell $ vs 252d — discretionary urgency."""
    return _rolling_zscore(unplanned_sell_value, YDAYS)


def f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    """log(63d planned sum / 63d unplanned sum) — quarterly plan-mix balance."""
    p = planned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    u = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_log(_safe_div(p, u))


def f18_iasp_104_unplanned_sell_share_of_total_63d(unplanned_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63d sum unplanned sell $ / 63d sum total insider sell $."""
    u = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    t = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(u, t)


def f18_iasp_105_unplanned_sell_top_decile_count_63d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Bars in last 63d with unplanned sell $ in trailing-252d top decile."""
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (unplanned_sell_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_106_unplanned_sell_log_diff_21d(unplanned_sell_value: pd.Series) -> pd.Series:
    """21d log change in unplanned sell $."""
    return _safe_log(unplanned_sell_value).diff(MDAYS)


def f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d(unplanned_sell_value: pd.Series) -> pd.Series:
    """63d unplanned sell sum / SMA(252d) of daily unplanned sell — ratio vs annual baseline."""
    s63 = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    sma = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s63, sma * QDAYS)


def f18_iasp_108_days_since_unplanned_sell_burst_252d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Bars since the last unplanned-sell-burst day (in trailing-252d top decile) within 252d."""
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (unplanned_sell_value >= thr).astype(float)
    return _recency_since_event(flag, YDAYS)


def f18_iasp_109_unplanned_sell_concentration_top3_days_63d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Fraction of 63d unplanned sell $ from top-3 days — burst concentration."""
    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-3:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True)


def f18_iasp_110_unplanned_sell_count_zscore_252d(unplanned_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily unplanned sell COUNT vs 252d."""
    return _rolling_zscore(unplanned_sell_count, YDAYS)


def f18_iasp_111_planned_sell_dryup_streak_max_252d(planned_sell_value: pd.Series) -> pd.Series:
    """Longest 252d consecutive run of zero planned-sell days — 10b5-1 dry-up."""
    flag = (planned_sell_value.fillna(0) == 0).astype(int)
    return _max_streak_above_zero(flag, YDAYS)


def f18_iasp_112_unplanned_sell_acceleration_21d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Second 21d log-change of unplanned sell $ — acceleration of discretionary selling."""
    return _safe_log(unplanned_sell_value).diff(MDAYS).diff(MDAYS)


def f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    """21d Δ in log(planned)−log(unplanned) — short-window mix rotation."""
    return (_safe_log(planned_sell_value) - _safe_log(unplanned_sell_value)).diff(MDAYS)


def f18_iasp_114_unplanned_sell_persistence_above_p75_252d(unplanned_sell_value: pd.Series) -> pd.Series:
    """Bars in last 252d where unplanned sell $ above trailing-252d p75 — sustained discretionary regime."""
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    flag = (unplanned_sell_value >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f18_iasp_115_sell_plan_mix_volatility_63d(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    """63d std of unplanned/(planned+unplanned) — mix volatility."""
    den = planned_sell_value.fillna(0) + unplanned_sell_value.fillna(0)
    ratio = _safe_div(unplanned_sell_value, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).std()


def f18_iasp_116_insider_holdings_post_pct_change_21d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """21d diff of insider post-transaction holdings % — monthly position-reduction signal."""
    return insider_holdings_post_pct.diff(MDAYS)


def f18_iasp_117_insider_holdings_post_pct_change_63d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """63d diff of insider holdings %."""
    return insider_holdings_post_pct.diff(QDAYS)


def f18_iasp_118_insider_holdings_post_pct_change_252d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """252d diff of insider holdings %."""
    return insider_holdings_post_pct.diff(YDAYS)


def f18_iasp_119_insider_holdings_drop_zscore_252d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Z-score of (current − 21d-ago) holdings % decline vs 252d distribution."""
    d = insider_holdings_post_pct.diff(MDAYS)
    return _rolling_zscore(d, YDAYS)


def f18_iasp_120_insider_holdings_under_p10_count_63d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Bars in last 63d where holdings % below trailing-252d p10 — bottom-decile residence."""
    thr = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    flag = (insider_holdings_post_pct <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_121_days_since_insider_holdings_max_252d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Bars since the 252d-rolling max of insider holdings %."""
    return _days_since_max(insider_holdings_post_pct, YDAYS)


def f18_iasp_122_insider_holdings_dryup_intensity_63d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Mean over 63d of negative-only daily holdings diffs — pure-decline intensity."""
    d = insider_holdings_post_pct.diff().clip(upper=0.0)
    return d.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_123_insider_holdings_acceleration_21d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Second 21d diff of holdings % — change in rate of insider exit."""
    return insider_holdings_post_pct.diff(MDAYS).diff(MDAYS)


def f18_iasp_124_insider_holdings_collapse_thrust_63d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Min(63d log diff of holdings %, 0) — worst quarterly collapse signal."""
    return _safe_log(insider_holdings_post_pct).diff(QDAYS).clip(upper=0.0)


def f18_iasp_125_insider_holdings_min_in_252d_log_distance(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """log(current holdings %) − log(252d rolling min holdings %) — distance from yearly trough."""
    mn = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(insider_holdings_post_pct) - _safe_log(mn)


def f18_iasp_126_insider_holdings_above_p50_streak_max_63d(insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Longest 63d run where holdings % > trailing-252d median — recovery persistence."""
    med = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((insider_holdings_post_pct - med) > 0).astype(int)
    return _max_streak_above_zero(flag, QDAYS)


def f18_iasp_127_ten_pct_holder_sell_value_zscore_252d(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily 10%-holder sell $ vs 252d — large-block discretionary distribution."""
    return _rolling_zscore(ten_pct_holder_sell_value, YDAYS)


def f18_iasp_128_ten_pct_holder_sell_value_sum_63d(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    """Trailing-63d sum of 10%-holder sell $."""
    return ten_pct_holder_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_129_ten_pct_holder_sell_log_diff_21d(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    """21d log change in 10%-holder sell $."""
    return _safe_log(ten_pct_holder_sell_value).diff(MDAYS)


def f18_iasp_130_ten_pct_holder_share_of_sell_63d(ten_pct_holder_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63d sum 10%-holder sell $ / 63d sum total insider sell $ — large-holder contribution share."""
    h = ten_pct_holder_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    t = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(h, t)


def f18_iasp_131_sell_dominance_composite_63d(insider_net_value: pd.Series, insider_sell_count: pd.Series, late_filings_count: pd.Series) -> pd.Series:
    """Mean over 63d of indicator (net_value<0 AND sell_count>=2 AND late_filings>=1) — fused distress score."""
    flag = ((insider_net_value < 0) & (insider_sell_count >= 2) & (late_filings_count >= 1)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_132_ceo_cfo_simul_top_decile_count_63d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    """Bars in last 63d where CEO and CFO each had sell $ in trailing-252d top decile of their own series."""
    ceo_thr = ceo_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    cfo_thr = cfo_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((ceo_sell_value >= ceo_thr) & (cfo_sell_value >= cfo_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_133_days_since_insider_buy_event_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Bars since the last day with any insider buy in 252d — general bullish-conviction dry-up."""
    flag = (insider_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS)


def f18_iasp_134_insider_capitulation_signal_63d(insider_sell_value: pd.Series, insider_sell_count: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Bars in last 63d where sell$ > trailing 252d p90 AND sell_count >= 3 AND buy$ == 0."""
    sell_thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((insider_sell_value >= sell_thr) & (insider_sell_count >= 3) & (insider_buy_value.fillna(0) == 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_135_sell_intensity_above_p95_count_252d(insider_sell_value: pd.Series) -> pd.Series:
    """Bars in last 252d with sell $ above trailing-252d p95 — annual-tail recurrence."""
    thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (insider_sell_value >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f18_iasp_136_sell_intensity_zscore_acceleration_21d(insider_sell_value: pd.Series) -> pd.Series:
    """21d Δ of (sell $ z-score vs 252d) — z-acceleration."""
    z = _rolling_zscore(insider_sell_value, YDAYS)
    return z.diff(MDAYS)


def f18_iasp_137_c_suite_sell_count_zscore_252d(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    """Daily count of C-suite sell events (CEO>0 + CFO>0), z-score vs 252d."""
    cnt = ((ceo_sell_value.fillna(0) > 0).astype(int) + (cfo_sell_value.fillna(0) > 0).astype(int)).astype(float)
    return _rolling_zscore(cnt, YDAYS)


def f18_iasp_138_sell_to_buy_value_ratio_zscore_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily sell$/buy$ ratio vs 252d distribution."""
    r = _safe_div(insider_sell_value, insider_buy_value)
    return _rolling_zscore(r, YDAYS)


def f18_iasp_139_sell_burst_intensity_max_63d(insider_sell_value: pd.Series) -> pd.Series:
    """Max daily sell $ within last 63d / trailing-252d median sell $ — peak burst-vs-baseline."""
    mx = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).max()
    med = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(mx, med)


def f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Bars in last 63d where sell $ > 0 today AND buy $ == 0 today AND zero buys in trailing 5d."""
    sell = insider_sell_value.fillna(0) > 0
    buy = insider_buy_value.fillna(0) > 0
    zero_buy_window = buy.rolling(WDAYS, min_periods=2).sum() == 0
    flag = (sell & ~buy & zero_buy_window).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d(insider_net_value: pd.Series) -> pd.Series:
    """Longest 252d consecutive run of net-sell days."""
    flag = (insider_net_value < 0).astype(int)
    return _max_streak_above_zero(flag, YDAYS)


def f18_iasp_142_net_sell_intensity_topdecile_count_252d(insider_net_value: pd.Series) -> pd.Series:
    """Bars in last 252d where |insider_net_value| is in trailing-252d top decile AND value < 0."""
    abs_thr = insider_net_value.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((insider_net_value.abs() >= abs_thr) & (insider_net_value < 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f18_iasp_143_sell_concentration_top1_day_share_of_63d(insider_sell_value: pd.Series) -> pd.Series:
    """Largest single sell-day $ / 63d sell-$ sum — short-window top-day concentration."""
    mx = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).max()
    tot = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(mx, tot)


def f18_iasp_144_sell_concentration_top1_day_share_of_252d(insider_sell_value: pd.Series) -> pd.Series:
    """Largest single sell-day $ / 252d sell-$ sum — annual top-day concentration."""
    mx = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).max()
    tot = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(mx, tot)


def f18_iasp_145_net_sell_topping_score_63d(insider_net_value: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Mean over 63d of (−net_value z) × (sell_count z) — joint sell-intensity + breadth score."""
    z_net = _rolling_zscore(insider_net_value, YDAYS)
    z_cnt = _rolling_zscore(insider_sell_count, YDAYS)
    return ((-z_net) * z_cnt).rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_146_net_sell_persistence_streak_max_63d(insider_net_value: pd.Series) -> pd.Series:
    """Longest 63d consecutive run of net-sell days — within-quarter persistence."""
    flag = (insider_net_value < 0).astype(int)
    return _max_streak_above_zero(flag, QDAYS)


def f18_iasp_147_insider_signal_inflection_count_63d(insider_net_value: pd.Series) -> pd.Series:
    """Count of net_value sign-flips (buy↔sell) within 63d — direction-change frequency."""
    sg = np.sign(insider_net_value.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_148_composite_distress_insider_score_63d(insider_net_value: pd.Series, insider_sell_value: pd.Series, insider_buy_value: pd.Series, late_filings_count: pd.Series) -> pd.Series:
    """Mean over 63d of (net<0)(sell_z>1)(buy==0)(late>=1) — fused distress score."""
    sell_z = _rolling_zscore(insider_sell_value, YDAYS)
    flag = ((insider_net_value < 0) & (sell_z > 1.0) & (insider_buy_value.fillna(0) == 0) & (late_filings_count >= 1)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f18_iasp_149_composite_insider_topping_score_252d(insider_sell_value: pd.Series, insider_sell_count: pd.Series, ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    """Mean over 252d of [pct-rank(sell$)+pct-rank(sell_count)+pct-rank(ceo_sell)+pct-rank(cfo_sell)]/4."""
    r1 = _rolling_rank_pct(insider_sell_value, YDAYS)
    r2 = _rolling_rank_pct(insider_sell_count, YDAYS)
    r3 = _rolling_rank_pct(ceo_sell_value, YDAYS)
    r4 = _rolling_rank_pct(cfo_sell_value, YDAYS)
    score = (r1 + r2 + r3 + r4) / 4.0
    return score.rolling(YDAYS, min_periods=QDAYS).mean()


def f18_iasp_150_composite_insider_blowoff_score_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series, insider_holdings_post_pct: pd.Series) -> pd.Series:
    """Mean over 252d of pct-rank(63d sell$ sum) × (1 − pct-rank(63d buy$ sum)) × (1 − pct-rank(holdings%))."""
    s63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    b63 = insider_buy_value.rolling(QDAYS, min_periods=MDAYS).sum()
    rs = _rolling_rank_pct(s63, YDAYS)
    rb = _rolling_rank_pct(b63, YDAYS)
    rh = _rolling_rank_pct(insider_holdings_post_pct, YDAYS)
    score = rs * (1.0 - rb) * (1.0 - rh)
    return score.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

INSIDER_ACTIVITY_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f18_iasp_076_ceo_buy_value_zscore_252d": {"inputs": ["ceo_buy_value"], "func": f18_iasp_076_ceo_buy_value_zscore_252d},
    "f18_iasp_077_days_since_ceo_buy_event_252d": {"inputs": ["ceo_buy_value"], "func": f18_iasp_077_days_since_ceo_buy_event_252d},
    "f18_iasp_078_ceo_buy_to_sell_log_ratio_63d": {"inputs": ["ceo_buy_value", "ceo_sell_value"], "func": f18_iasp_078_ceo_buy_to_sell_log_ratio_63d},
    "f18_iasp_079_cfo_buy_value_zscore_252d": {"inputs": ["cfo_buy_value"], "func": f18_iasp_079_cfo_buy_value_zscore_252d},
    "f18_iasp_080_days_since_cfo_buy_event_252d": {"inputs": ["cfo_buy_value"], "func": f18_iasp_080_days_since_cfo_buy_event_252d},
    "f18_iasp_081_ceo_cfo_joint_sell_days_count_63d": {"inputs": ["ceo_sell_value", "cfo_sell_value"], "func": f18_iasp_081_ceo_cfo_joint_sell_days_count_63d},
    "f18_iasp_082_multi_role_sell_days_count_63d": {"inputs": ["officer_sell_value", "director_sell_value"], "func": f18_iasp_082_multi_role_sell_days_count_63d},
    "f18_iasp_083_mass_sell_event_count_63d": {"inputs": ["insider_sell_count"], "func": f18_iasp_083_mass_sell_event_count_63d},
    "f18_iasp_084_insider_breadth_sell_pct_63d": {"inputs": ["insider_sell_count", "insider_buy_count"], "func": f18_iasp_084_insider_breadth_sell_pct_63d},
    "f18_iasp_085_insider_breadth_buy_pct_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": f18_iasp_085_insider_breadth_buy_pct_63d},
    "f18_iasp_086_insider_breadth_net_count_pct_63d": {"inputs": ["insider_sell_count", "insider_buy_count"], "func": f18_iasp_086_insider_breadth_net_count_pct_63d},
    "f18_iasp_087_cross_role_sell_dominance_index_63d": {"inputs": ["ceo_sell_value", "cfo_sell_value", "officer_sell_value", "director_sell_value"], "func": f18_iasp_087_cross_role_sell_dominance_index_63d},
    "f18_iasp_088_c_suite_sell_share_of_total_63d": {"inputs": ["ceo_sell_value", "cfo_sell_value", "insider_sell_value"], "func": f18_iasp_088_c_suite_sell_share_of_total_63d},
    "f18_iasp_089_director_sell_share_of_total_63d": {"inputs": ["director_sell_value", "insider_sell_value"], "func": f18_iasp_089_director_sell_share_of_total_63d},
    "f18_iasp_090_insider_sell_concentration_top_role_63d": {"inputs": ["ceo_sell_value", "cfo_sell_value", "officer_sell_value", "director_sell_value"], "func": f18_iasp_090_insider_sell_concentration_top_role_63d},
    "f18_iasp_091_mass_buy_event_count_63d": {"inputs": ["insider_buy_count"], "func": f18_iasp_091_mass_buy_event_count_63d},
    "f18_iasp_092_insider_breadth_buy_minus_sell_count_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": f18_iasp_092_insider_breadth_buy_minus_sell_count_63d},
    "f18_iasp_093_form4_filings_count_zscore_252d": {"inputs": ["form4_filings_count"], "func": f18_iasp_093_form4_filings_count_zscore_252d},
    "f18_iasp_094_form4_filings_count_sum_63d": {"inputs": ["form4_filings_count"], "func": f18_iasp_094_form4_filings_count_sum_63d},
    "f18_iasp_095_form4_filings_count_top_decile_count_63d": {"inputs": ["form4_filings_count"], "func": f18_iasp_095_form4_filings_count_top_decile_count_63d},
    "f18_iasp_096_form4_late_filings_count_63d": {"inputs": ["late_filings_count"], "func": f18_iasp_096_form4_late_filings_count_63d},
    "f18_iasp_097_form4_late_filings_pct_63d": {"inputs": ["late_filings_count", "form4_filings_count"], "func": f18_iasp_097_form4_late_filings_pct_63d},
    "f18_iasp_098_form4_late_filings_zscore_252d": {"inputs": ["late_filings_count"], "func": f18_iasp_098_form4_late_filings_zscore_252d},
    "f18_iasp_099_form4_late_burst_count_63d": {"inputs": ["late_filings_count"], "func": f18_iasp_099_form4_late_burst_count_63d},
    "f18_iasp_100_form4_filings_concentration_top5_days_63d": {"inputs": ["form4_filings_count"], "func": f18_iasp_100_form4_filings_concentration_top5_days_63d},
    "f18_iasp_101_planned_sell_value_zscore_252d": {"inputs": ["planned_sell_value"], "func": f18_iasp_101_planned_sell_value_zscore_252d},
    "f18_iasp_102_unplanned_sell_value_zscore_252d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_102_unplanned_sell_value_zscore_252d},
    "f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d": {"inputs": ["planned_sell_value", "unplanned_sell_value"], "func": f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d},
    "f18_iasp_104_unplanned_sell_share_of_total_63d": {"inputs": ["unplanned_sell_value", "insider_sell_value"], "func": f18_iasp_104_unplanned_sell_share_of_total_63d},
    "f18_iasp_105_unplanned_sell_top_decile_count_63d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_105_unplanned_sell_top_decile_count_63d},
    "f18_iasp_106_unplanned_sell_log_diff_21d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_106_unplanned_sell_log_diff_21d},
    "f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d},
    "f18_iasp_108_days_since_unplanned_sell_burst_252d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_108_days_since_unplanned_sell_burst_252d},
    "f18_iasp_109_unplanned_sell_concentration_top3_days_63d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_109_unplanned_sell_concentration_top3_days_63d},
    "f18_iasp_110_unplanned_sell_count_zscore_252d": {"inputs": ["unplanned_sell_count"], "func": f18_iasp_110_unplanned_sell_count_zscore_252d},
    "f18_iasp_111_planned_sell_dryup_streak_max_252d": {"inputs": ["planned_sell_value"], "func": f18_iasp_111_planned_sell_dryup_streak_max_252d},
    "f18_iasp_112_unplanned_sell_acceleration_21d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_112_unplanned_sell_acceleration_21d},
    "f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d": {"inputs": ["planned_sell_value", "unplanned_sell_value"], "func": f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d},
    "f18_iasp_114_unplanned_sell_persistence_above_p75_252d": {"inputs": ["unplanned_sell_value"], "func": f18_iasp_114_unplanned_sell_persistence_above_p75_252d},
    "f18_iasp_115_sell_plan_mix_volatility_63d": {"inputs": ["planned_sell_value", "unplanned_sell_value"], "func": f18_iasp_115_sell_plan_mix_volatility_63d},
    "f18_iasp_116_insider_holdings_post_pct_change_21d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_116_insider_holdings_post_pct_change_21d},
    "f18_iasp_117_insider_holdings_post_pct_change_63d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_117_insider_holdings_post_pct_change_63d},
    "f18_iasp_118_insider_holdings_post_pct_change_252d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_118_insider_holdings_post_pct_change_252d},
    "f18_iasp_119_insider_holdings_drop_zscore_252d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_119_insider_holdings_drop_zscore_252d},
    "f18_iasp_120_insider_holdings_under_p10_count_63d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_120_insider_holdings_under_p10_count_63d},
    "f18_iasp_121_days_since_insider_holdings_max_252d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_121_days_since_insider_holdings_max_252d},
    "f18_iasp_122_insider_holdings_dryup_intensity_63d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_122_insider_holdings_dryup_intensity_63d},
    "f18_iasp_123_insider_holdings_acceleration_21d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_123_insider_holdings_acceleration_21d},
    "f18_iasp_124_insider_holdings_collapse_thrust_63d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_124_insider_holdings_collapse_thrust_63d},
    "f18_iasp_125_insider_holdings_min_in_252d_log_distance": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_125_insider_holdings_min_in_252d_log_distance},
    "f18_iasp_126_insider_holdings_above_p50_streak_max_63d": {"inputs": ["insider_holdings_post_pct"], "func": f18_iasp_126_insider_holdings_above_p50_streak_max_63d},
    "f18_iasp_127_ten_pct_holder_sell_value_zscore_252d": {"inputs": ["ten_pct_holder_sell_value"], "func": f18_iasp_127_ten_pct_holder_sell_value_zscore_252d},
    "f18_iasp_128_ten_pct_holder_sell_value_sum_63d": {"inputs": ["ten_pct_holder_sell_value"], "func": f18_iasp_128_ten_pct_holder_sell_value_sum_63d},
    "f18_iasp_129_ten_pct_holder_sell_log_diff_21d": {"inputs": ["ten_pct_holder_sell_value"], "func": f18_iasp_129_ten_pct_holder_sell_log_diff_21d},
    "f18_iasp_130_ten_pct_holder_share_of_sell_63d": {"inputs": ["ten_pct_holder_sell_value", "insider_sell_value"], "func": f18_iasp_130_ten_pct_holder_share_of_sell_63d},
    "f18_iasp_131_sell_dominance_composite_63d": {"inputs": ["insider_net_value", "insider_sell_count", "late_filings_count"], "func": f18_iasp_131_sell_dominance_composite_63d},
    "f18_iasp_132_ceo_cfo_simul_top_decile_count_63d": {"inputs": ["ceo_sell_value", "cfo_sell_value"], "func": f18_iasp_132_ceo_cfo_simul_top_decile_count_63d},
    "f18_iasp_133_days_since_insider_buy_event_252d": {"inputs": ["insider_buy_value"], "func": f18_iasp_133_days_since_insider_buy_event_252d},
    "f18_iasp_134_insider_capitulation_signal_63d": {"inputs": ["insider_sell_value", "insider_sell_count", "insider_buy_value"], "func": f18_iasp_134_insider_capitulation_signal_63d},
    "f18_iasp_135_sell_intensity_above_p95_count_252d": {"inputs": ["insider_sell_value"], "func": f18_iasp_135_sell_intensity_above_p95_count_252d},
    "f18_iasp_136_sell_intensity_zscore_acceleration_21d": {"inputs": ["insider_sell_value"], "func": f18_iasp_136_sell_intensity_zscore_acceleration_21d},
    "f18_iasp_137_c_suite_sell_count_zscore_252d": {"inputs": ["ceo_sell_value", "cfo_sell_value"], "func": f18_iasp_137_c_suite_sell_count_zscore_252d},
    "f18_iasp_138_sell_to_buy_value_ratio_zscore_252d": {"inputs": ["insider_sell_value", "insider_buy_value"], "func": f18_iasp_138_sell_to_buy_value_ratio_zscore_252d},
    "f18_iasp_139_sell_burst_intensity_max_63d": {"inputs": ["insider_sell_value"], "func": f18_iasp_139_sell_burst_intensity_max_63d},
    "f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d": {"inputs": ["insider_sell_value", "insider_buy_value"], "func": f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d},
    "f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d": {"inputs": ["insider_net_value"], "func": f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d},
    "f18_iasp_142_net_sell_intensity_topdecile_count_252d": {"inputs": ["insider_net_value"], "func": f18_iasp_142_net_sell_intensity_topdecile_count_252d},
    "f18_iasp_143_sell_concentration_top1_day_share_of_63d": {"inputs": ["insider_sell_value"], "func": f18_iasp_143_sell_concentration_top1_day_share_of_63d},
    "f18_iasp_144_sell_concentration_top1_day_share_of_252d": {"inputs": ["insider_sell_value"], "func": f18_iasp_144_sell_concentration_top1_day_share_of_252d},
    "f18_iasp_145_net_sell_topping_score_63d": {"inputs": ["insider_net_value", "insider_sell_count"], "func": f18_iasp_145_net_sell_topping_score_63d},
    "f18_iasp_146_net_sell_persistence_streak_max_63d": {"inputs": ["insider_net_value"], "func": f18_iasp_146_net_sell_persistence_streak_max_63d},
    "f18_iasp_147_insider_signal_inflection_count_63d": {"inputs": ["insider_net_value"], "func": f18_iasp_147_insider_signal_inflection_count_63d},
    "f18_iasp_148_composite_distress_insider_score_63d": {"inputs": ["insider_net_value", "insider_sell_value", "insider_buy_value", "late_filings_count"], "func": f18_iasp_148_composite_distress_insider_score_63d},
    "f18_iasp_149_composite_insider_topping_score_252d": {"inputs": ["insider_sell_value", "insider_sell_count", "ceo_sell_value", "cfo_sell_value"], "func": f18_iasp_149_composite_insider_topping_score_252d},
    "f18_iasp_150_composite_insider_blowoff_score_252d": {"inputs": ["insider_sell_value", "insider_buy_value", "insider_holdings_post_pct"], "func": f18_iasp_150_composite_insider_blowoff_score_252d},
}
