
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

def _contains(s, pattern):
    if getattr(s, "name", None) == "action":
        s = globals().get("action_text", s)
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)

def _event_has(eventcodes, code):
    pat = rf"(^|\|){code}(\||$)"
    return eventcodes.astype("string").str.contains(pat, regex=True, na=False).astype(float)

def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

# v001: event 11 density 252d
def gm_f106_biotech_f106_event_11_density_252d_v001_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "11"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v002: event 21_22 density 252d
def gm_f106_biotech_f106_event_21_22_density_252d_v002_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "21") + _event_has(eventcodes, "22"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v003: event 34_35 density 252d
def gm_f106_biotech_f106_event_34_35_density_252d_v003_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "34") + _event_has(eventcodes, "35"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v004: event 52_53 density 252d
def gm_f106_biotech_f106_event_52_53_density_252d_v004_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "52") + _event_has(eventcodes, "53"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v005: event 71 density 252d
def gm_f106_biotech_f106_event_71_density_252d_v005_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "71"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v006: event 81 density 252d
def gm_f106_biotech_f106_event_81_density_252d_v006_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "81"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v007: event 91 density 252d
def gm_f106_biotech_f106_event_91_density_252d_v007_signal(eventcodes):
    result = _sum(_event_has(eventcodes, "91"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v008: event code breadth
def gm_f106_biotech_f106_event_code_breadth_v008_signal(eventcodes):
    parts = eventcodes.astype("string").str.split("|")
    result = parts.map(lambda x: len([v for v in x if v and v != "<NA>"])).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)

# v009: event code breadth 252d mean
def gm_f106_biotech_f106_event_code_breadth_252d_mean_v009_signal(eventcodes):
    breadth = gm_f106_biotech_f106_event_code_breadth_v008_signal(eventcodes)
    result = _mean(breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v010: dividend action flag
def gm_f106_biotech_f106_dividend_action_flag_v010_signal(action):
    result = _contains(action, "^DIVIDEND$")
    return result.replace([np.inf, -np.inf], np.nan)

# v011: split action flag
def gm_f106_biotech_f106_split_action_flag_v011_signal(action):
    result = _contains(action, "SPLIT")
    return result.replace([np.inf, -np.inf], np.nan)

# v012: listed action flag
def gm_f106_biotech_f106_listed_action_flag_v012_signal(action):
    result = _contains(action, "^LISTED$|INITIATED")
    return result.replace([np.inf, -np.inf], np.nan)

# v013: delisted action flag
def gm_f106_biotech_f106_delisted_action_flag_v013_signal(action):
    result = _contains(action, "DELIST|BANKRUPTCY|LIQUIDATION")
    return result.replace([np.inf, -np.inf], np.nan)

# v014: ticker change action flag
def gm_f106_biotech_f106_ticker_change_action_flag_v014_signal(action):
    result = _contains(action, "TICKERCHANGE")
    return result.replace([np.inf, -np.inf], np.nan)

# v015: merger acquisition action flag
def gm_f106_biotech_f106_merger_acquisition_action_flag_v015_signal(action):
    result = _contains(action, "ACQUISITION|MERGER")
    return result.replace([np.inf, -np.inf], np.nan)

# v016: spinoff action flag
def gm_f106_biotech_f106_spinoff_action_flag_v016_signal(action):
    result = _contains(action, "SPINOFF")
    return result.replace([np.inf, -np.inf], np.nan)

# v017: distress action 252d
def gm_f106_biotech_f106_distress_action_252d_v017_signal(action):
    result = _sum(_contains(action, "DELIST|BANKRUPTCY|LIQUIDATION"), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v018: corporate change 252d
def gm_f106_biotech_f106_corporate_change_252d_v018_signal(action):
    change = (
        _contains(action, "SPLIT")
        + _contains(action, "TICKERCHANGE")
        + _contains(action, "ACQUISITION|MERGER")
        + _contains(action, "SPINOFF")
    )
    result = _sum(change, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v019: action value signed distress
def gm_f106_biotech_f106_action_value_signed_distress_v019_signal(action, value):
    result = _contains(action, "DELIST|BANKRUPTCY|LIQUIDATION") * value.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v020: action value signed split
def gm_f106_biotech_f106_action_value_signed_split_v020_signal(action, value):
    result = _contains(action, "SPLIT") * value
    return result.replace([np.inf, -np.inf], np.nan)

# v021: has contraticker
def gm_f106_biotech_f106_has_contraticker_v021_signal(contraticker):
    result = contraticker.notna().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)

# v022: has contraname
def gm_f106_biotech_f106_has_contraname_v022_signal(contraname):
    result = contraname.notna().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)

# v023: sp500 added
def gm_f106_biotech_f106_sp500_added_v023_signal(action, note):
    result = _contains(action, "ADD|ADDED") + _contains(note, "ADD|ADDED")
    return result.replace([np.inf, -np.inf], np.nan)

# v024: sp500 removed
def gm_f106_biotech_f106_sp500_removed_v024_signal(action, note):
    result = _contains(action, "REMOVE|REMOVED|DELETE|DELETED") + _contains(note, "REMOVE|REMOVED|DELETE|DELETED")
    return result.replace([np.inf, -np.inf], np.nan)

# v025: sp500 change 252d
def gm_f106_biotech_f106_sp500_change_252d_v025_signal(action, note):
    added = _contains(action, "ADD|ADDED") + _contains(note, "ADD|ADDED")
    removed = _contains(action, "REMOVE|REMOVED|DELETE|DELETED") + _contains(note, "REMOVE|REMOVED|DELETE|DELETED")
    result = _sum(added + removed, 252)
    return result.replace([np.inf, -np.inf], np.nan)
