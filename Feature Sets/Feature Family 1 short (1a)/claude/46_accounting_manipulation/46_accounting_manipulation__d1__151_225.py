"""accounting_manipulation d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


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


def _ttm(s):
    return s.rolling(QQTRS, min_periods=1).sum()


def _dd_residual_series(accr: pd.Series, ncfo_a: pd.Series, window: int = QQTRS_5Y) -> pd.Series:
    x_lag = ncfo_a.shift(1)
    x_cur = ncfo_a
    x_lead = ncfo_a
    df = pd.concat([accr, x_lag, x_cur, x_lead], axis=1)
    df.columns = ["y", "x1", "x2", "x3"]
    arr = df.to_numpy(dtype=float)
    idx_series = pd.Series(np.arange(len(arr), dtype=float), index=accr.index)
    min_p = max(window // 2, 6)

    def _resid(idx_win):
        if len(idx_win) < min_p:
            return np.nan
        end_i = int(idx_win[-1])
        start_i = int(idx_win[0])
        block = arr[start_i : end_i + 1]
        mask = ~np.isnan(block).any(axis=1)
        if mask.sum() < min_p or not mask[-1]:
            return np.nan
        b = block[mask]
        y = b[:, 0]
        X = np.column_stack([np.ones(b.shape[0]), b[:, 1], b[:, 2], b[:, 3]])
        try:
            beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        except np.linalg.LinAlgError:
            return np.nan
        last = block[-1]
        pred = float(beta[0] + beta[1] * last[1] + beta[2] * last[2] + beta[3] * last[3])
        return float(last[0] - pred)

    return idx_series.rolling(window, min_periods=min_p).apply(_resid, raw=True)


def f46_amnp_151_piotroski_f_score_full_9_signals_d1(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series, currentassets: pd.Series, currentliab: pd.Series, sharesbas: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    ni_ttm = _ttm(netinc)
    ncfo_ttm = _ttm(ncfo)
    roa = _safe_div(ni_ttm, assets)
    s1 = (ni_ttm > 0).astype(float)
    s2 = (ncfo_ttm > 0).astype(float)
    s3 = ((roa - roa.shift(QQTRS)) > 0).astype(float)
    s4 = (ncfo_ttm > ni_ttm).astype(float)
    lev = _safe_div(debt, assets)
    s5 = ((lev - lev.shift(QQTRS)) < 0).astype(float)
    cr = _safe_div(currentassets, currentliab)
    s6 = ((cr - cr.shift(QQTRS)) > 0).astype(float)
    s7 = ((sharesbas - sharesbas.shift(QQTRS)) <= 0).astype(float)
    gm = _safe_div(gp, revenue)
    s8 = ((gm - gm.shift(QQTRS)) > 0).astype(float)
    at = _safe_div(revenue, assets)
    s9 = ((at - at.shift(QQTRS)) > 0).astype(float)
    parts = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    total = pd.Series(0.0, index=netinc.index)
    any_valid = pd.Series(False, index=netinc.index)
    for p in parts:
        valid = p.notna()
        total = total + p.where(valid, 0.0)
        any_valid = any_valid | valid
    return total.where(any_valid, np.nan).diff()


def f46_amnp_152_dechow_dichev_proper_residual_quality_5y_d1(workingcapital: pd.Series, depamor: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    delta_wc = workingcapital.diff()
    accr = _safe_div(delta_wc - depamor, assets)
    ncfo_a = _safe_div(ncfo, assets)
    return _dd_residual_series(accr, ncfo_a, window=QQTRS_5Y).diff()


def f46_amnp_153_big_bath_writedown_indicator_d1(opinc: pd.Series, intangibles: pd.Series, ppnenet: pd.Series) -> pd.Series:
    d_op = opinc.diff()
    sd_prior = d_op.shift(1).rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 3, 2)).std()
    drop = d_op < (-2.0 * sd_prior)
    d_intang = intangibles.diff()
    intang_down = d_intang < 0
    ppne_pct = _safe_div(ppnenet.diff(), ppnenet.shift(1).abs())
    ppne_drop = ppne_pct < -0.05
    valid = sd_prior.notna() & d_op.notna() & (d_intang.notna() | ppne_pct.notna())
    flag = (drop & (intang_down.fillna(False) | ppne_drop.fillna(False))).astype(float)
    return flag.where(valid, np.nan).diff()


def f46_amnp_154_round_tripping_revenue_proxy_d1(revenue: pd.Series, receivables: pd.Series, payables: pd.Series) -> pd.Series:
    z_rev = _rolling_zscore(revenue.diff(), QQTRS_2Y)
    z_rec = _rolling_zscore(receivables.diff(), QQTRS_2Y)
    z_pay = _rolling_zscore(payables.diff(), QQTRS_2Y)
    valid = z_rev.notna() & z_rec.notna() & z_pay.notna()
    flag = ((z_rev > 2.0) & (z_rec > 2.0) & (z_pay > 2.0)).astype(float)
    return flag.where(valid, np.nan).diff()


def f46_amnp_155_auditor_change_flag_proxy_4q_d1(auditor_change_event: pd.Series) -> pd.Series:
    s = auditor_change_event.astype(float)
    return s.rolling(QQTRS, min_periods=1).max().diff()


ACCOUNTING_MANIPULATION_D1_REGISTRY_151_225 = {
    "f46_amnp_151_piotroski_f_score_full_9_signals_d1": {"inputs": ["netinc", "ncfo", "assets", "debt", "currentassets", "currentliab", "sharesbas", "gp", "revenue"], "func": f46_amnp_151_piotroski_f_score_full_9_signals_d1},
    "f46_amnp_152_dechow_dichev_proper_residual_quality_5y_d1": {"inputs": ["workingcapital", "depamor", "ncfo", "assets"], "func": f46_amnp_152_dechow_dichev_proper_residual_quality_5y_d1},
    "f46_amnp_153_big_bath_writedown_indicator_d1": {"inputs": ["opinc", "intangibles", "ppnenet"], "func": f46_amnp_153_big_bath_writedown_indicator_d1},
    "f46_amnp_154_round_tripping_revenue_proxy_d1": {"inputs": ["revenue", "receivables", "payables"], "func": f46_amnp_154_round_tripping_revenue_proxy_d1},
    "f46_amnp_155_auditor_change_flag_proxy_4q_d1": {"inputs": ["auditor_change_event"], "func": f46_amnp_155_auditor_change_flag_proxy_4q_d1},
}
