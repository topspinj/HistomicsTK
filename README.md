# HistomicsTK-Lite

HistomicsTK-Lite is a lightweight and limited version of [HistomicsTK](https://github.com/DigitalSlideArchive/HistomicsTK).

It contains the same functionality as the original HistomicsTK package with the exception of:

- Girder Client
- Dockerfile and Vagrant set-up
- Cython modules:
    - histomicstk.features._compute_marginal_glcm_probs_cython
    - histomicstk.segmentation.label._trace_object_boundaries_cython
    - histomicstk.segmentation.nuclear.max_clustering_cython
- Functions that depend on Cython modules:
    - histomicstk.features.compute_haralick_features
    - histomicstk.features.compute_nuclei_features (does not support haralick capabilities)
    - histomicstk.segmentation.label.trace_object_boundaries
    - histomicstk.segmentation.nuclear.max_clustering