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



def ced_176_ced_001_dividend_cut_density_21_accel_1(ced_151_ced_001_dividend_cut_density_21_roc_1):
    feature = _s(ced_151_ced_001_dividend_cut_density_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ced_177_ced_007_listing_tier_decay_1_accel_42(ced_152_ced_007_listing_tier_decay_1_roc_42):
    feature = _s(ced_152_ced_007_listing_tier_decay_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ced_178_ced_013_delisting_notice_density_1512_accel_126(ced_153_ced_013_delisting_notice_density_1512_roc_126):
    feature = _s(ced_153_ced_013_delisting_notice_density_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ced_179_ced_019_going_concern_persistence_84_accel_378(ced_154_ced_019_going_concern_persistence_84_roc_378):
    feature = _s(ced_154_ced_019_going_concern_persistence_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ced_180_ced_025_event_density_z_756_accel_4(ced_155_ced_025_event_density_z_756_roc_4):
    feature = _s(ced_155_ced_025_event_density_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















CORPORATE_EVENT_DENSITY_REGISTRY_3RD_DERIVATIVES = {
    'ced_176_ced_001_dividend_cut_density_21_accel_1': {'inputs': ['ced_151_ced_001_dividend_cut_density_21_roc_1'], 'func': ced_176_ced_001_dividend_cut_density_21_accel_1},
    'ced_177_ced_007_listing_tier_decay_1_accel_42': {'inputs': ['ced_152_ced_007_listing_tier_decay_1_roc_42'], 'func': ced_177_ced_007_listing_tier_decay_1_accel_42},
    'ced_178_ced_013_delisting_notice_density_1512_accel_126': {'inputs': ['ced_153_ced_013_delisting_notice_density_1512_roc_126'], 'func': ced_178_ced_013_delisting_notice_density_1512_accel_126},
    'ced_179_ced_019_going_concern_persistence_84_accel_378': {'inputs': ['ced_154_ced_019_going_concern_persistence_84_roc_378'], 'func': ced_179_ced_019_going_concern_persistence_84_accel_378},
    'ced_180_ced_025_event_density_z_756_accel_4': {'inputs': ['ced_155_ced_025_event_density_z_756_roc_4'], 'func': ced_180_ced_025_event_density_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ced_replacement_d3_001(ced_replacement_d2_001):
    feature = _clean(ced_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_001'] = {'inputs': ['ced_replacement_d2_001'], 'func': ced_replacement_d3_001}


def ced_replacement_d3_002(ced_replacement_d2_002):
    feature = _clean(ced_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_002'] = {'inputs': ['ced_replacement_d2_002'], 'func': ced_replacement_d3_002}


def ced_replacement_d3_003(ced_replacement_d2_003):
    feature = _clean(ced_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_003'] = {'inputs': ['ced_replacement_d2_003'], 'func': ced_replacement_d3_003}


def ced_replacement_d3_004(ced_replacement_d2_004):
    feature = _clean(ced_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_004'] = {'inputs': ['ced_replacement_d2_004'], 'func': ced_replacement_d3_004}


def ced_replacement_d3_005(ced_replacement_d2_005):
    feature = _clean(ced_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_005'] = {'inputs': ['ced_replacement_d2_005'], 'func': ced_replacement_d3_005}


def ced_replacement_d3_006(ced_replacement_d2_006):
    feature = _clean(ced_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_006'] = {'inputs': ['ced_replacement_d2_006'], 'func': ced_replacement_d3_006}


def ced_replacement_d3_007(ced_replacement_d2_007):
    feature = _clean(ced_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_007'] = {'inputs': ['ced_replacement_d2_007'], 'func': ced_replacement_d3_007}


def ced_replacement_d3_008(ced_replacement_d2_008):
    feature = _clean(ced_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_008'] = {'inputs': ['ced_replacement_d2_008'], 'func': ced_replacement_d3_008}


def ced_replacement_d3_009(ced_replacement_d2_009):
    feature = _clean(ced_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_009'] = {'inputs': ['ced_replacement_d2_009'], 'func': ced_replacement_d3_009}


def ced_replacement_d3_010(ced_replacement_d2_010):
    feature = _clean(ced_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_010'] = {'inputs': ['ced_replacement_d2_010'], 'func': ced_replacement_d3_010}


def ced_replacement_d3_011(ced_replacement_d2_011):
    feature = _clean(ced_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_011'] = {'inputs': ['ced_replacement_d2_011'], 'func': ced_replacement_d3_011}


def ced_replacement_d3_012(ced_replacement_d2_012):
    feature = _clean(ced_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_012'] = {'inputs': ['ced_replacement_d2_012'], 'func': ced_replacement_d3_012}


def ced_replacement_d3_013(ced_replacement_d2_013):
    feature = _clean(ced_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_013'] = {'inputs': ['ced_replacement_d2_013'], 'func': ced_replacement_d3_013}


def ced_replacement_d3_014(ced_replacement_d2_014):
    feature = _clean(ced_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_014'] = {'inputs': ['ced_replacement_d2_014'], 'func': ced_replacement_d3_014}


def ced_replacement_d3_015(ced_replacement_d2_015):
    feature = _clean(ced_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_015'] = {'inputs': ['ced_replacement_d2_015'], 'func': ced_replacement_d3_015}


def ced_replacement_d3_016(ced_replacement_d2_016):
    feature = _clean(ced_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_016'] = {'inputs': ['ced_replacement_d2_016'], 'func': ced_replacement_d3_016}


def ced_replacement_d3_017(ced_replacement_d2_017):
    feature = _clean(ced_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_017'] = {'inputs': ['ced_replacement_d2_017'], 'func': ced_replacement_d3_017}


def ced_replacement_d3_018(ced_replacement_d2_018):
    feature = _clean(ced_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_018'] = {'inputs': ['ced_replacement_d2_018'], 'func': ced_replacement_d3_018}


def ced_replacement_d3_019(ced_replacement_d2_019):
    feature = _clean(ced_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_019'] = {'inputs': ['ced_replacement_d2_019'], 'func': ced_replacement_d3_019}


def ced_replacement_d3_020(ced_replacement_d2_020):
    feature = _clean(ced_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_020'] = {'inputs': ['ced_replacement_d2_020'], 'func': ced_replacement_d3_020}


def ced_replacement_d3_021(ced_replacement_d2_021):
    feature = _clean(ced_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_021'] = {'inputs': ['ced_replacement_d2_021'], 'func': ced_replacement_d3_021}


def ced_replacement_d3_022(ced_replacement_d2_022):
    feature = _clean(ced_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_022'] = {'inputs': ['ced_replacement_d2_022'], 'func': ced_replacement_d3_022}


def ced_replacement_d3_023(ced_replacement_d2_023):
    feature = _clean(ced_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_023'] = {'inputs': ['ced_replacement_d2_023'], 'func': ced_replacement_d3_023}


def ced_replacement_d3_024(ced_replacement_d2_024):
    feature = _clean(ced_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_024'] = {'inputs': ['ced_replacement_d2_024'], 'func': ced_replacement_d3_024}


def ced_replacement_d3_025(ced_replacement_d2_025):
    feature = _clean(ced_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_025'] = {'inputs': ['ced_replacement_d2_025'], 'func': ced_replacement_d3_025}


def ced_replacement_d3_026(ced_replacement_d2_026):
    feature = _clean(ced_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_026'] = {'inputs': ['ced_replacement_d2_026'], 'func': ced_replacement_d3_026}


def ced_replacement_d3_027(ced_replacement_d2_027):
    feature = _clean(ced_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_027'] = {'inputs': ['ced_replacement_d2_027'], 'func': ced_replacement_d3_027}


def ced_replacement_d3_028(ced_replacement_d2_028):
    feature = _clean(ced_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_028'] = {'inputs': ['ced_replacement_d2_028'], 'func': ced_replacement_d3_028}


def ced_replacement_d3_029(ced_replacement_d2_029):
    feature = _clean(ced_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_029'] = {'inputs': ['ced_replacement_d2_029'], 'func': ced_replacement_d3_029}


def ced_replacement_d3_030(ced_replacement_d2_030):
    feature = _clean(ced_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_030'] = {'inputs': ['ced_replacement_d2_030'], 'func': ced_replacement_d3_030}


def ced_replacement_d3_031(ced_replacement_d2_031):
    feature = _clean(ced_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_031'] = {'inputs': ['ced_replacement_d2_031'], 'func': ced_replacement_d3_031}


def ced_replacement_d3_032(ced_replacement_d2_032):
    feature = _clean(ced_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_032'] = {'inputs': ['ced_replacement_d2_032'], 'func': ced_replacement_d3_032}


def ced_replacement_d3_033(ced_replacement_d2_033):
    feature = _clean(ced_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_033'] = {'inputs': ['ced_replacement_d2_033'], 'func': ced_replacement_d3_033}


def ced_replacement_d3_034(ced_replacement_d2_034):
    feature = _clean(ced_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_034'] = {'inputs': ['ced_replacement_d2_034'], 'func': ced_replacement_d3_034}


def ced_replacement_d3_035(ced_replacement_d2_035):
    feature = _clean(ced_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_035'] = {'inputs': ['ced_replacement_d2_035'], 'func': ced_replacement_d3_035}


def ced_replacement_d3_036(ced_replacement_d2_036):
    feature = _clean(ced_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_036'] = {'inputs': ['ced_replacement_d2_036'], 'func': ced_replacement_d3_036}


def ced_replacement_d3_037(ced_replacement_d2_037):
    feature = _clean(ced_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_037'] = {'inputs': ['ced_replacement_d2_037'], 'func': ced_replacement_d3_037}


def ced_replacement_d3_038(ced_replacement_d2_038):
    feature = _clean(ced_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_038'] = {'inputs': ['ced_replacement_d2_038'], 'func': ced_replacement_d3_038}


def ced_replacement_d3_039(ced_replacement_d2_039):
    feature = _clean(ced_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_039'] = {'inputs': ['ced_replacement_d2_039'], 'func': ced_replacement_d3_039}


def ced_replacement_d3_040(ced_replacement_d2_040):
    feature = _clean(ced_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_040'] = {'inputs': ['ced_replacement_d2_040'], 'func': ced_replacement_d3_040}


def ced_replacement_d3_041(ced_replacement_d2_041):
    feature = _clean(ced_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_041'] = {'inputs': ['ced_replacement_d2_041'], 'func': ced_replacement_d3_041}


def ced_replacement_d3_042(ced_replacement_d2_042):
    feature = _clean(ced_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_042'] = {'inputs': ['ced_replacement_d2_042'], 'func': ced_replacement_d3_042}


def ced_replacement_d3_043(ced_replacement_d2_043):
    feature = _clean(ced_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_043'] = {'inputs': ['ced_replacement_d2_043'], 'func': ced_replacement_d3_043}


def ced_replacement_d3_044(ced_replacement_d2_044):
    feature = _clean(ced_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_044'] = {'inputs': ['ced_replacement_d2_044'], 'func': ced_replacement_d3_044}


def ced_replacement_d3_045(ced_replacement_d2_045):
    feature = _clean(ced_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_045'] = {'inputs': ['ced_replacement_d2_045'], 'func': ced_replacement_d3_045}


def ced_replacement_d3_046(ced_replacement_d2_046):
    feature = _clean(ced_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_046'] = {'inputs': ['ced_replacement_d2_046'], 'func': ced_replacement_d3_046}


def ced_replacement_d3_047(ced_replacement_d2_047):
    feature = _clean(ced_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_047'] = {'inputs': ['ced_replacement_d2_047'], 'func': ced_replacement_d3_047}


def ced_replacement_d3_048(ced_replacement_d2_048):
    feature = _clean(ced_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_048'] = {'inputs': ['ced_replacement_d2_048'], 'func': ced_replacement_d3_048}


def ced_replacement_d3_049(ced_replacement_d2_049):
    feature = _clean(ced_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_049'] = {'inputs': ['ced_replacement_d2_049'], 'func': ced_replacement_d3_049}


def ced_replacement_d3_050(ced_replacement_d2_050):
    feature = _clean(ced_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_050'] = {'inputs': ['ced_replacement_d2_050'], 'func': ced_replacement_d3_050}


def ced_replacement_d3_051(ced_replacement_d2_051):
    feature = _clean(ced_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_051'] = {'inputs': ['ced_replacement_d2_051'], 'func': ced_replacement_d3_051}


def ced_replacement_d3_052(ced_replacement_d2_052):
    feature = _clean(ced_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_052'] = {'inputs': ['ced_replacement_d2_052'], 'func': ced_replacement_d3_052}


def ced_replacement_d3_053(ced_replacement_d2_053):
    feature = _clean(ced_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_053'] = {'inputs': ['ced_replacement_d2_053'], 'func': ced_replacement_d3_053}


def ced_replacement_d3_054(ced_replacement_d2_054):
    feature = _clean(ced_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_054'] = {'inputs': ['ced_replacement_d2_054'], 'func': ced_replacement_d3_054}


def ced_replacement_d3_055(ced_replacement_d2_055):
    feature = _clean(ced_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_055'] = {'inputs': ['ced_replacement_d2_055'], 'func': ced_replacement_d3_055}


def ced_replacement_d3_056(ced_replacement_d2_056):
    feature = _clean(ced_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_056'] = {'inputs': ['ced_replacement_d2_056'], 'func': ced_replacement_d3_056}


def ced_replacement_d3_057(ced_replacement_d2_057):
    feature = _clean(ced_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_057'] = {'inputs': ['ced_replacement_d2_057'], 'func': ced_replacement_d3_057}


def ced_replacement_d3_058(ced_replacement_d2_058):
    feature = _clean(ced_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_058'] = {'inputs': ['ced_replacement_d2_058'], 'func': ced_replacement_d3_058}


def ced_replacement_d3_059(ced_replacement_d2_059):
    feature = _clean(ced_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_059'] = {'inputs': ['ced_replacement_d2_059'], 'func': ced_replacement_d3_059}


def ced_replacement_d3_060(ced_replacement_d2_060):
    feature = _clean(ced_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_060'] = {'inputs': ['ced_replacement_d2_060'], 'func': ced_replacement_d3_060}


def ced_replacement_d3_061(ced_replacement_d2_061):
    feature = _clean(ced_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_061'] = {'inputs': ['ced_replacement_d2_061'], 'func': ced_replacement_d3_061}


def ced_replacement_d3_062(ced_replacement_d2_062):
    feature = _clean(ced_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_062'] = {'inputs': ['ced_replacement_d2_062'], 'func': ced_replacement_d3_062}


def ced_replacement_d3_063(ced_replacement_d2_063):
    feature = _clean(ced_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_063'] = {'inputs': ['ced_replacement_d2_063'], 'func': ced_replacement_d3_063}


def ced_replacement_d3_064(ced_replacement_d2_064):
    feature = _clean(ced_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_064'] = {'inputs': ['ced_replacement_d2_064'], 'func': ced_replacement_d3_064}


def ced_replacement_d3_065(ced_replacement_d2_065):
    feature = _clean(ced_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_065'] = {'inputs': ['ced_replacement_d2_065'], 'func': ced_replacement_d3_065}


def ced_replacement_d3_066(ced_replacement_d2_066):
    feature = _clean(ced_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_066'] = {'inputs': ['ced_replacement_d2_066'], 'func': ced_replacement_d3_066}


def ced_replacement_d3_067(ced_replacement_d2_067):
    feature = _clean(ced_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_067'] = {'inputs': ['ced_replacement_d2_067'], 'func': ced_replacement_d3_067}


def ced_replacement_d3_068(ced_replacement_d2_068):
    feature = _clean(ced_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_068'] = {'inputs': ['ced_replacement_d2_068'], 'func': ced_replacement_d3_068}


def ced_replacement_d3_069(ced_replacement_d2_069):
    feature = _clean(ced_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_069'] = {'inputs': ['ced_replacement_d2_069'], 'func': ced_replacement_d3_069}


def ced_replacement_d3_070(ced_replacement_d2_070):
    feature = _clean(ced_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_070'] = {'inputs': ['ced_replacement_d2_070'], 'func': ced_replacement_d3_070}


def ced_replacement_d3_071(ced_replacement_d2_071):
    feature = _clean(ced_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_071'] = {'inputs': ['ced_replacement_d2_071'], 'func': ced_replacement_d3_071}


def ced_replacement_d3_072(ced_replacement_d2_072):
    feature = _clean(ced_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_072'] = {'inputs': ['ced_replacement_d2_072'], 'func': ced_replacement_d3_072}


def ced_replacement_d3_073(ced_replacement_d2_073):
    feature = _clean(ced_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_073'] = {'inputs': ['ced_replacement_d2_073'], 'func': ced_replacement_d3_073}


def ced_replacement_d3_074(ced_replacement_d2_074):
    feature = _clean(ced_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_074'] = {'inputs': ['ced_replacement_d2_074'], 'func': ced_replacement_d3_074}


def ced_replacement_d3_075(ced_replacement_d2_075):
    feature = _clean(ced_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_075'] = {'inputs': ['ced_replacement_d2_075'], 'func': ced_replacement_d3_075}


def ced_replacement_d3_076(ced_replacement_d2_076):
    feature = _clean(ced_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_076'] = {'inputs': ['ced_replacement_d2_076'], 'func': ced_replacement_d3_076}


def ced_replacement_d3_077(ced_replacement_d2_077):
    feature = _clean(ced_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_077'] = {'inputs': ['ced_replacement_d2_077'], 'func': ced_replacement_d3_077}


def ced_replacement_d3_078(ced_replacement_d2_078):
    feature = _clean(ced_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_078'] = {'inputs': ['ced_replacement_d2_078'], 'func': ced_replacement_d3_078}


def ced_replacement_d3_079(ced_replacement_d2_079):
    feature = _clean(ced_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_079'] = {'inputs': ['ced_replacement_d2_079'], 'func': ced_replacement_d3_079}


def ced_replacement_d3_080(ced_replacement_d2_080):
    feature = _clean(ced_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_080'] = {'inputs': ['ced_replacement_d2_080'], 'func': ced_replacement_d3_080}


def ced_replacement_d3_081(ced_replacement_d2_081):
    feature = _clean(ced_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_081'] = {'inputs': ['ced_replacement_d2_081'], 'func': ced_replacement_d3_081}


def ced_replacement_d3_082(ced_replacement_d2_082):
    feature = _clean(ced_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_082'] = {'inputs': ['ced_replacement_d2_082'], 'func': ced_replacement_d3_082}


def ced_replacement_d3_083(ced_replacement_d2_083):
    feature = _clean(ced_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_083'] = {'inputs': ['ced_replacement_d2_083'], 'func': ced_replacement_d3_083}


def ced_replacement_d3_084(ced_replacement_d2_084):
    feature = _clean(ced_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_084'] = {'inputs': ['ced_replacement_d2_084'], 'func': ced_replacement_d3_084}


def ced_replacement_d3_085(ced_replacement_d2_085):
    feature = _clean(ced_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_085'] = {'inputs': ['ced_replacement_d2_085'], 'func': ced_replacement_d3_085}


def ced_replacement_d3_086(ced_replacement_d2_086):
    feature = _clean(ced_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_086'] = {'inputs': ['ced_replacement_d2_086'], 'func': ced_replacement_d3_086}


def ced_replacement_d3_087(ced_replacement_d2_087):
    feature = _clean(ced_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_087'] = {'inputs': ['ced_replacement_d2_087'], 'func': ced_replacement_d3_087}


def ced_replacement_d3_088(ced_replacement_d2_088):
    feature = _clean(ced_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_088'] = {'inputs': ['ced_replacement_d2_088'], 'func': ced_replacement_d3_088}


def ced_replacement_d3_089(ced_replacement_d2_089):
    feature = _clean(ced_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_089'] = {'inputs': ['ced_replacement_d2_089'], 'func': ced_replacement_d3_089}


def ced_replacement_d3_090(ced_replacement_d2_090):
    feature = _clean(ced_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_090'] = {'inputs': ['ced_replacement_d2_090'], 'func': ced_replacement_d3_090}


def ced_replacement_d3_091(ced_replacement_d2_091):
    feature = _clean(ced_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_091'] = {'inputs': ['ced_replacement_d2_091'], 'func': ced_replacement_d3_091}


def ced_replacement_d3_092(ced_replacement_d2_092):
    feature = _clean(ced_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_092'] = {'inputs': ['ced_replacement_d2_092'], 'func': ced_replacement_d3_092}


def ced_replacement_d3_093(ced_replacement_d2_093):
    feature = _clean(ced_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_093'] = {'inputs': ['ced_replacement_d2_093'], 'func': ced_replacement_d3_093}


def ced_replacement_d3_094(ced_replacement_d2_094):
    feature = _clean(ced_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_094'] = {'inputs': ['ced_replacement_d2_094'], 'func': ced_replacement_d3_094}


def ced_replacement_d3_095(ced_replacement_d2_095):
    feature = _clean(ced_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_095'] = {'inputs': ['ced_replacement_d2_095'], 'func': ced_replacement_d3_095}


def ced_replacement_d3_096(ced_replacement_d2_096):
    feature = _clean(ced_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_096'] = {'inputs': ['ced_replacement_d2_096'], 'func': ced_replacement_d3_096}


def ced_replacement_d3_097(ced_replacement_d2_097):
    feature = _clean(ced_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_097'] = {'inputs': ['ced_replacement_d2_097'], 'func': ced_replacement_d3_097}


def ced_replacement_d3_098(ced_replacement_d2_098):
    feature = _clean(ced_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_098'] = {'inputs': ['ced_replacement_d2_098'], 'func': ced_replacement_d3_098}


def ced_replacement_d3_099(ced_replacement_d2_099):
    feature = _clean(ced_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_099'] = {'inputs': ['ced_replacement_d2_099'], 'func': ced_replacement_d3_099}


def ced_replacement_d3_100(ced_replacement_d2_100):
    feature = _clean(ced_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_100'] = {'inputs': ['ced_replacement_d2_100'], 'func': ced_replacement_d3_100}


def ced_replacement_d3_101(ced_replacement_d2_101):
    feature = _clean(ced_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_101'] = {'inputs': ['ced_replacement_d2_101'], 'func': ced_replacement_d3_101}


def ced_replacement_d3_102(ced_replacement_d2_102):
    feature = _clean(ced_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_102'] = {'inputs': ['ced_replacement_d2_102'], 'func': ced_replacement_d3_102}


def ced_replacement_d3_103(ced_replacement_d2_103):
    feature = _clean(ced_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_103'] = {'inputs': ['ced_replacement_d2_103'], 'func': ced_replacement_d3_103}


def ced_replacement_d3_104(ced_replacement_d2_104):
    feature = _clean(ced_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_104'] = {'inputs': ['ced_replacement_d2_104'], 'func': ced_replacement_d3_104}


def ced_replacement_d3_105(ced_replacement_d2_105):
    feature = _clean(ced_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_105'] = {'inputs': ['ced_replacement_d2_105'], 'func': ced_replacement_d3_105}


def ced_replacement_d3_106(ced_replacement_d2_106):
    feature = _clean(ced_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_106'] = {'inputs': ['ced_replacement_d2_106'], 'func': ced_replacement_d3_106}


def ced_replacement_d3_107(ced_replacement_d2_107):
    feature = _clean(ced_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_107'] = {'inputs': ['ced_replacement_d2_107'], 'func': ced_replacement_d3_107}


def ced_replacement_d3_108(ced_replacement_d2_108):
    feature = _clean(ced_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_108'] = {'inputs': ['ced_replacement_d2_108'], 'func': ced_replacement_d3_108}


def ced_replacement_d3_109(ced_replacement_d2_109):
    feature = _clean(ced_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_109'] = {'inputs': ['ced_replacement_d2_109'], 'func': ced_replacement_d3_109}


def ced_replacement_d3_110(ced_replacement_d2_110):
    feature = _clean(ced_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_110'] = {'inputs': ['ced_replacement_d2_110'], 'func': ced_replacement_d3_110}


def ced_replacement_d3_111(ced_replacement_d2_111):
    feature = _clean(ced_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_111'] = {'inputs': ['ced_replacement_d2_111'], 'func': ced_replacement_d3_111}


def ced_replacement_d3_112(ced_replacement_d2_112):
    feature = _clean(ced_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_112'] = {'inputs': ['ced_replacement_d2_112'], 'func': ced_replacement_d3_112}


def ced_replacement_d3_113(ced_replacement_d2_113):
    feature = _clean(ced_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_113'] = {'inputs': ['ced_replacement_d2_113'], 'func': ced_replacement_d3_113}


def ced_replacement_d3_114(ced_replacement_d2_114):
    feature = _clean(ced_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_114'] = {'inputs': ['ced_replacement_d2_114'], 'func': ced_replacement_d3_114}


def ced_replacement_d3_115(ced_replacement_d2_115):
    feature = _clean(ced_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_115'] = {'inputs': ['ced_replacement_d2_115'], 'func': ced_replacement_d3_115}


def ced_replacement_d3_116(ced_replacement_d2_116):
    feature = _clean(ced_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_116'] = {'inputs': ['ced_replacement_d2_116'], 'func': ced_replacement_d3_116}


def ced_replacement_d3_117(ced_replacement_d2_117):
    feature = _clean(ced_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_117'] = {'inputs': ['ced_replacement_d2_117'], 'func': ced_replacement_d3_117}


def ced_replacement_d3_118(ced_replacement_d2_118):
    feature = _clean(ced_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_118'] = {'inputs': ['ced_replacement_d2_118'], 'func': ced_replacement_d3_118}


def ced_replacement_d3_119(ced_replacement_d2_119):
    feature = _clean(ced_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_119'] = {'inputs': ['ced_replacement_d2_119'], 'func': ced_replacement_d3_119}


def ced_replacement_d3_120(ced_replacement_d2_120):
    feature = _clean(ced_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_120'] = {'inputs': ['ced_replacement_d2_120'], 'func': ced_replacement_d3_120}


def ced_replacement_d3_121(ced_replacement_d2_121):
    feature = _clean(ced_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_121'] = {'inputs': ['ced_replacement_d2_121'], 'func': ced_replacement_d3_121}


def ced_replacement_d3_122(ced_replacement_d2_122):
    feature = _clean(ced_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_122'] = {'inputs': ['ced_replacement_d2_122'], 'func': ced_replacement_d3_122}


def ced_replacement_d3_123(ced_replacement_d2_123):
    feature = _clean(ced_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_123'] = {'inputs': ['ced_replacement_d2_123'], 'func': ced_replacement_d3_123}


def ced_replacement_d3_124(ced_replacement_d2_124):
    feature = _clean(ced_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_124'] = {'inputs': ['ced_replacement_d2_124'], 'func': ced_replacement_d3_124}


def ced_replacement_d3_125(ced_replacement_d2_125):
    feature = _clean(ced_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_125'] = {'inputs': ['ced_replacement_d2_125'], 'func': ced_replacement_d3_125}


def ced_replacement_d3_126(ced_replacement_d2_126):
    feature = _clean(ced_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_126'] = {'inputs': ['ced_replacement_d2_126'], 'func': ced_replacement_d3_126}


def ced_replacement_d3_127(ced_replacement_d2_127):
    feature = _clean(ced_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_127'] = {'inputs': ['ced_replacement_d2_127'], 'func': ced_replacement_d3_127}


def ced_replacement_d3_128(ced_replacement_d2_128):
    feature = _clean(ced_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_128'] = {'inputs': ['ced_replacement_d2_128'], 'func': ced_replacement_d3_128}


def ced_replacement_d3_129(ced_replacement_d2_129):
    feature = _clean(ced_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_129'] = {'inputs': ['ced_replacement_d2_129'], 'func': ced_replacement_d3_129}


def ced_replacement_d3_130(ced_replacement_d2_130):
    feature = _clean(ced_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_130'] = {'inputs': ['ced_replacement_d2_130'], 'func': ced_replacement_d3_130}


def ced_replacement_d3_131(ced_replacement_d2_131):
    feature = _clean(ced_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_131'] = {'inputs': ['ced_replacement_d2_131'], 'func': ced_replacement_d3_131}


def ced_replacement_d3_132(ced_replacement_d2_132):
    feature = _clean(ced_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_132'] = {'inputs': ['ced_replacement_d2_132'], 'func': ced_replacement_d3_132}


def ced_replacement_d3_133(ced_replacement_d2_133):
    feature = _clean(ced_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_133'] = {'inputs': ['ced_replacement_d2_133'], 'func': ced_replacement_d3_133}


def ced_replacement_d3_134(ced_replacement_d2_134):
    feature = _clean(ced_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_134'] = {'inputs': ['ced_replacement_d2_134'], 'func': ced_replacement_d3_134}


def ced_replacement_d3_135(ced_replacement_d2_135):
    feature = _clean(ced_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_135'] = {'inputs': ['ced_replacement_d2_135'], 'func': ced_replacement_d3_135}


def ced_replacement_d3_136(ced_replacement_d2_136):
    feature = _clean(ced_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_136'] = {'inputs': ['ced_replacement_d2_136'], 'func': ced_replacement_d3_136}


def ced_replacement_d3_137(ced_replacement_d2_137):
    feature = _clean(ced_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_137'] = {'inputs': ['ced_replacement_d2_137'], 'func': ced_replacement_d3_137}


def ced_replacement_d3_138(ced_replacement_d2_138):
    feature = _clean(ced_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_138'] = {'inputs': ['ced_replacement_d2_138'], 'func': ced_replacement_d3_138}


def ced_replacement_d3_139(ced_replacement_d2_139):
    feature = _clean(ced_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_139'] = {'inputs': ['ced_replacement_d2_139'], 'func': ced_replacement_d3_139}


def ced_replacement_d3_140(ced_replacement_d2_140):
    feature = _clean(ced_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_140'] = {'inputs': ['ced_replacement_d2_140'], 'func': ced_replacement_d3_140}


def ced_replacement_d3_141(ced_replacement_d2_141):
    feature = _clean(ced_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_141'] = {'inputs': ['ced_replacement_d2_141'], 'func': ced_replacement_d3_141}


def ced_replacement_d3_142(ced_replacement_d2_142):
    feature = _clean(ced_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_142'] = {'inputs': ['ced_replacement_d2_142'], 'func': ced_replacement_d3_142}


def ced_replacement_d3_143(ced_replacement_d2_143):
    feature = _clean(ced_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_143'] = {'inputs': ['ced_replacement_d2_143'], 'func': ced_replacement_d3_143}


def ced_replacement_d3_144(ced_replacement_d2_144):
    feature = _clean(ced_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_144'] = {'inputs': ['ced_replacement_d2_144'], 'func': ced_replacement_d3_144}


def ced_replacement_d3_145(ced_replacement_d2_145):
    feature = _clean(ced_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_145'] = {'inputs': ['ced_replacement_d2_145'], 'func': ced_replacement_d3_145}


def ced_replacement_d3_146(ced_replacement_d2_146):
    feature = _clean(ced_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_146'] = {'inputs': ['ced_replacement_d2_146'], 'func': ced_replacement_d3_146}


def ced_replacement_d3_147(ced_replacement_d2_147):
    feature = _clean(ced_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_147'] = {'inputs': ['ced_replacement_d2_147'], 'func': ced_replacement_d3_147}


def ced_replacement_d3_148(ced_replacement_d2_148):
    feature = _clean(ced_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_148'] = {'inputs': ['ced_replacement_d2_148'], 'func': ced_replacement_d3_148}


def ced_replacement_d3_149(ced_replacement_d2_149):
    feature = _clean(ced_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_149'] = {'inputs': ['ced_replacement_d2_149'], 'func': ced_replacement_d3_149}


def ced_replacement_d3_150(ced_replacement_d2_150):
    feature = _clean(ced_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_150'] = {'inputs': ['ced_replacement_d2_150'], 'func': ced_replacement_d3_150}


def ced_replacement_d3_151(ced_replacement_d2_151):
    feature = _clean(ced_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
CED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ced_replacement_d3_151'] = {'inputs': ['ced_replacement_d2_151'], 'func': ced_replacement_d3_151}


# Third-derivative extensions for repaired first-base features.
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ced_base_universe_d3_001_ced_002_dividend_suspension_density_42(ced_base_universe_d2_001_ced_002_dividend_suspension_density_42):
    return _base_universe_d3(ced_base_universe_d2_001_ced_002_dividend_suspension_density_42, 1)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_001_ced_002_dividend_suspension_density_42'] = {'inputs': ['ced_base_universe_d2_001_ced_002_dividend_suspension_density_42'], 'func': ced_base_universe_d3_001_ced_002_dividend_suspension_density_42}


def ced_base_universe_d3_002_ced_003_reverse_split_density_63(ced_base_universe_d2_002_ced_003_reverse_split_density_63):
    return _base_universe_d3(ced_base_universe_d2_002_ced_003_reverse_split_density_63, 2)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_002_ced_003_reverse_split_density_63'] = {'inputs': ['ced_base_universe_d2_002_ced_003_reverse_split_density_63'], 'func': ced_base_universe_d3_002_ced_003_reverse_split_density_63}


def ced_base_universe_d3_003_ced_004_event_density_z_84(ced_base_universe_d2_003_ced_004_event_density_z_84):
    return _base_universe_d3(ced_base_universe_d2_003_ced_004_event_density_z_84, 3)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_003_ced_004_event_density_z_84'] = {'inputs': ['ced_base_universe_d2_003_ced_004_event_density_z_84'], 'func': ced_base_universe_d3_003_ced_004_event_density_z_84}


def ced_base_universe_d3_004_ced_005_going_concern_persistence_126(ced_base_universe_d2_004_ced_005_going_concern_persistence_126):
    return _base_universe_d3(ced_base_universe_d2_004_ced_005_going_concern_persistence_126, 4)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_004_ced_005_going_concern_persistence_126'] = {'inputs': ['ced_base_universe_d2_004_ced_005_going_concern_persistence_126'], 'func': ced_base_universe_d3_004_ced_005_going_concern_persistence_126}


def ced_base_universe_d3_005_ced_006_delisting_notice_density_189(ced_base_universe_d2_005_ced_006_delisting_notice_density_189):
    return _base_universe_d3(ced_base_universe_d2_005_ced_006_delisting_notice_density_189, 5)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_005_ced_006_delisting_notice_density_189'] = {'inputs': ['ced_base_universe_d2_005_ced_006_delisting_notice_density_189'], 'func': ced_base_universe_d3_005_ced_006_delisting_notice_density_189}


def ced_base_universe_d3_006_ced_008_dividend_cut_density_378(ced_base_universe_d2_006_ced_008_dividend_cut_density_378):
    return _base_universe_d3(ced_base_universe_d2_006_ced_008_dividend_cut_density_378, 6)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_006_ced_008_dividend_cut_density_378'] = {'inputs': ['ced_base_universe_d2_006_ced_008_dividend_cut_density_378'], 'func': ced_base_universe_d3_006_ced_008_dividend_cut_density_378}


def ced_base_universe_d3_007_ced_009_dividend_suspension_density_504(ced_base_universe_d2_007_ced_009_dividend_suspension_density_504):
    return _base_universe_d3(ced_base_universe_d2_007_ced_009_dividend_suspension_density_504, 7)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_007_ced_009_dividend_suspension_density_504'] = {'inputs': ['ced_base_universe_d2_007_ced_009_dividend_suspension_density_504'], 'func': ced_base_universe_d3_007_ced_009_dividend_suspension_density_504}


def ced_base_universe_d3_008_ced_010_reverse_split_density_756(ced_base_universe_d2_008_ced_010_reverse_split_density_756):
    return _base_universe_d3(ced_base_universe_d2_008_ced_010_reverse_split_density_756, 8)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_008_ced_010_reverse_split_density_756'] = {'inputs': ['ced_base_universe_d2_008_ced_010_reverse_split_density_756'], 'func': ced_base_universe_d3_008_ced_010_reverse_split_density_756}


def ced_base_universe_d3_009_ced_011_event_density_z_1008(ced_base_universe_d2_009_ced_011_event_density_z_1008):
    return _base_universe_d3(ced_base_universe_d2_009_ced_011_event_density_z_1008, 9)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_009_ced_011_event_density_z_1008'] = {'inputs': ['ced_base_universe_d2_009_ced_011_event_density_z_1008'], 'func': ced_base_universe_d3_009_ced_011_event_density_z_1008}


def ced_base_universe_d3_010_ced_012_going_concern_persistence_1260(ced_base_universe_d2_010_ced_012_going_concern_persistence_1260):
    return _base_universe_d3(ced_base_universe_d2_010_ced_012_going_concern_persistence_1260, 10)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_010_ced_012_going_concern_persistence_1260'] = {'inputs': ['ced_base_universe_d2_010_ced_012_going_concern_persistence_1260'], 'func': ced_base_universe_d3_010_ced_012_going_concern_persistence_1260}


def ced_base_universe_d3_011_ced_015_dividend_cut_density_252(ced_base_universe_d2_011_ced_015_dividend_cut_density_252):
    return _base_universe_d3(ced_base_universe_d2_011_ced_015_dividend_cut_density_252, 11)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_011_ced_015_dividend_cut_density_252'] = {'inputs': ['ced_base_universe_d2_011_ced_015_dividend_cut_density_252'], 'func': ced_base_universe_d3_011_ced_015_dividend_cut_density_252}


def ced_base_universe_d3_012_ced_018_event_density_z_63(ced_base_universe_d2_012_ced_018_event_density_z_63):
    return _base_universe_d3(ced_base_universe_d2_012_ced_018_event_density_z_63, 12)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_012_ced_018_event_density_z_63'] = {'inputs': ['ced_base_universe_d2_012_ced_018_event_density_z_63'], 'func': ced_base_universe_d3_012_ced_018_event_density_z_63}


def ced_base_universe_d3_013_ced_020_delisting_notice_density_126(ced_base_universe_d2_013_ced_020_delisting_notice_density_126):
    return _base_universe_d3(ced_base_universe_d2_013_ced_020_delisting_notice_density_126, 13)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_013_ced_020_delisting_notice_density_126'] = {'inputs': ['ced_base_universe_d2_013_ced_020_delisting_notice_density_126'], 'func': ced_base_universe_d3_013_ced_020_delisting_notice_density_126}


def ced_base_universe_d3_014_ced_026_going_concern_persistence_1008(ced_base_universe_d2_014_ced_026_going_concern_persistence_1008):
    return _base_universe_d3(ced_base_universe_d2_014_ced_026_going_concern_persistence_1008, 14)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_014_ced_026_going_concern_persistence_1008'] = {'inputs': ['ced_base_universe_d2_014_ced_026_going_concern_persistence_1008'], 'func': ced_base_universe_d3_014_ced_026_going_concern_persistence_1008}


def ced_base_universe_d3_015_ced_027_delisting_notice_density_1260(ced_base_universe_d2_015_ced_027_delisting_notice_density_1260):
    return _base_universe_d3(ced_base_universe_d2_015_ced_027_delisting_notice_density_1260, 15)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_015_ced_027_delisting_notice_density_1260'] = {'inputs': ['ced_base_universe_d2_015_ced_027_delisting_notice_density_1260'], 'func': ced_base_universe_d3_015_ced_027_delisting_notice_density_1260}


def ced_base_universe_d3_016_ced_032_event_density_z_42(ced_base_universe_d2_016_ced_032_event_density_z_42):
    return _base_universe_d3(ced_base_universe_d2_016_ced_032_event_density_z_42, 16)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_016_ced_032_event_density_z_42'] = {'inputs': ['ced_base_universe_d2_016_ced_032_event_density_z_42'], 'func': ced_base_universe_d3_016_ced_032_event_density_z_42}


def ced_base_universe_d3_017_ced_033_going_concern_persistence_63(ced_base_universe_d2_017_ced_033_going_concern_persistence_63):
    return _base_universe_d3(ced_base_universe_d2_017_ced_033_going_concern_persistence_63, 17)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_017_ced_033_going_concern_persistence_63'] = {'inputs': ['ced_base_universe_d2_017_ced_033_going_concern_persistence_63'], 'func': ced_base_universe_d3_017_ced_033_going_concern_persistence_63}


def ced_base_universe_d3_018_ced_034_delisting_notice_density_84(ced_base_universe_d2_018_ced_034_delisting_notice_density_84):
    return _base_universe_d3(ced_base_universe_d2_018_ced_034_delisting_notice_density_84, 18)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_018_ced_034_delisting_notice_density_84'] = {'inputs': ['ced_base_universe_d2_018_ced_034_delisting_notice_density_84'], 'func': ced_base_universe_d3_018_ced_034_delisting_notice_density_84}


def ced_base_universe_d3_019_ced_039_event_density_z_504(ced_base_universe_d2_019_ced_039_event_density_z_504):
    return _base_universe_d3(ced_base_universe_d2_019_ced_039_event_density_z_504, 19)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_019_ced_039_event_density_z_504'] = {'inputs': ['ced_base_universe_d2_019_ced_039_event_density_z_504'], 'func': ced_base_universe_d3_019_ced_039_event_density_z_504}


def ced_base_universe_d3_020_ced_040_going_concern_persistence_756(ced_base_universe_d2_020_ced_040_going_concern_persistence_756):
    return _base_universe_d3(ced_base_universe_d2_020_ced_040_going_concern_persistence_756, 20)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_020_ced_040_going_concern_persistence_756'] = {'inputs': ['ced_base_universe_d2_020_ced_040_going_concern_persistence_756'], 'func': ced_base_universe_d3_020_ced_040_going_concern_persistence_756}


def ced_base_universe_d3_021_ced_041_delisting_notice_density_1008(ced_base_universe_d2_021_ced_041_delisting_notice_density_1008):
    return _base_universe_d3(ced_base_universe_d2_021_ced_041_delisting_notice_density_1008, 21)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_021_ced_041_delisting_notice_density_1008'] = {'inputs': ['ced_base_universe_d2_021_ced_041_delisting_notice_density_1008'], 'func': ced_base_universe_d3_021_ced_041_delisting_notice_density_1008}


def ced_base_universe_d3_022_ced_046_event_density_z_21(ced_base_universe_d2_022_ced_046_event_density_z_21):
    return _base_universe_d3(ced_base_universe_d2_022_ced_046_event_density_z_21, 22)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_022_ced_046_event_density_z_21'] = {'inputs': ['ced_base_universe_d2_022_ced_046_event_density_z_21'], 'func': ced_base_universe_d3_022_ced_046_event_density_z_21}


def ced_base_universe_d3_023_ced_047_going_concern_persistence_42(ced_base_universe_d2_023_ced_047_going_concern_persistence_42):
    return _base_universe_d3(ced_base_universe_d2_023_ced_047_going_concern_persistence_42, 23)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_023_ced_047_going_concern_persistence_42'] = {'inputs': ['ced_base_universe_d2_023_ced_047_going_concern_persistence_42'], 'func': ced_base_universe_d3_023_ced_047_going_concern_persistence_42}


def ced_base_universe_d3_024_ced_053_event_density_z_378(ced_base_universe_d2_024_ced_053_event_density_z_378):
    return _base_universe_d3(ced_base_universe_d2_024_ced_053_event_density_z_378, 24)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_024_ced_053_event_density_z_378'] = {'inputs': ['ced_base_universe_d2_024_ced_053_event_density_z_378'], 'func': ced_base_universe_d3_024_ced_053_event_density_z_378}


def ced_base_universe_d3_025_ced_054_going_concern_persistence_504(ced_base_universe_d2_025_ced_054_going_concern_persistence_504):
    return _base_universe_d3(ced_base_universe_d2_025_ced_054_going_concern_persistence_504, 25)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_025_ced_054_going_concern_persistence_504'] = {'inputs': ['ced_base_universe_d2_025_ced_054_going_concern_persistence_504'], 'func': ced_base_universe_d3_025_ced_054_going_concern_persistence_504}


def ced_base_universe_d3_026_ced_060_event_density_z_252(ced_base_universe_d2_026_ced_060_event_density_z_252):
    return _base_universe_d3(ced_base_universe_d2_026_ced_060_event_density_z_252, 26)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_026_ced_060_event_density_z_252'] = {'inputs': ['ced_base_universe_d2_026_ced_060_event_density_z_252'], 'func': ced_base_universe_d3_026_ced_060_event_density_z_252}


def ced_base_universe_d3_027_ced_061_going_concern_persistence_21(ced_base_universe_d2_027_ced_061_going_concern_persistence_21):
    return _base_universe_d3(ced_base_universe_d2_027_ced_061_going_concern_persistence_21, 27)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_027_ced_061_going_concern_persistence_21'] = {'inputs': ['ced_base_universe_d2_027_ced_061_going_concern_persistence_21'], 'func': ced_base_universe_d3_027_ced_061_going_concern_persistence_21}


def ced_base_universe_d3_028_ced_068_going_concern_persistence_378(ced_base_universe_d2_028_ced_068_going_concern_persistence_378):
    return _base_universe_d3(ced_base_universe_d2_028_ced_068_going_concern_persistence_378, 28)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_028_ced_068_going_concern_persistence_378'] = {'inputs': ['ced_base_universe_d2_028_ced_068_going_concern_persistence_378'], 'func': ced_base_universe_d3_028_ced_068_going_concern_persistence_378}


def ced_base_universe_d3_029_ced_075_going_concern_persistence_252(ced_base_universe_d2_029_ced_075_going_concern_persistence_252):
    return _base_universe_d3(ced_base_universe_d2_029_ced_075_going_concern_persistence_252, 29)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_029_ced_075_going_concern_persistence_252'] = {'inputs': ['ced_base_universe_d2_029_ced_075_going_concern_persistence_252'], 'func': ced_base_universe_d3_029_ced_075_going_concern_persistence_252}


def ced_base_universe_d3_030_ced_basefill_007(ced_base_universe_d2_030_ced_basefill_007):
    return _base_universe_d3(ced_base_universe_d2_030_ced_basefill_007, 30)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_030_ced_basefill_007'] = {'inputs': ['ced_base_universe_d2_030_ced_basefill_007'], 'func': ced_base_universe_d3_030_ced_basefill_007}


def ced_base_universe_d3_031_ced_basefill_014(ced_base_universe_d2_031_ced_basefill_014):
    return _base_universe_d3(ced_base_universe_d2_031_ced_basefill_014, 31)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_031_ced_basefill_014'] = {'inputs': ['ced_base_universe_d2_031_ced_basefill_014'], 'func': ced_base_universe_d3_031_ced_basefill_014}


def ced_base_universe_d3_032_ced_basefill_016(ced_base_universe_d2_032_ced_basefill_016):
    return _base_universe_d3(ced_base_universe_d2_032_ced_basefill_016, 32)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_032_ced_basefill_016'] = {'inputs': ['ced_base_universe_d2_032_ced_basefill_016'], 'func': ced_base_universe_d3_032_ced_basefill_016}


def ced_base_universe_d3_033_ced_basefill_017(ced_base_universe_d2_033_ced_basefill_017):
    return _base_universe_d3(ced_base_universe_d2_033_ced_basefill_017, 33)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_033_ced_basefill_017'] = {'inputs': ['ced_base_universe_d2_033_ced_basefill_017'], 'func': ced_base_universe_d3_033_ced_basefill_017}


def ced_base_universe_d3_034_ced_basefill_021(ced_base_universe_d2_034_ced_basefill_021):
    return _base_universe_d3(ced_base_universe_d2_034_ced_basefill_021, 34)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_034_ced_basefill_021'] = {'inputs': ['ced_base_universe_d2_034_ced_basefill_021'], 'func': ced_base_universe_d3_034_ced_basefill_021}


def ced_base_universe_d3_035_ced_basefill_022(ced_base_universe_d2_035_ced_basefill_022):
    return _base_universe_d3(ced_base_universe_d2_035_ced_basefill_022, 35)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_035_ced_basefill_022'] = {'inputs': ['ced_base_universe_d2_035_ced_basefill_022'], 'func': ced_base_universe_d3_035_ced_basefill_022}


def ced_base_universe_d3_036_ced_basefill_023(ced_base_universe_d2_036_ced_basefill_023):
    return _base_universe_d3(ced_base_universe_d2_036_ced_basefill_023, 36)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_036_ced_basefill_023'] = {'inputs': ['ced_base_universe_d2_036_ced_basefill_023'], 'func': ced_base_universe_d3_036_ced_basefill_023}


def ced_base_universe_d3_037_ced_basefill_024(ced_base_universe_d2_037_ced_basefill_024):
    return _base_universe_d3(ced_base_universe_d2_037_ced_basefill_024, 37)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_037_ced_basefill_024'] = {'inputs': ['ced_base_universe_d2_037_ced_basefill_024'], 'func': ced_base_universe_d3_037_ced_basefill_024}


def ced_base_universe_d3_038_ced_basefill_028(ced_base_universe_d2_038_ced_basefill_028):
    return _base_universe_d3(ced_base_universe_d2_038_ced_basefill_028, 38)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_038_ced_basefill_028'] = {'inputs': ['ced_base_universe_d2_038_ced_basefill_028'], 'func': ced_base_universe_d3_038_ced_basefill_028}


def ced_base_universe_d3_039_ced_basefill_029(ced_base_universe_d2_039_ced_basefill_029):
    return _base_universe_d3(ced_base_universe_d2_039_ced_basefill_029, 39)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_039_ced_basefill_029'] = {'inputs': ['ced_base_universe_d2_039_ced_basefill_029'], 'func': ced_base_universe_d3_039_ced_basefill_029}


def ced_base_universe_d3_040_ced_basefill_030(ced_base_universe_d2_040_ced_basefill_030):
    return _base_universe_d3(ced_base_universe_d2_040_ced_basefill_030, 40)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_040_ced_basefill_030'] = {'inputs': ['ced_base_universe_d2_040_ced_basefill_030'], 'func': ced_base_universe_d3_040_ced_basefill_030}


def ced_base_universe_d3_041_ced_basefill_031(ced_base_universe_d2_041_ced_basefill_031):
    return _base_universe_d3(ced_base_universe_d2_041_ced_basefill_031, 41)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_041_ced_basefill_031'] = {'inputs': ['ced_base_universe_d2_041_ced_basefill_031'], 'func': ced_base_universe_d3_041_ced_basefill_031}


def ced_base_universe_d3_042_ced_basefill_035(ced_base_universe_d2_042_ced_basefill_035):
    return _base_universe_d3(ced_base_universe_d2_042_ced_basefill_035, 42)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_042_ced_basefill_035'] = {'inputs': ['ced_base_universe_d2_042_ced_basefill_035'], 'func': ced_base_universe_d3_042_ced_basefill_035}


def ced_base_universe_d3_043_ced_basefill_036(ced_base_universe_d2_043_ced_basefill_036):
    return _base_universe_d3(ced_base_universe_d2_043_ced_basefill_036, 43)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_043_ced_basefill_036'] = {'inputs': ['ced_base_universe_d2_043_ced_basefill_036'], 'func': ced_base_universe_d3_043_ced_basefill_036}


def ced_base_universe_d3_044_ced_basefill_037(ced_base_universe_d2_044_ced_basefill_037):
    return _base_universe_d3(ced_base_universe_d2_044_ced_basefill_037, 44)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_044_ced_basefill_037'] = {'inputs': ['ced_base_universe_d2_044_ced_basefill_037'], 'func': ced_base_universe_d3_044_ced_basefill_037}


def ced_base_universe_d3_045_ced_basefill_038(ced_base_universe_d2_045_ced_basefill_038):
    return _base_universe_d3(ced_base_universe_d2_045_ced_basefill_038, 45)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_045_ced_basefill_038'] = {'inputs': ['ced_base_universe_d2_045_ced_basefill_038'], 'func': ced_base_universe_d3_045_ced_basefill_038}


def ced_base_universe_d3_046_ced_basefill_042(ced_base_universe_d2_046_ced_basefill_042):
    return _base_universe_d3(ced_base_universe_d2_046_ced_basefill_042, 46)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_046_ced_basefill_042'] = {'inputs': ['ced_base_universe_d2_046_ced_basefill_042'], 'func': ced_base_universe_d3_046_ced_basefill_042}


def ced_base_universe_d3_047_ced_basefill_043(ced_base_universe_d2_047_ced_basefill_043):
    return _base_universe_d3(ced_base_universe_d2_047_ced_basefill_043, 47)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_047_ced_basefill_043'] = {'inputs': ['ced_base_universe_d2_047_ced_basefill_043'], 'func': ced_base_universe_d3_047_ced_basefill_043}


def ced_base_universe_d3_048_ced_basefill_044(ced_base_universe_d2_048_ced_basefill_044):
    return _base_universe_d3(ced_base_universe_d2_048_ced_basefill_044, 48)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_048_ced_basefill_044'] = {'inputs': ['ced_base_universe_d2_048_ced_basefill_044'], 'func': ced_base_universe_d3_048_ced_basefill_044}


def ced_base_universe_d3_049_ced_basefill_045(ced_base_universe_d2_049_ced_basefill_045):
    return _base_universe_d3(ced_base_universe_d2_049_ced_basefill_045, 49)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_049_ced_basefill_045'] = {'inputs': ['ced_base_universe_d2_049_ced_basefill_045'], 'func': ced_base_universe_d3_049_ced_basefill_045}


def ced_base_universe_d3_050_ced_basefill_048(ced_base_universe_d2_050_ced_basefill_048):
    return _base_universe_d3(ced_base_universe_d2_050_ced_basefill_048, 50)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_050_ced_basefill_048'] = {'inputs': ['ced_base_universe_d2_050_ced_basefill_048'], 'func': ced_base_universe_d3_050_ced_basefill_048}


def ced_base_universe_d3_051_ced_basefill_049(ced_base_universe_d2_051_ced_basefill_049):
    return _base_universe_d3(ced_base_universe_d2_051_ced_basefill_049, 51)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_051_ced_basefill_049'] = {'inputs': ['ced_base_universe_d2_051_ced_basefill_049'], 'func': ced_base_universe_d3_051_ced_basefill_049}


def ced_base_universe_d3_052_ced_basefill_050(ced_base_universe_d2_052_ced_basefill_050):
    return _base_universe_d3(ced_base_universe_d2_052_ced_basefill_050, 52)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_052_ced_basefill_050'] = {'inputs': ['ced_base_universe_d2_052_ced_basefill_050'], 'func': ced_base_universe_d3_052_ced_basefill_050}


def ced_base_universe_d3_053_ced_basefill_051(ced_base_universe_d2_053_ced_basefill_051):
    return _base_universe_d3(ced_base_universe_d2_053_ced_basefill_051, 53)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_053_ced_basefill_051'] = {'inputs': ['ced_base_universe_d2_053_ced_basefill_051'], 'func': ced_base_universe_d3_053_ced_basefill_051}


def ced_base_universe_d3_054_ced_basefill_052(ced_base_universe_d2_054_ced_basefill_052):
    return _base_universe_d3(ced_base_universe_d2_054_ced_basefill_052, 54)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_054_ced_basefill_052'] = {'inputs': ['ced_base_universe_d2_054_ced_basefill_052'], 'func': ced_base_universe_d3_054_ced_basefill_052}


def ced_base_universe_d3_055_ced_basefill_055(ced_base_universe_d2_055_ced_basefill_055):
    return _base_universe_d3(ced_base_universe_d2_055_ced_basefill_055, 55)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_055_ced_basefill_055'] = {'inputs': ['ced_base_universe_d2_055_ced_basefill_055'], 'func': ced_base_universe_d3_055_ced_basefill_055}


def ced_base_universe_d3_056_ced_basefill_056(ced_base_universe_d2_056_ced_basefill_056):
    return _base_universe_d3(ced_base_universe_d2_056_ced_basefill_056, 56)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_056_ced_basefill_056'] = {'inputs': ['ced_base_universe_d2_056_ced_basefill_056'], 'func': ced_base_universe_d3_056_ced_basefill_056}


def ced_base_universe_d3_057_ced_basefill_057(ced_base_universe_d2_057_ced_basefill_057):
    return _base_universe_d3(ced_base_universe_d2_057_ced_basefill_057, 57)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_057_ced_basefill_057'] = {'inputs': ['ced_base_universe_d2_057_ced_basefill_057'], 'func': ced_base_universe_d3_057_ced_basefill_057}


def ced_base_universe_d3_058_ced_basefill_058(ced_base_universe_d2_058_ced_basefill_058):
    return _base_universe_d3(ced_base_universe_d2_058_ced_basefill_058, 58)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_058_ced_basefill_058'] = {'inputs': ['ced_base_universe_d2_058_ced_basefill_058'], 'func': ced_base_universe_d3_058_ced_basefill_058}


def ced_base_universe_d3_059_ced_basefill_059(ced_base_universe_d2_059_ced_basefill_059):
    return _base_universe_d3(ced_base_universe_d2_059_ced_basefill_059, 59)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_059_ced_basefill_059'] = {'inputs': ['ced_base_universe_d2_059_ced_basefill_059'], 'func': ced_base_universe_d3_059_ced_basefill_059}


def ced_base_universe_d3_060_ced_basefill_062(ced_base_universe_d2_060_ced_basefill_062):
    return _base_universe_d3(ced_base_universe_d2_060_ced_basefill_062, 60)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_060_ced_basefill_062'] = {'inputs': ['ced_base_universe_d2_060_ced_basefill_062'], 'func': ced_base_universe_d3_060_ced_basefill_062}


def ced_base_universe_d3_061_ced_basefill_063(ced_base_universe_d2_061_ced_basefill_063):
    return _base_universe_d3(ced_base_universe_d2_061_ced_basefill_063, 61)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_061_ced_basefill_063'] = {'inputs': ['ced_base_universe_d2_061_ced_basefill_063'], 'func': ced_base_universe_d3_061_ced_basefill_063}


def ced_base_universe_d3_062_ced_basefill_064(ced_base_universe_d2_062_ced_basefill_064):
    return _base_universe_d3(ced_base_universe_d2_062_ced_basefill_064, 62)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_062_ced_basefill_064'] = {'inputs': ['ced_base_universe_d2_062_ced_basefill_064'], 'func': ced_base_universe_d3_062_ced_basefill_064}


def ced_base_universe_d3_063_ced_basefill_065(ced_base_universe_d2_063_ced_basefill_065):
    return _base_universe_d3(ced_base_universe_d2_063_ced_basefill_065, 63)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_063_ced_basefill_065'] = {'inputs': ['ced_base_universe_d2_063_ced_basefill_065'], 'func': ced_base_universe_d3_063_ced_basefill_065}


def ced_base_universe_d3_064_ced_basefill_066(ced_base_universe_d2_064_ced_basefill_066):
    return _base_universe_d3(ced_base_universe_d2_064_ced_basefill_066, 64)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_064_ced_basefill_066'] = {'inputs': ['ced_base_universe_d2_064_ced_basefill_066'], 'func': ced_base_universe_d3_064_ced_basefill_066}


def ced_base_universe_d3_065_ced_basefill_067(ced_base_universe_d2_065_ced_basefill_067):
    return _base_universe_d3(ced_base_universe_d2_065_ced_basefill_067, 65)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_065_ced_basefill_067'] = {'inputs': ['ced_base_universe_d2_065_ced_basefill_067'], 'func': ced_base_universe_d3_065_ced_basefill_067}


def ced_base_universe_d3_066_ced_basefill_069(ced_base_universe_d2_066_ced_basefill_069):
    return _base_universe_d3(ced_base_universe_d2_066_ced_basefill_069, 66)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_066_ced_basefill_069'] = {'inputs': ['ced_base_universe_d2_066_ced_basefill_069'], 'func': ced_base_universe_d3_066_ced_basefill_069}


def ced_base_universe_d3_067_ced_basefill_070(ced_base_universe_d2_067_ced_basefill_070):
    return _base_universe_d3(ced_base_universe_d2_067_ced_basefill_070, 67)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_067_ced_basefill_070'] = {'inputs': ['ced_base_universe_d2_067_ced_basefill_070'], 'func': ced_base_universe_d3_067_ced_basefill_070}


def ced_base_universe_d3_068_ced_basefill_071(ced_base_universe_d2_068_ced_basefill_071):
    return _base_universe_d3(ced_base_universe_d2_068_ced_basefill_071, 68)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_068_ced_basefill_071'] = {'inputs': ['ced_base_universe_d2_068_ced_basefill_071'], 'func': ced_base_universe_d3_068_ced_basefill_071}


def ced_base_universe_d3_069_ced_basefill_072(ced_base_universe_d2_069_ced_basefill_072):
    return _base_universe_d3(ced_base_universe_d2_069_ced_basefill_072, 69)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_069_ced_basefill_072'] = {'inputs': ['ced_base_universe_d2_069_ced_basefill_072'], 'func': ced_base_universe_d3_069_ced_basefill_072}


def ced_base_universe_d3_070_ced_basefill_073(ced_base_universe_d2_070_ced_basefill_073):
    return _base_universe_d3(ced_base_universe_d2_070_ced_basefill_073, 70)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_070_ced_basefill_073'] = {'inputs': ['ced_base_universe_d2_070_ced_basefill_073'], 'func': ced_base_universe_d3_070_ced_basefill_073}


def ced_base_universe_d3_071_ced_basefill_074(ced_base_universe_d2_071_ced_basefill_074):
    return _base_universe_d3(ced_base_universe_d2_071_ced_basefill_074, 71)
CED_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ced_base_universe_d3_071_ced_basefill_074'] = {'inputs': ['ced_base_universe_d2_071_ced_basefill_074'], 'func': ced_base_universe_d3_071_ced_basefill_074}
