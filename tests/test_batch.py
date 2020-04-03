from ost.helpers.settings import config_check


# Test burst batch for all slc ARD types
# [OST-GTC, OST-RTC, OST-minimal]
def test_burst_batch(slc_project_class):
    for ard_type in config_check['type']['choices']:
        slc_project_class.set_ard_type(ard_type)
        slc_project_class.bursts_to_ard(
            timeseries=False,
            timescan=False,
            mosaic=False,
            overwrite=False,
            cut_to_aoi=False,
        )


# Test GRDs to ARD kind of batch
def test_grds_to_ard(grd_project_class):
    for ard_type in config_check['type']['choices']:
        grd_project_class.set_ard_type(ard_type)
        grd_project_class.grds_to_ard(
            timeseries=False,
            timescan=False,
            mosaic=False,
            overwrite=False,
            cut_to_aoi=False
        )