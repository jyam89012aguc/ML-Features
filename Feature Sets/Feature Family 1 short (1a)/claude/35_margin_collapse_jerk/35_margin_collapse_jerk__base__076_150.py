"""margin_collapse_jerk base features 076_150 — short blowup pipeline 1a-inverse.

Margin jerk pattern detection: turning points, cliffs, regime shifts in the third difference of margin trajectories.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
SF1 quarterly cadence (lags 1, 4, 8, 12, 16, 20 quarters).
"""
import numpy as np
import pandas as pd


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_mad_z(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median().replace(0, np.nan)
    return (s - med) / (1.4826 * mad)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _sign_safe(s):
    return np.sign(s).where(s.notna(), np.nan)


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()


def _max_consec_true(b, window):
    return _consec_true_streak(b).rolling(window, min_periods=1).max()


def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()


def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()


def _winsorize(s, lo=0.1, hi=0.9, window=8, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    qlo = s.rolling(window, min_periods=min_periods).quantile(lo)
    qhi = s.rolling(window, min_periods=min_periods).quantile(hi)
    return s.clip(lower=qlo, upper=qhi)


def _jerk(s):
    """Quarter-over-quarter-over-quarter-over-quarter jerk (third diff)."""
    return s.diff().diff().diff()


def _accel(s):
    return s.diff().diff()


def _gm(revenue, gp):
    return _safe_div(gp, revenue.abs())


def _om(revenue, opinc):
    return _safe_div(opinc, revenue.abs())


def _em(revenue, ebitda):
    return _safe_div(ebitda, revenue.abs())


def _nm(revenue, netinc):
    return _safe_div(netinc, revenue.abs())


def _gm_ttm(revenue, gp):
    return _safe_div(_ttm(gp), _ttm(revenue).abs())


def _om_ttm(revenue, opinc):
    return _safe_div(_ttm(opinc), _ttm(revenue).abs())


def _em_ttm(revenue, ebitda):
    return _safe_div(_ttm(ebitda), _ttm(revenue).abs())


def _nm_ttm(revenue, netinc):
    return _safe_div(_ttm(netinc), _ttm(revenue).abs())


def _cusum(s, window):
    """Rolling CUSUM around mean — peak absolute excursion in window."""
    m = s.rolling(window, min_periods=max(window // 3, 2)).mean()
    dev = s - m
    return dev.rolling(window, min_periods=max(window // 3, 2)).apply(
        lambda w: float(np.nanmax(np.abs(np.nancumsum(w)))) if not np.all(np.isnan(w)) else np.nan, raw=True
    )


# ============================================================
#                    BASE FEATURES 076-150
# ============================================================

def f35_mcjk_076_4margin_jerk_kurt_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Kurtosis of per-q 4-margin jerk distribution over 8q."""
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    cross = pd.concat([g, o, e, n], axis=1).mean(axis=1)
    return cross.rolling(8, min_periods=3).kurt()


def f35_mcjk_077_gm_om_em_nm_jerk_descending_breach_count_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    """Count quarters where jerk ordering breaks the expected descending margin pattern (gm jerk > om jerk > nm jerk)."""
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); n = _jerk(_nm(revenue, netinc))
    breach = ~((g >= o) & (o >= n))
    return _rolling_count(breach, 8)


def f35_mcjk_078_4margin_jerk_avg_minus_ewma8(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Per-q mean of 4 margin jerks minus its EMA(8)."""
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    cross = pd.concat([g, o, e, n], axis=1).mean(axis=1)
    return cross - _ema(cross, 8)


def f35_mcjk_079_4margin_jerk_mean_persistence_lag1_12q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Lag-1 autocorr of per-q 4-margin avg jerk over 12q."""
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    cross = pd.concat([g, o, e, n], axis=1).mean(axis=1)
    return cross.rolling(12, min_periods=4).corr(cross.shift(1))


def f35_mcjk_080_gm_jerk_cusum_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """CUSUM peak absolute excursion of gm jerk over 12q."""
    j = _jerk(_gm(revenue, gp))
    return _cusum(j, 12)


def f35_mcjk_081_om_jerk_cusum_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """CUSUM peak absolute excursion of om jerk over 12q."""
    j = _jerk(_om(revenue, opinc))
    return _cusum(j, 12)


def f35_mcjk_082_em_jerk_cusum_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """CUSUM peak absolute excursion of em jerk over 12q."""
    j = _jerk(_em(revenue, ebitda))
    return _cusum(j, 12)


def f35_mcjk_083_nm_jerk_cusum_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """CUSUM peak absolute excursion of nm jerk over 12q."""
    j = _jerk(_nm(revenue, netinc))
    return _cusum(j, 12)


def f35_mcjk_084_gm_jerk_mean_shift_t_4q_vs_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """t-stat for mean shift in gm jerk: (mean4 - mean12)/sd12 over 12q."""
    j = _jerk(_gm(revenue, gp))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return (m4 - m12) / s12


def f35_mcjk_085_om_jerk_mean_shift_t_4q_vs_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """t-stat for mean shift in om jerk: (mean4 - mean12)/sd12 over 12q."""
    j = _jerk(_om(revenue, opinc))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return (m4 - m12) / s12


def f35_mcjk_086_em_jerk_mean_shift_t_4q_vs_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """t-stat for mean shift in em jerk: (mean4 - mean12)/sd12 over 12q."""
    j = _jerk(_em(revenue, ebitda))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return (m4 - m12) / s12


def f35_mcjk_087_nm_jerk_mean_shift_t_4q_vs_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """t-stat for mean shift in nm jerk: (mean4 - mean12)/sd12 over 12q."""
    j = _jerk(_nm(revenue, netinc))
    m4 = j.rolling(4, min_periods=2).mean(); m12 = j.rolling(12, min_periods=4).mean(); s12 = j.rolling(12, min_periods=4).std().replace(0, np.nan)
    return (m4 - m12) / s12


def f35_mcjk_088_gm_jerk_variance_jump_4q_vs_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Variance ratio of gm jerk 4q vs 12q."""
    j = _jerk(_gm(revenue, gp))
    return _safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())


def f35_mcjk_089_om_jerk_variance_jump_4q_vs_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Variance ratio of om jerk 4q vs 12q."""
    j = _jerk(_om(revenue, opinc))
    return _safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())


def f35_mcjk_090_em_jerk_variance_jump_4q_vs_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Variance ratio of em jerk 4q vs 12q."""
    j = _jerk(_em(revenue, ebitda))
    return _safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())


def f35_mcjk_091_nm_jerk_variance_jump_4q_vs_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Variance ratio of nm jerk 4q vs 12q."""
    j = _jerk(_nm(revenue, netinc))
    return _safe_div(j.rolling(4, min_periods=2).var(), j.rolling(12, min_periods=4).var())


def f35_mcjk_092_gm_jerk_quandt_proxy_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Quandt-style max split-mean-diff over 12q for gm jerk."""
    j = _jerk(_gm(revenue, gp))
    def _q(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            d = abs(v[:k].mean() - v[k:].mean())
            diffs.append(d)
        return float(max(diffs)) if diffs else np.nan
    return j.rolling(12, min_periods=6).apply(_q, raw=True)


def f35_mcjk_093_om_jerk_quandt_proxy_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Quandt-style max split-mean-diff over 12q for om jerk."""
    j = _jerk(_om(revenue, opinc))
    def _q(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            d = abs(v[:k].mean() - v[k:].mean())
            diffs.append(d)
        return float(max(diffs)) if diffs else np.nan
    return j.rolling(12, min_periods=6).apply(_q, raw=True)


def f35_mcjk_094_em_jerk_quandt_proxy_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Quandt-style max split-mean-diff over 12q for em jerk."""
    j = _jerk(_em(revenue, ebitda))
    def _q(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            d = abs(v[:k].mean() - v[k:].mean())
            diffs.append(d)
        return float(max(diffs)) if diffs else np.nan
    return j.rolling(12, min_periods=6).apply(_q, raw=True)


def f35_mcjk_095_nm_jerk_quandt_proxy_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Quandt-style max split-mean-diff over 12q for nm jerk."""
    j = _jerk(_nm(revenue, netinc))
    def _q(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            d = abs(v[:k].mean() - v[k:].mean())
            diffs.append(d)
        return float(max(diffs)) if diffs else np.nan
    return j.rolling(12, min_periods=6).apply(_q, raw=True)


def f35_mcjk_096_gm_jerk_break_recency_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Bars since maximum |jerk-mean-shift| occurred in last 12q."""
    j = _jerk(_gm(revenue, gp))
    def _br(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            diffs.append(abs(v[:k].mean() - v[k:].mean()))
        if not diffs:
            return np.nan
        return float(len(w) - 1 - (2 + int(np.argmax(diffs))))
    return j.rolling(12, min_periods=6).apply(_br, raw=True)


def f35_mcjk_097_om_jerk_break_recency_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Bars since maximum |jerk-mean-shift| occurred in last 12q."""
    j = _jerk(_om(revenue, opinc))
    def _br(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            diffs.append(abs(v[:k].mean() - v[k:].mean()))
        if not diffs:
            return np.nan
        return float(len(w) - 1 - (2 + int(np.argmax(diffs))))
    return j.rolling(12, min_periods=6).apply(_br, raw=True)


def f35_mcjk_098_em_jerk_break_recency_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Bars since maximum |jerk-mean-shift| occurred in last 12q."""
    j = _jerk(_em(revenue, ebitda))
    def _br(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            diffs.append(abs(v[:k].mean() - v[k:].mean()))
        if not diffs:
            return np.nan
        return float(len(w) - 1 - (2 + int(np.argmax(diffs))))
    return j.rolling(12, min_periods=6).apply(_br, raw=True)


def f35_mcjk_099_nm_jerk_break_recency_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Bars since maximum |jerk-mean-shift| occurred in last 12q."""
    j = _jerk(_nm(revenue, netinc))
    def _br(w):
        v = w[~np.isnan(w)]
        if len(v) < 6:
            return np.nan
        diffs = []
        for k in range(2, len(v) - 1):
            diffs.append(abs(v[:k].mean() - v[k:].mean()))
        if not diffs:
            return np.nan
        return float(len(w) - 1 - (2 + int(np.argmax(diffs))))
    return j.rolling(12, min_periods=6).apply(_br, raw=True)


def f35_mcjk_100_gm_jerk_q_since_min_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Quarters since gm jerk hit its 12q min."""
    j = _jerk(_gm(revenue, gp))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return j.rolling(12, min_periods=4).apply(_b, raw=True)


def f35_mcjk_101_om_jerk_q_since_min_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Quarters since om jerk hit its 12q min."""
    j = _jerk(_om(revenue, opinc))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return j.rolling(12, min_periods=4).apply(_b, raw=True)


def f35_mcjk_102_em_jerk_q_since_min_12q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Quarters since em jerk hit its 12q min."""
    j = _jerk(_em(revenue, ebitda))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return j.rolling(12, min_periods=4).apply(_b, raw=True)


def f35_mcjk_103_nm_jerk_q_since_min_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Quarters since nm jerk hit its 12q min."""
    j = _jerk(_nm(revenue, netinc))
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    return j.rolling(12, min_periods=4).apply(_b, raw=True)


def f35_mcjk_104_gm_jerk_ulcer_index_neg_8q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """RMS of negative gm jerks over 8q (Ulcer-style downside aggregator)."""
    j = _jerk(_gm(revenue, gp))
    neg = j.clip(upper=0)
    return np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())


def f35_mcjk_105_om_jerk_ulcer_index_neg_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """RMS of negative om jerks over 8q (Ulcer-style downside aggregator)."""
    j = _jerk(_om(revenue, opinc))
    neg = j.clip(upper=0)
    return np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())


def f35_mcjk_106_em_jerk_ulcer_index_neg_8q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """RMS of negative em jerks over 8q (Ulcer-style downside aggregator)."""
    j = _jerk(_em(revenue, ebitda))
    neg = j.clip(upper=0)
    return np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())


def f35_mcjk_107_nm_jerk_ulcer_index_neg_8q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """RMS of negative nm jerks over 8q (Ulcer-style downside aggregator)."""
    j = _jerk(_nm(revenue, netinc))
    neg = j.clip(upper=0)
    return np.sqrt(neg.pow(2).rolling(8, min_periods=3).mean())


def f35_mcjk_108_gm_jerk_event_count_below_q10_16q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Count quarters in last 16q where gm jerk fell below its 16q 10th-percentile."""
    j = _jerk(_gm(revenue, gp))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return _rolling_count(j < q10, 16)


def f35_mcjk_109_om_jerk_event_count_below_q10_16q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Count quarters in last 16q where om jerk fell below its 16q 10th-percentile."""
    j = _jerk(_om(revenue, opinc))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return _rolling_count(j < q10, 16)


def f35_mcjk_110_em_jerk_event_count_below_q10_16q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Count quarters in last 16q where em jerk fell below its 16q 10th-percentile."""
    j = _jerk(_em(revenue, ebitda))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return _rolling_count(j < q10, 16)


def f35_mcjk_111_nm_jerk_event_count_below_q10_16q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Count quarters in last 16q where nm jerk fell below its 16q 10th-percentile."""
    j = _jerk(_nm(revenue, netinc))
    q10 = j.rolling(16, min_periods=5).quantile(0.10)
    return _rolling_count(j < q10, 16)


def f35_mcjk_112_gm_jerk_decline_streak_max_16q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Max consecutive declining-jerk streak (jerk_t < jerk_{t-1}) over 16q."""
    j = _jerk(_gm(revenue, gp))
    return _max_consec_true(j < j.shift(1), 16)


def f35_mcjk_113_om_jerk_decline_streak_max_16q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Max consecutive declining-jerk streak (jerk_t < jerk_{t-1}) over 16q."""
    j = _jerk(_om(revenue, opinc))
    return _max_consec_true(j < j.shift(1), 16)


def f35_mcjk_114_em_jerk_decline_streak_max_16q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Max consecutive declining-jerk streak (jerk_t < jerk_{t-1}) over 16q."""
    j = _jerk(_em(revenue, ebitda))
    return _max_consec_true(j < j.shift(1), 16)


def f35_mcjk_115_nm_jerk_decline_streak_max_16q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Max consecutive declining-jerk streak (jerk_t < jerk_{t-1}) over 16q."""
    j = _jerk(_nm(revenue, netinc))
    return _max_consec_true(j < j.shift(1), 16)


def f35_mcjk_116_gm_jerk_recovery_speed_from_8q_min(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Current gm jerk minus 8q min divided by quarters since min."""
    j = _jerk(_gm(revenue, gp))
    mn = j.rolling(8, min_periods=3).min()
    def _qs(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    qs = j.rolling(8, min_periods=3).apply(_qs, raw=True).replace(0, np.nan)
    return _safe_div(j - mn, qs)


def f35_mcjk_117_om_jerk_recovery_speed_from_8q_min(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Current om jerk minus 8q min divided by quarters since min."""
    j = _jerk(_om(revenue, opinc))
    mn = j.rolling(8, min_periods=3).min()
    def _qs(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    qs = j.rolling(8, min_periods=3).apply(_qs, raw=True).replace(0, np.nan)
    return _safe_div(j - mn, qs)


def f35_mcjk_118_em_jerk_recovery_speed_from_8q_min(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Current em jerk minus 8q min divided by quarters since min."""
    j = _jerk(_em(revenue, ebitda))
    mn = j.rolling(8, min_periods=3).min()
    def _qs(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    qs = j.rolling(8, min_periods=3).apply(_qs, raw=True).replace(0, np.nan)
    return _safe_div(j - mn, qs)


def f35_mcjk_119_nm_jerk_recovery_speed_from_8q_min(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Current nm jerk minus 8q min divided by quarters since min."""
    j = _jerk(_nm(revenue, netinc))
    mn = j.rolling(8, min_periods=3).min()
    def _qs(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmin(w)))
    qs = j.rolling(8, min_periods=3).apply(_qs, raw=True).replace(0, np.nan)
    return _safe_div(j - mn, qs)


def f35_mcjk_120_composite_jerk_fragility_4margin_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Sum: z(gm jerk neg) + z(om jerk neg) + z(em jerk neg) + z(nm jerk neg) over 8q."""
    g = _rolling_zscore((-_jerk(_gm(revenue, gp))).clip(lower=0), 8); o = _rolling_zscore((-_jerk(_om(revenue, opinc))).clip(lower=0), 8); e = _rolling_zscore((-_jerk(_em(revenue, ebitda))).clip(lower=0), 8); n = _rolling_zscore((-_jerk(_nm(revenue, netinc))).clip(lower=0), 8)
    return g.fillna(0) + o.fillna(0) + e.fillna(0) + n.fillna(0)


def f35_mcjk_121_conditional_jerk_given_low_om_level_12q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Mean OM jerk over 12q conditional on OM level being below its 12q median."""
    om = _om(revenue, opinc); j = _jerk(om)
    cond = om < om.rolling(12, min_periods=4).median()
    return j.where(cond, np.nan).rolling(12, min_periods=4).mean()


def f35_mcjk_122_conditional_jerk_given_low_gm_level_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Mean GM jerk over 12q conditional on GM level being below its 12q median."""
    gm = _gm(revenue, gp); j = _jerk(gm)
    cond = gm < gm.rolling(12, min_periods=4).median()
    return j.where(cond, np.nan).rolling(12, min_periods=4).mean()


def f35_mcjk_123_conditional_jerk_given_neg_revenue_growth_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Mean NM jerk over 12q conditional on yoy revenue growth being negative."""
    n = _jerk(_nm(revenue, netinc))
    cond = _yoy_pct(revenue) < 0
    return n.where(cond, np.nan).rolling(12, min_periods=4).mean()


def f35_mcjk_124_om_jerk_minus_revenue_growth_jerk_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Z(OM jerk) minus Z(revenue-growth jerk) over 8q — operating-deleverage acceleration."""
    om_j = _rolling_zscore(_jerk(_om(revenue, opinc)), 8); rev_j = _rolling_zscore(_jerk(_yoy_pct(revenue)), 8)
    return om_j - rev_j


def f35_mcjk_125_nm_jerk_minus_revenue_growth_jerk_8q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Z(NM jerk) minus Z(revenue-growth jerk) over 8q."""
    n_j = _rolling_zscore(_jerk(_nm(revenue, netinc)), 8); rev_j = _rolling_zscore(_jerk(_yoy_pct(revenue)), 8)
    return n_j - rev_j


def f35_mcjk_126_cogs_share_jerk_onset_after_dormancy_8q(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Cogs/revenue jerk onset: |z(8q)|>3 after prior 4q calm (|z|<1 in >=75% of bars)."""
    ratio = _safe_div(cor, revenue.abs())
    j_z = _rolling_zscore(_jerk(ratio), 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f35_mcjk_127_sgna_share_jerk_cliff_conditional_on_high_share_8q(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    """SGA/revenue jerk magnitude, conditional on sgna-share in top 30% of 12q (high-cost regime)."""
    ratio = _safe_div(sgna, revenue.abs())
    j = _jerk(ratio)
    high = ratio > ratio.rolling(12, min_periods=4).quantile(0.70)
    return j.abs().where(high, np.nan).rolling(8, min_periods=3).max()


def f35_mcjk_128_opex_share_jerk_3consec_pos_streak_max_16q(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """Opex/revenue jerk: longest streak of 3-consec positive jerk z (z>1) qualifying bars, over 16q."""
    ratio = _safe_div(opex, revenue.abs())
    j_z = _rolling_zscore(_jerk(ratio), 8)
    pos = (j_z > 1).astype(int)
    streak3 = pos.rolling(3, min_periods=3).sum()
    qual = (streak3 >= 3).astype(int)
    def _maxrun(w):
        if np.all(np.isnan(w)):
            return np.nan
        w = np.nan_to_num(w, nan=0).astype(int)
        best = cur = 0
        for v in w:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        return float(best)
    return qual.rolling(16, min_periods=4).apply(_maxrun, raw=True)


def f35_mcjk_129_depamor_share_jerk_multi_horizon_onset_4_8_12q(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A/revenue jerk onset breadth: count of horizons (4,8,12) where |jerk z|>3."""
    ratio = _safe_div(depamor, revenue.abs())
    j = _jerk(ratio)
    o4 = (_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
    o8 = (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
    o12 = (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0)
    return o4 + o8 + o12


def f35_mcjk_130_cogs_sgna_jerk_simultaneous_jump_count_8q(revenue: pd.Series, cor: pd.Series, sgna: pd.Series) -> pd.Series:
    """Count quarters in 8q where both COGS/rev AND SGA/rev jerks exceeded 1.5*MAD."""
    rc = _safe_div(cor, revenue.abs()); rs = _safe_div(sgna, revenue.abs())
    jc = _jerk(rc); js = _jerk(rs)
    mc = jc.rolling(12, min_periods=4).median(); ms_ = js.rolling(12, min_periods=4).median()
    mac = (jc - mc).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    mas = (js - ms_).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cond = ((jc - mc).abs() > 1.5 * 1.4826 * mac) & ((js - ms_).abs() > 1.5 * 1.4826 * mas)
    return _rolling_count(cond, 8)


def f35_mcjk_131_cost_stack_jerk_dispersion_8q(revenue: pd.Series, cor: pd.Series, sgna: pd.Series, depamor: pd.Series) -> pd.Series:
    """Std across (COGS/rev, SGA/rev, D&A/rev) jerks per quarter, 8q mean."""
    rc = _jerk(_safe_div(cor, revenue.abs())); rs = _jerk(_safe_div(sgna, revenue.abs())); rd = _jerk(_safe_div(depamor, revenue.abs()))
    disp = pd.concat([rc, rs, rd], axis=1).std(axis=1)
    return disp.rolling(8, min_periods=3).mean()


def f35_mcjk_132_nm_jerk_smoothed_minus_raw_disagree_8q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Count quarters where sign(EMA(4) of NM jerk) disagrees with sign(NM jerk), in 8q."""
    j = _jerk(_nm(revenue, netinc))
    disagree = _sign_safe(_ema(j, 4)) != _sign_safe(j)
    return _rolling_count(disagree, 8)


def f35_mcjk_133_om_jerk_ema4_minus_ema12(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """EMA(4) of OM jerk minus EMA(12) — fast-vs-slow jerk regime."""
    j = _jerk(_om(revenue, opinc))
    return _ema(j, 4) - _ema(j, 12)


def f35_mcjk_134_nm_jerk_skew_change_8q_vs_16q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Skewness of NM jerk over 8q minus over 16q."""
    j = _jerk(_nm(revenue, netinc))
    return j.rolling(8, min_periods=3).skew() - j.rolling(16, min_periods=6).skew()


def f35_mcjk_135_om_jerk_ar1_persistence_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """AR(1) corr of OM jerk on its 1-lag over 8q."""
    j = _jerk(_om(revenue, opinc))
    return j.rolling(8, min_periods=3).corr(j.shift(1))


def f35_mcjk_136_gm_jerk_ar1_persistence_12q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """AR(1) corr of GM jerk on its 1-lag over 12q."""
    j = _jerk(_gm(revenue, gp))
    return j.rolling(12, min_periods=4).corr(j.shift(1))


def f35_mcjk_137_4margin_jerk_negative_q_in_last_4_count_4_indicator(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Indicator: in last 4 quarters, all 4 margins had at least one negative-jerk quarter."""
    g = _jerk(_gm(revenue, gp)) < 0; o = _jerk(_om(revenue, opinc)) < 0; e = _jerk(_em(revenue, ebitda)) < 0; n = _jerk(_nm(revenue, netinc)) < 0
    any_g = g.astype(float).rolling(4, min_periods=1).sum() > 0
    any_o = o.astype(float).rolling(4, min_periods=1).sum() > 0
    any_e = e.astype(float).rolling(4, min_periods=1).sum() > 0
    any_n = n.astype(float).rolling(4, min_periods=1).sum() > 0
    return (any_g & any_o & any_e & any_n).astype(float)


def f35_mcjk_138_om_jerk_decay_into_neg_terminal_4q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """(OM jerk - OM jerk lagged 4q) where OM jerk is currently negative."""
    j = _jerk(_om(revenue, opinc))
    cond = j < 0
    return (j - j.shift(4)).where(cond, np.nan)


def f35_mcjk_139_nm_jerk_terminal_collapse_proxy_20q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Z-score of NM jerk over 20q clipped at -3 then ema(8) — terminal-decline accumulator."""
    z = _rolling_zscore(_jerk(_nm(revenue, netinc)), 20).clip(upper=0)
    return _ema(z, 8)


def f35_mcjk_140_weighted_multi_margin_jerk_crash_z_clipm3_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Sum of clip(z(neg-jerk), 0, 3) across 4 margins, 8q."""
    g = _rolling_zscore((-_jerk(_gm(revenue, gp))).clip(lower=0), 8).clip(lower=0, upper=3)
    o = _rolling_zscore((-_jerk(_om(revenue, opinc))).clip(lower=0), 8).clip(lower=0, upper=3)
    e = _rolling_zscore((-_jerk(_em(revenue, ebitda))).clip(lower=0), 8).clip(lower=0, upper=3)
    n = _rolling_zscore((-_jerk(_nm(revenue, netinc))).clip(lower=0), 8).clip(lower=0, upper=3)
    return g.fillna(0) + o.fillna(0) + e.fillna(0) + n.fillna(0)


def f35_mcjk_141_multi_horizon_jerk_crash_score_om(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Sum of OM jerk negative-clip z at 8q + 12q + 20q — multi-horizon OM jerk crash."""
    j = _jerk(_om(revenue, opinc))
    neg = (-j).clip(lower=0)
    return _rolling_zscore(neg, 8).fillna(0) + _rolling_zscore(neg, 12).fillna(0) + _rolling_zscore(neg, 20).fillna(0)


def f35_mcjk_142_ewm_decay_jerk_crash_8q_nm_neg(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """EWMA(span 8) of (-NM jerk).clip(lower=0)."""
    j = _jerk(_nm(revenue, netinc))
    return _ema((-j).clip(lower=0), 8)


def f35_mcjk_143_logit_margin_jerk_crash_probability_om(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Logit-normalized linear combination of OM jerk z-scores at 8q, 12q, 20q."""
    j = _jerk(_om(revenue, opinc))
    score = -1.0 * (_rolling_zscore(j, 8).fillna(0) + 0.5 * _rolling_zscore(j, 12).fillna(0) + 0.25 * _rolling_zscore(j, 20).fillna(0))
    return 1.0 / (1.0 + np.exp(-score))


def f35_mcjk_144_mahalanobis_jerk_om_slope_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Approx Mahalanobis distance of (OM jerk, OM jerk slope4q) from 8q mean (uncorrelated approx)."""
    j = _jerk(_om(revenue, opinc)); sl = _rolling_slope(j, 4)
    z1 = _rolling_zscore(j, 8); z2 = _rolling_zscore(sl, 8)
    return (z1.pow(2) + z2.pow(2)).pow(0.5)


def f35_mcjk_145_hotelling_t_om_jerk_vol_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Hotelling-T proxy: sqrt(z(OM jerk)^2 + z(OM jerk vol)^2) over 8q."""
    j = _jerk(_om(revenue, opinc))
    vol = j.rolling(4, min_periods=2).std()
    return ((_rolling_zscore(j, 8).pow(2) + _rolling_zscore(vol, 8).pow(2))).pow(0.5)


def f35_mcjk_146_composite_jerk_collapse_aggregate(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """Aggregate: z(4margin compound) + z(majority-neg streak) + z(dispersion) + z(worst-margin signed)."""
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    z_g = _rolling_zscore(g, 8); z_o = _rolling_zscore(o, 8); z_e = _rolling_zscore(e, 8); z_n = _rolling_zscore(n, 8)
    compound = z_g + z_o + z_e + z_n
    majority = ((g < 0).astype(int) + (o < 0).astype(int) + (e < 0).astype(int) + (n < 0).astype(int)) >= 3
    streak = _max_consec_true(majority, 12)
    disp = pd.concat([g, o, e, n], axis=1).std(axis=1)
    worst = pd.concat([g, o, e, n], axis=1).min(axis=1)
    return _rolling_zscore(compound, 12).fillna(0) + _rolling_zscore(streak, 12).fillna(0) + _rolling_zscore(disp, 12).fillna(0) - _rolling_zscore(worst, 12).fillna(0)


def f35_mcjk_147_om_jerk_terminal_distance_5y_proxy(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Sum of last 20q clip(-OM jerk, 0) divided by 20."""
    j = _jerk(_om(revenue, opinc))
    return (-j).clip(lower=0).rolling(20, min_periods=6).sum() / 20.0


def f35_mcjk_148_gm_ttm_jerk_onset_after_dormancy_4q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Onset-after-calm on TTM-GM: jerk |z(8q)|>3 firing after 4q dormant period (|z|<1 in ≥75% of prior 4q)."""
    margin = _gm_ttm(revenue, gp)
    j = _jerk(margin)
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f35_mcjk_149_om_ttm_jerk_neg_streak_max_16q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Max consec negative-jerk streak on TTM-OM over 16q."""
    j = _jerk(_om_ttm(revenue, opinc))
    return _max_consec_true(j < 0, 16)


def f35_mcjk_150_nm_ttm_jerk_cliff_count_12q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Count of TTM-NM jerk cliffs (|jerk|>2*MAD) over 12q."""
    j = _jerk(_nm_ttm(revenue, netinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


MARGIN_COLLAPSE_JERK_BASE_REGISTRY_076_150 = {
    "f35_mcjk_076_4margin_jerk_kurt_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_076_4margin_jerk_kurt_8q},
    "f35_mcjk_077_gm_om_em_nm_jerk_descending_breach_count_8q": {"inputs": ["revenue", "gp", "opinc", "netinc"], "func": f35_mcjk_077_gm_om_em_nm_jerk_descending_breach_count_8q},
    "f35_mcjk_078_4margin_jerk_avg_minus_ewma8": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_078_4margin_jerk_avg_minus_ewma8},
    "f35_mcjk_079_4margin_jerk_mean_persistence_lag1_12q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_079_4margin_jerk_mean_persistence_lag1_12q},
    "f35_mcjk_080_gm_jerk_cusum_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_080_gm_jerk_cusum_12q},
    "f35_mcjk_081_om_jerk_cusum_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_081_om_jerk_cusum_12q},
    "f35_mcjk_082_em_jerk_cusum_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_082_em_jerk_cusum_12q},
    "f35_mcjk_083_nm_jerk_cusum_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_083_nm_jerk_cusum_12q},
    "f35_mcjk_084_gm_jerk_mean_shift_t_4q_vs_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_084_gm_jerk_mean_shift_t_4q_vs_12q},
    "f35_mcjk_085_om_jerk_mean_shift_t_4q_vs_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_085_om_jerk_mean_shift_t_4q_vs_12q},
    "f35_mcjk_086_em_jerk_mean_shift_t_4q_vs_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_086_em_jerk_mean_shift_t_4q_vs_12q},
    "f35_mcjk_087_nm_jerk_mean_shift_t_4q_vs_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_087_nm_jerk_mean_shift_t_4q_vs_12q},
    "f35_mcjk_088_gm_jerk_variance_jump_4q_vs_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_088_gm_jerk_variance_jump_4q_vs_12q},
    "f35_mcjk_089_om_jerk_variance_jump_4q_vs_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_089_om_jerk_variance_jump_4q_vs_12q},
    "f35_mcjk_090_em_jerk_variance_jump_4q_vs_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_090_em_jerk_variance_jump_4q_vs_12q},
    "f35_mcjk_091_nm_jerk_variance_jump_4q_vs_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_091_nm_jerk_variance_jump_4q_vs_12q},
    "f35_mcjk_092_gm_jerk_quandt_proxy_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_092_gm_jerk_quandt_proxy_12q},
    "f35_mcjk_093_om_jerk_quandt_proxy_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_093_om_jerk_quandt_proxy_12q},
    "f35_mcjk_094_em_jerk_quandt_proxy_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_094_em_jerk_quandt_proxy_12q},
    "f35_mcjk_095_nm_jerk_quandt_proxy_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_095_nm_jerk_quandt_proxy_12q},
    "f35_mcjk_096_gm_jerk_break_recency_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_096_gm_jerk_break_recency_12q},
    "f35_mcjk_097_om_jerk_break_recency_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_097_om_jerk_break_recency_12q},
    "f35_mcjk_098_em_jerk_break_recency_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_098_em_jerk_break_recency_12q},
    "f35_mcjk_099_nm_jerk_break_recency_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_099_nm_jerk_break_recency_12q},
    "f35_mcjk_100_gm_jerk_q_since_min_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_100_gm_jerk_q_since_min_12q},
    "f35_mcjk_101_om_jerk_q_since_min_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_101_om_jerk_q_since_min_12q},
    "f35_mcjk_102_em_jerk_q_since_min_12q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_102_em_jerk_q_since_min_12q},
    "f35_mcjk_103_nm_jerk_q_since_min_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_103_nm_jerk_q_since_min_12q},
    "f35_mcjk_104_gm_jerk_ulcer_index_neg_8q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_104_gm_jerk_ulcer_index_neg_8q},
    "f35_mcjk_105_om_jerk_ulcer_index_neg_8q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_105_om_jerk_ulcer_index_neg_8q},
    "f35_mcjk_106_em_jerk_ulcer_index_neg_8q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_106_em_jerk_ulcer_index_neg_8q},
    "f35_mcjk_107_nm_jerk_ulcer_index_neg_8q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_107_nm_jerk_ulcer_index_neg_8q},
    "f35_mcjk_108_gm_jerk_event_count_below_q10_16q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_108_gm_jerk_event_count_below_q10_16q},
    "f35_mcjk_109_om_jerk_event_count_below_q10_16q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_109_om_jerk_event_count_below_q10_16q},
    "f35_mcjk_110_em_jerk_event_count_below_q10_16q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_110_em_jerk_event_count_below_q10_16q},
    "f35_mcjk_111_nm_jerk_event_count_below_q10_16q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_111_nm_jerk_event_count_below_q10_16q},
    "f35_mcjk_112_gm_jerk_decline_streak_max_16q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_112_gm_jerk_decline_streak_max_16q},
    "f35_mcjk_113_om_jerk_decline_streak_max_16q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_113_om_jerk_decline_streak_max_16q},
    "f35_mcjk_114_em_jerk_decline_streak_max_16q": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_114_em_jerk_decline_streak_max_16q},
    "f35_mcjk_115_nm_jerk_decline_streak_max_16q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_115_nm_jerk_decline_streak_max_16q},
    "f35_mcjk_116_gm_jerk_recovery_speed_from_8q_min": {"inputs": ["revenue", "gp"], "func": f35_mcjk_116_gm_jerk_recovery_speed_from_8q_min},
    "f35_mcjk_117_om_jerk_recovery_speed_from_8q_min": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_117_om_jerk_recovery_speed_from_8q_min},
    "f35_mcjk_118_em_jerk_recovery_speed_from_8q_min": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_118_em_jerk_recovery_speed_from_8q_min},
    "f35_mcjk_119_nm_jerk_recovery_speed_from_8q_min": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_119_nm_jerk_recovery_speed_from_8q_min},
    "f35_mcjk_120_composite_jerk_fragility_4margin_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_120_composite_jerk_fragility_4margin_8q},
    "f35_mcjk_121_conditional_jerk_given_low_om_level_12q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_121_conditional_jerk_given_low_om_level_12q},
    "f35_mcjk_122_conditional_jerk_given_low_gm_level_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_122_conditional_jerk_given_low_gm_level_12q},
    "f35_mcjk_123_conditional_jerk_given_neg_revenue_growth_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_123_conditional_jerk_given_neg_revenue_growth_12q},
    "f35_mcjk_124_om_jerk_minus_revenue_growth_jerk_8q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_124_om_jerk_minus_revenue_growth_jerk_8q},
    "f35_mcjk_125_nm_jerk_minus_revenue_growth_jerk_8q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_125_nm_jerk_minus_revenue_growth_jerk_8q},
    "f35_mcjk_126_cogs_share_jerk_onset_after_dormancy_8q": {"inputs": ["revenue", "cor"], "func": f35_mcjk_126_cogs_share_jerk_onset_after_dormancy_8q},
    "f35_mcjk_127_sgna_share_jerk_cliff_conditional_on_high_share_8q": {"inputs": ["revenue", "sgna"], "func": f35_mcjk_127_sgna_share_jerk_cliff_conditional_on_high_share_8q},
    "f35_mcjk_128_opex_share_jerk_3consec_pos_streak_max_16q": {"inputs": ["revenue", "opex"], "func": f35_mcjk_128_opex_share_jerk_3consec_pos_streak_max_16q},
    "f35_mcjk_129_depamor_share_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["revenue", "depamor"], "func": f35_mcjk_129_depamor_share_jerk_multi_horizon_onset_4_8_12q},
    "f35_mcjk_130_cogs_sgna_jerk_simultaneous_jump_count_8q": {"inputs": ["revenue", "cor", "sgna"], "func": f35_mcjk_130_cogs_sgna_jerk_simultaneous_jump_count_8q},
    "f35_mcjk_131_cost_stack_jerk_dispersion_8q": {"inputs": ["revenue", "cor", "sgna", "depamor"], "func": f35_mcjk_131_cost_stack_jerk_dispersion_8q},
    "f35_mcjk_132_nm_jerk_smoothed_minus_raw_disagree_8q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_132_nm_jerk_smoothed_minus_raw_disagree_8q},
    "f35_mcjk_133_om_jerk_ema4_minus_ema12": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_133_om_jerk_ema4_minus_ema12},
    "f35_mcjk_134_nm_jerk_skew_change_8q_vs_16q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_134_nm_jerk_skew_change_8q_vs_16q},
    "f35_mcjk_135_om_jerk_ar1_persistence_8q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_135_om_jerk_ar1_persistence_8q},
    "f35_mcjk_136_gm_jerk_ar1_persistence_12q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_136_gm_jerk_ar1_persistence_12q},
    "f35_mcjk_137_4margin_jerk_negative_q_in_last_4_count_4_indicator": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_137_4margin_jerk_negative_q_in_last_4_count_4_indicator},
    "f35_mcjk_138_om_jerk_decay_into_neg_terminal_4q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_138_om_jerk_decay_into_neg_terminal_4q},
    "f35_mcjk_139_nm_jerk_terminal_collapse_proxy_20q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_139_nm_jerk_terminal_collapse_proxy_20q},
    "f35_mcjk_140_weighted_multi_margin_jerk_crash_z_clipm3_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_140_weighted_multi_margin_jerk_crash_z_clipm3_8q},
    "f35_mcjk_141_multi_horizon_jerk_crash_score_om": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_141_multi_horizon_jerk_crash_score_om},
    "f35_mcjk_142_ewm_decay_jerk_crash_8q_nm_neg": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_142_ewm_decay_jerk_crash_8q_nm_neg},
    "f35_mcjk_143_logit_margin_jerk_crash_probability_om": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_143_logit_margin_jerk_crash_probability_om},
    "f35_mcjk_144_mahalanobis_jerk_om_slope_8q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_144_mahalanobis_jerk_om_slope_8q},
    "f35_mcjk_145_hotelling_t_om_jerk_vol_8q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_145_hotelling_t_om_jerk_vol_8q},
    "f35_mcjk_146_composite_jerk_collapse_aggregate": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_146_composite_jerk_collapse_aggregate},
    "f35_mcjk_147_om_jerk_terminal_distance_5y_proxy": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_147_om_jerk_terminal_distance_5y_proxy},
    "f35_mcjk_148_gm_ttm_jerk_onset_after_dormancy_4q": {"inputs": ["revenue", "gp"], "func": f35_mcjk_148_gm_ttm_jerk_onset_after_dormancy_4q},
    "f35_mcjk_149_om_ttm_jerk_neg_streak_max_16q": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_149_om_ttm_jerk_neg_streak_max_16q},
    "f35_mcjk_150_nm_ttm_jerk_cliff_count_12q": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_150_nm_ttm_jerk_cliff_count_12q},
}
