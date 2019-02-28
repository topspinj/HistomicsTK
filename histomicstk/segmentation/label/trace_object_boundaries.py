import numpy as np
from skimage.measure import regionprops

def _remove_thin_colinear_spurs(px, py, eps_colinear_area=0):
    """Simplifies the given list of points by removing colinear spurs
    """

    keep = []  # indices of points to keep

    anchor = -1
    testpos = 0

    while testpos < len(px):

        # get coords of next triplet of points to test
        if testpos == len(px) - 1:
            if not len(keep):
                break
            nextpos = keep[0]
        else:
            nextpos = testpos + 1

        ind = [anchor, testpos, nextpos]
        x1, x2, x3 = px[ind]
        y1, y2, y3 = py[ind]

        # compute area of triangle formed by triplet
        area = 0.5 * np.linalg.det(
            np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]])
        )

        # if area > cutoff, add testpos to keep and move anchor to testpos
        if abs(area) > eps_colinear_area:

            keep.append(testpos)  # add testpos to keep list
            anchor = testpos      # make testpos the next anchor point
            testpos += 1

        else:

            testpos += 1

    px = px[keep]
    py = py[keep]

    return px, py
