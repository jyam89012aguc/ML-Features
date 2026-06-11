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



def lsr_176_lsr_001_dividend_cut_density_21_accel_1(lsr_151_lsr_001_dividend_cut_density_21_roc_1):
    feature = _s(lsr_151_lsr_001_dividend_cut_density_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def lsr_177_lsr_007_listing_tier_decay_1_accel_42(lsr_152_lsr_007_listing_tier_decay_1_roc_42):
    feature = _s(lsr_152_lsr_007_listing_tier_decay_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def lsr_178_lsr_013_delisting_notice_density_1512_accel_126(lsr_153_lsr_013_delisting_notice_density_1512_roc_126):
    feature = _s(lsr_153_lsr_013_delisting_notice_density_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def lsr_179_lsr_019_going_concern_persistence_84_accel_378(lsr_154_lsr_019_going_concern_persistence_84_roc_378):
    feature = _s(lsr_154_lsr_019_going_concern_persistence_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def lsr_180_lsr_025_event_density_z_756_accel_4(lsr_155_lsr_025_event_density_z_756_roc_4):
    feature = _s(lsr_155_lsr_025_event_density_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















LISTING_STATUS_RISK_REGISTRY_3RD_DERIVATIVES = {
    'lsr_176_lsr_001_dividend_cut_density_21_accel_1': {'inputs': ['lsr_151_lsr_001_dividend_cut_density_21_roc_1'], 'func': lsr_176_lsr_001_dividend_cut_density_21_accel_1},
    'lsr_177_lsr_007_listing_tier_decay_1_accel_42': {'inputs': ['lsr_152_lsr_007_listing_tier_decay_1_roc_42'], 'func': lsr_177_lsr_007_listing_tier_decay_1_accel_42},
    'lsr_178_lsr_013_delisting_notice_density_1512_accel_126': {'inputs': ['lsr_153_lsr_013_delisting_notice_density_1512_roc_126'], 'func': lsr_178_lsr_013_delisting_notice_density_1512_accel_126},
    'lsr_179_lsr_019_going_concern_persistence_84_accel_378': {'inputs': ['lsr_154_lsr_019_going_concern_persistence_84_roc_378'], 'func': lsr_179_lsr_019_going_concern_persistence_84_accel_378},
    'lsr_180_lsr_025_event_density_z_756_accel_4': {'inputs': ['lsr_155_lsr_025_event_density_z_756_roc_4'], 'func': lsr_180_lsr_025_event_density_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def lsr_replacement_d3_001(lsr_replacement_d2_001):
    feature = _clean(lsr_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_001'] = {'inputs': ['lsr_replacement_d2_001'], 'func': lsr_replacement_d3_001}


def lsr_replacement_d3_002(lsr_replacement_d2_002):
    feature = _clean(lsr_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_002'] = {'inputs': ['lsr_replacement_d2_002'], 'func': lsr_replacement_d3_002}


def lsr_replacement_d3_003(lsr_replacement_d2_003):
    feature = _clean(lsr_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_003'] = {'inputs': ['lsr_replacement_d2_003'], 'func': lsr_replacement_d3_003}


def lsr_replacement_d3_004(lsr_replacement_d2_004):
    feature = _clean(lsr_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_004'] = {'inputs': ['lsr_replacement_d2_004'], 'func': lsr_replacement_d3_004}


def lsr_replacement_d3_005(lsr_replacement_d2_005):
    feature = _clean(lsr_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_005'] = {'inputs': ['lsr_replacement_d2_005'], 'func': lsr_replacement_d3_005}


def lsr_replacement_d3_006(lsr_replacement_d2_006):
    feature = _clean(lsr_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_006'] = {'inputs': ['lsr_replacement_d2_006'], 'func': lsr_replacement_d3_006}


def lsr_replacement_d3_007(lsr_replacement_d2_007):
    feature = _clean(lsr_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_007'] = {'inputs': ['lsr_replacement_d2_007'], 'func': lsr_replacement_d3_007}


def lsr_replacement_d3_008(lsr_replacement_d2_008):
    feature = _clean(lsr_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_008'] = {'inputs': ['lsr_replacement_d2_008'], 'func': lsr_replacement_d3_008}


def lsr_replacement_d3_009(lsr_replacement_d2_009):
    feature = _clean(lsr_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_009'] = {'inputs': ['lsr_replacement_d2_009'], 'func': lsr_replacement_d3_009}


def lsr_replacement_d3_010(lsr_replacement_d2_010):
    feature = _clean(lsr_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_010'] = {'inputs': ['lsr_replacement_d2_010'], 'func': lsr_replacement_d3_010}


def lsr_replacement_d3_011(lsr_replacement_d2_011):
    feature = _clean(lsr_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_011'] = {'inputs': ['lsr_replacement_d2_011'], 'func': lsr_replacement_d3_011}


def lsr_replacement_d3_012(lsr_replacement_d2_012):
    feature = _clean(lsr_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_012'] = {'inputs': ['lsr_replacement_d2_012'], 'func': lsr_replacement_d3_012}


def lsr_replacement_d3_013(lsr_replacement_d2_013):
    feature = _clean(lsr_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_013'] = {'inputs': ['lsr_replacement_d2_013'], 'func': lsr_replacement_d3_013}


def lsr_replacement_d3_014(lsr_replacement_d2_014):
    feature = _clean(lsr_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_014'] = {'inputs': ['lsr_replacement_d2_014'], 'func': lsr_replacement_d3_014}


def lsr_replacement_d3_015(lsr_replacement_d2_015):
    feature = _clean(lsr_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_015'] = {'inputs': ['lsr_replacement_d2_015'], 'func': lsr_replacement_d3_015}


def lsr_replacement_d3_016(lsr_replacement_d2_016):
    feature = _clean(lsr_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_016'] = {'inputs': ['lsr_replacement_d2_016'], 'func': lsr_replacement_d3_016}


def lsr_replacement_d3_017(lsr_replacement_d2_017):
    feature = _clean(lsr_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_017'] = {'inputs': ['lsr_replacement_d2_017'], 'func': lsr_replacement_d3_017}


def lsr_replacement_d3_018(lsr_replacement_d2_018):
    feature = _clean(lsr_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_018'] = {'inputs': ['lsr_replacement_d2_018'], 'func': lsr_replacement_d3_018}


def lsr_replacement_d3_019(lsr_replacement_d2_019):
    feature = _clean(lsr_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_019'] = {'inputs': ['lsr_replacement_d2_019'], 'func': lsr_replacement_d3_019}


def lsr_replacement_d3_020(lsr_replacement_d2_020):
    feature = _clean(lsr_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_020'] = {'inputs': ['lsr_replacement_d2_020'], 'func': lsr_replacement_d3_020}


def lsr_replacement_d3_021(lsr_replacement_d2_021):
    feature = _clean(lsr_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_021'] = {'inputs': ['lsr_replacement_d2_021'], 'func': lsr_replacement_d3_021}


def lsr_replacement_d3_022(lsr_replacement_d2_022):
    feature = _clean(lsr_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_022'] = {'inputs': ['lsr_replacement_d2_022'], 'func': lsr_replacement_d3_022}


def lsr_replacement_d3_023(lsr_replacement_d2_023):
    feature = _clean(lsr_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_023'] = {'inputs': ['lsr_replacement_d2_023'], 'func': lsr_replacement_d3_023}


def lsr_replacement_d3_024(lsr_replacement_d2_024):
    feature = _clean(lsr_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_024'] = {'inputs': ['lsr_replacement_d2_024'], 'func': lsr_replacement_d3_024}


def lsr_replacement_d3_025(lsr_replacement_d2_025):
    feature = _clean(lsr_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_025'] = {'inputs': ['lsr_replacement_d2_025'], 'func': lsr_replacement_d3_025}


def lsr_replacement_d3_026(lsr_replacement_d2_026):
    feature = _clean(lsr_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_026'] = {'inputs': ['lsr_replacement_d2_026'], 'func': lsr_replacement_d3_026}


def lsr_replacement_d3_027(lsr_replacement_d2_027):
    feature = _clean(lsr_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_027'] = {'inputs': ['lsr_replacement_d2_027'], 'func': lsr_replacement_d3_027}


def lsr_replacement_d3_028(lsr_replacement_d2_028):
    feature = _clean(lsr_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_028'] = {'inputs': ['lsr_replacement_d2_028'], 'func': lsr_replacement_d3_028}


def lsr_replacement_d3_029(lsr_replacement_d2_029):
    feature = _clean(lsr_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_029'] = {'inputs': ['lsr_replacement_d2_029'], 'func': lsr_replacement_d3_029}


def lsr_replacement_d3_030(lsr_replacement_d2_030):
    feature = _clean(lsr_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_030'] = {'inputs': ['lsr_replacement_d2_030'], 'func': lsr_replacement_d3_030}


def lsr_replacement_d3_031(lsr_replacement_d2_031):
    feature = _clean(lsr_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_031'] = {'inputs': ['lsr_replacement_d2_031'], 'func': lsr_replacement_d3_031}


def lsr_replacement_d3_032(lsr_replacement_d2_032):
    feature = _clean(lsr_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_032'] = {'inputs': ['lsr_replacement_d2_032'], 'func': lsr_replacement_d3_032}


def lsr_replacement_d3_033(lsr_replacement_d2_033):
    feature = _clean(lsr_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_033'] = {'inputs': ['lsr_replacement_d2_033'], 'func': lsr_replacement_d3_033}


def lsr_replacement_d3_034(lsr_replacement_d2_034):
    feature = _clean(lsr_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_034'] = {'inputs': ['lsr_replacement_d2_034'], 'func': lsr_replacement_d3_034}


def lsr_replacement_d3_035(lsr_replacement_d2_035):
    feature = _clean(lsr_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_035'] = {'inputs': ['lsr_replacement_d2_035'], 'func': lsr_replacement_d3_035}


def lsr_replacement_d3_036(lsr_replacement_d2_036):
    feature = _clean(lsr_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_036'] = {'inputs': ['lsr_replacement_d2_036'], 'func': lsr_replacement_d3_036}


def lsr_replacement_d3_037(lsr_replacement_d2_037):
    feature = _clean(lsr_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_037'] = {'inputs': ['lsr_replacement_d2_037'], 'func': lsr_replacement_d3_037}


def lsr_replacement_d3_038(lsr_replacement_d2_038):
    feature = _clean(lsr_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_038'] = {'inputs': ['lsr_replacement_d2_038'], 'func': lsr_replacement_d3_038}


def lsr_replacement_d3_039(lsr_replacement_d2_039):
    feature = _clean(lsr_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_039'] = {'inputs': ['lsr_replacement_d2_039'], 'func': lsr_replacement_d3_039}


def lsr_replacement_d3_040(lsr_replacement_d2_040):
    feature = _clean(lsr_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_040'] = {'inputs': ['lsr_replacement_d2_040'], 'func': lsr_replacement_d3_040}


def lsr_replacement_d3_041(lsr_replacement_d2_041):
    feature = _clean(lsr_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_041'] = {'inputs': ['lsr_replacement_d2_041'], 'func': lsr_replacement_d3_041}


def lsr_replacement_d3_042(lsr_replacement_d2_042):
    feature = _clean(lsr_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_042'] = {'inputs': ['lsr_replacement_d2_042'], 'func': lsr_replacement_d3_042}


def lsr_replacement_d3_043(lsr_replacement_d2_043):
    feature = _clean(lsr_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_043'] = {'inputs': ['lsr_replacement_d2_043'], 'func': lsr_replacement_d3_043}


def lsr_replacement_d3_044(lsr_replacement_d2_044):
    feature = _clean(lsr_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_044'] = {'inputs': ['lsr_replacement_d2_044'], 'func': lsr_replacement_d3_044}


def lsr_replacement_d3_045(lsr_replacement_d2_045):
    feature = _clean(lsr_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_045'] = {'inputs': ['lsr_replacement_d2_045'], 'func': lsr_replacement_d3_045}


def lsr_replacement_d3_046(lsr_replacement_d2_046):
    feature = _clean(lsr_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_046'] = {'inputs': ['lsr_replacement_d2_046'], 'func': lsr_replacement_d3_046}


def lsr_replacement_d3_047(lsr_replacement_d2_047):
    feature = _clean(lsr_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_047'] = {'inputs': ['lsr_replacement_d2_047'], 'func': lsr_replacement_d3_047}


def lsr_replacement_d3_048(lsr_replacement_d2_048):
    feature = _clean(lsr_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_048'] = {'inputs': ['lsr_replacement_d2_048'], 'func': lsr_replacement_d3_048}


def lsr_replacement_d3_049(lsr_replacement_d2_049):
    feature = _clean(lsr_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_049'] = {'inputs': ['lsr_replacement_d2_049'], 'func': lsr_replacement_d3_049}


def lsr_replacement_d3_050(lsr_replacement_d2_050):
    feature = _clean(lsr_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_050'] = {'inputs': ['lsr_replacement_d2_050'], 'func': lsr_replacement_d3_050}


def lsr_replacement_d3_051(lsr_replacement_d2_051):
    feature = _clean(lsr_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_051'] = {'inputs': ['lsr_replacement_d2_051'], 'func': lsr_replacement_d3_051}


def lsr_replacement_d3_052(lsr_replacement_d2_052):
    feature = _clean(lsr_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_052'] = {'inputs': ['lsr_replacement_d2_052'], 'func': lsr_replacement_d3_052}


def lsr_replacement_d3_053(lsr_replacement_d2_053):
    feature = _clean(lsr_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_053'] = {'inputs': ['lsr_replacement_d2_053'], 'func': lsr_replacement_d3_053}


def lsr_replacement_d3_054(lsr_replacement_d2_054):
    feature = _clean(lsr_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_054'] = {'inputs': ['lsr_replacement_d2_054'], 'func': lsr_replacement_d3_054}


def lsr_replacement_d3_055(lsr_replacement_d2_055):
    feature = _clean(lsr_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_055'] = {'inputs': ['lsr_replacement_d2_055'], 'func': lsr_replacement_d3_055}


def lsr_replacement_d3_056(lsr_replacement_d2_056):
    feature = _clean(lsr_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_056'] = {'inputs': ['lsr_replacement_d2_056'], 'func': lsr_replacement_d3_056}


def lsr_replacement_d3_057(lsr_replacement_d2_057):
    feature = _clean(lsr_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_057'] = {'inputs': ['lsr_replacement_d2_057'], 'func': lsr_replacement_d3_057}


def lsr_replacement_d3_058(lsr_replacement_d2_058):
    feature = _clean(lsr_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_058'] = {'inputs': ['lsr_replacement_d2_058'], 'func': lsr_replacement_d3_058}


def lsr_replacement_d3_059(lsr_replacement_d2_059):
    feature = _clean(lsr_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_059'] = {'inputs': ['lsr_replacement_d2_059'], 'func': lsr_replacement_d3_059}


def lsr_replacement_d3_060(lsr_replacement_d2_060):
    feature = _clean(lsr_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_060'] = {'inputs': ['lsr_replacement_d2_060'], 'func': lsr_replacement_d3_060}


def lsr_replacement_d3_061(lsr_replacement_d2_061):
    feature = _clean(lsr_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_061'] = {'inputs': ['lsr_replacement_d2_061'], 'func': lsr_replacement_d3_061}


def lsr_replacement_d3_062(lsr_replacement_d2_062):
    feature = _clean(lsr_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_062'] = {'inputs': ['lsr_replacement_d2_062'], 'func': lsr_replacement_d3_062}


def lsr_replacement_d3_063(lsr_replacement_d2_063):
    feature = _clean(lsr_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_063'] = {'inputs': ['lsr_replacement_d2_063'], 'func': lsr_replacement_d3_063}


def lsr_replacement_d3_064(lsr_replacement_d2_064):
    feature = _clean(lsr_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_064'] = {'inputs': ['lsr_replacement_d2_064'], 'func': lsr_replacement_d3_064}


def lsr_replacement_d3_065(lsr_replacement_d2_065):
    feature = _clean(lsr_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_065'] = {'inputs': ['lsr_replacement_d2_065'], 'func': lsr_replacement_d3_065}


def lsr_replacement_d3_066(lsr_replacement_d2_066):
    feature = _clean(lsr_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_066'] = {'inputs': ['lsr_replacement_d2_066'], 'func': lsr_replacement_d3_066}


def lsr_replacement_d3_067(lsr_replacement_d2_067):
    feature = _clean(lsr_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_067'] = {'inputs': ['lsr_replacement_d2_067'], 'func': lsr_replacement_d3_067}


def lsr_replacement_d3_068(lsr_replacement_d2_068):
    feature = _clean(lsr_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_068'] = {'inputs': ['lsr_replacement_d2_068'], 'func': lsr_replacement_d3_068}


def lsr_replacement_d3_069(lsr_replacement_d2_069):
    feature = _clean(lsr_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_069'] = {'inputs': ['lsr_replacement_d2_069'], 'func': lsr_replacement_d3_069}


def lsr_replacement_d3_070(lsr_replacement_d2_070):
    feature = _clean(lsr_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_070'] = {'inputs': ['lsr_replacement_d2_070'], 'func': lsr_replacement_d3_070}


def lsr_replacement_d3_071(lsr_replacement_d2_071):
    feature = _clean(lsr_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_071'] = {'inputs': ['lsr_replacement_d2_071'], 'func': lsr_replacement_d3_071}


def lsr_replacement_d3_072(lsr_replacement_d2_072):
    feature = _clean(lsr_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_072'] = {'inputs': ['lsr_replacement_d2_072'], 'func': lsr_replacement_d3_072}


def lsr_replacement_d3_073(lsr_replacement_d2_073):
    feature = _clean(lsr_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_073'] = {'inputs': ['lsr_replacement_d2_073'], 'func': lsr_replacement_d3_073}


def lsr_replacement_d3_074(lsr_replacement_d2_074):
    feature = _clean(lsr_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_074'] = {'inputs': ['lsr_replacement_d2_074'], 'func': lsr_replacement_d3_074}


def lsr_replacement_d3_075(lsr_replacement_d2_075):
    feature = _clean(lsr_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_075'] = {'inputs': ['lsr_replacement_d2_075'], 'func': lsr_replacement_d3_075}


def lsr_replacement_d3_076(lsr_replacement_d2_076):
    feature = _clean(lsr_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_076'] = {'inputs': ['lsr_replacement_d2_076'], 'func': lsr_replacement_d3_076}


def lsr_replacement_d3_077(lsr_replacement_d2_077):
    feature = _clean(lsr_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_077'] = {'inputs': ['lsr_replacement_d2_077'], 'func': lsr_replacement_d3_077}


def lsr_replacement_d3_078(lsr_replacement_d2_078):
    feature = _clean(lsr_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_078'] = {'inputs': ['lsr_replacement_d2_078'], 'func': lsr_replacement_d3_078}


def lsr_replacement_d3_079(lsr_replacement_d2_079):
    feature = _clean(lsr_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_079'] = {'inputs': ['lsr_replacement_d2_079'], 'func': lsr_replacement_d3_079}


def lsr_replacement_d3_080(lsr_replacement_d2_080):
    feature = _clean(lsr_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_080'] = {'inputs': ['lsr_replacement_d2_080'], 'func': lsr_replacement_d3_080}


def lsr_replacement_d3_081(lsr_replacement_d2_081):
    feature = _clean(lsr_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_081'] = {'inputs': ['lsr_replacement_d2_081'], 'func': lsr_replacement_d3_081}


def lsr_replacement_d3_082(lsr_replacement_d2_082):
    feature = _clean(lsr_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_082'] = {'inputs': ['lsr_replacement_d2_082'], 'func': lsr_replacement_d3_082}


def lsr_replacement_d3_083(lsr_replacement_d2_083):
    feature = _clean(lsr_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_083'] = {'inputs': ['lsr_replacement_d2_083'], 'func': lsr_replacement_d3_083}


def lsr_replacement_d3_084(lsr_replacement_d2_084):
    feature = _clean(lsr_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_084'] = {'inputs': ['lsr_replacement_d2_084'], 'func': lsr_replacement_d3_084}


def lsr_replacement_d3_085(lsr_replacement_d2_085):
    feature = _clean(lsr_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_085'] = {'inputs': ['lsr_replacement_d2_085'], 'func': lsr_replacement_d3_085}


def lsr_replacement_d3_086(lsr_replacement_d2_086):
    feature = _clean(lsr_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_086'] = {'inputs': ['lsr_replacement_d2_086'], 'func': lsr_replacement_d3_086}


def lsr_replacement_d3_087(lsr_replacement_d2_087):
    feature = _clean(lsr_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_087'] = {'inputs': ['lsr_replacement_d2_087'], 'func': lsr_replacement_d3_087}


def lsr_replacement_d3_088(lsr_replacement_d2_088):
    feature = _clean(lsr_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_088'] = {'inputs': ['lsr_replacement_d2_088'], 'func': lsr_replacement_d3_088}


def lsr_replacement_d3_089(lsr_replacement_d2_089):
    feature = _clean(lsr_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_089'] = {'inputs': ['lsr_replacement_d2_089'], 'func': lsr_replacement_d3_089}


def lsr_replacement_d3_090(lsr_replacement_d2_090):
    feature = _clean(lsr_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_090'] = {'inputs': ['lsr_replacement_d2_090'], 'func': lsr_replacement_d3_090}


def lsr_replacement_d3_091(lsr_replacement_d2_091):
    feature = _clean(lsr_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_091'] = {'inputs': ['lsr_replacement_d2_091'], 'func': lsr_replacement_d3_091}


def lsr_replacement_d3_092(lsr_replacement_d2_092):
    feature = _clean(lsr_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_092'] = {'inputs': ['lsr_replacement_d2_092'], 'func': lsr_replacement_d3_092}


def lsr_replacement_d3_093(lsr_replacement_d2_093):
    feature = _clean(lsr_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_093'] = {'inputs': ['lsr_replacement_d2_093'], 'func': lsr_replacement_d3_093}


def lsr_replacement_d3_094(lsr_replacement_d2_094):
    feature = _clean(lsr_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_094'] = {'inputs': ['lsr_replacement_d2_094'], 'func': lsr_replacement_d3_094}


def lsr_replacement_d3_095(lsr_replacement_d2_095):
    feature = _clean(lsr_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_095'] = {'inputs': ['lsr_replacement_d2_095'], 'func': lsr_replacement_d3_095}


def lsr_replacement_d3_096(lsr_replacement_d2_096):
    feature = _clean(lsr_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_096'] = {'inputs': ['lsr_replacement_d2_096'], 'func': lsr_replacement_d3_096}


def lsr_replacement_d3_097(lsr_replacement_d2_097):
    feature = _clean(lsr_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_097'] = {'inputs': ['lsr_replacement_d2_097'], 'func': lsr_replacement_d3_097}


def lsr_replacement_d3_098(lsr_replacement_d2_098):
    feature = _clean(lsr_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_098'] = {'inputs': ['lsr_replacement_d2_098'], 'func': lsr_replacement_d3_098}


def lsr_replacement_d3_099(lsr_replacement_d2_099):
    feature = _clean(lsr_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_099'] = {'inputs': ['lsr_replacement_d2_099'], 'func': lsr_replacement_d3_099}


def lsr_replacement_d3_100(lsr_replacement_d2_100):
    feature = _clean(lsr_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_100'] = {'inputs': ['lsr_replacement_d2_100'], 'func': lsr_replacement_d3_100}


def lsr_replacement_d3_101(lsr_replacement_d2_101):
    feature = _clean(lsr_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_101'] = {'inputs': ['lsr_replacement_d2_101'], 'func': lsr_replacement_d3_101}


def lsr_replacement_d3_102(lsr_replacement_d2_102):
    feature = _clean(lsr_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_102'] = {'inputs': ['lsr_replacement_d2_102'], 'func': lsr_replacement_d3_102}


def lsr_replacement_d3_103(lsr_replacement_d2_103):
    feature = _clean(lsr_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_103'] = {'inputs': ['lsr_replacement_d2_103'], 'func': lsr_replacement_d3_103}


def lsr_replacement_d3_104(lsr_replacement_d2_104):
    feature = _clean(lsr_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_104'] = {'inputs': ['lsr_replacement_d2_104'], 'func': lsr_replacement_d3_104}


def lsr_replacement_d3_105(lsr_replacement_d2_105):
    feature = _clean(lsr_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_105'] = {'inputs': ['lsr_replacement_d2_105'], 'func': lsr_replacement_d3_105}


def lsr_replacement_d3_106(lsr_replacement_d2_106):
    feature = _clean(lsr_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_106'] = {'inputs': ['lsr_replacement_d2_106'], 'func': lsr_replacement_d3_106}


def lsr_replacement_d3_107(lsr_replacement_d2_107):
    feature = _clean(lsr_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_107'] = {'inputs': ['lsr_replacement_d2_107'], 'func': lsr_replacement_d3_107}


def lsr_replacement_d3_108(lsr_replacement_d2_108):
    feature = _clean(lsr_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_108'] = {'inputs': ['lsr_replacement_d2_108'], 'func': lsr_replacement_d3_108}


def lsr_replacement_d3_109(lsr_replacement_d2_109):
    feature = _clean(lsr_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_109'] = {'inputs': ['lsr_replacement_d2_109'], 'func': lsr_replacement_d3_109}


def lsr_replacement_d3_110(lsr_replacement_d2_110):
    feature = _clean(lsr_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_110'] = {'inputs': ['lsr_replacement_d2_110'], 'func': lsr_replacement_d3_110}


def lsr_replacement_d3_111(lsr_replacement_d2_111):
    feature = _clean(lsr_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_111'] = {'inputs': ['lsr_replacement_d2_111'], 'func': lsr_replacement_d3_111}


def lsr_replacement_d3_112(lsr_replacement_d2_112):
    feature = _clean(lsr_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_112'] = {'inputs': ['lsr_replacement_d2_112'], 'func': lsr_replacement_d3_112}


def lsr_replacement_d3_113(lsr_replacement_d2_113):
    feature = _clean(lsr_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_113'] = {'inputs': ['lsr_replacement_d2_113'], 'func': lsr_replacement_d3_113}


def lsr_replacement_d3_114(lsr_replacement_d2_114):
    feature = _clean(lsr_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_114'] = {'inputs': ['lsr_replacement_d2_114'], 'func': lsr_replacement_d3_114}


def lsr_replacement_d3_115(lsr_replacement_d2_115):
    feature = _clean(lsr_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_115'] = {'inputs': ['lsr_replacement_d2_115'], 'func': lsr_replacement_d3_115}


def lsr_replacement_d3_116(lsr_replacement_d2_116):
    feature = _clean(lsr_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_116'] = {'inputs': ['lsr_replacement_d2_116'], 'func': lsr_replacement_d3_116}


def lsr_replacement_d3_117(lsr_replacement_d2_117):
    feature = _clean(lsr_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_117'] = {'inputs': ['lsr_replacement_d2_117'], 'func': lsr_replacement_d3_117}


def lsr_replacement_d3_118(lsr_replacement_d2_118):
    feature = _clean(lsr_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_118'] = {'inputs': ['lsr_replacement_d2_118'], 'func': lsr_replacement_d3_118}


def lsr_replacement_d3_119(lsr_replacement_d2_119):
    feature = _clean(lsr_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_119'] = {'inputs': ['lsr_replacement_d2_119'], 'func': lsr_replacement_d3_119}


def lsr_replacement_d3_120(lsr_replacement_d2_120):
    feature = _clean(lsr_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_120'] = {'inputs': ['lsr_replacement_d2_120'], 'func': lsr_replacement_d3_120}


def lsr_replacement_d3_121(lsr_replacement_d2_121):
    feature = _clean(lsr_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_121'] = {'inputs': ['lsr_replacement_d2_121'], 'func': lsr_replacement_d3_121}


def lsr_replacement_d3_122(lsr_replacement_d2_122):
    feature = _clean(lsr_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_122'] = {'inputs': ['lsr_replacement_d2_122'], 'func': lsr_replacement_d3_122}


def lsr_replacement_d3_123(lsr_replacement_d2_123):
    feature = _clean(lsr_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_123'] = {'inputs': ['lsr_replacement_d2_123'], 'func': lsr_replacement_d3_123}


def lsr_replacement_d3_124(lsr_replacement_d2_124):
    feature = _clean(lsr_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_124'] = {'inputs': ['lsr_replacement_d2_124'], 'func': lsr_replacement_d3_124}


def lsr_replacement_d3_125(lsr_replacement_d2_125):
    feature = _clean(lsr_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_125'] = {'inputs': ['lsr_replacement_d2_125'], 'func': lsr_replacement_d3_125}


def lsr_replacement_d3_126(lsr_replacement_d2_126):
    feature = _clean(lsr_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_126'] = {'inputs': ['lsr_replacement_d2_126'], 'func': lsr_replacement_d3_126}


def lsr_replacement_d3_127(lsr_replacement_d2_127):
    feature = _clean(lsr_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_127'] = {'inputs': ['lsr_replacement_d2_127'], 'func': lsr_replacement_d3_127}


def lsr_replacement_d3_128(lsr_replacement_d2_128):
    feature = _clean(lsr_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_128'] = {'inputs': ['lsr_replacement_d2_128'], 'func': lsr_replacement_d3_128}


def lsr_replacement_d3_129(lsr_replacement_d2_129):
    feature = _clean(lsr_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_129'] = {'inputs': ['lsr_replacement_d2_129'], 'func': lsr_replacement_d3_129}


def lsr_replacement_d3_130(lsr_replacement_d2_130):
    feature = _clean(lsr_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_130'] = {'inputs': ['lsr_replacement_d2_130'], 'func': lsr_replacement_d3_130}


def lsr_replacement_d3_131(lsr_replacement_d2_131):
    feature = _clean(lsr_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_131'] = {'inputs': ['lsr_replacement_d2_131'], 'func': lsr_replacement_d3_131}


def lsr_replacement_d3_132(lsr_replacement_d2_132):
    feature = _clean(lsr_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_132'] = {'inputs': ['lsr_replacement_d2_132'], 'func': lsr_replacement_d3_132}


def lsr_replacement_d3_133(lsr_replacement_d2_133):
    feature = _clean(lsr_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_133'] = {'inputs': ['lsr_replacement_d2_133'], 'func': lsr_replacement_d3_133}


def lsr_replacement_d3_134(lsr_replacement_d2_134):
    feature = _clean(lsr_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_134'] = {'inputs': ['lsr_replacement_d2_134'], 'func': lsr_replacement_d3_134}


def lsr_replacement_d3_135(lsr_replacement_d2_135):
    feature = _clean(lsr_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_135'] = {'inputs': ['lsr_replacement_d2_135'], 'func': lsr_replacement_d3_135}


def lsr_replacement_d3_136(lsr_replacement_d2_136):
    feature = _clean(lsr_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_136'] = {'inputs': ['lsr_replacement_d2_136'], 'func': lsr_replacement_d3_136}


def lsr_replacement_d3_137(lsr_replacement_d2_137):
    feature = _clean(lsr_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_137'] = {'inputs': ['lsr_replacement_d2_137'], 'func': lsr_replacement_d3_137}


def lsr_replacement_d3_138(lsr_replacement_d2_138):
    feature = _clean(lsr_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_138'] = {'inputs': ['lsr_replacement_d2_138'], 'func': lsr_replacement_d3_138}


def lsr_replacement_d3_139(lsr_replacement_d2_139):
    feature = _clean(lsr_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_139'] = {'inputs': ['lsr_replacement_d2_139'], 'func': lsr_replacement_d3_139}


def lsr_replacement_d3_140(lsr_replacement_d2_140):
    feature = _clean(lsr_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_140'] = {'inputs': ['lsr_replacement_d2_140'], 'func': lsr_replacement_d3_140}


def lsr_replacement_d3_141(lsr_replacement_d2_141):
    feature = _clean(lsr_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_141'] = {'inputs': ['lsr_replacement_d2_141'], 'func': lsr_replacement_d3_141}


def lsr_replacement_d3_142(lsr_replacement_d2_142):
    feature = _clean(lsr_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_142'] = {'inputs': ['lsr_replacement_d2_142'], 'func': lsr_replacement_d3_142}


def lsr_replacement_d3_143(lsr_replacement_d2_143):
    feature = _clean(lsr_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_143'] = {'inputs': ['lsr_replacement_d2_143'], 'func': lsr_replacement_d3_143}


def lsr_replacement_d3_144(lsr_replacement_d2_144):
    feature = _clean(lsr_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_144'] = {'inputs': ['lsr_replacement_d2_144'], 'func': lsr_replacement_d3_144}


def lsr_replacement_d3_145(lsr_replacement_d2_145):
    feature = _clean(lsr_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_145'] = {'inputs': ['lsr_replacement_d2_145'], 'func': lsr_replacement_d3_145}


def lsr_replacement_d3_146(lsr_replacement_d2_146):
    feature = _clean(lsr_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_146'] = {'inputs': ['lsr_replacement_d2_146'], 'func': lsr_replacement_d3_146}


def lsr_replacement_d3_147(lsr_replacement_d2_147):
    feature = _clean(lsr_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_147'] = {'inputs': ['lsr_replacement_d2_147'], 'func': lsr_replacement_d3_147}


def lsr_replacement_d3_148(lsr_replacement_d2_148):
    feature = _clean(lsr_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_148'] = {'inputs': ['lsr_replacement_d2_148'], 'func': lsr_replacement_d3_148}


def lsr_replacement_d3_149(lsr_replacement_d2_149):
    feature = _clean(lsr_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_149'] = {'inputs': ['lsr_replacement_d2_149'], 'func': lsr_replacement_d3_149}


def lsr_replacement_d3_150(lsr_replacement_d2_150):
    feature = _clean(lsr_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_150'] = {'inputs': ['lsr_replacement_d2_150'], 'func': lsr_replacement_d3_150}


def lsr_replacement_d3_151(lsr_replacement_d2_151):
    feature = _clean(lsr_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
LSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['lsr_replacement_d3_151'] = {'inputs': ['lsr_replacement_d2_151'], 'func': lsr_replacement_d3_151}


# Third-derivative extensions for repaired first-base features.
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lsr_base_universe_d3_001_lsr_002_dividend_suspension_density_42(lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42):
    return _base_universe_d3(lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42, 1)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_001_lsr_002_dividend_suspension_density_42'] = {'inputs': ['lsr_base_universe_d2_001_lsr_002_dividend_suspension_density_42'], 'func': lsr_base_universe_d3_001_lsr_002_dividend_suspension_density_42}


def lsr_base_universe_d3_002_lsr_003_reverse_split_density_63(lsr_base_universe_d2_002_lsr_003_reverse_split_density_63):
    return _base_universe_d3(lsr_base_universe_d2_002_lsr_003_reverse_split_density_63, 2)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_002_lsr_003_reverse_split_density_63'] = {'inputs': ['lsr_base_universe_d2_002_lsr_003_reverse_split_density_63'], 'func': lsr_base_universe_d3_002_lsr_003_reverse_split_density_63}


def lsr_base_universe_d3_003_lsr_004_event_density_z_84(lsr_base_universe_d2_003_lsr_004_event_density_z_84):
    return _base_universe_d3(lsr_base_universe_d2_003_lsr_004_event_density_z_84, 3)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_003_lsr_004_event_density_z_84'] = {'inputs': ['lsr_base_universe_d2_003_lsr_004_event_density_z_84'], 'func': lsr_base_universe_d3_003_lsr_004_event_density_z_84}


def lsr_base_universe_d3_004_lsr_005_going_concern_persistence_126(lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126):
    return _base_universe_d3(lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126, 4)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_004_lsr_005_going_concern_persistence_126'] = {'inputs': ['lsr_base_universe_d2_004_lsr_005_going_concern_persistence_126'], 'func': lsr_base_universe_d3_004_lsr_005_going_concern_persistence_126}


def lsr_base_universe_d3_005_lsr_006_delisting_notice_density_189(lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189):
    return _base_universe_d3(lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189, 5)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_005_lsr_006_delisting_notice_density_189'] = {'inputs': ['lsr_base_universe_d2_005_lsr_006_delisting_notice_density_189'], 'func': lsr_base_universe_d3_005_lsr_006_delisting_notice_density_189}


def lsr_base_universe_d3_006_lsr_008_dividend_cut_density_378(lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378):
    return _base_universe_d3(lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378, 6)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_006_lsr_008_dividend_cut_density_378'] = {'inputs': ['lsr_base_universe_d2_006_lsr_008_dividend_cut_density_378'], 'func': lsr_base_universe_d3_006_lsr_008_dividend_cut_density_378}


def lsr_base_universe_d3_007_lsr_009_dividend_suspension_density_504(lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504):
    return _base_universe_d3(lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504, 7)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_007_lsr_009_dividend_suspension_density_504'] = {'inputs': ['lsr_base_universe_d2_007_lsr_009_dividend_suspension_density_504'], 'func': lsr_base_universe_d3_007_lsr_009_dividend_suspension_density_504}


def lsr_base_universe_d3_008_lsr_010_reverse_split_density_756(lsr_base_universe_d2_008_lsr_010_reverse_split_density_756):
    return _base_universe_d3(lsr_base_universe_d2_008_lsr_010_reverse_split_density_756, 8)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_008_lsr_010_reverse_split_density_756'] = {'inputs': ['lsr_base_universe_d2_008_lsr_010_reverse_split_density_756'], 'func': lsr_base_universe_d3_008_lsr_010_reverse_split_density_756}


def lsr_base_universe_d3_009_lsr_011_event_density_z_1008(lsr_base_universe_d2_009_lsr_011_event_density_z_1008):
    return _base_universe_d3(lsr_base_universe_d2_009_lsr_011_event_density_z_1008, 9)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_009_lsr_011_event_density_z_1008'] = {'inputs': ['lsr_base_universe_d2_009_lsr_011_event_density_z_1008'], 'func': lsr_base_universe_d3_009_lsr_011_event_density_z_1008}


def lsr_base_universe_d3_010_lsr_012_going_concern_persistence_1260(lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260):
    return _base_universe_d3(lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260, 10)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_010_lsr_012_going_concern_persistence_1260'] = {'inputs': ['lsr_base_universe_d2_010_lsr_012_going_concern_persistence_1260'], 'func': lsr_base_universe_d3_010_lsr_012_going_concern_persistence_1260}


def lsr_base_universe_d3_011_lsr_015_dividend_cut_density_252(lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252):
    return _base_universe_d3(lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252, 11)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_011_lsr_015_dividend_cut_density_252'] = {'inputs': ['lsr_base_universe_d2_011_lsr_015_dividend_cut_density_252'], 'func': lsr_base_universe_d3_011_lsr_015_dividend_cut_density_252}


def lsr_base_universe_d3_012_lsr_018_event_density_z_63(lsr_base_universe_d2_012_lsr_018_event_density_z_63):
    return _base_universe_d3(lsr_base_universe_d2_012_lsr_018_event_density_z_63, 12)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_012_lsr_018_event_density_z_63'] = {'inputs': ['lsr_base_universe_d2_012_lsr_018_event_density_z_63'], 'func': lsr_base_universe_d3_012_lsr_018_event_density_z_63}


def lsr_base_universe_d3_013_lsr_020_delisting_notice_density_126(lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126):
    return _base_universe_d3(lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126, 13)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_013_lsr_020_delisting_notice_density_126'] = {'inputs': ['lsr_base_universe_d2_013_lsr_020_delisting_notice_density_126'], 'func': lsr_base_universe_d3_013_lsr_020_delisting_notice_density_126}


def lsr_base_universe_d3_014_lsr_026_going_concern_persistence_1008(lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008):
    return _base_universe_d3(lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008, 14)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_014_lsr_026_going_concern_persistence_1008'] = {'inputs': ['lsr_base_universe_d2_014_lsr_026_going_concern_persistence_1008'], 'func': lsr_base_universe_d3_014_lsr_026_going_concern_persistence_1008}


def lsr_base_universe_d3_015_lsr_027_delisting_notice_density_1260(lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260):
    return _base_universe_d3(lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260, 15)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_015_lsr_027_delisting_notice_density_1260'] = {'inputs': ['lsr_base_universe_d2_015_lsr_027_delisting_notice_density_1260'], 'func': lsr_base_universe_d3_015_lsr_027_delisting_notice_density_1260}


def lsr_base_universe_d3_016_lsr_032_event_density_z_42(lsr_base_universe_d2_016_lsr_032_event_density_z_42):
    return _base_universe_d3(lsr_base_universe_d2_016_lsr_032_event_density_z_42, 16)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_016_lsr_032_event_density_z_42'] = {'inputs': ['lsr_base_universe_d2_016_lsr_032_event_density_z_42'], 'func': lsr_base_universe_d3_016_lsr_032_event_density_z_42}


def lsr_base_universe_d3_017_lsr_033_going_concern_persistence_63(lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63):
    return _base_universe_d3(lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63, 17)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_017_lsr_033_going_concern_persistence_63'] = {'inputs': ['lsr_base_universe_d2_017_lsr_033_going_concern_persistence_63'], 'func': lsr_base_universe_d3_017_lsr_033_going_concern_persistence_63}


def lsr_base_universe_d3_018_lsr_034_delisting_notice_density_84(lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84):
    return _base_universe_d3(lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84, 18)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_018_lsr_034_delisting_notice_density_84'] = {'inputs': ['lsr_base_universe_d2_018_lsr_034_delisting_notice_density_84'], 'func': lsr_base_universe_d3_018_lsr_034_delisting_notice_density_84}


def lsr_base_universe_d3_019_lsr_039_event_density_z_504(lsr_base_universe_d2_019_lsr_039_event_density_z_504):
    return _base_universe_d3(lsr_base_universe_d2_019_lsr_039_event_density_z_504, 19)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_019_lsr_039_event_density_z_504'] = {'inputs': ['lsr_base_universe_d2_019_lsr_039_event_density_z_504'], 'func': lsr_base_universe_d3_019_lsr_039_event_density_z_504}


def lsr_base_universe_d3_020_lsr_040_going_concern_persistence_756(lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756):
    return _base_universe_d3(lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756, 20)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_020_lsr_040_going_concern_persistence_756'] = {'inputs': ['lsr_base_universe_d2_020_lsr_040_going_concern_persistence_756'], 'func': lsr_base_universe_d3_020_lsr_040_going_concern_persistence_756}


def lsr_base_universe_d3_021_lsr_041_delisting_notice_density_1008(lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008):
    return _base_universe_d3(lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008, 21)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_021_lsr_041_delisting_notice_density_1008'] = {'inputs': ['lsr_base_universe_d2_021_lsr_041_delisting_notice_density_1008'], 'func': lsr_base_universe_d3_021_lsr_041_delisting_notice_density_1008}


def lsr_base_universe_d3_022_lsr_046_event_density_z_21(lsr_base_universe_d2_022_lsr_046_event_density_z_21):
    return _base_universe_d3(lsr_base_universe_d2_022_lsr_046_event_density_z_21, 22)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_022_lsr_046_event_density_z_21'] = {'inputs': ['lsr_base_universe_d2_022_lsr_046_event_density_z_21'], 'func': lsr_base_universe_d3_022_lsr_046_event_density_z_21}


def lsr_base_universe_d3_023_lsr_047_going_concern_persistence_42(lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42):
    return _base_universe_d3(lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42, 23)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_023_lsr_047_going_concern_persistence_42'] = {'inputs': ['lsr_base_universe_d2_023_lsr_047_going_concern_persistence_42'], 'func': lsr_base_universe_d3_023_lsr_047_going_concern_persistence_42}


def lsr_base_universe_d3_024_lsr_053_event_density_z_378(lsr_base_universe_d2_024_lsr_053_event_density_z_378):
    return _base_universe_d3(lsr_base_universe_d2_024_lsr_053_event_density_z_378, 24)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_024_lsr_053_event_density_z_378'] = {'inputs': ['lsr_base_universe_d2_024_lsr_053_event_density_z_378'], 'func': lsr_base_universe_d3_024_lsr_053_event_density_z_378}


def lsr_base_universe_d3_025_lsr_054_going_concern_persistence_504(lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504):
    return _base_universe_d3(lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504, 25)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_025_lsr_054_going_concern_persistence_504'] = {'inputs': ['lsr_base_universe_d2_025_lsr_054_going_concern_persistence_504'], 'func': lsr_base_universe_d3_025_lsr_054_going_concern_persistence_504}


def lsr_base_universe_d3_026_lsr_060_event_density_z_252(lsr_base_universe_d2_026_lsr_060_event_density_z_252):
    return _base_universe_d3(lsr_base_universe_d2_026_lsr_060_event_density_z_252, 26)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_026_lsr_060_event_density_z_252'] = {'inputs': ['lsr_base_universe_d2_026_lsr_060_event_density_z_252'], 'func': lsr_base_universe_d3_026_lsr_060_event_density_z_252}


def lsr_base_universe_d3_027_lsr_061_going_concern_persistence_21(lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21):
    return _base_universe_d3(lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21, 27)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_027_lsr_061_going_concern_persistence_21'] = {'inputs': ['lsr_base_universe_d2_027_lsr_061_going_concern_persistence_21'], 'func': lsr_base_universe_d3_027_lsr_061_going_concern_persistence_21}


def lsr_base_universe_d3_028_lsr_068_going_concern_persistence_378(lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378):
    return _base_universe_d3(lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378, 28)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_028_lsr_068_going_concern_persistence_378'] = {'inputs': ['lsr_base_universe_d2_028_lsr_068_going_concern_persistence_378'], 'func': lsr_base_universe_d3_028_lsr_068_going_concern_persistence_378}


def lsr_base_universe_d3_029_lsr_075_going_concern_persistence_252(lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252):
    return _base_universe_d3(lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252, 29)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_029_lsr_075_going_concern_persistence_252'] = {'inputs': ['lsr_base_universe_d2_029_lsr_075_going_concern_persistence_252'], 'func': lsr_base_universe_d3_029_lsr_075_going_concern_persistence_252}


def lsr_base_universe_d3_030_lsr_basefill_007(lsr_base_universe_d2_030_lsr_basefill_007):
    return _base_universe_d3(lsr_base_universe_d2_030_lsr_basefill_007, 30)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_030_lsr_basefill_007'] = {'inputs': ['lsr_base_universe_d2_030_lsr_basefill_007'], 'func': lsr_base_universe_d3_030_lsr_basefill_007}


def lsr_base_universe_d3_031_lsr_basefill_014(lsr_base_universe_d2_031_lsr_basefill_014):
    return _base_universe_d3(lsr_base_universe_d2_031_lsr_basefill_014, 31)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_031_lsr_basefill_014'] = {'inputs': ['lsr_base_universe_d2_031_lsr_basefill_014'], 'func': lsr_base_universe_d3_031_lsr_basefill_014}


def lsr_base_universe_d3_032_lsr_basefill_016(lsr_base_universe_d2_032_lsr_basefill_016):
    return _base_universe_d3(lsr_base_universe_d2_032_lsr_basefill_016, 32)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_032_lsr_basefill_016'] = {'inputs': ['lsr_base_universe_d2_032_lsr_basefill_016'], 'func': lsr_base_universe_d3_032_lsr_basefill_016}


def lsr_base_universe_d3_033_lsr_basefill_017(lsr_base_universe_d2_033_lsr_basefill_017):
    return _base_universe_d3(lsr_base_universe_d2_033_lsr_basefill_017, 33)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_033_lsr_basefill_017'] = {'inputs': ['lsr_base_universe_d2_033_lsr_basefill_017'], 'func': lsr_base_universe_d3_033_lsr_basefill_017}


def lsr_base_universe_d3_034_lsr_basefill_021(lsr_base_universe_d2_034_lsr_basefill_021):
    return _base_universe_d3(lsr_base_universe_d2_034_lsr_basefill_021, 34)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_034_lsr_basefill_021'] = {'inputs': ['lsr_base_universe_d2_034_lsr_basefill_021'], 'func': lsr_base_universe_d3_034_lsr_basefill_021}


def lsr_base_universe_d3_035_lsr_basefill_022(lsr_base_universe_d2_035_lsr_basefill_022):
    return _base_universe_d3(lsr_base_universe_d2_035_lsr_basefill_022, 35)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_035_lsr_basefill_022'] = {'inputs': ['lsr_base_universe_d2_035_lsr_basefill_022'], 'func': lsr_base_universe_d3_035_lsr_basefill_022}


def lsr_base_universe_d3_036_lsr_basefill_023(lsr_base_universe_d2_036_lsr_basefill_023):
    return _base_universe_d3(lsr_base_universe_d2_036_lsr_basefill_023, 36)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_036_lsr_basefill_023'] = {'inputs': ['lsr_base_universe_d2_036_lsr_basefill_023'], 'func': lsr_base_universe_d3_036_lsr_basefill_023}


def lsr_base_universe_d3_037_lsr_basefill_024(lsr_base_universe_d2_037_lsr_basefill_024):
    return _base_universe_d3(lsr_base_universe_d2_037_lsr_basefill_024, 37)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_037_lsr_basefill_024'] = {'inputs': ['lsr_base_universe_d2_037_lsr_basefill_024'], 'func': lsr_base_universe_d3_037_lsr_basefill_024}


def lsr_base_universe_d3_038_lsr_basefill_028(lsr_base_universe_d2_038_lsr_basefill_028):
    return _base_universe_d3(lsr_base_universe_d2_038_lsr_basefill_028, 38)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_038_lsr_basefill_028'] = {'inputs': ['lsr_base_universe_d2_038_lsr_basefill_028'], 'func': lsr_base_universe_d3_038_lsr_basefill_028}


def lsr_base_universe_d3_039_lsr_basefill_029(lsr_base_universe_d2_039_lsr_basefill_029):
    return _base_universe_d3(lsr_base_universe_d2_039_lsr_basefill_029, 39)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_039_lsr_basefill_029'] = {'inputs': ['lsr_base_universe_d2_039_lsr_basefill_029'], 'func': lsr_base_universe_d3_039_lsr_basefill_029}


def lsr_base_universe_d3_040_lsr_basefill_030(lsr_base_universe_d2_040_lsr_basefill_030):
    return _base_universe_d3(lsr_base_universe_d2_040_lsr_basefill_030, 40)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_040_lsr_basefill_030'] = {'inputs': ['lsr_base_universe_d2_040_lsr_basefill_030'], 'func': lsr_base_universe_d3_040_lsr_basefill_030}


def lsr_base_universe_d3_041_lsr_basefill_031(lsr_base_universe_d2_041_lsr_basefill_031):
    return _base_universe_d3(lsr_base_universe_d2_041_lsr_basefill_031, 41)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_041_lsr_basefill_031'] = {'inputs': ['lsr_base_universe_d2_041_lsr_basefill_031'], 'func': lsr_base_universe_d3_041_lsr_basefill_031}


def lsr_base_universe_d3_042_lsr_basefill_035(lsr_base_universe_d2_042_lsr_basefill_035):
    return _base_universe_d3(lsr_base_universe_d2_042_lsr_basefill_035, 42)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_042_lsr_basefill_035'] = {'inputs': ['lsr_base_universe_d2_042_lsr_basefill_035'], 'func': lsr_base_universe_d3_042_lsr_basefill_035}


def lsr_base_universe_d3_043_lsr_basefill_036(lsr_base_universe_d2_043_lsr_basefill_036):
    return _base_universe_d3(lsr_base_universe_d2_043_lsr_basefill_036, 43)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_043_lsr_basefill_036'] = {'inputs': ['lsr_base_universe_d2_043_lsr_basefill_036'], 'func': lsr_base_universe_d3_043_lsr_basefill_036}


def lsr_base_universe_d3_044_lsr_basefill_037(lsr_base_universe_d2_044_lsr_basefill_037):
    return _base_universe_d3(lsr_base_universe_d2_044_lsr_basefill_037, 44)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_044_lsr_basefill_037'] = {'inputs': ['lsr_base_universe_d2_044_lsr_basefill_037'], 'func': lsr_base_universe_d3_044_lsr_basefill_037}


def lsr_base_universe_d3_045_lsr_basefill_038(lsr_base_universe_d2_045_lsr_basefill_038):
    return _base_universe_d3(lsr_base_universe_d2_045_lsr_basefill_038, 45)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_045_lsr_basefill_038'] = {'inputs': ['lsr_base_universe_d2_045_lsr_basefill_038'], 'func': lsr_base_universe_d3_045_lsr_basefill_038}


def lsr_base_universe_d3_046_lsr_basefill_042(lsr_base_universe_d2_046_lsr_basefill_042):
    return _base_universe_d3(lsr_base_universe_d2_046_lsr_basefill_042, 46)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_046_lsr_basefill_042'] = {'inputs': ['lsr_base_universe_d2_046_lsr_basefill_042'], 'func': lsr_base_universe_d3_046_lsr_basefill_042}


def lsr_base_universe_d3_047_lsr_basefill_043(lsr_base_universe_d2_047_lsr_basefill_043):
    return _base_universe_d3(lsr_base_universe_d2_047_lsr_basefill_043, 47)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_047_lsr_basefill_043'] = {'inputs': ['lsr_base_universe_d2_047_lsr_basefill_043'], 'func': lsr_base_universe_d3_047_lsr_basefill_043}


def lsr_base_universe_d3_048_lsr_basefill_044(lsr_base_universe_d2_048_lsr_basefill_044):
    return _base_universe_d3(lsr_base_universe_d2_048_lsr_basefill_044, 48)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_048_lsr_basefill_044'] = {'inputs': ['lsr_base_universe_d2_048_lsr_basefill_044'], 'func': lsr_base_universe_d3_048_lsr_basefill_044}


def lsr_base_universe_d3_049_lsr_basefill_045(lsr_base_universe_d2_049_lsr_basefill_045):
    return _base_universe_d3(lsr_base_universe_d2_049_lsr_basefill_045, 49)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_049_lsr_basefill_045'] = {'inputs': ['lsr_base_universe_d2_049_lsr_basefill_045'], 'func': lsr_base_universe_d3_049_lsr_basefill_045}


def lsr_base_universe_d3_050_lsr_basefill_048(lsr_base_universe_d2_050_lsr_basefill_048):
    return _base_universe_d3(lsr_base_universe_d2_050_lsr_basefill_048, 50)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_050_lsr_basefill_048'] = {'inputs': ['lsr_base_universe_d2_050_lsr_basefill_048'], 'func': lsr_base_universe_d3_050_lsr_basefill_048}


def lsr_base_universe_d3_051_lsr_basefill_049(lsr_base_universe_d2_051_lsr_basefill_049):
    return _base_universe_d3(lsr_base_universe_d2_051_lsr_basefill_049, 51)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_051_lsr_basefill_049'] = {'inputs': ['lsr_base_universe_d2_051_lsr_basefill_049'], 'func': lsr_base_universe_d3_051_lsr_basefill_049}


def lsr_base_universe_d3_052_lsr_basefill_050(lsr_base_universe_d2_052_lsr_basefill_050):
    return _base_universe_d3(lsr_base_universe_d2_052_lsr_basefill_050, 52)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_052_lsr_basefill_050'] = {'inputs': ['lsr_base_universe_d2_052_lsr_basefill_050'], 'func': lsr_base_universe_d3_052_lsr_basefill_050}


def lsr_base_universe_d3_053_lsr_basefill_051(lsr_base_universe_d2_053_lsr_basefill_051):
    return _base_universe_d3(lsr_base_universe_d2_053_lsr_basefill_051, 53)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_053_lsr_basefill_051'] = {'inputs': ['lsr_base_universe_d2_053_lsr_basefill_051'], 'func': lsr_base_universe_d3_053_lsr_basefill_051}


def lsr_base_universe_d3_054_lsr_basefill_052(lsr_base_universe_d2_054_lsr_basefill_052):
    return _base_universe_d3(lsr_base_universe_d2_054_lsr_basefill_052, 54)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_054_lsr_basefill_052'] = {'inputs': ['lsr_base_universe_d2_054_lsr_basefill_052'], 'func': lsr_base_universe_d3_054_lsr_basefill_052}


def lsr_base_universe_d3_055_lsr_basefill_055(lsr_base_universe_d2_055_lsr_basefill_055):
    return _base_universe_d3(lsr_base_universe_d2_055_lsr_basefill_055, 55)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_055_lsr_basefill_055'] = {'inputs': ['lsr_base_universe_d2_055_lsr_basefill_055'], 'func': lsr_base_universe_d3_055_lsr_basefill_055}


def lsr_base_universe_d3_056_lsr_basefill_056(lsr_base_universe_d2_056_lsr_basefill_056):
    return _base_universe_d3(lsr_base_universe_d2_056_lsr_basefill_056, 56)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_056_lsr_basefill_056'] = {'inputs': ['lsr_base_universe_d2_056_lsr_basefill_056'], 'func': lsr_base_universe_d3_056_lsr_basefill_056}


def lsr_base_universe_d3_057_lsr_basefill_057(lsr_base_universe_d2_057_lsr_basefill_057):
    return _base_universe_d3(lsr_base_universe_d2_057_lsr_basefill_057, 57)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_057_lsr_basefill_057'] = {'inputs': ['lsr_base_universe_d2_057_lsr_basefill_057'], 'func': lsr_base_universe_d3_057_lsr_basefill_057}


def lsr_base_universe_d3_058_lsr_basefill_058(lsr_base_universe_d2_058_lsr_basefill_058):
    return _base_universe_d3(lsr_base_universe_d2_058_lsr_basefill_058, 58)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_058_lsr_basefill_058'] = {'inputs': ['lsr_base_universe_d2_058_lsr_basefill_058'], 'func': lsr_base_universe_d3_058_lsr_basefill_058}


def lsr_base_universe_d3_059_lsr_basefill_059(lsr_base_universe_d2_059_lsr_basefill_059):
    return _base_universe_d3(lsr_base_universe_d2_059_lsr_basefill_059, 59)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_059_lsr_basefill_059'] = {'inputs': ['lsr_base_universe_d2_059_lsr_basefill_059'], 'func': lsr_base_universe_d3_059_lsr_basefill_059}


def lsr_base_universe_d3_060_lsr_basefill_062(lsr_base_universe_d2_060_lsr_basefill_062):
    return _base_universe_d3(lsr_base_universe_d2_060_lsr_basefill_062, 60)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_060_lsr_basefill_062'] = {'inputs': ['lsr_base_universe_d2_060_lsr_basefill_062'], 'func': lsr_base_universe_d3_060_lsr_basefill_062}


def lsr_base_universe_d3_061_lsr_basefill_063(lsr_base_universe_d2_061_lsr_basefill_063):
    return _base_universe_d3(lsr_base_universe_d2_061_lsr_basefill_063, 61)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_061_lsr_basefill_063'] = {'inputs': ['lsr_base_universe_d2_061_lsr_basefill_063'], 'func': lsr_base_universe_d3_061_lsr_basefill_063}


def lsr_base_universe_d3_062_lsr_basefill_064(lsr_base_universe_d2_062_lsr_basefill_064):
    return _base_universe_d3(lsr_base_universe_d2_062_lsr_basefill_064, 62)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_062_lsr_basefill_064'] = {'inputs': ['lsr_base_universe_d2_062_lsr_basefill_064'], 'func': lsr_base_universe_d3_062_lsr_basefill_064}


def lsr_base_universe_d3_063_lsr_basefill_065(lsr_base_universe_d2_063_lsr_basefill_065):
    return _base_universe_d3(lsr_base_universe_d2_063_lsr_basefill_065, 63)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_063_lsr_basefill_065'] = {'inputs': ['lsr_base_universe_d2_063_lsr_basefill_065'], 'func': lsr_base_universe_d3_063_lsr_basefill_065}


def lsr_base_universe_d3_064_lsr_basefill_066(lsr_base_universe_d2_064_lsr_basefill_066):
    return _base_universe_d3(lsr_base_universe_d2_064_lsr_basefill_066, 64)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_064_lsr_basefill_066'] = {'inputs': ['lsr_base_universe_d2_064_lsr_basefill_066'], 'func': lsr_base_universe_d3_064_lsr_basefill_066}


def lsr_base_universe_d3_065_lsr_basefill_067(lsr_base_universe_d2_065_lsr_basefill_067):
    return _base_universe_d3(lsr_base_universe_d2_065_lsr_basefill_067, 65)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_065_lsr_basefill_067'] = {'inputs': ['lsr_base_universe_d2_065_lsr_basefill_067'], 'func': lsr_base_universe_d3_065_lsr_basefill_067}


def lsr_base_universe_d3_066_lsr_basefill_069(lsr_base_universe_d2_066_lsr_basefill_069):
    return _base_universe_d3(lsr_base_universe_d2_066_lsr_basefill_069, 66)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_066_lsr_basefill_069'] = {'inputs': ['lsr_base_universe_d2_066_lsr_basefill_069'], 'func': lsr_base_universe_d3_066_lsr_basefill_069}


def lsr_base_universe_d3_067_lsr_basefill_070(lsr_base_universe_d2_067_lsr_basefill_070):
    return _base_universe_d3(lsr_base_universe_d2_067_lsr_basefill_070, 67)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_067_lsr_basefill_070'] = {'inputs': ['lsr_base_universe_d2_067_lsr_basefill_070'], 'func': lsr_base_universe_d3_067_lsr_basefill_070}


def lsr_base_universe_d3_068_lsr_basefill_071(lsr_base_universe_d2_068_lsr_basefill_071):
    return _base_universe_d3(lsr_base_universe_d2_068_lsr_basefill_071, 68)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_068_lsr_basefill_071'] = {'inputs': ['lsr_base_universe_d2_068_lsr_basefill_071'], 'func': lsr_base_universe_d3_068_lsr_basefill_071}


def lsr_base_universe_d3_069_lsr_basefill_072(lsr_base_universe_d2_069_lsr_basefill_072):
    return _base_universe_d3(lsr_base_universe_d2_069_lsr_basefill_072, 69)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_069_lsr_basefill_072'] = {'inputs': ['lsr_base_universe_d2_069_lsr_basefill_072'], 'func': lsr_base_universe_d3_069_lsr_basefill_072}


def lsr_base_universe_d3_070_lsr_basefill_073(lsr_base_universe_d2_070_lsr_basefill_073):
    return _base_universe_d3(lsr_base_universe_d2_070_lsr_basefill_073, 70)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_070_lsr_basefill_073'] = {'inputs': ['lsr_base_universe_d2_070_lsr_basefill_073'], 'func': lsr_base_universe_d3_070_lsr_basefill_073}


def lsr_base_universe_d3_071_lsr_basefill_074(lsr_base_universe_d2_071_lsr_basefill_074):
    return _base_universe_d3(lsr_base_universe_d2_071_lsr_basefill_074, 71)
LSR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lsr_base_universe_d3_071_lsr_basefill_074'] = {'inputs': ['lsr_base_universe_d2_071_lsr_basefill_074'], 'func': lsr_base_universe_d3_071_lsr_basefill_074}
