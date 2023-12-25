# DTArrowDirectionEstimator
A Distance-transform based arrow direction estimator

In traditional arrow direction estimators, it is difficult for single algorithms to estimate arrows with both 7 and 9 sides. This arrow direction estimator based on distance-transform methods provides a robust arrow direction estimator.

This is one of the research output of **System Design Project 2022-2023** (Group 13), School of Informatics, The University of Edinburgh.

The algorithm performs the best when the arrow image is tightly bounded with the image frame (as we customise this algorithm with yoloV5 detected arrows with a bounding box).

# Requirements

OpenCV, numpy

# Usage

python3 detect.py <image_filename>

# Example Results

![image](https://github.com/LawrenceZ22/DTArrowDirectionEstimator/blob/main/example_results/example_result_1.png)

![image](https://github.com/LawrenceZ22/DTArrowDirectionEstimator/blob/main/example_results/example_result_2.png)

![image](https://github.com/LawrenceZ22/DTArrowDirectionEstimator/blob/main/example_results/example_result_4.png)

Even worked in some extreme cases!

![image](https://github.com/LawrenceZ22/DTArrowDirectionEstimator/blob/main/example_results/example_result_3.png)
