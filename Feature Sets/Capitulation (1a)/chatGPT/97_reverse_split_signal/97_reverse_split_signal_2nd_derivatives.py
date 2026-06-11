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



def rss_151_rss_001_dividend_cut_density_21_roc_1(rss_001_dividend_cut_density_21):
    feature = _s(rss_001_dividend_cut_density_21)
    return (_roc(feature, 1)).reindex(feature.index)

def rss_152_rss_007_listing_tier_decay_1_roc_42(rss_007_listing_tier_decay_1):
    feature = _s(rss_007_listing_tier_decay_1)
    return (_roc(feature, 42)).reindex(feature.index)

def rss_153_rss_013_delisting_notice_density_1512_roc_126(rss_013_delisting_notice_density_1512):
    feature = _s(rss_013_delisting_notice_density_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def rss_154_rss_019_going_concern_persistence_84_roc_378(rss_019_going_concern_persistence_84):
    feature = _s(rss_019_going_concern_persistence_84)
    return (_roc(feature, 378)).reindex(feature.index)

def rss_155_rss_025_event_density_z_756_roc_4(rss_025_event_density_z_756):
    feature = _s(rss_025_event_density_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















REVERSE_SPLIT_SIGNAL_REGISTRY_2ND_DERIVATIVES = {
    'rss_151_rss_001_dividend_cut_density_21_roc_1': {'inputs': ['rss_001_dividend_cut_density_21'], 'func': rss_151_rss_001_dividend_cut_density_21_roc_1},
    'rss_152_rss_007_listing_tier_decay_1_roc_42': {'inputs': ['rss_007_listing_tier_decay_1'], 'func': rss_152_rss_007_listing_tier_decay_1_roc_42},
    'rss_153_rss_013_delisting_notice_density_1512_roc_126': {'inputs': ['rss_013_delisting_notice_density_1512'], 'func': rss_153_rss_013_delisting_notice_density_1512_roc_126},
    'rss_154_rss_019_going_concern_persistence_84_roc_378': {'inputs': ['rss_019_going_concern_persistence_84'], 'func': rss_154_rss_019_going_concern_persistence_84_roc_378},
    'rss_155_rss_025_event_density_z_756_roc_4': {'inputs': ['rss_025_event_density_z_756'], 'func': rss_155_rss_025_event_density_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def rss_replacement_d2_001(rss_007_listing_tier_decay_1):
    feature = _clean(rss_007_listing_tier_decay_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_001'] = {'inputs': ['rss_007_listing_tier_decay_1'], 'func': rss_replacement_d2_001}


def rss_replacement_d2_002(rss_replacement_001):
    feature = _clean(rss_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_002'] = {'inputs': ['rss_replacement_001'], 'func': rss_replacement_d2_002}


def rss_replacement_d2_003(rss_replacement_002):
    feature = _clean(rss_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_003'] = {'inputs': ['rss_replacement_002'], 'func': rss_replacement_d2_003}


def rss_replacement_d2_004(rss_replacement_003):
    feature = _clean(rss_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_004'] = {'inputs': ['rss_replacement_003'], 'func': rss_replacement_d2_004}


def rss_replacement_d2_005(rss_replacement_004):
    feature = _clean(rss_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_005'] = {'inputs': ['rss_replacement_004'], 'func': rss_replacement_d2_005}


def rss_replacement_d2_006(rss_replacement_005):
    feature = _clean(rss_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_006'] = {'inputs': ['rss_replacement_005'], 'func': rss_replacement_d2_006}


def rss_replacement_d2_007(rss_replacement_006):
    feature = _clean(rss_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_007'] = {'inputs': ['rss_replacement_006'], 'func': rss_replacement_d2_007}


def rss_replacement_d2_008(rss_replacement_007):
    feature = _clean(rss_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_008'] = {'inputs': ['rss_replacement_007'], 'func': rss_replacement_d2_008}


def rss_replacement_d2_009(rss_replacement_008):
    feature = _clean(rss_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_009'] = {'inputs': ['rss_replacement_008'], 'func': rss_replacement_d2_009}


def rss_replacement_d2_010(rss_replacement_009):
    feature = _clean(rss_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_010'] = {'inputs': ['rss_replacement_009'], 'func': rss_replacement_d2_010}


def rss_replacement_d2_011(rss_replacement_010):
    feature = _clean(rss_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_011'] = {'inputs': ['rss_replacement_010'], 'func': rss_replacement_d2_011}


def rss_replacement_d2_012(rss_replacement_011):
    feature = _clean(rss_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_012'] = {'inputs': ['rss_replacement_011'], 'func': rss_replacement_d2_012}


def rss_replacement_d2_013(rss_replacement_012):
    feature = _clean(rss_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_013'] = {'inputs': ['rss_replacement_012'], 'func': rss_replacement_d2_013}


def rss_replacement_d2_014(rss_replacement_013):
    feature = _clean(rss_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_014'] = {'inputs': ['rss_replacement_013'], 'func': rss_replacement_d2_014}


def rss_replacement_d2_015(rss_replacement_014):
    feature = _clean(rss_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_015'] = {'inputs': ['rss_replacement_014'], 'func': rss_replacement_d2_015}


def rss_replacement_d2_016(rss_replacement_015):
    feature = _clean(rss_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_016'] = {'inputs': ['rss_replacement_015'], 'func': rss_replacement_d2_016}


def rss_replacement_d2_017(rss_replacement_016):
    feature = _clean(rss_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_017'] = {'inputs': ['rss_replacement_016'], 'func': rss_replacement_d2_017}


def rss_replacement_d2_018(rss_replacement_017):
    feature = _clean(rss_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_018'] = {'inputs': ['rss_replacement_017'], 'func': rss_replacement_d2_018}


def rss_replacement_d2_019(rss_replacement_018):
    feature = _clean(rss_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_019'] = {'inputs': ['rss_replacement_018'], 'func': rss_replacement_d2_019}


def rss_replacement_d2_020(rss_replacement_019):
    feature = _clean(rss_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_020'] = {'inputs': ['rss_replacement_019'], 'func': rss_replacement_d2_020}


def rss_replacement_d2_021(rss_replacement_020):
    feature = _clean(rss_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_021'] = {'inputs': ['rss_replacement_020'], 'func': rss_replacement_d2_021}


def rss_replacement_d2_022(rss_replacement_021):
    feature = _clean(rss_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_022'] = {'inputs': ['rss_replacement_021'], 'func': rss_replacement_d2_022}


def rss_replacement_d2_023(rss_replacement_022):
    feature = _clean(rss_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_023'] = {'inputs': ['rss_replacement_022'], 'func': rss_replacement_d2_023}


def rss_replacement_d2_024(rss_replacement_023):
    feature = _clean(rss_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_024'] = {'inputs': ['rss_replacement_023'], 'func': rss_replacement_d2_024}


def rss_replacement_d2_025(rss_replacement_024):
    feature = _clean(rss_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_025'] = {'inputs': ['rss_replacement_024'], 'func': rss_replacement_d2_025}


def rss_replacement_d2_026(rss_replacement_025):
    feature = _clean(rss_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_026'] = {'inputs': ['rss_replacement_025'], 'func': rss_replacement_d2_026}


def rss_replacement_d2_027(rss_replacement_026):
    feature = _clean(rss_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_027'] = {'inputs': ['rss_replacement_026'], 'func': rss_replacement_d2_027}


def rss_replacement_d2_028(rss_replacement_027):
    feature = _clean(rss_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_028'] = {'inputs': ['rss_replacement_027'], 'func': rss_replacement_d2_028}


def rss_replacement_d2_029(rss_replacement_028):
    feature = _clean(rss_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_029'] = {'inputs': ['rss_replacement_028'], 'func': rss_replacement_d2_029}


def rss_replacement_d2_030(rss_replacement_029):
    feature = _clean(rss_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_030'] = {'inputs': ['rss_replacement_029'], 'func': rss_replacement_d2_030}


def rss_replacement_d2_031(rss_replacement_030):
    feature = _clean(rss_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_031'] = {'inputs': ['rss_replacement_030'], 'func': rss_replacement_d2_031}


def rss_replacement_d2_032(rss_replacement_031):
    feature = _clean(rss_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_032'] = {'inputs': ['rss_replacement_031'], 'func': rss_replacement_d2_032}


def rss_replacement_d2_033(rss_replacement_032):
    feature = _clean(rss_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_033'] = {'inputs': ['rss_replacement_032'], 'func': rss_replacement_d2_033}


def rss_replacement_d2_034(rss_replacement_033):
    feature = _clean(rss_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_034'] = {'inputs': ['rss_replacement_033'], 'func': rss_replacement_d2_034}


def rss_replacement_d2_035(rss_replacement_034):
    feature = _clean(rss_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_035'] = {'inputs': ['rss_replacement_034'], 'func': rss_replacement_d2_035}


def rss_replacement_d2_036(rss_replacement_035):
    feature = _clean(rss_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_036'] = {'inputs': ['rss_replacement_035'], 'func': rss_replacement_d2_036}


def rss_replacement_d2_037(rss_replacement_036):
    feature = _clean(rss_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_037'] = {'inputs': ['rss_replacement_036'], 'func': rss_replacement_d2_037}


def rss_replacement_d2_038(rss_replacement_037):
    feature = _clean(rss_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_038'] = {'inputs': ['rss_replacement_037'], 'func': rss_replacement_d2_038}


def rss_replacement_d2_039(rss_replacement_038):
    feature = _clean(rss_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_039'] = {'inputs': ['rss_replacement_038'], 'func': rss_replacement_d2_039}


def rss_replacement_d2_040(rss_replacement_039):
    feature = _clean(rss_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_040'] = {'inputs': ['rss_replacement_039'], 'func': rss_replacement_d2_040}


def rss_replacement_d2_041(rss_replacement_040):
    feature = _clean(rss_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_041'] = {'inputs': ['rss_replacement_040'], 'func': rss_replacement_d2_041}


def rss_replacement_d2_042(rss_replacement_041):
    feature = _clean(rss_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_042'] = {'inputs': ['rss_replacement_041'], 'func': rss_replacement_d2_042}


def rss_replacement_d2_043(rss_replacement_042):
    feature = _clean(rss_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_043'] = {'inputs': ['rss_replacement_042'], 'func': rss_replacement_d2_043}


def rss_replacement_d2_044(rss_replacement_043):
    feature = _clean(rss_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_044'] = {'inputs': ['rss_replacement_043'], 'func': rss_replacement_d2_044}


def rss_replacement_d2_045(rss_replacement_044):
    feature = _clean(rss_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_045'] = {'inputs': ['rss_replacement_044'], 'func': rss_replacement_d2_045}


def rss_replacement_d2_046(rss_replacement_045):
    feature = _clean(rss_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_046'] = {'inputs': ['rss_replacement_045'], 'func': rss_replacement_d2_046}


def rss_replacement_d2_047(rss_replacement_046):
    feature = _clean(rss_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_047'] = {'inputs': ['rss_replacement_046'], 'func': rss_replacement_d2_047}


def rss_replacement_d2_048(rss_replacement_047):
    feature = _clean(rss_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_048'] = {'inputs': ['rss_replacement_047'], 'func': rss_replacement_d2_048}


def rss_replacement_d2_049(rss_replacement_048):
    feature = _clean(rss_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_049'] = {'inputs': ['rss_replacement_048'], 'func': rss_replacement_d2_049}


def rss_replacement_d2_050(rss_replacement_049):
    feature = _clean(rss_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_050'] = {'inputs': ['rss_replacement_049'], 'func': rss_replacement_d2_050}


def rss_replacement_d2_051(rss_replacement_050):
    feature = _clean(rss_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_051'] = {'inputs': ['rss_replacement_050'], 'func': rss_replacement_d2_051}


def rss_replacement_d2_052(rss_replacement_051):
    feature = _clean(rss_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_052'] = {'inputs': ['rss_replacement_051'], 'func': rss_replacement_d2_052}


def rss_replacement_d2_053(rss_replacement_052):
    feature = _clean(rss_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_053'] = {'inputs': ['rss_replacement_052'], 'func': rss_replacement_d2_053}


def rss_replacement_d2_054(rss_replacement_053):
    feature = _clean(rss_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_054'] = {'inputs': ['rss_replacement_053'], 'func': rss_replacement_d2_054}


def rss_replacement_d2_055(rss_replacement_054):
    feature = _clean(rss_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_055'] = {'inputs': ['rss_replacement_054'], 'func': rss_replacement_d2_055}


def rss_replacement_d2_056(rss_replacement_055):
    feature = _clean(rss_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_056'] = {'inputs': ['rss_replacement_055'], 'func': rss_replacement_d2_056}


def rss_replacement_d2_057(rss_replacement_056):
    feature = _clean(rss_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_057'] = {'inputs': ['rss_replacement_056'], 'func': rss_replacement_d2_057}


def rss_replacement_d2_058(rss_replacement_057):
    feature = _clean(rss_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_058'] = {'inputs': ['rss_replacement_057'], 'func': rss_replacement_d2_058}


def rss_replacement_d2_059(rss_replacement_058):
    feature = _clean(rss_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_059'] = {'inputs': ['rss_replacement_058'], 'func': rss_replacement_d2_059}


def rss_replacement_d2_060(rss_replacement_059):
    feature = _clean(rss_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_060'] = {'inputs': ['rss_replacement_059'], 'func': rss_replacement_d2_060}


def rss_replacement_d2_061(rss_replacement_060):
    feature = _clean(rss_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_061'] = {'inputs': ['rss_replacement_060'], 'func': rss_replacement_d2_061}


def rss_replacement_d2_062(rss_replacement_061):
    feature = _clean(rss_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_062'] = {'inputs': ['rss_replacement_061'], 'func': rss_replacement_d2_062}


def rss_replacement_d2_063(rss_replacement_062):
    feature = _clean(rss_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_063'] = {'inputs': ['rss_replacement_062'], 'func': rss_replacement_d2_063}


def rss_replacement_d2_064(rss_replacement_063):
    feature = _clean(rss_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_064'] = {'inputs': ['rss_replacement_063'], 'func': rss_replacement_d2_064}


def rss_replacement_d2_065(rss_replacement_064):
    feature = _clean(rss_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_065'] = {'inputs': ['rss_replacement_064'], 'func': rss_replacement_d2_065}


def rss_replacement_d2_066(rss_replacement_065):
    feature = _clean(rss_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_066'] = {'inputs': ['rss_replacement_065'], 'func': rss_replacement_d2_066}


def rss_replacement_d2_067(rss_replacement_066):
    feature = _clean(rss_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_067'] = {'inputs': ['rss_replacement_066'], 'func': rss_replacement_d2_067}


def rss_replacement_d2_068(rss_replacement_067):
    feature = _clean(rss_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_068'] = {'inputs': ['rss_replacement_067'], 'func': rss_replacement_d2_068}


def rss_replacement_d2_069(rss_replacement_068):
    feature = _clean(rss_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_069'] = {'inputs': ['rss_replacement_068'], 'func': rss_replacement_d2_069}


def rss_replacement_d2_070(rss_replacement_069):
    feature = _clean(rss_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_070'] = {'inputs': ['rss_replacement_069'], 'func': rss_replacement_d2_070}


def rss_replacement_d2_071(rss_replacement_070):
    feature = _clean(rss_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_071'] = {'inputs': ['rss_replacement_070'], 'func': rss_replacement_d2_071}


def rss_replacement_d2_072(rss_replacement_071):
    feature = _clean(rss_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_072'] = {'inputs': ['rss_replacement_071'], 'func': rss_replacement_d2_072}


def rss_replacement_d2_073(rss_replacement_072):
    feature = _clean(rss_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_073'] = {'inputs': ['rss_replacement_072'], 'func': rss_replacement_d2_073}


def rss_replacement_d2_074(rss_replacement_073):
    feature = _clean(rss_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_074'] = {'inputs': ['rss_replacement_073'], 'func': rss_replacement_d2_074}


def rss_replacement_d2_075(rss_replacement_074):
    feature = _clean(rss_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_075'] = {'inputs': ['rss_replacement_074'], 'func': rss_replacement_d2_075}


def rss_replacement_d2_076(rss_replacement_075):
    feature = _clean(rss_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_076'] = {'inputs': ['rss_replacement_075'], 'func': rss_replacement_d2_076}


def rss_replacement_d2_077(rss_replacement_076):
    feature = _clean(rss_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_077'] = {'inputs': ['rss_replacement_076'], 'func': rss_replacement_d2_077}


def rss_replacement_d2_078(rss_replacement_077):
    feature = _clean(rss_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_078'] = {'inputs': ['rss_replacement_077'], 'func': rss_replacement_d2_078}


def rss_replacement_d2_079(rss_replacement_078):
    feature = _clean(rss_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_079'] = {'inputs': ['rss_replacement_078'], 'func': rss_replacement_d2_079}


def rss_replacement_d2_080(rss_replacement_079):
    feature = _clean(rss_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_080'] = {'inputs': ['rss_replacement_079'], 'func': rss_replacement_d2_080}


def rss_replacement_d2_081(rss_replacement_080):
    feature = _clean(rss_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_081'] = {'inputs': ['rss_replacement_080'], 'func': rss_replacement_d2_081}


def rss_replacement_d2_082(rss_replacement_081):
    feature = _clean(rss_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_082'] = {'inputs': ['rss_replacement_081'], 'func': rss_replacement_d2_082}


def rss_replacement_d2_083(rss_replacement_082):
    feature = _clean(rss_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_083'] = {'inputs': ['rss_replacement_082'], 'func': rss_replacement_d2_083}


def rss_replacement_d2_084(rss_replacement_083):
    feature = _clean(rss_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_084'] = {'inputs': ['rss_replacement_083'], 'func': rss_replacement_d2_084}


def rss_replacement_d2_085(rss_replacement_084):
    feature = _clean(rss_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_085'] = {'inputs': ['rss_replacement_084'], 'func': rss_replacement_d2_085}


def rss_replacement_d2_086(rss_replacement_085):
    feature = _clean(rss_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_086'] = {'inputs': ['rss_replacement_085'], 'func': rss_replacement_d2_086}


def rss_replacement_d2_087(rss_replacement_086):
    feature = _clean(rss_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_087'] = {'inputs': ['rss_replacement_086'], 'func': rss_replacement_d2_087}


def rss_replacement_d2_088(rss_replacement_087):
    feature = _clean(rss_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_088'] = {'inputs': ['rss_replacement_087'], 'func': rss_replacement_d2_088}


def rss_replacement_d2_089(rss_replacement_088):
    feature = _clean(rss_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_089'] = {'inputs': ['rss_replacement_088'], 'func': rss_replacement_d2_089}


def rss_replacement_d2_090(rss_replacement_089):
    feature = _clean(rss_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_090'] = {'inputs': ['rss_replacement_089'], 'func': rss_replacement_d2_090}


def rss_replacement_d2_091(rss_replacement_090):
    feature = _clean(rss_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_091'] = {'inputs': ['rss_replacement_090'], 'func': rss_replacement_d2_091}


def rss_replacement_d2_092(rss_replacement_091):
    feature = _clean(rss_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_092'] = {'inputs': ['rss_replacement_091'], 'func': rss_replacement_d2_092}


def rss_replacement_d2_093(rss_replacement_092):
    feature = _clean(rss_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_093'] = {'inputs': ['rss_replacement_092'], 'func': rss_replacement_d2_093}


def rss_replacement_d2_094(rss_replacement_093):
    feature = _clean(rss_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_094'] = {'inputs': ['rss_replacement_093'], 'func': rss_replacement_d2_094}


def rss_replacement_d2_095(rss_replacement_094):
    feature = _clean(rss_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_095'] = {'inputs': ['rss_replacement_094'], 'func': rss_replacement_d2_095}


def rss_replacement_d2_096(rss_replacement_095):
    feature = _clean(rss_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_096'] = {'inputs': ['rss_replacement_095'], 'func': rss_replacement_d2_096}


def rss_replacement_d2_097(rss_replacement_096):
    feature = _clean(rss_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_097'] = {'inputs': ['rss_replacement_096'], 'func': rss_replacement_d2_097}


def rss_replacement_d2_098(rss_replacement_097):
    feature = _clean(rss_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_098'] = {'inputs': ['rss_replacement_097'], 'func': rss_replacement_d2_098}


def rss_replacement_d2_099(rss_replacement_098):
    feature = _clean(rss_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_099'] = {'inputs': ['rss_replacement_098'], 'func': rss_replacement_d2_099}


def rss_replacement_d2_100(rss_replacement_099):
    feature = _clean(rss_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_100'] = {'inputs': ['rss_replacement_099'], 'func': rss_replacement_d2_100}


def rss_replacement_d2_101(rss_replacement_100):
    feature = _clean(rss_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_101'] = {'inputs': ['rss_replacement_100'], 'func': rss_replacement_d2_101}


def rss_replacement_d2_102(rss_replacement_101):
    feature = _clean(rss_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_102'] = {'inputs': ['rss_replacement_101'], 'func': rss_replacement_d2_102}


def rss_replacement_d2_103(rss_replacement_102):
    feature = _clean(rss_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_103'] = {'inputs': ['rss_replacement_102'], 'func': rss_replacement_d2_103}


def rss_replacement_d2_104(rss_replacement_103):
    feature = _clean(rss_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_104'] = {'inputs': ['rss_replacement_103'], 'func': rss_replacement_d2_104}


def rss_replacement_d2_105(rss_replacement_104):
    feature = _clean(rss_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_105'] = {'inputs': ['rss_replacement_104'], 'func': rss_replacement_d2_105}


def rss_replacement_d2_106(rss_replacement_105):
    feature = _clean(rss_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_106'] = {'inputs': ['rss_replacement_105'], 'func': rss_replacement_d2_106}


def rss_replacement_d2_107(rss_replacement_106):
    feature = _clean(rss_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_107'] = {'inputs': ['rss_replacement_106'], 'func': rss_replacement_d2_107}


def rss_replacement_d2_108(rss_replacement_107):
    feature = _clean(rss_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_108'] = {'inputs': ['rss_replacement_107'], 'func': rss_replacement_d2_108}


def rss_replacement_d2_109(rss_replacement_108):
    feature = _clean(rss_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_109'] = {'inputs': ['rss_replacement_108'], 'func': rss_replacement_d2_109}


def rss_replacement_d2_110(rss_replacement_109):
    feature = _clean(rss_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_110'] = {'inputs': ['rss_replacement_109'], 'func': rss_replacement_d2_110}


def rss_replacement_d2_111(rss_replacement_110):
    feature = _clean(rss_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_111'] = {'inputs': ['rss_replacement_110'], 'func': rss_replacement_d2_111}


def rss_replacement_d2_112(rss_replacement_111):
    feature = _clean(rss_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_112'] = {'inputs': ['rss_replacement_111'], 'func': rss_replacement_d2_112}


def rss_replacement_d2_113(rss_replacement_112):
    feature = _clean(rss_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_113'] = {'inputs': ['rss_replacement_112'], 'func': rss_replacement_d2_113}


def rss_replacement_d2_114(rss_replacement_113):
    feature = _clean(rss_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_114'] = {'inputs': ['rss_replacement_113'], 'func': rss_replacement_d2_114}


def rss_replacement_d2_115(rss_replacement_114):
    feature = _clean(rss_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_115'] = {'inputs': ['rss_replacement_114'], 'func': rss_replacement_d2_115}


def rss_replacement_d2_116(rss_replacement_115):
    feature = _clean(rss_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_116'] = {'inputs': ['rss_replacement_115'], 'func': rss_replacement_d2_116}


def rss_replacement_d2_117(rss_replacement_116):
    feature = _clean(rss_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_117'] = {'inputs': ['rss_replacement_116'], 'func': rss_replacement_d2_117}


def rss_replacement_d2_118(rss_replacement_117):
    feature = _clean(rss_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_118'] = {'inputs': ['rss_replacement_117'], 'func': rss_replacement_d2_118}


def rss_replacement_d2_119(rss_replacement_118):
    feature = _clean(rss_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_119'] = {'inputs': ['rss_replacement_118'], 'func': rss_replacement_d2_119}


def rss_replacement_d2_120(rss_replacement_119):
    feature = _clean(rss_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_120'] = {'inputs': ['rss_replacement_119'], 'func': rss_replacement_d2_120}


def rss_replacement_d2_121(rss_replacement_120):
    feature = _clean(rss_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_121'] = {'inputs': ['rss_replacement_120'], 'func': rss_replacement_d2_121}


def rss_replacement_d2_122(rss_replacement_121):
    feature = _clean(rss_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_122'] = {'inputs': ['rss_replacement_121'], 'func': rss_replacement_d2_122}


def rss_replacement_d2_123(rss_replacement_122):
    feature = _clean(rss_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_123'] = {'inputs': ['rss_replacement_122'], 'func': rss_replacement_d2_123}


def rss_replacement_d2_124(rss_replacement_123):
    feature = _clean(rss_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_124'] = {'inputs': ['rss_replacement_123'], 'func': rss_replacement_d2_124}


def rss_replacement_d2_125(rss_replacement_124):
    feature = _clean(rss_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_125'] = {'inputs': ['rss_replacement_124'], 'func': rss_replacement_d2_125}


def rss_replacement_d2_126(rss_replacement_125):
    feature = _clean(rss_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_126'] = {'inputs': ['rss_replacement_125'], 'func': rss_replacement_d2_126}


def rss_replacement_d2_127(rss_replacement_126):
    feature = _clean(rss_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_127'] = {'inputs': ['rss_replacement_126'], 'func': rss_replacement_d2_127}


def rss_replacement_d2_128(rss_replacement_127):
    feature = _clean(rss_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_128'] = {'inputs': ['rss_replacement_127'], 'func': rss_replacement_d2_128}


def rss_replacement_d2_129(rss_replacement_128):
    feature = _clean(rss_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_129'] = {'inputs': ['rss_replacement_128'], 'func': rss_replacement_d2_129}


def rss_replacement_d2_130(rss_replacement_129):
    feature = _clean(rss_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_130'] = {'inputs': ['rss_replacement_129'], 'func': rss_replacement_d2_130}


def rss_replacement_d2_131(rss_replacement_130):
    feature = _clean(rss_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_131'] = {'inputs': ['rss_replacement_130'], 'func': rss_replacement_d2_131}


def rss_replacement_d2_132(rss_replacement_131):
    feature = _clean(rss_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_132'] = {'inputs': ['rss_replacement_131'], 'func': rss_replacement_d2_132}


def rss_replacement_d2_133(rss_replacement_132):
    feature = _clean(rss_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_133'] = {'inputs': ['rss_replacement_132'], 'func': rss_replacement_d2_133}


def rss_replacement_d2_134(rss_replacement_133):
    feature = _clean(rss_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_134'] = {'inputs': ['rss_replacement_133'], 'func': rss_replacement_d2_134}


def rss_replacement_d2_135(rss_replacement_134):
    feature = _clean(rss_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_135'] = {'inputs': ['rss_replacement_134'], 'func': rss_replacement_d2_135}


def rss_replacement_d2_136(rss_replacement_135):
    feature = _clean(rss_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_136'] = {'inputs': ['rss_replacement_135'], 'func': rss_replacement_d2_136}


def rss_replacement_d2_137(rss_replacement_136):
    feature = _clean(rss_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_137'] = {'inputs': ['rss_replacement_136'], 'func': rss_replacement_d2_137}


def rss_replacement_d2_138(rss_replacement_137):
    feature = _clean(rss_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_138'] = {'inputs': ['rss_replacement_137'], 'func': rss_replacement_d2_138}


def rss_replacement_d2_139(rss_replacement_138):
    feature = _clean(rss_replacement_138)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_139'] = {'inputs': ['rss_replacement_138'], 'func': rss_replacement_d2_139}


def rss_replacement_d2_140(rss_replacement_139):
    feature = _clean(rss_replacement_139)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_140'] = {'inputs': ['rss_replacement_139'], 'func': rss_replacement_d2_140}


def rss_replacement_d2_141(rss_replacement_140):
    feature = _clean(rss_replacement_140)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_141'] = {'inputs': ['rss_replacement_140'], 'func': rss_replacement_d2_141}


def rss_replacement_d2_142(rss_replacement_141):
    feature = _clean(rss_replacement_141)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_142'] = {'inputs': ['rss_replacement_141'], 'func': rss_replacement_d2_142}


def rss_replacement_d2_143(rss_replacement_142):
    feature = _clean(rss_replacement_142)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_143'] = {'inputs': ['rss_replacement_142'], 'func': rss_replacement_d2_143}


def rss_replacement_d2_144(rss_replacement_143):
    feature = _clean(rss_replacement_143)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_144'] = {'inputs': ['rss_replacement_143'], 'func': rss_replacement_d2_144}


def rss_replacement_d2_145(rss_replacement_144):
    feature = _clean(rss_replacement_144)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_145'] = {'inputs': ['rss_replacement_144'], 'func': rss_replacement_d2_145}


def rss_replacement_d2_146(rss_replacement_145):
    feature = _clean(rss_replacement_145)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_146'] = {'inputs': ['rss_replacement_145'], 'func': rss_replacement_d2_146}


def rss_replacement_d2_147(rss_replacement_146):
    feature = _clean(rss_replacement_146)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_147'] = {'inputs': ['rss_replacement_146'], 'func': rss_replacement_d2_147}


def rss_replacement_d2_148(rss_replacement_147):
    feature = _clean(rss_replacement_147)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_148'] = {'inputs': ['rss_replacement_147'], 'func': rss_replacement_d2_148}


def rss_replacement_d2_149(rss_replacement_148):
    feature = _clean(rss_replacement_148)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_149'] = {'inputs': ['rss_replacement_148'], 'func': rss_replacement_d2_149}


def rss_replacement_d2_150(rss_replacement_149):
    feature = _clean(rss_replacement_149)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_150'] = {'inputs': ['rss_replacement_149'], 'func': rss_replacement_d2_150}


def rss_replacement_d2_151(rss_replacement_150):
    feature = _clean(rss_replacement_150)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RSS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rss_replacement_d2_151'] = {'inputs': ['rss_replacement_150'], 'func': rss_replacement_d2_151}


# Base-universe derivative extensions for repaired first-base features.
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rss_base_universe_d2_001_rss_002_dividend_suspension_density_42(rss_002_dividend_suspension_density_42):
    return _base_universe_d2(rss_002_dividend_suspension_density_42, 1)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_001_rss_002_dividend_suspension_density_42'] = {'inputs': ['rss_002_dividend_suspension_density_42'], 'func': rss_base_universe_d2_001_rss_002_dividend_suspension_density_42}


def rss_base_universe_d2_002_rss_003_reverse_split_density_63(rss_003_reverse_split_density_63):
    return _base_universe_d2(rss_003_reverse_split_density_63, 2)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_002_rss_003_reverse_split_density_63'] = {'inputs': ['rss_003_reverse_split_density_63'], 'func': rss_base_universe_d2_002_rss_003_reverse_split_density_63}


def rss_base_universe_d2_003_rss_004_event_density_z_84(rss_004_event_density_z_84):
    return _base_universe_d2(rss_004_event_density_z_84, 3)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_003_rss_004_event_density_z_84'] = {'inputs': ['rss_004_event_density_z_84'], 'func': rss_base_universe_d2_003_rss_004_event_density_z_84}


def rss_base_universe_d2_004_rss_005_going_concern_persistence_126(rss_005_going_concern_persistence_126):
    return _base_universe_d2(rss_005_going_concern_persistence_126, 4)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_004_rss_005_going_concern_persistence_126'] = {'inputs': ['rss_005_going_concern_persistence_126'], 'func': rss_base_universe_d2_004_rss_005_going_concern_persistence_126}


def rss_base_universe_d2_005_rss_006_delisting_notice_density_189(rss_006_delisting_notice_density_189):
    return _base_universe_d2(rss_006_delisting_notice_density_189, 5)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_005_rss_006_delisting_notice_density_189'] = {'inputs': ['rss_006_delisting_notice_density_189'], 'func': rss_base_universe_d2_005_rss_006_delisting_notice_density_189}


def rss_base_universe_d2_006_rss_008_dividend_cut_density_378(rss_008_dividend_cut_density_378):
    return _base_universe_d2(rss_008_dividend_cut_density_378, 6)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_006_rss_008_dividend_cut_density_378'] = {'inputs': ['rss_008_dividend_cut_density_378'], 'func': rss_base_universe_d2_006_rss_008_dividend_cut_density_378}


def rss_base_universe_d2_007_rss_009_dividend_suspension_density_504(rss_009_dividend_suspension_density_504):
    return _base_universe_d2(rss_009_dividend_suspension_density_504, 7)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_007_rss_009_dividend_suspension_density_504'] = {'inputs': ['rss_009_dividend_suspension_density_504'], 'func': rss_base_universe_d2_007_rss_009_dividend_suspension_density_504}


def rss_base_universe_d2_008_rss_010_reverse_split_density_756(rss_010_reverse_split_density_756):
    return _base_universe_d2(rss_010_reverse_split_density_756, 8)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_008_rss_010_reverse_split_density_756'] = {'inputs': ['rss_010_reverse_split_density_756'], 'func': rss_base_universe_d2_008_rss_010_reverse_split_density_756}


def rss_base_universe_d2_009_rss_011_event_density_z_1008(rss_011_event_density_z_1008):
    return _base_universe_d2(rss_011_event_density_z_1008, 9)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_009_rss_011_event_density_z_1008'] = {'inputs': ['rss_011_event_density_z_1008'], 'func': rss_base_universe_d2_009_rss_011_event_density_z_1008}


def rss_base_universe_d2_010_rss_012_going_concern_persistence_1260(rss_012_going_concern_persistence_1260):
    return _base_universe_d2(rss_012_going_concern_persistence_1260, 10)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_010_rss_012_going_concern_persistence_1260'] = {'inputs': ['rss_012_going_concern_persistence_1260'], 'func': rss_base_universe_d2_010_rss_012_going_concern_persistence_1260}


def rss_base_universe_d2_011_rss_015_dividend_cut_density_252(rss_015_dividend_cut_density_252):
    return _base_universe_d2(rss_015_dividend_cut_density_252, 11)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_011_rss_015_dividend_cut_density_252'] = {'inputs': ['rss_015_dividend_cut_density_252'], 'func': rss_base_universe_d2_011_rss_015_dividend_cut_density_252}


def rss_base_universe_d2_012_rss_018_event_density_z_63(rss_018_event_density_z_63):
    return _base_universe_d2(rss_018_event_density_z_63, 12)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_012_rss_018_event_density_z_63'] = {'inputs': ['rss_018_event_density_z_63'], 'func': rss_base_universe_d2_012_rss_018_event_density_z_63}


def rss_base_universe_d2_013_rss_020_delisting_notice_density_126(rss_020_delisting_notice_density_126):
    return _base_universe_d2(rss_020_delisting_notice_density_126, 13)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_013_rss_020_delisting_notice_density_126'] = {'inputs': ['rss_020_delisting_notice_density_126'], 'func': rss_base_universe_d2_013_rss_020_delisting_notice_density_126}


def rss_base_universe_d2_014_rss_026_going_concern_persistence_1008(rss_026_going_concern_persistence_1008):
    return _base_universe_d2(rss_026_going_concern_persistence_1008, 14)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_014_rss_026_going_concern_persistence_1008'] = {'inputs': ['rss_026_going_concern_persistence_1008'], 'func': rss_base_universe_d2_014_rss_026_going_concern_persistence_1008}


def rss_base_universe_d2_015_rss_027_delisting_notice_density_1260(rss_027_delisting_notice_density_1260):
    return _base_universe_d2(rss_027_delisting_notice_density_1260, 15)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_015_rss_027_delisting_notice_density_1260'] = {'inputs': ['rss_027_delisting_notice_density_1260'], 'func': rss_base_universe_d2_015_rss_027_delisting_notice_density_1260}


def rss_base_universe_d2_016_rss_032_event_density_z_42(rss_032_event_density_z_42):
    return _base_universe_d2(rss_032_event_density_z_42, 16)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_016_rss_032_event_density_z_42'] = {'inputs': ['rss_032_event_density_z_42'], 'func': rss_base_universe_d2_016_rss_032_event_density_z_42}


def rss_base_universe_d2_017_rss_033_going_concern_persistence_63(rss_033_going_concern_persistence_63):
    return _base_universe_d2(rss_033_going_concern_persistence_63, 17)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_017_rss_033_going_concern_persistence_63'] = {'inputs': ['rss_033_going_concern_persistence_63'], 'func': rss_base_universe_d2_017_rss_033_going_concern_persistence_63}


def rss_base_universe_d2_018_rss_034_delisting_notice_density_84(rss_034_delisting_notice_density_84):
    return _base_universe_d2(rss_034_delisting_notice_density_84, 18)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_018_rss_034_delisting_notice_density_84'] = {'inputs': ['rss_034_delisting_notice_density_84'], 'func': rss_base_universe_d2_018_rss_034_delisting_notice_density_84}


def rss_base_universe_d2_019_rss_039_event_density_z_504(rss_039_event_density_z_504):
    return _base_universe_d2(rss_039_event_density_z_504, 19)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_019_rss_039_event_density_z_504'] = {'inputs': ['rss_039_event_density_z_504'], 'func': rss_base_universe_d2_019_rss_039_event_density_z_504}


def rss_base_universe_d2_020_rss_040_going_concern_persistence_756(rss_040_going_concern_persistence_756):
    return _base_universe_d2(rss_040_going_concern_persistence_756, 20)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_020_rss_040_going_concern_persistence_756'] = {'inputs': ['rss_040_going_concern_persistence_756'], 'func': rss_base_universe_d2_020_rss_040_going_concern_persistence_756}


def rss_base_universe_d2_021_rss_041_delisting_notice_density_1008(rss_041_delisting_notice_density_1008):
    return _base_universe_d2(rss_041_delisting_notice_density_1008, 21)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_021_rss_041_delisting_notice_density_1008'] = {'inputs': ['rss_041_delisting_notice_density_1008'], 'func': rss_base_universe_d2_021_rss_041_delisting_notice_density_1008}


def rss_base_universe_d2_022_rss_046_event_density_z_21(rss_046_event_density_z_21):
    return _base_universe_d2(rss_046_event_density_z_21, 22)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_022_rss_046_event_density_z_21'] = {'inputs': ['rss_046_event_density_z_21'], 'func': rss_base_universe_d2_022_rss_046_event_density_z_21}


def rss_base_universe_d2_023_rss_047_going_concern_persistence_42(rss_047_going_concern_persistence_42):
    return _base_universe_d2(rss_047_going_concern_persistence_42, 23)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_023_rss_047_going_concern_persistence_42'] = {'inputs': ['rss_047_going_concern_persistence_42'], 'func': rss_base_universe_d2_023_rss_047_going_concern_persistence_42}


def rss_base_universe_d2_024_rss_053_event_density_z_378(rss_053_event_density_z_378):
    return _base_universe_d2(rss_053_event_density_z_378, 24)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_024_rss_053_event_density_z_378'] = {'inputs': ['rss_053_event_density_z_378'], 'func': rss_base_universe_d2_024_rss_053_event_density_z_378}


def rss_base_universe_d2_025_rss_054_going_concern_persistence_504(rss_054_going_concern_persistence_504):
    return _base_universe_d2(rss_054_going_concern_persistence_504, 25)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_025_rss_054_going_concern_persistence_504'] = {'inputs': ['rss_054_going_concern_persistence_504'], 'func': rss_base_universe_d2_025_rss_054_going_concern_persistence_504}


def rss_base_universe_d2_026_rss_060_event_density_z_252(rss_060_event_density_z_252):
    return _base_universe_d2(rss_060_event_density_z_252, 26)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_026_rss_060_event_density_z_252'] = {'inputs': ['rss_060_event_density_z_252'], 'func': rss_base_universe_d2_026_rss_060_event_density_z_252}


def rss_base_universe_d2_027_rss_061_going_concern_persistence_21(rss_061_going_concern_persistence_21):
    return _base_universe_d2(rss_061_going_concern_persistence_21, 27)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_027_rss_061_going_concern_persistence_21'] = {'inputs': ['rss_061_going_concern_persistence_21'], 'func': rss_base_universe_d2_027_rss_061_going_concern_persistence_21}


def rss_base_universe_d2_028_rss_068_going_concern_persistence_378(rss_068_going_concern_persistence_378):
    return _base_universe_d2(rss_068_going_concern_persistence_378, 28)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_028_rss_068_going_concern_persistence_378'] = {'inputs': ['rss_068_going_concern_persistence_378'], 'func': rss_base_universe_d2_028_rss_068_going_concern_persistence_378}


def rss_base_universe_d2_029_rss_075_going_concern_persistence_252(rss_075_going_concern_persistence_252):
    return _base_universe_d2(rss_075_going_concern_persistence_252, 29)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_029_rss_075_going_concern_persistence_252'] = {'inputs': ['rss_075_going_concern_persistence_252'], 'func': rss_base_universe_d2_029_rss_075_going_concern_persistence_252}


def rss_base_universe_d2_030_rss_basefill_007(rss_basefill_007):
    return _base_universe_d2(rss_basefill_007, 30)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_030_rss_basefill_007'] = {'inputs': ['rss_basefill_007'], 'func': rss_base_universe_d2_030_rss_basefill_007}


def rss_base_universe_d2_031_rss_basefill_014(rss_basefill_014):
    return _base_universe_d2(rss_basefill_014, 31)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_031_rss_basefill_014'] = {'inputs': ['rss_basefill_014'], 'func': rss_base_universe_d2_031_rss_basefill_014}


def rss_base_universe_d2_032_rss_basefill_016(rss_basefill_016):
    return _base_universe_d2(rss_basefill_016, 32)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_032_rss_basefill_016'] = {'inputs': ['rss_basefill_016'], 'func': rss_base_universe_d2_032_rss_basefill_016}


def rss_base_universe_d2_033_rss_basefill_017(rss_basefill_017):
    return _base_universe_d2(rss_basefill_017, 33)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_033_rss_basefill_017'] = {'inputs': ['rss_basefill_017'], 'func': rss_base_universe_d2_033_rss_basefill_017}


def rss_base_universe_d2_034_rss_basefill_021(rss_basefill_021):
    return _base_universe_d2(rss_basefill_021, 34)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_034_rss_basefill_021'] = {'inputs': ['rss_basefill_021'], 'func': rss_base_universe_d2_034_rss_basefill_021}


def rss_base_universe_d2_035_rss_basefill_022(rss_basefill_022):
    return _base_universe_d2(rss_basefill_022, 35)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_035_rss_basefill_022'] = {'inputs': ['rss_basefill_022'], 'func': rss_base_universe_d2_035_rss_basefill_022}


def rss_base_universe_d2_036_rss_basefill_023(rss_basefill_023):
    return _base_universe_d2(rss_basefill_023, 36)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_036_rss_basefill_023'] = {'inputs': ['rss_basefill_023'], 'func': rss_base_universe_d2_036_rss_basefill_023}


def rss_base_universe_d2_037_rss_basefill_024(rss_basefill_024):
    return _base_universe_d2(rss_basefill_024, 37)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_037_rss_basefill_024'] = {'inputs': ['rss_basefill_024'], 'func': rss_base_universe_d2_037_rss_basefill_024}


def rss_base_universe_d2_038_rss_basefill_028(rss_basefill_028):
    return _base_universe_d2(rss_basefill_028, 38)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_038_rss_basefill_028'] = {'inputs': ['rss_basefill_028'], 'func': rss_base_universe_d2_038_rss_basefill_028}


def rss_base_universe_d2_039_rss_basefill_029(rss_basefill_029):
    return _base_universe_d2(rss_basefill_029, 39)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_039_rss_basefill_029'] = {'inputs': ['rss_basefill_029'], 'func': rss_base_universe_d2_039_rss_basefill_029}


def rss_base_universe_d2_040_rss_basefill_030(rss_basefill_030):
    return _base_universe_d2(rss_basefill_030, 40)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_040_rss_basefill_030'] = {'inputs': ['rss_basefill_030'], 'func': rss_base_universe_d2_040_rss_basefill_030}


def rss_base_universe_d2_041_rss_basefill_031(rss_basefill_031):
    return _base_universe_d2(rss_basefill_031, 41)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_041_rss_basefill_031'] = {'inputs': ['rss_basefill_031'], 'func': rss_base_universe_d2_041_rss_basefill_031}


def rss_base_universe_d2_042_rss_basefill_035(rss_basefill_035):
    return _base_universe_d2(rss_basefill_035, 42)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_042_rss_basefill_035'] = {'inputs': ['rss_basefill_035'], 'func': rss_base_universe_d2_042_rss_basefill_035}


def rss_base_universe_d2_043_rss_basefill_036(rss_basefill_036):
    return _base_universe_d2(rss_basefill_036, 43)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_043_rss_basefill_036'] = {'inputs': ['rss_basefill_036'], 'func': rss_base_universe_d2_043_rss_basefill_036}


def rss_base_universe_d2_044_rss_basefill_037(rss_basefill_037):
    return _base_universe_d2(rss_basefill_037, 44)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_044_rss_basefill_037'] = {'inputs': ['rss_basefill_037'], 'func': rss_base_universe_d2_044_rss_basefill_037}


def rss_base_universe_d2_045_rss_basefill_038(rss_basefill_038):
    return _base_universe_d2(rss_basefill_038, 45)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_045_rss_basefill_038'] = {'inputs': ['rss_basefill_038'], 'func': rss_base_universe_d2_045_rss_basefill_038}


def rss_base_universe_d2_046_rss_basefill_042(rss_basefill_042):
    return _base_universe_d2(rss_basefill_042, 46)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_046_rss_basefill_042'] = {'inputs': ['rss_basefill_042'], 'func': rss_base_universe_d2_046_rss_basefill_042}


def rss_base_universe_d2_047_rss_basefill_043(rss_basefill_043):
    return _base_universe_d2(rss_basefill_043, 47)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_047_rss_basefill_043'] = {'inputs': ['rss_basefill_043'], 'func': rss_base_universe_d2_047_rss_basefill_043}


def rss_base_universe_d2_048_rss_basefill_044(rss_basefill_044):
    return _base_universe_d2(rss_basefill_044, 48)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_048_rss_basefill_044'] = {'inputs': ['rss_basefill_044'], 'func': rss_base_universe_d2_048_rss_basefill_044}


def rss_base_universe_d2_049_rss_basefill_045(rss_basefill_045):
    return _base_universe_d2(rss_basefill_045, 49)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_049_rss_basefill_045'] = {'inputs': ['rss_basefill_045'], 'func': rss_base_universe_d2_049_rss_basefill_045}


def rss_base_universe_d2_050_rss_basefill_048(rss_basefill_048):
    return _base_universe_d2(rss_basefill_048, 50)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_050_rss_basefill_048'] = {'inputs': ['rss_basefill_048'], 'func': rss_base_universe_d2_050_rss_basefill_048}


def rss_base_universe_d2_051_rss_basefill_049(rss_basefill_049):
    return _base_universe_d2(rss_basefill_049, 51)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_051_rss_basefill_049'] = {'inputs': ['rss_basefill_049'], 'func': rss_base_universe_d2_051_rss_basefill_049}


def rss_base_universe_d2_052_rss_basefill_050(rss_basefill_050):
    return _base_universe_d2(rss_basefill_050, 52)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_052_rss_basefill_050'] = {'inputs': ['rss_basefill_050'], 'func': rss_base_universe_d2_052_rss_basefill_050}


def rss_base_universe_d2_053_rss_basefill_051(rss_basefill_051):
    return _base_universe_d2(rss_basefill_051, 53)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_053_rss_basefill_051'] = {'inputs': ['rss_basefill_051'], 'func': rss_base_universe_d2_053_rss_basefill_051}


def rss_base_universe_d2_054_rss_basefill_052(rss_basefill_052):
    return _base_universe_d2(rss_basefill_052, 54)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_054_rss_basefill_052'] = {'inputs': ['rss_basefill_052'], 'func': rss_base_universe_d2_054_rss_basefill_052}


def rss_base_universe_d2_055_rss_basefill_055(rss_basefill_055):
    return _base_universe_d2(rss_basefill_055, 55)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_055_rss_basefill_055'] = {'inputs': ['rss_basefill_055'], 'func': rss_base_universe_d2_055_rss_basefill_055}


def rss_base_universe_d2_056_rss_basefill_056(rss_basefill_056):
    return _base_universe_d2(rss_basefill_056, 56)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_056_rss_basefill_056'] = {'inputs': ['rss_basefill_056'], 'func': rss_base_universe_d2_056_rss_basefill_056}


def rss_base_universe_d2_057_rss_basefill_057(rss_basefill_057):
    return _base_universe_d2(rss_basefill_057, 57)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_057_rss_basefill_057'] = {'inputs': ['rss_basefill_057'], 'func': rss_base_universe_d2_057_rss_basefill_057}


def rss_base_universe_d2_058_rss_basefill_058(rss_basefill_058):
    return _base_universe_d2(rss_basefill_058, 58)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_058_rss_basefill_058'] = {'inputs': ['rss_basefill_058'], 'func': rss_base_universe_d2_058_rss_basefill_058}


def rss_base_universe_d2_059_rss_basefill_059(rss_basefill_059):
    return _base_universe_d2(rss_basefill_059, 59)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_059_rss_basefill_059'] = {'inputs': ['rss_basefill_059'], 'func': rss_base_universe_d2_059_rss_basefill_059}


def rss_base_universe_d2_060_rss_basefill_062(rss_basefill_062):
    return _base_universe_d2(rss_basefill_062, 60)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_060_rss_basefill_062'] = {'inputs': ['rss_basefill_062'], 'func': rss_base_universe_d2_060_rss_basefill_062}


def rss_base_universe_d2_061_rss_basefill_063(rss_basefill_063):
    return _base_universe_d2(rss_basefill_063, 61)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_061_rss_basefill_063'] = {'inputs': ['rss_basefill_063'], 'func': rss_base_universe_d2_061_rss_basefill_063}


def rss_base_universe_d2_062_rss_basefill_064(rss_basefill_064):
    return _base_universe_d2(rss_basefill_064, 62)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_062_rss_basefill_064'] = {'inputs': ['rss_basefill_064'], 'func': rss_base_universe_d2_062_rss_basefill_064}


def rss_base_universe_d2_063_rss_basefill_065(rss_basefill_065):
    return _base_universe_d2(rss_basefill_065, 63)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_063_rss_basefill_065'] = {'inputs': ['rss_basefill_065'], 'func': rss_base_universe_d2_063_rss_basefill_065}


def rss_base_universe_d2_064_rss_basefill_066(rss_basefill_066):
    return _base_universe_d2(rss_basefill_066, 64)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_064_rss_basefill_066'] = {'inputs': ['rss_basefill_066'], 'func': rss_base_universe_d2_064_rss_basefill_066}


def rss_base_universe_d2_065_rss_basefill_067(rss_basefill_067):
    return _base_universe_d2(rss_basefill_067, 65)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_065_rss_basefill_067'] = {'inputs': ['rss_basefill_067'], 'func': rss_base_universe_d2_065_rss_basefill_067}


def rss_base_universe_d2_066_rss_basefill_069(rss_basefill_069):
    return _base_universe_d2(rss_basefill_069, 66)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_066_rss_basefill_069'] = {'inputs': ['rss_basefill_069'], 'func': rss_base_universe_d2_066_rss_basefill_069}


def rss_base_universe_d2_067_rss_basefill_070(rss_basefill_070):
    return _base_universe_d2(rss_basefill_070, 67)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_067_rss_basefill_070'] = {'inputs': ['rss_basefill_070'], 'func': rss_base_universe_d2_067_rss_basefill_070}


def rss_base_universe_d2_068_rss_basefill_071(rss_basefill_071):
    return _base_universe_d2(rss_basefill_071, 68)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_068_rss_basefill_071'] = {'inputs': ['rss_basefill_071'], 'func': rss_base_universe_d2_068_rss_basefill_071}


def rss_base_universe_d2_069_rss_basefill_072(rss_basefill_072):
    return _base_universe_d2(rss_basefill_072, 69)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_069_rss_basefill_072'] = {'inputs': ['rss_basefill_072'], 'func': rss_base_universe_d2_069_rss_basefill_072}


def rss_base_universe_d2_070_rss_basefill_073(rss_basefill_073):
    return _base_universe_d2(rss_basefill_073, 70)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_070_rss_basefill_073'] = {'inputs': ['rss_basefill_073'], 'func': rss_base_universe_d2_070_rss_basefill_073}


def rss_base_universe_d2_071_rss_basefill_074(rss_basefill_074):
    return _base_universe_d2(rss_basefill_074, 71)
RSS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rss_base_universe_d2_071_rss_basefill_074'] = {'inputs': ['rss_basefill_074'], 'func': rss_base_universe_d2_071_rss_basefill_074}
