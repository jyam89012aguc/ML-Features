import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def evl_151_evl_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def evl_152_evl_007_interest_coverage_stress_252_roc_42(evl_007_interest_coverage_stress_252):
    feature = _s(evl_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def evl_153_evl_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def evl_154_evl_019_interest_coverage_stress_84_roc_378(evl_019_interest_coverage_stress_84):
    feature = _s(evl_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def evl_155_evl_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















EARNINGS_VOLATILITY_REGISTRY_2ND_DERIVATIVES = {
    'evl_151_evl_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': evl_151_evl_001_netinc_decline_1_roc_1},
    'evl_152_evl_007_interest_coverage_stress_252_roc_42': {'inputs': ['evl_007_interest_coverage_stress_252'], 'func': evl_152_evl_007_interest_coverage_stress_252_roc_42},
    'evl_153_evl_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': evl_153_evl_013_netinc_decline_1_roc_126},
    'evl_154_evl_019_interest_coverage_stress_84_roc_378': {'inputs': ['evl_019_interest_coverage_stress_84'], 'func': evl_154_evl_019_interest_coverage_stress_84_roc_378},
    'evl_155_evl_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': evl_155_evl_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ev_replacement_d2_001(ev_replacement_001):
    feature = _clean(ev_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_001'] = {'inputs': ['ev_replacement_001'], 'func': ev_replacement_d2_001}


def ev_replacement_d2_002(ev_replacement_002):
    feature = _clean(ev_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_002'] = {'inputs': ['ev_replacement_002'], 'func': ev_replacement_d2_002}


def ev_replacement_d2_003(ev_replacement_003):
    feature = _clean(ev_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_003'] = {'inputs': ['ev_replacement_003'], 'func': ev_replacement_d2_003}


def ev_replacement_d2_004(ev_replacement_004):
    feature = _clean(ev_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_004'] = {'inputs': ['ev_replacement_004'], 'func': ev_replacement_d2_004}


def ev_replacement_d2_005(ev_replacement_005):
    feature = _clean(ev_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_005'] = {'inputs': ['ev_replacement_005'], 'func': ev_replacement_d2_005}


def ev_replacement_d2_006(ev_replacement_006):
    feature = _clean(ev_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_006'] = {'inputs': ['ev_replacement_006'], 'func': ev_replacement_d2_006}


def ev_replacement_d2_007(ev_replacement_007):
    feature = _clean(ev_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_007'] = {'inputs': ['ev_replacement_007'], 'func': ev_replacement_d2_007}


def ev_replacement_d2_008(ev_replacement_008):
    feature = _clean(ev_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_008'] = {'inputs': ['ev_replacement_008'], 'func': ev_replacement_d2_008}


def ev_replacement_d2_009(ev_replacement_009):
    feature = _clean(ev_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_009'] = {'inputs': ['ev_replacement_009'], 'func': ev_replacement_d2_009}


def ev_replacement_d2_010(ev_replacement_010):
    feature = _clean(ev_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_010'] = {'inputs': ['ev_replacement_010'], 'func': ev_replacement_d2_010}


def ev_replacement_d2_011(ev_replacement_011):
    feature = _clean(ev_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_011'] = {'inputs': ['ev_replacement_011'], 'func': ev_replacement_d2_011}


def ev_replacement_d2_012(ev_replacement_012):
    feature = _clean(ev_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_012'] = {'inputs': ['ev_replacement_012'], 'func': ev_replacement_d2_012}


def ev_replacement_d2_013(ev_replacement_013):
    feature = _clean(ev_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_013'] = {'inputs': ['ev_replacement_013'], 'func': ev_replacement_d2_013}


def ev_replacement_d2_014(ev_replacement_014):
    feature = _clean(ev_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_014'] = {'inputs': ['ev_replacement_014'], 'func': ev_replacement_d2_014}


def ev_replacement_d2_015(ev_replacement_015):
    feature = _clean(ev_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_015'] = {'inputs': ['ev_replacement_015'], 'func': ev_replacement_d2_015}


def ev_replacement_d2_016(ev_replacement_016):
    feature = _clean(ev_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_016'] = {'inputs': ['ev_replacement_016'], 'func': ev_replacement_d2_016}


def ev_replacement_d2_017(ev_replacement_017):
    feature = _clean(ev_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_017'] = {'inputs': ['ev_replacement_017'], 'func': ev_replacement_d2_017}


def ev_replacement_d2_018(ev_replacement_018):
    feature = _clean(ev_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_018'] = {'inputs': ['ev_replacement_018'], 'func': ev_replacement_d2_018}


def ev_replacement_d2_019(ev_replacement_019):
    feature = _clean(ev_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_019'] = {'inputs': ['ev_replacement_019'], 'func': ev_replacement_d2_019}


def ev_replacement_d2_020(ev_replacement_020):
    feature = _clean(ev_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_020'] = {'inputs': ['ev_replacement_020'], 'func': ev_replacement_d2_020}


def ev_replacement_d2_021(ev_replacement_021):
    feature = _clean(ev_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_021'] = {'inputs': ['ev_replacement_021'], 'func': ev_replacement_d2_021}


def ev_replacement_d2_022(ev_replacement_022):
    feature = _clean(ev_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_022'] = {'inputs': ['ev_replacement_022'], 'func': ev_replacement_d2_022}


def ev_replacement_d2_023(ev_replacement_023):
    feature = _clean(ev_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_023'] = {'inputs': ['ev_replacement_023'], 'func': ev_replacement_d2_023}


def ev_replacement_d2_024(ev_replacement_024):
    feature = _clean(ev_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_024'] = {'inputs': ['ev_replacement_024'], 'func': ev_replacement_d2_024}


def ev_replacement_d2_025(ev_replacement_025):
    feature = _clean(ev_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_025'] = {'inputs': ['ev_replacement_025'], 'func': ev_replacement_d2_025}


def ev_replacement_d2_026(ev_replacement_026):
    feature = _clean(ev_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_026'] = {'inputs': ['ev_replacement_026'], 'func': ev_replacement_d2_026}


def ev_replacement_d2_027(ev_replacement_027):
    feature = _clean(ev_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_027'] = {'inputs': ['ev_replacement_027'], 'func': ev_replacement_d2_027}


def ev_replacement_d2_028(ev_replacement_028):
    feature = _clean(ev_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_028'] = {'inputs': ['ev_replacement_028'], 'func': ev_replacement_d2_028}


def ev_replacement_d2_029(ev_replacement_029):
    feature = _clean(ev_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_029'] = {'inputs': ['ev_replacement_029'], 'func': ev_replacement_d2_029}


def ev_replacement_d2_030(ev_replacement_030):
    feature = _clean(ev_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_030'] = {'inputs': ['ev_replacement_030'], 'func': ev_replacement_d2_030}


def ev_replacement_d2_031(ev_replacement_031):
    feature = _clean(ev_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_031'] = {'inputs': ['ev_replacement_031'], 'func': ev_replacement_d2_031}


def ev_replacement_d2_032(ev_replacement_032):
    feature = _clean(ev_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_032'] = {'inputs': ['ev_replacement_032'], 'func': ev_replacement_d2_032}


def ev_replacement_d2_033(ev_replacement_033):
    feature = _clean(ev_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_033'] = {'inputs': ['ev_replacement_033'], 'func': ev_replacement_d2_033}


def ev_replacement_d2_034(ev_replacement_034):
    feature = _clean(ev_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_034'] = {'inputs': ['ev_replacement_034'], 'func': ev_replacement_d2_034}


def ev_replacement_d2_035(ev_replacement_035):
    feature = _clean(ev_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_035'] = {'inputs': ['ev_replacement_035'], 'func': ev_replacement_d2_035}


def ev_replacement_d2_036(ev_replacement_036):
    feature = _clean(ev_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_036'] = {'inputs': ['ev_replacement_036'], 'func': ev_replacement_d2_036}


def ev_replacement_d2_037(ev_replacement_037):
    feature = _clean(ev_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_037'] = {'inputs': ['ev_replacement_037'], 'func': ev_replacement_d2_037}


def ev_replacement_d2_038(ev_replacement_038):
    feature = _clean(ev_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_038'] = {'inputs': ['ev_replacement_038'], 'func': ev_replacement_d2_038}


def ev_replacement_d2_039(ev_replacement_039):
    feature = _clean(ev_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_039'] = {'inputs': ['ev_replacement_039'], 'func': ev_replacement_d2_039}


def ev_replacement_d2_040(ev_replacement_040):
    feature = _clean(ev_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_040'] = {'inputs': ['ev_replacement_040'], 'func': ev_replacement_d2_040}


def ev_replacement_d2_041(ev_replacement_041):
    feature = _clean(ev_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_041'] = {'inputs': ['ev_replacement_041'], 'func': ev_replacement_d2_041}


def ev_replacement_d2_042(ev_replacement_042):
    feature = _clean(ev_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_042'] = {'inputs': ['ev_replacement_042'], 'func': ev_replacement_d2_042}


def ev_replacement_d2_043(ev_replacement_043):
    feature = _clean(ev_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_043'] = {'inputs': ['ev_replacement_043'], 'func': ev_replacement_d2_043}


def ev_replacement_d2_044(ev_replacement_044):
    feature = _clean(ev_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_044'] = {'inputs': ['ev_replacement_044'], 'func': ev_replacement_d2_044}


def ev_replacement_d2_045(ev_replacement_045):
    feature = _clean(ev_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_045'] = {'inputs': ['ev_replacement_045'], 'func': ev_replacement_d2_045}


def ev_replacement_d2_046(ev_replacement_046):
    feature = _clean(ev_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_046'] = {'inputs': ['ev_replacement_046'], 'func': ev_replacement_d2_046}


def ev_replacement_d2_047(ev_replacement_047):
    feature = _clean(ev_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_047'] = {'inputs': ['ev_replacement_047'], 'func': ev_replacement_d2_047}


def ev_replacement_d2_048(ev_replacement_048):
    feature = _clean(ev_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_048'] = {'inputs': ['ev_replacement_048'], 'func': ev_replacement_d2_048}


def ev_replacement_d2_049(ev_replacement_049):
    feature = _clean(ev_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_049'] = {'inputs': ['ev_replacement_049'], 'func': ev_replacement_d2_049}


def ev_replacement_d2_050(ev_replacement_050):
    feature = _clean(ev_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_050'] = {'inputs': ['ev_replacement_050'], 'func': ev_replacement_d2_050}


def ev_replacement_d2_051(ev_replacement_051):
    feature = _clean(ev_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_051'] = {'inputs': ['ev_replacement_051'], 'func': ev_replacement_d2_051}


def ev_replacement_d2_052(ev_replacement_052):
    feature = _clean(ev_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_052'] = {'inputs': ['ev_replacement_052'], 'func': ev_replacement_d2_052}


def ev_replacement_d2_053(ev_replacement_053):
    feature = _clean(ev_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_053'] = {'inputs': ['ev_replacement_053'], 'func': ev_replacement_d2_053}


def ev_replacement_d2_054(ev_replacement_054):
    feature = _clean(ev_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_054'] = {'inputs': ['ev_replacement_054'], 'func': ev_replacement_d2_054}


def ev_replacement_d2_055(ev_replacement_055):
    feature = _clean(ev_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_055'] = {'inputs': ['ev_replacement_055'], 'func': ev_replacement_d2_055}


def ev_replacement_d2_056(ev_replacement_056):
    feature = _clean(ev_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_056'] = {'inputs': ['ev_replacement_056'], 'func': ev_replacement_d2_056}


def ev_replacement_d2_057(ev_replacement_057):
    feature = _clean(ev_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_057'] = {'inputs': ['ev_replacement_057'], 'func': ev_replacement_d2_057}


def ev_replacement_d2_058(ev_replacement_058):
    feature = _clean(ev_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_058'] = {'inputs': ['ev_replacement_058'], 'func': ev_replacement_d2_058}


def ev_replacement_d2_059(ev_replacement_059):
    feature = _clean(ev_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_059'] = {'inputs': ['ev_replacement_059'], 'func': ev_replacement_d2_059}


def ev_replacement_d2_060(ev_replacement_060):
    feature = _clean(ev_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_060'] = {'inputs': ['ev_replacement_060'], 'func': ev_replacement_d2_060}


def ev_replacement_d2_061(ev_replacement_061):
    feature = _clean(ev_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_061'] = {'inputs': ['ev_replacement_061'], 'func': ev_replacement_d2_061}


def ev_replacement_d2_062(ev_replacement_062):
    feature = _clean(ev_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_062'] = {'inputs': ['ev_replacement_062'], 'func': ev_replacement_d2_062}


def ev_replacement_d2_063(ev_replacement_063):
    feature = _clean(ev_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_063'] = {'inputs': ['ev_replacement_063'], 'func': ev_replacement_d2_063}


def ev_replacement_d2_064(ev_replacement_064):
    feature = _clean(ev_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_064'] = {'inputs': ['ev_replacement_064'], 'func': ev_replacement_d2_064}


def ev_replacement_d2_065(ev_replacement_065):
    feature = _clean(ev_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_065'] = {'inputs': ['ev_replacement_065'], 'func': ev_replacement_d2_065}


def ev_replacement_d2_066(ev_replacement_066):
    feature = _clean(ev_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_066'] = {'inputs': ['ev_replacement_066'], 'func': ev_replacement_d2_066}


def ev_replacement_d2_067(ev_replacement_067):
    feature = _clean(ev_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_067'] = {'inputs': ['ev_replacement_067'], 'func': ev_replacement_d2_067}


def ev_replacement_d2_068(ev_replacement_068):
    feature = _clean(ev_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_068'] = {'inputs': ['ev_replacement_068'], 'func': ev_replacement_d2_068}


def ev_replacement_d2_069(ev_replacement_069):
    feature = _clean(ev_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_069'] = {'inputs': ['ev_replacement_069'], 'func': ev_replacement_d2_069}


def ev_replacement_d2_070(ev_replacement_070):
    feature = _clean(ev_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_070'] = {'inputs': ['ev_replacement_070'], 'func': ev_replacement_d2_070}


def ev_replacement_d2_071(ev_replacement_071):
    feature = _clean(ev_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_071'] = {'inputs': ['ev_replacement_071'], 'func': ev_replacement_d2_071}


def ev_replacement_d2_072(ev_replacement_072):
    feature = _clean(ev_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_072'] = {'inputs': ['ev_replacement_072'], 'func': ev_replacement_d2_072}


def ev_replacement_d2_073(ev_replacement_073):
    feature = _clean(ev_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_073'] = {'inputs': ['ev_replacement_073'], 'func': ev_replacement_d2_073}


def ev_replacement_d2_074(ev_replacement_074):
    feature = _clean(ev_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_074'] = {'inputs': ['ev_replacement_074'], 'func': ev_replacement_d2_074}


def ev_replacement_d2_075(ev_replacement_075):
    feature = _clean(ev_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_075'] = {'inputs': ['ev_replacement_075'], 'func': ev_replacement_d2_075}


def ev_replacement_d2_076(ev_replacement_076):
    feature = _clean(ev_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_076'] = {'inputs': ['ev_replacement_076'], 'func': ev_replacement_d2_076}


def ev_replacement_d2_077(ev_replacement_077):
    feature = _clean(ev_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_077'] = {'inputs': ['ev_replacement_077'], 'func': ev_replacement_d2_077}


def ev_replacement_d2_078(ev_replacement_078):
    feature = _clean(ev_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_078'] = {'inputs': ['ev_replacement_078'], 'func': ev_replacement_d2_078}


def ev_replacement_d2_079(ev_replacement_079):
    feature = _clean(ev_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_079'] = {'inputs': ['ev_replacement_079'], 'func': ev_replacement_d2_079}


def ev_replacement_d2_080(ev_replacement_080):
    feature = _clean(ev_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_080'] = {'inputs': ['ev_replacement_080'], 'func': ev_replacement_d2_080}


def ev_replacement_d2_081(ev_replacement_081):
    feature = _clean(ev_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_081'] = {'inputs': ['ev_replacement_081'], 'func': ev_replacement_d2_081}


def ev_replacement_d2_082(ev_replacement_082):
    feature = _clean(ev_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_082'] = {'inputs': ['ev_replacement_082'], 'func': ev_replacement_d2_082}


def ev_replacement_d2_083(ev_replacement_083):
    feature = _clean(ev_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_083'] = {'inputs': ['ev_replacement_083'], 'func': ev_replacement_d2_083}


def ev_replacement_d2_084(ev_replacement_084):
    feature = _clean(ev_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_084'] = {'inputs': ['ev_replacement_084'], 'func': ev_replacement_d2_084}


def ev_replacement_d2_085(ev_replacement_085):
    feature = _clean(ev_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_085'] = {'inputs': ['ev_replacement_085'], 'func': ev_replacement_d2_085}


def ev_replacement_d2_086(ev_replacement_086):
    feature = _clean(ev_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_086'] = {'inputs': ['ev_replacement_086'], 'func': ev_replacement_d2_086}


def ev_replacement_d2_087(ev_replacement_087):
    feature = _clean(ev_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_087'] = {'inputs': ['ev_replacement_087'], 'func': ev_replacement_d2_087}


def ev_replacement_d2_088(ev_replacement_088):
    feature = _clean(ev_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_088'] = {'inputs': ['ev_replacement_088'], 'func': ev_replacement_d2_088}


def ev_replacement_d2_089(ev_replacement_089):
    feature = _clean(ev_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_089'] = {'inputs': ['ev_replacement_089'], 'func': ev_replacement_d2_089}


def ev_replacement_d2_090(ev_replacement_090):
    feature = _clean(ev_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_090'] = {'inputs': ['ev_replacement_090'], 'func': ev_replacement_d2_090}


def ev_replacement_d2_091(ev_replacement_091):
    feature = _clean(ev_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_091'] = {'inputs': ['ev_replacement_091'], 'func': ev_replacement_d2_091}


def ev_replacement_d2_092(ev_replacement_092):
    feature = _clean(ev_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_092'] = {'inputs': ['ev_replacement_092'], 'func': ev_replacement_d2_092}


def ev_replacement_d2_093(ev_replacement_093):
    feature = _clean(ev_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_093'] = {'inputs': ['ev_replacement_093'], 'func': ev_replacement_d2_093}


def ev_replacement_d2_094(ev_replacement_094):
    feature = _clean(ev_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_094'] = {'inputs': ['ev_replacement_094'], 'func': ev_replacement_d2_094}


def ev_replacement_d2_095(ev_replacement_095):
    feature = _clean(ev_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_095'] = {'inputs': ['ev_replacement_095'], 'func': ev_replacement_d2_095}


def ev_replacement_d2_096(ev_replacement_096):
    feature = _clean(ev_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_096'] = {'inputs': ['ev_replacement_096'], 'func': ev_replacement_d2_096}


def ev_replacement_d2_097(ev_replacement_097):
    feature = _clean(ev_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_097'] = {'inputs': ['ev_replacement_097'], 'func': ev_replacement_d2_097}


def ev_replacement_d2_098(ev_replacement_098):
    feature = _clean(ev_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_098'] = {'inputs': ['ev_replacement_098'], 'func': ev_replacement_d2_098}


def ev_replacement_d2_099(ev_replacement_099):
    feature = _clean(ev_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_099'] = {'inputs': ['ev_replacement_099'], 'func': ev_replacement_d2_099}


def ev_replacement_d2_100(ev_replacement_100):
    feature = _clean(ev_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_100'] = {'inputs': ['ev_replacement_100'], 'func': ev_replacement_d2_100}


def ev_replacement_d2_101(ev_replacement_101):
    feature = _clean(ev_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_101'] = {'inputs': ['ev_replacement_101'], 'func': ev_replacement_d2_101}


def ev_replacement_d2_102(ev_replacement_102):
    feature = _clean(ev_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_102'] = {'inputs': ['ev_replacement_102'], 'func': ev_replacement_d2_102}


def ev_replacement_d2_103(ev_replacement_103):
    feature = _clean(ev_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_103'] = {'inputs': ['ev_replacement_103'], 'func': ev_replacement_d2_103}


def ev_replacement_d2_104(ev_replacement_104):
    feature = _clean(ev_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_104'] = {'inputs': ['ev_replacement_104'], 'func': ev_replacement_d2_104}


def ev_replacement_d2_105(ev_replacement_105):
    feature = _clean(ev_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_105'] = {'inputs': ['ev_replacement_105'], 'func': ev_replacement_d2_105}


def ev_replacement_d2_106(ev_replacement_106):
    feature = _clean(ev_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_106'] = {'inputs': ['ev_replacement_106'], 'func': ev_replacement_d2_106}


def ev_replacement_d2_107(ev_replacement_107):
    feature = _clean(ev_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_107'] = {'inputs': ['ev_replacement_107'], 'func': ev_replacement_d2_107}


def ev_replacement_d2_108(ev_replacement_108):
    feature = _clean(ev_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_108'] = {'inputs': ['ev_replacement_108'], 'func': ev_replacement_d2_108}


def ev_replacement_d2_109(ev_replacement_109):
    feature = _clean(ev_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_109'] = {'inputs': ['ev_replacement_109'], 'func': ev_replacement_d2_109}


def ev_replacement_d2_110(ev_replacement_110):
    feature = _clean(ev_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_110'] = {'inputs': ['ev_replacement_110'], 'func': ev_replacement_d2_110}


def ev_replacement_d2_111(ev_replacement_111):
    feature = _clean(ev_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_111'] = {'inputs': ['ev_replacement_111'], 'func': ev_replacement_d2_111}


def ev_replacement_d2_112(ev_replacement_112):
    feature = _clean(ev_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_112'] = {'inputs': ['ev_replacement_112'], 'func': ev_replacement_d2_112}


def ev_replacement_d2_113(ev_replacement_113):
    feature = _clean(ev_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_113'] = {'inputs': ['ev_replacement_113'], 'func': ev_replacement_d2_113}


def ev_replacement_d2_114(ev_replacement_114):
    feature = _clean(ev_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_114'] = {'inputs': ['ev_replacement_114'], 'func': ev_replacement_d2_114}


def ev_replacement_d2_115(ev_replacement_115):
    feature = _clean(ev_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_115'] = {'inputs': ['ev_replacement_115'], 'func': ev_replacement_d2_115}


def ev_replacement_d2_116(ev_replacement_116):
    feature = _clean(ev_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_116'] = {'inputs': ['ev_replacement_116'], 'func': ev_replacement_d2_116}


def ev_replacement_d2_117(ev_replacement_117):
    feature = _clean(ev_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_117'] = {'inputs': ['ev_replacement_117'], 'func': ev_replacement_d2_117}


def ev_replacement_d2_118(ev_replacement_118):
    feature = _clean(ev_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_118'] = {'inputs': ['ev_replacement_118'], 'func': ev_replacement_d2_118}


def ev_replacement_d2_119(ev_replacement_119):
    feature = _clean(ev_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_119'] = {'inputs': ['ev_replacement_119'], 'func': ev_replacement_d2_119}


def ev_replacement_d2_120(ev_replacement_120):
    feature = _clean(ev_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_120'] = {'inputs': ['ev_replacement_120'], 'func': ev_replacement_d2_120}


def ev_replacement_d2_121(ev_replacement_121):
    feature = _clean(ev_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_121'] = {'inputs': ['ev_replacement_121'], 'func': ev_replacement_d2_121}


def ev_replacement_d2_122(ev_replacement_122):
    feature = _clean(ev_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_122'] = {'inputs': ['ev_replacement_122'], 'func': ev_replacement_d2_122}


def ev_replacement_d2_123(ev_replacement_123):
    feature = _clean(ev_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_123'] = {'inputs': ['ev_replacement_123'], 'func': ev_replacement_d2_123}


def ev_replacement_d2_124(ev_replacement_124):
    feature = _clean(ev_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_124'] = {'inputs': ['ev_replacement_124'], 'func': ev_replacement_d2_124}


def ev_replacement_d2_125(ev_replacement_125):
    feature = _clean(ev_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_125'] = {'inputs': ['ev_replacement_125'], 'func': ev_replacement_d2_125}


def ev_replacement_d2_126(ev_replacement_126):
    feature = _clean(ev_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_126'] = {'inputs': ['ev_replacement_126'], 'func': ev_replacement_d2_126}


def ev_replacement_d2_127(ev_replacement_127):
    feature = _clean(ev_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_127'] = {'inputs': ['ev_replacement_127'], 'func': ev_replacement_d2_127}


def ev_replacement_d2_128(ev_replacement_128):
    feature = _clean(ev_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_128'] = {'inputs': ['ev_replacement_128'], 'func': ev_replacement_d2_128}


def ev_replacement_d2_129(ev_replacement_129):
    feature = _clean(ev_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_129'] = {'inputs': ['ev_replacement_129'], 'func': ev_replacement_d2_129}


def ev_replacement_d2_130(ev_replacement_130):
    feature = _clean(ev_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_130'] = {'inputs': ['ev_replacement_130'], 'func': ev_replacement_d2_130}


def ev_replacement_d2_131(ev_replacement_131):
    feature = _clean(ev_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_131'] = {'inputs': ['ev_replacement_131'], 'func': ev_replacement_d2_131}


def ev_replacement_d2_132(ev_replacement_132):
    feature = _clean(ev_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_132'] = {'inputs': ['ev_replacement_132'], 'func': ev_replacement_d2_132}


def ev_replacement_d2_133(ev_replacement_133):
    feature = _clean(ev_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_133'] = {'inputs': ['ev_replacement_133'], 'func': ev_replacement_d2_133}


def ev_replacement_d2_134(ev_replacement_134):
    feature = _clean(ev_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_134'] = {'inputs': ['ev_replacement_134'], 'func': ev_replacement_d2_134}


def ev_replacement_d2_135(ev_replacement_135):
    feature = _clean(ev_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_135'] = {'inputs': ['ev_replacement_135'], 'func': ev_replacement_d2_135}


def ev_replacement_d2_136(ev_replacement_136):
    feature = _clean(ev_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_136'] = {'inputs': ['ev_replacement_136'], 'func': ev_replacement_d2_136}


def ev_replacement_d2_137(ev_replacement_137):
    feature = _clean(ev_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_137'] = {'inputs': ['ev_replacement_137'], 'func': ev_replacement_d2_137}


def ev_replacement_d2_138(ev_replacement_138):
    feature = _clean(ev_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_138'] = {'inputs': ['ev_replacement_138'], 'func': ev_replacement_d2_138}


def ev_replacement_d2_139(ev_replacement_139):
    feature = _clean(ev_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_139'] = {'inputs': ['ev_replacement_139'], 'func': ev_replacement_d2_139}


def ev_replacement_d2_140(ev_replacement_140):
    feature = _clean(ev_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_140'] = {'inputs': ['ev_replacement_140'], 'func': ev_replacement_d2_140}


def ev_replacement_d2_141(ev_replacement_141):
    feature = _clean(ev_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_141'] = {'inputs': ['ev_replacement_141'], 'func': ev_replacement_d2_141}


def ev_replacement_d2_142(ev_replacement_142):
    feature = _clean(ev_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_142'] = {'inputs': ['ev_replacement_142'], 'func': ev_replacement_d2_142}


def ev_replacement_d2_143(ev_replacement_143):
    feature = _clean(ev_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_143'] = {'inputs': ['ev_replacement_143'], 'func': ev_replacement_d2_143}


def ev_replacement_d2_144(ev_replacement_144):
    feature = _clean(ev_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_144'] = {'inputs': ['ev_replacement_144'], 'func': ev_replacement_d2_144}


def ev_replacement_d2_145(ev_replacement_145):
    feature = _clean(ev_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_145'] = {'inputs': ['ev_replacement_145'], 'func': ev_replacement_d2_145}


def ev_replacement_d2_146(ev_replacement_146):
    feature = _clean(ev_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_146'] = {'inputs': ['ev_replacement_146'], 'func': ev_replacement_d2_146}


def ev_replacement_d2_147(ev_replacement_147):
    feature = _clean(ev_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_147'] = {'inputs': ['ev_replacement_147'], 'func': ev_replacement_d2_147}


def ev_replacement_d2_148(ev_replacement_148):
    feature = _clean(ev_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_148'] = {'inputs': ['ev_replacement_148'], 'func': ev_replacement_d2_148}


def ev_replacement_d2_149(ev_replacement_149):
    feature = _clean(ev_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_149'] = {'inputs': ['ev_replacement_149'], 'func': ev_replacement_d2_149}


def ev_replacement_d2_150(ev_replacement_150):
    feature = _clean(ev_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_150'] = {'inputs': ['ev_replacement_150'], 'func': ev_replacement_d2_150}


def ev_replacement_d2_151(ev_replacement_151):
    feature = _clean(ev_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_151'] = {'inputs': ['ev_replacement_151'], 'func': ev_replacement_d2_151}


def ev_replacement_d2_152(ev_replacement_152):
    feature = _clean(ev_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_152'] = {'inputs': ['ev_replacement_152'], 'func': ev_replacement_d2_152}


def ev_replacement_d2_153(ev_replacement_153):
    feature = _clean(ev_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_153'] = {'inputs': ['ev_replacement_153'], 'func': ev_replacement_d2_153}


def ev_replacement_d2_154(ev_replacement_154):
    feature = _clean(ev_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_154'] = {'inputs': ['ev_replacement_154'], 'func': ev_replacement_d2_154}


def ev_replacement_d2_155(ev_replacement_155):
    feature = _clean(ev_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_155'] = {'inputs': ['ev_replacement_155'], 'func': ev_replacement_d2_155}


def ev_replacement_d2_156(ev_replacement_156):
    feature = _clean(ev_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_156'] = {'inputs': ['ev_replacement_156'], 'func': ev_replacement_d2_156}


def ev_replacement_d2_157(ev_replacement_157):
    feature = _clean(ev_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_157'] = {'inputs': ['ev_replacement_157'], 'func': ev_replacement_d2_157}


def ev_replacement_d2_158(ev_replacement_158):
    feature = _clean(ev_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_158'] = {'inputs': ['ev_replacement_158'], 'func': ev_replacement_d2_158}


def ev_replacement_d2_159(ev_replacement_159):
    feature = _clean(ev_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_159'] = {'inputs': ['ev_replacement_159'], 'func': ev_replacement_d2_159}


def ev_replacement_d2_160(ev_replacement_160):
    feature = _clean(ev_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_160'] = {'inputs': ['ev_replacement_160'], 'func': ev_replacement_d2_160}


def ev_replacement_d2_161(ev_replacement_161):
    feature = _clean(ev_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_161'] = {'inputs': ['ev_replacement_161'], 'func': ev_replacement_d2_161}


def ev_replacement_d2_162(ev_replacement_162):
    feature = _clean(ev_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_162'] = {'inputs': ['ev_replacement_162'], 'func': ev_replacement_d2_162}


def ev_replacement_d2_163(ev_replacement_163):
    feature = _clean(ev_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_163'] = {'inputs': ['ev_replacement_163'], 'func': ev_replacement_d2_163}


def ev_replacement_d2_164(ev_replacement_164):
    feature = _clean(ev_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_164'] = {'inputs': ['ev_replacement_164'], 'func': ev_replacement_d2_164}


def ev_replacement_d2_165(ev_replacement_165):
    feature = _clean(ev_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_165'] = {'inputs': ['ev_replacement_165'], 'func': ev_replacement_d2_165}


def ev_replacement_d2_166(ev_replacement_166):
    feature = _clean(ev_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
EV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ev_replacement_d2_166'] = {'inputs': ['ev_replacement_166'], 'func': ev_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63(evl_003_fcf_burn_to_cash_63):
    return _base_universe_d2(evl_003_fcf_burn_to_cash_63, 1)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63'] = {'inputs': ['evl_003_fcf_burn_to_cash_63'], 'func': evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63}


def evl_base_universe_d2_002_evl_004_debt_to_equity_84(evl_004_debt_to_equity_84):
    return _base_universe_d2(evl_004_debt_to_equity_84, 2)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_002_evl_004_debt_to_equity_84'] = {'inputs': ['evl_004_debt_to_equity_84'], 'func': evl_base_universe_d2_002_evl_004_debt_to_equity_84}


def evl_base_universe_d2_003_evl_005_debt_to_assets_126(evl_005_debt_to_assets_126):
    return _base_universe_d2(evl_005_debt_to_assets_126, 3)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_003_evl_005_debt_to_assets_126'] = {'inputs': ['evl_005_debt_to_assets_126'], 'func': evl_base_universe_d2_003_evl_005_debt_to_assets_126}


def evl_base_universe_d2_004_evl_012_accrual_gap_1260(evl_012_accrual_gap_1260):
    return _base_universe_d2(evl_012_accrual_gap_1260, 4)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_004_evl_012_accrual_gap_1260'] = {'inputs': ['evl_012_accrual_gap_1260'], 'func': evl_base_universe_d2_004_evl_012_accrual_gap_1260}


def evl_base_universe_d2_005_evl_016_debt_to_equity_21(evl_016_debt_to_equity_21):
    return _base_universe_d2(evl_016_debt_to_equity_21, 5)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_005_evl_016_debt_to_equity_21'] = {'inputs': ['evl_016_debt_to_equity_21'], 'func': evl_base_universe_d2_005_evl_016_debt_to_equity_21}


def evl_base_universe_d2_006_evl_017_debt_to_assets_42(evl_017_debt_to_assets_42):
    return _base_universe_d2(evl_017_debt_to_assets_42, 6)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_006_evl_017_debt_to_assets_42'] = {'inputs': ['evl_017_debt_to_assets_42'], 'func': evl_base_universe_d2_006_evl_017_debt_to_assets_42}


def evl_base_universe_d2_007_evl_024_accrual_gap_504(evl_024_accrual_gap_504):
    return _base_universe_d2(evl_024_accrual_gap_504, 7)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_007_evl_024_accrual_gap_504'] = {'inputs': ['evl_024_accrual_gap_504'], 'func': evl_base_universe_d2_007_evl_024_accrual_gap_504}


def evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260(evl_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(evl_027_fcf_burn_to_cash_1260, 8)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260'] = {'inputs': ['evl_027_fcf_burn_to_cash_1260'], 'func': evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260}


def evl_base_universe_d2_009_evl_028_debt_to_equity_1512(evl_028_debt_to_equity_1512):
    return _base_universe_d2(evl_028_debt_to_equity_1512, 9)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_009_evl_028_debt_to_equity_1512'] = {'inputs': ['evl_028_debt_to_equity_1512'], 'func': evl_base_universe_d2_009_evl_028_debt_to_equity_1512}


def evl_base_universe_d2_010_evl_029_debt_to_assets_63(evl_029_debt_to_assets_63):
    return _base_universe_d2(evl_029_debt_to_assets_63, 10)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_010_evl_029_debt_to_assets_63'] = {'inputs': ['evl_029_debt_to_assets_63'], 'func': evl_base_universe_d2_010_evl_029_debt_to_assets_63}


def evl_base_universe_d2_011_evl_031_interest_coverage_stress_21(evl_031_interest_coverage_stress_21):
    return _base_universe_d2(evl_031_interest_coverage_stress_21, 11)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_011_evl_031_interest_coverage_stress_21'] = {'inputs': ['evl_031_interest_coverage_stress_21'], 'func': evl_base_universe_d2_011_evl_031_interest_coverage_stress_21}


def evl_base_universe_d2_012_evl_036_accrual_gap_189(evl_036_accrual_gap_189):
    return _base_universe_d2(evl_036_accrual_gap_189, 12)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_012_evl_036_accrual_gap_189'] = {'inputs': ['evl_036_accrual_gap_189'], 'func': evl_base_universe_d2_012_evl_036_accrual_gap_189}


def evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504(evl_039_fcf_burn_to_cash_504):
    return _base_universe_d2(evl_039_fcf_burn_to_cash_504, 13)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504'] = {'inputs': ['evl_039_fcf_burn_to_cash_504'], 'func': evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504}


def evl_base_universe_d2_014_evl_040_debt_to_equity_756(evl_040_debt_to_equity_756):
    return _base_universe_d2(evl_040_debt_to_equity_756, 14)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_014_evl_040_debt_to_equity_756'] = {'inputs': ['evl_040_debt_to_equity_756'], 'func': evl_base_universe_d2_014_evl_040_debt_to_equity_756}


def evl_base_universe_d2_015_evl_041_debt_to_assets_1008(evl_041_debt_to_assets_1008):
    return _base_universe_d2(evl_041_debt_to_assets_1008, 15)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_015_evl_041_debt_to_assets_1008'] = {'inputs': ['evl_041_debt_to_assets_1008'], 'func': evl_base_universe_d2_015_evl_041_debt_to_assets_1008}


def evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512(evl_043_interest_coverage_stress_1512):
    return _base_universe_d2(evl_043_interest_coverage_stress_1512, 16)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512'] = {'inputs': ['evl_043_interest_coverage_stress_1512'], 'func': evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512}


def evl_base_universe_d2_017_evl_048_accrual_gap_63(evl_048_accrual_gap_63):
    return _base_universe_d2(evl_048_accrual_gap_63, 17)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_017_evl_048_accrual_gap_63'] = {'inputs': ['evl_048_accrual_gap_63'], 'func': evl_base_universe_d2_017_evl_048_accrual_gap_63}


def evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189(evl_051_fcf_burn_to_cash_189):
    return _base_universe_d2(evl_051_fcf_burn_to_cash_189, 18)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189'] = {'inputs': ['evl_051_fcf_burn_to_cash_189'], 'func': evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189}


def evl_base_universe_d2_019_evl_052_debt_to_equity_252(evl_052_debt_to_equity_252):
    return _base_universe_d2(evl_052_debt_to_equity_252, 19)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_019_evl_052_debt_to_equity_252'] = {'inputs': ['evl_052_debt_to_equity_252'], 'func': evl_base_universe_d2_019_evl_052_debt_to_equity_252}


def evl_base_universe_d2_020_evl_053_debt_to_assets_378(evl_053_debt_to_assets_378):
    return _base_universe_d2(evl_053_debt_to_assets_378, 20)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_020_evl_053_debt_to_assets_378'] = {'inputs': ['evl_053_debt_to_assets_378'], 'func': evl_base_universe_d2_020_evl_053_debt_to_assets_378}


def evl_base_universe_d2_021_evl_055_interest_coverage_stress_756(evl_055_interest_coverage_stress_756):
    return _base_universe_d2(evl_055_interest_coverage_stress_756, 21)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_021_evl_055_interest_coverage_stress_756'] = {'inputs': ['evl_055_interest_coverage_stress_756'], 'func': evl_base_universe_d2_021_evl_055_interest_coverage_stress_756}


def evl_base_universe_d2_022_evl_060_accrual_gap_252(evl_060_accrual_gap_252):
    return _base_universe_d2(evl_060_accrual_gap_252, 22)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_022_evl_060_accrual_gap_252'] = {'inputs': ['evl_060_accrual_gap_252'], 'func': evl_base_universe_d2_022_evl_060_accrual_gap_252}


def evl_base_universe_d2_023_evl_basefill_001(evl_basefill_001):
    return _base_universe_d2(evl_basefill_001, 23)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_023_evl_basefill_001'] = {'inputs': ['evl_basefill_001'], 'func': evl_base_universe_d2_023_evl_basefill_001}


def evl_base_universe_d2_024_evl_basefill_002(evl_basefill_002):
    return _base_universe_d2(evl_basefill_002, 24)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_024_evl_basefill_002'] = {'inputs': ['evl_basefill_002'], 'func': evl_base_universe_d2_024_evl_basefill_002}


def evl_base_universe_d2_025_evl_basefill_006(evl_basefill_006):
    return _base_universe_d2(evl_basefill_006, 25)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_025_evl_basefill_006'] = {'inputs': ['evl_basefill_006'], 'func': evl_base_universe_d2_025_evl_basefill_006}


def evl_base_universe_d2_026_evl_basefill_008(evl_basefill_008):
    return _base_universe_d2(evl_basefill_008, 26)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_026_evl_basefill_008'] = {'inputs': ['evl_basefill_008'], 'func': evl_base_universe_d2_026_evl_basefill_008}


def evl_base_universe_d2_027_evl_basefill_009(evl_basefill_009):
    return _base_universe_d2(evl_basefill_009, 27)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_027_evl_basefill_009'] = {'inputs': ['evl_basefill_009'], 'func': evl_base_universe_d2_027_evl_basefill_009}


def evl_base_universe_d2_028_evl_basefill_010(evl_basefill_010):
    return _base_universe_d2(evl_basefill_010, 28)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_028_evl_basefill_010'] = {'inputs': ['evl_basefill_010'], 'func': evl_base_universe_d2_028_evl_basefill_010}


def evl_base_universe_d2_029_evl_basefill_011(evl_basefill_011):
    return _base_universe_d2(evl_basefill_011, 29)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_029_evl_basefill_011'] = {'inputs': ['evl_basefill_011'], 'func': evl_base_universe_d2_029_evl_basefill_011}


def evl_base_universe_d2_030_evl_basefill_013(evl_basefill_013):
    return _base_universe_d2(evl_basefill_013, 30)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_030_evl_basefill_013'] = {'inputs': ['evl_basefill_013'], 'func': evl_base_universe_d2_030_evl_basefill_013}


def evl_base_universe_d2_031_evl_basefill_014(evl_basefill_014):
    return _base_universe_d2(evl_basefill_014, 31)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_031_evl_basefill_014'] = {'inputs': ['evl_basefill_014'], 'func': evl_base_universe_d2_031_evl_basefill_014}


def evl_base_universe_d2_032_evl_basefill_015(evl_basefill_015):
    return _base_universe_d2(evl_basefill_015, 32)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_032_evl_basefill_015'] = {'inputs': ['evl_basefill_015'], 'func': evl_base_universe_d2_032_evl_basefill_015}


def evl_base_universe_d2_033_evl_basefill_018(evl_basefill_018):
    return _base_universe_d2(evl_basefill_018, 33)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_033_evl_basefill_018'] = {'inputs': ['evl_basefill_018'], 'func': evl_base_universe_d2_033_evl_basefill_018}


def evl_base_universe_d2_034_evl_basefill_020(evl_basefill_020):
    return _base_universe_d2(evl_basefill_020, 34)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_034_evl_basefill_020'] = {'inputs': ['evl_basefill_020'], 'func': evl_base_universe_d2_034_evl_basefill_020}


def evl_base_universe_d2_035_evl_basefill_021(evl_basefill_021):
    return _base_universe_d2(evl_basefill_021, 35)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_035_evl_basefill_021'] = {'inputs': ['evl_basefill_021'], 'func': evl_base_universe_d2_035_evl_basefill_021}


def evl_base_universe_d2_036_evl_basefill_022(evl_basefill_022):
    return _base_universe_d2(evl_basefill_022, 36)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_036_evl_basefill_022'] = {'inputs': ['evl_basefill_022'], 'func': evl_base_universe_d2_036_evl_basefill_022}


def evl_base_universe_d2_037_evl_basefill_023(evl_basefill_023):
    return _base_universe_d2(evl_basefill_023, 37)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_037_evl_basefill_023'] = {'inputs': ['evl_basefill_023'], 'func': evl_base_universe_d2_037_evl_basefill_023}


def evl_base_universe_d2_038_evl_basefill_025(evl_basefill_025):
    return _base_universe_d2(evl_basefill_025, 38)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_038_evl_basefill_025'] = {'inputs': ['evl_basefill_025'], 'func': evl_base_universe_d2_038_evl_basefill_025}


def evl_base_universe_d2_039_evl_basefill_026(evl_basefill_026):
    return _base_universe_d2(evl_basefill_026, 39)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_039_evl_basefill_026'] = {'inputs': ['evl_basefill_026'], 'func': evl_base_universe_d2_039_evl_basefill_026}


def evl_base_universe_d2_040_evl_basefill_030(evl_basefill_030):
    return _base_universe_d2(evl_basefill_030, 40)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_040_evl_basefill_030'] = {'inputs': ['evl_basefill_030'], 'func': evl_base_universe_d2_040_evl_basefill_030}


def evl_base_universe_d2_041_evl_basefill_032(evl_basefill_032):
    return _base_universe_d2(evl_basefill_032, 41)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_041_evl_basefill_032'] = {'inputs': ['evl_basefill_032'], 'func': evl_base_universe_d2_041_evl_basefill_032}


def evl_base_universe_d2_042_evl_basefill_033(evl_basefill_033):
    return _base_universe_d2(evl_basefill_033, 42)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_042_evl_basefill_033'] = {'inputs': ['evl_basefill_033'], 'func': evl_base_universe_d2_042_evl_basefill_033}


def evl_base_universe_d2_043_evl_basefill_034(evl_basefill_034):
    return _base_universe_d2(evl_basefill_034, 43)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_043_evl_basefill_034'] = {'inputs': ['evl_basefill_034'], 'func': evl_base_universe_d2_043_evl_basefill_034}


def evl_base_universe_d2_044_evl_basefill_035(evl_basefill_035):
    return _base_universe_d2(evl_basefill_035, 44)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_044_evl_basefill_035'] = {'inputs': ['evl_basefill_035'], 'func': evl_base_universe_d2_044_evl_basefill_035}


def evl_base_universe_d2_045_evl_basefill_037(evl_basefill_037):
    return _base_universe_d2(evl_basefill_037, 45)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_045_evl_basefill_037'] = {'inputs': ['evl_basefill_037'], 'func': evl_base_universe_d2_045_evl_basefill_037}


def evl_base_universe_d2_046_evl_basefill_038(evl_basefill_038):
    return _base_universe_d2(evl_basefill_038, 46)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_046_evl_basefill_038'] = {'inputs': ['evl_basefill_038'], 'func': evl_base_universe_d2_046_evl_basefill_038}


def evl_base_universe_d2_047_evl_basefill_042(evl_basefill_042):
    return _base_universe_d2(evl_basefill_042, 47)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_047_evl_basefill_042'] = {'inputs': ['evl_basefill_042'], 'func': evl_base_universe_d2_047_evl_basefill_042}


def evl_base_universe_d2_048_evl_basefill_044(evl_basefill_044):
    return _base_universe_d2(evl_basefill_044, 48)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_048_evl_basefill_044'] = {'inputs': ['evl_basefill_044'], 'func': evl_base_universe_d2_048_evl_basefill_044}


def evl_base_universe_d2_049_evl_basefill_045(evl_basefill_045):
    return _base_universe_d2(evl_basefill_045, 49)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_049_evl_basefill_045'] = {'inputs': ['evl_basefill_045'], 'func': evl_base_universe_d2_049_evl_basefill_045}


def evl_base_universe_d2_050_evl_basefill_046(evl_basefill_046):
    return _base_universe_d2(evl_basefill_046, 50)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_050_evl_basefill_046'] = {'inputs': ['evl_basefill_046'], 'func': evl_base_universe_d2_050_evl_basefill_046}


def evl_base_universe_d2_051_evl_basefill_047(evl_basefill_047):
    return _base_universe_d2(evl_basefill_047, 51)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_051_evl_basefill_047'] = {'inputs': ['evl_basefill_047'], 'func': evl_base_universe_d2_051_evl_basefill_047}


def evl_base_universe_d2_052_evl_basefill_049(evl_basefill_049):
    return _base_universe_d2(evl_basefill_049, 52)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_052_evl_basefill_049'] = {'inputs': ['evl_basefill_049'], 'func': evl_base_universe_d2_052_evl_basefill_049}


def evl_base_universe_d2_053_evl_basefill_050(evl_basefill_050):
    return _base_universe_d2(evl_basefill_050, 53)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_053_evl_basefill_050'] = {'inputs': ['evl_basefill_050'], 'func': evl_base_universe_d2_053_evl_basefill_050}


def evl_base_universe_d2_054_evl_basefill_054(evl_basefill_054):
    return _base_universe_d2(evl_basefill_054, 54)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_054_evl_basefill_054'] = {'inputs': ['evl_basefill_054'], 'func': evl_base_universe_d2_054_evl_basefill_054}


def evl_base_universe_d2_055_evl_basefill_056(evl_basefill_056):
    return _base_universe_d2(evl_basefill_056, 55)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_055_evl_basefill_056'] = {'inputs': ['evl_basefill_056'], 'func': evl_base_universe_d2_055_evl_basefill_056}


def evl_base_universe_d2_056_evl_basefill_057(evl_basefill_057):
    return _base_universe_d2(evl_basefill_057, 56)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_056_evl_basefill_057'] = {'inputs': ['evl_basefill_057'], 'func': evl_base_universe_d2_056_evl_basefill_057}


def evl_base_universe_d2_057_evl_basefill_058(evl_basefill_058):
    return _base_universe_d2(evl_basefill_058, 57)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_057_evl_basefill_058'] = {'inputs': ['evl_basefill_058'], 'func': evl_base_universe_d2_057_evl_basefill_058}


def evl_base_universe_d2_058_evl_basefill_059(evl_basefill_059):
    return _base_universe_d2(evl_basefill_059, 58)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_058_evl_basefill_059'] = {'inputs': ['evl_basefill_059'], 'func': evl_base_universe_d2_058_evl_basefill_059}


def evl_base_universe_d2_059_evl_basefill_061(evl_basefill_061):
    return _base_universe_d2(evl_basefill_061, 59)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_059_evl_basefill_061'] = {'inputs': ['evl_basefill_061'], 'func': evl_base_universe_d2_059_evl_basefill_061}


def evl_base_universe_d2_060_evl_basefill_062(evl_basefill_062):
    return _base_universe_d2(evl_basefill_062, 60)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_060_evl_basefill_062'] = {'inputs': ['evl_basefill_062'], 'func': evl_base_universe_d2_060_evl_basefill_062}


def evl_base_universe_d2_061_evl_basefill_063(evl_basefill_063):
    return _base_universe_d2(evl_basefill_063, 61)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_061_evl_basefill_063'] = {'inputs': ['evl_basefill_063'], 'func': evl_base_universe_d2_061_evl_basefill_063}


def evl_base_universe_d2_062_evl_basefill_064(evl_basefill_064):
    return _base_universe_d2(evl_basefill_064, 62)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_062_evl_basefill_064'] = {'inputs': ['evl_basefill_064'], 'func': evl_base_universe_d2_062_evl_basefill_064}


def evl_base_universe_d2_063_evl_basefill_065(evl_basefill_065):
    return _base_universe_d2(evl_basefill_065, 63)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_063_evl_basefill_065'] = {'inputs': ['evl_basefill_065'], 'func': evl_base_universe_d2_063_evl_basefill_065}


def evl_base_universe_d2_064_evl_basefill_066(evl_basefill_066):
    return _base_universe_d2(evl_basefill_066, 64)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_064_evl_basefill_066'] = {'inputs': ['evl_basefill_066'], 'func': evl_base_universe_d2_064_evl_basefill_066}


def evl_base_universe_d2_065_evl_basefill_067(evl_basefill_067):
    return _base_universe_d2(evl_basefill_067, 65)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_065_evl_basefill_067'] = {'inputs': ['evl_basefill_067'], 'func': evl_base_universe_d2_065_evl_basefill_067}


def evl_base_universe_d2_066_evl_basefill_068(evl_basefill_068):
    return _base_universe_d2(evl_basefill_068, 66)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_066_evl_basefill_068'] = {'inputs': ['evl_basefill_068'], 'func': evl_base_universe_d2_066_evl_basefill_068}


def evl_base_universe_d2_067_evl_basefill_069(evl_basefill_069):
    return _base_universe_d2(evl_basefill_069, 67)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_067_evl_basefill_069'] = {'inputs': ['evl_basefill_069'], 'func': evl_base_universe_d2_067_evl_basefill_069}


def evl_base_universe_d2_068_evl_basefill_070(evl_basefill_070):
    return _base_universe_d2(evl_basefill_070, 68)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_068_evl_basefill_070'] = {'inputs': ['evl_basefill_070'], 'func': evl_base_universe_d2_068_evl_basefill_070}


def evl_base_universe_d2_069_evl_basefill_071(evl_basefill_071):
    return _base_universe_d2(evl_basefill_071, 69)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_069_evl_basefill_071'] = {'inputs': ['evl_basefill_071'], 'func': evl_base_universe_d2_069_evl_basefill_071}


def evl_base_universe_d2_070_evl_basefill_072(evl_basefill_072):
    return _base_universe_d2(evl_basefill_072, 70)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_070_evl_basefill_072'] = {'inputs': ['evl_basefill_072'], 'func': evl_base_universe_d2_070_evl_basefill_072}


def evl_base_universe_d2_071_evl_basefill_073(evl_basefill_073):
    return _base_universe_d2(evl_basefill_073, 71)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_071_evl_basefill_073'] = {'inputs': ['evl_basefill_073'], 'func': evl_base_universe_d2_071_evl_basefill_073}


def evl_base_universe_d2_072_evl_basefill_074(evl_basefill_074):
    return _base_universe_d2(evl_basefill_074, 72)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_072_evl_basefill_074'] = {'inputs': ['evl_basefill_074'], 'func': evl_base_universe_d2_072_evl_basefill_074}


def evl_base_universe_d2_073_evl_basefill_075(evl_basefill_075):
    return _base_universe_d2(evl_basefill_075, 73)
EVL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evl_base_universe_d2_073_evl_basefill_075'] = {'inputs': ['evl_basefill_075'], 'func': evl_base_universe_d2_073_evl_basefill_075}
