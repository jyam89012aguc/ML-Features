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



def ced_151_ced_001_dividend_cut_density_21_roc_1(ced_001_dividend_cut_density_21):
    feature = _s(ced_001_dividend_cut_density_21)
    return (_roc(feature, 1)).reindex(feature.index)

def ced_152_ced_007_listing_tier_decay_1_roc_42(ced_007_listing_tier_decay_1):
    feature = _s(ced_007_listing_tier_decay_1)
    return (_roc(feature, 42)).reindex(feature.index)

def ced_153_ced_013_delisting_notice_density_1512_roc_126(ced_013_delisting_notice_density_1512):
    feature = _s(ced_013_delisting_notice_density_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def ced_154_ced_019_going_concern_persistence_84_roc_378(ced_019_going_concern_persistence_84):
    feature = _s(ced_019_going_concern_persistence_84)
    return (_roc(feature, 378)).reindex(feature.index)

def ced_155_ced_025_event_density_z_756_roc_4(ced_025_event_density_z_756):
    feature = _s(ced_025_event_density_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















CORPORATE_EVENT_DENSITY_REGISTRY_2ND_DERIVATIVES = {
    'ced_151_ced_001_dividend_cut_density_21_roc_1': {'inputs': ['ced_001_dividend_cut_density_21'], 'func': ced_151_ced_001_dividend_cut_density_21_roc_1},
    'ced_152_ced_007_listing_tier_decay_1_roc_42': {'inputs': ['ced_007_listing_tier_decay_1'], 'func': ced_152_ced_007_listing_tier_decay_1_roc_42},
    'ced_153_ced_013_delisting_notice_density_1512_roc_126': {'inputs': ['ced_013_delisting_notice_density_1512'], 'func': ced_153_ced_013_delisting_notice_density_1512_roc_126},
    'ced_154_ced_019_going_concern_persistence_84_roc_378': {'inputs': ['ced_019_going_concern_persistence_84'], 'func': ced_154_ced_019_going_concern_persistence_84_roc_378},
    'ced_155_ced_025_event_density_z_756_roc_4': {'inputs': ['ced_025_event_density_z_756'], 'func': ced_155_ced_025_event_density_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ced_replacement_d2_001(ced_007_listing_tier_decay_1):
    feature = _clean(ced_007_listing_tier_decay_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_001'] = {'inputs': ['ced_007_listing_tier_decay_1'], 'func': ced_replacement_d2_001}


def ced_replacement_d2_002(ced_replacement_001):
    feature = _clean(ced_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_002'] = {'inputs': ['ced_replacement_001'], 'func': ced_replacement_d2_002}


def ced_replacement_d2_003(ced_replacement_002):
    feature = _clean(ced_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_003'] = {'inputs': ['ced_replacement_002'], 'func': ced_replacement_d2_003}


def ced_replacement_d2_004(ced_replacement_003):
    feature = _clean(ced_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_004'] = {'inputs': ['ced_replacement_003'], 'func': ced_replacement_d2_004}


def ced_replacement_d2_005(ced_replacement_004):
    feature = _clean(ced_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_005'] = {'inputs': ['ced_replacement_004'], 'func': ced_replacement_d2_005}


def ced_replacement_d2_006(ced_replacement_005):
    feature = _clean(ced_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_006'] = {'inputs': ['ced_replacement_005'], 'func': ced_replacement_d2_006}


def ced_replacement_d2_007(ced_replacement_006):
    feature = _clean(ced_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_007'] = {'inputs': ['ced_replacement_006'], 'func': ced_replacement_d2_007}


def ced_replacement_d2_008(ced_replacement_007):
    feature = _clean(ced_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_008'] = {'inputs': ['ced_replacement_007'], 'func': ced_replacement_d2_008}


def ced_replacement_d2_009(ced_replacement_008):
    feature = _clean(ced_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_009'] = {'inputs': ['ced_replacement_008'], 'func': ced_replacement_d2_009}


def ced_replacement_d2_010(ced_replacement_009):
    feature = _clean(ced_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_010'] = {'inputs': ['ced_replacement_009'], 'func': ced_replacement_d2_010}


def ced_replacement_d2_011(ced_replacement_010):
    feature = _clean(ced_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_011'] = {'inputs': ['ced_replacement_010'], 'func': ced_replacement_d2_011}


def ced_replacement_d2_012(ced_replacement_011):
    feature = _clean(ced_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_012'] = {'inputs': ['ced_replacement_011'], 'func': ced_replacement_d2_012}


def ced_replacement_d2_013(ced_replacement_012):
    feature = _clean(ced_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_013'] = {'inputs': ['ced_replacement_012'], 'func': ced_replacement_d2_013}


def ced_replacement_d2_014(ced_replacement_013):
    feature = _clean(ced_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_014'] = {'inputs': ['ced_replacement_013'], 'func': ced_replacement_d2_014}


def ced_replacement_d2_015(ced_replacement_014):
    feature = _clean(ced_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_015'] = {'inputs': ['ced_replacement_014'], 'func': ced_replacement_d2_015}


def ced_replacement_d2_016(ced_replacement_015):
    feature = _clean(ced_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_016'] = {'inputs': ['ced_replacement_015'], 'func': ced_replacement_d2_016}


def ced_replacement_d2_017(ced_replacement_016):
    feature = _clean(ced_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_017'] = {'inputs': ['ced_replacement_016'], 'func': ced_replacement_d2_017}


def ced_replacement_d2_018(ced_replacement_017):
    feature = _clean(ced_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_018'] = {'inputs': ['ced_replacement_017'], 'func': ced_replacement_d2_018}


def ced_replacement_d2_019(ced_replacement_018):
    feature = _clean(ced_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_019'] = {'inputs': ['ced_replacement_018'], 'func': ced_replacement_d2_019}


def ced_replacement_d2_020(ced_replacement_019):
    feature = _clean(ced_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_020'] = {'inputs': ['ced_replacement_019'], 'func': ced_replacement_d2_020}


def ced_replacement_d2_021(ced_replacement_020):
    feature = _clean(ced_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_021'] = {'inputs': ['ced_replacement_020'], 'func': ced_replacement_d2_021}


def ced_replacement_d2_022(ced_replacement_021):
    feature = _clean(ced_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_022'] = {'inputs': ['ced_replacement_021'], 'func': ced_replacement_d2_022}


def ced_replacement_d2_023(ced_replacement_022):
    feature = _clean(ced_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_023'] = {'inputs': ['ced_replacement_022'], 'func': ced_replacement_d2_023}


def ced_replacement_d2_024(ced_replacement_023):
    feature = _clean(ced_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_024'] = {'inputs': ['ced_replacement_023'], 'func': ced_replacement_d2_024}


def ced_replacement_d2_025(ced_replacement_024):
    feature = _clean(ced_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_025'] = {'inputs': ['ced_replacement_024'], 'func': ced_replacement_d2_025}


def ced_replacement_d2_026(ced_replacement_025):
    feature = _clean(ced_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_026'] = {'inputs': ['ced_replacement_025'], 'func': ced_replacement_d2_026}


def ced_replacement_d2_027(ced_replacement_026):
    feature = _clean(ced_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_027'] = {'inputs': ['ced_replacement_026'], 'func': ced_replacement_d2_027}


def ced_replacement_d2_028(ced_replacement_027):
    feature = _clean(ced_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_028'] = {'inputs': ['ced_replacement_027'], 'func': ced_replacement_d2_028}


def ced_replacement_d2_029(ced_replacement_028):
    feature = _clean(ced_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_029'] = {'inputs': ['ced_replacement_028'], 'func': ced_replacement_d2_029}


def ced_replacement_d2_030(ced_replacement_029):
    feature = _clean(ced_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_030'] = {'inputs': ['ced_replacement_029'], 'func': ced_replacement_d2_030}


def ced_replacement_d2_031(ced_replacement_030):
    feature = _clean(ced_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_031'] = {'inputs': ['ced_replacement_030'], 'func': ced_replacement_d2_031}


def ced_replacement_d2_032(ced_replacement_031):
    feature = _clean(ced_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_032'] = {'inputs': ['ced_replacement_031'], 'func': ced_replacement_d2_032}


def ced_replacement_d2_033(ced_replacement_032):
    feature = _clean(ced_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_033'] = {'inputs': ['ced_replacement_032'], 'func': ced_replacement_d2_033}


def ced_replacement_d2_034(ced_replacement_033):
    feature = _clean(ced_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_034'] = {'inputs': ['ced_replacement_033'], 'func': ced_replacement_d2_034}


def ced_replacement_d2_035(ced_replacement_034):
    feature = _clean(ced_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_035'] = {'inputs': ['ced_replacement_034'], 'func': ced_replacement_d2_035}


def ced_replacement_d2_036(ced_replacement_035):
    feature = _clean(ced_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_036'] = {'inputs': ['ced_replacement_035'], 'func': ced_replacement_d2_036}


def ced_replacement_d2_037(ced_replacement_036):
    feature = _clean(ced_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_037'] = {'inputs': ['ced_replacement_036'], 'func': ced_replacement_d2_037}


def ced_replacement_d2_038(ced_replacement_037):
    feature = _clean(ced_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_038'] = {'inputs': ['ced_replacement_037'], 'func': ced_replacement_d2_038}


def ced_replacement_d2_039(ced_replacement_038):
    feature = _clean(ced_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_039'] = {'inputs': ['ced_replacement_038'], 'func': ced_replacement_d2_039}


def ced_replacement_d2_040(ced_replacement_039):
    feature = _clean(ced_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_040'] = {'inputs': ['ced_replacement_039'], 'func': ced_replacement_d2_040}


def ced_replacement_d2_041(ced_replacement_040):
    feature = _clean(ced_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_041'] = {'inputs': ['ced_replacement_040'], 'func': ced_replacement_d2_041}


def ced_replacement_d2_042(ced_replacement_041):
    feature = _clean(ced_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_042'] = {'inputs': ['ced_replacement_041'], 'func': ced_replacement_d2_042}


def ced_replacement_d2_043(ced_replacement_042):
    feature = _clean(ced_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_043'] = {'inputs': ['ced_replacement_042'], 'func': ced_replacement_d2_043}


def ced_replacement_d2_044(ced_replacement_043):
    feature = _clean(ced_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_044'] = {'inputs': ['ced_replacement_043'], 'func': ced_replacement_d2_044}


def ced_replacement_d2_045(ced_replacement_044):
    feature = _clean(ced_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_045'] = {'inputs': ['ced_replacement_044'], 'func': ced_replacement_d2_045}


def ced_replacement_d2_046(ced_replacement_045):
    feature = _clean(ced_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_046'] = {'inputs': ['ced_replacement_045'], 'func': ced_replacement_d2_046}


def ced_replacement_d2_047(ced_replacement_046):
    feature = _clean(ced_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_047'] = {'inputs': ['ced_replacement_046'], 'func': ced_replacement_d2_047}


def ced_replacement_d2_048(ced_replacement_047):
    feature = _clean(ced_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_048'] = {'inputs': ['ced_replacement_047'], 'func': ced_replacement_d2_048}


def ced_replacement_d2_049(ced_replacement_048):
    feature = _clean(ced_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_049'] = {'inputs': ['ced_replacement_048'], 'func': ced_replacement_d2_049}


def ced_replacement_d2_050(ced_replacement_049):
    feature = _clean(ced_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_050'] = {'inputs': ['ced_replacement_049'], 'func': ced_replacement_d2_050}


def ced_replacement_d2_051(ced_replacement_050):
    feature = _clean(ced_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_051'] = {'inputs': ['ced_replacement_050'], 'func': ced_replacement_d2_051}


def ced_replacement_d2_052(ced_replacement_051):
    feature = _clean(ced_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_052'] = {'inputs': ['ced_replacement_051'], 'func': ced_replacement_d2_052}


def ced_replacement_d2_053(ced_replacement_052):
    feature = _clean(ced_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_053'] = {'inputs': ['ced_replacement_052'], 'func': ced_replacement_d2_053}


def ced_replacement_d2_054(ced_replacement_053):
    feature = _clean(ced_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_054'] = {'inputs': ['ced_replacement_053'], 'func': ced_replacement_d2_054}


def ced_replacement_d2_055(ced_replacement_054):
    feature = _clean(ced_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_055'] = {'inputs': ['ced_replacement_054'], 'func': ced_replacement_d2_055}


def ced_replacement_d2_056(ced_replacement_055):
    feature = _clean(ced_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_056'] = {'inputs': ['ced_replacement_055'], 'func': ced_replacement_d2_056}


def ced_replacement_d2_057(ced_replacement_056):
    feature = _clean(ced_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_057'] = {'inputs': ['ced_replacement_056'], 'func': ced_replacement_d2_057}


def ced_replacement_d2_058(ced_replacement_057):
    feature = _clean(ced_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_058'] = {'inputs': ['ced_replacement_057'], 'func': ced_replacement_d2_058}


def ced_replacement_d2_059(ced_replacement_058):
    feature = _clean(ced_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_059'] = {'inputs': ['ced_replacement_058'], 'func': ced_replacement_d2_059}


def ced_replacement_d2_060(ced_replacement_059):
    feature = _clean(ced_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_060'] = {'inputs': ['ced_replacement_059'], 'func': ced_replacement_d2_060}


def ced_replacement_d2_061(ced_replacement_060):
    feature = _clean(ced_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_061'] = {'inputs': ['ced_replacement_060'], 'func': ced_replacement_d2_061}


def ced_replacement_d2_062(ced_replacement_061):
    feature = _clean(ced_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_062'] = {'inputs': ['ced_replacement_061'], 'func': ced_replacement_d2_062}


def ced_replacement_d2_063(ced_replacement_062):
    feature = _clean(ced_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_063'] = {'inputs': ['ced_replacement_062'], 'func': ced_replacement_d2_063}


def ced_replacement_d2_064(ced_replacement_063):
    feature = _clean(ced_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_064'] = {'inputs': ['ced_replacement_063'], 'func': ced_replacement_d2_064}


def ced_replacement_d2_065(ced_replacement_064):
    feature = _clean(ced_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_065'] = {'inputs': ['ced_replacement_064'], 'func': ced_replacement_d2_065}


def ced_replacement_d2_066(ced_replacement_065):
    feature = _clean(ced_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_066'] = {'inputs': ['ced_replacement_065'], 'func': ced_replacement_d2_066}


def ced_replacement_d2_067(ced_replacement_066):
    feature = _clean(ced_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_067'] = {'inputs': ['ced_replacement_066'], 'func': ced_replacement_d2_067}


def ced_replacement_d2_068(ced_replacement_067):
    feature = _clean(ced_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_068'] = {'inputs': ['ced_replacement_067'], 'func': ced_replacement_d2_068}


def ced_replacement_d2_069(ced_replacement_068):
    feature = _clean(ced_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_069'] = {'inputs': ['ced_replacement_068'], 'func': ced_replacement_d2_069}


def ced_replacement_d2_070(ced_replacement_069):
    feature = _clean(ced_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_070'] = {'inputs': ['ced_replacement_069'], 'func': ced_replacement_d2_070}


def ced_replacement_d2_071(ced_replacement_070):
    feature = _clean(ced_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_071'] = {'inputs': ['ced_replacement_070'], 'func': ced_replacement_d2_071}


def ced_replacement_d2_072(ced_replacement_071):
    feature = _clean(ced_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_072'] = {'inputs': ['ced_replacement_071'], 'func': ced_replacement_d2_072}


def ced_replacement_d2_073(ced_replacement_072):
    feature = _clean(ced_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_073'] = {'inputs': ['ced_replacement_072'], 'func': ced_replacement_d2_073}


def ced_replacement_d2_074(ced_replacement_073):
    feature = _clean(ced_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_074'] = {'inputs': ['ced_replacement_073'], 'func': ced_replacement_d2_074}


def ced_replacement_d2_075(ced_replacement_074):
    feature = _clean(ced_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_075'] = {'inputs': ['ced_replacement_074'], 'func': ced_replacement_d2_075}


def ced_replacement_d2_076(ced_replacement_075):
    feature = _clean(ced_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_076'] = {'inputs': ['ced_replacement_075'], 'func': ced_replacement_d2_076}


def ced_replacement_d2_077(ced_replacement_076):
    feature = _clean(ced_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_077'] = {'inputs': ['ced_replacement_076'], 'func': ced_replacement_d2_077}


def ced_replacement_d2_078(ced_replacement_077):
    feature = _clean(ced_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_078'] = {'inputs': ['ced_replacement_077'], 'func': ced_replacement_d2_078}


def ced_replacement_d2_079(ced_replacement_078):
    feature = _clean(ced_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_079'] = {'inputs': ['ced_replacement_078'], 'func': ced_replacement_d2_079}


def ced_replacement_d2_080(ced_replacement_079):
    feature = _clean(ced_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_080'] = {'inputs': ['ced_replacement_079'], 'func': ced_replacement_d2_080}


def ced_replacement_d2_081(ced_replacement_080):
    feature = _clean(ced_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_081'] = {'inputs': ['ced_replacement_080'], 'func': ced_replacement_d2_081}


def ced_replacement_d2_082(ced_replacement_081):
    feature = _clean(ced_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_082'] = {'inputs': ['ced_replacement_081'], 'func': ced_replacement_d2_082}


def ced_replacement_d2_083(ced_replacement_082):
    feature = _clean(ced_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_083'] = {'inputs': ['ced_replacement_082'], 'func': ced_replacement_d2_083}


def ced_replacement_d2_084(ced_replacement_083):
    feature = _clean(ced_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_084'] = {'inputs': ['ced_replacement_083'], 'func': ced_replacement_d2_084}


def ced_replacement_d2_085(ced_replacement_084):
    feature = _clean(ced_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_085'] = {'inputs': ['ced_replacement_084'], 'func': ced_replacement_d2_085}


def ced_replacement_d2_086(ced_replacement_085):
    feature = _clean(ced_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_086'] = {'inputs': ['ced_replacement_085'], 'func': ced_replacement_d2_086}


def ced_replacement_d2_087(ced_replacement_086):
    feature = _clean(ced_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_087'] = {'inputs': ['ced_replacement_086'], 'func': ced_replacement_d2_087}


def ced_replacement_d2_088(ced_replacement_087):
    feature = _clean(ced_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_088'] = {'inputs': ['ced_replacement_087'], 'func': ced_replacement_d2_088}


def ced_replacement_d2_089(ced_replacement_088):
    feature = _clean(ced_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_089'] = {'inputs': ['ced_replacement_088'], 'func': ced_replacement_d2_089}


def ced_replacement_d2_090(ced_replacement_089):
    feature = _clean(ced_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_090'] = {'inputs': ['ced_replacement_089'], 'func': ced_replacement_d2_090}


def ced_replacement_d2_091(ced_replacement_090):
    feature = _clean(ced_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_091'] = {'inputs': ['ced_replacement_090'], 'func': ced_replacement_d2_091}


def ced_replacement_d2_092(ced_replacement_091):
    feature = _clean(ced_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_092'] = {'inputs': ['ced_replacement_091'], 'func': ced_replacement_d2_092}


def ced_replacement_d2_093(ced_replacement_092):
    feature = _clean(ced_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_093'] = {'inputs': ['ced_replacement_092'], 'func': ced_replacement_d2_093}


def ced_replacement_d2_094(ced_replacement_093):
    feature = _clean(ced_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_094'] = {'inputs': ['ced_replacement_093'], 'func': ced_replacement_d2_094}


def ced_replacement_d2_095(ced_replacement_094):
    feature = _clean(ced_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_095'] = {'inputs': ['ced_replacement_094'], 'func': ced_replacement_d2_095}


def ced_replacement_d2_096(ced_replacement_095):
    feature = _clean(ced_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_096'] = {'inputs': ['ced_replacement_095'], 'func': ced_replacement_d2_096}


def ced_replacement_d2_097(ced_replacement_096):
    feature = _clean(ced_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_097'] = {'inputs': ['ced_replacement_096'], 'func': ced_replacement_d2_097}


def ced_replacement_d2_098(ced_replacement_097):
    feature = _clean(ced_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_098'] = {'inputs': ['ced_replacement_097'], 'func': ced_replacement_d2_098}


def ced_replacement_d2_099(ced_replacement_098):
    feature = _clean(ced_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_099'] = {'inputs': ['ced_replacement_098'], 'func': ced_replacement_d2_099}


def ced_replacement_d2_100(ced_replacement_099):
    feature = _clean(ced_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_100'] = {'inputs': ['ced_replacement_099'], 'func': ced_replacement_d2_100}


def ced_replacement_d2_101(ced_replacement_100):
    feature = _clean(ced_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_101'] = {'inputs': ['ced_replacement_100'], 'func': ced_replacement_d2_101}


def ced_replacement_d2_102(ced_replacement_101):
    feature = _clean(ced_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_102'] = {'inputs': ['ced_replacement_101'], 'func': ced_replacement_d2_102}


def ced_replacement_d2_103(ced_replacement_102):
    feature = _clean(ced_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_103'] = {'inputs': ['ced_replacement_102'], 'func': ced_replacement_d2_103}


def ced_replacement_d2_104(ced_replacement_103):
    feature = _clean(ced_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_104'] = {'inputs': ['ced_replacement_103'], 'func': ced_replacement_d2_104}


def ced_replacement_d2_105(ced_replacement_104):
    feature = _clean(ced_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_105'] = {'inputs': ['ced_replacement_104'], 'func': ced_replacement_d2_105}


def ced_replacement_d2_106(ced_replacement_105):
    feature = _clean(ced_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_106'] = {'inputs': ['ced_replacement_105'], 'func': ced_replacement_d2_106}


def ced_replacement_d2_107(ced_replacement_106):
    feature = _clean(ced_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_107'] = {'inputs': ['ced_replacement_106'], 'func': ced_replacement_d2_107}


def ced_replacement_d2_108(ced_replacement_107):
    feature = _clean(ced_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_108'] = {'inputs': ['ced_replacement_107'], 'func': ced_replacement_d2_108}


def ced_replacement_d2_109(ced_replacement_108):
    feature = _clean(ced_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_109'] = {'inputs': ['ced_replacement_108'], 'func': ced_replacement_d2_109}


def ced_replacement_d2_110(ced_replacement_109):
    feature = _clean(ced_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_110'] = {'inputs': ['ced_replacement_109'], 'func': ced_replacement_d2_110}


def ced_replacement_d2_111(ced_replacement_110):
    feature = _clean(ced_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_111'] = {'inputs': ['ced_replacement_110'], 'func': ced_replacement_d2_111}


def ced_replacement_d2_112(ced_replacement_111):
    feature = _clean(ced_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_112'] = {'inputs': ['ced_replacement_111'], 'func': ced_replacement_d2_112}


def ced_replacement_d2_113(ced_replacement_112):
    feature = _clean(ced_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_113'] = {'inputs': ['ced_replacement_112'], 'func': ced_replacement_d2_113}


def ced_replacement_d2_114(ced_replacement_113):
    feature = _clean(ced_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_114'] = {'inputs': ['ced_replacement_113'], 'func': ced_replacement_d2_114}


def ced_replacement_d2_115(ced_replacement_114):
    feature = _clean(ced_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_115'] = {'inputs': ['ced_replacement_114'], 'func': ced_replacement_d2_115}


def ced_replacement_d2_116(ced_replacement_115):
    feature = _clean(ced_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_116'] = {'inputs': ['ced_replacement_115'], 'func': ced_replacement_d2_116}


def ced_replacement_d2_117(ced_replacement_116):
    feature = _clean(ced_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_117'] = {'inputs': ['ced_replacement_116'], 'func': ced_replacement_d2_117}


def ced_replacement_d2_118(ced_replacement_117):
    feature = _clean(ced_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_118'] = {'inputs': ['ced_replacement_117'], 'func': ced_replacement_d2_118}


def ced_replacement_d2_119(ced_replacement_118):
    feature = _clean(ced_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_119'] = {'inputs': ['ced_replacement_118'], 'func': ced_replacement_d2_119}


def ced_replacement_d2_120(ced_replacement_119):
    feature = _clean(ced_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_120'] = {'inputs': ['ced_replacement_119'], 'func': ced_replacement_d2_120}


def ced_replacement_d2_121(ced_replacement_120):
    feature = _clean(ced_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_121'] = {'inputs': ['ced_replacement_120'], 'func': ced_replacement_d2_121}


def ced_replacement_d2_122(ced_replacement_121):
    feature = _clean(ced_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_122'] = {'inputs': ['ced_replacement_121'], 'func': ced_replacement_d2_122}


def ced_replacement_d2_123(ced_replacement_122):
    feature = _clean(ced_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_123'] = {'inputs': ['ced_replacement_122'], 'func': ced_replacement_d2_123}


def ced_replacement_d2_124(ced_replacement_123):
    feature = _clean(ced_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_124'] = {'inputs': ['ced_replacement_123'], 'func': ced_replacement_d2_124}


def ced_replacement_d2_125(ced_replacement_124):
    feature = _clean(ced_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_125'] = {'inputs': ['ced_replacement_124'], 'func': ced_replacement_d2_125}


def ced_replacement_d2_126(ced_replacement_125):
    feature = _clean(ced_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_126'] = {'inputs': ['ced_replacement_125'], 'func': ced_replacement_d2_126}


def ced_replacement_d2_127(ced_replacement_126):
    feature = _clean(ced_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_127'] = {'inputs': ['ced_replacement_126'], 'func': ced_replacement_d2_127}


def ced_replacement_d2_128(ced_replacement_127):
    feature = _clean(ced_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_128'] = {'inputs': ['ced_replacement_127'], 'func': ced_replacement_d2_128}


def ced_replacement_d2_129(ced_replacement_128):
    feature = _clean(ced_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_129'] = {'inputs': ['ced_replacement_128'], 'func': ced_replacement_d2_129}


def ced_replacement_d2_130(ced_replacement_129):
    feature = _clean(ced_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_130'] = {'inputs': ['ced_replacement_129'], 'func': ced_replacement_d2_130}


def ced_replacement_d2_131(ced_replacement_130):
    feature = _clean(ced_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_131'] = {'inputs': ['ced_replacement_130'], 'func': ced_replacement_d2_131}


def ced_replacement_d2_132(ced_replacement_131):
    feature = _clean(ced_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_132'] = {'inputs': ['ced_replacement_131'], 'func': ced_replacement_d2_132}


def ced_replacement_d2_133(ced_replacement_132):
    feature = _clean(ced_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_133'] = {'inputs': ['ced_replacement_132'], 'func': ced_replacement_d2_133}


def ced_replacement_d2_134(ced_replacement_133):
    feature = _clean(ced_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_134'] = {'inputs': ['ced_replacement_133'], 'func': ced_replacement_d2_134}


def ced_replacement_d2_135(ced_replacement_134):
    feature = _clean(ced_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_135'] = {'inputs': ['ced_replacement_134'], 'func': ced_replacement_d2_135}


def ced_replacement_d2_136(ced_replacement_135):
    feature = _clean(ced_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_136'] = {'inputs': ['ced_replacement_135'], 'func': ced_replacement_d2_136}


def ced_replacement_d2_137(ced_replacement_136):
    feature = _clean(ced_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_137'] = {'inputs': ['ced_replacement_136'], 'func': ced_replacement_d2_137}


def ced_replacement_d2_138(ced_replacement_137):
    feature = _clean(ced_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_138'] = {'inputs': ['ced_replacement_137'], 'func': ced_replacement_d2_138}


def ced_replacement_d2_139(ced_replacement_138):
    feature = _clean(ced_replacement_138)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_139'] = {'inputs': ['ced_replacement_138'], 'func': ced_replacement_d2_139}


def ced_replacement_d2_140(ced_replacement_139):
    feature = _clean(ced_replacement_139)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_140'] = {'inputs': ['ced_replacement_139'], 'func': ced_replacement_d2_140}


def ced_replacement_d2_141(ced_replacement_140):
    feature = _clean(ced_replacement_140)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_141'] = {'inputs': ['ced_replacement_140'], 'func': ced_replacement_d2_141}


def ced_replacement_d2_142(ced_replacement_141):
    feature = _clean(ced_replacement_141)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_142'] = {'inputs': ['ced_replacement_141'], 'func': ced_replacement_d2_142}


def ced_replacement_d2_143(ced_replacement_142):
    feature = _clean(ced_replacement_142)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_143'] = {'inputs': ['ced_replacement_142'], 'func': ced_replacement_d2_143}


def ced_replacement_d2_144(ced_replacement_143):
    feature = _clean(ced_replacement_143)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_144'] = {'inputs': ['ced_replacement_143'], 'func': ced_replacement_d2_144}


def ced_replacement_d2_145(ced_replacement_144):
    feature = _clean(ced_replacement_144)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_145'] = {'inputs': ['ced_replacement_144'], 'func': ced_replacement_d2_145}


def ced_replacement_d2_146(ced_replacement_145):
    feature = _clean(ced_replacement_145)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_146'] = {'inputs': ['ced_replacement_145'], 'func': ced_replacement_d2_146}


def ced_replacement_d2_147(ced_replacement_146):
    feature = _clean(ced_replacement_146)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_147'] = {'inputs': ['ced_replacement_146'], 'func': ced_replacement_d2_147}


def ced_replacement_d2_148(ced_replacement_147):
    feature = _clean(ced_replacement_147)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_148'] = {'inputs': ['ced_replacement_147'], 'func': ced_replacement_d2_148}


def ced_replacement_d2_149(ced_replacement_148):
    feature = _clean(ced_replacement_148)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_149'] = {'inputs': ['ced_replacement_148'], 'func': ced_replacement_d2_149}


def ced_replacement_d2_150(ced_replacement_149):
    feature = _clean(ced_replacement_149)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_150'] = {'inputs': ['ced_replacement_149'], 'func': ced_replacement_d2_150}


def ced_replacement_d2_151(ced_replacement_150):
    feature = _clean(ced_replacement_150)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
CED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ced_replacement_d2_151'] = {'inputs': ['ced_replacement_150'], 'func': ced_replacement_d2_151}


# Base-universe derivative extensions for repaired first-base features.
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ced_base_universe_d2_001_ced_002_dividend_suspension_density_42(ced_002_dividend_suspension_density_42):
    return _base_universe_d2(ced_002_dividend_suspension_density_42, 1)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_001_ced_002_dividend_suspension_density_42'] = {'inputs': ['ced_002_dividend_suspension_density_42'], 'func': ced_base_universe_d2_001_ced_002_dividend_suspension_density_42}


def ced_base_universe_d2_002_ced_003_reverse_split_density_63(ced_003_reverse_split_density_63):
    return _base_universe_d2(ced_003_reverse_split_density_63, 2)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_002_ced_003_reverse_split_density_63'] = {'inputs': ['ced_003_reverse_split_density_63'], 'func': ced_base_universe_d2_002_ced_003_reverse_split_density_63}


def ced_base_universe_d2_003_ced_004_event_density_z_84(ced_004_event_density_z_84):
    return _base_universe_d2(ced_004_event_density_z_84, 3)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_003_ced_004_event_density_z_84'] = {'inputs': ['ced_004_event_density_z_84'], 'func': ced_base_universe_d2_003_ced_004_event_density_z_84}


def ced_base_universe_d2_004_ced_005_going_concern_persistence_126(ced_005_going_concern_persistence_126):
    return _base_universe_d2(ced_005_going_concern_persistence_126, 4)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_004_ced_005_going_concern_persistence_126'] = {'inputs': ['ced_005_going_concern_persistence_126'], 'func': ced_base_universe_d2_004_ced_005_going_concern_persistence_126}


def ced_base_universe_d2_005_ced_006_delisting_notice_density_189(ced_006_delisting_notice_density_189):
    return _base_universe_d2(ced_006_delisting_notice_density_189, 5)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_005_ced_006_delisting_notice_density_189'] = {'inputs': ['ced_006_delisting_notice_density_189'], 'func': ced_base_universe_d2_005_ced_006_delisting_notice_density_189}


def ced_base_universe_d2_006_ced_008_dividend_cut_density_378(ced_008_dividend_cut_density_378):
    return _base_universe_d2(ced_008_dividend_cut_density_378, 6)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_006_ced_008_dividend_cut_density_378'] = {'inputs': ['ced_008_dividend_cut_density_378'], 'func': ced_base_universe_d2_006_ced_008_dividend_cut_density_378}


def ced_base_universe_d2_007_ced_009_dividend_suspension_density_504(ced_009_dividend_suspension_density_504):
    return _base_universe_d2(ced_009_dividend_suspension_density_504, 7)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_007_ced_009_dividend_suspension_density_504'] = {'inputs': ['ced_009_dividend_suspension_density_504'], 'func': ced_base_universe_d2_007_ced_009_dividend_suspension_density_504}


def ced_base_universe_d2_008_ced_010_reverse_split_density_756(ced_010_reverse_split_density_756):
    return _base_universe_d2(ced_010_reverse_split_density_756, 8)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_008_ced_010_reverse_split_density_756'] = {'inputs': ['ced_010_reverse_split_density_756'], 'func': ced_base_universe_d2_008_ced_010_reverse_split_density_756}


def ced_base_universe_d2_009_ced_011_event_density_z_1008(ced_011_event_density_z_1008):
    return _base_universe_d2(ced_011_event_density_z_1008, 9)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_009_ced_011_event_density_z_1008'] = {'inputs': ['ced_011_event_density_z_1008'], 'func': ced_base_universe_d2_009_ced_011_event_density_z_1008}


def ced_base_universe_d2_010_ced_012_going_concern_persistence_1260(ced_012_going_concern_persistence_1260):
    return _base_universe_d2(ced_012_going_concern_persistence_1260, 10)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_010_ced_012_going_concern_persistence_1260'] = {'inputs': ['ced_012_going_concern_persistence_1260'], 'func': ced_base_universe_d2_010_ced_012_going_concern_persistence_1260}


def ced_base_universe_d2_011_ced_015_dividend_cut_density_252(ced_015_dividend_cut_density_252):
    return _base_universe_d2(ced_015_dividend_cut_density_252, 11)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_011_ced_015_dividend_cut_density_252'] = {'inputs': ['ced_015_dividend_cut_density_252'], 'func': ced_base_universe_d2_011_ced_015_dividend_cut_density_252}


def ced_base_universe_d2_012_ced_018_event_density_z_63(ced_018_event_density_z_63):
    return _base_universe_d2(ced_018_event_density_z_63, 12)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_012_ced_018_event_density_z_63'] = {'inputs': ['ced_018_event_density_z_63'], 'func': ced_base_universe_d2_012_ced_018_event_density_z_63}


def ced_base_universe_d2_013_ced_020_delisting_notice_density_126(ced_020_delisting_notice_density_126):
    return _base_universe_d2(ced_020_delisting_notice_density_126, 13)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_013_ced_020_delisting_notice_density_126'] = {'inputs': ['ced_020_delisting_notice_density_126'], 'func': ced_base_universe_d2_013_ced_020_delisting_notice_density_126}


def ced_base_universe_d2_014_ced_026_going_concern_persistence_1008(ced_026_going_concern_persistence_1008):
    return _base_universe_d2(ced_026_going_concern_persistence_1008, 14)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_014_ced_026_going_concern_persistence_1008'] = {'inputs': ['ced_026_going_concern_persistence_1008'], 'func': ced_base_universe_d2_014_ced_026_going_concern_persistence_1008}


def ced_base_universe_d2_015_ced_027_delisting_notice_density_1260(ced_027_delisting_notice_density_1260):
    return _base_universe_d2(ced_027_delisting_notice_density_1260, 15)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_015_ced_027_delisting_notice_density_1260'] = {'inputs': ['ced_027_delisting_notice_density_1260'], 'func': ced_base_universe_d2_015_ced_027_delisting_notice_density_1260}


def ced_base_universe_d2_016_ced_032_event_density_z_42(ced_032_event_density_z_42):
    return _base_universe_d2(ced_032_event_density_z_42, 16)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_016_ced_032_event_density_z_42'] = {'inputs': ['ced_032_event_density_z_42'], 'func': ced_base_universe_d2_016_ced_032_event_density_z_42}


def ced_base_universe_d2_017_ced_033_going_concern_persistence_63(ced_033_going_concern_persistence_63):
    return _base_universe_d2(ced_033_going_concern_persistence_63, 17)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_017_ced_033_going_concern_persistence_63'] = {'inputs': ['ced_033_going_concern_persistence_63'], 'func': ced_base_universe_d2_017_ced_033_going_concern_persistence_63}


def ced_base_universe_d2_018_ced_034_delisting_notice_density_84(ced_034_delisting_notice_density_84):
    return _base_universe_d2(ced_034_delisting_notice_density_84, 18)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_018_ced_034_delisting_notice_density_84'] = {'inputs': ['ced_034_delisting_notice_density_84'], 'func': ced_base_universe_d2_018_ced_034_delisting_notice_density_84}


def ced_base_universe_d2_019_ced_039_event_density_z_504(ced_039_event_density_z_504):
    return _base_universe_d2(ced_039_event_density_z_504, 19)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_019_ced_039_event_density_z_504'] = {'inputs': ['ced_039_event_density_z_504'], 'func': ced_base_universe_d2_019_ced_039_event_density_z_504}


def ced_base_universe_d2_020_ced_040_going_concern_persistence_756(ced_040_going_concern_persistence_756):
    return _base_universe_d2(ced_040_going_concern_persistence_756, 20)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_020_ced_040_going_concern_persistence_756'] = {'inputs': ['ced_040_going_concern_persistence_756'], 'func': ced_base_universe_d2_020_ced_040_going_concern_persistence_756}


def ced_base_universe_d2_021_ced_041_delisting_notice_density_1008(ced_041_delisting_notice_density_1008):
    return _base_universe_d2(ced_041_delisting_notice_density_1008, 21)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_021_ced_041_delisting_notice_density_1008'] = {'inputs': ['ced_041_delisting_notice_density_1008'], 'func': ced_base_universe_d2_021_ced_041_delisting_notice_density_1008}


def ced_base_universe_d2_022_ced_046_event_density_z_21(ced_046_event_density_z_21):
    return _base_universe_d2(ced_046_event_density_z_21, 22)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_022_ced_046_event_density_z_21'] = {'inputs': ['ced_046_event_density_z_21'], 'func': ced_base_universe_d2_022_ced_046_event_density_z_21}


def ced_base_universe_d2_023_ced_047_going_concern_persistence_42(ced_047_going_concern_persistence_42):
    return _base_universe_d2(ced_047_going_concern_persistence_42, 23)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_023_ced_047_going_concern_persistence_42'] = {'inputs': ['ced_047_going_concern_persistence_42'], 'func': ced_base_universe_d2_023_ced_047_going_concern_persistence_42}


def ced_base_universe_d2_024_ced_053_event_density_z_378(ced_053_event_density_z_378):
    return _base_universe_d2(ced_053_event_density_z_378, 24)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_024_ced_053_event_density_z_378'] = {'inputs': ['ced_053_event_density_z_378'], 'func': ced_base_universe_d2_024_ced_053_event_density_z_378}


def ced_base_universe_d2_025_ced_054_going_concern_persistence_504(ced_054_going_concern_persistence_504):
    return _base_universe_d2(ced_054_going_concern_persistence_504, 25)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_025_ced_054_going_concern_persistence_504'] = {'inputs': ['ced_054_going_concern_persistence_504'], 'func': ced_base_universe_d2_025_ced_054_going_concern_persistence_504}


def ced_base_universe_d2_026_ced_060_event_density_z_252(ced_060_event_density_z_252):
    return _base_universe_d2(ced_060_event_density_z_252, 26)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_026_ced_060_event_density_z_252'] = {'inputs': ['ced_060_event_density_z_252'], 'func': ced_base_universe_d2_026_ced_060_event_density_z_252}


def ced_base_universe_d2_027_ced_061_going_concern_persistence_21(ced_061_going_concern_persistence_21):
    return _base_universe_d2(ced_061_going_concern_persistence_21, 27)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_027_ced_061_going_concern_persistence_21'] = {'inputs': ['ced_061_going_concern_persistence_21'], 'func': ced_base_universe_d2_027_ced_061_going_concern_persistence_21}


def ced_base_universe_d2_028_ced_068_going_concern_persistence_378(ced_068_going_concern_persistence_378):
    return _base_universe_d2(ced_068_going_concern_persistence_378, 28)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_028_ced_068_going_concern_persistence_378'] = {'inputs': ['ced_068_going_concern_persistence_378'], 'func': ced_base_universe_d2_028_ced_068_going_concern_persistence_378}


def ced_base_universe_d2_029_ced_075_going_concern_persistence_252(ced_075_going_concern_persistence_252):
    return _base_universe_d2(ced_075_going_concern_persistence_252, 29)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_029_ced_075_going_concern_persistence_252'] = {'inputs': ['ced_075_going_concern_persistence_252'], 'func': ced_base_universe_d2_029_ced_075_going_concern_persistence_252}


def ced_base_universe_d2_030_ced_basefill_007(ced_basefill_007):
    return _base_universe_d2(ced_basefill_007, 30)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_030_ced_basefill_007'] = {'inputs': ['ced_basefill_007'], 'func': ced_base_universe_d2_030_ced_basefill_007}


def ced_base_universe_d2_031_ced_basefill_014(ced_basefill_014):
    return _base_universe_d2(ced_basefill_014, 31)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_031_ced_basefill_014'] = {'inputs': ['ced_basefill_014'], 'func': ced_base_universe_d2_031_ced_basefill_014}


def ced_base_universe_d2_032_ced_basefill_016(ced_basefill_016):
    return _base_universe_d2(ced_basefill_016, 32)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_032_ced_basefill_016'] = {'inputs': ['ced_basefill_016'], 'func': ced_base_universe_d2_032_ced_basefill_016}


def ced_base_universe_d2_033_ced_basefill_017(ced_basefill_017):
    return _base_universe_d2(ced_basefill_017, 33)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_033_ced_basefill_017'] = {'inputs': ['ced_basefill_017'], 'func': ced_base_universe_d2_033_ced_basefill_017}


def ced_base_universe_d2_034_ced_basefill_021(ced_basefill_021):
    return _base_universe_d2(ced_basefill_021, 34)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_034_ced_basefill_021'] = {'inputs': ['ced_basefill_021'], 'func': ced_base_universe_d2_034_ced_basefill_021}


def ced_base_universe_d2_035_ced_basefill_022(ced_basefill_022):
    return _base_universe_d2(ced_basefill_022, 35)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_035_ced_basefill_022'] = {'inputs': ['ced_basefill_022'], 'func': ced_base_universe_d2_035_ced_basefill_022}


def ced_base_universe_d2_036_ced_basefill_023(ced_basefill_023):
    return _base_universe_d2(ced_basefill_023, 36)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_036_ced_basefill_023'] = {'inputs': ['ced_basefill_023'], 'func': ced_base_universe_d2_036_ced_basefill_023}


def ced_base_universe_d2_037_ced_basefill_024(ced_basefill_024):
    return _base_universe_d2(ced_basefill_024, 37)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_037_ced_basefill_024'] = {'inputs': ['ced_basefill_024'], 'func': ced_base_universe_d2_037_ced_basefill_024}


def ced_base_universe_d2_038_ced_basefill_028(ced_basefill_028):
    return _base_universe_d2(ced_basefill_028, 38)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_038_ced_basefill_028'] = {'inputs': ['ced_basefill_028'], 'func': ced_base_universe_d2_038_ced_basefill_028}


def ced_base_universe_d2_039_ced_basefill_029(ced_basefill_029):
    return _base_universe_d2(ced_basefill_029, 39)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_039_ced_basefill_029'] = {'inputs': ['ced_basefill_029'], 'func': ced_base_universe_d2_039_ced_basefill_029}


def ced_base_universe_d2_040_ced_basefill_030(ced_basefill_030):
    return _base_universe_d2(ced_basefill_030, 40)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_040_ced_basefill_030'] = {'inputs': ['ced_basefill_030'], 'func': ced_base_universe_d2_040_ced_basefill_030}


def ced_base_universe_d2_041_ced_basefill_031(ced_basefill_031):
    return _base_universe_d2(ced_basefill_031, 41)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_041_ced_basefill_031'] = {'inputs': ['ced_basefill_031'], 'func': ced_base_universe_d2_041_ced_basefill_031}


def ced_base_universe_d2_042_ced_basefill_035(ced_basefill_035):
    return _base_universe_d2(ced_basefill_035, 42)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_042_ced_basefill_035'] = {'inputs': ['ced_basefill_035'], 'func': ced_base_universe_d2_042_ced_basefill_035}


def ced_base_universe_d2_043_ced_basefill_036(ced_basefill_036):
    return _base_universe_d2(ced_basefill_036, 43)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_043_ced_basefill_036'] = {'inputs': ['ced_basefill_036'], 'func': ced_base_universe_d2_043_ced_basefill_036}


def ced_base_universe_d2_044_ced_basefill_037(ced_basefill_037):
    return _base_universe_d2(ced_basefill_037, 44)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_044_ced_basefill_037'] = {'inputs': ['ced_basefill_037'], 'func': ced_base_universe_d2_044_ced_basefill_037}


def ced_base_universe_d2_045_ced_basefill_038(ced_basefill_038):
    return _base_universe_d2(ced_basefill_038, 45)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_045_ced_basefill_038'] = {'inputs': ['ced_basefill_038'], 'func': ced_base_universe_d2_045_ced_basefill_038}


def ced_base_universe_d2_046_ced_basefill_042(ced_basefill_042):
    return _base_universe_d2(ced_basefill_042, 46)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_046_ced_basefill_042'] = {'inputs': ['ced_basefill_042'], 'func': ced_base_universe_d2_046_ced_basefill_042}


def ced_base_universe_d2_047_ced_basefill_043(ced_basefill_043):
    return _base_universe_d2(ced_basefill_043, 47)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_047_ced_basefill_043'] = {'inputs': ['ced_basefill_043'], 'func': ced_base_universe_d2_047_ced_basefill_043}


def ced_base_universe_d2_048_ced_basefill_044(ced_basefill_044):
    return _base_universe_d2(ced_basefill_044, 48)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_048_ced_basefill_044'] = {'inputs': ['ced_basefill_044'], 'func': ced_base_universe_d2_048_ced_basefill_044}


def ced_base_universe_d2_049_ced_basefill_045(ced_basefill_045):
    return _base_universe_d2(ced_basefill_045, 49)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_049_ced_basefill_045'] = {'inputs': ['ced_basefill_045'], 'func': ced_base_universe_d2_049_ced_basefill_045}


def ced_base_universe_d2_050_ced_basefill_048(ced_basefill_048):
    return _base_universe_d2(ced_basefill_048, 50)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_050_ced_basefill_048'] = {'inputs': ['ced_basefill_048'], 'func': ced_base_universe_d2_050_ced_basefill_048}


def ced_base_universe_d2_051_ced_basefill_049(ced_basefill_049):
    return _base_universe_d2(ced_basefill_049, 51)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_051_ced_basefill_049'] = {'inputs': ['ced_basefill_049'], 'func': ced_base_universe_d2_051_ced_basefill_049}


def ced_base_universe_d2_052_ced_basefill_050(ced_basefill_050):
    return _base_universe_d2(ced_basefill_050, 52)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_052_ced_basefill_050'] = {'inputs': ['ced_basefill_050'], 'func': ced_base_universe_d2_052_ced_basefill_050}


def ced_base_universe_d2_053_ced_basefill_051(ced_basefill_051):
    return _base_universe_d2(ced_basefill_051, 53)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_053_ced_basefill_051'] = {'inputs': ['ced_basefill_051'], 'func': ced_base_universe_d2_053_ced_basefill_051}


def ced_base_universe_d2_054_ced_basefill_052(ced_basefill_052):
    return _base_universe_d2(ced_basefill_052, 54)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_054_ced_basefill_052'] = {'inputs': ['ced_basefill_052'], 'func': ced_base_universe_d2_054_ced_basefill_052}


def ced_base_universe_d2_055_ced_basefill_055(ced_basefill_055):
    return _base_universe_d2(ced_basefill_055, 55)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_055_ced_basefill_055'] = {'inputs': ['ced_basefill_055'], 'func': ced_base_universe_d2_055_ced_basefill_055}


def ced_base_universe_d2_056_ced_basefill_056(ced_basefill_056):
    return _base_universe_d2(ced_basefill_056, 56)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_056_ced_basefill_056'] = {'inputs': ['ced_basefill_056'], 'func': ced_base_universe_d2_056_ced_basefill_056}


def ced_base_universe_d2_057_ced_basefill_057(ced_basefill_057):
    return _base_universe_d2(ced_basefill_057, 57)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_057_ced_basefill_057'] = {'inputs': ['ced_basefill_057'], 'func': ced_base_universe_d2_057_ced_basefill_057}


def ced_base_universe_d2_058_ced_basefill_058(ced_basefill_058):
    return _base_universe_d2(ced_basefill_058, 58)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_058_ced_basefill_058'] = {'inputs': ['ced_basefill_058'], 'func': ced_base_universe_d2_058_ced_basefill_058}


def ced_base_universe_d2_059_ced_basefill_059(ced_basefill_059):
    return _base_universe_d2(ced_basefill_059, 59)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_059_ced_basefill_059'] = {'inputs': ['ced_basefill_059'], 'func': ced_base_universe_d2_059_ced_basefill_059}


def ced_base_universe_d2_060_ced_basefill_062(ced_basefill_062):
    return _base_universe_d2(ced_basefill_062, 60)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_060_ced_basefill_062'] = {'inputs': ['ced_basefill_062'], 'func': ced_base_universe_d2_060_ced_basefill_062}


def ced_base_universe_d2_061_ced_basefill_063(ced_basefill_063):
    return _base_universe_d2(ced_basefill_063, 61)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_061_ced_basefill_063'] = {'inputs': ['ced_basefill_063'], 'func': ced_base_universe_d2_061_ced_basefill_063}


def ced_base_universe_d2_062_ced_basefill_064(ced_basefill_064):
    return _base_universe_d2(ced_basefill_064, 62)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_062_ced_basefill_064'] = {'inputs': ['ced_basefill_064'], 'func': ced_base_universe_d2_062_ced_basefill_064}


def ced_base_universe_d2_063_ced_basefill_065(ced_basefill_065):
    return _base_universe_d2(ced_basefill_065, 63)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_063_ced_basefill_065'] = {'inputs': ['ced_basefill_065'], 'func': ced_base_universe_d2_063_ced_basefill_065}


def ced_base_universe_d2_064_ced_basefill_066(ced_basefill_066):
    return _base_universe_d2(ced_basefill_066, 64)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_064_ced_basefill_066'] = {'inputs': ['ced_basefill_066'], 'func': ced_base_universe_d2_064_ced_basefill_066}


def ced_base_universe_d2_065_ced_basefill_067(ced_basefill_067):
    return _base_universe_d2(ced_basefill_067, 65)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_065_ced_basefill_067'] = {'inputs': ['ced_basefill_067'], 'func': ced_base_universe_d2_065_ced_basefill_067}


def ced_base_universe_d2_066_ced_basefill_069(ced_basefill_069):
    return _base_universe_d2(ced_basefill_069, 66)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_066_ced_basefill_069'] = {'inputs': ['ced_basefill_069'], 'func': ced_base_universe_d2_066_ced_basefill_069}


def ced_base_universe_d2_067_ced_basefill_070(ced_basefill_070):
    return _base_universe_d2(ced_basefill_070, 67)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_067_ced_basefill_070'] = {'inputs': ['ced_basefill_070'], 'func': ced_base_universe_d2_067_ced_basefill_070}


def ced_base_universe_d2_068_ced_basefill_071(ced_basefill_071):
    return _base_universe_d2(ced_basefill_071, 68)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_068_ced_basefill_071'] = {'inputs': ['ced_basefill_071'], 'func': ced_base_universe_d2_068_ced_basefill_071}


def ced_base_universe_d2_069_ced_basefill_072(ced_basefill_072):
    return _base_universe_d2(ced_basefill_072, 69)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_069_ced_basefill_072'] = {'inputs': ['ced_basefill_072'], 'func': ced_base_universe_d2_069_ced_basefill_072}


def ced_base_universe_d2_070_ced_basefill_073(ced_basefill_073):
    return _base_universe_d2(ced_basefill_073, 70)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_070_ced_basefill_073'] = {'inputs': ['ced_basefill_073'], 'func': ced_base_universe_d2_070_ced_basefill_073}


def ced_base_universe_d2_071_ced_basefill_074(ced_basefill_074):
    return _base_universe_d2(ced_basefill_074, 71)
CED_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ced_base_universe_d2_071_ced_basefill_074'] = {'inputs': ['ced_basefill_074'], 'func': ced_base_universe_d2_071_ced_basefill_074}
