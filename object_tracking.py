import cv2
import numpy as np
from object_detection import ObjectDetection
import math

# Initialize object detection
od = ObjectDetection()

cap = cv2.VideoCapture("los_angeles.mp4")

# Initialize frame count
count = 0

# Initialize center points of the objects
center_points_prev_frame = []

# Initialize tracking objects
tracking_objects = {}
track_id = 0

try:
  
  while True:
    ret, frame = cap.read()
    count += 1
    # Break the loop if there is no frame
    if not ret:
      break
    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    
    # Get center points of the detected objects
    center_points_cur_frame = []
    
    # Draw boxes on frame
    for box in boxes:
      x, y, w, h = box
      cx = (x + x + w) // 2
      cy = (y + y + h) // 2
      center_points_cur_frame.append((cx, cy))
      # print(f"Frame No. {count}'s Box: {x}, {y}, {w}, {h}")
      # cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
      
    # (Only at the beginning) Compare the center points of the current frame with the previous frame
    if count <= 2:
      for pt in center_points_cur_frame:
        for pt2 in center_points_prev_frame:
          # Calculate the distance between the points
          distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
          
          # If the distance is less than 20, then it is the same object
          if distance < 20:
            tracking_objects[track_id] = pt
            track_id += 1
            
    # Compare the center points of the current frame with the previous frame
    else:
      
      # Make a copy of the tracking objects and center points
      tracking_objects_copy = tracking_objects.copy()
      center_points_cur_frame_copy = center_points_cur_frame.copy()
      
      # loop through the tracking objects and center points copies
      for obj_id, pt in tracking_objects_copy.items():
        
        obj_exist = False # Check if the object still exists
        
        for pt2 in center_points_cur_frame_copy:
          # Calculate the distance between the points
          distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
          
          # Update the object's center point if the distance is less than 20
          if distance < 20:
            tracking_objects[obj_id] = pt # Update the object's center point
            obj_exist = True # The object exists
            if pt2 in center_points_cur_frame:
              center_points_cur_frame.remove(pt2) # Remove the point from the current frame
            continue
        
        # Delete the object if it does not exist
        if not obj_exist:
          tracking_objects.pop(obj_id)
    
      # Add the remaining points to the tracking objects
      for pt in center_points_cur_frame:
        tracking_objects[track_id] = pt
        track_id += 1

    for obj_id, pt in tracking_objects.items():
      cv2.circle(frame, pt, 5, (255, 0, 0), -1)
      cv2.putText(frame, f"{obj_id}", (pt[0], pt[1]-10), 0, 1, (255, 0, 0), 2)
          
    
    # print(f"Current Frame:\n{center_points_cur_frame},\nPrevious Frame:\n{center_points_prev_frame}")
      
    # Show frame
    cv2.imshow("Frame", frame)
    
    # Make a copy of the points
    center_points_prev_frame = center_points_cur_frame.copy()
  
    # Break the loop if the "Esc" key is pressed
    key = cv2.waitKey(1)
    if key == 27:
      break
    
except Exception as e:
  print("Error: ", e)