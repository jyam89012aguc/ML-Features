"""revenue_deceleration_acceleration d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


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


def _yoy(s):
    return _safe_div(s - s.shift(QQTRS), s.shift(QQTRS).abs())


def f29_rdac_151_hmm_decel_posterior_2state_8q_d2(revenue: pd.Series) -> pd.Series:
    if revenue is None:
        return pd.Series(np.nan)
    yoy = _yoy(revenue)

    def _post(w):
        valid = w[~np.isnan(w)]
        if len(valid) < 4:
            return np.nan
        sorted_w = np.sort(valid)
        med = np.median(valid)
        low = sorted_w[sorted_w <= med]
        high = sorted_w[sorted_w > med]
        if len(low) < 2 or len(high) < 2:
            return np.nan
        mu_d, sd_d = float(low.mean()), float(low.std(ddof=1))
        mu_h, sd_h = float(high.mean()), float(high.std(ddof=1))
        if sd_d <= 0 or sd_h <= 0 or not np.isfinite(sd_d) or not np.isfinite(sd_h):
            return np.nan
        x_t = w[-1]
        if np.isnan(x_t):
            return np.nan
        pi_d = len(low) / len(valid)
        pi_h = len(high) / len(valid)
        p_d = np.exp(-0.5 * ((x_t - mu_d) / sd_d) ** 2) / (sd_d * np.sqrt(2.0 * np.pi))
        p_h = np.exp(-0.5 * ((x_t - mu_h) / sd_h) ** 2) / (sd_h * np.sqrt(2.0 * np.pi))
        num = p_d * pi_d
        den = num + p_h * pi_h
        if den <= 0 or not np.isfinite(den):
            return np.nan
        return float(num / den)

    return yoy.rolling(QQTRS_2Y, min_periods=4).apply(_post, raw=True).diff().diff()


def f29_rdac_152_markov_switching_variance_posterior_8q_d2(revenue: pd.Series) -> pd.Series:
    if revenue is None:
        return pd.Series(np.nan)
    yoy = _yoy(revenue)
    ch = yoy.diff()
    vol = ch.abs()

    def _post_var(w):
        valid = w[~np.isnan(w)]
        if len(valid) < 4:
            return np.nan
        sorted_w = np.sort(valid)
        med = np.median(valid)
        low = sorted_w[sorted_w <= med]
        high = sorted_w[sorted_w > med]
        if len(low) < 2 or len(high) < 2:
            return np.nan
        mu_l, sd_l = float(low.mean()), float(low.std(ddof=1))
        mu_h, sd_h = float(high.mean()), float(high.std(ddof=1))
        if sd_l <= 0 or sd_h <= 0 or not np.isfinite(sd_l) or not np.isfinite(sd_h):
            return np.nan
        x_t = w[-1]
        if np.isnan(x_t):
            return np.nan
        pi_l = len(low) / len(valid)
        pi_h = len(high) / len(valid)
        p_l = np.exp(-0.5 * ((x_t - mu_l) / sd_l) ** 2) / (sd_l * np.sqrt(2.0 * np.pi))
        p_h = np.exp(-0.5 * ((x_t - mu_h) / sd_h) ** 2) / (sd_h * np.sqrt(2.0 * np.pi))
        num = p_h * pi_h
        den = p_l * pi_l + num
        if den <= 0 or not np.isfinite(den):
            return np.nan
        return float(num / den)

    return vol.rolling(QQTRS_2Y, min_periods=4).apply(_post_var, raw=True).diff().diff()


def f29_rdac_153_multi_metric_break_dispersion_8q_d2(revenue: pd.Series, gp: pd.Series, netinc: pd.Series) -> pd.Series:
    if revenue is None or gp is None or netinc is None:
        return pd.Series(np.nan)
    rev_yoy = _yoy(revenue)
    gp_yoy = _yoy(gp)
    ni_yoy = _yoy(netinc)

    def _break_q(w):
        valid = w[~np.isnan(w)]
        if len(valid) < 6:
            return np.nan
        n = len(w)
        best_diff = -np.inf
        best_q = np.nan
        for k in range(2, n - 1):
            left = w[:k]
            right = w[k:]
            lv = left[~np.isnan(left)]
            rv = right[~np.isnan(right)]
            if len(lv) < 2 or len(rv) < 2:
                continue
            d = abs(float(lv.mean()) - float(rv.mean()))
            if d > best_diff:
                best_diff = d
                best_q = k
        return float(best_q) if np.isfinite(best_q) else np.nan

    bq_rev = rev_yoy.rolling(QQTRS_2Y, min_periods=6).apply(_break_q, raw=True)
    bq_gp = gp_yoy.rolling(QQTRS_2Y, min_periods=6).apply(_break_q, raw=True)
    bq_ni = ni_yoy.rolling(QQTRS_2Y, min_periods=6).apply(_break_q, raw=True)
    stacked = pd.concat([bq_rev, bq_gp, bq_ni], axis=1)
    return (stacked.max(axis=1) - stacked.min(axis=1)).diff().diff()


def f29_rdac_154_calm_then_cliff_indicator_d2(revenue: pd.Series) -> pd.Series:
    if revenue is None:
        return pd.Series(np.nan)
    yoy = _yoy(revenue)
    sd_prior5 = yoy.shift(1).rolling(5, min_periods=3).std()
    sd_full12 = yoy.rolling(QQTRS_3Y, min_periods=6).std()
    jump = (yoy - yoy.shift(1)).abs()
    cond_calm = sd_prior5 < 0.5 * sd_full12
    cond_cliff = jump > 3.0 * sd_prior5
    out = (cond_calm & cond_cliff).astype(float)
    return out.where(yoy.notna() & sd_prior5.notna() & sd_full12.notna(), np.nan).diff().diff()


REVENUE_DECELERATION_ACCELERATION_D2_REGISTRY_151_225 = {
    "f29_rdac_151_hmm_decel_posterior_2state_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_151_hmm_decel_posterior_2state_8q_d2},
    "f29_rdac_152_markov_switching_variance_posterior_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_152_markov_switching_variance_posterior_8q_d2},
    "f29_rdac_153_multi_metric_break_dispersion_8q_d2": {"inputs": ["revenue", "gp", "netinc"], "func": f29_rdac_153_multi_metric_break_dispersion_8q_d2},
    "f29_rdac_154_calm_then_cliff_indicator_d2": {"inputs": ["revenue"], "func": f29_rdac_154_calm_then_cliff_indicator_d2},
}
