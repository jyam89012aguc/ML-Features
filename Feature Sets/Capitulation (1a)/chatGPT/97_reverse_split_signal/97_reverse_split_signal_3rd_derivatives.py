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



def rss_176_rss_001_dividend_cut_density_21_accel_1(rss_151_rss_001_dividend_cut_density_21_roc_1):
    feature = _s(rss_151_rss_001_dividend_cut_density_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rss_177_rss_007_listing_tier_decay_1_accel_42(rss_152_rss_007_listing_tier_decay_1_roc_42):
    feature = _s(rss_152_rss_007_listing_tier_decay_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rss_178_rss_013_delisting_notice_density_1512_accel_126(rss_153_rss_013_delisting_notice_density_1512_roc_126):
    feature = _s(rss_153_rss_013_delisting_notice_density_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rss_179_rss_019_going_concern_persistence_84_accel_378(rss_154_rss_019_going_concern_persistence_84_roc_378):
    feature = _s(rss_154_rss_019_going_concern_persistence_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def rss_180_rss_025_event_density_z_756_accel_4(rss_155_rss_025_event_density_z_756_roc_4):
    feature = _s(rss_155_rss_025_event_density_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















REVERSE_SPLIT_SIGNAL_REGISTRY_3RD_DERIVATIVES = {
    'rss_176_rss_001_dividend_cut_density_21_accel_1': {'inputs': ['rss_151_rss_001_dividend_cut_density_21_roc_1'], 'func': rss_176_rss_001_dividend_cut_density_21_accel_1},
    'rss_177_rss_007_listing_tier_decay_1_accel_42': {'inputs': ['rss_152_rss_007_listing_tier_decay_1_roc_42'], 'func': rss_177_rss_007_listing_tier_decay_1_accel_42},
    'rss_178_rss_013_delisting_notice_density_1512_accel_126': {'inputs': ['rss_153_rss_013_delisting_notice_density_1512_roc_126'], 'func': rss_178_rss_013_delisting_notice_density_1512_accel_126},
    'rss_179_rss_019_going_concern_persistence_84_accel_378': {'inputs': ['rss_154_rss_019_going_concern_persistence_84_roc_378'], 'func': rss_179_rss_019_going_concern_persistence_84_accel_378},
    'rss_180_rss_025_event_density_z_756_accel_4': {'inputs': ['rss_155_rss_025_event_density_z_756_roc_4'], 'func': rss_180_rss_025_event_density_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rss_replacement_d3_001(rss_replacement_d2_001):
    feature = _clean(rss_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_001'] = {'inputs': ['rss_replacement_d2_001'], 'func': rss_replacement_d3_001}


def rss_replacement_d3_002(rss_replacement_d2_002):
    feature = _clean(rss_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_002'] = {'inputs': ['rss_replacement_d2_002'], 'func': rss_replacement_d3_002}


def rss_replacement_d3_003(rss_replacement_d2_003):
    feature = _clean(rss_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_003'] = {'inputs': ['rss_replacement_d2_003'], 'func': rss_replacement_d3_003}


def rss_replacement_d3_004(rss_replacement_d2_004):
    feature = _clean(rss_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_004'] = {'inputs': ['rss_replacement_d2_004'], 'func': rss_replacement_d3_004}


def rss_replacement_d3_005(rss_replacement_d2_005):
    feature = _clean(rss_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_005'] = {'inputs': ['rss_replacement_d2_005'], 'func': rss_replacement_d3_005}


def rss_replacement_d3_006(rss_replacement_d2_006):
    feature = _clean(rss_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_006'] = {'inputs': ['rss_replacement_d2_006'], 'func': rss_replacement_d3_006}


def rss_replacement_d3_007(rss_replacement_d2_007):
    feature = _clean(rss_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_007'] = {'inputs': ['rss_replacement_d2_007'], 'func': rss_replacement_d3_007}


def rss_replacement_d3_008(rss_replacement_d2_008):
    feature = _clean(rss_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_008'] = {'inputs': ['rss_replacement_d2_008'], 'func': rss_replacement_d3_008}


def rss_replacement_d3_009(rss_replacement_d2_009):
    feature = _clean(rss_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_009'] = {'inputs': ['rss_replacement_d2_009'], 'func': rss_replacement_d3_009}


def rss_replacement_d3_010(rss_replacement_d2_010):
    feature = _clean(rss_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_010'] = {'inputs': ['rss_replacement_d2_010'], 'func': rss_replacement_d3_010}


def rss_replacement_d3_011(rss_replacement_d2_011):
    feature = _clean(rss_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_011'] = {'inputs': ['rss_replacement_d2_011'], 'func': rss_replacement_d3_011}


def rss_replacement_d3_012(rss_replacement_d2_012):
    feature = _clean(rss_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_012'] = {'inputs': ['rss_replacement_d2_012'], 'func': rss_replacement_d3_012}


def rss_replacement_d3_013(rss_replacement_d2_013):
    feature = _clean(rss_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_013'] = {'inputs': ['rss_replacement_d2_013'], 'func': rss_replacement_d3_013}


def rss_replacement_d3_014(rss_replacement_d2_014):
    feature = _clean(rss_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_014'] = {'inputs': ['rss_replacement_d2_014'], 'func': rss_replacement_d3_014}


def rss_replacement_d3_015(rss_replacement_d2_015):
    feature = _clean(rss_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_015'] = {'inputs': ['rss_replacement_d2_015'], 'func': rss_replacement_d3_015}


def rss_replacement_d3_016(rss_replacement_d2_016):
    feature = _clean(rss_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_016'] = {'inputs': ['rss_replacement_d2_016'], 'func': rss_replacement_d3_016}


def rss_replacement_d3_017(rss_replacement_d2_017):
    feature = _clean(rss_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_017'] = {'inputs': ['rss_replacement_d2_017'], 'func': rss_replacement_d3_017}


def rss_replacement_d3_018(rss_replacement_d2_018):
    feature = _clean(rss_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_018'] = {'inputs': ['rss_replacement_d2_018'], 'func': rss_replacement_d3_018}


def rss_replacement_d3_019(rss_replacement_d2_019):
    feature = _clean(rss_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_019'] = {'inputs': ['rss_replacement_d2_019'], 'func': rss_replacement_d3_019}


def rss_replacement_d3_020(rss_replacement_d2_020):
    feature = _clean(rss_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_020'] = {'inputs': ['rss_replacement_d2_020'], 'func': rss_replacement_d3_020}


def rss_replacement_d3_021(rss_replacement_d2_021):
    feature = _clean(rss_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_021'] = {'inputs': ['rss_replacement_d2_021'], 'func': rss_replacement_d3_021}


def rss_replacement_d3_022(rss_replacement_d2_022):
    feature = _clean(rss_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_022'] = {'inputs': ['rss_replacement_d2_022'], 'func': rss_replacement_d3_022}


def rss_replacement_d3_023(rss_replacement_d2_023):
    feature = _clean(rss_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_023'] = {'inputs': ['rss_replacement_d2_023'], 'func': rss_replacement_d3_023}


def rss_replacement_d3_024(rss_replacement_d2_024):
    feature = _clean(rss_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_024'] = {'inputs': ['rss_replacement_d2_024'], 'func': rss_replacement_d3_024}


def rss_replacement_d3_025(rss_replacement_d2_025):
    feature = _clean(rss_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_025'] = {'inputs': ['rss_replacement_d2_025'], 'func': rss_replacement_d3_025}


def rss_replacement_d3_026(rss_replacement_d2_026):
    feature = _clean(rss_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_026'] = {'inputs': ['rss_replacement_d2_026'], 'func': rss_replacement_d3_026}


def rss_replacement_d3_027(rss_replacement_d2_027):
    feature = _clean(rss_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_027'] = {'inputs': ['rss_replacement_d2_027'], 'func': rss_replacement_d3_027}


def rss_replacement_d3_028(rss_replacement_d2_028):
    feature = _clean(rss_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_028'] = {'inputs': ['rss_replacement_d2_028'], 'func': rss_replacement_d3_028}


def rss_replacement_d3_029(rss_replacement_d2_029):
    feature = _clean(rss_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_029'] = {'inputs': ['rss_replacement_d2_029'], 'func': rss_replacement_d3_029}


def rss_replacement_d3_030(rss_replacement_d2_030):
    feature = _clean(rss_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_030'] = {'inputs': ['rss_replacement_d2_030'], 'func': rss_replacement_d3_030}


def rss_replacement_d3_031(rss_replacement_d2_031):
    feature = _clean(rss_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_031'] = {'inputs': ['rss_replacement_d2_031'], 'func': rss_replacement_d3_031}


def rss_replacement_d3_032(rss_replacement_d2_032):
    feature = _clean(rss_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_032'] = {'inputs': ['rss_replacement_d2_032'], 'func': rss_replacement_d3_032}


def rss_replacement_d3_033(rss_replacement_d2_033):
    feature = _clean(rss_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_033'] = {'inputs': ['rss_replacement_d2_033'], 'func': rss_replacement_d3_033}


def rss_replacement_d3_034(rss_replacement_d2_034):
    feature = _clean(rss_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_034'] = {'inputs': ['rss_replacement_d2_034'], 'func': rss_replacement_d3_034}


def rss_replacement_d3_035(rss_replacement_d2_035):
    feature = _clean(rss_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_035'] = {'inputs': ['rss_replacement_d2_035'], 'func': rss_replacement_d3_035}


def rss_replacement_d3_036(rss_replacement_d2_036):
    feature = _clean(rss_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_036'] = {'inputs': ['rss_replacement_d2_036'], 'func': rss_replacement_d3_036}


def rss_replacement_d3_037(rss_replacement_d2_037):
    feature = _clean(rss_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_037'] = {'inputs': ['rss_replacement_d2_037'], 'func': rss_replacement_d3_037}


def rss_replacement_d3_038(rss_replacement_d2_038):
    feature = _clean(rss_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_038'] = {'inputs': ['rss_replacement_d2_038'], 'func': rss_replacement_d3_038}


def rss_replacement_d3_039(rss_replacement_d2_039):
    feature = _clean(rss_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_039'] = {'inputs': ['rss_replacement_d2_039'], 'func': rss_replacement_d3_039}


def rss_replacement_d3_040(rss_replacement_d2_040):
    feature = _clean(rss_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_040'] = {'inputs': ['rss_replacement_d2_040'], 'func': rss_replacement_d3_040}


def rss_replacement_d3_041(rss_replacement_d2_041):
    feature = _clean(rss_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_041'] = {'inputs': ['rss_replacement_d2_041'], 'func': rss_replacement_d3_041}


def rss_replacement_d3_042(rss_replacement_d2_042):
    feature = _clean(rss_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_042'] = {'inputs': ['rss_replacement_d2_042'], 'func': rss_replacement_d3_042}


def rss_replacement_d3_043(rss_replacement_d2_043):
    feature = _clean(rss_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_043'] = {'inputs': ['rss_replacement_d2_043'], 'func': rss_replacement_d3_043}


def rss_replacement_d3_044(rss_replacement_d2_044):
    feature = _clean(rss_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_044'] = {'inputs': ['rss_replacement_d2_044'], 'func': rss_replacement_d3_044}


def rss_replacement_d3_045(rss_replacement_d2_045):
    feature = _clean(rss_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_045'] = {'inputs': ['rss_replacement_d2_045'], 'func': rss_replacement_d3_045}


def rss_replacement_d3_046(rss_replacement_d2_046):
    feature = _clean(rss_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_046'] = {'inputs': ['rss_replacement_d2_046'], 'func': rss_replacement_d3_046}


def rss_replacement_d3_047(rss_replacement_d2_047):
    feature = _clean(rss_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_047'] = {'inputs': ['rss_replacement_d2_047'], 'func': rss_replacement_d3_047}


def rss_replacement_d3_048(rss_replacement_d2_048):
    feature = _clean(rss_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_048'] = {'inputs': ['rss_replacement_d2_048'], 'func': rss_replacement_d3_048}


def rss_replacement_d3_049(rss_replacement_d2_049):
    feature = _clean(rss_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_049'] = {'inputs': ['rss_replacement_d2_049'], 'func': rss_replacement_d3_049}


def rss_replacement_d3_050(rss_replacement_d2_050):
    feature = _clean(rss_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_050'] = {'inputs': ['rss_replacement_d2_050'], 'func': rss_replacement_d3_050}


def rss_replacement_d3_051(rss_replacement_d2_051):
    feature = _clean(rss_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_051'] = {'inputs': ['rss_replacement_d2_051'], 'func': rss_replacement_d3_051}


def rss_replacement_d3_052(rss_replacement_d2_052):
    feature = _clean(rss_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_052'] = {'inputs': ['rss_replacement_d2_052'], 'func': rss_replacement_d3_052}


def rss_replacement_d3_053(rss_replacement_d2_053):
    feature = _clean(rss_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_053'] = {'inputs': ['rss_replacement_d2_053'], 'func': rss_replacement_d3_053}


def rss_replacement_d3_054(rss_replacement_d2_054):
    feature = _clean(rss_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_054'] = {'inputs': ['rss_replacement_d2_054'], 'func': rss_replacement_d3_054}


def rss_replacement_d3_055(rss_replacement_d2_055):
    feature = _clean(rss_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_055'] = {'inputs': ['rss_replacement_d2_055'], 'func': rss_replacement_d3_055}


def rss_replacement_d3_056(rss_replacement_d2_056):
    feature = _clean(rss_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_056'] = {'inputs': ['rss_replacement_d2_056'], 'func': rss_replacement_d3_056}


def rss_replacement_d3_057(rss_replacement_d2_057):
    feature = _clean(rss_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_057'] = {'inputs': ['rss_replacement_d2_057'], 'func': rss_replacement_d3_057}


def rss_replacement_d3_058(rss_replacement_d2_058):
    feature = _clean(rss_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_058'] = {'inputs': ['rss_replacement_d2_058'], 'func': rss_replacement_d3_058}


def rss_replacement_d3_059(rss_replacement_d2_059):
    feature = _clean(rss_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_059'] = {'inputs': ['rss_replacement_d2_059'], 'func': rss_replacement_d3_059}


def rss_replacement_d3_060(rss_replacement_d2_060):
    feature = _clean(rss_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_060'] = {'inputs': ['rss_replacement_d2_060'], 'func': rss_replacement_d3_060}


def rss_replacement_d3_061(rss_replacement_d2_061):
    feature = _clean(rss_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_061'] = {'inputs': ['rss_replacement_d2_061'], 'func': rss_replacement_d3_061}


def rss_replacement_d3_062(rss_replacement_d2_062):
    feature = _clean(rss_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_062'] = {'inputs': ['rss_replacement_d2_062'], 'func': rss_replacement_d3_062}


def rss_replacement_d3_063(rss_replacement_d2_063):
    feature = _clean(rss_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_063'] = {'inputs': ['rss_replacement_d2_063'], 'func': rss_replacement_d3_063}


def rss_replacement_d3_064(rss_replacement_d2_064):
    feature = _clean(rss_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_064'] = {'inputs': ['rss_replacement_d2_064'], 'func': rss_replacement_d3_064}


def rss_replacement_d3_065(rss_replacement_d2_065):
    feature = _clean(rss_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_065'] = {'inputs': ['rss_replacement_d2_065'], 'func': rss_replacement_d3_065}


def rss_replacement_d3_066(rss_replacement_d2_066):
    feature = _clean(rss_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_066'] = {'inputs': ['rss_replacement_d2_066'], 'func': rss_replacement_d3_066}


def rss_replacement_d3_067(rss_replacement_d2_067):
    feature = _clean(rss_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_067'] = {'inputs': ['rss_replacement_d2_067'], 'func': rss_replacement_d3_067}


def rss_replacement_d3_068(rss_replacement_d2_068):
    feature = _clean(rss_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_068'] = {'inputs': ['rss_replacement_d2_068'], 'func': rss_replacement_d3_068}


def rss_replacement_d3_069(rss_replacement_d2_069):
    feature = _clean(rss_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_069'] = {'inputs': ['rss_replacement_d2_069'], 'func': rss_replacement_d3_069}


def rss_replacement_d3_070(rss_replacement_d2_070):
    feature = _clean(rss_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_070'] = {'inputs': ['rss_replacement_d2_070'], 'func': rss_replacement_d3_070}


def rss_replacement_d3_071(rss_replacement_d2_071):
    feature = _clean(rss_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_071'] = {'inputs': ['rss_replacement_d2_071'], 'func': rss_replacement_d3_071}


def rss_replacement_d3_072(rss_replacement_d2_072):
    feature = _clean(rss_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_072'] = {'inputs': ['rss_replacement_d2_072'], 'func': rss_replacement_d3_072}


def rss_replacement_d3_073(rss_replacement_d2_073):
    feature = _clean(rss_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_073'] = {'inputs': ['rss_replacement_d2_073'], 'func': rss_replacement_d3_073}


def rss_replacement_d3_074(rss_replacement_d2_074):
    feature = _clean(rss_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_074'] = {'inputs': ['rss_replacement_d2_074'], 'func': rss_replacement_d3_074}


def rss_replacement_d3_075(rss_replacement_d2_075):
    feature = _clean(rss_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_075'] = {'inputs': ['rss_replacement_d2_075'], 'func': rss_replacement_d3_075}


def rss_replacement_d3_076(rss_replacement_d2_076):
    feature = _clean(rss_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_076'] = {'inputs': ['rss_replacement_d2_076'], 'func': rss_replacement_d3_076}


def rss_replacement_d3_077(rss_replacement_d2_077):
    feature = _clean(rss_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_077'] = {'inputs': ['rss_replacement_d2_077'], 'func': rss_replacement_d3_077}


def rss_replacement_d3_078(rss_replacement_d2_078):
    feature = _clean(rss_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_078'] = {'inputs': ['rss_replacement_d2_078'], 'func': rss_replacement_d3_078}


def rss_replacement_d3_079(rss_replacement_d2_079):
    feature = _clean(rss_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_079'] = {'inputs': ['rss_replacement_d2_079'], 'func': rss_replacement_d3_079}


def rss_replacement_d3_080(rss_replacement_d2_080):
    feature = _clean(rss_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_080'] = {'inputs': ['rss_replacement_d2_080'], 'func': rss_replacement_d3_080}


def rss_replacement_d3_081(rss_replacement_d2_081):
    feature = _clean(rss_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_081'] = {'inputs': ['rss_replacement_d2_081'], 'func': rss_replacement_d3_081}


def rss_replacement_d3_082(rss_replacement_d2_082):
    feature = _clean(rss_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_082'] = {'inputs': ['rss_replacement_d2_082'], 'func': rss_replacement_d3_082}


def rss_replacement_d3_083(rss_replacement_d2_083):
    feature = _clean(rss_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_083'] = {'inputs': ['rss_replacement_d2_083'], 'func': rss_replacement_d3_083}


def rss_replacement_d3_084(rss_replacement_d2_084):
    feature = _clean(rss_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_084'] = {'inputs': ['rss_replacement_d2_084'], 'func': rss_replacement_d3_084}


def rss_replacement_d3_085(rss_replacement_d2_085):
    feature = _clean(rss_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_085'] = {'inputs': ['rss_replacement_d2_085'], 'func': rss_replacement_d3_085}


def rss_replacement_d3_086(rss_replacement_d2_086):
    feature = _clean(rss_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_086'] = {'inputs': ['rss_replacement_d2_086'], 'func': rss_replacement_d3_086}


def rss_replacement_d3_087(rss_replacement_d2_087):
    feature = _clean(rss_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_087'] = {'inputs': ['rss_replacement_d2_087'], 'func': rss_replacement_d3_087}


def rss_replacement_d3_088(rss_replacement_d2_088):
    feature = _clean(rss_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_088'] = {'inputs': ['rss_replacement_d2_088'], 'func': rss_replacement_d3_088}


def rss_replacement_d3_089(rss_replacement_d2_089):
    feature = _clean(rss_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_089'] = {'inputs': ['rss_replacement_d2_089'], 'func': rss_replacement_d3_089}


def rss_replacement_d3_090(rss_replacement_d2_090):
    feature = _clean(rss_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_090'] = {'inputs': ['rss_replacement_d2_090'], 'func': rss_replacement_d3_090}


def rss_replacement_d3_091(rss_replacement_d2_091):
    feature = _clean(rss_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_091'] = {'inputs': ['rss_replacement_d2_091'], 'func': rss_replacement_d3_091}


def rss_replacement_d3_092(rss_replacement_d2_092):
    feature = _clean(rss_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_092'] = {'inputs': ['rss_replacement_d2_092'], 'func': rss_replacement_d3_092}


def rss_replacement_d3_093(rss_replacement_d2_093):
    feature = _clean(rss_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_093'] = {'inputs': ['rss_replacement_d2_093'], 'func': rss_replacement_d3_093}


def rss_replacement_d3_094(rss_replacement_d2_094):
    feature = _clean(rss_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_094'] = {'inputs': ['rss_replacement_d2_094'], 'func': rss_replacement_d3_094}


def rss_replacement_d3_095(rss_replacement_d2_095):
    feature = _clean(rss_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_095'] = {'inputs': ['rss_replacement_d2_095'], 'func': rss_replacement_d3_095}


def rss_replacement_d3_096(rss_replacement_d2_096):
    feature = _clean(rss_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_096'] = {'inputs': ['rss_replacement_d2_096'], 'func': rss_replacement_d3_096}


def rss_replacement_d3_097(rss_replacement_d2_097):
    feature = _clean(rss_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_097'] = {'inputs': ['rss_replacement_d2_097'], 'func': rss_replacement_d3_097}


def rss_replacement_d3_098(rss_replacement_d2_098):
    feature = _clean(rss_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_098'] = {'inputs': ['rss_replacement_d2_098'], 'func': rss_replacement_d3_098}


def rss_replacement_d3_099(rss_replacement_d2_099):
    feature = _clean(rss_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_099'] = {'inputs': ['rss_replacement_d2_099'], 'func': rss_replacement_d3_099}


def rss_replacement_d3_100(rss_replacement_d2_100):
    feature = _clean(rss_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_100'] = {'inputs': ['rss_replacement_d2_100'], 'func': rss_replacement_d3_100}


def rss_replacement_d3_101(rss_replacement_d2_101):
    feature = _clean(rss_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_101'] = {'inputs': ['rss_replacement_d2_101'], 'func': rss_replacement_d3_101}


def rss_replacement_d3_102(rss_replacement_d2_102):
    feature = _clean(rss_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_102'] = {'inputs': ['rss_replacement_d2_102'], 'func': rss_replacement_d3_102}


def rss_replacement_d3_103(rss_replacement_d2_103):
    feature = _clean(rss_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_103'] = {'inputs': ['rss_replacement_d2_103'], 'func': rss_replacement_d3_103}


def rss_replacement_d3_104(rss_replacement_d2_104):
    feature = _clean(rss_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_104'] = {'inputs': ['rss_replacement_d2_104'], 'func': rss_replacement_d3_104}


def rss_replacement_d3_105(rss_replacement_d2_105):
    feature = _clean(rss_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_105'] = {'inputs': ['rss_replacement_d2_105'], 'func': rss_replacement_d3_105}


def rss_replacement_d3_106(rss_replacement_d2_106):
    feature = _clean(rss_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_106'] = {'inputs': ['rss_replacement_d2_106'], 'func': rss_replacement_d3_106}


def rss_replacement_d3_107(rss_replacement_d2_107):
    feature = _clean(rss_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_107'] = {'inputs': ['rss_replacement_d2_107'], 'func': rss_replacement_d3_107}


def rss_replacement_d3_108(rss_replacement_d2_108):
    feature = _clean(rss_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_108'] = {'inputs': ['rss_replacement_d2_108'], 'func': rss_replacement_d3_108}


def rss_replacement_d3_109(rss_replacement_d2_109):
    feature = _clean(rss_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_109'] = {'inputs': ['rss_replacement_d2_109'], 'func': rss_replacement_d3_109}


def rss_replacement_d3_110(rss_replacement_d2_110):
    feature = _clean(rss_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_110'] = {'inputs': ['rss_replacement_d2_110'], 'func': rss_replacement_d3_110}


def rss_replacement_d3_111(rss_replacement_d2_111):
    feature = _clean(rss_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_111'] = {'inputs': ['rss_replacement_d2_111'], 'func': rss_replacement_d3_111}


def rss_replacement_d3_112(rss_replacement_d2_112):
    feature = _clean(rss_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_112'] = {'inputs': ['rss_replacement_d2_112'], 'func': rss_replacement_d3_112}


def rss_replacement_d3_113(rss_replacement_d2_113):
    feature = _clean(rss_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_113'] = {'inputs': ['rss_replacement_d2_113'], 'func': rss_replacement_d3_113}


def rss_replacement_d3_114(rss_replacement_d2_114):
    feature = _clean(rss_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_114'] = {'inputs': ['rss_replacement_d2_114'], 'func': rss_replacement_d3_114}


def rss_replacement_d3_115(rss_replacement_d2_115):
    feature = _clean(rss_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_115'] = {'inputs': ['rss_replacement_d2_115'], 'func': rss_replacement_d3_115}


def rss_replacement_d3_116(rss_replacement_d2_116):
    feature = _clean(rss_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_116'] = {'inputs': ['rss_replacement_d2_116'], 'func': rss_replacement_d3_116}


def rss_replacement_d3_117(rss_replacement_d2_117):
    feature = _clean(rss_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_117'] = {'inputs': ['rss_replacement_d2_117'], 'func': rss_replacement_d3_117}


def rss_replacement_d3_118(rss_replacement_d2_118):
    feature = _clean(rss_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_118'] = {'inputs': ['rss_replacement_d2_118'], 'func': rss_replacement_d3_118}


def rss_replacement_d3_119(rss_replacement_d2_119):
    feature = _clean(rss_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_119'] = {'inputs': ['rss_replacement_d2_119'], 'func': rss_replacement_d3_119}


def rss_replacement_d3_120(rss_replacement_d2_120):
    feature = _clean(rss_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_120'] = {'inputs': ['rss_replacement_d2_120'], 'func': rss_replacement_d3_120}


def rss_replacement_d3_121(rss_replacement_d2_121):
    feature = _clean(rss_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_121'] = {'inputs': ['rss_replacement_d2_121'], 'func': rss_replacement_d3_121}


def rss_replacement_d3_122(rss_replacement_d2_122):
    feature = _clean(rss_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_122'] = {'inputs': ['rss_replacement_d2_122'], 'func': rss_replacement_d3_122}


def rss_replacement_d3_123(rss_replacement_d2_123):
    feature = _clean(rss_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_123'] = {'inputs': ['rss_replacement_d2_123'], 'func': rss_replacement_d3_123}


def rss_replacement_d3_124(rss_replacement_d2_124):
    feature = _clean(rss_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_124'] = {'inputs': ['rss_replacement_d2_124'], 'func': rss_replacement_d3_124}


def rss_replacement_d3_125(rss_replacement_d2_125):
    feature = _clean(rss_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_125'] = {'inputs': ['rss_replacement_d2_125'], 'func': rss_replacement_d3_125}


def rss_replacement_d3_126(rss_replacement_d2_126):
    feature = _clean(rss_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_126'] = {'inputs': ['rss_replacement_d2_126'], 'func': rss_replacement_d3_126}


def rss_replacement_d3_127(rss_replacement_d2_127):
    feature = _clean(rss_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_127'] = {'inputs': ['rss_replacement_d2_127'], 'func': rss_replacement_d3_127}


def rss_replacement_d3_128(rss_replacement_d2_128):
    feature = _clean(rss_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_128'] = {'inputs': ['rss_replacement_d2_128'], 'func': rss_replacement_d3_128}


def rss_replacement_d3_129(rss_replacement_d2_129):
    feature = _clean(rss_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_129'] = {'inputs': ['rss_replacement_d2_129'], 'func': rss_replacement_d3_129}


def rss_replacement_d3_130(rss_replacement_d2_130):
    feature = _clean(rss_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_130'] = {'inputs': ['rss_replacement_d2_130'], 'func': rss_replacement_d3_130}


def rss_replacement_d3_131(rss_replacement_d2_131):
    feature = _clean(rss_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_131'] = {'inputs': ['rss_replacement_d2_131'], 'func': rss_replacement_d3_131}


def rss_replacement_d3_132(rss_replacement_d2_132):
    feature = _clean(rss_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_132'] = {'inputs': ['rss_replacement_d2_132'], 'func': rss_replacement_d3_132}


def rss_replacement_d3_133(rss_replacement_d2_133):
    feature = _clean(rss_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_133'] = {'inputs': ['rss_replacement_d2_133'], 'func': rss_replacement_d3_133}


def rss_replacement_d3_134(rss_replacement_d2_134):
    feature = _clean(rss_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_134'] = {'inputs': ['rss_replacement_d2_134'], 'func': rss_replacement_d3_134}


def rss_replacement_d3_135(rss_replacement_d2_135):
    feature = _clean(rss_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_135'] = {'inputs': ['rss_replacement_d2_135'], 'func': rss_replacement_d3_135}


def rss_replacement_d3_136(rss_replacement_d2_136):
    feature = _clean(rss_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_136'] = {'inputs': ['rss_replacement_d2_136'], 'func': rss_replacement_d3_136}


def rss_replacement_d3_137(rss_replacement_d2_137):
    feature = _clean(rss_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_137'] = {'inputs': ['rss_replacement_d2_137'], 'func': rss_replacement_d3_137}


def rss_replacement_d3_138(rss_replacement_d2_138):
    feature = _clean(rss_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_138'] = {'inputs': ['rss_replacement_d2_138'], 'func': rss_replacement_d3_138}


def rss_replacement_d3_139(rss_replacement_d2_139):
    feature = _clean(rss_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_139'] = {'inputs': ['rss_replacement_d2_139'], 'func': rss_replacement_d3_139}


def rss_replacement_d3_140(rss_replacement_d2_140):
    feature = _clean(rss_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_140'] = {'inputs': ['rss_replacement_d2_140'], 'func': rss_replacement_d3_140}


def rss_replacement_d3_141(rss_replacement_d2_141):
    feature = _clean(rss_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_141'] = {'inputs': ['rss_replacement_d2_141'], 'func': rss_replacement_d3_141}


def rss_replacement_d3_142(rss_replacement_d2_142):
    feature = _clean(rss_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_142'] = {'inputs': ['rss_replacement_d2_142'], 'func': rss_replacement_d3_142}


def rss_replacement_d3_143(rss_replacement_d2_143):
    feature = _clean(rss_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_143'] = {'inputs': ['rss_replacement_d2_143'], 'func': rss_replacement_d3_143}


def rss_replacement_d3_144(rss_replacement_d2_144):
    feature = _clean(rss_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_144'] = {'inputs': ['rss_replacement_d2_144'], 'func': rss_replacement_d3_144}


def rss_replacement_d3_145(rss_replacement_d2_145):
    feature = _clean(rss_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_145'] = {'inputs': ['rss_replacement_d2_145'], 'func': rss_replacement_d3_145}


def rss_replacement_d3_146(rss_replacement_d2_146):
    feature = _clean(rss_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_146'] = {'inputs': ['rss_replacement_d2_146'], 'func': rss_replacement_d3_146}


def rss_replacement_d3_147(rss_replacement_d2_147):
    feature = _clean(rss_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_147'] = {'inputs': ['rss_replacement_d2_147'], 'func': rss_replacement_d3_147}


def rss_replacement_d3_148(rss_replacement_d2_148):
    feature = _clean(rss_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_148'] = {'inputs': ['rss_replacement_d2_148'], 'func': rss_replacement_d3_148}


def rss_replacement_d3_149(rss_replacement_d2_149):
    feature = _clean(rss_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_149'] = {'inputs': ['rss_replacement_d2_149'], 'func': rss_replacement_d3_149}


def rss_replacement_d3_150(rss_replacement_d2_150):
    feature = _clean(rss_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_150'] = {'inputs': ['rss_replacement_d2_150'], 'func': rss_replacement_d3_150}


def rss_replacement_d3_151(rss_replacement_d2_151):
    feature = _clean(rss_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RSS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rss_replacement_d3_151'] = {'inputs': ['rss_replacement_d2_151'], 'func': rss_replacement_d3_151}


# Third-derivative extensions for repaired first-base features.
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rss_base_universe_d3_001_rss_002_dividend_suspension_density_42(rss_base_universe_d2_001_rss_002_dividend_suspension_density_42):
    return _base_universe_d3(rss_base_universe_d2_001_rss_002_dividend_suspension_density_42, 1)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_001_rss_002_dividend_suspension_density_42'] = {'inputs': ['rss_base_universe_d2_001_rss_002_dividend_suspension_density_42'], 'func': rss_base_universe_d3_001_rss_002_dividend_suspension_density_42}


def rss_base_universe_d3_002_rss_003_reverse_split_density_63(rss_base_universe_d2_002_rss_003_reverse_split_density_63):
    return _base_universe_d3(rss_base_universe_d2_002_rss_003_reverse_split_density_63, 2)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_002_rss_003_reverse_split_density_63'] = {'inputs': ['rss_base_universe_d2_002_rss_003_reverse_split_density_63'], 'func': rss_base_universe_d3_002_rss_003_reverse_split_density_63}


def rss_base_universe_d3_003_rss_004_event_density_z_84(rss_base_universe_d2_003_rss_004_event_density_z_84):
    return _base_universe_d3(rss_base_universe_d2_003_rss_004_event_density_z_84, 3)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_003_rss_004_event_density_z_84'] = {'inputs': ['rss_base_universe_d2_003_rss_004_event_density_z_84'], 'func': rss_base_universe_d3_003_rss_004_event_density_z_84}


def rss_base_universe_d3_004_rss_005_going_concern_persistence_126(rss_base_universe_d2_004_rss_005_going_concern_persistence_126):
    return _base_universe_d3(rss_base_universe_d2_004_rss_005_going_concern_persistence_126, 4)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_004_rss_005_going_concern_persistence_126'] = {'inputs': ['rss_base_universe_d2_004_rss_005_going_concern_persistence_126'], 'func': rss_base_universe_d3_004_rss_005_going_concern_persistence_126}


def rss_base_universe_d3_005_rss_006_delisting_notice_density_189(rss_base_universe_d2_005_rss_006_delisting_notice_density_189):
    return _base_universe_d3(rss_base_universe_d2_005_rss_006_delisting_notice_density_189, 5)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_005_rss_006_delisting_notice_density_189'] = {'inputs': ['rss_base_universe_d2_005_rss_006_delisting_notice_density_189'], 'func': rss_base_universe_d3_005_rss_006_delisting_notice_density_189}


def rss_base_universe_d3_006_rss_008_dividend_cut_density_378(rss_base_universe_d2_006_rss_008_dividend_cut_density_378):
    return _base_universe_d3(rss_base_universe_d2_006_rss_008_dividend_cut_density_378, 6)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_006_rss_008_dividend_cut_density_378'] = {'inputs': ['rss_base_universe_d2_006_rss_008_dividend_cut_density_378'], 'func': rss_base_universe_d3_006_rss_008_dividend_cut_density_378}


def rss_base_universe_d3_007_rss_009_dividend_suspension_density_504(rss_base_universe_d2_007_rss_009_dividend_suspension_density_504):
    return _base_universe_d3(rss_base_universe_d2_007_rss_009_dividend_suspension_density_504, 7)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_007_rss_009_dividend_suspension_density_504'] = {'inputs': ['rss_base_universe_d2_007_rss_009_dividend_suspension_density_504'], 'func': rss_base_universe_d3_007_rss_009_dividend_suspension_density_504}


def rss_base_universe_d3_008_rss_010_reverse_split_density_756(rss_base_universe_d2_008_rss_010_reverse_split_density_756):
    return _base_universe_d3(rss_base_universe_d2_008_rss_010_reverse_split_density_756, 8)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_008_rss_010_reverse_split_density_756'] = {'inputs': ['rss_base_universe_d2_008_rss_010_reverse_split_density_756'], 'func': rss_base_universe_d3_008_rss_010_reverse_split_density_756}


def rss_base_universe_d3_009_rss_011_event_density_z_1008(rss_base_universe_d2_009_rss_011_event_density_z_1008):
    return _base_universe_d3(rss_base_universe_d2_009_rss_011_event_density_z_1008, 9)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_009_rss_011_event_density_z_1008'] = {'inputs': ['rss_base_universe_d2_009_rss_011_event_density_z_1008'], 'func': rss_base_universe_d3_009_rss_011_event_density_z_1008}


def rss_base_universe_d3_010_rss_012_going_concern_persistence_1260(rss_base_universe_d2_010_rss_012_going_concern_persistence_1260):
    return _base_universe_d3(rss_base_universe_d2_010_rss_012_going_concern_persistence_1260, 10)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_010_rss_012_going_concern_persistence_1260'] = {'inputs': ['rss_base_universe_d2_010_rss_012_going_concern_persistence_1260'], 'func': rss_base_universe_d3_010_rss_012_going_concern_persistence_1260}


def rss_base_universe_d3_011_rss_015_dividend_cut_density_252(rss_base_universe_d2_011_rss_015_dividend_cut_density_252):
    return _base_universe_d3(rss_base_universe_d2_011_rss_015_dividend_cut_density_252, 11)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_011_rss_015_dividend_cut_density_252'] = {'inputs': ['rss_base_universe_d2_011_rss_015_dividend_cut_density_252'], 'func': rss_base_universe_d3_011_rss_015_dividend_cut_density_252}


def rss_base_universe_d3_012_rss_018_event_density_z_63(rss_base_universe_d2_012_rss_018_event_density_z_63):
    return _base_universe_d3(rss_base_universe_d2_012_rss_018_event_density_z_63, 12)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_012_rss_018_event_density_z_63'] = {'inputs': ['rss_base_universe_d2_012_rss_018_event_density_z_63'], 'func': rss_base_universe_d3_012_rss_018_event_density_z_63}


def rss_base_universe_d3_013_rss_020_delisting_notice_density_126(rss_base_universe_d2_013_rss_020_delisting_notice_density_126):
    return _base_universe_d3(rss_base_universe_d2_013_rss_020_delisting_notice_density_126, 13)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_013_rss_020_delisting_notice_density_126'] = {'inputs': ['rss_base_universe_d2_013_rss_020_delisting_notice_density_126'], 'func': rss_base_universe_d3_013_rss_020_delisting_notice_density_126}


def rss_base_universe_d3_014_rss_026_going_concern_persistence_1008(rss_base_universe_d2_014_rss_026_going_concern_persistence_1008):
    return _base_universe_d3(rss_base_universe_d2_014_rss_026_going_concern_persistence_1008, 14)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_014_rss_026_going_concern_persistence_1008'] = {'inputs': ['rss_base_universe_d2_014_rss_026_going_concern_persistence_1008'], 'func': rss_base_universe_d3_014_rss_026_going_concern_persistence_1008}


def rss_base_universe_d3_015_rss_027_delisting_notice_density_1260(rss_base_universe_d2_015_rss_027_delisting_notice_density_1260):
    return _base_universe_d3(rss_base_universe_d2_015_rss_027_delisting_notice_density_1260, 15)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_015_rss_027_delisting_notice_density_1260'] = {'inputs': ['rss_base_universe_d2_015_rss_027_delisting_notice_density_1260'], 'func': rss_base_universe_d3_015_rss_027_delisting_notice_density_1260}


def rss_base_universe_d3_016_rss_032_event_density_z_42(rss_base_universe_d2_016_rss_032_event_density_z_42):
    return _base_universe_d3(rss_base_universe_d2_016_rss_032_event_density_z_42, 16)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_016_rss_032_event_density_z_42'] = {'inputs': ['rss_base_universe_d2_016_rss_032_event_density_z_42'], 'func': rss_base_universe_d3_016_rss_032_event_density_z_42}


def rss_base_universe_d3_017_rss_033_going_concern_persistence_63(rss_base_universe_d2_017_rss_033_going_concern_persistence_63):
    return _base_universe_d3(rss_base_universe_d2_017_rss_033_going_concern_persistence_63, 17)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_017_rss_033_going_concern_persistence_63'] = {'inputs': ['rss_base_universe_d2_017_rss_033_going_concern_persistence_63'], 'func': rss_base_universe_d3_017_rss_033_going_concern_persistence_63}


def rss_base_universe_d3_018_rss_034_delisting_notice_density_84(rss_base_universe_d2_018_rss_034_delisting_notice_density_84):
    return _base_universe_d3(rss_base_universe_d2_018_rss_034_delisting_notice_density_84, 18)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_018_rss_034_delisting_notice_density_84'] = {'inputs': ['rss_base_universe_d2_018_rss_034_delisting_notice_density_84'], 'func': rss_base_universe_d3_018_rss_034_delisting_notice_density_84}


def rss_base_universe_d3_019_rss_039_event_density_z_504(rss_base_universe_d2_019_rss_039_event_density_z_504):
    return _base_universe_d3(rss_base_universe_d2_019_rss_039_event_density_z_504, 19)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_019_rss_039_event_density_z_504'] = {'inputs': ['rss_base_universe_d2_019_rss_039_event_density_z_504'], 'func': rss_base_universe_d3_019_rss_039_event_density_z_504}


def rss_base_universe_d3_020_rss_040_going_concern_persistence_756(rss_base_universe_d2_020_rss_040_going_concern_persistence_756):
    return _base_universe_d3(rss_base_universe_d2_020_rss_040_going_concern_persistence_756, 20)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_020_rss_040_going_concern_persistence_756'] = {'inputs': ['rss_base_universe_d2_020_rss_040_going_concern_persistence_756'], 'func': rss_base_universe_d3_020_rss_040_going_concern_persistence_756}


def rss_base_universe_d3_021_rss_041_delisting_notice_density_1008(rss_base_universe_d2_021_rss_041_delisting_notice_density_1008):
    return _base_universe_d3(rss_base_universe_d2_021_rss_041_delisting_notice_density_1008, 21)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_021_rss_041_delisting_notice_density_1008'] = {'inputs': ['rss_base_universe_d2_021_rss_041_delisting_notice_density_1008'], 'func': rss_base_universe_d3_021_rss_041_delisting_notice_density_1008}


def rss_base_universe_d3_022_rss_046_event_density_z_21(rss_base_universe_d2_022_rss_046_event_density_z_21):
    return _base_universe_d3(rss_base_universe_d2_022_rss_046_event_density_z_21, 22)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_022_rss_046_event_density_z_21'] = {'inputs': ['rss_base_universe_d2_022_rss_046_event_density_z_21'], 'func': rss_base_universe_d3_022_rss_046_event_density_z_21}


def rss_base_universe_d3_023_rss_047_going_concern_persistence_42(rss_base_universe_d2_023_rss_047_going_concern_persistence_42):
    return _base_universe_d3(rss_base_universe_d2_023_rss_047_going_concern_persistence_42, 23)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_023_rss_047_going_concern_persistence_42'] = {'inputs': ['rss_base_universe_d2_023_rss_047_going_concern_persistence_42'], 'func': rss_base_universe_d3_023_rss_047_going_concern_persistence_42}


def rss_base_universe_d3_024_rss_053_event_density_z_378(rss_base_universe_d2_024_rss_053_event_density_z_378):
    return _base_universe_d3(rss_base_universe_d2_024_rss_053_event_density_z_378, 24)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_024_rss_053_event_density_z_378'] = {'inputs': ['rss_base_universe_d2_024_rss_053_event_density_z_378'], 'func': rss_base_universe_d3_024_rss_053_event_density_z_378}


def rss_base_universe_d3_025_rss_054_going_concern_persistence_504(rss_base_universe_d2_025_rss_054_going_concern_persistence_504):
    return _base_universe_d3(rss_base_universe_d2_025_rss_054_going_concern_persistence_504, 25)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_025_rss_054_going_concern_persistence_504'] = {'inputs': ['rss_base_universe_d2_025_rss_054_going_concern_persistence_504'], 'func': rss_base_universe_d3_025_rss_054_going_concern_persistence_504}


def rss_base_universe_d3_026_rss_060_event_density_z_252(rss_base_universe_d2_026_rss_060_event_density_z_252):
    return _base_universe_d3(rss_base_universe_d2_026_rss_060_event_density_z_252, 26)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_026_rss_060_event_density_z_252'] = {'inputs': ['rss_base_universe_d2_026_rss_060_event_density_z_252'], 'func': rss_base_universe_d3_026_rss_060_event_density_z_252}


def rss_base_universe_d3_027_rss_061_going_concern_persistence_21(rss_base_universe_d2_027_rss_061_going_concern_persistence_21):
    return _base_universe_d3(rss_base_universe_d2_027_rss_061_going_concern_persistence_21, 27)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_027_rss_061_going_concern_persistence_21'] = {'inputs': ['rss_base_universe_d2_027_rss_061_going_concern_persistence_21'], 'func': rss_base_universe_d3_027_rss_061_going_concern_persistence_21}


def rss_base_universe_d3_028_rss_068_going_concern_persistence_378(rss_base_universe_d2_028_rss_068_going_concern_persistence_378):
    return _base_universe_d3(rss_base_universe_d2_028_rss_068_going_concern_persistence_378, 28)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_028_rss_068_going_concern_persistence_378'] = {'inputs': ['rss_base_universe_d2_028_rss_068_going_concern_persistence_378'], 'func': rss_base_universe_d3_028_rss_068_going_concern_persistence_378}


def rss_base_universe_d3_029_rss_075_going_concern_persistence_252(rss_base_universe_d2_029_rss_075_going_concern_persistence_252):
    return _base_universe_d3(rss_base_universe_d2_029_rss_075_going_concern_persistence_252, 29)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_029_rss_075_going_concern_persistence_252'] = {'inputs': ['rss_base_universe_d2_029_rss_075_going_concern_persistence_252'], 'func': rss_base_universe_d3_029_rss_075_going_concern_persistence_252}


def rss_base_universe_d3_030_rss_basefill_007(rss_base_universe_d2_030_rss_basefill_007):
    return _base_universe_d3(rss_base_universe_d2_030_rss_basefill_007, 30)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_030_rss_basefill_007'] = {'inputs': ['rss_base_universe_d2_030_rss_basefill_007'], 'func': rss_base_universe_d3_030_rss_basefill_007}


def rss_base_universe_d3_031_rss_basefill_014(rss_base_universe_d2_031_rss_basefill_014):
    return _base_universe_d3(rss_base_universe_d2_031_rss_basefill_014, 31)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_031_rss_basefill_014'] = {'inputs': ['rss_base_universe_d2_031_rss_basefill_014'], 'func': rss_base_universe_d3_031_rss_basefill_014}


def rss_base_universe_d3_032_rss_basefill_016(rss_base_universe_d2_032_rss_basefill_016):
    return _base_universe_d3(rss_base_universe_d2_032_rss_basefill_016, 32)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_032_rss_basefill_016'] = {'inputs': ['rss_base_universe_d2_032_rss_basefill_016'], 'func': rss_base_universe_d3_032_rss_basefill_016}


def rss_base_universe_d3_033_rss_basefill_017(rss_base_universe_d2_033_rss_basefill_017):
    return _base_universe_d3(rss_base_universe_d2_033_rss_basefill_017, 33)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_033_rss_basefill_017'] = {'inputs': ['rss_base_universe_d2_033_rss_basefill_017'], 'func': rss_base_universe_d3_033_rss_basefill_017}


def rss_base_universe_d3_034_rss_basefill_021(rss_base_universe_d2_034_rss_basefill_021):
    return _base_universe_d3(rss_base_universe_d2_034_rss_basefill_021, 34)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_034_rss_basefill_021'] = {'inputs': ['rss_base_universe_d2_034_rss_basefill_021'], 'func': rss_base_universe_d3_034_rss_basefill_021}


def rss_base_universe_d3_035_rss_basefill_022(rss_base_universe_d2_035_rss_basefill_022):
    return _base_universe_d3(rss_base_universe_d2_035_rss_basefill_022, 35)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_035_rss_basefill_022'] = {'inputs': ['rss_base_universe_d2_035_rss_basefill_022'], 'func': rss_base_universe_d3_035_rss_basefill_022}


def rss_base_universe_d3_036_rss_basefill_023(rss_base_universe_d2_036_rss_basefill_023):
    return _base_universe_d3(rss_base_universe_d2_036_rss_basefill_023, 36)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_036_rss_basefill_023'] = {'inputs': ['rss_base_universe_d2_036_rss_basefill_023'], 'func': rss_base_universe_d3_036_rss_basefill_023}


def rss_base_universe_d3_037_rss_basefill_024(rss_base_universe_d2_037_rss_basefill_024):
    return _base_universe_d3(rss_base_universe_d2_037_rss_basefill_024, 37)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_037_rss_basefill_024'] = {'inputs': ['rss_base_universe_d2_037_rss_basefill_024'], 'func': rss_base_universe_d3_037_rss_basefill_024}


def rss_base_universe_d3_038_rss_basefill_028(rss_base_universe_d2_038_rss_basefill_028):
    return _base_universe_d3(rss_base_universe_d2_038_rss_basefill_028, 38)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_038_rss_basefill_028'] = {'inputs': ['rss_base_universe_d2_038_rss_basefill_028'], 'func': rss_base_universe_d3_038_rss_basefill_028}


def rss_base_universe_d3_039_rss_basefill_029(rss_base_universe_d2_039_rss_basefill_029):
    return _base_universe_d3(rss_base_universe_d2_039_rss_basefill_029, 39)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_039_rss_basefill_029'] = {'inputs': ['rss_base_universe_d2_039_rss_basefill_029'], 'func': rss_base_universe_d3_039_rss_basefill_029}


def rss_base_universe_d3_040_rss_basefill_030(rss_base_universe_d2_040_rss_basefill_030):
    return _base_universe_d3(rss_base_universe_d2_040_rss_basefill_030, 40)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_040_rss_basefill_030'] = {'inputs': ['rss_base_universe_d2_040_rss_basefill_030'], 'func': rss_base_universe_d3_040_rss_basefill_030}


def rss_base_universe_d3_041_rss_basefill_031(rss_base_universe_d2_041_rss_basefill_031):
    return _base_universe_d3(rss_base_universe_d2_041_rss_basefill_031, 41)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_041_rss_basefill_031'] = {'inputs': ['rss_base_universe_d2_041_rss_basefill_031'], 'func': rss_base_universe_d3_041_rss_basefill_031}


def rss_base_universe_d3_042_rss_basefill_035(rss_base_universe_d2_042_rss_basefill_035):
    return _base_universe_d3(rss_base_universe_d2_042_rss_basefill_035, 42)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_042_rss_basefill_035'] = {'inputs': ['rss_base_universe_d2_042_rss_basefill_035'], 'func': rss_base_universe_d3_042_rss_basefill_035}


def rss_base_universe_d3_043_rss_basefill_036(rss_base_universe_d2_043_rss_basefill_036):
    return _base_universe_d3(rss_base_universe_d2_043_rss_basefill_036, 43)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_043_rss_basefill_036'] = {'inputs': ['rss_base_universe_d2_043_rss_basefill_036'], 'func': rss_base_universe_d3_043_rss_basefill_036}


def rss_base_universe_d3_044_rss_basefill_037(rss_base_universe_d2_044_rss_basefill_037):
    return _base_universe_d3(rss_base_universe_d2_044_rss_basefill_037, 44)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_044_rss_basefill_037'] = {'inputs': ['rss_base_universe_d2_044_rss_basefill_037'], 'func': rss_base_universe_d3_044_rss_basefill_037}


def rss_base_universe_d3_045_rss_basefill_038(rss_base_universe_d2_045_rss_basefill_038):
    return _base_universe_d3(rss_base_universe_d2_045_rss_basefill_038, 45)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_045_rss_basefill_038'] = {'inputs': ['rss_base_universe_d2_045_rss_basefill_038'], 'func': rss_base_universe_d3_045_rss_basefill_038}


def rss_base_universe_d3_046_rss_basefill_042(rss_base_universe_d2_046_rss_basefill_042):
    return _base_universe_d3(rss_base_universe_d2_046_rss_basefill_042, 46)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_046_rss_basefill_042'] = {'inputs': ['rss_base_universe_d2_046_rss_basefill_042'], 'func': rss_base_universe_d3_046_rss_basefill_042}


def rss_base_universe_d3_047_rss_basefill_043(rss_base_universe_d2_047_rss_basefill_043):
    return _base_universe_d3(rss_base_universe_d2_047_rss_basefill_043, 47)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_047_rss_basefill_043'] = {'inputs': ['rss_base_universe_d2_047_rss_basefill_043'], 'func': rss_base_universe_d3_047_rss_basefill_043}


def rss_base_universe_d3_048_rss_basefill_044(rss_base_universe_d2_048_rss_basefill_044):
    return _base_universe_d3(rss_base_universe_d2_048_rss_basefill_044, 48)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_048_rss_basefill_044'] = {'inputs': ['rss_base_universe_d2_048_rss_basefill_044'], 'func': rss_base_universe_d3_048_rss_basefill_044}


def rss_base_universe_d3_049_rss_basefill_045(rss_base_universe_d2_049_rss_basefill_045):
    return _base_universe_d3(rss_base_universe_d2_049_rss_basefill_045, 49)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_049_rss_basefill_045'] = {'inputs': ['rss_base_universe_d2_049_rss_basefill_045'], 'func': rss_base_universe_d3_049_rss_basefill_045}


def rss_base_universe_d3_050_rss_basefill_048(rss_base_universe_d2_050_rss_basefill_048):
    return _base_universe_d3(rss_base_universe_d2_050_rss_basefill_048, 50)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_050_rss_basefill_048'] = {'inputs': ['rss_base_universe_d2_050_rss_basefill_048'], 'func': rss_base_universe_d3_050_rss_basefill_048}


def rss_base_universe_d3_051_rss_basefill_049(rss_base_universe_d2_051_rss_basefill_049):
    return _base_universe_d3(rss_base_universe_d2_051_rss_basefill_049, 51)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_051_rss_basefill_049'] = {'inputs': ['rss_base_universe_d2_051_rss_basefill_049'], 'func': rss_base_universe_d3_051_rss_basefill_049}


def rss_base_universe_d3_052_rss_basefill_050(rss_base_universe_d2_052_rss_basefill_050):
    return _base_universe_d3(rss_base_universe_d2_052_rss_basefill_050, 52)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_052_rss_basefill_050'] = {'inputs': ['rss_base_universe_d2_052_rss_basefill_050'], 'func': rss_base_universe_d3_052_rss_basefill_050}


def rss_base_universe_d3_053_rss_basefill_051(rss_base_universe_d2_053_rss_basefill_051):
    return _base_universe_d3(rss_base_universe_d2_053_rss_basefill_051, 53)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_053_rss_basefill_051'] = {'inputs': ['rss_base_universe_d2_053_rss_basefill_051'], 'func': rss_base_universe_d3_053_rss_basefill_051}


def rss_base_universe_d3_054_rss_basefill_052(rss_base_universe_d2_054_rss_basefill_052):
    return _base_universe_d3(rss_base_universe_d2_054_rss_basefill_052, 54)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_054_rss_basefill_052'] = {'inputs': ['rss_base_universe_d2_054_rss_basefill_052'], 'func': rss_base_universe_d3_054_rss_basefill_052}


def rss_base_universe_d3_055_rss_basefill_055(rss_base_universe_d2_055_rss_basefill_055):
    return _base_universe_d3(rss_base_universe_d2_055_rss_basefill_055, 55)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_055_rss_basefill_055'] = {'inputs': ['rss_base_universe_d2_055_rss_basefill_055'], 'func': rss_base_universe_d3_055_rss_basefill_055}


def rss_base_universe_d3_056_rss_basefill_056(rss_base_universe_d2_056_rss_basefill_056):
    return _base_universe_d3(rss_base_universe_d2_056_rss_basefill_056, 56)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_056_rss_basefill_056'] = {'inputs': ['rss_base_universe_d2_056_rss_basefill_056'], 'func': rss_base_universe_d3_056_rss_basefill_056}


def rss_base_universe_d3_057_rss_basefill_057(rss_base_universe_d2_057_rss_basefill_057):
    return _base_universe_d3(rss_base_universe_d2_057_rss_basefill_057, 57)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_057_rss_basefill_057'] = {'inputs': ['rss_base_universe_d2_057_rss_basefill_057'], 'func': rss_base_universe_d3_057_rss_basefill_057}


def rss_base_universe_d3_058_rss_basefill_058(rss_base_universe_d2_058_rss_basefill_058):
    return _base_universe_d3(rss_base_universe_d2_058_rss_basefill_058, 58)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_058_rss_basefill_058'] = {'inputs': ['rss_base_universe_d2_058_rss_basefill_058'], 'func': rss_base_universe_d3_058_rss_basefill_058}


def rss_base_universe_d3_059_rss_basefill_059(rss_base_universe_d2_059_rss_basefill_059):
    return _base_universe_d3(rss_base_universe_d2_059_rss_basefill_059, 59)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_059_rss_basefill_059'] = {'inputs': ['rss_base_universe_d2_059_rss_basefill_059'], 'func': rss_base_universe_d3_059_rss_basefill_059}


def rss_base_universe_d3_060_rss_basefill_062(rss_base_universe_d2_060_rss_basefill_062):
    return _base_universe_d3(rss_base_universe_d2_060_rss_basefill_062, 60)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_060_rss_basefill_062'] = {'inputs': ['rss_base_universe_d2_060_rss_basefill_062'], 'func': rss_base_universe_d3_060_rss_basefill_062}


def rss_base_universe_d3_061_rss_basefill_063(rss_base_universe_d2_061_rss_basefill_063):
    return _base_universe_d3(rss_base_universe_d2_061_rss_basefill_063, 61)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_061_rss_basefill_063'] = {'inputs': ['rss_base_universe_d2_061_rss_basefill_063'], 'func': rss_base_universe_d3_061_rss_basefill_063}


def rss_base_universe_d3_062_rss_basefill_064(rss_base_universe_d2_062_rss_basefill_064):
    return _base_universe_d3(rss_base_universe_d2_062_rss_basefill_064, 62)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_062_rss_basefill_064'] = {'inputs': ['rss_base_universe_d2_062_rss_basefill_064'], 'func': rss_base_universe_d3_062_rss_basefill_064}


def rss_base_universe_d3_063_rss_basefill_065(rss_base_universe_d2_063_rss_basefill_065):
    return _base_universe_d3(rss_base_universe_d2_063_rss_basefill_065, 63)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_063_rss_basefill_065'] = {'inputs': ['rss_base_universe_d2_063_rss_basefill_065'], 'func': rss_base_universe_d3_063_rss_basefill_065}


def rss_base_universe_d3_064_rss_basefill_066(rss_base_universe_d2_064_rss_basefill_066):
    return _base_universe_d3(rss_base_universe_d2_064_rss_basefill_066, 64)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_064_rss_basefill_066'] = {'inputs': ['rss_base_universe_d2_064_rss_basefill_066'], 'func': rss_base_universe_d3_064_rss_basefill_066}


def rss_base_universe_d3_065_rss_basefill_067(rss_base_universe_d2_065_rss_basefill_067):
    return _base_universe_d3(rss_base_universe_d2_065_rss_basefill_067, 65)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_065_rss_basefill_067'] = {'inputs': ['rss_base_universe_d2_065_rss_basefill_067'], 'func': rss_base_universe_d3_065_rss_basefill_067}


def rss_base_universe_d3_066_rss_basefill_069(rss_base_universe_d2_066_rss_basefill_069):
    return _base_universe_d3(rss_base_universe_d2_066_rss_basefill_069, 66)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_066_rss_basefill_069'] = {'inputs': ['rss_base_universe_d2_066_rss_basefill_069'], 'func': rss_base_universe_d3_066_rss_basefill_069}


def rss_base_universe_d3_067_rss_basefill_070(rss_base_universe_d2_067_rss_basefill_070):
    return _base_universe_d3(rss_base_universe_d2_067_rss_basefill_070, 67)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_067_rss_basefill_070'] = {'inputs': ['rss_base_universe_d2_067_rss_basefill_070'], 'func': rss_base_universe_d3_067_rss_basefill_070}


def rss_base_universe_d3_068_rss_basefill_071(rss_base_universe_d2_068_rss_basefill_071):
    return _base_universe_d3(rss_base_universe_d2_068_rss_basefill_071, 68)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_068_rss_basefill_071'] = {'inputs': ['rss_base_universe_d2_068_rss_basefill_071'], 'func': rss_base_universe_d3_068_rss_basefill_071}


def rss_base_universe_d3_069_rss_basefill_072(rss_base_universe_d2_069_rss_basefill_072):
    return _base_universe_d3(rss_base_universe_d2_069_rss_basefill_072, 69)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_069_rss_basefill_072'] = {'inputs': ['rss_base_universe_d2_069_rss_basefill_072'], 'func': rss_base_universe_d3_069_rss_basefill_072}


def rss_base_universe_d3_070_rss_basefill_073(rss_base_universe_d2_070_rss_basefill_073):
    return _base_universe_d3(rss_base_universe_d2_070_rss_basefill_073, 70)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_070_rss_basefill_073'] = {'inputs': ['rss_base_universe_d2_070_rss_basefill_073'], 'func': rss_base_universe_d3_070_rss_basefill_073}


def rss_base_universe_d3_071_rss_basefill_074(rss_base_universe_d2_071_rss_basefill_074):
    return _base_universe_d3(rss_base_universe_d2_071_rss_basefill_074, 71)
RSS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rss_base_universe_d3_071_rss_basefill_074'] = {'inputs': ['rss_base_universe_d2_071_rss_basefill_074'], 'func': rss_base_universe_d3_071_rss_basefill_074}
