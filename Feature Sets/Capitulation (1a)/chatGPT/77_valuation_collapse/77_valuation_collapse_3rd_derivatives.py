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



def vcl_176_vcl_001_pe_compression_z_21_accel_1(vcl_151_vcl_001_pe_compression_z_21_roc_1):
    feature = _s(vcl_151_vcl_001_pe_compression_z_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vcl_177_vcl_007_earnings_yield_spike_252_accel_42(vcl_152_vcl_007_earnings_yield_spike_252_roc_42):
    feature = _s(vcl_152_vcl_007_earnings_yield_spike_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vcl_178_vcl_013_ev_marketcap_gap_1512_accel_126(vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126):
    feature = _s(vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vcl_179_vcl_019_ps_compression_z_84_accel_378(vcl_154_vcl_019_ps_compression_z_84_roc_378):
    feature = _s(vcl_154_vcl_019_ps_compression_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def vcl_180_vcl_025_pe_compression_z_756_accel_4(vcl_155_vcl_025_pe_compression_z_756_roc_4):
    feature = _s(vcl_155_vcl_025_pe_compression_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















VALUATION_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    'vcl_176_vcl_001_pe_compression_z_21_accel_1': {'inputs': ['vcl_151_vcl_001_pe_compression_z_21_roc_1'], 'func': vcl_176_vcl_001_pe_compression_z_21_accel_1},
    'vcl_177_vcl_007_earnings_yield_spike_252_accel_42': {'inputs': ['vcl_152_vcl_007_earnings_yield_spike_252_roc_42'], 'func': vcl_177_vcl_007_earnings_yield_spike_252_accel_42},
    'vcl_178_vcl_013_ev_marketcap_gap_1512_accel_126': {'inputs': ['vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126'], 'func': vcl_178_vcl_013_ev_marketcap_gap_1512_accel_126},
    'vcl_179_vcl_019_ps_compression_z_84_accel_378': {'inputs': ['vcl_154_vcl_019_ps_compression_z_84_roc_378'], 'func': vcl_179_vcl_019_ps_compression_z_84_accel_378},
    'vcl_180_vcl_025_pe_compression_z_756_accel_4': {'inputs': ['vcl_155_vcl_025_pe_compression_z_756_roc_4'], 'func': vcl_180_vcl_025_pe_compression_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vc_replacement_d3_001(vc_replacement_d2_001):
    feature = _clean(vc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_001'] = {'inputs': ['vc_replacement_d2_001'], 'func': vc_replacement_d3_001}


def vc_replacement_d3_002(vc_replacement_d2_002):
    feature = _clean(vc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_002'] = {'inputs': ['vc_replacement_d2_002'], 'func': vc_replacement_d3_002}


def vc_replacement_d3_003(vc_replacement_d2_003):
    feature = _clean(vc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_003'] = {'inputs': ['vc_replacement_d2_003'], 'func': vc_replacement_d3_003}


def vc_replacement_d3_004(vc_replacement_d2_004):
    feature = _clean(vc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_004'] = {'inputs': ['vc_replacement_d2_004'], 'func': vc_replacement_d3_004}


def vc_replacement_d3_005(vc_replacement_d2_005):
    feature = _clean(vc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_005'] = {'inputs': ['vc_replacement_d2_005'], 'func': vc_replacement_d3_005}


def vc_replacement_d3_006(vc_replacement_d2_006):
    feature = _clean(vc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_006'] = {'inputs': ['vc_replacement_d2_006'], 'func': vc_replacement_d3_006}


def vc_replacement_d3_007(vc_replacement_d2_007):
    feature = _clean(vc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_007'] = {'inputs': ['vc_replacement_d2_007'], 'func': vc_replacement_d3_007}


def vc_replacement_d3_008(vc_replacement_d2_008):
    feature = _clean(vc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_008'] = {'inputs': ['vc_replacement_d2_008'], 'func': vc_replacement_d3_008}


def vc_replacement_d3_009(vc_replacement_d2_009):
    feature = _clean(vc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_009'] = {'inputs': ['vc_replacement_d2_009'], 'func': vc_replacement_d3_009}


def vc_replacement_d3_010(vc_replacement_d2_010):
    feature = _clean(vc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_010'] = {'inputs': ['vc_replacement_d2_010'], 'func': vc_replacement_d3_010}


def vc_replacement_d3_011(vc_replacement_d2_011):
    feature = _clean(vc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_011'] = {'inputs': ['vc_replacement_d2_011'], 'func': vc_replacement_d3_011}


def vc_replacement_d3_012(vc_replacement_d2_012):
    feature = _clean(vc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_012'] = {'inputs': ['vc_replacement_d2_012'], 'func': vc_replacement_d3_012}


def vc_replacement_d3_013(vc_replacement_d2_013):
    feature = _clean(vc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_013'] = {'inputs': ['vc_replacement_d2_013'], 'func': vc_replacement_d3_013}


def vc_replacement_d3_014(vc_replacement_d2_014):
    feature = _clean(vc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_014'] = {'inputs': ['vc_replacement_d2_014'], 'func': vc_replacement_d3_014}


def vc_replacement_d3_015(vc_replacement_d2_015):
    feature = _clean(vc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_015'] = {'inputs': ['vc_replacement_d2_015'], 'func': vc_replacement_d3_015}


def vc_replacement_d3_016(vc_replacement_d2_016):
    feature = _clean(vc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_016'] = {'inputs': ['vc_replacement_d2_016'], 'func': vc_replacement_d3_016}


def vc_replacement_d3_017(vc_replacement_d2_017):
    feature = _clean(vc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_017'] = {'inputs': ['vc_replacement_d2_017'], 'func': vc_replacement_d3_017}


def vc_replacement_d3_018(vc_replacement_d2_018):
    feature = _clean(vc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_018'] = {'inputs': ['vc_replacement_d2_018'], 'func': vc_replacement_d3_018}


def vc_replacement_d3_019(vc_replacement_d2_019):
    feature = _clean(vc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_019'] = {'inputs': ['vc_replacement_d2_019'], 'func': vc_replacement_d3_019}


def vc_replacement_d3_020(vc_replacement_d2_020):
    feature = _clean(vc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_020'] = {'inputs': ['vc_replacement_d2_020'], 'func': vc_replacement_d3_020}


def vc_replacement_d3_021(vc_replacement_d2_021):
    feature = _clean(vc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_021'] = {'inputs': ['vc_replacement_d2_021'], 'func': vc_replacement_d3_021}


def vc_replacement_d3_022(vc_replacement_d2_022):
    feature = _clean(vc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_022'] = {'inputs': ['vc_replacement_d2_022'], 'func': vc_replacement_d3_022}


def vc_replacement_d3_023(vc_replacement_d2_023):
    feature = _clean(vc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_023'] = {'inputs': ['vc_replacement_d2_023'], 'func': vc_replacement_d3_023}


def vc_replacement_d3_024(vc_replacement_d2_024):
    feature = _clean(vc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_024'] = {'inputs': ['vc_replacement_d2_024'], 'func': vc_replacement_d3_024}


def vc_replacement_d3_025(vc_replacement_d2_025):
    feature = _clean(vc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_025'] = {'inputs': ['vc_replacement_d2_025'], 'func': vc_replacement_d3_025}


def vc_replacement_d3_026(vc_replacement_d2_026):
    feature = _clean(vc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_026'] = {'inputs': ['vc_replacement_d2_026'], 'func': vc_replacement_d3_026}


def vc_replacement_d3_027(vc_replacement_d2_027):
    feature = _clean(vc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_027'] = {'inputs': ['vc_replacement_d2_027'], 'func': vc_replacement_d3_027}


def vc_replacement_d3_028(vc_replacement_d2_028):
    feature = _clean(vc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_028'] = {'inputs': ['vc_replacement_d2_028'], 'func': vc_replacement_d3_028}


def vc_replacement_d3_029(vc_replacement_d2_029):
    feature = _clean(vc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_029'] = {'inputs': ['vc_replacement_d2_029'], 'func': vc_replacement_d3_029}


def vc_replacement_d3_030(vc_replacement_d2_030):
    feature = _clean(vc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_030'] = {'inputs': ['vc_replacement_d2_030'], 'func': vc_replacement_d3_030}


def vc_replacement_d3_031(vc_replacement_d2_031):
    feature = _clean(vc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_031'] = {'inputs': ['vc_replacement_d2_031'], 'func': vc_replacement_d3_031}


def vc_replacement_d3_032(vc_replacement_d2_032):
    feature = _clean(vc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_032'] = {'inputs': ['vc_replacement_d2_032'], 'func': vc_replacement_d3_032}


def vc_replacement_d3_033(vc_replacement_d2_033):
    feature = _clean(vc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_033'] = {'inputs': ['vc_replacement_d2_033'], 'func': vc_replacement_d3_033}


def vc_replacement_d3_034(vc_replacement_d2_034):
    feature = _clean(vc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_034'] = {'inputs': ['vc_replacement_d2_034'], 'func': vc_replacement_d3_034}


def vc_replacement_d3_035(vc_replacement_d2_035):
    feature = _clean(vc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_035'] = {'inputs': ['vc_replacement_d2_035'], 'func': vc_replacement_d3_035}


def vc_replacement_d3_036(vc_replacement_d2_036):
    feature = _clean(vc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_036'] = {'inputs': ['vc_replacement_d2_036'], 'func': vc_replacement_d3_036}


def vc_replacement_d3_037(vc_replacement_d2_037):
    feature = _clean(vc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_037'] = {'inputs': ['vc_replacement_d2_037'], 'func': vc_replacement_d3_037}


def vc_replacement_d3_038(vc_replacement_d2_038):
    feature = _clean(vc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_038'] = {'inputs': ['vc_replacement_d2_038'], 'func': vc_replacement_d3_038}


def vc_replacement_d3_039(vc_replacement_d2_039):
    feature = _clean(vc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_039'] = {'inputs': ['vc_replacement_d2_039'], 'func': vc_replacement_d3_039}


def vc_replacement_d3_040(vc_replacement_d2_040):
    feature = _clean(vc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_040'] = {'inputs': ['vc_replacement_d2_040'], 'func': vc_replacement_d3_040}


def vc_replacement_d3_041(vc_replacement_d2_041):
    feature = _clean(vc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_041'] = {'inputs': ['vc_replacement_d2_041'], 'func': vc_replacement_d3_041}


def vc_replacement_d3_042(vc_replacement_d2_042):
    feature = _clean(vc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_042'] = {'inputs': ['vc_replacement_d2_042'], 'func': vc_replacement_d3_042}


def vc_replacement_d3_043(vc_replacement_d2_043):
    feature = _clean(vc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_043'] = {'inputs': ['vc_replacement_d2_043'], 'func': vc_replacement_d3_043}


def vc_replacement_d3_044(vc_replacement_d2_044):
    feature = _clean(vc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_044'] = {'inputs': ['vc_replacement_d2_044'], 'func': vc_replacement_d3_044}


def vc_replacement_d3_045(vc_replacement_d2_045):
    feature = _clean(vc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_045'] = {'inputs': ['vc_replacement_d2_045'], 'func': vc_replacement_d3_045}


def vc_replacement_d3_046(vc_replacement_d2_046):
    feature = _clean(vc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_046'] = {'inputs': ['vc_replacement_d2_046'], 'func': vc_replacement_d3_046}


def vc_replacement_d3_047(vc_replacement_d2_047):
    feature = _clean(vc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_047'] = {'inputs': ['vc_replacement_d2_047'], 'func': vc_replacement_d3_047}


def vc_replacement_d3_048(vc_replacement_d2_048):
    feature = _clean(vc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_048'] = {'inputs': ['vc_replacement_d2_048'], 'func': vc_replacement_d3_048}


def vc_replacement_d3_049(vc_replacement_d2_049):
    feature = _clean(vc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_049'] = {'inputs': ['vc_replacement_d2_049'], 'func': vc_replacement_d3_049}


def vc_replacement_d3_050(vc_replacement_d2_050):
    feature = _clean(vc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_050'] = {'inputs': ['vc_replacement_d2_050'], 'func': vc_replacement_d3_050}


def vc_replacement_d3_051(vc_replacement_d2_051):
    feature = _clean(vc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_051'] = {'inputs': ['vc_replacement_d2_051'], 'func': vc_replacement_d3_051}


def vc_replacement_d3_052(vc_replacement_d2_052):
    feature = _clean(vc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_052'] = {'inputs': ['vc_replacement_d2_052'], 'func': vc_replacement_d3_052}


def vc_replacement_d3_053(vc_replacement_d2_053):
    feature = _clean(vc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_053'] = {'inputs': ['vc_replacement_d2_053'], 'func': vc_replacement_d3_053}


def vc_replacement_d3_054(vc_replacement_d2_054):
    feature = _clean(vc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_054'] = {'inputs': ['vc_replacement_d2_054'], 'func': vc_replacement_d3_054}


def vc_replacement_d3_055(vc_replacement_d2_055):
    feature = _clean(vc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_055'] = {'inputs': ['vc_replacement_d2_055'], 'func': vc_replacement_d3_055}


def vc_replacement_d3_056(vc_replacement_d2_056):
    feature = _clean(vc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_056'] = {'inputs': ['vc_replacement_d2_056'], 'func': vc_replacement_d3_056}


def vc_replacement_d3_057(vc_replacement_d2_057):
    feature = _clean(vc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_057'] = {'inputs': ['vc_replacement_d2_057'], 'func': vc_replacement_d3_057}


def vc_replacement_d3_058(vc_replacement_d2_058):
    feature = _clean(vc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_058'] = {'inputs': ['vc_replacement_d2_058'], 'func': vc_replacement_d3_058}


def vc_replacement_d3_059(vc_replacement_d2_059):
    feature = _clean(vc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_059'] = {'inputs': ['vc_replacement_d2_059'], 'func': vc_replacement_d3_059}


def vc_replacement_d3_060(vc_replacement_d2_060):
    feature = _clean(vc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_060'] = {'inputs': ['vc_replacement_d2_060'], 'func': vc_replacement_d3_060}


def vc_replacement_d3_061(vc_replacement_d2_061):
    feature = _clean(vc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_061'] = {'inputs': ['vc_replacement_d2_061'], 'func': vc_replacement_d3_061}


def vc_replacement_d3_062(vc_replacement_d2_062):
    feature = _clean(vc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_062'] = {'inputs': ['vc_replacement_d2_062'], 'func': vc_replacement_d3_062}


def vc_replacement_d3_063(vc_replacement_d2_063):
    feature = _clean(vc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_063'] = {'inputs': ['vc_replacement_d2_063'], 'func': vc_replacement_d3_063}


def vc_replacement_d3_064(vc_replacement_d2_064):
    feature = _clean(vc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_064'] = {'inputs': ['vc_replacement_d2_064'], 'func': vc_replacement_d3_064}


def vc_replacement_d3_065(vc_replacement_d2_065):
    feature = _clean(vc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_065'] = {'inputs': ['vc_replacement_d2_065'], 'func': vc_replacement_d3_065}


def vc_replacement_d3_066(vc_replacement_d2_066):
    feature = _clean(vc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_066'] = {'inputs': ['vc_replacement_d2_066'], 'func': vc_replacement_d3_066}


def vc_replacement_d3_067(vc_replacement_d2_067):
    feature = _clean(vc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_067'] = {'inputs': ['vc_replacement_d2_067'], 'func': vc_replacement_d3_067}


def vc_replacement_d3_068(vc_replacement_d2_068):
    feature = _clean(vc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_068'] = {'inputs': ['vc_replacement_d2_068'], 'func': vc_replacement_d3_068}


def vc_replacement_d3_069(vc_replacement_d2_069):
    feature = _clean(vc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_069'] = {'inputs': ['vc_replacement_d2_069'], 'func': vc_replacement_d3_069}


def vc_replacement_d3_070(vc_replacement_d2_070):
    feature = _clean(vc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_070'] = {'inputs': ['vc_replacement_d2_070'], 'func': vc_replacement_d3_070}


def vc_replacement_d3_071(vc_replacement_d2_071):
    feature = _clean(vc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_071'] = {'inputs': ['vc_replacement_d2_071'], 'func': vc_replacement_d3_071}


def vc_replacement_d3_072(vc_replacement_d2_072):
    feature = _clean(vc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_072'] = {'inputs': ['vc_replacement_d2_072'], 'func': vc_replacement_d3_072}


def vc_replacement_d3_073(vc_replacement_d2_073):
    feature = _clean(vc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_073'] = {'inputs': ['vc_replacement_d2_073'], 'func': vc_replacement_d3_073}


def vc_replacement_d3_074(vc_replacement_d2_074):
    feature = _clean(vc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_074'] = {'inputs': ['vc_replacement_d2_074'], 'func': vc_replacement_d3_074}


def vc_replacement_d3_075(vc_replacement_d2_075):
    feature = _clean(vc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_075'] = {'inputs': ['vc_replacement_d2_075'], 'func': vc_replacement_d3_075}


def vc_replacement_d3_076(vc_replacement_d2_076):
    feature = _clean(vc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_076'] = {'inputs': ['vc_replacement_d2_076'], 'func': vc_replacement_d3_076}


def vc_replacement_d3_077(vc_replacement_d2_077):
    feature = _clean(vc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_077'] = {'inputs': ['vc_replacement_d2_077'], 'func': vc_replacement_d3_077}


def vc_replacement_d3_078(vc_replacement_d2_078):
    feature = _clean(vc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_078'] = {'inputs': ['vc_replacement_d2_078'], 'func': vc_replacement_d3_078}


def vc_replacement_d3_079(vc_replacement_d2_079):
    feature = _clean(vc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_079'] = {'inputs': ['vc_replacement_d2_079'], 'func': vc_replacement_d3_079}


def vc_replacement_d3_080(vc_replacement_d2_080):
    feature = _clean(vc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_080'] = {'inputs': ['vc_replacement_d2_080'], 'func': vc_replacement_d3_080}


def vc_replacement_d3_081(vc_replacement_d2_081):
    feature = _clean(vc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_081'] = {'inputs': ['vc_replacement_d2_081'], 'func': vc_replacement_d3_081}


def vc_replacement_d3_082(vc_replacement_d2_082):
    feature = _clean(vc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_082'] = {'inputs': ['vc_replacement_d2_082'], 'func': vc_replacement_d3_082}


def vc_replacement_d3_083(vc_replacement_d2_083):
    feature = _clean(vc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_083'] = {'inputs': ['vc_replacement_d2_083'], 'func': vc_replacement_d3_083}


def vc_replacement_d3_084(vc_replacement_d2_084):
    feature = _clean(vc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_084'] = {'inputs': ['vc_replacement_d2_084'], 'func': vc_replacement_d3_084}


def vc_replacement_d3_085(vc_replacement_d2_085):
    feature = _clean(vc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_085'] = {'inputs': ['vc_replacement_d2_085'], 'func': vc_replacement_d3_085}


def vc_replacement_d3_086(vc_replacement_d2_086):
    feature = _clean(vc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_086'] = {'inputs': ['vc_replacement_d2_086'], 'func': vc_replacement_d3_086}


def vc_replacement_d3_087(vc_replacement_d2_087):
    feature = _clean(vc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_087'] = {'inputs': ['vc_replacement_d2_087'], 'func': vc_replacement_d3_087}


def vc_replacement_d3_088(vc_replacement_d2_088):
    feature = _clean(vc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_088'] = {'inputs': ['vc_replacement_d2_088'], 'func': vc_replacement_d3_088}


def vc_replacement_d3_089(vc_replacement_d2_089):
    feature = _clean(vc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_089'] = {'inputs': ['vc_replacement_d2_089'], 'func': vc_replacement_d3_089}


def vc_replacement_d3_090(vc_replacement_d2_090):
    feature = _clean(vc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_090'] = {'inputs': ['vc_replacement_d2_090'], 'func': vc_replacement_d3_090}


def vc_replacement_d3_091(vc_replacement_d2_091):
    feature = _clean(vc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_091'] = {'inputs': ['vc_replacement_d2_091'], 'func': vc_replacement_d3_091}


def vc_replacement_d3_092(vc_replacement_d2_092):
    feature = _clean(vc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_092'] = {'inputs': ['vc_replacement_d2_092'], 'func': vc_replacement_d3_092}


def vc_replacement_d3_093(vc_replacement_d2_093):
    feature = _clean(vc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_093'] = {'inputs': ['vc_replacement_d2_093'], 'func': vc_replacement_d3_093}


def vc_replacement_d3_094(vc_replacement_d2_094):
    feature = _clean(vc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_094'] = {'inputs': ['vc_replacement_d2_094'], 'func': vc_replacement_d3_094}


def vc_replacement_d3_095(vc_replacement_d2_095):
    feature = _clean(vc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_095'] = {'inputs': ['vc_replacement_d2_095'], 'func': vc_replacement_d3_095}


def vc_replacement_d3_096(vc_replacement_d2_096):
    feature = _clean(vc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_096'] = {'inputs': ['vc_replacement_d2_096'], 'func': vc_replacement_d3_096}


def vc_replacement_d3_097(vc_replacement_d2_097):
    feature = _clean(vc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_097'] = {'inputs': ['vc_replacement_d2_097'], 'func': vc_replacement_d3_097}


def vc_replacement_d3_098(vc_replacement_d2_098):
    feature = _clean(vc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_098'] = {'inputs': ['vc_replacement_d2_098'], 'func': vc_replacement_d3_098}


def vc_replacement_d3_099(vc_replacement_d2_099):
    feature = _clean(vc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_099'] = {'inputs': ['vc_replacement_d2_099'], 'func': vc_replacement_d3_099}


def vc_replacement_d3_100(vc_replacement_d2_100):
    feature = _clean(vc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_100'] = {'inputs': ['vc_replacement_d2_100'], 'func': vc_replacement_d3_100}


def vc_replacement_d3_101(vc_replacement_d2_101):
    feature = _clean(vc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_101'] = {'inputs': ['vc_replacement_d2_101'], 'func': vc_replacement_d3_101}


def vc_replacement_d3_102(vc_replacement_d2_102):
    feature = _clean(vc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_102'] = {'inputs': ['vc_replacement_d2_102'], 'func': vc_replacement_d3_102}


def vc_replacement_d3_103(vc_replacement_d2_103):
    feature = _clean(vc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_103'] = {'inputs': ['vc_replacement_d2_103'], 'func': vc_replacement_d3_103}


def vc_replacement_d3_104(vc_replacement_d2_104):
    feature = _clean(vc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_104'] = {'inputs': ['vc_replacement_d2_104'], 'func': vc_replacement_d3_104}


def vc_replacement_d3_105(vc_replacement_d2_105):
    feature = _clean(vc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_105'] = {'inputs': ['vc_replacement_d2_105'], 'func': vc_replacement_d3_105}


def vc_replacement_d3_106(vc_replacement_d2_106):
    feature = _clean(vc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_106'] = {'inputs': ['vc_replacement_d2_106'], 'func': vc_replacement_d3_106}


def vc_replacement_d3_107(vc_replacement_d2_107):
    feature = _clean(vc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_107'] = {'inputs': ['vc_replacement_d2_107'], 'func': vc_replacement_d3_107}


def vc_replacement_d3_108(vc_replacement_d2_108):
    feature = _clean(vc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_108'] = {'inputs': ['vc_replacement_d2_108'], 'func': vc_replacement_d3_108}


def vc_replacement_d3_109(vc_replacement_d2_109):
    feature = _clean(vc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_109'] = {'inputs': ['vc_replacement_d2_109'], 'func': vc_replacement_d3_109}


def vc_replacement_d3_110(vc_replacement_d2_110):
    feature = _clean(vc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_110'] = {'inputs': ['vc_replacement_d2_110'], 'func': vc_replacement_d3_110}


def vc_replacement_d3_111(vc_replacement_d2_111):
    feature = _clean(vc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_111'] = {'inputs': ['vc_replacement_d2_111'], 'func': vc_replacement_d3_111}


def vc_replacement_d3_112(vc_replacement_d2_112):
    feature = _clean(vc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_112'] = {'inputs': ['vc_replacement_d2_112'], 'func': vc_replacement_d3_112}


def vc_replacement_d3_113(vc_replacement_d2_113):
    feature = _clean(vc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_113'] = {'inputs': ['vc_replacement_d2_113'], 'func': vc_replacement_d3_113}


def vc_replacement_d3_114(vc_replacement_d2_114):
    feature = _clean(vc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_114'] = {'inputs': ['vc_replacement_d2_114'], 'func': vc_replacement_d3_114}


def vc_replacement_d3_115(vc_replacement_d2_115):
    feature = _clean(vc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_115'] = {'inputs': ['vc_replacement_d2_115'], 'func': vc_replacement_d3_115}


def vc_replacement_d3_116(vc_replacement_d2_116):
    feature = _clean(vc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_116'] = {'inputs': ['vc_replacement_d2_116'], 'func': vc_replacement_d3_116}


def vc_replacement_d3_117(vc_replacement_d2_117):
    feature = _clean(vc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_117'] = {'inputs': ['vc_replacement_d2_117'], 'func': vc_replacement_d3_117}


def vc_replacement_d3_118(vc_replacement_d2_118):
    feature = _clean(vc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_118'] = {'inputs': ['vc_replacement_d2_118'], 'func': vc_replacement_d3_118}


def vc_replacement_d3_119(vc_replacement_d2_119):
    feature = _clean(vc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_119'] = {'inputs': ['vc_replacement_d2_119'], 'func': vc_replacement_d3_119}


def vc_replacement_d3_120(vc_replacement_d2_120):
    feature = _clean(vc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_120'] = {'inputs': ['vc_replacement_d2_120'], 'func': vc_replacement_d3_120}


def vc_replacement_d3_121(vc_replacement_d2_121):
    feature = _clean(vc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_121'] = {'inputs': ['vc_replacement_d2_121'], 'func': vc_replacement_d3_121}


def vc_replacement_d3_122(vc_replacement_d2_122):
    feature = _clean(vc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_122'] = {'inputs': ['vc_replacement_d2_122'], 'func': vc_replacement_d3_122}


def vc_replacement_d3_123(vc_replacement_d2_123):
    feature = _clean(vc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_123'] = {'inputs': ['vc_replacement_d2_123'], 'func': vc_replacement_d3_123}


def vc_replacement_d3_124(vc_replacement_d2_124):
    feature = _clean(vc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_124'] = {'inputs': ['vc_replacement_d2_124'], 'func': vc_replacement_d3_124}


def vc_replacement_d3_125(vc_replacement_d2_125):
    feature = _clean(vc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_125'] = {'inputs': ['vc_replacement_d2_125'], 'func': vc_replacement_d3_125}


def vc_replacement_d3_126(vc_replacement_d2_126):
    feature = _clean(vc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_126'] = {'inputs': ['vc_replacement_d2_126'], 'func': vc_replacement_d3_126}


def vc_replacement_d3_127(vc_replacement_d2_127):
    feature = _clean(vc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_127'] = {'inputs': ['vc_replacement_d2_127'], 'func': vc_replacement_d3_127}


def vc_replacement_d3_128(vc_replacement_d2_128):
    feature = _clean(vc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_128'] = {'inputs': ['vc_replacement_d2_128'], 'func': vc_replacement_d3_128}


def vc_replacement_d3_129(vc_replacement_d2_129):
    feature = _clean(vc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_129'] = {'inputs': ['vc_replacement_d2_129'], 'func': vc_replacement_d3_129}


def vc_replacement_d3_130(vc_replacement_d2_130):
    feature = _clean(vc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_130'] = {'inputs': ['vc_replacement_d2_130'], 'func': vc_replacement_d3_130}


def vc_replacement_d3_131(vc_replacement_d2_131):
    feature = _clean(vc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_131'] = {'inputs': ['vc_replacement_d2_131'], 'func': vc_replacement_d3_131}


def vc_replacement_d3_132(vc_replacement_d2_132):
    feature = _clean(vc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_132'] = {'inputs': ['vc_replacement_d2_132'], 'func': vc_replacement_d3_132}


def vc_replacement_d3_133(vc_replacement_d2_133):
    feature = _clean(vc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_133'] = {'inputs': ['vc_replacement_d2_133'], 'func': vc_replacement_d3_133}


def vc_replacement_d3_134(vc_replacement_d2_134):
    feature = _clean(vc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_134'] = {'inputs': ['vc_replacement_d2_134'], 'func': vc_replacement_d3_134}


def vc_replacement_d3_135(vc_replacement_d2_135):
    feature = _clean(vc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_135'] = {'inputs': ['vc_replacement_d2_135'], 'func': vc_replacement_d3_135}


def vc_replacement_d3_136(vc_replacement_d2_136):
    feature = _clean(vc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_136'] = {'inputs': ['vc_replacement_d2_136'], 'func': vc_replacement_d3_136}


def vc_replacement_d3_137(vc_replacement_d2_137):
    feature = _clean(vc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_137'] = {'inputs': ['vc_replacement_d2_137'], 'func': vc_replacement_d3_137}


def vc_replacement_d3_138(vc_replacement_d2_138):
    feature = _clean(vc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_138'] = {'inputs': ['vc_replacement_d2_138'], 'func': vc_replacement_d3_138}


# Third-derivative extensions for repaired first-base features.
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vcl_base_universe_d3_001_vcl_002_pb_compression_z_42(vcl_base_universe_d2_001_vcl_002_pb_compression_z_42):
    return _base_universe_d3(vcl_base_universe_d2_001_vcl_002_pb_compression_z_42, 1)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_001_vcl_002_pb_compression_z_42'] = {'inputs': ['vcl_base_universe_d2_001_vcl_002_pb_compression_z_42'], 'func': vcl_base_universe_d3_001_vcl_002_pb_compression_z_42}


def vcl_base_universe_d3_002_vcl_003_ps_compression_z_63(vcl_base_universe_d2_002_vcl_003_ps_compression_z_63):
    return _base_universe_d3(vcl_base_universe_d2_002_vcl_003_ps_compression_z_63, 2)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_002_vcl_003_ps_compression_z_63'] = {'inputs': ['vcl_base_universe_d2_002_vcl_003_ps_compression_z_63'], 'func': vcl_base_universe_d3_002_vcl_003_ps_compression_z_63}


def vcl_base_universe_d3_003_vcl_005_ev_marketcap_gap_126(vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126):
    return _base_universe_d3(vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126, 3)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_003_vcl_005_ev_marketcap_gap_126'] = {'inputs': ['vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126'], 'func': vcl_base_universe_d3_003_vcl_005_ev_marketcap_gap_126}


def vcl_base_universe_d3_004_vcl_006_dividend_yield_spike_189(vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189):
    return _base_universe_d3(vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189, 4)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_004_vcl_006_dividend_yield_spike_189'] = {'inputs': ['vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189'], 'func': vcl_base_universe_d3_004_vcl_006_dividend_yield_spike_189}


def vcl_base_universe_d3_005_vcl_008_valuation_history_depth_378(vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378):
    return _base_universe_d3(vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378, 5)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_005_vcl_008_valuation_history_depth_378'] = {'inputs': ['vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378'], 'func': vcl_base_universe_d3_005_vcl_008_valuation_history_depth_378}


def vcl_base_universe_d3_006_vcl_009_pe_compression_z_504(vcl_base_universe_d2_006_vcl_009_pe_compression_z_504):
    return _base_universe_d3(vcl_base_universe_d2_006_vcl_009_pe_compression_z_504, 6)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_006_vcl_009_pe_compression_z_504'] = {'inputs': ['vcl_base_universe_d2_006_vcl_009_pe_compression_z_504'], 'func': vcl_base_universe_d3_006_vcl_009_pe_compression_z_504}


def vcl_base_universe_d3_007_vcl_010_pb_compression_z_756(vcl_base_universe_d2_007_vcl_010_pb_compression_z_756):
    return _base_universe_d3(vcl_base_universe_d2_007_vcl_010_pb_compression_z_756, 7)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_007_vcl_010_pb_compression_z_756'] = {'inputs': ['vcl_base_universe_d2_007_vcl_010_pb_compression_z_756'], 'func': vcl_base_universe_d3_007_vcl_010_pb_compression_z_756}


def vcl_base_universe_d3_008_vcl_011_ps_compression_z_1008(vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008):
    return _base_universe_d3(vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008, 8)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_008_vcl_011_ps_compression_z_1008'] = {'inputs': ['vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008'], 'func': vcl_base_universe_d3_008_vcl_011_ps_compression_z_1008}


def vcl_base_universe_d3_009_vcl_014_dividend_yield_spike_63(vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63):
    return _base_universe_d3(vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63, 9)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_009_vcl_014_dividend_yield_spike_63'] = {'inputs': ['vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63'], 'func': vcl_base_universe_d3_009_vcl_014_dividend_yield_spike_63}


def vcl_base_universe_d3_010_vcl_016_valuation_history_depth_21(vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21):
    return _base_universe_d3(vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21, 10)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_010_vcl_016_valuation_history_depth_21'] = {'inputs': ['vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21'], 'func': vcl_base_universe_d3_010_vcl_016_valuation_history_depth_21}


def vcl_base_universe_d3_011_vcl_021_ev_marketcap_gap_189(vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189):
    return _base_universe_d3(vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189, 11)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_011_vcl_021_ev_marketcap_gap_189'] = {'inputs': ['vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189'], 'func': vcl_base_universe_d3_011_vcl_021_ev_marketcap_gap_189}


def vcl_base_universe_d3_012_vcl_023_earnings_yield_spike_378(vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378):
    return _base_universe_d3(vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378, 12)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_012_vcl_023_earnings_yield_spike_378'] = {'inputs': ['vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378'], 'func': vcl_base_universe_d3_012_vcl_023_earnings_yield_spike_378}


def vcl_base_universe_d3_013_vcl_024_valuation_history_depth_504(vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504):
    return _base_universe_d3(vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504, 13)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_013_vcl_024_valuation_history_depth_504'] = {'inputs': ['vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504'], 'func': vcl_base_universe_d3_013_vcl_024_valuation_history_depth_504}


def vcl_base_universe_d3_014_vcl_027_ps_compression_z_1260(vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260):
    return _base_universe_d3(vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260, 14)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_014_vcl_027_ps_compression_z_1260'] = {'inputs': ['vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260'], 'func': vcl_base_universe_d3_014_vcl_027_ps_compression_z_1260}


def vcl_base_universe_d3_015_vcl_029_ev_marketcap_gap_63(vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63):
    return _base_universe_d3(vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63, 15)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_015_vcl_029_ev_marketcap_gap_63'] = {'inputs': ['vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63'], 'func': vcl_base_universe_d3_015_vcl_029_ev_marketcap_gap_63}


def vcl_base_universe_d3_016_vcl_031_earnings_yield_spike_21(vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21):
    return _base_universe_d3(vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21, 16)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_016_vcl_031_earnings_yield_spike_21'] = {'inputs': ['vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21'], 'func': vcl_base_universe_d3_016_vcl_031_earnings_yield_spike_21}


def vcl_base_universe_d3_017_vcl_032_valuation_history_depth_42(vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42):
    return _base_universe_d3(vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42, 17)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_017_vcl_032_valuation_history_depth_42'] = {'inputs': ['vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42'], 'func': vcl_base_universe_d3_017_vcl_032_valuation_history_depth_42}


def vcl_base_universe_d3_018_vcl_035_ps_compression_z_126(vcl_base_universe_d2_018_vcl_035_ps_compression_z_126):
    return _base_universe_d3(vcl_base_universe_d2_018_vcl_035_ps_compression_z_126, 18)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_018_vcl_035_ps_compression_z_126'] = {'inputs': ['vcl_base_universe_d2_018_vcl_035_ps_compression_z_126'], 'func': vcl_base_universe_d3_018_vcl_035_ps_compression_z_126}


def vcl_base_universe_d3_019_vcl_037_ev_marketcap_gap_252(vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252):
    return _base_universe_d3(vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252, 19)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_019_vcl_037_ev_marketcap_gap_252'] = {'inputs': ['vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252'], 'func': vcl_base_universe_d3_019_vcl_037_ev_marketcap_gap_252}


def vcl_base_universe_d3_020_vcl_039_earnings_yield_spike_504(vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504):
    return _base_universe_d3(vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504, 20)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_020_vcl_039_earnings_yield_spike_504'] = {'inputs': ['vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504'], 'func': vcl_base_universe_d3_020_vcl_039_earnings_yield_spike_504}


def vcl_base_universe_d3_021_vcl_040_valuation_history_depth_756(vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756):
    return _base_universe_d3(vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756, 21)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_021_vcl_040_valuation_history_depth_756'] = {'inputs': ['vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756'], 'func': vcl_base_universe_d3_021_vcl_040_valuation_history_depth_756}


def vcl_base_universe_d3_022_vcl_043_ps_compression_z_1512(vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512):
    return _base_universe_d3(vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512, 22)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_022_vcl_043_ps_compression_z_1512'] = {'inputs': ['vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512'], 'func': vcl_base_universe_d3_022_vcl_043_ps_compression_z_1512}


def vcl_base_universe_d3_023_vcl_047_earnings_yield_spike_42(vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42):
    return _base_universe_d3(vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42, 23)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_023_vcl_047_earnings_yield_spike_42'] = {'inputs': ['vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42'], 'func': vcl_base_universe_d3_023_vcl_047_earnings_yield_spike_42}


def vcl_base_universe_d3_024_vcl_048_valuation_history_depth_63(vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63):
    return _base_universe_d3(vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63, 24)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_024_vcl_048_valuation_history_depth_63'] = {'inputs': ['vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63'], 'func': vcl_base_universe_d3_024_vcl_048_valuation_history_depth_63}


def vcl_base_universe_d3_025_vcl_051_ps_compression_z_189(vcl_base_universe_d2_025_vcl_051_ps_compression_z_189):
    return _base_universe_d3(vcl_base_universe_d2_025_vcl_051_ps_compression_z_189, 25)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_025_vcl_051_ps_compression_z_189'] = {'inputs': ['vcl_base_universe_d2_025_vcl_051_ps_compression_z_189'], 'func': vcl_base_universe_d3_025_vcl_051_ps_compression_z_189}


def vcl_base_universe_d3_026_vcl_053_ev_marketcap_gap_378(vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378):
    return _base_universe_d3(vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378, 26)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_026_vcl_053_ev_marketcap_gap_378'] = {'inputs': ['vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378'], 'func': vcl_base_universe_d3_026_vcl_053_ev_marketcap_gap_378}


def vcl_base_universe_d3_027_vcl_055_earnings_yield_spike_756(vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756):
    return _base_universe_d3(vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756, 27)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_027_vcl_055_earnings_yield_spike_756'] = {'inputs': ['vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756'], 'func': vcl_base_universe_d3_027_vcl_055_earnings_yield_spike_756}


def vcl_base_universe_d3_028_vcl_056_valuation_history_depth_1008(vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008):
    return _base_universe_d3(vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008, 28)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_028_vcl_056_valuation_history_depth_1008'] = {'inputs': ['vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008'], 'func': vcl_base_universe_d3_028_vcl_056_valuation_history_depth_1008}


def vcl_base_universe_d3_029_vcl_061_ev_marketcap_gap_21(vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21):
    return _base_universe_d3(vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21, 29)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_029_vcl_061_ev_marketcap_gap_21'] = {'inputs': ['vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21'], 'func': vcl_base_universe_d3_029_vcl_061_ev_marketcap_gap_21}


def vcl_base_universe_d3_030_vcl_064_valuation_history_depth_84(vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84):
    return _base_universe_d3(vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84, 30)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_030_vcl_064_valuation_history_depth_84'] = {'inputs': ['vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84'], 'func': vcl_base_universe_d3_030_vcl_064_valuation_history_depth_84}


def vcl_base_universe_d3_031_vcl_067_ps_compression_z_252(vcl_base_universe_d2_031_vcl_067_ps_compression_z_252):
    return _base_universe_d3(vcl_base_universe_d2_031_vcl_067_ps_compression_z_252, 31)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_031_vcl_067_ps_compression_z_252'] = {'inputs': ['vcl_base_universe_d2_031_vcl_067_ps_compression_z_252'], 'func': vcl_base_universe_d3_031_vcl_067_ps_compression_z_252}


def vcl_base_universe_d3_032_vcl_069_ev_marketcap_gap_504(vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504):
    return _base_universe_d3(vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504, 32)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_032_vcl_069_ev_marketcap_gap_504'] = {'inputs': ['vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504'], 'func': vcl_base_universe_d3_032_vcl_069_ev_marketcap_gap_504}


def vcl_base_universe_d3_033_vcl_071_earnings_yield_spike_1008(vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008):
    return _base_universe_d3(vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008, 33)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_033_vcl_071_earnings_yield_spike_1008'] = {'inputs': ['vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008'], 'func': vcl_base_universe_d3_033_vcl_071_earnings_yield_spike_1008}


def vcl_base_universe_d3_034_vcl_072_valuation_history_depth_1260(vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260):
    return _base_universe_d3(vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260, 34)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_034_vcl_072_valuation_history_depth_1260'] = {'inputs': ['vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260'], 'func': vcl_base_universe_d3_034_vcl_072_valuation_history_depth_1260}


def vcl_base_universe_d3_035_vcl_basefill_004(vcl_base_universe_d2_035_vcl_basefill_004):
    return _base_universe_d3(vcl_base_universe_d2_035_vcl_basefill_004, 35)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_035_vcl_basefill_004'] = {'inputs': ['vcl_base_universe_d2_035_vcl_basefill_004'], 'func': vcl_base_universe_d3_035_vcl_basefill_004}


def vcl_base_universe_d3_036_vcl_basefill_012(vcl_base_universe_d2_036_vcl_basefill_012):
    return _base_universe_d3(vcl_base_universe_d2_036_vcl_basefill_012, 36)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_036_vcl_basefill_012'] = {'inputs': ['vcl_base_universe_d2_036_vcl_basefill_012'], 'func': vcl_base_universe_d3_036_vcl_basefill_012}


def vcl_base_universe_d3_037_vcl_basefill_015(vcl_base_universe_d2_037_vcl_basefill_015):
    return _base_universe_d3(vcl_base_universe_d2_037_vcl_basefill_015, 37)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_037_vcl_basefill_015'] = {'inputs': ['vcl_base_universe_d2_037_vcl_basefill_015'], 'func': vcl_base_universe_d3_037_vcl_basefill_015}


def vcl_base_universe_d3_038_vcl_basefill_017(vcl_base_universe_d2_038_vcl_basefill_017):
    return _base_universe_d3(vcl_base_universe_d2_038_vcl_basefill_017, 38)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_038_vcl_basefill_017'] = {'inputs': ['vcl_base_universe_d2_038_vcl_basefill_017'], 'func': vcl_base_universe_d3_038_vcl_basefill_017}


def vcl_base_universe_d3_039_vcl_basefill_018(vcl_base_universe_d2_039_vcl_basefill_018):
    return _base_universe_d3(vcl_base_universe_d2_039_vcl_basefill_018, 39)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_039_vcl_basefill_018'] = {'inputs': ['vcl_base_universe_d2_039_vcl_basefill_018'], 'func': vcl_base_universe_d3_039_vcl_basefill_018}


def vcl_base_universe_d3_040_vcl_basefill_020(vcl_base_universe_d2_040_vcl_basefill_020):
    return _base_universe_d3(vcl_base_universe_d2_040_vcl_basefill_020, 40)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_040_vcl_basefill_020'] = {'inputs': ['vcl_base_universe_d2_040_vcl_basefill_020'], 'func': vcl_base_universe_d3_040_vcl_basefill_020}


def vcl_base_universe_d3_041_vcl_basefill_022(vcl_base_universe_d2_041_vcl_basefill_022):
    return _base_universe_d3(vcl_base_universe_d2_041_vcl_basefill_022, 41)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_041_vcl_basefill_022'] = {'inputs': ['vcl_base_universe_d2_041_vcl_basefill_022'], 'func': vcl_base_universe_d3_041_vcl_basefill_022}


def vcl_base_universe_d3_042_vcl_basefill_025(vcl_base_universe_d2_042_vcl_basefill_025):
    return _base_universe_d3(vcl_base_universe_d2_042_vcl_basefill_025, 42)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_042_vcl_basefill_025'] = {'inputs': ['vcl_base_universe_d2_042_vcl_basefill_025'], 'func': vcl_base_universe_d3_042_vcl_basefill_025}


def vcl_base_universe_d3_043_vcl_basefill_026(vcl_base_universe_d2_043_vcl_basefill_026):
    return _base_universe_d3(vcl_base_universe_d2_043_vcl_basefill_026, 43)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_043_vcl_basefill_026'] = {'inputs': ['vcl_base_universe_d2_043_vcl_basefill_026'], 'func': vcl_base_universe_d3_043_vcl_basefill_026}


def vcl_base_universe_d3_044_vcl_basefill_028(vcl_base_universe_d2_044_vcl_basefill_028):
    return _base_universe_d3(vcl_base_universe_d2_044_vcl_basefill_028, 44)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_044_vcl_basefill_028'] = {'inputs': ['vcl_base_universe_d2_044_vcl_basefill_028'], 'func': vcl_base_universe_d3_044_vcl_basefill_028}


def vcl_base_universe_d3_045_vcl_basefill_030(vcl_base_universe_d2_045_vcl_basefill_030):
    return _base_universe_d3(vcl_base_universe_d2_045_vcl_basefill_030, 45)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_045_vcl_basefill_030'] = {'inputs': ['vcl_base_universe_d2_045_vcl_basefill_030'], 'func': vcl_base_universe_d3_045_vcl_basefill_030}


def vcl_base_universe_d3_046_vcl_basefill_033(vcl_base_universe_d2_046_vcl_basefill_033):
    return _base_universe_d3(vcl_base_universe_d2_046_vcl_basefill_033, 46)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_046_vcl_basefill_033'] = {'inputs': ['vcl_base_universe_d2_046_vcl_basefill_033'], 'func': vcl_base_universe_d3_046_vcl_basefill_033}


def vcl_base_universe_d3_047_vcl_basefill_034(vcl_base_universe_d2_047_vcl_basefill_034):
    return _base_universe_d3(vcl_base_universe_d2_047_vcl_basefill_034, 47)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_047_vcl_basefill_034'] = {'inputs': ['vcl_base_universe_d2_047_vcl_basefill_034'], 'func': vcl_base_universe_d3_047_vcl_basefill_034}


def vcl_base_universe_d3_048_vcl_basefill_036(vcl_base_universe_d2_048_vcl_basefill_036):
    return _base_universe_d3(vcl_base_universe_d2_048_vcl_basefill_036, 48)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_048_vcl_basefill_036'] = {'inputs': ['vcl_base_universe_d2_048_vcl_basefill_036'], 'func': vcl_base_universe_d3_048_vcl_basefill_036}


def vcl_base_universe_d3_049_vcl_basefill_038(vcl_base_universe_d2_049_vcl_basefill_038):
    return _base_universe_d3(vcl_base_universe_d2_049_vcl_basefill_038, 49)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_049_vcl_basefill_038'] = {'inputs': ['vcl_base_universe_d2_049_vcl_basefill_038'], 'func': vcl_base_universe_d3_049_vcl_basefill_038}


def vcl_base_universe_d3_050_vcl_basefill_041(vcl_base_universe_d2_050_vcl_basefill_041):
    return _base_universe_d3(vcl_base_universe_d2_050_vcl_basefill_041, 50)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_050_vcl_basefill_041'] = {'inputs': ['vcl_base_universe_d2_050_vcl_basefill_041'], 'func': vcl_base_universe_d3_050_vcl_basefill_041}


def vcl_base_universe_d3_051_vcl_basefill_042(vcl_base_universe_d2_051_vcl_basefill_042):
    return _base_universe_d3(vcl_base_universe_d2_051_vcl_basefill_042, 51)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_051_vcl_basefill_042'] = {'inputs': ['vcl_base_universe_d2_051_vcl_basefill_042'], 'func': vcl_base_universe_d3_051_vcl_basefill_042}


def vcl_base_universe_d3_052_vcl_basefill_044(vcl_base_universe_d2_052_vcl_basefill_044):
    return _base_universe_d3(vcl_base_universe_d2_052_vcl_basefill_044, 52)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_052_vcl_basefill_044'] = {'inputs': ['vcl_base_universe_d2_052_vcl_basefill_044'], 'func': vcl_base_universe_d3_052_vcl_basefill_044}


def vcl_base_universe_d3_053_vcl_basefill_045(vcl_base_universe_d2_053_vcl_basefill_045):
    return _base_universe_d3(vcl_base_universe_d2_053_vcl_basefill_045, 53)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_053_vcl_basefill_045'] = {'inputs': ['vcl_base_universe_d2_053_vcl_basefill_045'], 'func': vcl_base_universe_d3_053_vcl_basefill_045}


def vcl_base_universe_d3_054_vcl_basefill_046(vcl_base_universe_d2_054_vcl_basefill_046):
    return _base_universe_d3(vcl_base_universe_d2_054_vcl_basefill_046, 54)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_054_vcl_basefill_046'] = {'inputs': ['vcl_base_universe_d2_054_vcl_basefill_046'], 'func': vcl_base_universe_d3_054_vcl_basefill_046}


def vcl_base_universe_d3_055_vcl_basefill_049(vcl_base_universe_d2_055_vcl_basefill_049):
    return _base_universe_d3(vcl_base_universe_d2_055_vcl_basefill_049, 55)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_055_vcl_basefill_049'] = {'inputs': ['vcl_base_universe_d2_055_vcl_basefill_049'], 'func': vcl_base_universe_d3_055_vcl_basefill_049}


def vcl_base_universe_d3_056_vcl_basefill_050(vcl_base_universe_d2_056_vcl_basefill_050):
    return _base_universe_d3(vcl_base_universe_d2_056_vcl_basefill_050, 56)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_056_vcl_basefill_050'] = {'inputs': ['vcl_base_universe_d2_056_vcl_basefill_050'], 'func': vcl_base_universe_d3_056_vcl_basefill_050}


def vcl_base_universe_d3_057_vcl_basefill_052(vcl_base_universe_d2_057_vcl_basefill_052):
    return _base_universe_d3(vcl_base_universe_d2_057_vcl_basefill_052, 57)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_057_vcl_basefill_052'] = {'inputs': ['vcl_base_universe_d2_057_vcl_basefill_052'], 'func': vcl_base_universe_d3_057_vcl_basefill_052}


def vcl_base_universe_d3_058_vcl_basefill_054(vcl_base_universe_d2_058_vcl_basefill_054):
    return _base_universe_d3(vcl_base_universe_d2_058_vcl_basefill_054, 58)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_058_vcl_basefill_054'] = {'inputs': ['vcl_base_universe_d2_058_vcl_basefill_054'], 'func': vcl_base_universe_d3_058_vcl_basefill_054}


def vcl_base_universe_d3_059_vcl_basefill_057(vcl_base_universe_d2_059_vcl_basefill_057):
    return _base_universe_d3(vcl_base_universe_d2_059_vcl_basefill_057, 59)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_059_vcl_basefill_057'] = {'inputs': ['vcl_base_universe_d2_059_vcl_basefill_057'], 'func': vcl_base_universe_d3_059_vcl_basefill_057}


def vcl_base_universe_d3_060_vcl_basefill_058(vcl_base_universe_d2_060_vcl_basefill_058):
    return _base_universe_d3(vcl_base_universe_d2_060_vcl_basefill_058, 60)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_060_vcl_basefill_058'] = {'inputs': ['vcl_base_universe_d2_060_vcl_basefill_058'], 'func': vcl_base_universe_d3_060_vcl_basefill_058}


def vcl_base_universe_d3_061_vcl_basefill_059(vcl_base_universe_d2_061_vcl_basefill_059):
    return _base_universe_d3(vcl_base_universe_d2_061_vcl_basefill_059, 61)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_061_vcl_basefill_059'] = {'inputs': ['vcl_base_universe_d2_061_vcl_basefill_059'], 'func': vcl_base_universe_d3_061_vcl_basefill_059}


def vcl_base_universe_d3_062_vcl_basefill_060(vcl_base_universe_d2_062_vcl_basefill_060):
    return _base_universe_d3(vcl_base_universe_d2_062_vcl_basefill_060, 62)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_062_vcl_basefill_060'] = {'inputs': ['vcl_base_universe_d2_062_vcl_basefill_060'], 'func': vcl_base_universe_d3_062_vcl_basefill_060}


def vcl_base_universe_d3_063_vcl_basefill_062(vcl_base_universe_d2_063_vcl_basefill_062):
    return _base_universe_d3(vcl_base_universe_d2_063_vcl_basefill_062, 63)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_063_vcl_basefill_062'] = {'inputs': ['vcl_base_universe_d2_063_vcl_basefill_062'], 'func': vcl_base_universe_d3_063_vcl_basefill_062}


def vcl_base_universe_d3_064_vcl_basefill_063(vcl_base_universe_d2_064_vcl_basefill_063):
    return _base_universe_d3(vcl_base_universe_d2_064_vcl_basefill_063, 64)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_064_vcl_basefill_063'] = {'inputs': ['vcl_base_universe_d2_064_vcl_basefill_063'], 'func': vcl_base_universe_d3_064_vcl_basefill_063}


def vcl_base_universe_d3_065_vcl_basefill_065(vcl_base_universe_d2_065_vcl_basefill_065):
    return _base_universe_d3(vcl_base_universe_d2_065_vcl_basefill_065, 65)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_065_vcl_basefill_065'] = {'inputs': ['vcl_base_universe_d2_065_vcl_basefill_065'], 'func': vcl_base_universe_d3_065_vcl_basefill_065}


def vcl_base_universe_d3_066_vcl_basefill_066(vcl_base_universe_d2_066_vcl_basefill_066):
    return _base_universe_d3(vcl_base_universe_d2_066_vcl_basefill_066, 66)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_066_vcl_basefill_066'] = {'inputs': ['vcl_base_universe_d2_066_vcl_basefill_066'], 'func': vcl_base_universe_d3_066_vcl_basefill_066}


def vcl_base_universe_d3_067_vcl_basefill_068(vcl_base_universe_d2_067_vcl_basefill_068):
    return _base_universe_d3(vcl_base_universe_d2_067_vcl_basefill_068, 67)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_067_vcl_basefill_068'] = {'inputs': ['vcl_base_universe_d2_067_vcl_basefill_068'], 'func': vcl_base_universe_d3_067_vcl_basefill_068}


def vcl_base_universe_d3_068_vcl_basefill_070(vcl_base_universe_d2_068_vcl_basefill_070):
    return _base_universe_d3(vcl_base_universe_d2_068_vcl_basefill_070, 68)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_068_vcl_basefill_070'] = {'inputs': ['vcl_base_universe_d2_068_vcl_basefill_070'], 'func': vcl_base_universe_d3_068_vcl_basefill_070}


def vcl_base_universe_d3_069_vcl_basefill_073(vcl_base_universe_d2_069_vcl_basefill_073):
    return _base_universe_d3(vcl_base_universe_d2_069_vcl_basefill_073, 69)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_069_vcl_basefill_073'] = {'inputs': ['vcl_base_universe_d2_069_vcl_basefill_073'], 'func': vcl_base_universe_d3_069_vcl_basefill_073}


def vcl_base_universe_d3_070_vcl_basefill_074(vcl_base_universe_d2_070_vcl_basefill_074):
    return _base_universe_d3(vcl_base_universe_d2_070_vcl_basefill_074, 70)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_070_vcl_basefill_074'] = {'inputs': ['vcl_base_universe_d2_070_vcl_basefill_074'], 'func': vcl_base_universe_d3_070_vcl_basefill_074}


def vcl_base_universe_d3_071_vcl_basefill_075(vcl_base_universe_d2_071_vcl_basefill_075):
    return _base_universe_d3(vcl_base_universe_d2_071_vcl_basefill_075, 71)
VCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcl_base_universe_d3_071_vcl_basefill_075'] = {'inputs': ['vcl_base_universe_d2_071_vcl_basefill_075'], 'func': vcl_base_universe_d3_071_vcl_basefill_075}
