"""Family f104 - Event and corporate-action categorical signals.

Sharadar tables: EVENTS, ACTIONS, SP500
Fields: eventcodes, action, value, contraticker, contraname, note.

Existing f098-f100 use generic action/event density. This family models the
source categorical codes directly so delistings, splits, ticker changes,
bankruptcy/liquidation, M&A, dividends, and index adds/removals are not reduced
to one undifferentiated count.
"""
import numpy as np


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _contains(s, pattern):
    if getattr(s, "name", None) == "action":
        s = globals().get("action_text", s)
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)


def _event_has(eventcodes, code):
    pat = rf"(^|\|){code}(\||$)"
    return eventcodes.astype("string").str.contains(pat, regex=True, na=False).astype(float)


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def eac_f104_event_11_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "11"), 252))


def eac_f104_event_21_22_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "21") + _event_has(eventcodes, "22"), 252))


def eac_f104_event_34_35_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "34") + _event_has(eventcodes, "35"), 252))


def eac_f104_event_52_53_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "52") + _event_has(eventcodes, "53"), 252))


def eac_f104_event_71_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "71"), 252))


def eac_f104_event_81_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "81"), 252))


def eac_f104_event_91_density_252d_signal(eventcodes):
    return _clean(_sum(_event_has(eventcodes, "91"), 252))


def eac_f104_event_code_breadth_signal(eventcodes):
    parts = eventcodes.astype("string").str.split("|")
    return _clean(parts.map(lambda x: len([v for v in x if v and v != "<NA>"])).astype(float))


def eac_f104_event_code_breadth_252d_mean_signal(eventcodes):
    return _clean(_mean(eac_f104_event_code_breadth_signal(eventcodes), 252))


def eac_f104_dividend_action_flag_signal(action):
    return _contains(action, "^DIVIDEND$")


def eac_f104_split_action_flag_signal(action):
    return _contains(action, "SPLIT")


def eac_f104_listed_action_flag_signal(action):
    return _contains(action, "^LISTED$|INITIATED")


def eac_f104_delisted_action_flag_signal(action):
    return _contains(action, "DELIST|BANKRUPTCY|LIQUIDATION")


def eac_f104_ticker_change_action_flag_signal(action):
    return _contains(action, "TICKERCHANGE")


def eac_f104_merger_acquisition_action_flag_signal(action):
    return _contains(action, "ACQUISITION|MERGER")


def eac_f104_spinoff_action_flag_signal(action):
    return _contains(action, "SPINOFF")


def eac_f104_distress_action_252d_signal(action):
    return _clean(_sum(eac_f104_delisted_action_flag_signal(action), 252))


def eac_f104_corporate_change_252d_signal(action):
    change = (
        eac_f104_split_action_flag_signal(action)
        + eac_f104_ticker_change_action_flag_signal(action)
        + eac_f104_merger_acquisition_action_flag_signal(action)
        + eac_f104_spinoff_action_flag_signal(action)
    )
    return _clean(_sum(change, 252))


def eac_f104_action_value_signed_distress_signal(action, value):
    return _clean(eac_f104_delisted_action_flag_signal(action) * value.abs())


def eac_f104_action_value_signed_split_signal(action, value):
    return _clean(eac_f104_split_action_flag_signal(action) * value)


def eac_f104_has_contraticker_signal(contraticker):
    return contraticker.notna().astype(float)


def eac_f104_has_contraname_signal(contraname):
    return contraname.notna().astype(float)


def eac_f104_sp500_added_signal(action, note):
    return _contains(action, "ADD|ADDED") + _contains(note, "ADD|ADDED")


def eac_f104_sp500_removed_signal(action, note):
    return _contains(action, "REMOVE|REMOVED|DELETE|DELETED") + _contains(note, "REMOVE|REMOVED|DELETE|DELETED")


def eac_f104_sp500_change_252d_signal(action, note):
    return _clean(_sum(eac_f104_sp500_added_signal(action, note) + eac_f104_sp500_removed_signal(action, note), 252))
