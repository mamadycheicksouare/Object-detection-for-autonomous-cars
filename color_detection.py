import cv2


def detect_traffic_light_color(image, bbox):
    """
    Detect the color of the traffic light within a bounding box.

    Parameters:
    - image: The input image in which to detect the traffic light.
    - bbox: The bounding box (xmin, ymin, xmax, ymax) that defines the region of interest.

    Returns:
    - 0 if red light is detected
    - 1 if green light is detected
    - -1 if no red or green light is detected
    """
    xmin, ymin, xmax, ymax = bbox
    roi = image[ymin:ymax, xmin:xmax]

    # Convert ROI to HSV color space
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)



    lower_red1 = (5, 115, 205)
    upper_red1 = (25, 215, 255)

    lower_green = (26, 25, 179)
    upper_green = (42, 125, 254)

    # Create masks for red color
    mask_red1 = cv2.inRange(hsv_roi, lower_red1, upper_red1)

    # Create mask for green color
    mask_green = cv2.inRange(hsv_roi, lower_green, upper_green)

    # Calculate the bounding box area
    bbox_area = (xmax - xmin) * (ymax - ymin)

    # Calculate the minimum area for detection (5% of the bbox area)
    min_light_area = 0.05 * bbox_area

    # Check for color presence
    red_area = cv2.countNonZero(mask_red1)
    green_area = cv2.countNonZero(mask_green)

    red_detected = red_area > min_light_area
    green_detected = green_area > min_light_area

    if red_detected:
        return 0
    elif green_detected:
        return 1
    else:
        return -1


def get_largest_bbox(bboxes):
    """
    Find the index of the bounding box with the largest area from a list of bounding boxes.

    Parameters:
    - bboxes: A list of bounding boxes, each defined as a tuple (xmin, ymin, xmax, ymax).

    Returns:
    - The index of the bounding box with the largest area.
    """
    if not bboxes:
        return None

    largest_index = 0
    largest_area = (bboxes[0][2] - bboxes[0][0]) * (bboxes[0][3] - bboxes[0][1])

    for i in range(0, len(bboxes)):
        area = (bboxes[i][2] - bboxes[i][0]) * (bboxes[i][3] - bboxes[i][1])
        if area > largest_area:
            largest_area = area
            largest_index = i

    return largest_index
