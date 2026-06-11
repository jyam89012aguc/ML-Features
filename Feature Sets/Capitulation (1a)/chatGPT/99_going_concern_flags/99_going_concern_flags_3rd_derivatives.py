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



def gcf_176_gcf_001_dividend_cut_density_21_accel_1(gcf_151_gcf_001_dividend_cut_density_21_roc_1):
    feature = _s(gcf_151_gcf_001_dividend_cut_density_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def gcf_177_gcf_007_listing_tier_decay_1_accel_42(gcf_152_gcf_007_listing_tier_decay_1_roc_42):
    feature = _s(gcf_152_gcf_007_listing_tier_decay_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def gcf_178_gcf_013_delisting_notice_density_1512_accel_126(gcf_153_gcf_013_delisting_notice_density_1512_roc_126):
    feature = _s(gcf_153_gcf_013_delisting_notice_density_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def gcf_179_gcf_019_going_concern_persistence_84_accel_378(gcf_154_gcf_019_going_concern_persistence_84_roc_378):
    feature = _s(gcf_154_gcf_019_going_concern_persistence_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def gcf_180_gcf_025_event_density_z_756_accel_4(gcf_155_gcf_025_event_density_z_756_roc_4):
    feature = _s(gcf_155_gcf_025_event_density_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















GOING_CONCERN_FLAGS_REGISTRY_3RD_DERIVATIVES = {
    'gcf_176_gcf_001_dividend_cut_density_21_accel_1': {'inputs': ['gcf_151_gcf_001_dividend_cut_density_21_roc_1'], 'func': gcf_176_gcf_001_dividend_cut_density_21_accel_1},
    'gcf_177_gcf_007_listing_tier_decay_1_accel_42': {'inputs': ['gcf_152_gcf_007_listing_tier_decay_1_roc_42'], 'func': gcf_177_gcf_007_listing_tier_decay_1_accel_42},
    'gcf_178_gcf_013_delisting_notice_density_1512_accel_126': {'inputs': ['gcf_153_gcf_013_delisting_notice_density_1512_roc_126'], 'func': gcf_178_gcf_013_delisting_notice_density_1512_accel_126},
    'gcf_179_gcf_019_going_concern_persistence_84_accel_378': {'inputs': ['gcf_154_gcf_019_going_concern_persistence_84_roc_378'], 'func': gcf_179_gcf_019_going_concern_persistence_84_accel_378},
    'gcf_180_gcf_025_event_density_z_756_accel_4': {'inputs': ['gcf_155_gcf_025_event_density_z_756_roc_4'], 'func': gcf_180_gcf_025_event_density_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def gcf_replacement_d3_001(gcf_replacement_d2_001):
    feature = _clean(gcf_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_001'] = {'inputs': ['gcf_replacement_d2_001'], 'func': gcf_replacement_d3_001}


def gcf_replacement_d3_002(gcf_replacement_d2_002):
    feature = _clean(gcf_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_002'] = {'inputs': ['gcf_replacement_d2_002'], 'func': gcf_replacement_d3_002}


def gcf_replacement_d3_003(gcf_replacement_d2_003):
    feature = _clean(gcf_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_003'] = {'inputs': ['gcf_replacement_d2_003'], 'func': gcf_replacement_d3_003}


def gcf_replacement_d3_004(gcf_replacement_d2_004):
    feature = _clean(gcf_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_004'] = {'inputs': ['gcf_replacement_d2_004'], 'func': gcf_replacement_d3_004}


def gcf_replacement_d3_005(gcf_replacement_d2_005):
    feature = _clean(gcf_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_005'] = {'inputs': ['gcf_replacement_d2_005'], 'func': gcf_replacement_d3_005}


def gcf_replacement_d3_006(gcf_replacement_d2_006):
    feature = _clean(gcf_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_006'] = {'inputs': ['gcf_replacement_d2_006'], 'func': gcf_replacement_d3_006}


def gcf_replacement_d3_007(gcf_replacement_d2_007):
    feature = _clean(gcf_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_007'] = {'inputs': ['gcf_replacement_d2_007'], 'func': gcf_replacement_d3_007}


def gcf_replacement_d3_008(gcf_replacement_d2_008):
    feature = _clean(gcf_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_008'] = {'inputs': ['gcf_replacement_d2_008'], 'func': gcf_replacement_d3_008}


def gcf_replacement_d3_009(gcf_replacement_d2_009):
    feature = _clean(gcf_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_009'] = {'inputs': ['gcf_replacement_d2_009'], 'func': gcf_replacement_d3_009}


def gcf_replacement_d3_010(gcf_replacement_d2_010):
    feature = _clean(gcf_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_010'] = {'inputs': ['gcf_replacement_d2_010'], 'func': gcf_replacement_d3_010}


def gcf_replacement_d3_011(gcf_replacement_d2_011):
    feature = _clean(gcf_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_011'] = {'inputs': ['gcf_replacement_d2_011'], 'func': gcf_replacement_d3_011}


def gcf_replacement_d3_012(gcf_replacement_d2_012):
    feature = _clean(gcf_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_012'] = {'inputs': ['gcf_replacement_d2_012'], 'func': gcf_replacement_d3_012}


def gcf_replacement_d3_013(gcf_replacement_d2_013):
    feature = _clean(gcf_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_013'] = {'inputs': ['gcf_replacement_d2_013'], 'func': gcf_replacement_d3_013}


def gcf_replacement_d3_014(gcf_replacement_d2_014):
    feature = _clean(gcf_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_014'] = {'inputs': ['gcf_replacement_d2_014'], 'func': gcf_replacement_d3_014}


def gcf_replacement_d3_015(gcf_replacement_d2_015):
    feature = _clean(gcf_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_015'] = {'inputs': ['gcf_replacement_d2_015'], 'func': gcf_replacement_d3_015}


def gcf_replacement_d3_016(gcf_replacement_d2_016):
    feature = _clean(gcf_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_016'] = {'inputs': ['gcf_replacement_d2_016'], 'func': gcf_replacement_d3_016}


def gcf_replacement_d3_017(gcf_replacement_d2_017):
    feature = _clean(gcf_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_017'] = {'inputs': ['gcf_replacement_d2_017'], 'func': gcf_replacement_d3_017}


def gcf_replacement_d3_018(gcf_replacement_d2_018):
    feature = _clean(gcf_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_018'] = {'inputs': ['gcf_replacement_d2_018'], 'func': gcf_replacement_d3_018}


def gcf_replacement_d3_019(gcf_replacement_d2_019):
    feature = _clean(gcf_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_019'] = {'inputs': ['gcf_replacement_d2_019'], 'func': gcf_replacement_d3_019}


def gcf_replacement_d3_020(gcf_replacement_d2_020):
    feature = _clean(gcf_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_020'] = {'inputs': ['gcf_replacement_d2_020'], 'func': gcf_replacement_d3_020}


def gcf_replacement_d3_021(gcf_replacement_d2_021):
    feature = _clean(gcf_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_021'] = {'inputs': ['gcf_replacement_d2_021'], 'func': gcf_replacement_d3_021}


def gcf_replacement_d3_022(gcf_replacement_d2_022):
    feature = _clean(gcf_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_022'] = {'inputs': ['gcf_replacement_d2_022'], 'func': gcf_replacement_d3_022}


def gcf_replacement_d3_023(gcf_replacement_d2_023):
    feature = _clean(gcf_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_023'] = {'inputs': ['gcf_replacement_d2_023'], 'func': gcf_replacement_d3_023}


def gcf_replacement_d3_024(gcf_replacement_d2_024):
    feature = _clean(gcf_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_024'] = {'inputs': ['gcf_replacement_d2_024'], 'func': gcf_replacement_d3_024}


def gcf_replacement_d3_025(gcf_replacement_d2_025):
    feature = _clean(gcf_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_025'] = {'inputs': ['gcf_replacement_d2_025'], 'func': gcf_replacement_d3_025}


def gcf_replacement_d3_026(gcf_replacement_d2_026):
    feature = _clean(gcf_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_026'] = {'inputs': ['gcf_replacement_d2_026'], 'func': gcf_replacement_d3_026}


def gcf_replacement_d3_027(gcf_replacement_d2_027):
    feature = _clean(gcf_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_027'] = {'inputs': ['gcf_replacement_d2_027'], 'func': gcf_replacement_d3_027}


def gcf_replacement_d3_028(gcf_replacement_d2_028):
    feature = _clean(gcf_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_028'] = {'inputs': ['gcf_replacement_d2_028'], 'func': gcf_replacement_d3_028}


def gcf_replacement_d3_029(gcf_replacement_d2_029):
    feature = _clean(gcf_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_029'] = {'inputs': ['gcf_replacement_d2_029'], 'func': gcf_replacement_d3_029}


def gcf_replacement_d3_030(gcf_replacement_d2_030):
    feature = _clean(gcf_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_030'] = {'inputs': ['gcf_replacement_d2_030'], 'func': gcf_replacement_d3_030}


def gcf_replacement_d3_031(gcf_replacement_d2_031):
    feature = _clean(gcf_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_031'] = {'inputs': ['gcf_replacement_d2_031'], 'func': gcf_replacement_d3_031}


def gcf_replacement_d3_032(gcf_replacement_d2_032):
    feature = _clean(gcf_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_032'] = {'inputs': ['gcf_replacement_d2_032'], 'func': gcf_replacement_d3_032}


def gcf_replacement_d3_033(gcf_replacement_d2_033):
    feature = _clean(gcf_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_033'] = {'inputs': ['gcf_replacement_d2_033'], 'func': gcf_replacement_d3_033}


def gcf_replacement_d3_034(gcf_replacement_d2_034):
    feature = _clean(gcf_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_034'] = {'inputs': ['gcf_replacement_d2_034'], 'func': gcf_replacement_d3_034}


def gcf_replacement_d3_035(gcf_replacement_d2_035):
    feature = _clean(gcf_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_035'] = {'inputs': ['gcf_replacement_d2_035'], 'func': gcf_replacement_d3_035}


def gcf_replacement_d3_036(gcf_replacement_d2_036):
    feature = _clean(gcf_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_036'] = {'inputs': ['gcf_replacement_d2_036'], 'func': gcf_replacement_d3_036}


def gcf_replacement_d3_037(gcf_replacement_d2_037):
    feature = _clean(gcf_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_037'] = {'inputs': ['gcf_replacement_d2_037'], 'func': gcf_replacement_d3_037}


def gcf_replacement_d3_038(gcf_replacement_d2_038):
    feature = _clean(gcf_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_038'] = {'inputs': ['gcf_replacement_d2_038'], 'func': gcf_replacement_d3_038}


def gcf_replacement_d3_039(gcf_replacement_d2_039):
    feature = _clean(gcf_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_039'] = {'inputs': ['gcf_replacement_d2_039'], 'func': gcf_replacement_d3_039}


def gcf_replacement_d3_040(gcf_replacement_d2_040):
    feature = _clean(gcf_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_040'] = {'inputs': ['gcf_replacement_d2_040'], 'func': gcf_replacement_d3_040}


def gcf_replacement_d3_041(gcf_replacement_d2_041):
    feature = _clean(gcf_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_041'] = {'inputs': ['gcf_replacement_d2_041'], 'func': gcf_replacement_d3_041}


def gcf_replacement_d3_042(gcf_replacement_d2_042):
    feature = _clean(gcf_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_042'] = {'inputs': ['gcf_replacement_d2_042'], 'func': gcf_replacement_d3_042}


def gcf_replacement_d3_043(gcf_replacement_d2_043):
    feature = _clean(gcf_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_043'] = {'inputs': ['gcf_replacement_d2_043'], 'func': gcf_replacement_d3_043}


def gcf_replacement_d3_044(gcf_replacement_d2_044):
    feature = _clean(gcf_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_044'] = {'inputs': ['gcf_replacement_d2_044'], 'func': gcf_replacement_d3_044}


def gcf_replacement_d3_045(gcf_replacement_d2_045):
    feature = _clean(gcf_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_045'] = {'inputs': ['gcf_replacement_d2_045'], 'func': gcf_replacement_d3_045}


def gcf_replacement_d3_046(gcf_replacement_d2_046):
    feature = _clean(gcf_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_046'] = {'inputs': ['gcf_replacement_d2_046'], 'func': gcf_replacement_d3_046}


def gcf_replacement_d3_047(gcf_replacement_d2_047):
    feature = _clean(gcf_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_047'] = {'inputs': ['gcf_replacement_d2_047'], 'func': gcf_replacement_d3_047}


def gcf_replacement_d3_048(gcf_replacement_d2_048):
    feature = _clean(gcf_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_048'] = {'inputs': ['gcf_replacement_d2_048'], 'func': gcf_replacement_d3_048}


def gcf_replacement_d3_049(gcf_replacement_d2_049):
    feature = _clean(gcf_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_049'] = {'inputs': ['gcf_replacement_d2_049'], 'func': gcf_replacement_d3_049}


def gcf_replacement_d3_050(gcf_replacement_d2_050):
    feature = _clean(gcf_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_050'] = {'inputs': ['gcf_replacement_d2_050'], 'func': gcf_replacement_d3_050}


def gcf_replacement_d3_051(gcf_replacement_d2_051):
    feature = _clean(gcf_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_051'] = {'inputs': ['gcf_replacement_d2_051'], 'func': gcf_replacement_d3_051}


def gcf_replacement_d3_052(gcf_replacement_d2_052):
    feature = _clean(gcf_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_052'] = {'inputs': ['gcf_replacement_d2_052'], 'func': gcf_replacement_d3_052}


def gcf_replacement_d3_053(gcf_replacement_d2_053):
    feature = _clean(gcf_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_053'] = {'inputs': ['gcf_replacement_d2_053'], 'func': gcf_replacement_d3_053}


def gcf_replacement_d3_054(gcf_replacement_d2_054):
    feature = _clean(gcf_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_054'] = {'inputs': ['gcf_replacement_d2_054'], 'func': gcf_replacement_d3_054}


def gcf_replacement_d3_055(gcf_replacement_d2_055):
    feature = _clean(gcf_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_055'] = {'inputs': ['gcf_replacement_d2_055'], 'func': gcf_replacement_d3_055}


def gcf_replacement_d3_056(gcf_replacement_d2_056):
    feature = _clean(gcf_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_056'] = {'inputs': ['gcf_replacement_d2_056'], 'func': gcf_replacement_d3_056}


def gcf_replacement_d3_057(gcf_replacement_d2_057):
    feature = _clean(gcf_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_057'] = {'inputs': ['gcf_replacement_d2_057'], 'func': gcf_replacement_d3_057}


def gcf_replacement_d3_058(gcf_replacement_d2_058):
    feature = _clean(gcf_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_058'] = {'inputs': ['gcf_replacement_d2_058'], 'func': gcf_replacement_d3_058}


def gcf_replacement_d3_059(gcf_replacement_d2_059):
    feature = _clean(gcf_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_059'] = {'inputs': ['gcf_replacement_d2_059'], 'func': gcf_replacement_d3_059}


def gcf_replacement_d3_060(gcf_replacement_d2_060):
    feature = _clean(gcf_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_060'] = {'inputs': ['gcf_replacement_d2_060'], 'func': gcf_replacement_d3_060}


def gcf_replacement_d3_061(gcf_replacement_d2_061):
    feature = _clean(gcf_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_061'] = {'inputs': ['gcf_replacement_d2_061'], 'func': gcf_replacement_d3_061}


def gcf_replacement_d3_062(gcf_replacement_d2_062):
    feature = _clean(gcf_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_062'] = {'inputs': ['gcf_replacement_d2_062'], 'func': gcf_replacement_d3_062}


def gcf_replacement_d3_063(gcf_replacement_d2_063):
    feature = _clean(gcf_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_063'] = {'inputs': ['gcf_replacement_d2_063'], 'func': gcf_replacement_d3_063}


def gcf_replacement_d3_064(gcf_replacement_d2_064):
    feature = _clean(gcf_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_064'] = {'inputs': ['gcf_replacement_d2_064'], 'func': gcf_replacement_d3_064}


def gcf_replacement_d3_065(gcf_replacement_d2_065):
    feature = _clean(gcf_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_065'] = {'inputs': ['gcf_replacement_d2_065'], 'func': gcf_replacement_d3_065}


def gcf_replacement_d3_066(gcf_replacement_d2_066):
    feature = _clean(gcf_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_066'] = {'inputs': ['gcf_replacement_d2_066'], 'func': gcf_replacement_d3_066}


def gcf_replacement_d3_067(gcf_replacement_d2_067):
    feature = _clean(gcf_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_067'] = {'inputs': ['gcf_replacement_d2_067'], 'func': gcf_replacement_d3_067}


def gcf_replacement_d3_068(gcf_replacement_d2_068):
    feature = _clean(gcf_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_068'] = {'inputs': ['gcf_replacement_d2_068'], 'func': gcf_replacement_d3_068}


def gcf_replacement_d3_069(gcf_replacement_d2_069):
    feature = _clean(gcf_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_069'] = {'inputs': ['gcf_replacement_d2_069'], 'func': gcf_replacement_d3_069}


def gcf_replacement_d3_070(gcf_replacement_d2_070):
    feature = _clean(gcf_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_070'] = {'inputs': ['gcf_replacement_d2_070'], 'func': gcf_replacement_d3_070}


def gcf_replacement_d3_071(gcf_replacement_d2_071):
    feature = _clean(gcf_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_071'] = {'inputs': ['gcf_replacement_d2_071'], 'func': gcf_replacement_d3_071}


def gcf_replacement_d3_072(gcf_replacement_d2_072):
    feature = _clean(gcf_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_072'] = {'inputs': ['gcf_replacement_d2_072'], 'func': gcf_replacement_d3_072}


def gcf_replacement_d3_073(gcf_replacement_d2_073):
    feature = _clean(gcf_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_073'] = {'inputs': ['gcf_replacement_d2_073'], 'func': gcf_replacement_d3_073}


def gcf_replacement_d3_074(gcf_replacement_d2_074):
    feature = _clean(gcf_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_074'] = {'inputs': ['gcf_replacement_d2_074'], 'func': gcf_replacement_d3_074}


def gcf_replacement_d3_075(gcf_replacement_d2_075):
    feature = _clean(gcf_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_075'] = {'inputs': ['gcf_replacement_d2_075'], 'func': gcf_replacement_d3_075}


def gcf_replacement_d3_076(gcf_replacement_d2_076):
    feature = _clean(gcf_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_076'] = {'inputs': ['gcf_replacement_d2_076'], 'func': gcf_replacement_d3_076}


def gcf_replacement_d3_077(gcf_replacement_d2_077):
    feature = _clean(gcf_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_077'] = {'inputs': ['gcf_replacement_d2_077'], 'func': gcf_replacement_d3_077}


def gcf_replacement_d3_078(gcf_replacement_d2_078):
    feature = _clean(gcf_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_078'] = {'inputs': ['gcf_replacement_d2_078'], 'func': gcf_replacement_d3_078}


def gcf_replacement_d3_079(gcf_replacement_d2_079):
    feature = _clean(gcf_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_079'] = {'inputs': ['gcf_replacement_d2_079'], 'func': gcf_replacement_d3_079}


def gcf_replacement_d3_080(gcf_replacement_d2_080):
    feature = _clean(gcf_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_080'] = {'inputs': ['gcf_replacement_d2_080'], 'func': gcf_replacement_d3_080}


def gcf_replacement_d3_081(gcf_replacement_d2_081):
    feature = _clean(gcf_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_081'] = {'inputs': ['gcf_replacement_d2_081'], 'func': gcf_replacement_d3_081}


def gcf_replacement_d3_082(gcf_replacement_d2_082):
    feature = _clean(gcf_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_082'] = {'inputs': ['gcf_replacement_d2_082'], 'func': gcf_replacement_d3_082}


def gcf_replacement_d3_083(gcf_replacement_d2_083):
    feature = _clean(gcf_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_083'] = {'inputs': ['gcf_replacement_d2_083'], 'func': gcf_replacement_d3_083}


def gcf_replacement_d3_084(gcf_replacement_d2_084):
    feature = _clean(gcf_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_084'] = {'inputs': ['gcf_replacement_d2_084'], 'func': gcf_replacement_d3_084}


def gcf_replacement_d3_085(gcf_replacement_d2_085):
    feature = _clean(gcf_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_085'] = {'inputs': ['gcf_replacement_d2_085'], 'func': gcf_replacement_d3_085}


def gcf_replacement_d3_086(gcf_replacement_d2_086):
    feature = _clean(gcf_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_086'] = {'inputs': ['gcf_replacement_d2_086'], 'func': gcf_replacement_d3_086}


def gcf_replacement_d3_087(gcf_replacement_d2_087):
    feature = _clean(gcf_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_087'] = {'inputs': ['gcf_replacement_d2_087'], 'func': gcf_replacement_d3_087}


def gcf_replacement_d3_088(gcf_replacement_d2_088):
    feature = _clean(gcf_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_088'] = {'inputs': ['gcf_replacement_d2_088'], 'func': gcf_replacement_d3_088}


def gcf_replacement_d3_089(gcf_replacement_d2_089):
    feature = _clean(gcf_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_089'] = {'inputs': ['gcf_replacement_d2_089'], 'func': gcf_replacement_d3_089}


def gcf_replacement_d3_090(gcf_replacement_d2_090):
    feature = _clean(gcf_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_090'] = {'inputs': ['gcf_replacement_d2_090'], 'func': gcf_replacement_d3_090}


def gcf_replacement_d3_091(gcf_replacement_d2_091):
    feature = _clean(gcf_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_091'] = {'inputs': ['gcf_replacement_d2_091'], 'func': gcf_replacement_d3_091}


def gcf_replacement_d3_092(gcf_replacement_d2_092):
    feature = _clean(gcf_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_092'] = {'inputs': ['gcf_replacement_d2_092'], 'func': gcf_replacement_d3_092}


def gcf_replacement_d3_093(gcf_replacement_d2_093):
    feature = _clean(gcf_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_093'] = {'inputs': ['gcf_replacement_d2_093'], 'func': gcf_replacement_d3_093}


def gcf_replacement_d3_094(gcf_replacement_d2_094):
    feature = _clean(gcf_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_094'] = {'inputs': ['gcf_replacement_d2_094'], 'func': gcf_replacement_d3_094}


def gcf_replacement_d3_095(gcf_replacement_d2_095):
    feature = _clean(gcf_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_095'] = {'inputs': ['gcf_replacement_d2_095'], 'func': gcf_replacement_d3_095}


def gcf_replacement_d3_096(gcf_replacement_d2_096):
    feature = _clean(gcf_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_096'] = {'inputs': ['gcf_replacement_d2_096'], 'func': gcf_replacement_d3_096}


def gcf_replacement_d3_097(gcf_replacement_d2_097):
    feature = _clean(gcf_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_097'] = {'inputs': ['gcf_replacement_d2_097'], 'func': gcf_replacement_d3_097}


def gcf_replacement_d3_098(gcf_replacement_d2_098):
    feature = _clean(gcf_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_098'] = {'inputs': ['gcf_replacement_d2_098'], 'func': gcf_replacement_d3_098}


def gcf_replacement_d3_099(gcf_replacement_d2_099):
    feature = _clean(gcf_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_099'] = {'inputs': ['gcf_replacement_d2_099'], 'func': gcf_replacement_d3_099}


def gcf_replacement_d3_100(gcf_replacement_d2_100):
    feature = _clean(gcf_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_100'] = {'inputs': ['gcf_replacement_d2_100'], 'func': gcf_replacement_d3_100}


def gcf_replacement_d3_101(gcf_replacement_d2_101):
    feature = _clean(gcf_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_101'] = {'inputs': ['gcf_replacement_d2_101'], 'func': gcf_replacement_d3_101}


def gcf_replacement_d3_102(gcf_replacement_d2_102):
    feature = _clean(gcf_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_102'] = {'inputs': ['gcf_replacement_d2_102'], 'func': gcf_replacement_d3_102}


def gcf_replacement_d3_103(gcf_replacement_d2_103):
    feature = _clean(gcf_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_103'] = {'inputs': ['gcf_replacement_d2_103'], 'func': gcf_replacement_d3_103}


def gcf_replacement_d3_104(gcf_replacement_d2_104):
    feature = _clean(gcf_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_104'] = {'inputs': ['gcf_replacement_d2_104'], 'func': gcf_replacement_d3_104}


def gcf_replacement_d3_105(gcf_replacement_d2_105):
    feature = _clean(gcf_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_105'] = {'inputs': ['gcf_replacement_d2_105'], 'func': gcf_replacement_d3_105}


def gcf_replacement_d3_106(gcf_replacement_d2_106):
    feature = _clean(gcf_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_106'] = {'inputs': ['gcf_replacement_d2_106'], 'func': gcf_replacement_d3_106}


def gcf_replacement_d3_107(gcf_replacement_d2_107):
    feature = _clean(gcf_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_107'] = {'inputs': ['gcf_replacement_d2_107'], 'func': gcf_replacement_d3_107}


def gcf_replacement_d3_108(gcf_replacement_d2_108):
    feature = _clean(gcf_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_108'] = {'inputs': ['gcf_replacement_d2_108'], 'func': gcf_replacement_d3_108}


def gcf_replacement_d3_109(gcf_replacement_d2_109):
    feature = _clean(gcf_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_109'] = {'inputs': ['gcf_replacement_d2_109'], 'func': gcf_replacement_d3_109}


def gcf_replacement_d3_110(gcf_replacement_d2_110):
    feature = _clean(gcf_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_110'] = {'inputs': ['gcf_replacement_d2_110'], 'func': gcf_replacement_d3_110}


def gcf_replacement_d3_111(gcf_replacement_d2_111):
    feature = _clean(gcf_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_111'] = {'inputs': ['gcf_replacement_d2_111'], 'func': gcf_replacement_d3_111}


def gcf_replacement_d3_112(gcf_replacement_d2_112):
    feature = _clean(gcf_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_112'] = {'inputs': ['gcf_replacement_d2_112'], 'func': gcf_replacement_d3_112}


def gcf_replacement_d3_113(gcf_replacement_d2_113):
    feature = _clean(gcf_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_113'] = {'inputs': ['gcf_replacement_d2_113'], 'func': gcf_replacement_d3_113}


def gcf_replacement_d3_114(gcf_replacement_d2_114):
    feature = _clean(gcf_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_114'] = {'inputs': ['gcf_replacement_d2_114'], 'func': gcf_replacement_d3_114}


def gcf_replacement_d3_115(gcf_replacement_d2_115):
    feature = _clean(gcf_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_115'] = {'inputs': ['gcf_replacement_d2_115'], 'func': gcf_replacement_d3_115}


def gcf_replacement_d3_116(gcf_replacement_d2_116):
    feature = _clean(gcf_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_116'] = {'inputs': ['gcf_replacement_d2_116'], 'func': gcf_replacement_d3_116}


def gcf_replacement_d3_117(gcf_replacement_d2_117):
    feature = _clean(gcf_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_117'] = {'inputs': ['gcf_replacement_d2_117'], 'func': gcf_replacement_d3_117}


def gcf_replacement_d3_118(gcf_replacement_d2_118):
    feature = _clean(gcf_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_118'] = {'inputs': ['gcf_replacement_d2_118'], 'func': gcf_replacement_d3_118}


def gcf_replacement_d3_119(gcf_replacement_d2_119):
    feature = _clean(gcf_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_119'] = {'inputs': ['gcf_replacement_d2_119'], 'func': gcf_replacement_d3_119}


def gcf_replacement_d3_120(gcf_replacement_d2_120):
    feature = _clean(gcf_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_120'] = {'inputs': ['gcf_replacement_d2_120'], 'func': gcf_replacement_d3_120}


def gcf_replacement_d3_121(gcf_replacement_d2_121):
    feature = _clean(gcf_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_121'] = {'inputs': ['gcf_replacement_d2_121'], 'func': gcf_replacement_d3_121}


def gcf_replacement_d3_122(gcf_replacement_d2_122):
    feature = _clean(gcf_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_122'] = {'inputs': ['gcf_replacement_d2_122'], 'func': gcf_replacement_d3_122}


def gcf_replacement_d3_123(gcf_replacement_d2_123):
    feature = _clean(gcf_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_123'] = {'inputs': ['gcf_replacement_d2_123'], 'func': gcf_replacement_d3_123}


def gcf_replacement_d3_124(gcf_replacement_d2_124):
    feature = _clean(gcf_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_124'] = {'inputs': ['gcf_replacement_d2_124'], 'func': gcf_replacement_d3_124}


def gcf_replacement_d3_125(gcf_replacement_d2_125):
    feature = _clean(gcf_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_125'] = {'inputs': ['gcf_replacement_d2_125'], 'func': gcf_replacement_d3_125}


def gcf_replacement_d3_126(gcf_replacement_d2_126):
    feature = _clean(gcf_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_126'] = {'inputs': ['gcf_replacement_d2_126'], 'func': gcf_replacement_d3_126}


def gcf_replacement_d3_127(gcf_replacement_d2_127):
    feature = _clean(gcf_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_127'] = {'inputs': ['gcf_replacement_d2_127'], 'func': gcf_replacement_d3_127}


def gcf_replacement_d3_128(gcf_replacement_d2_128):
    feature = _clean(gcf_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_128'] = {'inputs': ['gcf_replacement_d2_128'], 'func': gcf_replacement_d3_128}


def gcf_replacement_d3_129(gcf_replacement_d2_129):
    feature = _clean(gcf_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_129'] = {'inputs': ['gcf_replacement_d2_129'], 'func': gcf_replacement_d3_129}


def gcf_replacement_d3_130(gcf_replacement_d2_130):
    feature = _clean(gcf_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_130'] = {'inputs': ['gcf_replacement_d2_130'], 'func': gcf_replacement_d3_130}


def gcf_replacement_d3_131(gcf_replacement_d2_131):
    feature = _clean(gcf_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_131'] = {'inputs': ['gcf_replacement_d2_131'], 'func': gcf_replacement_d3_131}


def gcf_replacement_d3_132(gcf_replacement_d2_132):
    feature = _clean(gcf_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_132'] = {'inputs': ['gcf_replacement_d2_132'], 'func': gcf_replacement_d3_132}


def gcf_replacement_d3_133(gcf_replacement_d2_133):
    feature = _clean(gcf_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_133'] = {'inputs': ['gcf_replacement_d2_133'], 'func': gcf_replacement_d3_133}


def gcf_replacement_d3_134(gcf_replacement_d2_134):
    feature = _clean(gcf_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_134'] = {'inputs': ['gcf_replacement_d2_134'], 'func': gcf_replacement_d3_134}


def gcf_replacement_d3_135(gcf_replacement_d2_135):
    feature = _clean(gcf_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_135'] = {'inputs': ['gcf_replacement_d2_135'], 'func': gcf_replacement_d3_135}


def gcf_replacement_d3_136(gcf_replacement_d2_136):
    feature = _clean(gcf_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_136'] = {'inputs': ['gcf_replacement_d2_136'], 'func': gcf_replacement_d3_136}


def gcf_replacement_d3_137(gcf_replacement_d2_137):
    feature = _clean(gcf_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_137'] = {'inputs': ['gcf_replacement_d2_137'], 'func': gcf_replacement_d3_137}


def gcf_replacement_d3_138(gcf_replacement_d2_138):
    feature = _clean(gcf_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_138'] = {'inputs': ['gcf_replacement_d2_138'], 'func': gcf_replacement_d3_138}


def gcf_replacement_d3_139(gcf_replacement_d2_139):
    feature = _clean(gcf_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_139'] = {'inputs': ['gcf_replacement_d2_139'], 'func': gcf_replacement_d3_139}


def gcf_replacement_d3_140(gcf_replacement_d2_140):
    feature = _clean(gcf_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_140'] = {'inputs': ['gcf_replacement_d2_140'], 'func': gcf_replacement_d3_140}


def gcf_replacement_d3_141(gcf_replacement_d2_141):
    feature = _clean(gcf_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_141'] = {'inputs': ['gcf_replacement_d2_141'], 'func': gcf_replacement_d3_141}


def gcf_replacement_d3_142(gcf_replacement_d2_142):
    feature = _clean(gcf_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_142'] = {'inputs': ['gcf_replacement_d2_142'], 'func': gcf_replacement_d3_142}


def gcf_replacement_d3_143(gcf_replacement_d2_143):
    feature = _clean(gcf_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_143'] = {'inputs': ['gcf_replacement_d2_143'], 'func': gcf_replacement_d3_143}


def gcf_replacement_d3_144(gcf_replacement_d2_144):
    feature = _clean(gcf_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_144'] = {'inputs': ['gcf_replacement_d2_144'], 'func': gcf_replacement_d3_144}


def gcf_replacement_d3_145(gcf_replacement_d2_145):
    feature = _clean(gcf_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_145'] = {'inputs': ['gcf_replacement_d2_145'], 'func': gcf_replacement_d3_145}


def gcf_replacement_d3_146(gcf_replacement_d2_146):
    feature = _clean(gcf_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_146'] = {'inputs': ['gcf_replacement_d2_146'], 'func': gcf_replacement_d3_146}


def gcf_replacement_d3_147(gcf_replacement_d2_147):
    feature = _clean(gcf_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_147'] = {'inputs': ['gcf_replacement_d2_147'], 'func': gcf_replacement_d3_147}


def gcf_replacement_d3_148(gcf_replacement_d2_148):
    feature = _clean(gcf_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_148'] = {'inputs': ['gcf_replacement_d2_148'], 'func': gcf_replacement_d3_148}


def gcf_replacement_d3_149(gcf_replacement_d2_149):
    feature = _clean(gcf_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_149'] = {'inputs': ['gcf_replacement_d2_149'], 'func': gcf_replacement_d3_149}


def gcf_replacement_d3_150(gcf_replacement_d2_150):
    feature = _clean(gcf_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_150'] = {'inputs': ['gcf_replacement_d2_150'], 'func': gcf_replacement_d3_150}


def gcf_replacement_d3_151(gcf_replacement_d2_151):
    feature = _clean(gcf_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
GCF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gcf_replacement_d3_151'] = {'inputs': ['gcf_replacement_d2_151'], 'func': gcf_replacement_d3_151}


# Third-derivative extensions for repaired first-base features.
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gcf_base_universe_d3_001_gcf_002_dividend_suspension_density_42(gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42):
    return _base_universe_d3(gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42, 1)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_001_gcf_002_dividend_suspension_density_42'] = {'inputs': ['gcf_base_universe_d2_001_gcf_002_dividend_suspension_density_42'], 'func': gcf_base_universe_d3_001_gcf_002_dividend_suspension_density_42}


def gcf_base_universe_d3_002_gcf_003_reverse_split_density_63(gcf_base_universe_d2_002_gcf_003_reverse_split_density_63):
    return _base_universe_d3(gcf_base_universe_d2_002_gcf_003_reverse_split_density_63, 2)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_002_gcf_003_reverse_split_density_63'] = {'inputs': ['gcf_base_universe_d2_002_gcf_003_reverse_split_density_63'], 'func': gcf_base_universe_d3_002_gcf_003_reverse_split_density_63}


def gcf_base_universe_d3_003_gcf_004_event_density_z_84(gcf_base_universe_d2_003_gcf_004_event_density_z_84):
    return _base_universe_d3(gcf_base_universe_d2_003_gcf_004_event_density_z_84, 3)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_003_gcf_004_event_density_z_84'] = {'inputs': ['gcf_base_universe_d2_003_gcf_004_event_density_z_84'], 'func': gcf_base_universe_d3_003_gcf_004_event_density_z_84}


def gcf_base_universe_d3_004_gcf_005_going_concern_persistence_126(gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126):
    return _base_universe_d3(gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126, 4)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_004_gcf_005_going_concern_persistence_126'] = {'inputs': ['gcf_base_universe_d2_004_gcf_005_going_concern_persistence_126'], 'func': gcf_base_universe_d3_004_gcf_005_going_concern_persistence_126}


def gcf_base_universe_d3_005_gcf_006_delisting_notice_density_189(gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189):
    return _base_universe_d3(gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189, 5)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_005_gcf_006_delisting_notice_density_189'] = {'inputs': ['gcf_base_universe_d2_005_gcf_006_delisting_notice_density_189'], 'func': gcf_base_universe_d3_005_gcf_006_delisting_notice_density_189}


def gcf_base_universe_d3_006_gcf_008_dividend_cut_density_378(gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378):
    return _base_universe_d3(gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378, 6)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_006_gcf_008_dividend_cut_density_378'] = {'inputs': ['gcf_base_universe_d2_006_gcf_008_dividend_cut_density_378'], 'func': gcf_base_universe_d3_006_gcf_008_dividend_cut_density_378}


def gcf_base_universe_d3_007_gcf_009_dividend_suspension_density_504(gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504):
    return _base_universe_d3(gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504, 7)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_007_gcf_009_dividend_suspension_density_504'] = {'inputs': ['gcf_base_universe_d2_007_gcf_009_dividend_suspension_density_504'], 'func': gcf_base_universe_d3_007_gcf_009_dividend_suspension_density_504}


def gcf_base_universe_d3_008_gcf_010_reverse_split_density_756(gcf_base_universe_d2_008_gcf_010_reverse_split_density_756):
    return _base_universe_d3(gcf_base_universe_d2_008_gcf_010_reverse_split_density_756, 8)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_008_gcf_010_reverse_split_density_756'] = {'inputs': ['gcf_base_universe_d2_008_gcf_010_reverse_split_density_756'], 'func': gcf_base_universe_d3_008_gcf_010_reverse_split_density_756}


def gcf_base_universe_d3_009_gcf_011_event_density_z_1008(gcf_base_universe_d2_009_gcf_011_event_density_z_1008):
    return _base_universe_d3(gcf_base_universe_d2_009_gcf_011_event_density_z_1008, 9)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_009_gcf_011_event_density_z_1008'] = {'inputs': ['gcf_base_universe_d2_009_gcf_011_event_density_z_1008'], 'func': gcf_base_universe_d3_009_gcf_011_event_density_z_1008}


def gcf_base_universe_d3_010_gcf_012_going_concern_persistence_1260(gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260):
    return _base_universe_d3(gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260, 10)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_010_gcf_012_going_concern_persistence_1260'] = {'inputs': ['gcf_base_universe_d2_010_gcf_012_going_concern_persistence_1260'], 'func': gcf_base_universe_d3_010_gcf_012_going_concern_persistence_1260}


def gcf_base_universe_d3_011_gcf_015_dividend_cut_density_252(gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252):
    return _base_universe_d3(gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252, 11)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_011_gcf_015_dividend_cut_density_252'] = {'inputs': ['gcf_base_universe_d2_011_gcf_015_dividend_cut_density_252'], 'func': gcf_base_universe_d3_011_gcf_015_dividend_cut_density_252}


def gcf_base_universe_d3_012_gcf_018_event_density_z_63(gcf_base_universe_d2_012_gcf_018_event_density_z_63):
    return _base_universe_d3(gcf_base_universe_d2_012_gcf_018_event_density_z_63, 12)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_012_gcf_018_event_density_z_63'] = {'inputs': ['gcf_base_universe_d2_012_gcf_018_event_density_z_63'], 'func': gcf_base_universe_d3_012_gcf_018_event_density_z_63}


def gcf_base_universe_d3_013_gcf_020_delisting_notice_density_126(gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126):
    return _base_universe_d3(gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126, 13)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_013_gcf_020_delisting_notice_density_126'] = {'inputs': ['gcf_base_universe_d2_013_gcf_020_delisting_notice_density_126'], 'func': gcf_base_universe_d3_013_gcf_020_delisting_notice_density_126}


def gcf_base_universe_d3_014_gcf_026_going_concern_persistence_1008(gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008):
    return _base_universe_d3(gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008, 14)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_014_gcf_026_going_concern_persistence_1008'] = {'inputs': ['gcf_base_universe_d2_014_gcf_026_going_concern_persistence_1008'], 'func': gcf_base_universe_d3_014_gcf_026_going_concern_persistence_1008}


def gcf_base_universe_d3_015_gcf_027_delisting_notice_density_1260(gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260):
    return _base_universe_d3(gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260, 15)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_015_gcf_027_delisting_notice_density_1260'] = {'inputs': ['gcf_base_universe_d2_015_gcf_027_delisting_notice_density_1260'], 'func': gcf_base_universe_d3_015_gcf_027_delisting_notice_density_1260}


def gcf_base_universe_d3_016_gcf_032_event_density_z_42(gcf_base_universe_d2_016_gcf_032_event_density_z_42):
    return _base_universe_d3(gcf_base_universe_d2_016_gcf_032_event_density_z_42, 16)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_016_gcf_032_event_density_z_42'] = {'inputs': ['gcf_base_universe_d2_016_gcf_032_event_density_z_42'], 'func': gcf_base_universe_d3_016_gcf_032_event_density_z_42}


def gcf_base_universe_d3_017_gcf_033_going_concern_persistence_63(gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63):
    return _base_universe_d3(gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63, 17)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_017_gcf_033_going_concern_persistence_63'] = {'inputs': ['gcf_base_universe_d2_017_gcf_033_going_concern_persistence_63'], 'func': gcf_base_universe_d3_017_gcf_033_going_concern_persistence_63}


def gcf_base_universe_d3_018_gcf_034_delisting_notice_density_84(gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84):
    return _base_universe_d3(gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84, 18)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_018_gcf_034_delisting_notice_density_84'] = {'inputs': ['gcf_base_universe_d2_018_gcf_034_delisting_notice_density_84'], 'func': gcf_base_universe_d3_018_gcf_034_delisting_notice_density_84}


def gcf_base_universe_d3_019_gcf_039_event_density_z_504(gcf_base_universe_d2_019_gcf_039_event_density_z_504):
    return _base_universe_d3(gcf_base_universe_d2_019_gcf_039_event_density_z_504, 19)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_019_gcf_039_event_density_z_504'] = {'inputs': ['gcf_base_universe_d2_019_gcf_039_event_density_z_504'], 'func': gcf_base_universe_d3_019_gcf_039_event_density_z_504}


def gcf_base_universe_d3_020_gcf_040_going_concern_persistence_756(gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756):
    return _base_universe_d3(gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756, 20)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_020_gcf_040_going_concern_persistence_756'] = {'inputs': ['gcf_base_universe_d2_020_gcf_040_going_concern_persistence_756'], 'func': gcf_base_universe_d3_020_gcf_040_going_concern_persistence_756}


def gcf_base_universe_d3_021_gcf_041_delisting_notice_density_1008(gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008):
    return _base_universe_d3(gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008, 21)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_021_gcf_041_delisting_notice_density_1008'] = {'inputs': ['gcf_base_universe_d2_021_gcf_041_delisting_notice_density_1008'], 'func': gcf_base_universe_d3_021_gcf_041_delisting_notice_density_1008}


def gcf_base_universe_d3_022_gcf_046_event_density_z_21(gcf_base_universe_d2_022_gcf_046_event_density_z_21):
    return _base_universe_d3(gcf_base_universe_d2_022_gcf_046_event_density_z_21, 22)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_022_gcf_046_event_density_z_21'] = {'inputs': ['gcf_base_universe_d2_022_gcf_046_event_density_z_21'], 'func': gcf_base_universe_d3_022_gcf_046_event_density_z_21}


def gcf_base_universe_d3_023_gcf_047_going_concern_persistence_42(gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42):
    return _base_universe_d3(gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42, 23)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_023_gcf_047_going_concern_persistence_42'] = {'inputs': ['gcf_base_universe_d2_023_gcf_047_going_concern_persistence_42'], 'func': gcf_base_universe_d3_023_gcf_047_going_concern_persistence_42}


def gcf_base_universe_d3_024_gcf_053_event_density_z_378(gcf_base_universe_d2_024_gcf_053_event_density_z_378):
    return _base_universe_d3(gcf_base_universe_d2_024_gcf_053_event_density_z_378, 24)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_024_gcf_053_event_density_z_378'] = {'inputs': ['gcf_base_universe_d2_024_gcf_053_event_density_z_378'], 'func': gcf_base_universe_d3_024_gcf_053_event_density_z_378}


def gcf_base_universe_d3_025_gcf_054_going_concern_persistence_504(gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504):
    return _base_universe_d3(gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504, 25)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_025_gcf_054_going_concern_persistence_504'] = {'inputs': ['gcf_base_universe_d2_025_gcf_054_going_concern_persistence_504'], 'func': gcf_base_universe_d3_025_gcf_054_going_concern_persistence_504}


def gcf_base_universe_d3_026_gcf_060_event_density_z_252(gcf_base_universe_d2_026_gcf_060_event_density_z_252):
    return _base_universe_d3(gcf_base_universe_d2_026_gcf_060_event_density_z_252, 26)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_026_gcf_060_event_density_z_252'] = {'inputs': ['gcf_base_universe_d2_026_gcf_060_event_density_z_252'], 'func': gcf_base_universe_d3_026_gcf_060_event_density_z_252}


def gcf_base_universe_d3_027_gcf_061_going_concern_persistence_21(gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21):
    return _base_universe_d3(gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21, 27)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_027_gcf_061_going_concern_persistence_21'] = {'inputs': ['gcf_base_universe_d2_027_gcf_061_going_concern_persistence_21'], 'func': gcf_base_universe_d3_027_gcf_061_going_concern_persistence_21}


def gcf_base_universe_d3_028_gcf_068_going_concern_persistence_378(gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378):
    return _base_universe_d3(gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378, 28)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_028_gcf_068_going_concern_persistence_378'] = {'inputs': ['gcf_base_universe_d2_028_gcf_068_going_concern_persistence_378'], 'func': gcf_base_universe_d3_028_gcf_068_going_concern_persistence_378}


def gcf_base_universe_d3_029_gcf_075_going_concern_persistence_252(gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252):
    return _base_universe_d3(gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252, 29)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_029_gcf_075_going_concern_persistence_252'] = {'inputs': ['gcf_base_universe_d2_029_gcf_075_going_concern_persistence_252'], 'func': gcf_base_universe_d3_029_gcf_075_going_concern_persistence_252}


def gcf_base_universe_d3_030_gcf_basefill_007(gcf_base_universe_d2_030_gcf_basefill_007):
    return _base_universe_d3(gcf_base_universe_d2_030_gcf_basefill_007, 30)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_030_gcf_basefill_007'] = {'inputs': ['gcf_base_universe_d2_030_gcf_basefill_007'], 'func': gcf_base_universe_d3_030_gcf_basefill_007}


def gcf_base_universe_d3_031_gcf_basefill_014(gcf_base_universe_d2_031_gcf_basefill_014):
    return _base_universe_d3(gcf_base_universe_d2_031_gcf_basefill_014, 31)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_031_gcf_basefill_014'] = {'inputs': ['gcf_base_universe_d2_031_gcf_basefill_014'], 'func': gcf_base_universe_d3_031_gcf_basefill_014}


def gcf_base_universe_d3_032_gcf_basefill_016(gcf_base_universe_d2_032_gcf_basefill_016):
    return _base_universe_d3(gcf_base_universe_d2_032_gcf_basefill_016, 32)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_032_gcf_basefill_016'] = {'inputs': ['gcf_base_universe_d2_032_gcf_basefill_016'], 'func': gcf_base_universe_d3_032_gcf_basefill_016}


def gcf_base_universe_d3_033_gcf_basefill_017(gcf_base_universe_d2_033_gcf_basefill_017):
    return _base_universe_d3(gcf_base_universe_d2_033_gcf_basefill_017, 33)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_033_gcf_basefill_017'] = {'inputs': ['gcf_base_universe_d2_033_gcf_basefill_017'], 'func': gcf_base_universe_d3_033_gcf_basefill_017}


def gcf_base_universe_d3_034_gcf_basefill_021(gcf_base_universe_d2_034_gcf_basefill_021):
    return _base_universe_d3(gcf_base_universe_d2_034_gcf_basefill_021, 34)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_034_gcf_basefill_021'] = {'inputs': ['gcf_base_universe_d2_034_gcf_basefill_021'], 'func': gcf_base_universe_d3_034_gcf_basefill_021}


def gcf_base_universe_d3_035_gcf_basefill_022(gcf_base_universe_d2_035_gcf_basefill_022):
    return _base_universe_d3(gcf_base_universe_d2_035_gcf_basefill_022, 35)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_035_gcf_basefill_022'] = {'inputs': ['gcf_base_universe_d2_035_gcf_basefill_022'], 'func': gcf_base_universe_d3_035_gcf_basefill_022}


def gcf_base_universe_d3_036_gcf_basefill_023(gcf_base_universe_d2_036_gcf_basefill_023):
    return _base_universe_d3(gcf_base_universe_d2_036_gcf_basefill_023, 36)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_036_gcf_basefill_023'] = {'inputs': ['gcf_base_universe_d2_036_gcf_basefill_023'], 'func': gcf_base_universe_d3_036_gcf_basefill_023}


def gcf_base_universe_d3_037_gcf_basefill_024(gcf_base_universe_d2_037_gcf_basefill_024):
    return _base_universe_d3(gcf_base_universe_d2_037_gcf_basefill_024, 37)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_037_gcf_basefill_024'] = {'inputs': ['gcf_base_universe_d2_037_gcf_basefill_024'], 'func': gcf_base_universe_d3_037_gcf_basefill_024}


def gcf_base_universe_d3_038_gcf_basefill_028(gcf_base_universe_d2_038_gcf_basefill_028):
    return _base_universe_d3(gcf_base_universe_d2_038_gcf_basefill_028, 38)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_038_gcf_basefill_028'] = {'inputs': ['gcf_base_universe_d2_038_gcf_basefill_028'], 'func': gcf_base_universe_d3_038_gcf_basefill_028}


def gcf_base_universe_d3_039_gcf_basefill_029(gcf_base_universe_d2_039_gcf_basefill_029):
    return _base_universe_d3(gcf_base_universe_d2_039_gcf_basefill_029, 39)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_039_gcf_basefill_029'] = {'inputs': ['gcf_base_universe_d2_039_gcf_basefill_029'], 'func': gcf_base_universe_d3_039_gcf_basefill_029}


def gcf_base_universe_d3_040_gcf_basefill_030(gcf_base_universe_d2_040_gcf_basefill_030):
    return _base_universe_d3(gcf_base_universe_d2_040_gcf_basefill_030, 40)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_040_gcf_basefill_030'] = {'inputs': ['gcf_base_universe_d2_040_gcf_basefill_030'], 'func': gcf_base_universe_d3_040_gcf_basefill_030}


def gcf_base_universe_d3_041_gcf_basefill_031(gcf_base_universe_d2_041_gcf_basefill_031):
    return _base_universe_d3(gcf_base_universe_d2_041_gcf_basefill_031, 41)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_041_gcf_basefill_031'] = {'inputs': ['gcf_base_universe_d2_041_gcf_basefill_031'], 'func': gcf_base_universe_d3_041_gcf_basefill_031}


def gcf_base_universe_d3_042_gcf_basefill_035(gcf_base_universe_d2_042_gcf_basefill_035):
    return _base_universe_d3(gcf_base_universe_d2_042_gcf_basefill_035, 42)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_042_gcf_basefill_035'] = {'inputs': ['gcf_base_universe_d2_042_gcf_basefill_035'], 'func': gcf_base_universe_d3_042_gcf_basefill_035}


def gcf_base_universe_d3_043_gcf_basefill_036(gcf_base_universe_d2_043_gcf_basefill_036):
    return _base_universe_d3(gcf_base_universe_d2_043_gcf_basefill_036, 43)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_043_gcf_basefill_036'] = {'inputs': ['gcf_base_universe_d2_043_gcf_basefill_036'], 'func': gcf_base_universe_d3_043_gcf_basefill_036}


def gcf_base_universe_d3_044_gcf_basefill_037(gcf_base_universe_d2_044_gcf_basefill_037):
    return _base_universe_d3(gcf_base_universe_d2_044_gcf_basefill_037, 44)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_044_gcf_basefill_037'] = {'inputs': ['gcf_base_universe_d2_044_gcf_basefill_037'], 'func': gcf_base_universe_d3_044_gcf_basefill_037}


def gcf_base_universe_d3_045_gcf_basefill_038(gcf_base_universe_d2_045_gcf_basefill_038):
    return _base_universe_d3(gcf_base_universe_d2_045_gcf_basefill_038, 45)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_045_gcf_basefill_038'] = {'inputs': ['gcf_base_universe_d2_045_gcf_basefill_038'], 'func': gcf_base_universe_d3_045_gcf_basefill_038}


def gcf_base_universe_d3_046_gcf_basefill_042(gcf_base_universe_d2_046_gcf_basefill_042):
    return _base_universe_d3(gcf_base_universe_d2_046_gcf_basefill_042, 46)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_046_gcf_basefill_042'] = {'inputs': ['gcf_base_universe_d2_046_gcf_basefill_042'], 'func': gcf_base_universe_d3_046_gcf_basefill_042}


def gcf_base_universe_d3_047_gcf_basefill_043(gcf_base_universe_d2_047_gcf_basefill_043):
    return _base_universe_d3(gcf_base_universe_d2_047_gcf_basefill_043, 47)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_047_gcf_basefill_043'] = {'inputs': ['gcf_base_universe_d2_047_gcf_basefill_043'], 'func': gcf_base_universe_d3_047_gcf_basefill_043}


def gcf_base_universe_d3_048_gcf_basefill_044(gcf_base_universe_d2_048_gcf_basefill_044):
    return _base_universe_d3(gcf_base_universe_d2_048_gcf_basefill_044, 48)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_048_gcf_basefill_044'] = {'inputs': ['gcf_base_universe_d2_048_gcf_basefill_044'], 'func': gcf_base_universe_d3_048_gcf_basefill_044}


def gcf_base_universe_d3_049_gcf_basefill_045(gcf_base_universe_d2_049_gcf_basefill_045):
    return _base_universe_d3(gcf_base_universe_d2_049_gcf_basefill_045, 49)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_049_gcf_basefill_045'] = {'inputs': ['gcf_base_universe_d2_049_gcf_basefill_045'], 'func': gcf_base_universe_d3_049_gcf_basefill_045}


def gcf_base_universe_d3_050_gcf_basefill_048(gcf_base_universe_d2_050_gcf_basefill_048):
    return _base_universe_d3(gcf_base_universe_d2_050_gcf_basefill_048, 50)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_050_gcf_basefill_048'] = {'inputs': ['gcf_base_universe_d2_050_gcf_basefill_048'], 'func': gcf_base_universe_d3_050_gcf_basefill_048}


def gcf_base_universe_d3_051_gcf_basefill_049(gcf_base_universe_d2_051_gcf_basefill_049):
    return _base_universe_d3(gcf_base_universe_d2_051_gcf_basefill_049, 51)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_051_gcf_basefill_049'] = {'inputs': ['gcf_base_universe_d2_051_gcf_basefill_049'], 'func': gcf_base_universe_d3_051_gcf_basefill_049}


def gcf_base_universe_d3_052_gcf_basefill_050(gcf_base_universe_d2_052_gcf_basefill_050):
    return _base_universe_d3(gcf_base_universe_d2_052_gcf_basefill_050, 52)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_052_gcf_basefill_050'] = {'inputs': ['gcf_base_universe_d2_052_gcf_basefill_050'], 'func': gcf_base_universe_d3_052_gcf_basefill_050}


def gcf_base_universe_d3_053_gcf_basefill_051(gcf_base_universe_d2_053_gcf_basefill_051):
    return _base_universe_d3(gcf_base_universe_d2_053_gcf_basefill_051, 53)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_053_gcf_basefill_051'] = {'inputs': ['gcf_base_universe_d2_053_gcf_basefill_051'], 'func': gcf_base_universe_d3_053_gcf_basefill_051}


def gcf_base_universe_d3_054_gcf_basefill_052(gcf_base_universe_d2_054_gcf_basefill_052):
    return _base_universe_d3(gcf_base_universe_d2_054_gcf_basefill_052, 54)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_054_gcf_basefill_052'] = {'inputs': ['gcf_base_universe_d2_054_gcf_basefill_052'], 'func': gcf_base_universe_d3_054_gcf_basefill_052}


def gcf_base_universe_d3_055_gcf_basefill_055(gcf_base_universe_d2_055_gcf_basefill_055):
    return _base_universe_d3(gcf_base_universe_d2_055_gcf_basefill_055, 55)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_055_gcf_basefill_055'] = {'inputs': ['gcf_base_universe_d2_055_gcf_basefill_055'], 'func': gcf_base_universe_d3_055_gcf_basefill_055}


def gcf_base_universe_d3_056_gcf_basefill_056(gcf_base_universe_d2_056_gcf_basefill_056):
    return _base_universe_d3(gcf_base_universe_d2_056_gcf_basefill_056, 56)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_056_gcf_basefill_056'] = {'inputs': ['gcf_base_universe_d2_056_gcf_basefill_056'], 'func': gcf_base_universe_d3_056_gcf_basefill_056}


def gcf_base_universe_d3_057_gcf_basefill_057(gcf_base_universe_d2_057_gcf_basefill_057):
    return _base_universe_d3(gcf_base_universe_d2_057_gcf_basefill_057, 57)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_057_gcf_basefill_057'] = {'inputs': ['gcf_base_universe_d2_057_gcf_basefill_057'], 'func': gcf_base_universe_d3_057_gcf_basefill_057}


def gcf_base_universe_d3_058_gcf_basefill_058(gcf_base_universe_d2_058_gcf_basefill_058):
    return _base_universe_d3(gcf_base_universe_d2_058_gcf_basefill_058, 58)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_058_gcf_basefill_058'] = {'inputs': ['gcf_base_universe_d2_058_gcf_basefill_058'], 'func': gcf_base_universe_d3_058_gcf_basefill_058}


def gcf_base_universe_d3_059_gcf_basefill_059(gcf_base_universe_d2_059_gcf_basefill_059):
    return _base_universe_d3(gcf_base_universe_d2_059_gcf_basefill_059, 59)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_059_gcf_basefill_059'] = {'inputs': ['gcf_base_universe_d2_059_gcf_basefill_059'], 'func': gcf_base_universe_d3_059_gcf_basefill_059}


def gcf_base_universe_d3_060_gcf_basefill_062(gcf_base_universe_d2_060_gcf_basefill_062):
    return _base_universe_d3(gcf_base_universe_d2_060_gcf_basefill_062, 60)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_060_gcf_basefill_062'] = {'inputs': ['gcf_base_universe_d2_060_gcf_basefill_062'], 'func': gcf_base_universe_d3_060_gcf_basefill_062}


def gcf_base_universe_d3_061_gcf_basefill_063(gcf_base_universe_d2_061_gcf_basefill_063):
    return _base_universe_d3(gcf_base_universe_d2_061_gcf_basefill_063, 61)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_061_gcf_basefill_063'] = {'inputs': ['gcf_base_universe_d2_061_gcf_basefill_063'], 'func': gcf_base_universe_d3_061_gcf_basefill_063}


def gcf_base_universe_d3_062_gcf_basefill_064(gcf_base_universe_d2_062_gcf_basefill_064):
    return _base_universe_d3(gcf_base_universe_d2_062_gcf_basefill_064, 62)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_062_gcf_basefill_064'] = {'inputs': ['gcf_base_universe_d2_062_gcf_basefill_064'], 'func': gcf_base_universe_d3_062_gcf_basefill_064}


def gcf_base_universe_d3_063_gcf_basefill_065(gcf_base_universe_d2_063_gcf_basefill_065):
    return _base_universe_d3(gcf_base_universe_d2_063_gcf_basefill_065, 63)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_063_gcf_basefill_065'] = {'inputs': ['gcf_base_universe_d2_063_gcf_basefill_065'], 'func': gcf_base_universe_d3_063_gcf_basefill_065}


def gcf_base_universe_d3_064_gcf_basefill_066(gcf_base_universe_d2_064_gcf_basefill_066):
    return _base_universe_d3(gcf_base_universe_d2_064_gcf_basefill_066, 64)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_064_gcf_basefill_066'] = {'inputs': ['gcf_base_universe_d2_064_gcf_basefill_066'], 'func': gcf_base_universe_d3_064_gcf_basefill_066}


def gcf_base_universe_d3_065_gcf_basefill_067(gcf_base_universe_d2_065_gcf_basefill_067):
    return _base_universe_d3(gcf_base_universe_d2_065_gcf_basefill_067, 65)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_065_gcf_basefill_067'] = {'inputs': ['gcf_base_universe_d2_065_gcf_basefill_067'], 'func': gcf_base_universe_d3_065_gcf_basefill_067}


def gcf_base_universe_d3_066_gcf_basefill_069(gcf_base_universe_d2_066_gcf_basefill_069):
    return _base_universe_d3(gcf_base_universe_d2_066_gcf_basefill_069, 66)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_066_gcf_basefill_069'] = {'inputs': ['gcf_base_universe_d2_066_gcf_basefill_069'], 'func': gcf_base_universe_d3_066_gcf_basefill_069}


def gcf_base_universe_d3_067_gcf_basefill_070(gcf_base_universe_d2_067_gcf_basefill_070):
    return _base_universe_d3(gcf_base_universe_d2_067_gcf_basefill_070, 67)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_067_gcf_basefill_070'] = {'inputs': ['gcf_base_universe_d2_067_gcf_basefill_070'], 'func': gcf_base_universe_d3_067_gcf_basefill_070}


def gcf_base_universe_d3_068_gcf_basefill_071(gcf_base_universe_d2_068_gcf_basefill_071):
    return _base_universe_d3(gcf_base_universe_d2_068_gcf_basefill_071, 68)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_068_gcf_basefill_071'] = {'inputs': ['gcf_base_universe_d2_068_gcf_basefill_071'], 'func': gcf_base_universe_d3_068_gcf_basefill_071}


def gcf_base_universe_d3_069_gcf_basefill_072(gcf_base_universe_d2_069_gcf_basefill_072):
    return _base_universe_d3(gcf_base_universe_d2_069_gcf_basefill_072, 69)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_069_gcf_basefill_072'] = {'inputs': ['gcf_base_universe_d2_069_gcf_basefill_072'], 'func': gcf_base_universe_d3_069_gcf_basefill_072}


def gcf_base_universe_d3_070_gcf_basefill_073(gcf_base_universe_d2_070_gcf_basefill_073):
    return _base_universe_d3(gcf_base_universe_d2_070_gcf_basefill_073, 70)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_070_gcf_basefill_073'] = {'inputs': ['gcf_base_universe_d2_070_gcf_basefill_073'], 'func': gcf_base_universe_d3_070_gcf_basefill_073}


def gcf_base_universe_d3_071_gcf_basefill_074(gcf_base_universe_d2_071_gcf_basefill_074):
    return _base_universe_d3(gcf_base_universe_d2_071_gcf_basefill_074, 71)
GCF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gcf_base_universe_d3_071_gcf_basefill_074'] = {'inputs': ['gcf_base_universe_d2_071_gcf_basefill_074'], 'func': gcf_base_universe_d3_071_gcf_basefill_074}
