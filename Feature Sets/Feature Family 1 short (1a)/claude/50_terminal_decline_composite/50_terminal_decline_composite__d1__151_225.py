"""terminal_decline_composite d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12


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


def f50_tdcp_151_insider_mass_exit_x_drawdown_d1(insider_sell_value: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    if insider_sell_value is None or close is None or high is None:
        return pd.Series(np.nan)
    sell_63d = insider_sell_value.rolling(QDAYS, min_periods=int(QDAYS * 0.3)).sum()
    rmax = high.rolling(YDAYS, min_periods=int(YDAYS * 0.3)).max()
    dd = 1.0 - _safe_div(close, rmax)
    return (sell_63d * dd).diff()


def f50_tdcp_152_si_accel_x_terminal_state_d1(shortinterest: pd.Series, netinc: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    if shortinterest is None or netinc is None or close is None or high is None:
        return pd.Series(np.nan)
    si_accel = shortinterest.diff(QDAYS)
    rmax = high.rolling(YDAYS, min_periods=int(YDAYS * 0.3)).max()
    dd = 1.0 - _safe_div(close, rmax)
    terminal = ((netinc < 0) & (dd > 0.5)).astype(float)
    return (si_accel * terminal).diff()


def f50_tdcp_153_all_distress_signals_count_q_d1(netinc: pd.Series, ncfo: pd.Series, fcf: pd.Series, close: pd.Series, high: pd.Series, sharesbas: pd.Series, debt: pd.Series, opinc: pd.Series) -> pd.Series:
    if any(x is None for x in [netinc, ncfo, fcf, close, high, sharesbas, debt, opinc]):
        return pd.Series(np.nan)
    rmax = high.rolling(YDAYS, min_periods=int(YDAYS * 0.3)).max()
    dd = 1.0 - _safe_div(close, rmax)
    sb_yoy = _safe_div(sharesbas - sharesbas.shift(YDAYS), sharesbas.shift(YDAYS).abs())
    debt_yoy = _safe_div(debt - debt.shift(YDAYS), debt.shift(YDAYS).abs())
    opinc_yoy = _safe_div(opinc - opinc.shift(YDAYS), opinc.shift(YDAYS).abs())
    s1 = (netinc < 0).astype(float).where(netinc.notna(), 0.0)
    s2 = (ncfo < 0).astype(float).where(ncfo.notna(), 0.0)
    s3 = (fcf < 0).astype(float).where(fcf.notna(), 0.0)
    s4 = (dd > 0.30).astype(float).where(dd.notna(), 0.0)
    s5 = (sb_yoy > 0.05).astype(float).where(sb_yoy.notna(), 0.0)
    s6 = (debt_yoy > 0.10).astype(float).where(debt_yoy.notna(), 0.0)
    s7 = (opinc_yoy < 0).astype(float).where(opinc_yoy.notna(), 0.0)
    total = s1 + s2 + s3 + s4 + s5 + s6 + s7
    any_valid = netinc.notna() | ncfo.notna() | fcf.notna() | dd.notna() | sb_yoy.notna() | debt_yoy.notna() | opinc_yoy.notna()
    return total.where(any_valid, np.nan).diff()


def f50_tdcp_154_time_in_distress_persistence_12q_d1(netinc: pd.Series, fcf: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    if netinc is None or fcf is None or close is None or high is None:
        return pd.Series(np.nan)
    rmax = high.rolling(YDAYS, min_periods=int(YDAYS * 0.3)).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = ((netinc < 0) & (fcf < 0) & (dd > 0.30)).astype(float)
    cond = cond.where(netinc.notna() & fcf.notna() & dd.notna(), 0.0)
    return (cond.rolling(12 * QDAYS, min_periods=int(12 * QDAYS * 0.25)).mean() * 12.0).diff()


def f50_tdcp_155_terminal_state_2state_posterior_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    if any(x is None for x in [revenue, opinc, fcf, close, high]):
        return pd.Series(np.nan)
    rev_yoy = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    om = _safe_div(opinc, revenue)
    fcf_yoy = _safe_div(fcf - fcf.shift(YDAYS), fcf.shift(YDAYS).abs())
    rmax = high.rolling(YDAYS, min_periods=int(YDAYS * 0.3)).max()
    dd = 1.0 - _safe_div(close, rmax)
    df = pd.concat([rev_yoy, om, fcf_yoy, dd], axis=1)
    df.columns = ["a", "b", "c", "d"]
    win = YDAYS
    mp = int(win * 0.3)
    a_med = df["a"].rolling(win, min_periods=mp).median()
    b_med = df["b"].rolling(win, min_periods=mp).median()
    c_med = df["c"].rolling(win, min_periods=mp).median()
    d_med = df["d"].rolling(win, min_periods=mp).median()
    a_dist = df["a"].rolling(win, min_periods=mp).min()
    b_dist = df["b"].rolling(win, min_periods=mp).min()
    c_dist = df["c"].rolling(win, min_periods=mp).min()
    d_dist = df["d"].rolling(win, min_periods=mp).max()
    a_sd = df["a"].rolling(win, min_periods=mp).std().replace(0, np.nan)
    b_sd = df["b"].rolling(win, min_periods=mp).std().replace(0, np.nan)
    c_sd = df["c"].rolling(win, min_periods=mp).std().replace(0, np.nan)
    d_sd = df["d"].rolling(win, min_periods=mp).std().replace(0, np.nan)
    dist_h = np.sqrt(((df["a"] - a_med) / a_sd) ** 2 + ((df["b"] - b_med) / b_sd) ** 2 + ((df["c"] - c_med) / c_sd) ** 2 + ((df["d"] - d_med) / d_sd) ** 2)
    dist_d = np.sqrt(((df["a"] - a_dist) / a_sd) ** 2 + ((df["b"] - b_dist) / b_sd) ** 2 + ((df["c"] - c_dist) / c_sd) ** 2 + ((df["d"] - d_dist) / d_sd) ** 2)
    inv_h = 1.0 / dist_h.replace(0, np.nan)
    inv_d = 1.0 / dist_d.replace(0, np.nan)
    denom = (inv_h + inv_d).replace(0, np.nan)
    return _safe_div(inv_d, denom).diff()


TERMINAL_DECLINE_COMPOSITE_D1_REGISTRY_151_225 = {
    "f50_tdcp_151_insider_mass_exit_x_drawdown_d1": {"inputs": ["insider_sell_value", "close", "high"], "func": f50_tdcp_151_insider_mass_exit_x_drawdown_d1},
    "f50_tdcp_152_si_accel_x_terminal_state_d1": {"inputs": ["shortinterest", "netinc", "close", "high"], "func": f50_tdcp_152_si_accel_x_terminal_state_d1},
    "f50_tdcp_153_all_distress_signals_count_q_d1": {"inputs": ["netinc", "ncfo", "fcf", "close", "high", "sharesbas", "debt", "opinc"], "func": f50_tdcp_153_all_distress_signals_count_q_d1},
    "f50_tdcp_154_time_in_distress_persistence_12q_d1": {"inputs": ["netinc", "fcf", "close", "high"], "func": f50_tdcp_154_time_in_distress_persistence_12q_d1},
    "f50_tdcp_155_terminal_state_2state_posterior_d1": {"inputs": ["revenue", "opinc", "fcf", "close", "high"], "func": f50_tdcp_155_terminal_state_2state_posterior_d1},
}
