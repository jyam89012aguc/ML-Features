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



def dvd_151_dvd_001_dividend_cut_density_21_roc_1(dvd_001_dividend_cut_density_21):
    feature = _s(dvd_001_dividend_cut_density_21)
    return (_roc(feature, 1)).reindex(feature.index)

def dvd_152_dvd_007_listing_tier_decay_1_roc_42(dvd_007_listing_tier_decay_1):
    feature = _s(dvd_007_listing_tier_decay_1)
    return (_roc(feature, 42)).reindex(feature.index)

def dvd_153_dvd_013_delisting_notice_density_1512_roc_126(dvd_013_delisting_notice_density_1512):
    feature = _s(dvd_013_delisting_notice_density_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def dvd_154_dvd_019_going_concern_persistence_84_roc_378(dvd_019_going_concern_persistence_84):
    feature = _s(dvd_019_going_concern_persistence_84)
    return (_roc(feature, 378)).reindex(feature.index)

def dvd_155_dvd_025_event_density_z_756_roc_4(dvd_025_event_density_z_756):
    feature = _s(dvd_025_event_density_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















DIVIDEND_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    'dvd_151_dvd_001_dividend_cut_density_21_roc_1': {'inputs': ['dvd_001_dividend_cut_density_21'], 'func': dvd_151_dvd_001_dividend_cut_density_21_roc_1},
    'dvd_152_dvd_007_listing_tier_decay_1_roc_42': {'inputs': ['dvd_007_listing_tier_decay_1'], 'func': dvd_152_dvd_007_listing_tier_decay_1_roc_42},
    'dvd_153_dvd_013_delisting_notice_density_1512_roc_126': {'inputs': ['dvd_013_delisting_notice_density_1512'], 'func': dvd_153_dvd_013_delisting_notice_density_1512_roc_126},
    'dvd_154_dvd_019_going_concern_persistence_84_roc_378': {'inputs': ['dvd_019_going_concern_persistence_84'], 'func': dvd_154_dvd_019_going_concern_persistence_84_roc_378},
    'dvd_155_dvd_025_event_density_z_756_roc_4': {'inputs': ['dvd_025_event_density_z_756'], 'func': dvd_155_dvd_025_event_density_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def dd_replacement_d2_001(dvd_007_listing_tier_decay_1):
    feature = _clean(dvd_007_listing_tier_decay_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_001'] = {'inputs': ['dvd_007_listing_tier_decay_1'], 'func': dd_replacement_d2_001}


def dd_replacement_d2_002(dd_replacement_001):
    feature = _clean(dd_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_002'] = {'inputs': ['dd_replacement_001'], 'func': dd_replacement_d2_002}


def dd_replacement_d2_003(dd_replacement_002):
    feature = _clean(dd_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_003'] = {'inputs': ['dd_replacement_002'], 'func': dd_replacement_d2_003}


def dd_replacement_d2_004(dd_replacement_003):
    feature = _clean(dd_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_004'] = {'inputs': ['dd_replacement_003'], 'func': dd_replacement_d2_004}


def dd_replacement_d2_005(dd_replacement_004):
    feature = _clean(dd_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_005'] = {'inputs': ['dd_replacement_004'], 'func': dd_replacement_d2_005}


def dd_replacement_d2_006(dd_replacement_005):
    feature = _clean(dd_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_006'] = {'inputs': ['dd_replacement_005'], 'func': dd_replacement_d2_006}


def dd_replacement_d2_007(dd_replacement_006):
    feature = _clean(dd_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_007'] = {'inputs': ['dd_replacement_006'], 'func': dd_replacement_d2_007}


def dd_replacement_d2_008(dd_replacement_007):
    feature = _clean(dd_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_008'] = {'inputs': ['dd_replacement_007'], 'func': dd_replacement_d2_008}


def dd_replacement_d2_009(dd_replacement_008):
    feature = _clean(dd_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_009'] = {'inputs': ['dd_replacement_008'], 'func': dd_replacement_d2_009}


def dd_replacement_d2_010(dd_replacement_009):
    feature = _clean(dd_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_010'] = {'inputs': ['dd_replacement_009'], 'func': dd_replacement_d2_010}


def dd_replacement_d2_011(dd_replacement_010):
    feature = _clean(dd_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_011'] = {'inputs': ['dd_replacement_010'], 'func': dd_replacement_d2_011}


def dd_replacement_d2_012(dd_replacement_011):
    feature = _clean(dd_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_012'] = {'inputs': ['dd_replacement_011'], 'func': dd_replacement_d2_012}


def dd_replacement_d2_013(dd_replacement_012):
    feature = _clean(dd_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_013'] = {'inputs': ['dd_replacement_012'], 'func': dd_replacement_d2_013}


def dd_replacement_d2_014(dd_replacement_013):
    feature = _clean(dd_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_014'] = {'inputs': ['dd_replacement_013'], 'func': dd_replacement_d2_014}


def dd_replacement_d2_015(dd_replacement_014):
    feature = _clean(dd_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_015'] = {'inputs': ['dd_replacement_014'], 'func': dd_replacement_d2_015}


def dd_replacement_d2_016(dd_replacement_015):
    feature = _clean(dd_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_016'] = {'inputs': ['dd_replacement_015'], 'func': dd_replacement_d2_016}


def dd_replacement_d2_017(dd_replacement_016):
    feature = _clean(dd_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_017'] = {'inputs': ['dd_replacement_016'], 'func': dd_replacement_d2_017}


def dd_replacement_d2_018(dd_replacement_017):
    feature = _clean(dd_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_018'] = {'inputs': ['dd_replacement_017'], 'func': dd_replacement_d2_018}


def dd_replacement_d2_019(dd_replacement_018):
    feature = _clean(dd_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_019'] = {'inputs': ['dd_replacement_018'], 'func': dd_replacement_d2_019}


def dd_replacement_d2_020(dd_replacement_019):
    feature = _clean(dd_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_020'] = {'inputs': ['dd_replacement_019'], 'func': dd_replacement_d2_020}


def dd_replacement_d2_021(dd_replacement_020):
    feature = _clean(dd_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_021'] = {'inputs': ['dd_replacement_020'], 'func': dd_replacement_d2_021}


def dd_replacement_d2_022(dd_replacement_021):
    feature = _clean(dd_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_022'] = {'inputs': ['dd_replacement_021'], 'func': dd_replacement_d2_022}


def dd_replacement_d2_023(dd_replacement_022):
    feature = _clean(dd_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_023'] = {'inputs': ['dd_replacement_022'], 'func': dd_replacement_d2_023}


def dd_replacement_d2_024(dd_replacement_023):
    feature = _clean(dd_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_024'] = {'inputs': ['dd_replacement_023'], 'func': dd_replacement_d2_024}


def dd_replacement_d2_025(dd_replacement_024):
    feature = _clean(dd_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_025'] = {'inputs': ['dd_replacement_024'], 'func': dd_replacement_d2_025}


def dd_replacement_d2_026(dd_replacement_025):
    feature = _clean(dd_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_026'] = {'inputs': ['dd_replacement_025'], 'func': dd_replacement_d2_026}


def dd_replacement_d2_027(dd_replacement_026):
    feature = _clean(dd_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_027'] = {'inputs': ['dd_replacement_026'], 'func': dd_replacement_d2_027}


def dd_replacement_d2_028(dd_replacement_027):
    feature = _clean(dd_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_028'] = {'inputs': ['dd_replacement_027'], 'func': dd_replacement_d2_028}


def dd_replacement_d2_029(dd_replacement_028):
    feature = _clean(dd_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_029'] = {'inputs': ['dd_replacement_028'], 'func': dd_replacement_d2_029}


def dd_replacement_d2_030(dd_replacement_029):
    feature = _clean(dd_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_030'] = {'inputs': ['dd_replacement_029'], 'func': dd_replacement_d2_030}


def dd_replacement_d2_031(dd_replacement_030):
    feature = _clean(dd_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_031'] = {'inputs': ['dd_replacement_030'], 'func': dd_replacement_d2_031}


def dd_replacement_d2_032(dd_replacement_031):
    feature = _clean(dd_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_032'] = {'inputs': ['dd_replacement_031'], 'func': dd_replacement_d2_032}


def dd_replacement_d2_033(dd_replacement_032):
    feature = _clean(dd_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_033'] = {'inputs': ['dd_replacement_032'], 'func': dd_replacement_d2_033}


def dd_replacement_d2_034(dd_replacement_033):
    feature = _clean(dd_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_034'] = {'inputs': ['dd_replacement_033'], 'func': dd_replacement_d2_034}


def dd_replacement_d2_035(dd_replacement_034):
    feature = _clean(dd_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_035'] = {'inputs': ['dd_replacement_034'], 'func': dd_replacement_d2_035}


def dd_replacement_d2_036(dd_replacement_035):
    feature = _clean(dd_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_036'] = {'inputs': ['dd_replacement_035'], 'func': dd_replacement_d2_036}


def dd_replacement_d2_037(dd_replacement_036):
    feature = _clean(dd_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_037'] = {'inputs': ['dd_replacement_036'], 'func': dd_replacement_d2_037}


def dd_replacement_d2_038(dd_replacement_037):
    feature = _clean(dd_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_038'] = {'inputs': ['dd_replacement_037'], 'func': dd_replacement_d2_038}


def dd_replacement_d2_039(dd_replacement_038):
    feature = _clean(dd_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_039'] = {'inputs': ['dd_replacement_038'], 'func': dd_replacement_d2_039}


def dd_replacement_d2_040(dd_replacement_039):
    feature = _clean(dd_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_040'] = {'inputs': ['dd_replacement_039'], 'func': dd_replacement_d2_040}


def dd_replacement_d2_041(dd_replacement_040):
    feature = _clean(dd_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_041'] = {'inputs': ['dd_replacement_040'], 'func': dd_replacement_d2_041}


def dd_replacement_d2_042(dd_replacement_041):
    feature = _clean(dd_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_042'] = {'inputs': ['dd_replacement_041'], 'func': dd_replacement_d2_042}


def dd_replacement_d2_043(dd_replacement_042):
    feature = _clean(dd_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_043'] = {'inputs': ['dd_replacement_042'], 'func': dd_replacement_d2_043}


def dd_replacement_d2_044(dd_replacement_043):
    feature = _clean(dd_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_044'] = {'inputs': ['dd_replacement_043'], 'func': dd_replacement_d2_044}


def dd_replacement_d2_045(dd_replacement_044):
    feature = _clean(dd_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_045'] = {'inputs': ['dd_replacement_044'], 'func': dd_replacement_d2_045}


def dd_replacement_d2_046(dd_replacement_045):
    feature = _clean(dd_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_046'] = {'inputs': ['dd_replacement_045'], 'func': dd_replacement_d2_046}


def dd_replacement_d2_047(dd_replacement_046):
    feature = _clean(dd_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_047'] = {'inputs': ['dd_replacement_046'], 'func': dd_replacement_d2_047}


def dd_replacement_d2_048(dd_replacement_047):
    feature = _clean(dd_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_048'] = {'inputs': ['dd_replacement_047'], 'func': dd_replacement_d2_048}


def dd_replacement_d2_049(dd_replacement_048):
    feature = _clean(dd_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_049'] = {'inputs': ['dd_replacement_048'], 'func': dd_replacement_d2_049}


def dd_replacement_d2_050(dd_replacement_049):
    feature = _clean(dd_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_050'] = {'inputs': ['dd_replacement_049'], 'func': dd_replacement_d2_050}


def dd_replacement_d2_051(dd_replacement_050):
    feature = _clean(dd_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_051'] = {'inputs': ['dd_replacement_050'], 'func': dd_replacement_d2_051}


def dd_replacement_d2_052(dd_replacement_051):
    feature = _clean(dd_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_052'] = {'inputs': ['dd_replacement_051'], 'func': dd_replacement_d2_052}


def dd_replacement_d2_053(dd_replacement_052):
    feature = _clean(dd_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_053'] = {'inputs': ['dd_replacement_052'], 'func': dd_replacement_d2_053}


def dd_replacement_d2_054(dd_replacement_053):
    feature = _clean(dd_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_054'] = {'inputs': ['dd_replacement_053'], 'func': dd_replacement_d2_054}


def dd_replacement_d2_055(dd_replacement_054):
    feature = _clean(dd_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_055'] = {'inputs': ['dd_replacement_054'], 'func': dd_replacement_d2_055}


def dd_replacement_d2_056(dd_replacement_055):
    feature = _clean(dd_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_056'] = {'inputs': ['dd_replacement_055'], 'func': dd_replacement_d2_056}


def dd_replacement_d2_057(dd_replacement_056):
    feature = _clean(dd_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_057'] = {'inputs': ['dd_replacement_056'], 'func': dd_replacement_d2_057}


def dd_replacement_d2_058(dd_replacement_057):
    feature = _clean(dd_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_058'] = {'inputs': ['dd_replacement_057'], 'func': dd_replacement_d2_058}


def dd_replacement_d2_059(dd_replacement_058):
    feature = _clean(dd_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_059'] = {'inputs': ['dd_replacement_058'], 'func': dd_replacement_d2_059}


def dd_replacement_d2_060(dd_replacement_059):
    feature = _clean(dd_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_060'] = {'inputs': ['dd_replacement_059'], 'func': dd_replacement_d2_060}


def dd_replacement_d2_061(dd_replacement_060):
    feature = _clean(dd_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_061'] = {'inputs': ['dd_replacement_060'], 'func': dd_replacement_d2_061}


def dd_replacement_d2_062(dd_replacement_061):
    feature = _clean(dd_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_062'] = {'inputs': ['dd_replacement_061'], 'func': dd_replacement_d2_062}


def dd_replacement_d2_063(dd_replacement_062):
    feature = _clean(dd_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_063'] = {'inputs': ['dd_replacement_062'], 'func': dd_replacement_d2_063}


def dd_replacement_d2_064(dd_replacement_063):
    feature = _clean(dd_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_064'] = {'inputs': ['dd_replacement_063'], 'func': dd_replacement_d2_064}


def dd_replacement_d2_065(dd_replacement_064):
    feature = _clean(dd_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_065'] = {'inputs': ['dd_replacement_064'], 'func': dd_replacement_d2_065}


def dd_replacement_d2_066(dd_replacement_065):
    feature = _clean(dd_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_066'] = {'inputs': ['dd_replacement_065'], 'func': dd_replacement_d2_066}


def dd_replacement_d2_067(dd_replacement_066):
    feature = _clean(dd_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_067'] = {'inputs': ['dd_replacement_066'], 'func': dd_replacement_d2_067}


def dd_replacement_d2_068(dd_replacement_067):
    feature = _clean(dd_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_068'] = {'inputs': ['dd_replacement_067'], 'func': dd_replacement_d2_068}


def dd_replacement_d2_069(dd_replacement_068):
    feature = _clean(dd_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_069'] = {'inputs': ['dd_replacement_068'], 'func': dd_replacement_d2_069}


def dd_replacement_d2_070(dd_replacement_069):
    feature = _clean(dd_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_070'] = {'inputs': ['dd_replacement_069'], 'func': dd_replacement_d2_070}


def dd_replacement_d2_071(dd_replacement_070):
    feature = _clean(dd_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_071'] = {'inputs': ['dd_replacement_070'], 'func': dd_replacement_d2_071}


def dd_replacement_d2_072(dd_replacement_071):
    feature = _clean(dd_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_072'] = {'inputs': ['dd_replacement_071'], 'func': dd_replacement_d2_072}


def dd_replacement_d2_073(dd_replacement_072):
    feature = _clean(dd_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_073'] = {'inputs': ['dd_replacement_072'], 'func': dd_replacement_d2_073}


def dd_replacement_d2_074(dd_replacement_073):
    feature = _clean(dd_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_074'] = {'inputs': ['dd_replacement_073'], 'func': dd_replacement_d2_074}


def dd_replacement_d2_075(dd_replacement_074):
    feature = _clean(dd_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_075'] = {'inputs': ['dd_replacement_074'], 'func': dd_replacement_d2_075}


def dd_replacement_d2_076(dd_replacement_075):
    feature = _clean(dd_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_076'] = {'inputs': ['dd_replacement_075'], 'func': dd_replacement_d2_076}


def dd_replacement_d2_077(dd_replacement_076):
    feature = _clean(dd_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_077'] = {'inputs': ['dd_replacement_076'], 'func': dd_replacement_d2_077}


def dd_replacement_d2_078(dd_replacement_077):
    feature = _clean(dd_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_078'] = {'inputs': ['dd_replacement_077'], 'func': dd_replacement_d2_078}


def dd_replacement_d2_079(dd_replacement_078):
    feature = _clean(dd_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_079'] = {'inputs': ['dd_replacement_078'], 'func': dd_replacement_d2_079}


def dd_replacement_d2_080(dd_replacement_079):
    feature = _clean(dd_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_080'] = {'inputs': ['dd_replacement_079'], 'func': dd_replacement_d2_080}


def dd_replacement_d2_081(dd_replacement_080):
    feature = _clean(dd_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_081'] = {'inputs': ['dd_replacement_080'], 'func': dd_replacement_d2_081}


def dd_replacement_d2_082(dd_replacement_081):
    feature = _clean(dd_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_082'] = {'inputs': ['dd_replacement_081'], 'func': dd_replacement_d2_082}


def dd_replacement_d2_083(dd_replacement_082):
    feature = _clean(dd_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_083'] = {'inputs': ['dd_replacement_082'], 'func': dd_replacement_d2_083}


def dd_replacement_d2_084(dd_replacement_083):
    feature = _clean(dd_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_084'] = {'inputs': ['dd_replacement_083'], 'func': dd_replacement_d2_084}


def dd_replacement_d2_085(dd_replacement_084):
    feature = _clean(dd_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_085'] = {'inputs': ['dd_replacement_084'], 'func': dd_replacement_d2_085}


def dd_replacement_d2_086(dd_replacement_085):
    feature = _clean(dd_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_086'] = {'inputs': ['dd_replacement_085'], 'func': dd_replacement_d2_086}


def dd_replacement_d2_087(dd_replacement_086):
    feature = _clean(dd_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_087'] = {'inputs': ['dd_replacement_086'], 'func': dd_replacement_d2_087}


def dd_replacement_d2_088(dd_replacement_087):
    feature = _clean(dd_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_088'] = {'inputs': ['dd_replacement_087'], 'func': dd_replacement_d2_088}


def dd_replacement_d2_089(dd_replacement_088):
    feature = _clean(dd_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_089'] = {'inputs': ['dd_replacement_088'], 'func': dd_replacement_d2_089}


def dd_replacement_d2_090(dd_replacement_089):
    feature = _clean(dd_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_090'] = {'inputs': ['dd_replacement_089'], 'func': dd_replacement_d2_090}


def dd_replacement_d2_091(dd_replacement_090):
    feature = _clean(dd_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_091'] = {'inputs': ['dd_replacement_090'], 'func': dd_replacement_d2_091}


def dd_replacement_d2_092(dd_replacement_091):
    feature = _clean(dd_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_092'] = {'inputs': ['dd_replacement_091'], 'func': dd_replacement_d2_092}


def dd_replacement_d2_093(dd_replacement_092):
    feature = _clean(dd_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_093'] = {'inputs': ['dd_replacement_092'], 'func': dd_replacement_d2_093}


def dd_replacement_d2_094(dd_replacement_093):
    feature = _clean(dd_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_094'] = {'inputs': ['dd_replacement_093'], 'func': dd_replacement_d2_094}


def dd_replacement_d2_095(dd_replacement_094):
    feature = _clean(dd_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_095'] = {'inputs': ['dd_replacement_094'], 'func': dd_replacement_d2_095}


def dd_replacement_d2_096(dd_replacement_095):
    feature = _clean(dd_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_096'] = {'inputs': ['dd_replacement_095'], 'func': dd_replacement_d2_096}


def dd_replacement_d2_097(dd_replacement_096):
    feature = _clean(dd_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_097'] = {'inputs': ['dd_replacement_096'], 'func': dd_replacement_d2_097}


def dd_replacement_d2_098(dd_replacement_097):
    feature = _clean(dd_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_098'] = {'inputs': ['dd_replacement_097'], 'func': dd_replacement_d2_098}


def dd_replacement_d2_099(dd_replacement_098):
    feature = _clean(dd_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_099'] = {'inputs': ['dd_replacement_098'], 'func': dd_replacement_d2_099}


def dd_replacement_d2_100(dd_replacement_099):
    feature = _clean(dd_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_100'] = {'inputs': ['dd_replacement_099'], 'func': dd_replacement_d2_100}


def dd_replacement_d2_101(dd_replacement_100):
    feature = _clean(dd_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_101'] = {'inputs': ['dd_replacement_100'], 'func': dd_replacement_d2_101}


def dd_replacement_d2_102(dd_replacement_101):
    feature = _clean(dd_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_102'] = {'inputs': ['dd_replacement_101'], 'func': dd_replacement_d2_102}


def dd_replacement_d2_103(dd_replacement_102):
    feature = _clean(dd_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_103'] = {'inputs': ['dd_replacement_102'], 'func': dd_replacement_d2_103}


def dd_replacement_d2_104(dd_replacement_103):
    feature = _clean(dd_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_104'] = {'inputs': ['dd_replacement_103'], 'func': dd_replacement_d2_104}


def dd_replacement_d2_105(dd_replacement_104):
    feature = _clean(dd_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_105'] = {'inputs': ['dd_replacement_104'], 'func': dd_replacement_d2_105}


def dd_replacement_d2_106(dd_replacement_105):
    feature = _clean(dd_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_106'] = {'inputs': ['dd_replacement_105'], 'func': dd_replacement_d2_106}


def dd_replacement_d2_107(dd_replacement_106):
    feature = _clean(dd_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_107'] = {'inputs': ['dd_replacement_106'], 'func': dd_replacement_d2_107}


def dd_replacement_d2_108(dd_replacement_107):
    feature = _clean(dd_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_108'] = {'inputs': ['dd_replacement_107'], 'func': dd_replacement_d2_108}


def dd_replacement_d2_109(dd_replacement_108):
    feature = _clean(dd_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_109'] = {'inputs': ['dd_replacement_108'], 'func': dd_replacement_d2_109}


def dd_replacement_d2_110(dd_replacement_109):
    feature = _clean(dd_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_110'] = {'inputs': ['dd_replacement_109'], 'func': dd_replacement_d2_110}


def dd_replacement_d2_111(dd_replacement_110):
    feature = _clean(dd_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_111'] = {'inputs': ['dd_replacement_110'], 'func': dd_replacement_d2_111}


def dd_replacement_d2_112(dd_replacement_111):
    feature = _clean(dd_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_112'] = {'inputs': ['dd_replacement_111'], 'func': dd_replacement_d2_112}


def dd_replacement_d2_113(dd_replacement_112):
    feature = _clean(dd_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_113'] = {'inputs': ['dd_replacement_112'], 'func': dd_replacement_d2_113}


def dd_replacement_d2_114(dd_replacement_113):
    feature = _clean(dd_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_114'] = {'inputs': ['dd_replacement_113'], 'func': dd_replacement_d2_114}


def dd_replacement_d2_115(dd_replacement_114):
    feature = _clean(dd_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_115'] = {'inputs': ['dd_replacement_114'], 'func': dd_replacement_d2_115}


def dd_replacement_d2_116(dd_replacement_115):
    feature = _clean(dd_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_116'] = {'inputs': ['dd_replacement_115'], 'func': dd_replacement_d2_116}


def dd_replacement_d2_117(dd_replacement_116):
    feature = _clean(dd_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_117'] = {'inputs': ['dd_replacement_116'], 'func': dd_replacement_d2_117}


def dd_replacement_d2_118(dd_replacement_117):
    feature = _clean(dd_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_118'] = {'inputs': ['dd_replacement_117'], 'func': dd_replacement_d2_118}


def dd_replacement_d2_119(dd_replacement_118):
    feature = _clean(dd_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_119'] = {'inputs': ['dd_replacement_118'], 'func': dd_replacement_d2_119}


def dd_replacement_d2_120(dd_replacement_119):
    feature = _clean(dd_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_120'] = {'inputs': ['dd_replacement_119'], 'func': dd_replacement_d2_120}


def dd_replacement_d2_121(dd_replacement_120):
    feature = _clean(dd_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_121'] = {'inputs': ['dd_replacement_120'], 'func': dd_replacement_d2_121}


def dd_replacement_d2_122(dd_replacement_121):
    feature = _clean(dd_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_122'] = {'inputs': ['dd_replacement_121'], 'func': dd_replacement_d2_122}


def dd_replacement_d2_123(dd_replacement_122):
    feature = _clean(dd_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_123'] = {'inputs': ['dd_replacement_122'], 'func': dd_replacement_d2_123}


def dd_replacement_d2_124(dd_replacement_123):
    feature = _clean(dd_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_124'] = {'inputs': ['dd_replacement_123'], 'func': dd_replacement_d2_124}


def dd_replacement_d2_125(dd_replacement_124):
    feature = _clean(dd_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_125'] = {'inputs': ['dd_replacement_124'], 'func': dd_replacement_d2_125}


def dd_replacement_d2_126(dd_replacement_125):
    feature = _clean(dd_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_126'] = {'inputs': ['dd_replacement_125'], 'func': dd_replacement_d2_126}


def dd_replacement_d2_127(dd_replacement_126):
    feature = _clean(dd_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_127'] = {'inputs': ['dd_replacement_126'], 'func': dd_replacement_d2_127}


def dd_replacement_d2_128(dd_replacement_127):
    feature = _clean(dd_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_128'] = {'inputs': ['dd_replacement_127'], 'func': dd_replacement_d2_128}


def dd_replacement_d2_129(dd_replacement_128):
    feature = _clean(dd_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_129'] = {'inputs': ['dd_replacement_128'], 'func': dd_replacement_d2_129}


def dd_replacement_d2_130(dd_replacement_129):
    feature = _clean(dd_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_130'] = {'inputs': ['dd_replacement_129'], 'func': dd_replacement_d2_130}


def dd_replacement_d2_131(dd_replacement_130):
    feature = _clean(dd_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_131'] = {'inputs': ['dd_replacement_130'], 'func': dd_replacement_d2_131}


def dd_replacement_d2_132(dd_replacement_131):
    feature = _clean(dd_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_132'] = {'inputs': ['dd_replacement_131'], 'func': dd_replacement_d2_132}


def dd_replacement_d2_133(dd_replacement_132):
    feature = _clean(dd_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_133'] = {'inputs': ['dd_replacement_132'], 'func': dd_replacement_d2_133}


def dd_replacement_d2_134(dd_replacement_133):
    feature = _clean(dd_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_134'] = {'inputs': ['dd_replacement_133'], 'func': dd_replacement_d2_134}


def dd_replacement_d2_135(dd_replacement_134):
    feature = _clean(dd_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_135'] = {'inputs': ['dd_replacement_134'], 'func': dd_replacement_d2_135}


def dd_replacement_d2_136(dd_replacement_135):
    feature = _clean(dd_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_136'] = {'inputs': ['dd_replacement_135'], 'func': dd_replacement_d2_136}


def dd_replacement_d2_137(dd_replacement_136):
    feature = _clean(dd_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_137'] = {'inputs': ['dd_replacement_136'], 'func': dd_replacement_d2_137}


def dd_replacement_d2_138(dd_replacement_137):
    feature = _clean(dd_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_138'] = {'inputs': ['dd_replacement_137'], 'func': dd_replacement_d2_138}


def dd_replacement_d2_139(dd_replacement_138):
    feature = _clean(dd_replacement_138)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_139'] = {'inputs': ['dd_replacement_138'], 'func': dd_replacement_d2_139}


def dd_replacement_d2_140(dd_replacement_139):
    feature = _clean(dd_replacement_139)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_140'] = {'inputs': ['dd_replacement_139'], 'func': dd_replacement_d2_140}


def dd_replacement_d2_141(dd_replacement_140):
    feature = _clean(dd_replacement_140)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_141'] = {'inputs': ['dd_replacement_140'], 'func': dd_replacement_d2_141}


def dd_replacement_d2_142(dd_replacement_141):
    feature = _clean(dd_replacement_141)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_142'] = {'inputs': ['dd_replacement_141'], 'func': dd_replacement_d2_142}


def dd_replacement_d2_143(dd_replacement_142):
    feature = _clean(dd_replacement_142)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_143'] = {'inputs': ['dd_replacement_142'], 'func': dd_replacement_d2_143}


def dd_replacement_d2_144(dd_replacement_143):
    feature = _clean(dd_replacement_143)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_144'] = {'inputs': ['dd_replacement_143'], 'func': dd_replacement_d2_144}


def dd_replacement_d2_145(dd_replacement_144):
    feature = _clean(dd_replacement_144)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_145'] = {'inputs': ['dd_replacement_144'], 'func': dd_replacement_d2_145}


def dd_replacement_d2_146(dd_replacement_145):
    feature = _clean(dd_replacement_145)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_146'] = {'inputs': ['dd_replacement_145'], 'func': dd_replacement_d2_146}


def dd_replacement_d2_147(dd_replacement_146):
    feature = _clean(dd_replacement_146)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_147'] = {'inputs': ['dd_replacement_146'], 'func': dd_replacement_d2_147}


def dd_replacement_d2_148(dd_replacement_147):
    feature = _clean(dd_replacement_147)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_148'] = {'inputs': ['dd_replacement_147'], 'func': dd_replacement_d2_148}


def dd_replacement_d2_149(dd_replacement_148):
    feature = _clean(dd_replacement_148)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_149'] = {'inputs': ['dd_replacement_148'], 'func': dd_replacement_d2_149}


def dd_replacement_d2_150(dd_replacement_149):
    feature = _clean(dd_replacement_149)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_150'] = {'inputs': ['dd_replacement_149'], 'func': dd_replacement_d2_150}


def dd_replacement_d2_151(dd_replacement_150):
    feature = _clean(dd_replacement_150)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_151'] = {'inputs': ['dd_replacement_150'], 'func': dd_replacement_d2_151}


# Base-universe derivative extensions for repaired first-base features.
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dvd_base_universe_d2_001_dvd_002_dividend_suspension_density_42(dvd_002_dividend_suspension_density_42):
    return _base_universe_d2(dvd_002_dividend_suspension_density_42, 1)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_001_dvd_002_dividend_suspension_density_42'] = {'inputs': ['dvd_002_dividend_suspension_density_42'], 'func': dvd_base_universe_d2_001_dvd_002_dividend_suspension_density_42}


def dvd_base_universe_d2_002_dvd_003_reverse_split_density_63(dvd_003_reverse_split_density_63):
    return _base_universe_d2(dvd_003_reverse_split_density_63, 2)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_002_dvd_003_reverse_split_density_63'] = {'inputs': ['dvd_003_reverse_split_density_63'], 'func': dvd_base_universe_d2_002_dvd_003_reverse_split_density_63}


def dvd_base_universe_d2_003_dvd_004_event_density_z_84(dvd_004_event_density_z_84):
    return _base_universe_d2(dvd_004_event_density_z_84, 3)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_003_dvd_004_event_density_z_84'] = {'inputs': ['dvd_004_event_density_z_84'], 'func': dvd_base_universe_d2_003_dvd_004_event_density_z_84}


def dvd_base_universe_d2_004_dvd_005_going_concern_persistence_126(dvd_005_going_concern_persistence_126):
    return _base_universe_d2(dvd_005_going_concern_persistence_126, 4)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_004_dvd_005_going_concern_persistence_126'] = {'inputs': ['dvd_005_going_concern_persistence_126'], 'func': dvd_base_universe_d2_004_dvd_005_going_concern_persistence_126}


def dvd_base_universe_d2_005_dvd_006_delisting_notice_density_189(dvd_006_delisting_notice_density_189):
    return _base_universe_d2(dvd_006_delisting_notice_density_189, 5)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_005_dvd_006_delisting_notice_density_189'] = {'inputs': ['dvd_006_delisting_notice_density_189'], 'func': dvd_base_universe_d2_005_dvd_006_delisting_notice_density_189}


def dvd_base_universe_d2_006_dvd_008_dividend_cut_density_378(dvd_008_dividend_cut_density_378):
    return _base_universe_d2(dvd_008_dividend_cut_density_378, 6)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_006_dvd_008_dividend_cut_density_378'] = {'inputs': ['dvd_008_dividend_cut_density_378'], 'func': dvd_base_universe_d2_006_dvd_008_dividend_cut_density_378}


def dvd_base_universe_d2_007_dvd_009_dividend_suspension_density_504(dvd_009_dividend_suspension_density_504):
    return _base_universe_d2(dvd_009_dividend_suspension_density_504, 7)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_007_dvd_009_dividend_suspension_density_504'] = {'inputs': ['dvd_009_dividend_suspension_density_504'], 'func': dvd_base_universe_d2_007_dvd_009_dividend_suspension_density_504}


def dvd_base_universe_d2_008_dvd_010_reverse_split_density_756(dvd_010_reverse_split_density_756):
    return _base_universe_d2(dvd_010_reverse_split_density_756, 8)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_008_dvd_010_reverse_split_density_756'] = {'inputs': ['dvd_010_reverse_split_density_756'], 'func': dvd_base_universe_d2_008_dvd_010_reverse_split_density_756}


def dvd_base_universe_d2_009_dvd_011_event_density_z_1008(dvd_011_event_density_z_1008):
    return _base_universe_d2(dvd_011_event_density_z_1008, 9)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_009_dvd_011_event_density_z_1008'] = {'inputs': ['dvd_011_event_density_z_1008'], 'func': dvd_base_universe_d2_009_dvd_011_event_density_z_1008}


def dvd_base_universe_d2_010_dvd_012_going_concern_persistence_1260(dvd_012_going_concern_persistence_1260):
    return _base_universe_d2(dvd_012_going_concern_persistence_1260, 10)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_010_dvd_012_going_concern_persistence_1260'] = {'inputs': ['dvd_012_going_concern_persistence_1260'], 'func': dvd_base_universe_d2_010_dvd_012_going_concern_persistence_1260}


def dvd_base_universe_d2_011_dvd_015_dividend_cut_density_252(dvd_015_dividend_cut_density_252):
    return _base_universe_d2(dvd_015_dividend_cut_density_252, 11)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_011_dvd_015_dividend_cut_density_252'] = {'inputs': ['dvd_015_dividend_cut_density_252'], 'func': dvd_base_universe_d2_011_dvd_015_dividend_cut_density_252}


def dvd_base_universe_d2_012_dvd_018_event_density_z_63(dvd_018_event_density_z_63):
    return _base_universe_d2(dvd_018_event_density_z_63, 12)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_012_dvd_018_event_density_z_63'] = {'inputs': ['dvd_018_event_density_z_63'], 'func': dvd_base_universe_d2_012_dvd_018_event_density_z_63}


def dvd_base_universe_d2_013_dvd_020_delisting_notice_density_126(dvd_020_delisting_notice_density_126):
    return _base_universe_d2(dvd_020_delisting_notice_density_126, 13)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_013_dvd_020_delisting_notice_density_126'] = {'inputs': ['dvd_020_delisting_notice_density_126'], 'func': dvd_base_universe_d2_013_dvd_020_delisting_notice_density_126}


def dvd_base_universe_d2_014_dvd_026_going_concern_persistence_1008(dvd_026_going_concern_persistence_1008):
    return _base_universe_d2(dvd_026_going_concern_persistence_1008, 14)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_014_dvd_026_going_concern_persistence_1008'] = {'inputs': ['dvd_026_going_concern_persistence_1008'], 'func': dvd_base_universe_d2_014_dvd_026_going_concern_persistence_1008}


def dvd_base_universe_d2_015_dvd_027_delisting_notice_density_1260(dvd_027_delisting_notice_density_1260):
    return _base_universe_d2(dvd_027_delisting_notice_density_1260, 15)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_015_dvd_027_delisting_notice_density_1260'] = {'inputs': ['dvd_027_delisting_notice_density_1260'], 'func': dvd_base_universe_d2_015_dvd_027_delisting_notice_density_1260}


def dvd_base_universe_d2_016_dvd_032_event_density_z_42(dvd_032_event_density_z_42):
    return _base_universe_d2(dvd_032_event_density_z_42, 16)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_016_dvd_032_event_density_z_42'] = {'inputs': ['dvd_032_event_density_z_42'], 'func': dvd_base_universe_d2_016_dvd_032_event_density_z_42}


def dvd_base_universe_d2_017_dvd_033_going_concern_persistence_63(dvd_033_going_concern_persistence_63):
    return _base_universe_d2(dvd_033_going_concern_persistence_63, 17)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_017_dvd_033_going_concern_persistence_63'] = {'inputs': ['dvd_033_going_concern_persistence_63'], 'func': dvd_base_universe_d2_017_dvd_033_going_concern_persistence_63}


def dvd_base_universe_d2_018_dvd_034_delisting_notice_density_84(dvd_034_delisting_notice_density_84):
    return _base_universe_d2(dvd_034_delisting_notice_density_84, 18)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_018_dvd_034_delisting_notice_density_84'] = {'inputs': ['dvd_034_delisting_notice_density_84'], 'func': dvd_base_universe_d2_018_dvd_034_delisting_notice_density_84}


def dvd_base_universe_d2_019_dvd_039_event_density_z_504(dvd_039_event_density_z_504):
    return _base_universe_d2(dvd_039_event_density_z_504, 19)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_019_dvd_039_event_density_z_504'] = {'inputs': ['dvd_039_event_density_z_504'], 'func': dvd_base_universe_d2_019_dvd_039_event_density_z_504}


def dvd_base_universe_d2_020_dvd_040_going_concern_persistence_756(dvd_040_going_concern_persistence_756):
    return _base_universe_d2(dvd_040_going_concern_persistence_756, 20)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_020_dvd_040_going_concern_persistence_756'] = {'inputs': ['dvd_040_going_concern_persistence_756'], 'func': dvd_base_universe_d2_020_dvd_040_going_concern_persistence_756}


def dvd_base_universe_d2_021_dvd_041_delisting_notice_density_1008(dvd_041_delisting_notice_density_1008):
    return _base_universe_d2(dvd_041_delisting_notice_density_1008, 21)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_021_dvd_041_delisting_notice_density_1008'] = {'inputs': ['dvd_041_delisting_notice_density_1008'], 'func': dvd_base_universe_d2_021_dvd_041_delisting_notice_density_1008}


def dvd_base_universe_d2_022_dvd_046_event_density_z_21(dvd_046_event_density_z_21):
    return _base_universe_d2(dvd_046_event_density_z_21, 22)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_022_dvd_046_event_density_z_21'] = {'inputs': ['dvd_046_event_density_z_21'], 'func': dvd_base_universe_d2_022_dvd_046_event_density_z_21}


def dvd_base_universe_d2_023_dvd_047_going_concern_persistence_42(dvd_047_going_concern_persistence_42):
    return _base_universe_d2(dvd_047_going_concern_persistence_42, 23)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_023_dvd_047_going_concern_persistence_42'] = {'inputs': ['dvd_047_going_concern_persistence_42'], 'func': dvd_base_universe_d2_023_dvd_047_going_concern_persistence_42}


def dvd_base_universe_d2_024_dvd_053_event_density_z_378(dvd_053_event_density_z_378):
    return _base_universe_d2(dvd_053_event_density_z_378, 24)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_024_dvd_053_event_density_z_378'] = {'inputs': ['dvd_053_event_density_z_378'], 'func': dvd_base_universe_d2_024_dvd_053_event_density_z_378}


def dvd_base_universe_d2_025_dvd_054_going_concern_persistence_504(dvd_054_going_concern_persistence_504):
    return _base_universe_d2(dvd_054_going_concern_persistence_504, 25)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_025_dvd_054_going_concern_persistence_504'] = {'inputs': ['dvd_054_going_concern_persistence_504'], 'func': dvd_base_universe_d2_025_dvd_054_going_concern_persistence_504}


def dvd_base_universe_d2_026_dvd_060_event_density_z_252(dvd_060_event_density_z_252):
    return _base_universe_d2(dvd_060_event_density_z_252, 26)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_026_dvd_060_event_density_z_252'] = {'inputs': ['dvd_060_event_density_z_252'], 'func': dvd_base_universe_d2_026_dvd_060_event_density_z_252}


def dvd_base_universe_d2_027_dvd_061_going_concern_persistence_21(dvd_061_going_concern_persistence_21):
    return _base_universe_d2(dvd_061_going_concern_persistence_21, 27)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_027_dvd_061_going_concern_persistence_21'] = {'inputs': ['dvd_061_going_concern_persistence_21'], 'func': dvd_base_universe_d2_027_dvd_061_going_concern_persistence_21}


def dvd_base_universe_d2_028_dvd_068_going_concern_persistence_378(dvd_068_going_concern_persistence_378):
    return _base_universe_d2(dvd_068_going_concern_persistence_378, 28)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_028_dvd_068_going_concern_persistence_378'] = {'inputs': ['dvd_068_going_concern_persistence_378'], 'func': dvd_base_universe_d2_028_dvd_068_going_concern_persistence_378}


def dvd_base_universe_d2_029_dvd_075_going_concern_persistence_252(dvd_075_going_concern_persistence_252):
    return _base_universe_d2(dvd_075_going_concern_persistence_252, 29)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_029_dvd_075_going_concern_persistence_252'] = {'inputs': ['dvd_075_going_concern_persistence_252'], 'func': dvd_base_universe_d2_029_dvd_075_going_concern_persistence_252}


def dvd_base_universe_d2_030_dvd_basefill_007(dvd_basefill_007):
    return _base_universe_d2(dvd_basefill_007, 30)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_030_dvd_basefill_007'] = {'inputs': ['dvd_basefill_007'], 'func': dvd_base_universe_d2_030_dvd_basefill_007}


def dvd_base_universe_d2_031_dvd_basefill_014(dvd_basefill_014):
    return _base_universe_d2(dvd_basefill_014, 31)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_031_dvd_basefill_014'] = {'inputs': ['dvd_basefill_014'], 'func': dvd_base_universe_d2_031_dvd_basefill_014}


def dvd_base_universe_d2_032_dvd_basefill_016(dvd_basefill_016):
    return _base_universe_d2(dvd_basefill_016, 32)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_032_dvd_basefill_016'] = {'inputs': ['dvd_basefill_016'], 'func': dvd_base_universe_d2_032_dvd_basefill_016}


def dvd_base_universe_d2_033_dvd_basefill_017(dvd_basefill_017):
    return _base_universe_d2(dvd_basefill_017, 33)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_033_dvd_basefill_017'] = {'inputs': ['dvd_basefill_017'], 'func': dvd_base_universe_d2_033_dvd_basefill_017}


def dvd_base_universe_d2_034_dvd_basefill_021(dvd_basefill_021):
    return _base_universe_d2(dvd_basefill_021, 34)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_034_dvd_basefill_021'] = {'inputs': ['dvd_basefill_021'], 'func': dvd_base_universe_d2_034_dvd_basefill_021}


def dvd_base_universe_d2_035_dvd_basefill_022(dvd_basefill_022):
    return _base_universe_d2(dvd_basefill_022, 35)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_035_dvd_basefill_022'] = {'inputs': ['dvd_basefill_022'], 'func': dvd_base_universe_d2_035_dvd_basefill_022}


def dvd_base_universe_d2_036_dvd_basefill_023(dvd_basefill_023):
    return _base_universe_d2(dvd_basefill_023, 36)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_036_dvd_basefill_023'] = {'inputs': ['dvd_basefill_023'], 'func': dvd_base_universe_d2_036_dvd_basefill_023}


def dvd_base_universe_d2_037_dvd_basefill_024(dvd_basefill_024):
    return _base_universe_d2(dvd_basefill_024, 37)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_037_dvd_basefill_024'] = {'inputs': ['dvd_basefill_024'], 'func': dvd_base_universe_d2_037_dvd_basefill_024}


def dvd_base_universe_d2_038_dvd_basefill_028(dvd_basefill_028):
    return _base_universe_d2(dvd_basefill_028, 38)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_038_dvd_basefill_028'] = {'inputs': ['dvd_basefill_028'], 'func': dvd_base_universe_d2_038_dvd_basefill_028}


def dvd_base_universe_d2_039_dvd_basefill_029(dvd_basefill_029):
    return _base_universe_d2(dvd_basefill_029, 39)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_039_dvd_basefill_029'] = {'inputs': ['dvd_basefill_029'], 'func': dvd_base_universe_d2_039_dvd_basefill_029}


def dvd_base_universe_d2_040_dvd_basefill_030(dvd_basefill_030):
    return _base_universe_d2(dvd_basefill_030, 40)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_040_dvd_basefill_030'] = {'inputs': ['dvd_basefill_030'], 'func': dvd_base_universe_d2_040_dvd_basefill_030}


def dvd_base_universe_d2_041_dvd_basefill_031(dvd_basefill_031):
    return _base_universe_d2(dvd_basefill_031, 41)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_041_dvd_basefill_031'] = {'inputs': ['dvd_basefill_031'], 'func': dvd_base_universe_d2_041_dvd_basefill_031}


def dvd_base_universe_d2_042_dvd_basefill_035(dvd_basefill_035):
    return _base_universe_d2(dvd_basefill_035, 42)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_042_dvd_basefill_035'] = {'inputs': ['dvd_basefill_035'], 'func': dvd_base_universe_d2_042_dvd_basefill_035}


def dvd_base_universe_d2_043_dvd_basefill_036(dvd_basefill_036):
    return _base_universe_d2(dvd_basefill_036, 43)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_043_dvd_basefill_036'] = {'inputs': ['dvd_basefill_036'], 'func': dvd_base_universe_d2_043_dvd_basefill_036}


def dvd_base_universe_d2_044_dvd_basefill_037(dvd_basefill_037):
    return _base_universe_d2(dvd_basefill_037, 44)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_044_dvd_basefill_037'] = {'inputs': ['dvd_basefill_037'], 'func': dvd_base_universe_d2_044_dvd_basefill_037}


def dvd_base_universe_d2_045_dvd_basefill_038(dvd_basefill_038):
    return _base_universe_d2(dvd_basefill_038, 45)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_045_dvd_basefill_038'] = {'inputs': ['dvd_basefill_038'], 'func': dvd_base_universe_d2_045_dvd_basefill_038}


def dvd_base_universe_d2_046_dvd_basefill_042(dvd_basefill_042):
    return _base_universe_d2(dvd_basefill_042, 46)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_046_dvd_basefill_042'] = {'inputs': ['dvd_basefill_042'], 'func': dvd_base_universe_d2_046_dvd_basefill_042}


def dvd_base_universe_d2_047_dvd_basefill_043(dvd_basefill_043):
    return _base_universe_d2(dvd_basefill_043, 47)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_047_dvd_basefill_043'] = {'inputs': ['dvd_basefill_043'], 'func': dvd_base_universe_d2_047_dvd_basefill_043}


def dvd_base_universe_d2_048_dvd_basefill_044(dvd_basefill_044):
    return _base_universe_d2(dvd_basefill_044, 48)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_048_dvd_basefill_044'] = {'inputs': ['dvd_basefill_044'], 'func': dvd_base_universe_d2_048_dvd_basefill_044}


def dvd_base_universe_d2_049_dvd_basefill_045(dvd_basefill_045):
    return _base_universe_d2(dvd_basefill_045, 49)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_049_dvd_basefill_045'] = {'inputs': ['dvd_basefill_045'], 'func': dvd_base_universe_d2_049_dvd_basefill_045}


def dvd_base_universe_d2_050_dvd_basefill_048(dvd_basefill_048):
    return _base_universe_d2(dvd_basefill_048, 50)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_050_dvd_basefill_048'] = {'inputs': ['dvd_basefill_048'], 'func': dvd_base_universe_d2_050_dvd_basefill_048}


def dvd_base_universe_d2_051_dvd_basefill_049(dvd_basefill_049):
    return _base_universe_d2(dvd_basefill_049, 51)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_051_dvd_basefill_049'] = {'inputs': ['dvd_basefill_049'], 'func': dvd_base_universe_d2_051_dvd_basefill_049}


def dvd_base_universe_d2_052_dvd_basefill_050(dvd_basefill_050):
    return _base_universe_d2(dvd_basefill_050, 52)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_052_dvd_basefill_050'] = {'inputs': ['dvd_basefill_050'], 'func': dvd_base_universe_d2_052_dvd_basefill_050}


def dvd_base_universe_d2_053_dvd_basefill_051(dvd_basefill_051):
    return _base_universe_d2(dvd_basefill_051, 53)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_053_dvd_basefill_051'] = {'inputs': ['dvd_basefill_051'], 'func': dvd_base_universe_d2_053_dvd_basefill_051}


def dvd_base_universe_d2_054_dvd_basefill_052(dvd_basefill_052):
    return _base_universe_d2(dvd_basefill_052, 54)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_054_dvd_basefill_052'] = {'inputs': ['dvd_basefill_052'], 'func': dvd_base_universe_d2_054_dvd_basefill_052}


def dvd_base_universe_d2_055_dvd_basefill_055(dvd_basefill_055):
    return _base_universe_d2(dvd_basefill_055, 55)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_055_dvd_basefill_055'] = {'inputs': ['dvd_basefill_055'], 'func': dvd_base_universe_d2_055_dvd_basefill_055}


def dvd_base_universe_d2_056_dvd_basefill_056(dvd_basefill_056):
    return _base_universe_d2(dvd_basefill_056, 56)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_056_dvd_basefill_056'] = {'inputs': ['dvd_basefill_056'], 'func': dvd_base_universe_d2_056_dvd_basefill_056}


def dvd_base_universe_d2_057_dvd_basefill_057(dvd_basefill_057):
    return _base_universe_d2(dvd_basefill_057, 57)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_057_dvd_basefill_057'] = {'inputs': ['dvd_basefill_057'], 'func': dvd_base_universe_d2_057_dvd_basefill_057}


def dvd_base_universe_d2_058_dvd_basefill_058(dvd_basefill_058):
    return _base_universe_d2(dvd_basefill_058, 58)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_058_dvd_basefill_058'] = {'inputs': ['dvd_basefill_058'], 'func': dvd_base_universe_d2_058_dvd_basefill_058}


def dvd_base_universe_d2_059_dvd_basefill_059(dvd_basefill_059):
    return _base_universe_d2(dvd_basefill_059, 59)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_059_dvd_basefill_059'] = {'inputs': ['dvd_basefill_059'], 'func': dvd_base_universe_d2_059_dvd_basefill_059}


def dvd_base_universe_d2_060_dvd_basefill_062(dvd_basefill_062):
    return _base_universe_d2(dvd_basefill_062, 60)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_060_dvd_basefill_062'] = {'inputs': ['dvd_basefill_062'], 'func': dvd_base_universe_d2_060_dvd_basefill_062}


def dvd_base_universe_d2_061_dvd_basefill_063(dvd_basefill_063):
    return _base_universe_d2(dvd_basefill_063, 61)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_061_dvd_basefill_063'] = {'inputs': ['dvd_basefill_063'], 'func': dvd_base_universe_d2_061_dvd_basefill_063}


def dvd_base_universe_d2_062_dvd_basefill_064(dvd_basefill_064):
    return _base_universe_d2(dvd_basefill_064, 62)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_062_dvd_basefill_064'] = {'inputs': ['dvd_basefill_064'], 'func': dvd_base_universe_d2_062_dvd_basefill_064}


def dvd_base_universe_d2_063_dvd_basefill_065(dvd_basefill_065):
    return _base_universe_d2(dvd_basefill_065, 63)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_063_dvd_basefill_065'] = {'inputs': ['dvd_basefill_065'], 'func': dvd_base_universe_d2_063_dvd_basefill_065}


def dvd_base_universe_d2_064_dvd_basefill_066(dvd_basefill_066):
    return _base_universe_d2(dvd_basefill_066, 64)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_064_dvd_basefill_066'] = {'inputs': ['dvd_basefill_066'], 'func': dvd_base_universe_d2_064_dvd_basefill_066}


def dvd_base_universe_d2_065_dvd_basefill_067(dvd_basefill_067):
    return _base_universe_d2(dvd_basefill_067, 65)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_065_dvd_basefill_067'] = {'inputs': ['dvd_basefill_067'], 'func': dvd_base_universe_d2_065_dvd_basefill_067}


def dvd_base_universe_d2_066_dvd_basefill_069(dvd_basefill_069):
    return _base_universe_d2(dvd_basefill_069, 66)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_066_dvd_basefill_069'] = {'inputs': ['dvd_basefill_069'], 'func': dvd_base_universe_d2_066_dvd_basefill_069}


def dvd_base_universe_d2_067_dvd_basefill_070(dvd_basefill_070):
    return _base_universe_d2(dvd_basefill_070, 67)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_067_dvd_basefill_070'] = {'inputs': ['dvd_basefill_070'], 'func': dvd_base_universe_d2_067_dvd_basefill_070}


def dvd_base_universe_d2_068_dvd_basefill_071(dvd_basefill_071):
    return _base_universe_d2(dvd_basefill_071, 68)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_068_dvd_basefill_071'] = {'inputs': ['dvd_basefill_071'], 'func': dvd_base_universe_d2_068_dvd_basefill_071}


def dvd_base_universe_d2_069_dvd_basefill_072(dvd_basefill_072):
    return _base_universe_d2(dvd_basefill_072, 69)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_069_dvd_basefill_072'] = {'inputs': ['dvd_basefill_072'], 'func': dvd_base_universe_d2_069_dvd_basefill_072}


def dvd_base_universe_d2_070_dvd_basefill_073(dvd_basefill_073):
    return _base_universe_d2(dvd_basefill_073, 70)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_070_dvd_basefill_073'] = {'inputs': ['dvd_basefill_073'], 'func': dvd_base_universe_d2_070_dvd_basefill_073}


def dvd_base_universe_d2_071_dvd_basefill_074(dvd_basefill_074):
    return _base_universe_d2(dvd_basefill_074, 71)
DVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvd_base_universe_d2_071_dvd_basefill_074'] = {'inputs': ['dvd_basefill_074'], 'func': dvd_base_universe_d2_071_dvd_basefill_074}
