frame_thresh_1 = 15
frame_thresh_2 = 10
frame_thresh_3 = 5

close_thresh = 0.3#(close_avg+open_avg)/2.0
flag = 0
yawn_countdown = 0
map_counter = 0
map_flag = 1

# print(close_thresh)

capture = cv2.VideoCapture(0)