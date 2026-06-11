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



def gcf_151_gcf_001_dividend_cut_density_21_roc_1(gcf_001_dividend_cut_density_21):
    feature = _s(gcf_001_dividend_cut_density_21)
    return (_roc(feature, 1)).reindex(feature.index)

def gcf_152_gcf_007_listing_tier_decay_1_roc_42(gcf_007_listing_tier_decay_1):
    feature = _s(gcf_007_listing_tier_decay_1)
    return (_roc(feature, 42)).reindex(feature.index)

def gcf_153_gcf_013_delisting_notice_density_1512_roc_126(gcf_013_delisting_notice_density_1512):
    feature = _s(gcf_013_delisting_notice_density_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def gcf_154_gcf_019_going_concern_persistence_84_roc_378(gcf_019_going_concern_persistence_84):
    feature = _s(gcf_019_going_concern_persistence_84)
    return (_roc(feature, 378)).reindex(feature.index)

def gcf_155_gcf_025_event_density_z_756_roc_4(gcf_025_event_density_z_756):
    feature = _s(gcf_025_event_density_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















GOING_CONCERN_FLAGS_REGISTRY_2ND_DERIVATIVES = {
    'gcf_151_gcf_001_dividend_cut_density_21_roc_1': {'inputs': ['gcf_001_dividend_cut_density_21'], 'func': gcf_151_gcf_001_dividend_cut_density_21_roc_1},
    'gcf_152_gcf_007_listing_tier_decay_1_roc_42': {'inputs': ['gcf_007_listing_tier_decay_1'], 'func': gcf_152_gcf_007_listing_tier_decay_1_roc_42},
    'gcf_153_gcf_013_delisting_notice_density_1512_roc_126': {'inputs': ['gcf_013_delisting_notice_density_1512'], 'func': gcf_153_gcf_013_delisting_notice_density_1512_roc_126},
    'gcf_154_gcf_019_going_concern_persistence_84_roc_378': {'inputs': ['gcf_019_going_concern_persistence_84'], 'func': gcf_154_gcf_019_going_concern_persistence_84_roc_378},
    'gcf_155_gcf_025_event_density_z_756_roc_4': {'inputs': ['gcf_025_event_density_z_756'], 'func': gcf_155_gcf_025_event_density_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def gcf_replacement_d2_001(gcf_007_listing_tier_decay_1):
    feature = _clean(gcf_007_listing_tier_decay_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_001'] = {'inputs': ['gcf_007_listing_tier_decay_1'], 'func': gcf_replacement_d2_001}


def gcf_replacement_d2_002(gcf_replacement_001):
    feature = _clean(gcf_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_002'] = {'inputs': ['gcf_replacement_001'], 'func': gcf_replacement_d2_002}


def gcf_replacement_d2_003(gcf_replacement_002):
    feature = _clean(gcf_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_003'] = {'inputs': ['gcf_replacement_002'], 'func': gcf_replacement_d2_003}


def gcf_replacement_d2_004(gcf_replacement_003):
    feature = _clean(gcf_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_004'] = {'inputs': ['gcf_replacement_003'], 'func': gcf_replacement_d2_004}


def gcf_replacement_d2_005(gcf_replacement_004):
    feature = _clean(gcf_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_005'] = {'inputs': ['gcf_replacement_004'], 'func': gcf_replacement_d2_005}


def gcf_replacement_d2_006(gcf_replacement_005):
    feature = _clean(gcf_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_006'] = {'inputs': ['gcf_replacement_005'], 'func': gcf_replacement_d2_006}


def gcf_replacement_d2_007(gcf_replacement_006):
    feature = _clean(gcf_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_007'] = {'inputs': ['gcf_replacement_006'], 'func': gcf_replacement_d2_007}


def gcf_replacement_d2_008(gcf_replacement_007):
    feature = _clean(gcf_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_008'] = {'inputs': ['gcf_replacement_007'], 'func': gcf_replacement_d2_008}


def gcf_replacement_d2_009(gcf_replacement_008):
    feature = _clean(gcf_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_009'] = {'inputs': ['gcf_replacement_008'], 'func': gcf_replacement_d2_009}


def gcf_replacement_d2_010(gcf_replacement_009):
    feature = _clean(gcf_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_010'] = {'inputs': ['gcf_replacement_009'], 'func': gcf_replacement_d2_010}


def gcf_replacement_d2_011(gcf_replacement_010):
    feature = _clean(gcf_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_011'] = {'inputs': ['gcf_replacement_010'], 'func': gcf_replacement_d2_011}


def gcf_replacement_d2_012(gcf_replacement_011):
    feature = _clean(gcf_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_012'] = {'inputs': ['gcf_replacement_011'], 'func': gcf_replacement_d2_012}


def gcf_replacement_d2_013(gcf_replacement_012):
    feature = _clean(gcf_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_013'] = {'inputs': ['gcf_replacement_012'], 'func': gcf_replacement_d2_013}


def gcf_replacement_d2_014(gcf_replacement_013):
    feature = _clean(gcf_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_014'] = {'inputs': ['gcf_replacement_013'], 'func': gcf_replacement_d2_014}


def gcf_replacement_d2_015(gcf_replacement_014):
    feature = _clean(gcf_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_015'] = {'inputs': ['gcf_replacement_014'], 'func': gcf_replacement_d2_015}


def gcf_replacement_d2_016(gcf_replacement_015):
    feature = _clean(gcf_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_016'] = {'inputs': ['gcf_replacement_015'], 'func': gcf_replacement_d2_016}


def gcf_replacement_d2_017(gcf_replacement_016):
    feature = _clean(gcf_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_017'] = {'inputs': ['gcf_replacement_016'], 'func': gcf_replacement_d2_017}


def gcf_replacement_d2_018(gcf_replacement_017):
    feature = _clean(gcf_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_018'] = {'inputs': ['gcf_replacement_017'], 'func': gcf_replacement_d2_018}


def gcf_replacement_d2_019(gcf_replacement_018):
    feature = _clean(gcf_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_019'] = {'inputs': ['gcf_replacement_018'], 'func': gcf_replacement_d2_019}


def gcf_replacement_d2_020(gcf_replacement_019):
    feature = _clean(gcf_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_020'] = {'inputs': ['gcf_replacement_019'], 'func': gcf_replacement_d2_020}


def gcf_replacement_d2_021(gcf_replacement_020):
    feature = _clean(gcf_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_021'] = {'inputs': ['gcf_replacement_020'], 'func': gcf_replacement_d2_021}


def gcf_replacement_d2_022(gcf_replacement_021):
    feature = _clean(gcf_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_022'] = {'inputs': ['gcf_replacement_021'], 'func': gcf_replacement_d2_022}


def gcf_replacement_d2_023(gcf_replacement_022):
    feature = _clean(gcf_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_023'] = {'inputs': ['gcf_replacement_022'], 'func': gcf_replacement_d2_023}


def gcf_replacement_d2_024(gcf_replacement_023):
    feature = _clean(gcf_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_024'] = {'inputs': ['gcf_replacement_023'], 'func': gcf_replacement_d2_024}


def gcf_replacement_d2_025(gcf_replacement_024):
    feature = _clean(gcf_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_025'] = {'inputs': ['gcf_replacement_024'], 'func': gcf_replacement_d2_025}


def gcf_replacement_d2_026(gcf_replacement_025):
    feature = _clean(gcf_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_026'] = {'inputs': ['gcf_replacement_025'], 'func': gcf_replacement_d2_026}


def gcf_replacement_d2_027(gcf_replacement_026):
    feature = _clean(gcf_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_027'] = {'inputs': ['gcf_replacement_026'], 'func': gcf_replacement_d2_027}


def gcf_replacement_d2_028(gcf_replacement_027):
    feature = _clean(gcf_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_028'] = {'inputs': ['gcf_replacement_027'], 'func': gcf_replacement_d2_028}


def gcf_replacement_d2_029(gcf_replacement_028):
    feature = _clean(gcf_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_029'] = {'inputs': ['gcf_replacement_028'], 'func': gcf_replacement_d2_029}


def gcf_replacement_d2_030(gcf_replacement_029):
    feature = _clean(gcf_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_030'] = {'inputs': ['gcf_replacement_029'], 'func': gcf_replacement_d2_030}


def gcf_replacement_d2_031(gcf_replacement_030):
    feature = _clean(gcf_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_031'] = {'inputs': ['gcf_replacement_030'], 'func': gcf_replacement_d2_031}


def gcf_replacement_d2_032(gcf_replacement_031):
    feature = _clean(gcf_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_032'] = {'inputs': ['gcf_replacement_031'], 'func': gcf_replacement_d2_032}


def gcf_replacement_d2_033(gcf_replacement_032):
    feature = _clean(gcf_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_033'] = {'inputs': ['gcf_replacement_032'], 'func': gcf_replacement_d2_033}


def gcf_replacement_d2_034(gcf_replacement_033):
    feature = _clean(gcf_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_034'] = {'inputs': ['gcf_replacement_033'], 'func': gcf_replacement_d2_034}


def gcf_replacement_d2_035(gcf_replacement_034):
    feature = _clean(gcf_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_035'] = {'inputs': ['gcf_replacement_034'], 'func': gcf_replacement_d2_035}


def gcf_replacement_d2_036(gcf_replacement_035):
    feature = _clean(gcf_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_036'] = {'inputs': ['gcf_replacement_035'], 'func': gcf_replacement_d2_036}


def gcf_replacement_d2_037(gcf_replacement_036):
    feature = _clean(gcf_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_037'] = {'inputs': ['gcf_replacement_036'], 'func': gcf_replacement_d2_037}


def gcf_replacement_d2_038(gcf_replacement_037):
    feature = _clean(gcf_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_038'] = {'inputs': ['gcf_replacement_037'], 'func': gcf_replacement_d2_038}


def gcf_replacement_d2_039(gcf_replacement_038):
    feature = _clean(gcf_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_039'] = {'inputs': ['gcf_replacement_038'], 'func': gcf_replacement_d2_039}


def gcf_replacement_d2_040(gcf_replacement_039):
    feature = _clean(gcf_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_040'] = {'inputs': ['gcf_replacement_039'], 'func': gcf_replacement_d2_040}


def gcf_replacement_d2_041(gcf_replacement_040):
    feature = _clean(gcf_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_041'] = {'inputs': ['gcf_replacement_040'], 'func': gcf_replacement_d2_041}


def gcf_replacement_d2_042(gcf_replacement_041):
    feature = _clean(gcf_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_042'] = {'inputs': ['gcf_replacement_041'], 'func': gcf_replacement_d2_042}


def gcf_replacement_d2_043(gcf_replacement_042):
    feature = _clean(gcf_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_043'] = {'inputs': ['gcf_replacement_042'], 'func': gcf_replacement_d2_043}


def gcf_replacement_d2_044(gcf_replacement_043):
    feature = _clean(gcf_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_044'] = {'inputs': ['gcf_replacement_043'], 'func': gcf_replacement_d2_044}


def gcf_replacement_d2_045(gcf_replacement_044):
    feature = _clean(gcf_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_045'] = {'inputs': ['gcf_replacement_044'], 'func': gcf_replacement_d2_045}


def gcf_replacement_d2_046(gcf_replacement_045):
    feature = _clean(gcf_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_046'] = {'inputs': ['gcf_replacement_045'], 'func': gcf_replacement_d2_046}


def gcf_replacement_d2_047(gcf_replacement_046):
    feature = _clean(gcf_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_047'] = {'inputs': ['gcf_replacement_046'], 'func': gcf_replacement_d2_047}


def gcf_replacement_d2_048(gcf_replacement_047):
    feature = _clean(gcf_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_048'] = {'inputs': ['gcf_replacement_047'], 'func': gcf_replacement_d2_048}


def gcf_replacement_d2_049(gcf_replacement_048):
    feature = _clean(gcf_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_049'] = {'inputs': ['gcf_replacement_048'], 'func': gcf_replacement_d2_049}


def gcf_replacement_d2_050(gcf_replacement_049):
    feature = _clean(gcf_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_050'] = {'inputs': ['gcf_replacement_049'], 'func': gcf_replacement_d2_050}


def gcf_replacement_d2_051(gcf_replacement_050):
    feature = _clean(gcf_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_051'] = {'inputs': ['gcf_replacement_050'], 'func': gcf_replacement_d2_051}


def gcf_replacement_d2_052(gcf_replacement_051):
    feature = _clean(gcf_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_052'] = {'inputs': ['gcf_replacement_051'], 'func': gcf_replacement_d2_052}


def gcf_replacement_d2_053(gcf_replacement_052):
    feature = _clean(gcf_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_053'] = {'inputs': ['gcf_replacement_052'], 'func': gcf_replacement_d2_053}


def gcf_replacement_d2_054(gcf_replacement_053):
    feature = _clean(gcf_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_054'] = {'inputs': ['gcf_replacement_053'], 'func': gcf_replacement_d2_054}


def gcf_replacement_d2_055(gcf_replacement_054):
    feature = _clean(gcf_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_055'] = {'inputs': ['gcf_replacement_054'], 'func': gcf_replacement_d2_055}


def gcf_replacement_d2_056(gcf_replacement_055):
    feature = _clean(gcf_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_056'] = {'inputs': ['gcf_replacement_055'], 'func': gcf_replacement_d2_056}


def gcf_replacement_d2_057(gcf_replacement_056):
    feature = _clean(gcf_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_057'] = {'inputs': ['gcf_replacement_056'], 'func': gcf_replacement_d2_057}


def gcf_replacement_d2_058(gcf_replacement_057):
    feature = _clean(gcf_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_058'] = {'inputs': ['gcf_replacement_057'], 'func': gcf_replacement_d2_058}


def gcf_replacement_d2_059(gcf_replacement_058):
    feature = _clean(gcf_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_059'] = {'inputs': ['gcf_replacement_058'], 'func': gcf_replacement_d2_059}


def gcf_replacement_d2_060(gcf_replacement_059):
    feature = _clean(gcf_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_060'] = {'inputs': ['gcf_replacement_059'], 'func': gcf_replacement_d2_060}


def gcf_replacement_d2_061(gcf_replacement_060):
    feature = _clean(gcf_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_061'] = {'inputs': ['gcf_replacement_060'], 'func': gcf_replacement_d2_061}


def gcf_replacement_d2_062(gcf_replacement_061):
    feature = _clean(gcf_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_062'] = {'inputs': ['gcf_replacement_061'], 'func': gcf_replacement_d2_062}


def gcf_replacement_d2_063(gcf_replacement_062):
    feature = _clean(gcf_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_063'] = {'inputs': ['gcf_replacement_062'], 'func': gcf_replacement_d2_063}


def gcf_replacement_d2_064(gcf_replacement_063):
    feature = _clean(gcf_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_064'] = {'inputs': ['gcf_replacement_063'], 'func': gcf_replacement_d2_064}


def gcf_replacement_d2_065(gcf_replacement_064):
    feature = _clean(gcf_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_065'] = {'inputs': ['gcf_replacement_064'], 'func': gcf_replacement_d2_065}


def gcf_replacement_d2_066(gcf_replacement_065):
    feature = _clean(gcf_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_066'] = {'inputs': ['gcf_replacement_065'], 'func': gcf_replacement_d2_066}


def gcf_replacement_d2_067(gcf_replacement_066):
    feature = _clean(gcf_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_067'] = {'inputs': ['gcf_replacement_066'], 'func': gcf_replacement_d2_067}


def gcf_replacement_d2_068(gcf_replacement_067):
    feature = _clean(gcf_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_068'] = {'inputs': ['gcf_replacement_067'], 'func': gcf_replacement_d2_068}


def gcf_replacement_d2_069(gcf_replacement_068):
    feature = _clean(gcf_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_069'] = {'inputs': ['gcf_replacement_068'], 'func': gcf_replacement_d2_069}


def gcf_replacement_d2_070(gcf_replacement_069):
    feature = _clean(gcf_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_070'] = {'inputs': ['gcf_replacement_069'], 'func': gcf_replacement_d2_070}


def gcf_replacement_d2_071(gcf_replacement_070):
    feature = _clean(gcf_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_071'] = {'inputs': ['gcf_replacement_070'], 'func': gcf_replacement_d2_071}


def gcf_replacement_d2_072(gcf_replacement_071):
    feature = _clean(gcf_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_072'] = {'inputs': ['gcf_replacement_071'], 'func': gcf_replacement_d2_072}


def gcf_replacement_d2_073(gcf_replacement_072):
    feature = _clean(gcf_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_073'] = {'inputs': ['gcf_replacement_072'], 'func': gcf_replacement_d2_073}


def gcf_replacement_d2_074(gcf_replacement_073):
    feature = _clean(gcf_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_074'] = {'inputs': ['gcf_replacement_073'], 'func': gcf_replacement_d2_074}


def gcf_replacement_d2_075(gcf_replacement_074):
    feature = _clean(gcf_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_075'] = {'inputs': ['gcf_replacement_074'], 'func': gcf_replacement_d2_075}


def gcf_replacement_d2_076(gcf_replacement_075):
    feature = _clean(gcf_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_076'] = {'inputs': ['gcf_replacement_075'], 'func': gcf_replacement_d2_076}


def gcf_replacement_d2_077(gcf_replacement_076):
    feature = _clean(gcf_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_077'] = {'inputs': ['gcf_replacement_076'], 'func': gcf_replacement_d2_077}


def gcf_replacement_d2_078(gcf_replacement_077):
    feature = _clean(gcf_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_078'] = {'inputs': ['gcf_replacement_077'], 'func': gcf_replacement_d2_078}


def gcf_replacement_d2_079(gcf_replacement_078):
    feature = _clean(gcf_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_079'] = {'inputs': ['gcf_replacement_078'], 'func': gcf_replacement_d2_079}


def gcf_replacement_d2_080(gcf_replacement_079):
    feature = _clean(gcf_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_080'] = {'inputs': ['gcf_replacement_079'], 'func': gcf_replacement_d2_080}


def gcf_replacement_d2_081(gcf_replacement_080):
    feature = _clean(gcf_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_081'] = {'inputs': ['gcf_replacement_080'], 'func': gcf_replacement_d2_081}


def gcf_replacement_d2_082(gcf_replacement_081):
    feature = _clean(gcf_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_082'] = {'inputs': ['gcf_replacement_081'], 'func': gcf_replacement_d2_082}


def gcf_replacement_d2_083(gcf_replacement_082):
    feature = _clean(gcf_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_083'] = {'inputs': ['gcf_replacement_082'], 'func': gcf_replacement_d2_083}


def gcf_replacement_d2_084(gcf_replacement_083):
    feature = _clean(gcf_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_084'] = {'inputs': ['gcf_replacement_083'], 'func': gcf_replacement_d2_084}


def gcf_replacement_d2_085(gcf_replacement_084):
    feature = _clean(gcf_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_085'] = {'inputs': ['gcf_replacement_084'], 'func': gcf_replacement_d2_085}


def gcf_replacement_d2_086(gcf_replacement_085):
    feature = _clean(gcf_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_086'] = {'inputs': ['gcf_replacement_085'], 'func': gcf_replacement_d2_086}


def gcf_replacement_d2_087(gcf_replacement_086):
    feature = _clean(gcf_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_087'] = {'inputs': ['gcf_replacement_086'], 'func': gcf_replacement_d2_087}


def gcf_replacement_d2_088(gcf_replacement_087):
    feature = _clean(gcf_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_088'] = {'inputs': ['gcf_replacement_087'], 'func': gcf_replacement_d2_088}


def gcf_replacement_d2_089(gcf_replacement_088):
    feature = _clean(gcf_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_089'] = {'inputs': ['gcf_replacement_088'], 'func': gcf_replacement_d2_089}


def gcf_replacement_d2_090(gcf_replacement_089):
    feature = _clean(gcf_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_090'] = {'inputs': ['gcf_replacement_089'], 'func': gcf_replacement_d2_090}


def gcf_replacement_d2_091(gcf_replacement_090):
    feature = _clean(gcf_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_091'] = {'inputs': ['gcf_replacement_090'], 'func': gcf_replacement_d2_091}


def gcf_replacement_d2_092(gcf_replacement_091):
    feature = _clean(gcf_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_092'] = {'inputs': ['gcf_replacement_091'], 'func': gcf_replacement_d2_092}


def gcf_replacement_d2_093(gcf_replacement_092):
    feature = _clean(gcf_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_093'] = {'inputs': ['gcf_replacement_092'], 'func': gcf_replacement_d2_093}


def gcf_replacement_d2_094(gcf_replacement_093):
    feature = _clean(gcf_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_094'] = {'inputs': ['gcf_replacement_093'], 'func': gcf_replacement_d2_094}


def gcf_replacement_d2_095(gcf_replacement_094):
    feature = _clean(gcf_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_095'] = {'inputs': ['gcf_replacement_094'], 'func': gcf_replacement_d2_095}


def gcf_replacement_d2_096(gcf_replacement_095):
    feature = _clean(gcf_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_096'] = {'inputs': ['gcf_replacement_095'], 'func': gcf_replacement_d2_096}


def gcf_replacement_d2_097(gcf_replacement_096):
    feature = _clean(gcf_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_097'] = {'inputs': ['gcf_replacement_096'], 'func': gcf_replacement_d2_097}


def gcf_replacement_d2_098(gcf_replacement_097):
    feature = _clean(gcf_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_098'] = {'inputs': ['gcf_replacement_097'], 'func': gcf_replacement_d2_098}


def gcf_replacement_d2_099(gcf_replacement_098):
    feature = _clean(gcf_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_099'] = {'inputs': ['gcf_replacement_098'], 'func': gcf_replacement_d2_099}


def gcf_replacement_d2_100(gcf_replacement_099):
    feature = _clean(gcf_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_100'] = {'inputs': ['gcf_replacement_099'], 'func': gcf_replacement_d2_100}


def gcf_replacement_d2_101(gcf_replacement_100):
    feature = _clean(gcf_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_101'] = {'inputs': ['gcf_replacement_100'], 'func': gcf_replacement_d2_101}


def gcf_replacement_d2_102(gcf_replacement_101):
    feature = _clean(gcf_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_102'] = {'inputs': ['gcf_replacement_101'], 'func': gcf_replacement_d2_102}


def gcf_replacement_d2_103(gcf_replacement_102):
    feature = _clean(gcf_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_103'] = {'inputs': ['gcf_replacement_102'], 'func': gcf_replacement_d2_103}


def gcf_replacement_d2_104(gcf_replacement_103):
    feature = _clean(gcf_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_104'] = {'inputs': ['gcf_replacement_103'], 'func': gcf_replacement_d2_104}


def gcf_replacement_d2_105(gcf_replacement_104):
    feature = _clean(gcf_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_105'] = {'inputs': ['gcf_replacement_104'], 'func': gcf_replacement_d2_105}


def gcf_replacement_d2_106(gcf_replacement_105):
    feature = _clean(gcf_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_106'] = {'inputs': ['gcf_replacement_105'], 'func': gcf_replacement_d2_106}


def gcf_replacement_d2_107(gcf_replacement_106):
    feature = _clean(gcf_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_107'] = {'inputs': ['gcf_replacement_106'], 'func': gcf_replacement_d2_107}


def gcf_replacement_d2_108(gcf_replacement_107):
    feature = _clean(gcf_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_108'] = {'inputs': ['gcf_replacement_107'], 'func': gcf_replacement_d2_108}


def gcf_replacement_d2_109(gcf_replacement_108):
    feature = _clean(gcf_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_109'] = {'inputs': ['gcf_replacement_108'], 'func': gcf_replacement_d2_109}


def gcf_replacement_d2_110(gcf_replacement_109):
    feature = _clean(gcf_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_110'] = {'inputs': ['gcf_replacement_109'], 'func': gcf_replacement_d2_110}


def gcf_replacement_d2_111(gcf_replacement_110):
    feature = _clean(gcf_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_111'] = {'inputs': ['gcf_replacement_110'], 'func': gcf_replacement_d2_111}


def gcf_replacement_d2_112(gcf_replacement_111):
    feature = _clean(gcf_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_112'] = {'inputs': ['gcf_replacement_111'], 'func': gcf_replacement_d2_112}


def gcf_replacement_d2_113(gcf_replacement_112):
    feature = _clean(gcf_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_113'] = {'inputs': ['gcf_replacement_112'], 'func': gcf_replacement_d2_113}


def gcf_replacement_d2_114(gcf_replacement_113):
    feature = _clean(gcf_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_114'] = {'inputs': ['gcf_replacement_113'], 'func': gcf_replacement_d2_114}


def gcf_replacement_d2_115(gcf_replacement_114):
    feature = _clean(gcf_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_115'] = {'inputs': ['gcf_replacement_114'], 'func': gcf_replacement_d2_115}


def gcf_replacement_d2_116(gcf_replacement_115):
    feature = _clean(gcf_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_116'] = {'inputs': ['gcf_replacement_115'], 'func': gcf_replacement_d2_116}


def gcf_replacement_d2_117(gcf_replacement_116):
    feature = _clean(gcf_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_117'] = {'inputs': ['gcf_replacement_116'], 'func': gcf_replacement_d2_117}


def gcf_replacement_d2_118(gcf_replacement_117):
    feature = _clean(gcf_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_118'] = {'inputs': ['gcf_replacement_117'], 'func': gcf_replacement_d2_118}


def gcf_replacement_d2_119(gcf_replacement_118):
    feature = _clean(gcf_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_119'] = {'inputs': ['gcf_replacement_118'], 'func': gcf_replacement_d2_119}


def gcf_replacement_d2_120(gcf_replacement_119):
    feature = _clean(gcf_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_120'] = {'inputs': ['gcf_replacement_119'], 'func': gcf_replacement_d2_120}


def gcf_replacement_d2_121(gcf_replacement_120):
    feature = _clean(gcf_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_121'] = {'inputs': ['gcf_replacement_120'], 'func': gcf_replacement_d2_121}


def gcf_replacement_d2_122(gcf_replacement_121):
    feature = _clean(gcf_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_122'] = {'inputs': ['gcf_replacement_121'], 'func': gcf_replacement_d2_122}


def gcf_replacement_d2_123(gcf_replacement_122):
    feature = _clean(gcf_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_123'] = {'inputs': ['gcf_replacement_122'], 'func': gcf_replacement_d2_123}


def gcf_replacement_d2_124(gcf_replacement_123):
    feature = _clean(gcf_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_124'] = {'inputs': ['gcf_replacement_123'], 'func': gcf_replacement_d2_124}


def gcf_replacement_d2_125(gcf_replacement_124):
    feature = _clean(gcf_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_125'] = {'inputs': ['gcf_replacement_124'], 'func': gcf_replacement_d2_125}


def gcf_replacement_d2_126(gcf_replacement_125):
    feature = _clean(gcf_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_126'] = {'inputs': ['gcf_replacement_125'], 'func': gcf_replacement_d2_126}


def gcf_replacement_d2_127(gcf_replacement_126):
    feature = _clean(gcf_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_127'] = {'inputs': ['gcf_replacement_126'], 'func': gcf_replacement_d2_127}


def gcf_replacement_d2_128(gcf_replacement_127):
    feature = _clean(gcf_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_128'] = {'inputs': ['gcf_replacement_127'], 'func': gcf_replacement_d2_128}


def gcf_replacement_d2_129(gcf_replacement_128):
    feature = _clean(gcf_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_129'] = {'inputs': ['gcf_replacement_128'], 'func': gcf_replacement_d2_129}


def gcf_replacement_d2_130(gcf_replacement_129):
    feature = _clean(gcf_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_130'] = {'inputs': ['gcf_replacement_129'], 'func': gcf_replacement_d2_130}


def gcf_replacement_d2_131(gcf_replacement_130):
    feature = _clean(gcf_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_131'] = {'inputs': ['gcf_replacement_130'], 'func': gcf_replacement_d2_131}


def gcf_replacement_d2_132(gcf_replacement_131):
    feature = _clean(gcf_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_132'] = {'inputs': ['gcf_replacement_131'], 'func': gcf_replacement_d2_132}


def gcf_replacement_d2_133(gcf_replacement_132):
    feature = _clean(gcf_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_133'] = {'inputs': ['gcf_replacement_132'], 'func': gcf_replacement_d2_133}


def gcf_replacement_d2_134(gcf_replacement_133):
    feature = _clean(gcf_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_134'] = {'inputs': ['gcf_replacement_133'], 'func': gcf_replacement_d2_134}


def gcf_replacement_d2_135(gcf_replacement_134):
    feature = _clean(gcf_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_135'] = {'inputs': ['gcf_replacement_134'], 'func': gcf_replacement_d2_135}


def gcf_replacement_d2_136(gcf_replacement_135):
    feature = _clean(gcf_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_136'] = {'inputs': ['gcf_replacement_135'], 'func': gcf_replacement_d2_136}


def gcf_replacement_d2_137(gcf_replacement_136):
    feature = _clean(gcf_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_137'] = {'inputs': ['gcf_replacement_136'], 'func': gcf_replacement_d2_137}


def gcf_replacement_d2_138(gcf_replacement_137):
    feature = _clean(gcf_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_138'] = {'inputs': ['gcf_replacement_137'], 'func': gcf_replacement_d2_138}


def gcf_replacement_d2_139(gcf_replacement_138):
    feature = _clean(gcf_replacement_138)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_139'] = {'inputs': ['gcf_replacement_138'], 'func': gcf_replacement_d2_139}


def gcf_replacement_d2_140(gcf_replacement_139):
    feature = _clean(gcf_replacement_139)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_140'] = {'inputs': ['gcf_replacement_139'], 'func': gcf_replacement_d2_140}


def gcf_replacement_d2_141(gcf_replacement_140):
    feature = _clean(gcf_replacement_140)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_141'] = {'inputs': ['gcf_replacement_140'], 'func': gcf_replacement_d2_141}


def gcf_replacement_d2_142(gcf_replacement_141):
    feature = _clean(gcf_replacement_141)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_142'] = {'inputs': ['gcf_replacement_141'], 'func': gcf_replacement_d2_142}


def gcf_replacement_d2_143(gcf_replacement_142):
    feature = _clean(gcf_replacement_142)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_143'] = {'inputs': ['gcf_replacement_142'], 'func': gcf_replacement_d2_143}


def gcf_replacement_d2_144(gcf_replacement_143):
    feature = _clean(gcf_replacement_143)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_144'] = {'inputs': ['gcf_replacement_143'], 'func': gcf_replacement_d2_144}


def gcf_replacement_d2_145(gcf_replacement_144):
    feature = _clean(gcf_replacement_144)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_145'] = {'inputs': ['gcf_replacement_144'], 'func': gcf_replacement_d2_145}


def gcf_replacement_d2_146(gcf_replacement_145):
    feature = _clean(gcf_replacement_145)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_146'] = {'inputs': ['gcf_replacement_145'], 'func': gcf_replacement_d2_146}


def gcf_replacement_d2_147(gcf_replacement_146):
    feature = _clean(gcf_replacement_146)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_147'] = {'inputs': ['gcf_replacement_146'], 'func': gcf_replacement_d2_147}


def gcf_replacement_d2_148(gcf_replacement_147):
    feature = _clean(gcf_replacement_147)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_148'] = {'inputs': ['gcf_replacement_147'], 'func': gcf_replacement_d2_148}


def gcf_replacement_d2_149(gcf_replacement_148):
    feature = _clean(gcf_replacement_148)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_149'] = {'inputs': ['gcf_replacement_148'], 'func': gcf_replacement_d2_149}


def gcf_replacement_d2_150(gcf_replacement_149):
    feature = _clean(gcf_replacement_149)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_150'] = {'inputs': ['gcf_replacement_149'], 'func': gcf_replacement_d2_150}


def gcf_replacement_d2_151(gcf_replacement_150):
    feature = _clean(gcf_replacement_150)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
GCF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gcf_replacement_d2_151'] = {'inputs': ['gcf_replacement_150'], 'func': gcf_replacement_d2_151}


# Base-universe derivative extensions for repaired first-base features.
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42(gcf_002_dividend_suspension_density_42):
    return _base_universe_d2(gcf_002_dividend_suspension_density_42, 1)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42'] = {'inputs': ['gcf_002_dividend_suspension_density_42'], 'func': gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42}


def gcf_base_universe_d2_002_gcf_003_reverse_split_density_63(gcf_003_reverse_split_density_63):
    return _base_universe_d2(gcf_003_reverse_split_density_63, 2)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_002_gcf_003_reverse_split_density_63'] = {'inputs': ['gcf_003_reverse_split_density_63'], 'func': gcf_base_universe_d2_002_gcf_003_reverse_split_density_63}


def gcf_base_universe_d2_003_gcf_004_event_density_z_84(gcf_004_event_density_z_84):
    return _base_universe_d2(gcf_004_event_density_z_84, 3)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_003_gcf_004_event_density_z_84'] = {'inputs': ['gcf_004_event_density_z_84'], 'func': gcf_base_universe_d2_003_gcf_004_event_density_z_84}


def gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126(gcf_005_going_concern_persistence_126):
    return _base_universe_d2(gcf_005_going_concern_persistence_126, 4)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126'] = {'inputs': ['gcf_005_going_concern_persistence_126'], 'func': gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126}


def gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189(gcf_006_delisting_notice_density_189):
    return _base_universe_d2(gcf_006_delisting_notice_density_189, 5)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189'] = {'inputs': ['gcf_006_delisting_notice_density_189'], 'func': gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189}


def gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378(gcf_008_dividend_cut_density_378):
    return _base_universe_d2(gcf_008_dividend_cut_density_378, 6)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378'] = {'inputs': ['gcf_008_dividend_cut_density_378'], 'func': gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378}


def gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504(gcf_009_dividend_suspension_density_504):
    return _base_universe_d2(gcf_009_dividend_suspension_density_504, 7)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504'] = {'inputs': ['gcf_009_dividend_suspension_density_504'], 'func': gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504}


def gcf_base_universe_d2_008_gcf_010_reverse_split_density_756(gcf_010_reverse_split_density_756):
    return _base_universe_d2(gcf_010_reverse_split_density_756, 8)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_008_gcf_010_reverse_split_density_756'] = {'inputs': ['gcf_010_reverse_split_density_756'], 'func': gcf_base_universe_d2_008_gcf_010_reverse_split_density_756}


def gcf_base_universe_d2_009_gcf_011_event_density_z_1008(gcf_011_event_density_z_1008):
    return _base_universe_d2(gcf_011_event_density_z_1008, 9)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_009_gcf_011_event_density_z_1008'] = {'inputs': ['gcf_011_event_density_z_1008'], 'func': gcf_base_universe_d2_009_gcf_011_event_density_z_1008}


def gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260(gcf_012_going_concern_persistence_1260):
    return _base_universe_d2(gcf_012_going_concern_persistence_1260, 10)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260'] = {'inputs': ['gcf_012_going_concern_persistence_1260'], 'func': gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260}


def gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252(gcf_015_dividend_cut_density_252):
    return _base_universe_d2(gcf_015_dividend_cut_density_252, 11)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252'] = {'inputs': ['gcf_015_dividend_cut_density_252'], 'func': gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252}


def gcf_base_universe_d2_012_gcf_018_event_density_z_63(gcf_018_event_density_z_63):
    return _base_universe_d2(gcf_018_event_density_z_63, 12)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_012_gcf_018_event_density_z_63'] = {'inputs': ['gcf_018_event_density_z_63'], 'func': gcf_base_universe_d2_012_gcf_018_event_density_z_63}


def gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126(gcf_020_delisting_notice_density_126):
    return _base_universe_d2(gcf_020_delisting_notice_density_126, 13)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126'] = {'inputs': ['gcf_020_delisting_notice_density_126'], 'func': gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126}


def gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008(gcf_026_going_concern_persistence_1008):
    return _base_universe_d2(gcf_026_going_concern_persistence_1008, 14)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008'] = {'inputs': ['gcf_026_going_concern_persistence_1008'], 'func': gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008}


def gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260(gcf_027_delisting_notice_density_1260):
    return _base_universe_d2(gcf_027_delisting_notice_density_1260, 15)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260'] = {'inputs': ['gcf_027_delisting_notice_density_1260'], 'func': gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260}


def gcf_base_universe_d2_016_gcf_032_event_density_z_42(gcf_032_event_density_z_42):
    return _base_universe_d2(gcf_032_event_density_z_42, 16)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_016_gcf_032_event_density_z_42'] = {'inputs': ['gcf_032_event_density_z_42'], 'func': gcf_base_universe_d2_016_gcf_032_event_density_z_42}


def gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63(gcf_033_going_concern_persistence_63):
    return _base_universe_d2(gcf_033_going_concern_persistence_63, 17)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63'] = {'inputs': ['gcf_033_going_concern_persistence_63'], 'func': gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63}


def gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84(gcf_034_delisting_notice_density_84):
    return _base_universe_d2(gcf_034_delisting_notice_density_84, 18)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84'] = {'inputs': ['gcf_034_delisting_notice_density_84'], 'func': gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84}


def gcf_base_universe_d2_019_gcf_039_event_density_z_504(gcf_039_event_density_z_504):
    return _base_universe_d2(gcf_039_event_density_z_504, 19)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_019_gcf_039_event_density_z_504'] = {'inputs': ['gcf_039_event_density_z_504'], 'func': gcf_base_universe_d2_019_gcf_039_event_density_z_504}


def gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756(gcf_040_going_concern_persistence_756):
    return _base_universe_d2(gcf_040_going_concern_persistence_756, 20)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756'] = {'inputs': ['gcf_040_going_concern_persistence_756'], 'func': gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756}


def gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008(gcf_041_delisting_notice_density_1008):
    return _base_universe_d2(gcf_041_delisting_notice_density_1008, 21)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008'] = {'inputs': ['gcf_041_delisting_notice_density_1008'], 'func': gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008}


def gcf_base_universe_d2_022_gcf_046_event_density_z_21(gcf_046_event_density_z_21):
    return _base_universe_d2(gcf_046_event_density_z_21, 22)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_022_gcf_046_event_density_z_21'] = {'inputs': ['gcf_046_event_density_z_21'], 'func': gcf_base_universe_d2_022_gcf_046_event_density_z_21}


def gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42(gcf_047_going_concern_persistence_42):
    return _base_universe_d2(gcf_047_going_concern_persistence_42, 23)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42'] = {'inputs': ['gcf_047_going_concern_persistence_42'], 'func': gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42}


def gcf_base_universe_d2_024_gcf_053_event_density_z_378(gcf_053_event_density_z_378):
    return _base_universe_d2(gcf_053_event_density_z_378, 24)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_024_gcf_053_event_density_z_378'] = {'inputs': ['gcf_053_event_density_z_378'], 'func': gcf_base_universe_d2_024_gcf_053_event_density_z_378}


def gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504(gcf_054_going_concern_persistence_504):
    return _base_universe_d2(gcf_054_going_concern_persistence_504, 25)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504'] = {'inputs': ['gcf_054_going_concern_persistence_504'], 'func': gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504}


def gcf_base_universe_d2_026_gcf_060_event_density_z_252(gcf_060_event_density_z_252):
    return _base_universe_d2(gcf_060_event_density_z_252, 26)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_026_gcf_060_event_density_z_252'] = {'inputs': ['gcf_060_event_density_z_252'], 'func': gcf_base_universe_d2_026_gcf_060_event_density_z_252}


def gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21(gcf_061_going_concern_persistence_21):
    return _base_universe_d2(gcf_061_going_concern_persistence_21, 27)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21'] = {'inputs': ['gcf_061_going_concern_persistence_21'], 'func': gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21}


def gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378(gcf_068_going_concern_persistence_378):
    return _base_universe_d2(gcf_068_going_concern_persistence_378, 28)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378'] = {'inputs': ['gcf_068_going_concern_persistence_378'], 'func': gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378}


def gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252(gcf_075_going_concern_persistence_252):
    return _base_universe_d2(gcf_075_going_concern_persistence_252, 29)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252'] = {'inputs': ['gcf_075_going_concern_persistence_252'], 'func': gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252}


def gcf_base_universe_d2_030_gcf_basefill_007(gcf_basefill_007):
    return _base_universe_d2(gcf_basefill_007, 30)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_030_gcf_basefill_007'] = {'inputs': ['gcf_basefill_007'], 'func': gcf_base_universe_d2_030_gcf_basefill_007}


def gcf_base_universe_d2_031_gcf_basefill_014(gcf_basefill_014):
    return _base_universe_d2(gcf_basefill_014, 31)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_031_gcf_basefill_014'] = {'inputs': ['gcf_basefill_014'], 'func': gcf_base_universe_d2_031_gcf_basefill_014}


def gcf_base_universe_d2_032_gcf_basefill_016(gcf_basefill_016):
    return _base_universe_d2(gcf_basefill_016, 32)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_032_gcf_basefill_016'] = {'inputs': ['gcf_basefill_016'], 'func': gcf_base_universe_d2_032_gcf_basefill_016}


def gcf_base_universe_d2_033_gcf_basefill_017(gcf_basefill_017):
    return _base_universe_d2(gcf_basefill_017, 33)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_033_gcf_basefill_017'] = {'inputs': ['gcf_basefill_017'], 'func': gcf_base_universe_d2_033_gcf_basefill_017}


def gcf_base_universe_d2_034_gcf_basefill_021(gcf_basefill_021):
    return _base_universe_d2(gcf_basefill_021, 34)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_034_gcf_basefill_021'] = {'inputs': ['gcf_basefill_021'], 'func': gcf_base_universe_d2_034_gcf_basefill_021}


def gcf_base_universe_d2_035_gcf_basefill_022(gcf_basefill_022):
    return _base_universe_d2(gcf_basefill_022, 35)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_035_gcf_basefill_022'] = {'inputs': ['gcf_basefill_022'], 'func': gcf_base_universe_d2_035_gcf_basefill_022}


def gcf_base_universe_d2_036_gcf_basefill_023(gcf_basefill_023):
    return _base_universe_d2(gcf_basefill_023, 36)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_036_gcf_basefill_023'] = {'inputs': ['gcf_basefill_023'], 'func': gcf_base_universe_d2_036_gcf_basefill_023}


def gcf_base_universe_d2_037_gcf_basefill_024(gcf_basefill_024):
    return _base_universe_d2(gcf_basefill_024, 37)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_037_gcf_basefill_024'] = {'inputs': ['gcf_basefill_024'], 'func': gcf_base_universe_d2_037_gcf_basefill_024}


def gcf_base_universe_d2_038_gcf_basefill_028(gcf_basefill_028):
    return _base_universe_d2(gcf_basefill_028, 38)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_038_gcf_basefill_028'] = {'inputs': ['gcf_basefill_028'], 'func': gcf_base_universe_d2_038_gcf_basefill_028}


def gcf_base_universe_d2_039_gcf_basefill_029(gcf_basefill_029):
    return _base_universe_d2(gcf_basefill_029, 39)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_039_gcf_basefill_029'] = {'inputs': ['gcf_basefill_029'], 'func': gcf_base_universe_d2_039_gcf_basefill_029}


def gcf_base_universe_d2_040_gcf_basefill_030(gcf_basefill_030):
    return _base_universe_d2(gcf_basefill_030, 40)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_040_gcf_basefill_030'] = {'inputs': ['gcf_basefill_030'], 'func': gcf_base_universe_d2_040_gcf_basefill_030}


def gcf_base_universe_d2_041_gcf_basefill_031(gcf_basefill_031):
    return _base_universe_d2(gcf_basefill_031, 41)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_041_gcf_basefill_031'] = {'inputs': ['gcf_basefill_031'], 'func': gcf_base_universe_d2_041_gcf_basefill_031}


def gcf_base_universe_d2_042_gcf_basefill_035(gcf_basefill_035):
    return _base_universe_d2(gcf_basefill_035, 42)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_042_gcf_basefill_035'] = {'inputs': ['gcf_basefill_035'], 'func': gcf_base_universe_d2_042_gcf_basefill_035}


def gcf_base_universe_d2_043_gcf_basefill_036(gcf_basefill_036):
    return _base_universe_d2(gcf_basefill_036, 43)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_043_gcf_basefill_036'] = {'inputs': ['gcf_basefill_036'], 'func': gcf_base_universe_d2_043_gcf_basefill_036}


def gcf_base_universe_d2_044_gcf_basefill_037(gcf_basefill_037):
    return _base_universe_d2(gcf_basefill_037, 44)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_044_gcf_basefill_037'] = {'inputs': ['gcf_basefill_037'], 'func': gcf_base_universe_d2_044_gcf_basefill_037}


def gcf_base_universe_d2_045_gcf_basefill_038(gcf_basefill_038):
    return _base_universe_d2(gcf_basefill_038, 45)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_045_gcf_basefill_038'] = {'inputs': ['gcf_basefill_038'], 'func': gcf_base_universe_d2_045_gcf_basefill_038}


def gcf_base_universe_d2_046_gcf_basefill_042(gcf_basefill_042):
    return _base_universe_d2(gcf_basefill_042, 46)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_046_gcf_basefill_042'] = {'inputs': ['gcf_basefill_042'], 'func': gcf_base_universe_d2_046_gcf_basefill_042}


def gcf_base_universe_d2_047_gcf_basefill_043(gcf_basefill_043):
    return _base_universe_d2(gcf_basefill_043, 47)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_047_gcf_basefill_043'] = {'inputs': ['gcf_basefill_043'], 'func': gcf_base_universe_d2_047_gcf_basefill_043}


def gcf_base_universe_d2_048_gcf_basefill_044(gcf_basefill_044):
    return _base_universe_d2(gcf_basefill_044, 48)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_048_gcf_basefill_044'] = {'inputs': ['gcf_basefill_044'], 'func': gcf_base_universe_d2_048_gcf_basefill_044}


def gcf_base_universe_d2_049_gcf_basefill_045(gcf_basefill_045):
    return _base_universe_d2(gcf_basefill_045, 49)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_049_gcf_basefill_045'] = {'inputs': ['gcf_basefill_045'], 'func': gcf_base_universe_d2_049_gcf_basefill_045}


def gcf_base_universe_d2_050_gcf_basefill_048(gcf_basefill_048):
    return _base_universe_d2(gcf_basefill_048, 50)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_050_gcf_basefill_048'] = {'inputs': ['gcf_basefill_048'], 'func': gcf_base_universe_d2_050_gcf_basefill_048}


def gcf_base_universe_d2_051_gcf_basefill_049(gcf_basefill_049):
    return _base_universe_d2(gcf_basefill_049, 51)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_051_gcf_basefill_049'] = {'inputs': ['gcf_basefill_049'], 'func': gcf_base_universe_d2_051_gcf_basefill_049}


def gcf_base_universe_d2_052_gcf_basefill_050(gcf_basefill_050):
    return _base_universe_d2(gcf_basefill_050, 52)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_052_gcf_basefill_050'] = {'inputs': ['gcf_basefill_050'], 'func': gcf_base_universe_d2_052_gcf_basefill_050}


def gcf_base_universe_d2_053_gcf_basefill_051(gcf_basefill_051):
    return _base_universe_d2(gcf_basefill_051, 53)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_053_gcf_basefill_051'] = {'inputs': ['gcf_basefill_051'], 'func': gcf_base_universe_d2_053_gcf_basefill_051}


def gcf_base_universe_d2_054_gcf_basefill_052(gcf_basefill_052):
    return _base_universe_d2(gcf_basefill_052, 54)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_054_gcf_basefill_052'] = {'inputs': ['gcf_basefill_052'], 'func': gcf_base_universe_d2_054_gcf_basefill_052}


def gcf_base_universe_d2_055_gcf_basefill_055(gcf_basefill_055):
    return _base_universe_d2(gcf_basefill_055, 55)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_055_gcf_basefill_055'] = {'inputs': ['gcf_basefill_055'], 'func': gcf_base_universe_d2_055_gcf_basefill_055}


def gcf_base_universe_d2_056_gcf_basefill_056(gcf_basefill_056):
    return _base_universe_d2(gcf_basefill_056, 56)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_056_gcf_basefill_056'] = {'inputs': ['gcf_basefill_056'], 'func': gcf_base_universe_d2_056_gcf_basefill_056}


def gcf_base_universe_d2_057_gcf_basefill_057(gcf_basefill_057):
    return _base_universe_d2(gcf_basefill_057, 57)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_057_gcf_basefill_057'] = {'inputs': ['gcf_basefill_057'], 'func': gcf_base_universe_d2_057_gcf_basefill_057}


def gcf_base_universe_d2_058_gcf_basefill_058(gcf_basefill_058):
    return _base_universe_d2(gcf_basefill_058, 58)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_058_gcf_basefill_058'] = {'inputs': ['gcf_basefill_058'], 'func': gcf_base_universe_d2_058_gcf_basefill_058}


def gcf_base_universe_d2_059_gcf_basefill_059(gcf_basefill_059):
    return _base_universe_d2(gcf_basefill_059, 59)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_059_gcf_basefill_059'] = {'inputs': ['gcf_basefill_059'], 'func': gcf_base_universe_d2_059_gcf_basefill_059}


def gcf_base_universe_d2_060_gcf_basefill_062(gcf_basefill_062):
    return _base_universe_d2(gcf_basefill_062, 60)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_060_gcf_basefill_062'] = {'inputs': ['gcf_basefill_062'], 'func': gcf_base_universe_d2_060_gcf_basefill_062}


def gcf_base_universe_d2_061_gcf_basefill_063(gcf_basefill_063):
    return _base_universe_d2(gcf_basefill_063, 61)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_061_gcf_basefill_063'] = {'inputs': ['gcf_basefill_063'], 'func': gcf_base_universe_d2_061_gcf_basefill_063}


def gcf_base_universe_d2_062_gcf_basefill_064(gcf_basefill_064):
    return _base_universe_d2(gcf_basefill_064, 62)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_062_gcf_basefill_064'] = {'inputs': ['gcf_basefill_064'], 'func': gcf_base_universe_d2_062_gcf_basefill_064}


def gcf_base_universe_d2_063_gcf_basefill_065(gcf_basefill_065):
    return _base_universe_d2(gcf_basefill_065, 63)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_063_gcf_basefill_065'] = {'inputs': ['gcf_basefill_065'], 'func': gcf_base_universe_d2_063_gcf_basefill_065}


def gcf_base_universe_d2_064_gcf_basefill_066(gcf_basefill_066):
    return _base_universe_d2(gcf_basefill_066, 64)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_064_gcf_basefill_066'] = {'inputs': ['gcf_basefill_066'], 'func': gcf_base_universe_d2_064_gcf_basefill_066}


def gcf_base_universe_d2_065_gcf_basefill_067(gcf_basefill_067):
    return _base_universe_d2(gcf_basefill_067, 65)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_065_gcf_basefill_067'] = {'inputs': ['gcf_basefill_067'], 'func': gcf_base_universe_d2_065_gcf_basefill_067}


def gcf_base_universe_d2_066_gcf_basefill_069(gcf_basefill_069):
    return _base_universe_d2(gcf_basefill_069, 66)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_066_gcf_basefill_069'] = {'inputs': ['gcf_basefill_069'], 'func': gcf_base_universe_d2_066_gcf_basefill_069}


def gcf_base_universe_d2_067_gcf_basefill_070(gcf_basefill_070):
    return _base_universe_d2(gcf_basefill_070, 67)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_067_gcf_basefill_070'] = {'inputs': ['gcf_basefill_070'], 'func': gcf_base_universe_d2_067_gcf_basefill_070}


def gcf_base_universe_d2_068_gcf_basefill_071(gcf_basefill_071):
    return _base_universe_d2(gcf_basefill_071, 68)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_068_gcf_basefill_071'] = {'inputs': ['gcf_basefill_071'], 'func': gcf_base_universe_d2_068_gcf_basefill_071}


def gcf_base_universe_d2_069_gcf_basefill_072(gcf_basefill_072):
    return _base_universe_d2(gcf_basefill_072, 69)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_069_gcf_basefill_072'] = {'inputs': ['gcf_basefill_072'], 'func': gcf_base_universe_d2_069_gcf_basefill_072}


def gcf_base_universe_d2_070_gcf_basefill_073(gcf_basefill_073):
    return _base_universe_d2(gcf_basefill_073, 70)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_070_gcf_basefill_073'] = {'inputs': ['gcf_basefill_073'], 'func': gcf_base_universe_d2_070_gcf_basefill_073}


def gcf_base_universe_d2_071_gcf_basefill_074(gcf_basefill_074):
    return _base_universe_d2(gcf_basefill_074, 71)
GCF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gcf_base_universe_d2_071_gcf_basefill_074'] = {'inputs': ['gcf_basefill_074'], 'func': gcf_base_universe_d2_071_gcf_basefill_074}
