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



def lsr_151_lsr_001_dividend_cut_density_21_roc_1(lsr_001_dividend_cut_density_21):
    feature = _s(lsr_001_dividend_cut_density_21)
    return (_roc(feature, 1)).reindex(feature.index)

def lsr_152_lsr_007_listing_tier_decay_1_roc_42(lsr_007_listing_tier_decay_1):
    feature = _s(lsr_007_listing_tier_decay_1)
    return (_roc(feature, 42)).reindex(feature.index)

def lsr_153_lsr_013_delisting_notice_density_1512_roc_126(lsr_013_delisting_notice_density_1512):
    feature = _s(lsr_013_delisting_notice_density_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def lsr_154_lsr_019_going_concern_persistence_84_roc_378(lsr_019_going_concern_persistence_84):
    feature = _s(lsr_019_going_concern_persistence_84)
    return (_roc(feature, 378)).reindex(feature.index)

def lsr_155_lsr_025_event_density_z_756_roc_4(lsr_025_event_density_z_756):
    feature = _s(lsr_025_event_density_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















LISTING_STATUS_RISK_REGISTRY_2ND_DERIVATIVES = {
    'lsr_151_lsr_001_dividend_cut_density_21_roc_1': {'inputs': ['lsr_001_dividend_cut_density_21'], 'func': lsr_151_lsr_001_dividend_cut_density_21_roc_1},
    'lsr_152_lsr_007_listing_tier_decay_1_roc_42': {'inputs': ['lsr_007_listing_tier_decay_1'], 'func': lsr_152_lsr_007_listing_tier_decay_1_roc_42},
    'lsr_153_lsr_013_delisting_notice_density_1512_roc_126': {'inputs': ['lsr_013_delisting_notice_density_1512'], 'func': lsr_153_lsr_013_delisting_notice_density_1512_roc_126},
    'lsr_154_lsr_019_going_concern_persistence_84_roc_378': {'inputs': ['lsr_019_going_concern_persistence_84'], 'func': lsr_154_lsr_019_going_concern_persistence_84_roc_378},
    'lsr_155_lsr_025_event_density_z_756_roc_4': {'inputs': ['lsr_025_event_density_z_756'], 'func': lsr_155_lsr_025_event_density_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def lsr_replacement_d2_001(lsr_007_listing_tier_decay_1):
    feature = _clean(lsr_007_listing_tier_decay_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_001'] = {'inputs': ['lsr_007_listing_tier_decay_1'], 'func': lsr_replacement_d2_001}


def lsr_replacement_d2_002(lsr_replacement_001):
    feature = _clean(lsr_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_002'] = {'inputs': ['lsr_replacement_001'], 'func': lsr_replacement_d2_002}


def lsr_replacement_d2_003(lsr_replacement_002):
    feature = _clean(lsr_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_003'] = {'inputs': ['lsr_replacement_002'], 'func': lsr_replacement_d2_003}


def lsr_replacement_d2_004(lsr_replacement_003):
    feature = _clean(lsr_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_004'] = {'inputs': ['lsr_replacement_003'], 'func': lsr_replacement_d2_004}


def lsr_replacement_d2_005(lsr_replacement_004):
    feature = _clean(lsr_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_005'] = {'inputs': ['lsr_replacement_004'], 'func': lsr_replacement_d2_005}


def lsr_replacement_d2_006(lsr_replacement_005):
    feature = _clean(lsr_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_006'] = {'inputs': ['lsr_replacement_005'], 'func': lsr_replacement_d2_006}


def lsr_replacement_d2_007(lsr_replacement_006):
    feature = _clean(lsr_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_007'] = {'inputs': ['lsr_replacement_006'], 'func': lsr_replacement_d2_007}


def lsr_replacement_d2_008(lsr_replacement_007):
    feature = _clean(lsr_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_008'] = {'inputs': ['lsr_replacement_007'], 'func': lsr_replacement_d2_008}


def lsr_replacement_d2_009(lsr_replacement_008):
    feature = _clean(lsr_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_009'] = {'inputs': ['lsr_replacement_008'], 'func': lsr_replacement_d2_009}


def lsr_replacement_d2_010(lsr_replacement_009):
    feature = _clean(lsr_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_010'] = {'inputs': ['lsr_replacement_009'], 'func': lsr_replacement_d2_010}


def lsr_replacement_d2_011(lsr_replacement_010):
    feature = _clean(lsr_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_011'] = {'inputs': ['lsr_replacement_010'], 'func': lsr_replacement_d2_011}


def lsr_replacement_d2_012(lsr_replacement_011):
    feature = _clean(lsr_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_012'] = {'inputs': ['lsr_replacement_011'], 'func': lsr_replacement_d2_012}


def lsr_replacement_d2_013(lsr_replacement_012):
    feature = _clean(lsr_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_013'] = {'inputs': ['lsr_replacement_012'], 'func': lsr_replacement_d2_013}


def lsr_replacement_d2_014(lsr_replacement_013):
    feature = _clean(lsr_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_014'] = {'inputs': ['lsr_replacement_013'], 'func': lsr_replacement_d2_014}


def lsr_replacement_d2_015(lsr_replacement_014):
    feature = _clean(lsr_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_015'] = {'inputs': ['lsr_replacement_014'], 'func': lsr_replacement_d2_015}


def lsr_replacement_d2_016(lsr_replacement_015):
    feature = _clean(lsr_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_016'] = {'inputs': ['lsr_replacement_015'], 'func': lsr_replacement_d2_016}


def lsr_replacement_d2_017(lsr_replacement_016):
    feature = _clean(lsr_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_017'] = {'inputs': ['lsr_replacement_016'], 'func': lsr_replacement_d2_017}


def lsr_replacement_d2_018(lsr_replacement_017):
    feature = _clean(lsr_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_018'] = {'inputs': ['lsr_replacement_017'], 'func': lsr_replacement_d2_018}


def lsr_replacement_d2_019(lsr_replacement_018):
    feature = _clean(lsr_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_019'] = {'inputs': ['lsr_replacement_018'], 'func': lsr_replacement_d2_019}


def lsr_replacement_d2_020(lsr_replacement_019):
    feature = _clean(lsr_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_020'] = {'inputs': ['lsr_replacement_019'], 'func': lsr_replacement_d2_020}


def lsr_replacement_d2_021(lsr_replacement_020):
    feature = _clean(lsr_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_021'] = {'inputs': ['lsr_replacement_020'], 'func': lsr_replacement_d2_021}


def lsr_replacement_d2_022(lsr_replacement_021):
    feature = _clean(lsr_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_022'] = {'inputs': ['lsr_replacement_021'], 'func': lsr_replacement_d2_022}


def lsr_replacement_d2_023(lsr_replacement_022):
    feature = _clean(lsr_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_023'] = {'inputs': ['lsr_replacement_022'], 'func': lsr_replacement_d2_023}


def lsr_replacement_d2_024(lsr_replacement_023):
    feature = _clean(lsr_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_024'] = {'inputs': ['lsr_replacement_023'], 'func': lsr_replacement_d2_024}


def lsr_replacement_d2_025(lsr_replacement_024):
    feature = _clean(lsr_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_025'] = {'inputs': ['lsr_replacement_024'], 'func': lsr_replacement_d2_025}


def lsr_replacement_d2_026(lsr_replacement_025):
    feature = _clean(lsr_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_026'] = {'inputs': ['lsr_replacement_025'], 'func': lsr_replacement_d2_026}


def lsr_replacement_d2_027(lsr_replacement_026):
    feature = _clean(lsr_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_027'] = {'inputs': ['lsr_replacement_026'], 'func': lsr_replacement_d2_027}


def lsr_replacement_d2_028(lsr_replacement_027):
    feature = _clean(lsr_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_028'] = {'inputs': ['lsr_replacement_027'], 'func': lsr_replacement_d2_028}


def lsr_replacement_d2_029(lsr_replacement_028):
    feature = _clean(lsr_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_029'] = {'inputs': ['lsr_replacement_028'], 'func': lsr_replacement_d2_029}


def lsr_replacement_d2_030(lsr_replacement_029):
    feature = _clean(lsr_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_030'] = {'inputs': ['lsr_replacement_029'], 'func': lsr_replacement_d2_030}


def lsr_replacement_d2_031(lsr_replacement_030):
    feature = _clean(lsr_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_031'] = {'inputs': ['lsr_replacement_030'], 'func': lsr_replacement_d2_031}


def lsr_replacement_d2_032(lsr_replacement_031):
    feature = _clean(lsr_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_032'] = {'inputs': ['lsr_replacement_031'], 'func': lsr_replacement_d2_032}


def lsr_replacement_d2_033(lsr_replacement_032):
    feature = _clean(lsr_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_033'] = {'inputs': ['lsr_replacement_032'], 'func': lsr_replacement_d2_033}


def lsr_replacement_d2_034(lsr_replacement_033):
    feature = _clean(lsr_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_034'] = {'inputs': ['lsr_replacement_033'], 'func': lsr_replacement_d2_034}


def lsr_replacement_d2_035(lsr_replacement_034):
    feature = _clean(lsr_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_035'] = {'inputs': ['lsr_replacement_034'], 'func': lsr_replacement_d2_035}


def lsr_replacement_d2_036(lsr_replacement_035):
    feature = _clean(lsr_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_036'] = {'inputs': ['lsr_replacement_035'], 'func': lsr_replacement_d2_036}


def lsr_replacement_d2_037(lsr_replacement_036):
    feature = _clean(lsr_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_037'] = {'inputs': ['lsr_replacement_036'], 'func': lsr_replacement_d2_037}


def lsr_replacement_d2_038(lsr_replacement_037):
    feature = _clean(lsr_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_038'] = {'inputs': ['lsr_replacement_037'], 'func': lsr_replacement_d2_038}


def lsr_replacement_d2_039(lsr_replacement_038):
    feature = _clean(lsr_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_039'] = {'inputs': ['lsr_replacement_038'], 'func': lsr_replacement_d2_039}


def lsr_replacement_d2_040(lsr_replacement_039):
    feature = _clean(lsr_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_040'] = {'inputs': ['lsr_replacement_039'], 'func': lsr_replacement_d2_040}


def lsr_replacement_d2_041(lsr_replacement_040):
    feature = _clean(lsr_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_041'] = {'inputs': ['lsr_replacement_040'], 'func': lsr_replacement_d2_041}


def lsr_replacement_d2_042(lsr_replacement_041):
    feature = _clean(lsr_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_042'] = {'inputs': ['lsr_replacement_041'], 'func': lsr_replacement_d2_042}


def lsr_replacement_d2_043(lsr_replacement_042):
    feature = _clean(lsr_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_043'] = {'inputs': ['lsr_replacement_042'], 'func': lsr_replacement_d2_043}


def lsr_replacement_d2_044(lsr_replacement_043):
    feature = _clean(lsr_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_044'] = {'inputs': ['lsr_replacement_043'], 'func': lsr_replacement_d2_044}


def lsr_replacement_d2_045(lsr_replacement_044):
    feature = _clean(lsr_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_045'] = {'inputs': ['lsr_replacement_044'], 'func': lsr_replacement_d2_045}


def lsr_replacement_d2_046(lsr_replacement_045):
    feature = _clean(lsr_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_046'] = {'inputs': ['lsr_replacement_045'], 'func': lsr_replacement_d2_046}


def lsr_replacement_d2_047(lsr_replacement_046):
    feature = _clean(lsr_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_047'] = {'inputs': ['lsr_replacement_046'], 'func': lsr_replacement_d2_047}


def lsr_replacement_d2_048(lsr_replacement_047):
    feature = _clean(lsr_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_048'] = {'inputs': ['lsr_replacement_047'], 'func': lsr_replacement_d2_048}


def lsr_replacement_d2_049(lsr_replacement_048):
    feature = _clean(lsr_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_049'] = {'inputs': ['lsr_replacement_048'], 'func': lsr_replacement_d2_049}


def lsr_replacement_d2_050(lsr_replacement_049):
    feature = _clean(lsr_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_050'] = {'inputs': ['lsr_replacement_049'], 'func': lsr_replacement_d2_050}


def lsr_replacement_d2_051(lsr_replacement_050):
    feature = _clean(lsr_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_051'] = {'inputs': ['lsr_replacement_050'], 'func': lsr_replacement_d2_051}


def lsr_replacement_d2_052(lsr_replacement_051):
    feature = _clean(lsr_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_052'] = {'inputs': ['lsr_replacement_051'], 'func': lsr_replacement_d2_052}


def lsr_replacement_d2_053(lsr_replacement_052):
    feature = _clean(lsr_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_053'] = {'inputs': ['lsr_replacement_052'], 'func': lsr_replacement_d2_053}


def lsr_replacement_d2_054(lsr_replacement_053):
    feature = _clean(lsr_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_054'] = {'inputs': ['lsr_replacement_053'], 'func': lsr_replacement_d2_054}


def lsr_replacement_d2_055(lsr_replacement_054):
    feature = _clean(lsr_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_055'] = {'inputs': ['lsr_replacement_054'], 'func': lsr_replacement_d2_055}


def lsr_replacement_d2_056(lsr_replacement_055):
    feature = _clean(lsr_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_056'] = {'inputs': ['lsr_replacement_055'], 'func': lsr_replacement_d2_056}


def lsr_replacement_d2_057(lsr_replacement_056):
    feature = _clean(lsr_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_057'] = {'inputs': ['lsr_replacement_056'], 'func': lsr_replacement_d2_057}


def lsr_replacement_d2_058(lsr_replacement_057):
    feature = _clean(lsr_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_058'] = {'inputs': ['lsr_replacement_057'], 'func': lsr_replacement_d2_058}


def lsr_replacement_d2_059(lsr_replacement_058):
    feature = _clean(lsr_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_059'] = {'inputs': ['lsr_replacement_058'], 'func': lsr_replacement_d2_059}


def lsr_replacement_d2_060(lsr_replacement_059):
    feature = _clean(lsr_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_060'] = {'inputs': ['lsr_replacement_059'], 'func': lsr_replacement_d2_060}


def lsr_replacement_d2_061(lsr_replacement_060):
    feature = _clean(lsr_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_061'] = {'inputs': ['lsr_replacement_060'], 'func': lsr_replacement_d2_061}


def lsr_replacement_d2_062(lsr_replacement_061):
    feature = _clean(lsr_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_062'] = {'inputs': ['lsr_replacement_061'], 'func': lsr_replacement_d2_062}


def lsr_replacement_d2_063(lsr_replacement_062):
    feature = _clean(lsr_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_063'] = {'inputs': ['lsr_replacement_062'], 'func': lsr_replacement_d2_063}


def lsr_replacement_d2_064(lsr_replacement_063):
    feature = _clean(lsr_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_064'] = {'inputs': ['lsr_replacement_063'], 'func': lsr_replacement_d2_064}


def lsr_replacement_d2_065(lsr_replacement_064):
    feature = _clean(lsr_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_065'] = {'inputs': ['lsr_replacement_064'], 'func': lsr_replacement_d2_065}


def lsr_replacement_d2_066(lsr_replacement_065):
    feature = _clean(lsr_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_066'] = {'inputs': ['lsr_replacement_065'], 'func': lsr_replacement_d2_066}


def lsr_replacement_d2_067(lsr_replacement_066):
    feature = _clean(lsr_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_067'] = {'inputs': ['lsr_replacement_066'], 'func': lsr_replacement_d2_067}


def lsr_replacement_d2_068(lsr_replacement_067):
    feature = _clean(lsr_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_068'] = {'inputs': ['lsr_replacement_067'], 'func': lsr_replacement_d2_068}


def lsr_replacement_d2_069(lsr_replacement_068):
    feature = _clean(lsr_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_069'] = {'inputs': ['lsr_replacement_068'], 'func': lsr_replacement_d2_069}


def lsr_replacement_d2_070(lsr_replacement_069):
    feature = _clean(lsr_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_070'] = {'inputs': ['lsr_replacement_069'], 'func': lsr_replacement_d2_070}


def lsr_replacement_d2_071(lsr_replacement_070):
    feature = _clean(lsr_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_071'] = {'inputs': ['lsr_replacement_070'], 'func': lsr_replacement_d2_071}


def lsr_replacement_d2_072(lsr_replacement_071):
    feature = _clean(lsr_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_072'] = {'inputs': ['lsr_replacement_071'], 'func': lsr_replacement_d2_072}


def lsr_replacement_d2_073(lsr_replacement_072):
    feature = _clean(lsr_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_073'] = {'inputs': ['lsr_replacement_072'], 'func': lsr_replacement_d2_073}


def lsr_replacement_d2_074(lsr_replacement_073):
    feature = _clean(lsr_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_074'] = {'inputs': ['lsr_replacement_073'], 'func': lsr_replacement_d2_074}


def lsr_replacement_d2_075(lsr_replacement_074):
    feature = _clean(lsr_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_075'] = {'inputs': ['lsr_replacement_074'], 'func': lsr_replacement_d2_075}


def lsr_replacement_d2_076(lsr_replacement_075):
    feature = _clean(lsr_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_076'] = {'inputs': ['lsr_replacement_075'], 'func': lsr_replacement_d2_076}


def lsr_replacement_d2_077(lsr_replacement_076):
    feature = _clean(lsr_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_077'] = {'inputs': ['lsr_replacement_076'], 'func': lsr_replacement_d2_077}


def lsr_replacement_d2_078(lsr_replacement_077):
    feature = _clean(lsr_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_078'] = {'inputs': ['lsr_replacement_077'], 'func': lsr_replacement_d2_078}


def lsr_replacement_d2_079(lsr_replacement_078):
    feature = _clean(lsr_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_079'] = {'inputs': ['lsr_replacement_078'], 'func': lsr_replacement_d2_079}


def lsr_replacement_d2_080(lsr_replacement_079):
    feature = _clean(lsr_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_080'] = {'inputs': ['lsr_replacement_079'], 'func': lsr_replacement_d2_080}


def lsr_replacement_d2_081(lsr_replacement_080):
    feature = _clean(lsr_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_081'] = {'inputs': ['lsr_replacement_080'], 'func': lsr_replacement_d2_081}


def lsr_replacement_d2_082(lsr_replacement_081):
    feature = _clean(lsr_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_082'] = {'inputs': ['lsr_replacement_081'], 'func': lsr_replacement_d2_082}


def lsr_replacement_d2_083(lsr_replacement_082):
    feature = _clean(lsr_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_083'] = {'inputs': ['lsr_replacement_082'], 'func': lsr_replacement_d2_083}


def lsr_replacement_d2_084(lsr_replacement_083):
    feature = _clean(lsr_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_084'] = {'inputs': ['lsr_replacement_083'], 'func': lsr_replacement_d2_084}


def lsr_replacement_d2_085(lsr_replacement_084):
    feature = _clean(lsr_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_085'] = {'inputs': ['lsr_replacement_084'], 'func': lsr_replacement_d2_085}


def lsr_replacement_d2_086(lsr_replacement_085):
    feature = _clean(lsr_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_086'] = {'inputs': ['lsr_replacement_085'], 'func': lsr_replacement_d2_086}


def lsr_replacement_d2_087(lsr_replacement_086):
    feature = _clean(lsr_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_087'] = {'inputs': ['lsr_replacement_086'], 'func': lsr_replacement_d2_087}


def lsr_replacement_d2_088(lsr_replacement_087):
    feature = _clean(lsr_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_088'] = {'inputs': ['lsr_replacement_087'], 'func': lsr_replacement_d2_088}


def lsr_replacement_d2_089(lsr_replacement_088):
    feature = _clean(lsr_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_089'] = {'inputs': ['lsr_replacement_088'], 'func': lsr_replacement_d2_089}


def lsr_replacement_d2_090(lsr_replacement_089):
    feature = _clean(lsr_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_090'] = {'inputs': ['lsr_replacement_089'], 'func': lsr_replacement_d2_090}


def lsr_replacement_d2_091(lsr_replacement_090):
    feature = _clean(lsr_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_091'] = {'inputs': ['lsr_replacement_090'], 'func': lsr_replacement_d2_091}


def lsr_replacement_d2_092(lsr_replacement_091):
    feature = _clean(lsr_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_092'] = {'inputs': ['lsr_replacement_091'], 'func': lsr_replacement_d2_092}


def lsr_replacement_d2_093(lsr_replacement_092):
    feature = _clean(lsr_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_093'] = {'inputs': ['lsr_replacement_092'], 'func': lsr_replacement_d2_093}


def lsr_replacement_d2_094(lsr_replacement_093):
    feature = _clean(lsr_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_094'] = {'inputs': ['lsr_replacement_093'], 'func': lsr_replacement_d2_094}


def lsr_replacement_d2_095(lsr_replacement_094):
    feature = _clean(lsr_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_095'] = {'inputs': ['lsr_replacement_094'], 'func': lsr_replacement_d2_095}


def lsr_replacement_d2_096(lsr_replacement_095):
    feature = _clean(lsr_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_096'] = {'inputs': ['lsr_replacement_095'], 'func': lsr_replacement_d2_096}


def lsr_replacement_d2_097(lsr_replacement_096):
    feature = _clean(lsr_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_097'] = {'inputs': ['lsr_replacement_096'], 'func': lsr_replacement_d2_097}


def lsr_replacement_d2_098(lsr_replacement_097):
    feature = _clean(lsr_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_098'] = {'inputs': ['lsr_replacement_097'], 'func': lsr_replacement_d2_098}


def lsr_replacement_d2_099(lsr_replacement_098):
    feature = _clean(lsr_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_099'] = {'inputs': ['lsr_replacement_098'], 'func': lsr_replacement_d2_099}


def lsr_replacement_d2_100(lsr_replacement_099):
    feature = _clean(lsr_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_100'] = {'inputs': ['lsr_replacement_099'], 'func': lsr_replacement_d2_100}


def lsr_replacement_d2_101(lsr_replacement_100):
    feature = _clean(lsr_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_101'] = {'inputs': ['lsr_replacement_100'], 'func': lsr_replacement_d2_101}


def lsr_replacement_d2_102(lsr_replacement_101):
    feature = _clean(lsr_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_102'] = {'inputs': ['lsr_replacement_101'], 'func': lsr_replacement_d2_102}


def lsr_replacement_d2_103(lsr_replacement_102):
    feature = _clean(lsr_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_103'] = {'inputs': ['lsr_replacement_102'], 'func': lsr_replacement_d2_103}


def lsr_replacement_d2_104(lsr_replacement_103):
    feature = _clean(lsr_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_104'] = {'inputs': ['lsr_replacement_103'], 'func': lsr_replacement_d2_104}


def lsr_replacement_d2_105(lsr_replacement_104):
    feature = _clean(lsr_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_105'] = {'inputs': ['lsr_replacement_104'], 'func': lsr_replacement_d2_105}


def lsr_replacement_d2_106(lsr_replacement_105):
    feature = _clean(lsr_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_106'] = {'inputs': ['lsr_replacement_105'], 'func': lsr_replacement_d2_106}


def lsr_replacement_d2_107(lsr_replacement_106):
    feature = _clean(lsr_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_107'] = {'inputs': ['lsr_replacement_106'], 'func': lsr_replacement_d2_107}


def lsr_replacement_d2_108(lsr_replacement_107):
    feature = _clean(lsr_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_108'] = {'inputs': ['lsr_replacement_107'], 'func': lsr_replacement_d2_108}


def lsr_replacement_d2_109(lsr_replacement_108):
    feature = _clean(lsr_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_109'] = {'inputs': ['lsr_replacement_108'], 'func': lsr_replacement_d2_109}


def lsr_replacement_d2_110(lsr_replacement_109):
    feature = _clean(lsr_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_110'] = {'inputs': ['lsr_replacement_109'], 'func': lsr_replacement_d2_110}


def lsr_replacement_d2_111(lsr_replacement_110):
    feature = _clean(lsr_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_111'] = {'inputs': ['lsr_replacement_110'], 'func': lsr_replacement_d2_111}


def lsr_replacement_d2_112(lsr_replacement_111):
    feature = _clean(lsr_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_112'] = {'inputs': ['lsr_replacement_111'], 'func': lsr_replacement_d2_112}


def lsr_replacement_d2_113(lsr_replacement_112):
    feature = _clean(lsr_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_113'] = {'inputs': ['lsr_replacement_112'], 'func': lsr_replacement_d2_113}


def lsr_replacement_d2_114(lsr_replacement_113):
    feature = _clean(lsr_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_114'] = {'inputs': ['lsr_replacement_113'], 'func': lsr_replacement_d2_114}


def lsr_replacement_d2_115(lsr_replacement_114):
    feature = _clean(lsr_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_115'] = {'inputs': ['lsr_replacement_114'], 'func': lsr_replacement_d2_115}


def lsr_replacement_d2_116(lsr_replacement_115):
    feature = _clean(lsr_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_116'] = {'inputs': ['lsr_replacement_115'], 'func': lsr_replacement_d2_116}


def lsr_replacement_d2_117(lsr_replacement_116):
    feature = _clean(lsr_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_117'] = {'inputs': ['lsr_replacement_116'], 'func': lsr_replacement_d2_117}


def lsr_replacement_d2_118(lsr_replacement_117):
    feature = _clean(lsr_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_118'] = {'inputs': ['lsr_replacement_117'], 'func': lsr_replacement_d2_118}


def lsr_replacement_d2_119(lsr_replacement_118):
    feature = _clean(lsr_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_119'] = {'inputs': ['lsr_replacement_118'], 'func': lsr_replacement_d2_119}


def lsr_replacement_d2_120(lsr_replacement_119):
    feature = _clean(lsr_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_120'] = {'inputs': ['lsr_replacement_119'], 'func': lsr_replacement_d2_120}


def lsr_replacement_d2_121(lsr_replacement_120):
    feature = _clean(lsr_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_121'] = {'inputs': ['lsr_replacement_120'], 'func': lsr_replacement_d2_121}


def lsr_replacement_d2_122(lsr_replacement_121):
    feature = _clean(lsr_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_122'] = {'inputs': ['lsr_replacement_121'], 'func': lsr_replacement_d2_122}


def lsr_replacement_d2_123(lsr_replacement_122):
    feature = _clean(lsr_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_123'] = {'inputs': ['lsr_replacement_122'], 'func': lsr_replacement_d2_123}


def lsr_replacement_d2_124(lsr_replacement_123):
    feature = _clean(lsr_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_124'] = {'inputs': ['lsr_replacement_123'], 'func': lsr_replacement_d2_124}


def lsr_replacement_d2_125(lsr_replacement_124):
    feature = _clean(lsr_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_125'] = {'inputs': ['lsr_replacement_124'], 'func': lsr_replacement_d2_125}


def lsr_replacement_d2_126(lsr_replacement_125):
    feature = _clean(lsr_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_126'] = {'inputs': ['lsr_replacement_125'], 'func': lsr_replacement_d2_126}


def lsr_replacement_d2_127(lsr_replacement_126):
    feature = _clean(lsr_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_127'] = {'inputs': ['lsr_replacement_126'], 'func': lsr_replacement_d2_127}


def lsr_replacement_d2_128(lsr_replacement_127):
    feature = _clean(lsr_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_128'] = {'inputs': ['lsr_replacement_127'], 'func': lsr_replacement_d2_128}


def lsr_replacement_d2_129(lsr_replacement_128):
    feature = _clean(lsr_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_129'] = {'inputs': ['lsr_replacement_128'], 'func': lsr_replacement_d2_129}


def lsr_replacement_d2_130(lsr_replacement_129):
    feature = _clean(lsr_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_130'] = {'inputs': ['lsr_replacement_129'], 'func': lsr_replacement_d2_130}


def lsr_replacement_d2_131(lsr_replacement_130):
    feature = _clean(lsr_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_131'] = {'inputs': ['lsr_replacement_130'], 'func': lsr_replacement_d2_131}


def lsr_replacement_d2_132(lsr_replacement_131):
    feature = _clean(lsr_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_132'] = {'inputs': ['lsr_replacement_131'], 'func': lsr_replacement_d2_132}


def lsr_replacement_d2_133(lsr_replacement_132):
    feature = _clean(lsr_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_133'] = {'inputs': ['lsr_replacement_132'], 'func': lsr_replacement_d2_133}


def lsr_replacement_d2_134(lsr_replacement_133):
    feature = _clean(lsr_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_134'] = {'inputs': ['lsr_replacement_133'], 'func': lsr_replacement_d2_134}


def lsr_replacement_d2_135(lsr_replacement_134):
    feature = _clean(lsr_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_135'] = {'inputs': ['lsr_replacement_134'], 'func': lsr_replacement_d2_135}


def lsr_replacement_d2_136(lsr_replacement_135):
    feature = _clean(lsr_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_136'] = {'inputs': ['lsr_replacement_135'], 'func': lsr_replacement_d2_136}


def lsr_replacement_d2_137(lsr_replacement_136):
    feature = _clean(lsr_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_137'] = {'inputs': ['lsr_replacement_136'], 'func': lsr_replacement_d2_137}


def lsr_replacement_d2_138(lsr_replacement_137):
    feature = _clean(lsr_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_138'] = {'inputs': ['lsr_replacement_137'], 'func': lsr_replacement_d2_138}


def lsr_replacement_d2_139(lsr_replacement_138):
    feature = _clean(lsr_replacement_138)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_139'] = {'inputs': ['lsr_replacement_138'], 'func': lsr_replacement_d2_139}


def lsr_replacement_d2_140(lsr_replacement_139):
    feature = _clean(lsr_replacement_139)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_140'] = {'inputs': ['lsr_replacement_139'], 'func': lsr_replacement_d2_140}


def lsr_replacement_d2_141(lsr_replacement_140):
    feature = _clean(lsr_replacement_140)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_141'] = {'inputs': ['lsr_replacement_140'], 'func': lsr_replacement_d2_141}


def lsr_replacement_d2_142(lsr_replacement_141):
    feature = _clean(lsr_replacement_141)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_142'] = {'inputs': ['lsr_replacement_141'], 'func': lsr_replacement_d2_142}


def lsr_replacement_d2_143(lsr_replacement_142):
    feature = _clean(lsr_replacement_142)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_143'] = {'inputs': ['lsr_replacement_142'], 'func': lsr_replacement_d2_143}


def lsr_replacement_d2_144(lsr_replacement_143):
    feature = _clean(lsr_replacement_143)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_144'] = {'inputs': ['lsr_replacement_143'], 'func': lsr_replacement_d2_144}


def lsr_replacement_d2_145(lsr_replacement_144):
    feature = _clean(lsr_replacement_144)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_145'] = {'inputs': ['lsr_replacement_144'], 'func': lsr_replacement_d2_145}


def lsr_replacement_d2_146(lsr_replacement_145):
    feature = _clean(lsr_replacement_145)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_146'] = {'inputs': ['lsr_replacement_145'], 'func': lsr_replacement_d2_146}


def lsr_replacement_d2_147(lsr_replacement_146):
    feature = _clean(lsr_replacement_146)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_147'] = {'inputs': ['lsr_replacement_146'], 'func': lsr_replacement_d2_147}


def lsr_replacement_d2_148(lsr_replacement_147):
    feature = _clean(lsr_replacement_147)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_148'] = {'inputs': ['lsr_replacement_147'], 'func': lsr_replacement_d2_148}


def lsr_replacement_d2_149(lsr_replacement_148):
    feature = _clean(lsr_replacement_148)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_149'] = {'inputs': ['lsr_replacement_148'], 'func': lsr_replacement_d2_149}


def lsr_replacement_d2_150(lsr_replacement_149):
    feature = _clean(lsr_replacement_149)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_150'] = {'inputs': ['lsr_replacement_149'], 'func': lsr_replacement_d2_150}


def lsr_replacement_d2_151(lsr_replacement_150):
    feature = _clean(lsr_replacement_150)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
LSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lsr_replacement_d2_151'] = {'inputs': ['lsr_replacement_150'], 'func': lsr_replacement_d2_151}


# Base-universe derivative extensions for repaired first-base features.
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42(lsr_002_dividend_suspension_density_42):
    return _base_universe_d2(lsr_002_dividend_suspension_density_42, 1)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42'] = {'inputs': ['lsr_002_dividend_suspension_density_42'], 'func': lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42}


def lsr_base_universe_d2_002_lsr_003_reverse_split_density_63(lsr_003_reverse_split_density_63):
    return _base_universe_d2(lsr_003_reverse_split_density_63, 2)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_002_lsr_003_reverse_split_density_63'] = {'inputs': ['lsr_003_reverse_split_density_63'], 'func': lsr_base_universe_d2_002_lsr_003_reverse_split_density_63}


def lsr_base_universe_d2_003_lsr_004_event_density_z_84(lsr_004_event_density_z_84):
    return _base_universe_d2(lsr_004_event_density_z_84, 3)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_003_lsr_004_event_density_z_84'] = {'inputs': ['lsr_004_event_density_z_84'], 'func': lsr_base_universe_d2_003_lsr_004_event_density_z_84}


def lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126(lsr_005_going_concern_persistence_126):
    return _base_universe_d2(lsr_005_going_concern_persistence_126, 4)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126'] = {'inputs': ['lsr_005_going_concern_persistence_126'], 'func': lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126}


def lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189(lsr_006_delisting_notice_density_189):
    return _base_universe_d2(lsr_006_delisting_notice_density_189, 5)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189'] = {'inputs': ['lsr_006_delisting_notice_density_189'], 'func': lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189}


def lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378(lsr_008_dividend_cut_density_378):
    return _base_universe_d2(lsr_008_dividend_cut_density_378, 6)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378'] = {'inputs': ['lsr_008_dividend_cut_density_378'], 'func': lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378}


def lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504(lsr_009_dividend_suspension_density_504):
    return _base_universe_d2(lsr_009_dividend_suspension_density_504, 7)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504'] = {'inputs': ['lsr_009_dividend_suspension_density_504'], 'func': lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504}


def lsr_base_universe_d2_008_lsr_010_reverse_split_density_756(lsr_010_reverse_split_density_756):
    return _base_universe_d2(lsr_010_reverse_split_density_756, 8)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_008_lsr_010_reverse_split_density_756'] = {'inputs': ['lsr_010_reverse_split_density_756'], 'func': lsr_base_universe_d2_008_lsr_010_reverse_split_density_756}


def lsr_base_universe_d2_009_lsr_011_event_density_z_1008(lsr_011_event_density_z_1008):
    return _base_universe_d2(lsr_011_event_density_z_1008, 9)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_009_lsr_011_event_density_z_1008'] = {'inputs': ['lsr_011_event_density_z_1008'], 'func': lsr_base_universe_d2_009_lsr_011_event_density_z_1008}


def lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260(lsr_012_going_concern_persistence_1260):
    return _base_universe_d2(lsr_012_going_concern_persistence_1260, 10)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260'] = {'inputs': ['lsr_012_going_concern_persistence_1260'], 'func': lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260}


def lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252(lsr_015_dividend_cut_density_252):
    return _base_universe_d2(lsr_015_dividend_cut_density_252, 11)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252'] = {'inputs': ['lsr_015_dividend_cut_density_252'], 'func': lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252}


def lsr_base_universe_d2_012_lsr_018_event_density_z_63(lsr_018_event_density_z_63):
    return _base_universe_d2(lsr_018_event_density_z_63, 12)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_012_lsr_018_event_density_z_63'] = {'inputs': ['lsr_018_event_density_z_63'], 'func': lsr_base_universe_d2_012_lsr_018_event_density_z_63}


def lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126(lsr_020_delisting_notice_density_126):
    return _base_universe_d2(lsr_020_delisting_notice_density_126, 13)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126'] = {'inputs': ['lsr_020_delisting_notice_density_126'], 'func': lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126}


def lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008(lsr_026_going_concern_persistence_1008):
    return _base_universe_d2(lsr_026_going_concern_persistence_1008, 14)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008'] = {'inputs': ['lsr_026_going_concern_persistence_1008'], 'func': lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008}


def lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260(lsr_027_delisting_notice_density_1260):
    return _base_universe_d2(lsr_027_delisting_notice_density_1260, 15)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260'] = {'inputs': ['lsr_027_delisting_notice_density_1260'], 'func': lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260}


def lsr_base_universe_d2_016_lsr_032_event_density_z_42(lsr_032_event_density_z_42):
    return _base_universe_d2(lsr_032_event_density_z_42, 16)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_016_lsr_032_event_density_z_42'] = {'inputs': ['lsr_032_event_density_z_42'], 'func': lsr_base_universe_d2_016_lsr_032_event_density_z_42}


def lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63(lsr_033_going_concern_persistence_63):
    return _base_universe_d2(lsr_033_going_concern_persistence_63, 17)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63'] = {'inputs': ['lsr_033_going_concern_persistence_63'], 'func': lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63}


def lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84(lsr_034_delisting_notice_density_84):
    return _base_universe_d2(lsr_034_delisting_notice_density_84, 18)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84'] = {'inputs': ['lsr_034_delisting_notice_density_84'], 'func': lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84}


def lsr_base_universe_d2_019_lsr_039_event_density_z_504(lsr_039_event_density_z_504):
    return _base_universe_d2(lsr_039_event_density_z_504, 19)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_019_lsr_039_event_density_z_504'] = {'inputs': ['lsr_039_event_density_z_504'], 'func': lsr_base_universe_d2_019_lsr_039_event_density_z_504}


def lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756(lsr_040_going_concern_persistence_756):
    return _base_universe_d2(lsr_040_going_concern_persistence_756, 20)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756'] = {'inputs': ['lsr_040_going_concern_persistence_756'], 'func': lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756}


def lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008(lsr_041_delisting_notice_density_1008):
    return _base_universe_d2(lsr_041_delisting_notice_density_1008, 21)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008'] = {'inputs': ['lsr_041_delisting_notice_density_1008'], 'func': lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008}


def lsr_base_universe_d2_022_lsr_046_event_density_z_21(lsr_046_event_density_z_21):
    return _base_universe_d2(lsr_046_event_density_z_21, 22)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_022_lsr_046_event_density_z_21'] = {'inputs': ['lsr_046_event_density_z_21'], 'func': lsr_base_universe_d2_022_lsr_046_event_density_z_21}


def lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42(lsr_047_going_concern_persistence_42):
    return _base_universe_d2(lsr_047_going_concern_persistence_42, 23)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42'] = {'inputs': ['lsr_047_going_concern_persistence_42'], 'func': lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42}


def lsr_base_universe_d2_024_lsr_053_event_density_z_378(lsr_053_event_density_z_378):
    return _base_universe_d2(lsr_053_event_density_z_378, 24)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_024_lsr_053_event_density_z_378'] = {'inputs': ['lsr_053_event_density_z_378'], 'func': lsr_base_universe_d2_024_lsr_053_event_density_z_378}


def lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504(lsr_054_going_concern_persistence_504):
    return _base_universe_d2(lsr_054_going_concern_persistence_504, 25)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504'] = {'inputs': ['lsr_054_going_concern_persistence_504'], 'func': lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504}


def lsr_base_universe_d2_026_lsr_060_event_density_z_252(lsr_060_event_density_z_252):
    return _base_universe_d2(lsr_060_event_density_z_252, 26)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_026_lsr_060_event_density_z_252'] = {'inputs': ['lsr_060_event_density_z_252'], 'func': lsr_base_universe_d2_026_lsr_060_event_density_z_252}


def lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21(lsr_061_going_concern_persistence_21):
    return _base_universe_d2(lsr_061_going_concern_persistence_21, 27)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21'] = {'inputs': ['lsr_061_going_concern_persistence_21'], 'func': lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21}


def lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378(lsr_068_going_concern_persistence_378):
    return _base_universe_d2(lsr_068_going_concern_persistence_378, 28)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378'] = {'inputs': ['lsr_068_going_concern_persistence_378'], 'func': lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378}


def lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252(lsr_075_going_concern_persistence_252):
    return _base_universe_d2(lsr_075_going_concern_persistence_252, 29)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252'] = {'inputs': ['lsr_075_going_concern_persistence_252'], 'func': lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252}


def lsr_base_universe_d2_030_lsr_basefill_007(lsr_basefill_007):
    return _base_universe_d2(lsr_basefill_007, 30)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_030_lsr_basefill_007'] = {'inputs': ['lsr_basefill_007'], 'func': lsr_base_universe_d2_030_lsr_basefill_007}


def lsr_base_universe_d2_031_lsr_basefill_014(lsr_basefill_014):
    return _base_universe_d2(lsr_basefill_014, 31)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_031_lsr_basefill_014'] = {'inputs': ['lsr_basefill_014'], 'func': lsr_base_universe_d2_031_lsr_basefill_014}


def lsr_base_universe_d2_032_lsr_basefill_016(lsr_basefill_016):
    return _base_universe_d2(lsr_basefill_016, 32)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_032_lsr_basefill_016'] = {'inputs': ['lsr_basefill_016'], 'func': lsr_base_universe_d2_032_lsr_basefill_016}


def lsr_base_universe_d2_033_lsr_basefill_017(lsr_basefill_017):
    return _base_universe_d2(lsr_basefill_017, 33)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_033_lsr_basefill_017'] = {'inputs': ['lsr_basefill_017'], 'func': lsr_base_universe_d2_033_lsr_basefill_017}


def lsr_base_universe_d2_034_lsr_basefill_021(lsr_basefill_021):
    return _base_universe_d2(lsr_basefill_021, 34)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_034_lsr_basefill_021'] = {'inputs': ['lsr_basefill_021'], 'func': lsr_base_universe_d2_034_lsr_basefill_021}


def lsr_base_universe_d2_035_lsr_basefill_022(lsr_basefill_022):
    return _base_universe_d2(lsr_basefill_022, 35)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_035_lsr_basefill_022'] = {'inputs': ['lsr_basefill_022'], 'func': lsr_base_universe_d2_035_lsr_basefill_022}


def lsr_base_universe_d2_036_lsr_basefill_023(lsr_basefill_023):
    return _base_universe_d2(lsr_basefill_023, 36)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_036_lsr_basefill_023'] = {'inputs': ['lsr_basefill_023'], 'func': lsr_base_universe_d2_036_lsr_basefill_023}


def lsr_base_universe_d2_037_lsr_basefill_024(lsr_basefill_024):
    return _base_universe_d2(lsr_basefill_024, 37)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_037_lsr_basefill_024'] = {'inputs': ['lsr_basefill_024'], 'func': lsr_base_universe_d2_037_lsr_basefill_024}


def lsr_base_universe_d2_038_lsr_basefill_028(lsr_basefill_028):
    return _base_universe_d2(lsr_basefill_028, 38)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_038_lsr_basefill_028'] = {'inputs': ['lsr_basefill_028'], 'func': lsr_base_universe_d2_038_lsr_basefill_028}


def lsr_base_universe_d2_039_lsr_basefill_029(lsr_basefill_029):
    return _base_universe_d2(lsr_basefill_029, 39)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_039_lsr_basefill_029'] = {'inputs': ['lsr_basefill_029'], 'func': lsr_base_universe_d2_039_lsr_basefill_029}


def lsr_base_universe_d2_040_lsr_basefill_030(lsr_basefill_030):
    return _base_universe_d2(lsr_basefill_030, 40)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_040_lsr_basefill_030'] = {'inputs': ['lsr_basefill_030'], 'func': lsr_base_universe_d2_040_lsr_basefill_030}


def lsr_base_universe_d2_041_lsr_basefill_031(lsr_basefill_031):
    return _base_universe_d2(lsr_basefill_031, 41)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_041_lsr_basefill_031'] = {'inputs': ['lsr_basefill_031'], 'func': lsr_base_universe_d2_041_lsr_basefill_031}


def lsr_base_universe_d2_042_lsr_basefill_035(lsr_basefill_035):
    return _base_universe_d2(lsr_basefill_035, 42)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_042_lsr_basefill_035'] = {'inputs': ['lsr_basefill_035'], 'func': lsr_base_universe_d2_042_lsr_basefill_035}


def lsr_base_universe_d2_043_lsr_basefill_036(lsr_basefill_036):
    return _base_universe_d2(lsr_basefill_036, 43)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_043_lsr_basefill_036'] = {'inputs': ['lsr_basefill_036'], 'func': lsr_base_universe_d2_043_lsr_basefill_036}


def lsr_base_universe_d2_044_lsr_basefill_037(lsr_basefill_037):
    return _base_universe_d2(lsr_basefill_037, 44)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_044_lsr_basefill_037'] = {'inputs': ['lsr_basefill_037'], 'func': lsr_base_universe_d2_044_lsr_basefill_037}


def lsr_base_universe_d2_045_lsr_basefill_038(lsr_basefill_038):
    return _base_universe_d2(lsr_basefill_038, 45)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_045_lsr_basefill_038'] = {'inputs': ['lsr_basefill_038'], 'func': lsr_base_universe_d2_045_lsr_basefill_038}


def lsr_base_universe_d2_046_lsr_basefill_042(lsr_basefill_042):
    return _base_universe_d2(lsr_basefill_042, 46)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_046_lsr_basefill_042'] = {'inputs': ['lsr_basefill_042'], 'func': lsr_base_universe_d2_046_lsr_basefill_042}


def lsr_base_universe_d2_047_lsr_basefill_043(lsr_basefill_043):
    return _base_universe_d2(lsr_basefill_043, 47)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_047_lsr_basefill_043'] = {'inputs': ['lsr_basefill_043'], 'func': lsr_base_universe_d2_047_lsr_basefill_043}


def lsr_base_universe_d2_048_lsr_basefill_044(lsr_basefill_044):
    return _base_universe_d2(lsr_basefill_044, 48)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_048_lsr_basefill_044'] = {'inputs': ['lsr_basefill_044'], 'func': lsr_base_universe_d2_048_lsr_basefill_044}


def lsr_base_universe_d2_049_lsr_basefill_045(lsr_basefill_045):
    return _base_universe_d2(lsr_basefill_045, 49)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_049_lsr_basefill_045'] = {'inputs': ['lsr_basefill_045'], 'func': lsr_base_universe_d2_049_lsr_basefill_045}


def lsr_base_universe_d2_050_lsr_basefill_048(lsr_basefill_048):
    return _base_universe_d2(lsr_basefill_048, 50)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_050_lsr_basefill_048'] = {'inputs': ['lsr_basefill_048'], 'func': lsr_base_universe_d2_050_lsr_basefill_048}


def lsr_base_universe_d2_051_lsr_basefill_049(lsr_basefill_049):
    return _base_universe_d2(lsr_basefill_049, 51)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_051_lsr_basefill_049'] = {'inputs': ['lsr_basefill_049'], 'func': lsr_base_universe_d2_051_lsr_basefill_049}


def lsr_base_universe_d2_052_lsr_basefill_050(lsr_basefill_050):
    return _base_universe_d2(lsr_basefill_050, 52)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_052_lsr_basefill_050'] = {'inputs': ['lsr_basefill_050'], 'func': lsr_base_universe_d2_052_lsr_basefill_050}


def lsr_base_universe_d2_053_lsr_basefill_051(lsr_basefill_051):
    return _base_universe_d2(lsr_basefill_051, 53)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_053_lsr_basefill_051'] = {'inputs': ['lsr_basefill_051'], 'func': lsr_base_universe_d2_053_lsr_basefill_051}


def lsr_base_universe_d2_054_lsr_basefill_052(lsr_basefill_052):
    return _base_universe_d2(lsr_basefill_052, 54)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_054_lsr_basefill_052'] = {'inputs': ['lsr_basefill_052'], 'func': lsr_base_universe_d2_054_lsr_basefill_052}


def lsr_base_universe_d2_055_lsr_basefill_055(lsr_basefill_055):
    return _base_universe_d2(lsr_basefill_055, 55)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_055_lsr_basefill_055'] = {'inputs': ['lsr_basefill_055'], 'func': lsr_base_universe_d2_055_lsr_basefill_055}


def lsr_base_universe_d2_056_lsr_basefill_056(lsr_basefill_056):
    return _base_universe_d2(lsr_basefill_056, 56)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_056_lsr_basefill_056'] = {'inputs': ['lsr_basefill_056'], 'func': lsr_base_universe_d2_056_lsr_basefill_056}


def lsr_base_universe_d2_057_lsr_basefill_057(lsr_basefill_057):
    return _base_universe_d2(lsr_basefill_057, 57)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_057_lsr_basefill_057'] = {'inputs': ['lsr_basefill_057'], 'func': lsr_base_universe_d2_057_lsr_basefill_057}


def lsr_base_universe_d2_058_lsr_basefill_058(lsr_basefill_058):
    return _base_universe_d2(lsr_basefill_058, 58)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_058_lsr_basefill_058'] = {'inputs': ['lsr_basefill_058'], 'func': lsr_base_universe_d2_058_lsr_basefill_058}


def lsr_base_universe_d2_059_lsr_basefill_059(lsr_basefill_059):
    return _base_universe_d2(lsr_basefill_059, 59)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_059_lsr_basefill_059'] = {'inputs': ['lsr_basefill_059'], 'func': lsr_base_universe_d2_059_lsr_basefill_059}


def lsr_base_universe_d2_060_lsr_basefill_062(lsr_basefill_062):
    return _base_universe_d2(lsr_basefill_062, 60)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_060_lsr_basefill_062'] = {'inputs': ['lsr_basefill_062'], 'func': lsr_base_universe_d2_060_lsr_basefill_062}


def lsr_base_universe_d2_061_lsr_basefill_063(lsr_basefill_063):
    return _base_universe_d2(lsr_basefill_063, 61)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_061_lsr_basefill_063'] = {'inputs': ['lsr_basefill_063'], 'func': lsr_base_universe_d2_061_lsr_basefill_063}


def lsr_base_universe_d2_062_lsr_basefill_064(lsr_basefill_064):
    return _base_universe_d2(lsr_basefill_064, 62)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_062_lsr_basefill_064'] = {'inputs': ['lsr_basefill_064'], 'func': lsr_base_universe_d2_062_lsr_basefill_064}


def lsr_base_universe_d2_063_lsr_basefill_065(lsr_basefill_065):
    return _base_universe_d2(lsr_basefill_065, 63)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_063_lsr_basefill_065'] = {'inputs': ['lsr_basefill_065'], 'func': lsr_base_universe_d2_063_lsr_basefill_065}


def lsr_base_universe_d2_064_lsr_basefill_066(lsr_basefill_066):
    return _base_universe_d2(lsr_basefill_066, 64)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_064_lsr_basefill_066'] = {'inputs': ['lsr_basefill_066'], 'func': lsr_base_universe_d2_064_lsr_basefill_066}


def lsr_base_universe_d2_065_lsr_basefill_067(lsr_basefill_067):
    return _base_universe_d2(lsr_basefill_067, 65)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_065_lsr_basefill_067'] = {'inputs': ['lsr_basefill_067'], 'func': lsr_base_universe_d2_065_lsr_basefill_067}


def lsr_base_universe_d2_066_lsr_basefill_069(lsr_basefill_069):
    return _base_universe_d2(lsr_basefill_069, 66)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_066_lsr_basefill_069'] = {'inputs': ['lsr_basefill_069'], 'func': lsr_base_universe_d2_066_lsr_basefill_069}


def lsr_base_universe_d2_067_lsr_basefill_070(lsr_basefill_070):
    return _base_universe_d2(lsr_basefill_070, 67)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_067_lsr_basefill_070'] = {'inputs': ['lsr_basefill_070'], 'func': lsr_base_universe_d2_067_lsr_basefill_070}


def lsr_base_universe_d2_068_lsr_basefill_071(lsr_basefill_071):
    return _base_universe_d2(lsr_basefill_071, 68)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_068_lsr_basefill_071'] = {'inputs': ['lsr_basefill_071'], 'func': lsr_base_universe_d2_068_lsr_basefill_071}


def lsr_base_universe_d2_069_lsr_basefill_072(lsr_basefill_072):
    return _base_universe_d2(lsr_basefill_072, 69)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_069_lsr_basefill_072'] = {'inputs': ['lsr_basefill_072'], 'func': lsr_base_universe_d2_069_lsr_basefill_072}


def lsr_base_universe_d2_070_lsr_basefill_073(lsr_basefill_073):
    return _base_universe_d2(lsr_basefill_073, 70)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_070_lsr_basefill_073'] = {'inputs': ['lsr_basefill_073'], 'func': lsr_base_universe_d2_070_lsr_basefill_073}


def lsr_base_universe_d2_071_lsr_basefill_074(lsr_basefill_074):
    return _base_universe_d2(lsr_basefill_074, 71)
LSR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lsr_base_universe_d2_071_lsr_basefill_074'] = {'inputs': ['lsr_basefill_074'], 'func': lsr_base_universe_d2_071_lsr_basefill_074}
