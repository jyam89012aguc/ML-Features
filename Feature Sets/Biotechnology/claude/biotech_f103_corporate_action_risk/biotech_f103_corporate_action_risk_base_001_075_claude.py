"""Family f103 - Corporate action risk from silver DB actions | base 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _flag(action, values):
    text = globals().get("action_text", action).fillna("").astype(str).str.lower()
    return text.isin(values).astype(float)


def _contains(action, token):
    return globals().get("action_text", action).fillna("").astype(str).str.lower().str.contains(token, regex=False).astype(float)


# 252d bankruptcy/liquidation action cadence
def car_f103_corporate_action_risk_bankruptcy_252d_base_v001_signal(action):
    result = _sum(_flag(action, {"bankruptcyliquidation"}), 252)
    return _clean(result)


# 252d regulatory or voluntary delisting cadence
def car_f103_corporate_action_risk_delisting_252d_base_v002_signal(action):
    result = _sum(_flag(action, {"regulatorydelisting", "voluntarydelisting", "delisted"}), 252)
    return _clean(result)


# 504d distress action cadence
def car_f103_corporate_action_risk_distress_504d_base_v003_signal(action):
    flags = _flag(action, {"bankruptcyliquidation", "regulatorydelisting", "voluntarydelisting", "delisted"})
    result = _sum(flags, 504)
    return _clean(result)


# 252d split cadence
def car_f103_corporate_action_risk_split_252d_base_v004_signal(action):
    result = _sum(_contains(action, "split"), 252)
    return _clean(result)


# 1008d split cadence
def car_f103_corporate_action_risk_split_1008d_base_v005_signal(action):
    result = _sum(_contains(action, "split"), 1008)
    return _clean(result)


# 252d ticker change cadence
def car_f103_corporate_action_risk_ticker_change_252d_base_v006_signal(action):
    result = _sum(_contains(action, "tickerchange"), 252)
    return _clean(result)


# 1008d ticker change cadence
def car_f103_corporate_action_risk_ticker_change_1008d_base_v007_signal(action):
    result = _sum(_contains(action, "tickerchange"), 1008)
    return _clean(result)


# 504d acquisition action cadence
def car_f103_corporate_action_risk_acquisition_504d_base_v008_signal(action):
    result = _sum(_contains(action, "acquisition"), 504)
    return _clean(result)


# 504d spinoff action cadence
def car_f103_corporate_action_risk_spinoff_504d_base_v009_signal(action):
    result = _sum(_contains(action, "spinoff"), 504)
    return _clean(result)


# 252d non-dividend corporate action density
def car_f103_corporate_action_risk_non_dividend_density_252d_base_v010_signal(action):
    text = action.fillna("").astype(str).str.lower()
    result = _sum((text.ne("") & text.ne("dividend")).astype(float), 252)
    return _clean(result)


# 252d corporate action value pressure
def car_f103_corporate_action_risk_action_value_252d_base_v011_signal(action, value):
    text = action.fillna("").astype(str).str.lower()
    result = _sum(value.where(text.ne("dividend")).abs(), 252)
    return _clean(result)


# 252d identity instability: ticker changes plus splits
def car_f103_corporate_action_risk_identity_instability_252d_base_v012_signal(action):
    result = _sum(_contains(action, "tickerchange") + _contains(action, "split"), 252)
    return _clean(result)
